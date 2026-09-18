# -*- coding: utf-8 -*-
"""
validate_batch.py — phase F du skill `patches-maillage-eco3min` : validation
programmatique d'un lot de patches DEPUIS LES FICHIERS JSON ÉCRITS, contre le
contenu source de l'export du mega.

Ce script est la référence exécutable du §7 (et rejoue les gates de la phase A
§1, de la phase B §2.2 à §2.5, du §3.1, §3.3, §3.5, §3.6, §3.7, §4 et §5).
Il ne remplace ni la relecture E (sens, F1→F8) ni le jugement : il garantit
qu'un patch livré passe le plugin ET respecte chaque règle mesurable.
Un lot dont il signale une ERREUR n'est pas livré.

Usage (depuis n'importe où) :

    python ~/.claude/skills/patches-maillage-eco3min/scripts/validate_batch.py \
        --patches patches-2026-09-18/ --export conseil_maillage_18_09.json

    --patches   un dossier (tous les *.json) ou un ou plusieurs fichiers.
    --export    l'export du mega (conseil `optimizations[]` ou « targets manual »
                `articles[]`). Sans lui, seuls les contrôles fichier + lot sont
                joués et le script le dit : ce n'est PAS une validation complète.
    --selftest  tests négatifs : mute des patches du lot et vérifie que chaque
                défaut est attrapé (à lancer après toute modification du script).

Import depuis un script de production :

    import sys, os
    sys.path.insert(0, os.path.expanduser('~/.claude/skills/patches-maillage-eco3min/scripts'))
    from validate_batch import validate, load_patches, load_export
    report = validate(load_patches(['patches-x-fr-001.json']), load_export('export.json'))
    assert not report.errors, report.render()

Sévérités :
    ERREUR  — bloquant, le lot ne part pas (§7 : « corrigé ou skippé — jamais livré »).
    ALERTE  — non bloquant, à reporter tel quel au rapport (densité §5, liens non
              listés par le conseil, entités brutes).

Décisions du 18/09/2026 (Paul) qui fixent deux règles jusque-là ambiguës :
    - cap 18 patches par cible : PAR FICHIER (« anti-explosion de fichier ») ;
      un lot peut en livrer davantage réparti sur plusieurs fichiers.
    - « ouverture répétée » (§4.2, §7) : les DEUX premiers mots du texte visible
      de l'insertion, casse et ponctuation ignorées ; un premier mot répété est
      toléré (« The », « A », « Une »), deux premiers mots identiques sur deux
      insertions de la même langue du lot = ERREUR.

Ce que ce script NE vérifie PAS (relecture E, humaine) : la pertinence du
bloc hôte, F1 hors lexique, F2 (interruption d'explication), F3 (antécédent
de l'anaphore), F4 faux-ami, F5 classe hors-domaine, l'honnêteté sémantique
de l'ancre §3.6, le pivot croisé §4.3, l'AMF §8 hors mots-clés évidents.
"""

import argparse
import collections
import glob
import io
import json
import os
import re
import sys

# ---------------------------------------------------------------------------
# Lexiques (copie fidèle du skill ; le skill fait foi, mettre à jour ici ET là)
# ---------------------------------------------------------------------------

# §3.1 — enrobages-pointeurs interdits (FR + EN), « ni leurs variantes proches »
FORBIDDEN_POINTERS = [
    r"voir aussi", r"voir également", r"à voir\b", r"\bvoir\s+<a", r"\bvoir l['’]",
    r"sur le même thème", r"dans le même registre", r"à rapprocher de",
    r"lecture connexe", r"lecture liée", r"sujet voisin", r"sujet connexe",
    r"en complément", r"pour aller plus loin", r"à lire aussi", r"\bconsulter\b",
    r"see also", r"\bsee\s+<a", r"on the same theme", r"related read(?:ing)?s?\b",
    r"a related angle", r"a neighbou?ring", r"in the same vein", r"further reading",
    r"refer to",
]
# §3.2.2 — verbes de renvoi interdits (texte visible, en tête de proposition)
REFERRAL_VERBS = r"\b(voir|consulter|consultez|see|refer to|cf\.)\b"
# §3.3 — sur-affirmation du contenu cible (lexique attesté, liste ouverte)
OVERCLAIM = [
    r"documente ce point", r"expose la méthode", r"\bdémontre\b",
    r"tous les chiffres sont posés", r"décompose cette dynamique",
    r"approfondit ce sujet", r"the full reading", r"laid out in", r"unpacked in",
    r"en tire les conséquences", r"prolonge cette lecture",
    r"\bdetailed in\b", r"\bdocumented in\b", r"\bdétaillée? dans\b",
]
# §8 — AMF, mots-clés prescriptifs évidents (le reste relève de la relecture)
AMF = r"\b(devrait|devraient|il faut|should|must buy|must sell|acheter maintenant|vendre maintenant)\b"
# §3.6 — élisions cassées (FR)
ELISION = re.compile(r"\b(de|à)\s+l(e|es)\b")
# §2.4 — anti-abréviation (même liste que outils/extract_anchors.py, avec frontière de mot)
ABBR = re.compile(
    r'(?<![A-Za-zÀ-ÿ])'
    r'(?:U\.S|e\.g|i\.e|etc|vs|No|Dr|St|cf|p\.ex|Mr|Mrs|Ms|Inc|Fig|al|approx'
    r'|Jr|Sr|Ave|Sq|min|max|art|ex|env)\.$', re.I)
CLOSING_INLINE = re.compile(r'^\s*</(strong|em|b|i|a|span|sup|sub|code|mark|u)\b')
NEW_SENTENCE = re.compile(r'^\s+[A-ZÀÂÉÈÊËÎÏÔÖÙÛÜÇ«"]')
DEMONSTRATIVE = re.compile(r'^(Ce|Cet|Cette|Ces|This|That|These|Those)\s+\w+')
ENTITY = re.compile(r'&(?:[a-zA-Z]+|#\d+|#x[0-9a-fA-F]+);')
SITE = 'https://eco3min.fr/'

# §5 — planchers de densité par famille (mots par lien) ou plafonds de liens
DENSITY_FLOOR = {
    'sub_pillar': 70, 'major_article': 70, 'deep_study': 70,
    'foundation_article': 90, 'case_study': 90, 'faq': 90, 'satellite': 90,
    'uncategorized': 90, 'beginner': 90,
}
LINK_CAP = {'tool': 10, 'dataset': 5, 'pillar': 30}   # pillar : note d'information seulement

MAX_PATCHES_PER_FILE = 20      # CLAUDE.md projet C
MAX_PER_TARGET_PER_FILE = 18   # §4, décision du 18/09/2026 : par fichier
MIN_BLOCK_INDEX = 2            # §2.5.5


# ---------------------------------------------------------------------------
# Chargement
# ---------------------------------------------------------------------------

class Patch(object):
    __slots__ = ('file', 'idx', 'post_id', 'anchor', 'insert', 'expected', 'comment', 'lang_hint')

    def __init__(self, file, idx, d):
        self.file = os.path.basename(file)
        self.idx = idx
        self.post_id = d.get('post_id')
        self.anchor = d.get('anchor_before', '') or ''
        self.insert = d.get('insert_after_anchor', '') or ''
        self.expected = d.get('expected_occurrences')
        self.comment = d.get('comment', '')
        m = re.search(r'-(fr|en)-\d+\.json$', self.file)
        self.lang_hint = m.group(1) if m else None

    @property
    def tag(self):
        return '%s#%d post %s' % (self.file, self.idx, self.post_id)

    @property
    def href(self):
        m = re.search(r'href="([^"]*)"', self.insert)
        return m.group(1) if m else ''

    @property
    def visible(self):
        return re.sub(r'<[^>]+>', '', self.insert).strip()

    @property
    def anchor_text(self):
        m = re.search(r'<a\b[^>]*>(.*?)</a>', self.insert, re.S)
        return re.sub(r'<[^>]+>', '', m.group(1)).strip() if m else ''


def load_patches(paths):
    """paths : dossier, fichier, ou liste. Retourne (patches, meta_par_fichier)."""
    if isinstance(paths, str):
        paths = [paths]
    files = []
    for p in paths:
        if os.path.isdir(p):
            files += sorted(glob.glob(os.path.join(p, '*.json')))
        else:
            files.append(p)
    patches, meta = [], {}
    for f in files:
        d = json.load(io.open(f, encoding='utf-8'))
        meta[os.path.basename(f)] = {k: d.get(k) for k in ('batch_id', 'generated_at', 'cluster')}
        for i, p in enumerate(d.get('patches') or []):
            patches.append(Patch(f, i, p))
    return patches, meta


def load_export(path):
    """Normalise conseil (`source_*`) et targets manual (`articles[]`)."""
    if not path:
        return None
    data = json.load(io.open(path, encoding='utf-8'))
    items = data.get('optimizations') or data.get('articles') or []
    src = {}
    for a in items:
        pid = a.get('source_post_id', a.get('post_id'))
        src[pid] = dict(
            post_id=pid,
            content=a.get('source_post_content', a.get('post_content', '')) or '',
            lang=a.get('source_lang', a.get('lang')),
            level=a.get('source_level', a.get('level')),
            url=a.get('source_url', a.get('url', '')) or '',
            words=a.get('source_word_count', a.get('word_count')),
            existing=a.get('source_existing_outgoing', a.get('outgoing_internal_links')),
            missing={_norm_url(m.get('target_url', '')): m for m in (a.get('missing_links') or [])},
        )
    return src


# ---------------------------------------------------------------------------
# Utilitaires
# ---------------------------------------------------------------------------

def _norm_url(u):
    u = (u or '').strip().replace('http://', 'https://')
    u = re.sub(r'^https://www\.', 'https://', u)
    return u.rstrip('/') + '/'


def forbidden_ranges(html):
    """Zones où une ancre est invalide pour le plugin : attributs, script/style,
    commentaires, shortcodes, <a> existants (§2.2)."""
    bad = []
    for pat in (r'<script\b.*?</script>', r'<style\b.*?</style>', r'<!--.*?-->',
                r'<a\b[^>]*>.*?</a>', r'\[[a-z0-9_]+[^\]]*\]'):
        for m in re.finditer(pat, html, re.S | re.I):
            bad.append((m.start(), m.end()))
    for m in re.finditer(r'<[^>]+>', html):      # tout tag = zone d'attributs
        bad.append((m.start(), m.end()))
    return bad


def _in_bad(a, b, bad):
    return any(x < b and a < y for x, y in bad)


def host_block(html, pos):
    """(start, end, index) du <p> qui contient pos ; index = rang du <p> dans le contenu."""
    starts = [m.start() for m in re.finditer(r'<p\b', html)]
    before = [s for s in starts if s <= pos]
    if not before:
        return None
    start = before[-1]
    end = html.find('</p>', pos)
    end = end if end != -1 else len(html)
    return start, end, len(before) - 1


def opening_key(visible, n):
    words = re.findall(r"[\w'’-]+", visible.lower())
    return ' '.join(words[:n])


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

class Report(object):
    def __init__(self):
        self.errors, self.alerts, self.info = [], [], []

    def err(self, where, rule, msg=''):
        self.errors.append((where, rule, msg))

    def alert(self, where, rule, msg=''):
        self.alerts.append((where, rule, msg))

    def render(self):
        out = []
        for lst, name in ((self.errors, 'ERREUR'), (self.alerts, 'ALERTE')):
            for where, rule, msg in lst:
                out.append('%-6s %s — %s%s' % (name, where, rule, (' : ' + msg) if msg else ''))
        out += self.info
        by_rule = collections.Counter(r for _, r, _ in self.errors)
        out.append('— %d erreur(s) %s, %d alerte(s).' % (
            len(self.errors), dict(by_rule) if by_rule else '', len(self.alerts)))
        return '\n'.join(out)


def validate(patches, src=None, meta=None):
    R = Report()
    if not patches:
        R.err('lot', 'aucun patch chargé')
        return R
    meta = meta or {}

    # ---- fichier : schéma et volumes ---------------------------------------
    per_file = collections.defaultdict(list)
    for p in patches:
        per_file[p.file].append(p)
    for f, ps in per_file.items():
        m = meta.get(f, {})
        if not m.get('batch_id') or not re.match(r'^[a-zA-Z0-9_-]+$', m['batch_id'] or ''):
            R.err(f, 'batch_id manquant ou invalide', repr(m.get('batch_id')))
        if len(ps) > MAX_PATCHES_PER_FILE:
            R.err(f, '> %d patches par fichier' % MAX_PATCHES_PER_FILE, str(len(ps)))
        tcount = collections.Counter(_norm_url(p.href) for p in ps if p.href)
        for u, k in tcount.items():
            if k > MAX_PER_TARGET_PER_FILE:
                R.err(f, 'over-target-cap (%d par cible et par fichier)' % MAX_PER_TARGET_PER_FILE, '%s ×%d' % (u, k))

    # ---- patch : contrôles sans export ------------------------------------
    lang_of = {}
    for p in patches:
        t = p.tag
        if not isinstance(p.post_id, int) or p.post_id < 1:
            R.err(t, 'post_id invalide', repr(p.post_id))
        if p.expected != 1:
            R.err(t, 'expected_occurrences != 1', repr(p.expected))
        L = len(p.anchor)
        if not (80 <= L <= 200):
            R.err(t, 'ancre hors 80-200', str(L))
        if re.search(r'<[^>]+>', p.anchor):
            R.err(t, 'balise HTML dans l\'ancre')
        if ENTITY.search(p.anchor):
            R.err(t, 'entité HTML dans l\'ancre', ENTITY.search(p.anchor).group(0))
        elif '&' in p.anchor:
            R.alert(t, '& brut dans l\'ancre (vérifier la forme stockée en base)')
        if p.anchor != p.anchor.strip():
            R.err(t, 'ancre avec espace de bord (slice non propre)')
        if p.anchor[-1:] not in '.!?»':
            R.err(t, 'ancre sans ponctuation finale (§2.4)', repr(p.anchor[-8:]))
        if ABBR.search(p.anchor):
            R.err(t, 'coupe sur abréviation (§2.4)', p.anchor[-12:])
        # insertion
        if not p.insert.startswith(' '):
            R.err(t, 'insertion sans espace initial (§3.5)')
        if len(re.findall(r'<a\b', p.insert)) != 1 or p.insert.count('</a>') != 1:
            R.err(t, '<a> non unique ou non équilibré (§3.5)')
        if re.search(r'<(?!/?a\b)[a-zA-Z]', p.insert):
            R.err(t, 'balise autre que <a> dans l\'insertion')
        h = p.href
        if not h.startswith(SITE):
            R.err(t, 'href absent ou non absolu eco3min.fr', h)
        vis = p.visible
        if not vis or vis[-1] not in '.!?»':
            R.err(t, 'insertion sans ponctuation finale (§3.5)', vis[-12:])
        if vis and not (vis[0].isupper() or vis[0] in '«"'):
            R.err(t, 'insertion sans majuscule en tête (§3.5)', vis[:20])
        if '  ' in vis:
            R.err(t, 'double espace dans l\'insertion (F7)')
        if re.search(r'\s[,.]', p.insert):   # « : » et « ; » précédés d'une espace sont du français correct
            R.err(t, 'espace avant virgule ou point (F7)')
        if not p.anchor_text:
            R.err(t, 'texte d\'ancre <a> vide')
        for pat in FORBIDDEN_POINTERS:
            if re.search(pat, p.insert, re.I):
                R.err(t, 'enrobage-pointeur interdit (§3.1)', pat)
                break
        if re.search(REFERRAL_VERBS, vis, re.I):
            R.err(t, 'verbe de renvoi (§3.2)', re.search(REFERRAL_VERBS, vis, re.I).group(0))
        for pat in OVERCLAIM:
            if re.search(pat, vis, re.I):
                R.err(t, 'sur-affirmation du contenu cible (§3.3 / F1)', pat)
                break
        if re.search(AMF, vis, re.I):
            R.err(t, 'formulation prescriptive (§8 AMF)', re.search(AMF, vis, re.I).group(0))
        # langue
        lang = None
        if src and p.post_id in src:
            lang = src[p.post_id]['lang']
        lang = lang or p.lang_hint or ('en' if h.startswith(SITE + 'en/') else 'fr')
        lang_of[p.tag] = lang
        href_en = h.startswith(SITE + 'en/')
        if (lang == 'fr' and href_en) or (lang == 'en' and not href_en and h):
            R.err(t, 'cross-langue (§1.3)', '%s → %s' % (lang, h))
        if lang == 'fr':
            if ELISION.search(vis):
                R.err(t, 'élision cassée de le / à les (§3.6)', ELISION.search(vis).group(0))
            if re.search(r"\bde (assurance|étude|analyse|économie|inflation|emploi)\b", vis):
                R.err(t, 'élision cassée « de » + voyelle (§3.6)')

    # ---- patch : contrôles contre le contenu source -----------------------
    block_used = collections.defaultdict(list)
    patches_per_source = collections.Counter()
    if src is None:
        R.info.append('INFO   export absent : contrôles occurrences, position, bloc hôte, doublon-cible, '
                      'self-link, densité NON joués. Validation incomplète.')
    else:
        for p in patches:
            t = p.tag
            s = src.get(p.post_id)
            if s is None:
                R.err(t, 'post_id absent de l\'export')
                continue
            html = s['content']
            patches_per_source[p.post_id] += 1
            n = html.count(p.anchor)
            if n != 1:
                R.err(t, 'occurrences != 1 dans le contenu source', str(n))
                continue
            pos = html.find(p.anchor)
            end = pos + len(p.anchor)
            if _in_bad(pos, end, forbidden_ranges(html)):
                R.err(t, 'ancre dans une zone interdite (attribut, <a>, script, commentaire, shortcode)')
            nxt = html[end:end + 240]
            if CLOSING_INLINE.match(nxt):
                R.err(t, 'fermante inline après l\'ancre (§2.4)', nxt[:16])
            if not (NEW_SENTENCE.match(nxt) or re.match(r'^\s*<', nxt) or not nxt.strip()):
                R.err(t, 'ce qui suit l\'ancre ne démarre pas une phrase (§2.4)', repr(nxt[:30]))
            hb = host_block(html, pos)
            if hb is None:
                R.err(t, 'ancre hors de tout <p>')
            else:
                bstart, bend, bidx = hb
                block = html[bstart:bend]
                rest = html[end:bend]
                ms = re.search(r'[.!?»](?=\s|<|$)', rest)
                next_sentence = rest[:ms.end()] if ms else rest
                if re.search(r'<a\b', next_sentence):
                    R.err(t, 'anti-empilement : <a> dans la phrase qui suit l\'ancre (§2.5.4)')
                nl = len(re.findall(r'<a\b', block))
                words = len(re.findall(r'\w+', re.sub(r'<[^>]+>', '', block)))
                if nl > 2 and not (nl == 3 and words >= 80):
                    R.err(t, 'gate paragraphe gradué (§2.5.3)', '%d liens, %d mots' % (nl, words))
                h = _norm_url(p.href)
                ml = s['missing'].get(h)
                tlevel = (ml or {}).get('target_level')
                if bidx < MIN_BLOCK_INDEX and tlevel != 'pillar':
                    R.err(t, 'dans les 2 premiers paragraphes hors pilier parent (§2.5.5)',
                          'p#%d, target_level=%s' % (bidx, tlevel))
                block_used[(p.post_id, bstart)].append(t)
                if ml is None and s['missing']:
                    R.alert(t, 'cible non listée dans missing_links du conseil', h)
            # doublon-cible / self-link (§1.1, §1.2) — href EXACT (une URL de pilier
            # est le préfixe de ses sous-piliers : jamais de test par sous-chaîne)
            h = _norm_url(p.href)
            existing = {_norm_url(u) for u in re.findall(r'href="([^"]+)"', html)}
            if h in existing:
                R.err(t, 'doublon-cible : la source lie déjà cette URL (§1.2)', h)
            if s['url'] and h == _norm_url(s['url']):
                R.err(t, 'self-link (§1.1)', h)
            if p.lang_hint and s['lang'] and p.lang_hint != s['lang']:
                R.err(t, 'fichier -%s- mais source %s' % (p.lang_hint, s['lang']))
        for (pid, b), tags in block_used.items():
            if len(tags) > 1:
                R.err(' / '.join(tags), 'un bloc hôte reçoit plus d\'un patch du lot (§2.5, décision 18/09/2026)')
        # densité §5 — alerte, jamais un skip
        for pid, k in patches_per_source.items():
            s = src[pid]
            html = s['content']
            words = s['words'] or len(re.findall(r'\w+', re.sub(r'<[^>]+>', '', html)))
            links = len(re.findall(r'href="https?://eco3min\.fr', html)) + k
            lvl = s['level']
            if lvl in DENSITY_FLOOR:
                d = words / links if links else float('inf')
                if d < DENSITY_FLOOR[lvl]:
                    R.alert('post %s' % pid, 'densité §5', '%s, %d mots, %d liens après patch → %.1f mots/lien (plancher %d)'
                            % (lvl, words, links, d, DENSITY_FLOOR[lvl]))
            elif lvl in LINK_CAP and links > LINK_CAP[lvl]:
                R.alert('post %s' % pid, 'densité §5', '%s, %d liens sortants après patch (repère %d)' % (lvl, links, LINK_CAP[lvl]))

    # ---- lot : diversité par langue (§3.7, §4) -----------------------------
    by_lang = collections.defaultdict(list)
    for p in patches:
        by_lang[lang_of[p.tag]].append(p)
    for lang, ps in by_lang.items():
        # §4.1 unicité des textes d'ancre
        c = collections.Counter(p.anchor_text.lower() for p in ps if p.anchor_text)
        for a, k in c.items():
            if k > 1:
                R.err('lot [%s]' % lang, 'texte d\'ancre <a> dupliqué (§4.1)', '« %s » ×%d' % (a, k))
        # anchor_before dupliquée (même slice, deux patches)
        c2 = collections.Counter(p.anchor for p in ps)
        for a, k in c2.items():
            if k > 1:
                R.err('lot [%s]' % lang, 'anchor_before dupliquée', '« %s… » ×%d' % (a[:40], k))
        opens = [p.visible for p in ps]
        # §3.7.1 plafond démonstratif-sujet
        dem = [o for o in opens if DEMONSTRATIVE.match(o)]
        cap = int(len(ps) * 0.20) if len(ps) >= 5 else 0
        if len(dem) > cap:
            R.err('lot [%s]' % lang, 'plafond démonstratif-sujet (§3.7.1)', '%d/%d (cap %d)' % (len(dem), len(ps), cap))
        # §4.2 ouverture répétée = deux premiers mots identiques (décision 18/09/2026)
        c3 = collections.Counter(opening_key(o, 2) for o in opens)
        for k2, k in c3.items():
            if k > 1 and k2:
                R.err('lot [%s]' % lang, 'ouverture répétée, deux premiers mots identiques (§4.2)', '« %s » ×%d' % (k2, k))
        # §3.7.3 squelette (4 premiers mots) sur deux patches consécutifs, dans l'ordre des fichiers
        sk = [opening_key(o, 4) for o in opens]
        for i in range(1, len(sk)):
            if sk[i] and sk[i] == sk[i - 1]:
                R.err(ps[i].tag, 'squelette d\'ouverture répété sur patches consécutifs (§3.7.3)', sk[i])
        firsts = {opening_key(o, 1) for o in opens}
        if len(firsts) < min(5, len(ps)):
            R.err('lot [%s]' % lang, 'variété d\'ouverture insuffisante (§3.7.3)', '%d premiers mots distincts' % len(firsts))
        R.info.append('INFO   [%s] %d patches, %d ouvertures démonstratives (cap %d), %d premiers mots distincts.'
                      % (lang, len(ps), len(dem), cap, len(firsts)))
    return R


# ---------------------------------------------------------------------------
# Tests négatifs
# ---------------------------------------------------------------------------

def selftest(patches, src, meta):
    """Mute des patches réels et vérifie que chaque défaut est attrapé."""
    import copy
    base = validate(patches, src, meta)
    assert not base.errors, 'le lot de référence doit être propre avant le selftest :\n' + base.render()
    ok = 0
    cases = []
    p0 = [p for p in patches if src is None or p.post_id in src][0]

    def mut(name, fn, expect):
        ps = copy.deepcopy(patches)
        tgt = [p for p in ps if p.tag == p0.tag][0]
        fn(tgt, ps)
        r = validate(ps, src, meta)
        hit = any(expect in rule for _, rule, _ in r.errors)
        cases.append((name, hit))
        return hit

    def set_anchor(p, ps, a):
        p.anchor = a
    if src:  # sans export, une ancre retapée est indétectable par construction : seul le contenu source la révèle
        mut('ancre retapée (un caractère divergent)', lambda p, ps: set_anchor(p, ps, p.anchor[:10] + ('X' if p.anchor[10] != 'X' else 'Y') + p.anchor[11:]),
            'occurrences != 1')
    mut('ancre trop courte', lambda p, ps: set_anchor(p, ps, p.anchor[:60]), 'hors 80-200')
    mut('balise dans l\'ancre', lambda p, ps: set_anchor(p, ps, '<em>' + p.anchor[4:]), 'balise HTML')
    mut('entité dans l\'ancre', lambda p, ps: set_anchor(p, ps, p.anchor[:-6] + '&nbsp;.'), 'entité')
    mut('coupe sur abréviation', lambda p, ps: set_anchor(p, ps, p.anchor[:-5] + ' U.S.'), 'abréviation')
    mut('see also', lambda p, ps: setattr(p, 'insert', ' See also ' + p.insert.strip() ), 'enrobage-pointeur')
    mut('voir aussi', lambda p, ps: setattr(p, 'insert', ' Voir aussi ' + p.insert.strip()), 'enrobage-pointeur')
    mut('sur-affirmation', lambda p, ps: setattr(p, 'insert', ' The mechanism is documented in ' + p.insert.strip()), 'sur-affirmation')
    mut('cross-langue', lambda p, ps: setattr(p, 'insert', p.insert.replace(SITE + 'en/', SITE) if SITE + 'en/' in p.insert else p.insert.replace(SITE, SITE + 'en/')), 'cross-langue')
    mut('deux <a>', lambda p, ps: setattr(p, 'insert', p.insert + ' <a href="https://eco3min.fr/x/">y</a>.'), '<a> non unique')
    mut('href relatif', lambda p, ps: setattr(p, 'insert', p.insert.replace(SITE, '/')), 'href absent ou non absolu')
    mut('sans espace initial', lambda p, ps: setattr(p, 'insert', p.insert.lstrip()), 'espace initial')
    mut('sans ponctuation finale', lambda p, ps: setattr(p, 'insert', p.insert.rstrip().rstrip('.!?»')), 'ponctuation finale')
    mut('prescriptif', lambda p, ps: setattr(p, 'insert', p.insert[:-1] + ', which investors should buy.'), 'prescriptive')
    mut('expected_occurrences 2', lambda p, ps: setattr(p, 'expected', 2), 'expected_occurrences')

    def dup_anchor_text(p, ps):
        other = [q for q in ps if q.tag != p.tag and lang_key(q) == lang_key(p)][0]
        p.insert = re.sub(r'<a\b[^>]*>.*?</a>', lambda m: m.group(0).split('>', 1)[0] + '>' + other.anchor_text + '</a>', p.insert, count=1, flags=re.S)
    mut('texte d\'ancre dupliqué', dup_anchor_text, 'dupliqué')

    def dup_opening(p, ps):
        other = [q for q in ps if q.tag != p.tag and lang_key(q) == lang_key(p)][0]
        w = re.findall(r"[\w'’-]+", other.visible)[:2]
        p.insert = ' ' + ' '.join(w) + ' ' + p.insert.strip()[0].lower() + p.insert.strip()[1:]
    mut('ouverture répétée (2 mots)', dup_opening, 'ouverture répétée')

    def too_many_demo(p, ps):
        same = [q for q in ps if lang_key(q) == lang_key(p)]
        for q in same[:max(1, int(len(same) * 0.2) + 1)]:
            q.insert = ' Cette ' + q.insert.strip()[0].lower() + q.insert.strip()[1:]
    mut('plafond démonstratif', too_many_demo, 'démonstratif')

    if src:
        s = src[p0.post_id]
        html = s['content']

        def closing_inline(p, ps):
            m = re.search(r'([^<>]{80,200}[.!?])(</(?:strong|em)>)', html)
            if m and html.count(m.group(1)) == 1:
                p.anchor = m.group(1)
            else:
                p.anchor = 'x' * 100  # pas de cas dans cette source → occurrences 0
        mut('fermante inline', closing_inline, 'fermante inline' if re.search(r'[^<>]{80,200}[.!?]</(?:strong|em)>', html) else 'occurrences')

        def doublon(p, ps):
            u = re.findall(r'href="(https://eco3min\.fr/[^"]+)"', html)
            p.insert = re.sub(r'href="[^"]*"', 'href="%s"' % (u[0] if u else SITE), p.insert, count=1)
        mut('doublon-cible exact', doublon, 'doublon-cible' if re.search(r'href="https://eco3min\.fr/', html) else 'cross-langue')

        def same_block(p, ps):
            q = copy.deepcopy(p)
            q.idx = 999
            q.insert = ' Another wording here for the test <a href="https://eco3min.fr/en/zzz-test/">a distinct anchor text</a>.'
            ps.append(q)
        mut('deux patches même bloc', same_block, 'plus d\'un patch')

        def intro(p, ps):
            m = re.search(r'<p\b[^>]*>([^<]{80,200}[.!?])', html)
            p.anchor = m.group(1) if m and html.count(m.group(1)) == 1 else p.anchor
            p.insert = re.sub(r'href="[^"]*"', 'href="https://eco3min.fr/en/zzz-not-a-pillar/"', p.insert, count=1)
        mut('2 premiers paragraphes hors pilier', intro, '2 premiers paragraphes')

    for name, hit in cases:
        print('  %s %s' % ('✅' if hit else '❌', name))
        ok += hit
    print('selftest : %d/%d défauts attrapés' % (ok, len(cases)))
    return ok == len(cases)


def lang_key(p):
    return p.lang_hint or ('en' if p.href.startswith(SITE + 'en/') else 'fr')


# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--patches', nargs='+', required=True, help='dossier du lot ou fichiers JSON')
    ap.add_argument('--export', help='export du mega (conseil ou targets manual)')
    ap.add_argument('--selftest', action='store_true', help='tests négatifs par mutation')
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
    patches, meta = load_patches(args.patches)
    src = load_export(args.export)
    if args.selftest:
        sys.exit(0 if selftest(patches, src, meta) else 1)
    R = validate(patches, src, meta)
    print(R.render())
    print('%d patches dans %d fichier(s), export %s.' % (
        len(patches), len(meta), 'chargé (%d sources)' % len(src) if src else 'ABSENT'))
    sys.exit(1 if R.errors else 0)


if __name__ == '__main__':
    main()

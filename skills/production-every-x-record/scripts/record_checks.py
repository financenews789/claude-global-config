# -*- coding: utf-8 -*-
"""Gardes bloquantes des pages « Every X since Y » (production-every-x-record).

Regroupe les contrôles que chaque production recopiait dans son validate.py, pour
qu'ils s'importent au lieu de se réécrire (et dériver) à chaque page :

- §4  bloc HTML sans commentaire, sans <script>, sans <h1>, sans JSON-LD, un seul <style> ;
- §4  CSS 100 % scopé : chaque sélecteur du <style> commence par le wrapper
      (at-rules @media / @supports déroulées, @font-face / @keyframes ignorées) ;
- §2.5 zéro cosplay d'autorité (« Cite this », DOI, « Abstract », share, click-to-copy,
      badges, ORCID / affiliation, capture email, logo de licence) ;
- Méthode anti-erreur : payloads base64 du snippet décodés et re-parsés (round-trip),
      FAQ du JSON-LD identique à la FAQ visible (paires h3/p), garde-fou par slug
      vérifié statiquement ET par simulation PHP avec stubs WordPress (émission sur
      chaque slug du bundle, silence sur un slug tiers), `node --check` du JS,
      cohérence des chiffres-clés entre livrables.

Import depuis un dossier de production :

    import os, sys
    sys.path.insert(0, os.path.expanduser('~/.claude/skills/production-every-x-record/scripts'))
    from record_checks import run_all

    fails = run_all(
        html={'en': html_en, 'fr': html_fr},        # contenu des blocs Custom HTML (str)
        php=snippet_php,                            # code du snippet Code Snippets (str)
        wrapper='.e3m-bankfail',                    # classe unique du wrapper
        slugs={'en': 'every-us-bank-failure-since-1934',
               'fr': 'toutes-les-faillites-bancaires-americaines-depuis-1934'},
        js_path='src/chart.js',                     # facultatif (les payloads JS du snippet
                                                    # passent node --check dans tous les cas)
        figures={'en': ['4,117', '2,499'], 'fr': ['4 117', '2 499']},   # facultatif
        extra_texts={'en': {'comment': comment_en}},                    # facultatif
    )
    assert not fails, fails

Chaque fonction renvoie une liste de défauts (vide = OK) ; `run_all` les agrège,
imprime une ligne OK / ECHEC par contrôle et renvoie la liste complète.

En ligne de commande (depuis le dossier de la production) :

    py -3.14 ~/.claude/skills/production-every-x-record/scripts/record_checks.py \
        --wrapper .e3m-bankfail --php snippet.php \
        --html en=page_en.html fr=page_fr.html \
        --slug en=every-us-bank-failure-since-1934 fr=toutes-les-faillites-bancaires-americaines-depuis-1934 \
        [--js src/chart.js] [--figure en=4,117 --figure fr=4\\ 117]

Code de sortie 1 dès qu'un contrôle échoue.
"""
import argparse
import base64
import html as _html
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

COMMENT = re.compile(r'<!--.*?-->', re.S)
TAG = re.compile(r'<[^>]+>')
FOREIGN_SLUG = 'page-tierce-sans-rapport-e3m-test'


# ---------------------------------------------------------------------------
# utilitaires
# ---------------------------------------------------------------------------
def _norm(s):
    """Texte sans balises, entités décodées, blancs normalisés."""
    s = TAG.sub('', s or '')
    s = _html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()


def visible_text(html):
    """Texte visible d'un bloc HTML : sans <style>, sans balises. Les espaces insécables
    (U+00A0, U+202F, U+2009) sont CONSERVÉS : « 4 117 » et « 38,6 % » se grep-ent tels quels."""
    s = TAG.sub(' ', re.sub(r'<style\b.*?</style>', ' ', html, flags=re.S | re.I))
    s = _html.unescape(s)
    return re.sub(r'[ \t\r\n\f\v]+', ' ', s).strip()


def _lab(label):
    return (label + ' : ') if label else ''


# ---------------------------------------------------------------------------
# §4 — bloc HTML
# ---------------------------------------------------------------------------
def html_clean(html, label=''):
    """Bloc Custom HTML : markup + CSS uniquement (§4), zéro commentaire HTML (rappel bloquant)."""
    f, L = [], _lab(label)
    if COMMENT.search(html):
        f.append(L + 'commentaire HTML dans le contenu (Autoptimize / wpautop, incident du 27/08/2026)')
    if re.search(r'<script\b', html, re.I):
        f.append(L + '<script> dans le bloc HTML : le JS vit dans le snippet au wp_footer')
    if re.search(r'<h1\b', html, re.I):
        f.append(L + '<h1> dans le bloc HTML : Blocksy fournit le H1')
    if 'ld+json' in html:
        f.append(L + 'JSON-LD dans le contenu : il vit dans le snippet, en base64 par slug')
    n = len(re.findall(r'<style\b', html, re.I))
    if n > 1:
        f.append(L + '%d blocs <style> (attendu : un seul, en tête du wrapper)' % n)
    if re.search(r'<!--\s*VERIFY', html, re.I):
        f.append(L + 'marqueur <!-- VERIFY --> restant : fait hors-CSV non sourcé')
    return f


def css_selectors(css):
    """Liste des sélecteurs d'un CSS. @media / @supports / @container / @layer sont
    déroulés (leurs sélecteurs internes comptent) ; @font-face, @keyframes, @page,
    @import, @charset ne portent pas de sélecteur d'élément et sont ignorés."""
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    css = re.sub(r'@(import|charset|namespace)\b[^;{]*;', '', css)
    sels = []

    def walk(s):
        i = 0
        while True:
            j = s.find('{', i)
            if j < 0:
                return
            head = s[i:j].strip()
            depth, k = 1, j + 1
            while k < len(s) and depth:
                if s[k] == '{':
                    depth += 1
                elif s[k] == '}':
                    depth -= 1
                k += 1
            body = s[j + 1:k - 1]
            if head.startswith('@'):
                name = re.split(r'[\s(]', head, maxsplit=1)[0].lower()
                if name in ('@media', '@supports', '@container', '@layer', '@document'):
                    walk(body)
            else:
                sels.extend(x.strip() for x in head.split(',') if x.strip())
            i = k

    walk(css)
    return sels


def css_scoped(html_or_css, wrapper, label=''):
    """§4 BLOQUANT : chaque sélecteur commence par le wrapper (suivi d'un espace, d'un
    combinateur, d'une pseudo-classe ou de la fin). `body{}`, `*{}`, `p{}`, `.autre{}` → défaut."""
    m = re.search(r'<style\b[^>]*>(.*?)</style>', html_or_css, re.S | re.I)
    css = m.group(1) if m else html_or_css
    ok = re.compile(r'^' + re.escape(wrapper) + r'(?![\w-])')
    bad = [s for s in css_selectors(css) if not ok.match(s)]
    return [_lab(label) + 'sélecteur hors wrapper %s : `%s`' % (wrapper, s) for s in bad]


# ---------------------------------------------------------------------------
# §2.5 — cosplay d'autorité
# ---------------------------------------------------------------------------
COSPLAY = [
    (r'\bcite\s+this\b|\bhow\s+to\s+cite\b|\bciter\s+cette\s+(page|étude|etude)\b|\bcomment\s+citer\b',
     'bloc « Cite this » / « How to cite »'),
    (r'\bDOI\b|doi\.org/|\bbibtex\b', 'DOI / BibTeX'),
    (r'<h[2-6][^>]*>\s*(abstract|résumé\s+académique)\s*</h|class="[^"]*\babstract\b', 'cadre « Abstract »'),
    (r'\bworking\s+paper\b|\bdownload\s+the\s+paper\b|\bpdf\s+version\b|\bversion\s+pdf\b|\btélécharger\s+le\s+papier\b',
     '« Working paper » / « Download the paper » / PDF'),
    (r'>\s*share(\s+this(\s+research)?)?\s*<|>\s*partager\s*<|class="[^"]*\bshare', 'boutons Share'),
    (r'click[- ]to[- ]copy|\bcopy\s+(this\s+|the\s+)?(stat|phrase|quote|citation|link|sentence)\b|\bcopier\s+(la|cette)\s+(phrase|stat|citation)\b|data-copy|class="[^"]*\bcopy',
     'click-to-copy'),
    (r'>\s*(peer[- ]reviewed|open\s+research|public\s+dataset|verified|open\s+data|données\s+ouvertes)\s*<|class="[^"]*\b(badge|pill|seal|trust)',
     'badge / pill d\'autorité'),
    (r'\bORCID\b|about\s+the\s+(researcher|author)|à\s+propos\s+de\s+l.auteur|>\s*affiliation\s*<|class="[^"]*\b(author|affiliation)',
     'bloc auteur / affiliation'),
    (r'<input[^>]*type="email"|<form\b|>\s*subscribe\s*<|>\s*(s.abonner|abonnez-vous|s.inscrire)\s*<|class="[^"]*\bnewsletter',
     'capture email / newsletter'),
    (r'licensebuttons\.net|mirrors\.creativecommons\.org|i\.creativecommons\.org|class="[^"]*\bcc-(badge|logo|icon)',
     'logo de licence décoratif'),
    (r'\b\d[\d,\.\s]*\s+(views|citations|downloads|vues|téléchargements)\b', 'compteur de vues / citations'),
]


def cosplay_scan(html, label=''):
    """§2.5 : l'autorité se gagne par le contenu, jamais par des widgets. Renvoie les motifs trouvés."""
    f = []
    for pat, what in COSPLAY:
        hits = re.findall(pat, html, re.I)
        if hits:
            h = hits[0] if isinstance(hits[0], str) else ' '.join(x for x in hits[0] if x)
            f.append(_lab(label) + 'cosplay %s (« %s »)' % (what, _norm(h)[:60]))
    return f


# ---------------------------------------------------------------------------
# FAQ visible et JSON-LD
# ---------------------------------------------------------------------------
def faq_pairs(html):
    """Paires (question, réponse) de la FAQ visible : chaque <h3> et le <p> qui le suit."""
    out = []
    for m in re.finditer(r'<h3\b[^>]*>(.*?)</h3>\s*(?:<p\b[^>]*>(.*?)</p>)?', html, re.S | re.I):
        out.append((_norm(m.group(1)), _norm(m.group(2))))
    return out


def _jsonld_lang(obj):
    nodes = obj.get('@graph', [obj]) if isinstance(obj, dict) else []
    for n in nodes:
        if isinstance(n, dict) and n.get('inLanguage'):
            return str(n['inLanguage']).split('-')[0].lower()
    return None


def decode_payloads(php, min_len=200, expected_jsonld=None):
    """Tous les blobs base64 du snippet (chaînes PHP entre quotes simples), décodés en UTF-8
    strict et re-parsés. Renvoie (payloads, défauts) ; payload = dict(kind, raw, obj, lang)
    avec kind ∈ {'jsonld', 'json', 'js', 'text'}. expected_jsonld = nombre de JSON-LD
    attendus (un par slug) : un blob rendu illisible par un caractère hors alphabet
    n'est plus reconnu comme base64, le compte le rattrape."""
    payloads, fails = [], []
    for m in re.finditer(r"'([A-Za-z0-9+/=\s]{%d,})'" % min_len, php):
        b = re.sub(r'\s', '', m.group(1))
        try:
            raw = base64.b64decode(b, validate=True).decode('utf-8', 'strict')
        except Exception as e:  # noqa: BLE001
            fails.append('base64 indécodable (%s…) : %s' % (b[:24], e))
            continue
        p = {'raw': raw, 'kind': 'text', 'obj': None, 'lang': None}
        head = raw.lstrip()[:1]
        if head in '{[':
            try:
                p['obj'] = json.loads(raw)
                p['kind'] = 'json'
                if isinstance(p['obj'], dict) and ('@graph' in p['obj'] or '@context' in p['obj']):
                    p['kind'] = 'jsonld'
                    p['lang'] = _jsonld_lang(p['obj'])
            except Exception as e:  # noqa: BLE001
                fails.append('JSON invalide dans un payload base64 (%s…) : %s' % (raw[:40], e))
        elif re.search(r'\bfunction\b|=>|\bvar\b|\bconst\b|\blet\b', raw):
            p['kind'] = 'js'
        payloads.append(p)
    n_ld = sum(1 for p in payloads if p['kind'] == 'jsonld')
    if not n_ld:
        fails.append('aucun JSON-LD base64 dans le snippet (il doit y en avoir un par slug)')
    elif expected_jsonld is not None and n_ld != expected_jsonld:
        fails.append('%d JSON-LD base64 décodés, %d attendus (un par slug) : blob absent ou illisible'
                     % (n_ld, expected_jsonld))
    return payloads, fails


def faq_matches_jsonld(html_by_lang, payloads):
    """La FAQ du JSON-LD (FAQPage.mainEntity) doit être IDENTIQUE à la FAQ visible :
    mêmes questions dans le même ordre, mêmes réponses (texte normalisé)."""
    fails, seen = [], set()
    for p in payloads:
        if p['kind'] != 'jsonld':
            continue
        lang = p['lang']
        g = p['obj'].get('@graph', [p['obj']])
        if lang not in html_by_lang:
            fails.append('JSON-LD inLanguage=%r sans page correspondante' % lang)
            continue
        seen.add(lang)
        faq = [n for n in g if isinstance(n, dict) and n.get('@type') == 'FAQPage']
        if not faq:
            fails.append('%s : pas de FAQPage dans le JSON-LD' % lang)
            continue
        qa = [(_norm(q.get('name')), _norm((q.get('acceptedAnswer') or {}).get('text')))
              for q in faq[0].get('mainEntity', [])]
        vis = faq_pairs(html_by_lang[lang])
        if [q for q, _ in qa] != [q for q, _ in vis]:
            fails.append('%s : questions FAQ JSON-LD ≠ FAQ visible (%d vs %d) ; JSON-LD=%s ; visible=%s'
                         % (lang, len(qa), len(vis), [q[:40] for q, _ in qa], [q[:40] for q, _ in vis]))
            continue
        for (q, a), (_, av) in zip(qa, vis):
            if a != av:
                fails.append('%s : réponse FAQ différente pour « %s »' % (lang, q[:60]))
    for lang in html_by_lang:
        if lang not in seen:
            fails.append('%s : aucun JSON-LD de cette langue dans le snippet' % lang)
    return fails


# ---------------------------------------------------------------------------
# snippet PHP : garde-fou par slug
# ---------------------------------------------------------------------------
def snippet_static(php, slugs):
    """Motif canonique (eco3min-import-contenu-bilingue) : pas de <?php de tête, garde par
    is_singular('page') + get_queried_object() instanceof WP_Post + map par post_name,
    appelée en tête de CHAQUE hook, aucune lib cdnjs ni <script src>."""
    f = []
    norm = re.sub(r'\s+', ' ', php)
    if php.lstrip().startswith('<?php'):
        f.append('le code commence par <?php (Code Snippets l\'ajoute lui-même)')
    if 'cdnjs' in php:
        f.append('lib cdnjs (bloquée par la CSP)')
    if re.search(r'<script[^>]+src\s*=', php, re.I):
        f.append('<script src=…> : le chart interactif est du canvas vanilla, aucune lib')
    if not re.search(r"is_singular\(\s*['\"]page['\"]\s*\)", norm):
        f.append('garde-fou : is_singular(\'page\') absent')
    if 'instanceof WP_Post' not in norm:
        f.append('garde-fou : test `instanceof WP_Post` absent')
    if 'post_name' not in norm:
        f.append('garde-fou : map par post_name absente')
    for lang, slug in slugs.items():
        if slug not in php:
            f.append('slug %s « %s » absent du snippet' % (lang, slug))
    m = re.search(r'function\s+(\w+)\s*\(\s*\)\s*\{[^}]*is_singular', norm)
    fn = m.group(1) if m else None
    hooks = re.findall(r"add_action\(\s*['\"](\w+)['\"]", norm)
    for h in ('wp_head', 'wp_footer'):
        if h not in hooks:
            f.append('hook %s absent (JSON-LD au wp_head, chart au wp_footer)' % h)
    if fn:
        for seg in re.split(r"add_action\(\s*['\"]\w+['\"]", norm)[1:]:
            if fn + '()' not in seg[:400] or 'return;' not in seg[:600]:
                f.append('un hook n\'appelle pas %s() en tête avec return : garde-fou manquant' % fn)
                break
    else:
        f.append('aucune fonction de garde factorisée (function xxx(){ … is_singular … }) trouvée')
    return f


_HARNESS = r'''<?php
$__E3M = array('hooks' => array(), 'slug' => '');
class WP_Post { public $post_name; public $post_type = 'page'; public $ID = 1;
  function __construct($s) { $this->post_name = $s; } }
function add_action($h, $cb, $p = 10, $a = 1) { global $__E3M; $__E3M['hooks'][$h][] = $cb; }
function add_filter($h, $cb, $p = 10, $a = 1) { add_action($h, $cb, $p, $a); }
function add_shortcode($t, $cb) {}
function is_singular($t = '') { global $__E3M; return $__E3M['slug'] !== '' && ($t === '' || $t === 'page' || (is_array($t) && in_array('page', $t))); }
function is_page($x = '') { return is_singular('page'); }
function get_queried_object() { global $__E3M; return $__E3M['slug'] === '' ? null : new WP_Post($__E3M['slug']); }
function get_post() { return get_queried_object(); }
function get_queried_object_id() { return 1; }
function esc_attr($s) { return $s; } function esc_html($s) { return $s; } function esc_url($s) { return $s; }
function esc_js($s) { return $s; } function wp_json_encode($x) { return json_encode($x); }
function home_url($p = '') { return 'https://eco3min.fr' . $p; }
require $argv[2];
$out = array();
foreach (explode(',', $argv[1]) as $slug) {
  $__E3M['slug'] = $slug;
  foreach ($__E3M['hooks'] as $h => $cbs) {
    ob_start();
    foreach ($cbs as $cb) { call_user_func($cb); }
    $out[$slug][$h] = strlen(ob_get_clean());
  }
}
echo json_encode($out);
'''


def php_simulate(php, slugs, foreign=FOREIGN_SLUG):
    """`php -l` puis exécution du snippet avec des stubs WP minimaux : chaque hook doit
    émettre sur chaque slug du bundle et rester MUET sur un slug tiers (anti-fuite)."""
    exe = shutil.which('php')
    if not exe:
        return ['php introuvable : simulation impossible (faire php -l + stubs ailleurs avant livraison)']
    d = tempfile.mkdtemp(prefix='e3m-record-')
    try:
        snip = os.path.join(d, 'snippet.php')
        harn = os.path.join(d, 'harness.php')
        io.open(snip, 'w', encoding='utf-8', newline='\n').write('<?php\n' + php)
        io.open(harn, 'w', encoding='utf-8', newline='\n').write(_HARNESS)
        r = subprocess.run([exe, '-l', snip], capture_output=True)
        if r.returncode != 0:
            return ['php -l : ' + (r.stdout + r.stderr).decode('utf-8', 'replace')[:400]]
        all_slugs = list(slugs.values()) + [foreign]
        r = subprocess.run([exe, harn, ','.join(all_slugs), snip], capture_output=True)
        if r.returncode != 0:
            return ['simulation PHP : ' + (r.stdout + r.stderr).decode('utf-8', 'replace')[:400]]
        try:
            out = json.loads(r.stdout.decode('utf-8', 'replace').strip().splitlines()[-1])
        except Exception as e:  # noqa: BLE001
            return ['simulation PHP : sortie illisible (%s) : %s' % (e, r.stdout[:200])]
        f = []
        for lang, slug in slugs.items():
            for h in ('wp_head', 'wp_footer'):
                if not out.get(slug, {}).get(h):
                    f.append('simulation : %s n\'émet rien sur le slug %s « %s »' % (h, lang, slug))
        for h, n in out.get(foreign, {}).items():
            if n:
                f.append('simulation : FUITE, %s émet %d octets sur un slug tiers' % (h, n))
        return f
    finally:
        shutil.rmtree(d, ignore_errors=True)


# ---------------------------------------------------------------------------
# JS et chiffres
# ---------------------------------------------------------------------------
def node_check(js, is_path=False, label=''):
    """`node --check` sur un fichier ou une chaîne JS."""
    exe = shutil.which('node')
    if not exe:
        return ['node introuvable : node --check impossible']
    d = None
    try:
        path = js
        if not is_path:
            d = tempfile.mkdtemp(prefix='e3m-js-')
            path = os.path.join(d, 'payload.js')
            io.open(path, 'w', encoding='utf-8', newline='\n').write(js)
        r = subprocess.run([exe, '--check', path], capture_output=True)
        if r.returncode == 0:
            return []
        return [_lab(label) + 'node --check : ' + r.stderr.decode('utf-8', 'replace').strip()[:300]]
    finally:
        if d:
            shutil.rmtree(d, ignore_errors=True)


def figures_present(texts, figures):
    """Chaque chiffre-clé doit apparaître tel quel dans chaque livrable narratif
    (bloc HTML, 1er commentaire, social…). texts = {label: texte}, figures = liste de
    chaînes au format de la langue, insécables compris (« 4 117 », « 38,6 % »).
    Le JSON-LD n'est pas un livrable narratif : il n'est pas soumis à ce contrôle."""
    f = []
    for fig in figures:
        miss = [k for k, t in texts.items() if fig not in t]
        if miss:
            f.append('chiffre « %s » absent de : %s' % (fig, ', '.join(miss)))
    return f


# ---------------------------------------------------------------------------
# tout
# ---------------------------------------------------------------------------
def run_all(html, php, wrapper, slugs, js_path=None, figures=None, extra_texts=None, quiet=False):
    """Enchaîne tous les contrôles. html = {lang: bloc HTML}, php = code du snippet,
    slugs = {lang: slug}, figures = liste (toutes langues) ou {lang: liste},
    extra_texts = {lang: {label: texte}} (commentaire Reddit, social…). Renvoie les défauts."""
    results = []

    def add(name, fails):
        results.append((name, fails))
        if not quiet:
            print(('  OK     ' if not fails else '  ECHEC  ') + name)
            for x in fails:
                print('           - ' + x)

    for lang, h in html.items():
        add('%s bloc HTML propre (sans commentaire / script / h1 / JSON-LD)' % lang, html_clean(h, lang))
        add('%s CSS 100 %% scopé sous %s' % (lang, wrapper), css_scoped(h, wrapper, lang))
        add('%s zéro cosplay d\'autorité' % lang, cosplay_scan(h, lang))
    add('snippet : motif de garde canonique', snippet_static(php, slugs))
    payloads, pf = decode_payloads(php, expected_jsonld=len(slugs))
    add('snippet : round-trip base64 (%d payloads : %s)' % (len(payloads), ', '.join(p['kind'] for p in payloads)), pf)
    add('FAQ JSON-LD = FAQ visible', faq_matches_jsonld(html, payloads))
    add('snippet : php -l + simulation (émet sur les slugs, muet ailleurs)', php_simulate(php, slugs))
    for i, p in enumerate(p for p in payloads if p['kind'] == 'js'):
        add('snippet : node --check du payload JS #%d' % (i + 1), node_check(p['raw']))
    if js_path:
        add('node --check %s' % os.path.basename(js_path), node_check(js_path, is_path=True))
    if figures:
        per_lang = figures if isinstance(figures, dict) else {l: figures for l in html}
        for lang, figs in per_lang.items():
            texts = {'html_' + lang: visible_text(html.get(lang, ''))}
            for k, t in ((extra_texts or {}).get(lang) or {}).items():
                texts[k] = t
            add('%s chiffres-clés identiques dans chaque livrable' % lang, figures_present(texts, figs))
    fails = [n + ' -> ' + x for n, fs in results for x in fs]
    if not quiet:
        print('\n' + ('TOUS LES CONTROLES PASSENT' if not fails else '%d CONTROLE(S) EN ECHEC' % len(fails)))
    return fails


def _kv(items):
    out = {}
    for it in items or []:
        k, v = it.split('=', 1)
        out[k] = v
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description='Gardes production-every-x-record')
    ap.add_argument('--wrapper', required=True)
    ap.add_argument('--php', required=True)
    ap.add_argument('--html', nargs='+', required=True, help='lang=fichier.html')
    ap.add_argument('--slug', nargs='+', required=True, help='lang=slug')
    ap.add_argument('--js')
    ap.add_argument('--figure', action='append', help='lang=chiffre (répétable)')
    a = ap.parse_args(argv)
    html = {l: io.open(p, encoding='utf-8').read() for l, p in _kv(a.html).items()}
    figures = {}
    for it in a.figure or []:
        l, v = it.split('=', 1)
        figures.setdefault(l, []).append(v)
    fails = run_all(html, io.open(a.php, encoding='utf-8').read(), a.wrapper, _kv(a.slug),
                    js_path=a.js, figures=figures or None)
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())

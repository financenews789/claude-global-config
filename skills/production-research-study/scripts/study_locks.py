# -*- coding: utf-8 -*-
"""Mechanical locks for an Eco3min research study (production-research-study).

Every audit_extract.py from R1 to R12 re-typed the same guards and they drifted
between copies: the hedge regex of R1 requires a digit or dollar sign, R4 adds
the French forms, R2 lists different AI tics than R1, R3 and R4 use different
counting nouns. The vocabulary here is the one written in SKILL.md §18.3
(Verrous D, E, G), §12.5 (tolerances), §12.6 (report format) and the closing
RAPPEL BLOQUANT (zero HTML comment). A study script imports it:

    import os, sys
    sys.path.insert(0, os.path.expanduser(
        '~/.claude/skills/production-research-study/scripts'))
    from study_locks import (Claims, TOLERANCE, close, scan_hedges,
                             scan_counting_claims, editorial_locks,
                             assert_no_html_comments, strip_html)

    df = pd.read_csv('study.csv', parse_dates=['date'])      # raw CSV only (Verrou A)
    pages = {'EN': open('page_body.html', encoding='utf-8').read(),
             'FR': open('page_fr.html', encoding='utf-8').read()}

    C = Claims(pages)                                        # Step 6, §12.4 / §12.6
    latest = df.iloc[-1]
    C.add('Latest T5YIE 60bp above 2% target', '60 basis points',
          close((latest.t5yie - 2.00) * 100, 60, 'bp'))
    print(C.report('Study R13'))
    C.halt_if_fail()

    hj = json.load(open('hedge_justifications.json', encoding='utf-8'))
    for lang, html in pages.items():                         # Step 6.5d, Verrou D
        bad = scan_hedges(strip_html(html), justified=hj, fr=(lang == 'FR'))
        assert not bad, ('6.5d unjustified hedge', bad)
        counts = scan_counting_claims(strip_html(html), fr=(lang == 'FR'))
        unbacked = [c for c in counts if c[0] not in ASSERTED_NUMBERS]
        assert not unbacked, ('6.5e counting claim without assertion', unbacked)
        locks = editorial_locks(strip_html(html))            # Step 6.5g, Verrou G
        assert not any(locks.values()), ('6.5g', locks)
        assert_no_html_comments(html)                        # RAPPEL BLOQUANT

`editorial_locks` counts only the em dash U+2014; the en dash of ranges
(`1959–2007`) and the minus sign (`−0,013`) are untouched by construction.
`fr=True` extends the hedge words and the counting nouns with the French forms
observed in the bilingual studies R2 and R4; the English lists are the SKILL.md
ones and are always active.

The locks are deliberately stricter than the copies they replace. Re-run on the
delivered R1-R4 (15/09/2026), where every audit_extract.py had logged zero:
  - R2 and R3 never scanned social_package.md for Verrou G; the script finds
    4 em dashes there, all in markdown headings ("# Social package — R2").
    The doctrine puts the social package in scope: real misses.
  - `should` / `must` are scanned as bare words (the §18.3 vocabulary); R2 and
    R4 only matched "you should", "investors should", "must consider". A
    methodological "whether the yield should be trailing or forward" or a FAQ
    "Should the premium use…" is not applied to a profile: pass it through
    `allow=(...)` with the reason printed in the audit output, never by
    shortening the word list.
  - "~600" in the heading "## LinkedIn (~600)" is the §22.1 length budget, not
    a hedge on a value: justify it in hedge_justifications.json or scan the
    posted copy blocks rather than the whole file.
"""
import re

# ── §12.5 tolerances — "pas de générosité" ───────────────────────────────────
TOLERANCE = {
    'pct_abs': 0.005,   # pourcentage absolu (ex : 2.60%)     ±0.005% (= 0.5bp)
    'pct_rel': 0.05,    # pourcentage relatif (%)              ±0.05% absolu
    'pp': 0.005,        # percentage points                    ±0.005pp
    'bp': 1.0,          # basis points                         ±1bp
    'count': 0.0,       # comptages (n=X)                      exact
    'ratio': 0.015,     # ratios (X×)                          ±0.015
    'mean': 0.01,       # moyennes / médianes                  ±0.01
}


def close(value, expected, kind):
    """True when |value - expected| is within the §12.5 tolerance for `kind`."""
    return abs(float(value) - float(expected)) <= TOLERANCE[kind]


# ── §12.4 / §12.6 claim collector ────────────────────────────────────────────
class Claims(object):
    """add_claim(description, expected_text_in_html, verifier) + §12.6 report.

    `texts` is a dict {label: text}. A claim passes when its verifier is true
    AND expected_text_in_html is present in at least one text (or in the text
    named by `where`). fail > 0 → halt_if_fail() raises: no tolerable count.
    """

    def __init__(self, texts):
        if isinstance(texts, str):
            texts = {'html': texts}
        self.texts = dict(texts)
        self.rows = []

    def add(self, description, expected_text_in_html, verifier, where=None, csv_value=None):
        targets = [self.texts[where]] if where else list(self.texts.values())
        present = any(expected_text_in_html in t for t in targets)
        ok = bool(verifier) and present
        self.rows.append(dict(description=description, expected=expected_text_in_html,
                              verifier=bool(verifier), present=present, ok=ok,
                              csv_value=csv_value))
        return ok

    add_claim = add

    @property
    def failures(self):
        return [r for r in self.rows if not r['ok']]

    def report(self, title=''):
        n, f = len(self.rows), len(self.failures)
        out = ['EXHAUSTIVE VALUE-BY-VALUE VERIFICATION' + (' — %s' % title if title else ''),
               '======================================',
               'Total claims:    %d' % n,
               'Pass:            %d' % (n - f),
               'Fail:            %d' % f]
        if f:
            out.append('')
            out.append('FAILURE DETAILS:')
            for r in self.failures:
                why = 'verifier false' if not r['verifier'] else 'text not found'
                out.append('  ✗ %s: expected %r, %s, csv_value=%s'
                           % (r['description'], r['expected'], why, r['csv_value']))
        return '\n'.join(out)

    def halt_if_fail(self):
        if self.failures:
            raise AssertionError('HALT — %d claim(s) failed; no delivery (§12.6)' % len(self.failures))


# ── helpers ──────────────────────────────────────────────────────────────────
_TAG = re.compile(r'<[^>]+>')
_WS = re.compile(r'\s+')


def strip_html(html):
    """Visible text of an HTML body (tags removed, whitespace collapsed)."""
    return _WS.sub(' ', _TAG.sub(' ', html))


def _ctx(text, start, end, width=40):
    return text[max(0, start - width):end + width].replace('\n', ' ')


# ── Verrou D — hedges (§18.3, §14.5, §18.1 règle 3) ──────────────────────────
HEDGE_WORDS = ('approximately', 'roughly', 'about', 'around', 'nearly', 'close to')
HEDGE_WORDS_FR = ('environ', 'près de', 'pres de', 'presque', 'quelque', 'quasiment', 'à peu près')
_NUM = r'[−\-]?\$?\d[\d.,]*'


def _hedge_re(fr):
    words = HEDGE_WORDS + (HEDGE_WORDS_FR if fr else ())
    alt = '|'.join(re.escape(w) for w in words)
    return re.compile(r'\b(?:%s)\s+(?:%s)|~\s?%s' % (alt, _NUM, _NUM), re.I)


def scan_hedges(text, justified=None, fr=False):
    """Hedge word followed by a number (Verrou D).

    Returns [(match, context)]. With `justified` (the hedge_justifications.json
    dict, keys = the exact hedge strings), returns only the unjustified ones.
    """
    hits = []
    known = {k.lower().strip() for k in (justified or {})}
    for m in _hedge_re(fr).finditer(text):
        s = _WS.sub(' ', m.group(0)).strip()
        if s.lower() in known:
            continue
        hits.append((s, _ctx(text, m.start(), m.end())))
    return hits


# ── Verrou E — counting claims (§18.3) ───────────────────────────────────────
COUNT_NOUNS = ('events', 'occurrences', 'observations', 'onsets', 'episodes', 'recessions',
               'false positives', 'triggers', 'crossings', 'cases', 'instances', 'times',
               'weeks', 'months', 'years')
COUNT_NOUNS_FR = ('événements', 'evenements', 'occurrences', 'observations', 'épisodes', 'episodes',
                  'récessions', 'recessions', 'faux positifs', 'déclenchements', 'croisements',
                  'cas', 'fois', 'semaines', 'mois', 'années', 'annees', 'ans')


def _count_re(fr):
    nouns = COUNT_NOUNS + (COUNT_NOUNS_FR if fr else ())
    alt = '|'.join(re.escape(n) for n in nouns)
    return re.compile(r'\b(\d{1,4})\s+(?:(?:consecutive|distinct|separate|full|calendar|trading|'
                      r'consécutifs|consécutives|distincts|distinctes)\s+)?(%s)\b'
                      r'|\b(\d{1,4})\s+of\s+(?:the\s+)?(\d{1,4})\b|\b(\d{1,4})/(\d{1,4})\b' % alt, re.I)


def scan_counting_claims(text, fr=False):
    """Every 'N <noun>', 'N of M' and 'N/M' in the text (Verrou E).

    Returns a sorted set of (N, form, context). Each N must be produced by an
    explicit assertion in compute_stats.py; the caller compares against its
    asserted numbers. Dates such as 12/2024 are excluded from the N/M form by
    the 1-4 digit bound on both sides only; whitelist them on the caller side.
    """
    found = set()
    for m in _count_re(fr).finditer(text):
        if m.group(1):
            found.add((m.group(1), m.group(2).lower(), _ctx(text, m.start(), m.end())))
        elif m.group(3):
            found.add((m.group(3), 'of %s' % m.group(4), _ctx(text, m.start(), m.end())))
        else:
            found.add((m.group(5), '/%s' % m.group(6), _ctx(text, m.start(), m.end())))
    return sorted(found)


# ── Verrou G — editorial locks (§18.3, editeur-eco3min, AMF 2, 3, 6) ─────────
EM_DASH = '—'
AI_TICS = ('worth noting', 'delve', 'dive into', 'ever-evolving', 'paradigm shift',
           'as we navigate', 'in conclusion,', 'truly', 'literally', 'undeniably', 'fundamentally')
PRESCRIPTIVE = ('should', 'must', 'need to', 'ought to', 'we recommend')
ACTION_TIMING = ('buy', 'sell', 'entry point', 'price target', 'now is the time',
                 'overweight', 'underweight')


def _word_hits(text, words, allow=()):
    hits = []
    low = text.lower()
    for w in words:
        pat = r'(?<![\w-])%s(?![\w-])' % re.escape(w)
        for m in re.finditer(pat, low):
            ctx = _ctx(text, m.start(), m.end())
            if any(a.lower() in ctx.lower() for a in allow):
                continue
            hits.append((w, ctx))
    return hits


def editorial_locks(text, allow=()):
    """Verrou G on a site-facing deliverable (body, social package, metas, alt, title).

    Returns {'em_dash': [...], 'ai_tics': [...], 'prescriptive': [...], 'action': [...]};
    every list must be empty. Only U+2014 counts as em dash: ranges keep the en
    dash (1959–2007) and negatives keep the minus sign (−0,013). `allow` lists
    documented exceptions (context substrings) that are not counted, e.g. a
    quoted title; use it sparingly and say so in the audit output.
    """
    em = [(EM_DASH, _ctx(text, m.start(), m.end())) for m in re.finditer(EM_DASH, text)]
    return {
        'em_dash': em,
        'ai_tics': _word_hits(text, AI_TICS, allow),
        'prescriptive': _word_hits(text, PRESCRIPTIVE, allow),
        'action': _word_hits(text, ACTION_TIMING, allow),
    }


# ── RAPPEL BLOQUANT — zéro commentaire HTML dans le contenu publié ────────────
_HTML_COMMENT = re.compile(r'<!--.*?-->', re.S)


def find_html_comments(html):
    return _HTML_COMMENT.findall(html)


def assert_no_html_comments(html):
    found = find_html_comments(html)
    assert not found, 'commentaire HTML dans le contenu: %r' % [c[:60] for c in found[:5]]
    return True


# ── Verrou H — anti-répétition de série (ajouté le 17/09/2026) ───────────────
# Constaté sur R3→R9 : squelette fixe voulu (blocs machine), mais trois figures
# de prose revenaient d'une étude à l'autre : la phrase-pivot toujours bâtie en
# antithèse (« a shared trend, not a shared week » ; « absorbs the shock; records
# the anchor » ; « bought no margin; it is the margin »), le Beat 1 titré « What
# the [X] story says » deux études de suite, le label « Robustness, disclosed: »
# verbatim de R3 à R9. Le squelette est le contrat d'audit et reste ; c'est la
# phrase qui doit tourner. Le verrou lit les études déjà livrées dans out/ et
# bloque la répétition, il n'impose aucune forme.
import datetime as _dt
import glob as _glob
import os as _os

# H2 des blocs fixes (§19) : autorisés à l'identique sur toute la série.
FIXED_H2 = {
    'latest observation', 'summary', 'executive summary', 'key statistics',
    'the record in six numbers', 'forward distribution', 'levels to watch',
    'key levels to watch', 'historical turning points', 'methodology',
    'data sources and references', 'sources and references', 'data sources & references',
    'sources', 'limitations', 'limits', 'frequently asked questions', 'faq', 'questions',
    'related', 'related research', 'download the dataset', 'data tables',
    'decade and episode tables', 'era and episode tables', 'era and lead-lag tables',
    'era, decade and frequency tables', 'decade by decade',
    # FR
    'dernière observation', 'derniere observation', 'résumé', 'resume', 'synthèse', 'synthese',
    'le dossier en six chiffres', 'distribution à terme', 'distribution a terme',
    'niveaux à surveiller', 'niveaux a surveiller', 'points de retournement historiques',
    'méthodologie', 'methodologie', 'sources et références', 'sources et references',
    'limites', 'questions fréquentes', 'questions frequentes', 'foire aux questions',
    'à lire aussi', 'a lire aussi', 'tableaux de données', 'tableaux de donnees',
}
# Blocs fixes dont le libellé varie d'une étude à l'autre (panneau de stats,
# tableaux, distribution forward, points de retournement) : familles.
FIXED_H2_PATTERNS = (
    r'six (numbers|chiffres|nombres)',
    r'^points de retournement',
    r'^(historical )?turning points',
    r'^tableaux? (par|de|des|d.)\b',
    r'\btables$',
    r'^distribution (forward|à terme|a terme)',
    r'^forward distribution',
    r'^what .+ (was|were) followed by$',
    r'^ce qui a suivi .+',
)

# Gabarits de titre de Beat : un même gabarit sur deux études consécutives = ÉCHEC.
H2_TEMPLATES = (
    r'^what the .+ (story|reading|narrative|view|thesis) says$',
    r'^ce que (dit|raconte) (le|la|l.)\s?.+',
    r'^where (the|that|this) .+ (holds up|is weakest|sits|breaks)$',
    r'^what this does not settle$',
    r'^ce que (cela|ça|ceci) ne tranche pas$',
    r'^pick any .+',
    r'^choisis(sez)? .+',
)

# Labels de la phrase de robustesse (TL;DR). Le même label que l'étude
# précédente = ÉCHEC. Le menu vit dans references/07-verrous-a-g.md §18.3 H.
ROBUSTNESS_LABELS = (
    'robustness, disclosed', 'checked the other way', 'same result if', 'same sign if',
    'alternative measure', 'the sample without', 'with a later start', 'on the other convention',
    'robustesse, divulguée', 'robustesse, divulguee', 'vérifié dans l.autre sens', 'verifie dans l.autre sens',
    'même résultat si', 'meme resultat si', 'même signe si', 'meme signe si', 'mesure alternative',
    'l.échantillon sans', 'l.echantillon sans', 'avec un départ plus tardif', 'avec un depart plus tardif',
    'sur l.autre convention',
)

PIVOT_FIGURES = ('antithesis', 'temporal', 'number', 'question', 'definition', 'other')
_FIGURE_FR = {'antithèse': 'antithesis', 'antithese': 'antithesis', 'temporel': 'temporal',
              'temporelle': 'temporal', 'chiffre': 'number', 'nombre': 'number',
              'définition': 'definition', 'autre': 'other'}

_H2 = re.compile(r'<h2[^>]*>(.*?)</h2>', re.S | re.I)
_README_DATE = re.compile(r'Produit le (\d{2})/(\d{2})/(\d{4})')
_README_PIVOT = re.compile(
    r'\*\*Phrase-pivot\*\*[^\n]*?(?:figure\s*:\s*([a-zA-Zéè]+))?[^\n]*\n\s*\n((?:>[^\n]*\n?)+)', re.I)


def h2_titles(html):
    """Visible text of every <h2>, in order, whitespace collapsed."""
    return [_WS.sub(' ', _TAG.sub('', t)).strip() for t in _H2.findall(html)]


def classify_pivot(sentence):
    """Heuristic figure of a pivot sentence; the README declaration wins when present.

    temporal   : opens on a time marker (Before/Since/Avant/Depuis/In 20xx)
    question   : ends with ?
    antithesis : ', not ' / ' pas ' / ' non ' / but / two clauses on ';' or ' : '
    number     : carries a digit and no opposition marker
    definition : 'X is a Y' / 'X est un Y' without opposition
    """
    s = sentence.strip().strip('>').strip()
    low = s.lower()
    if re.match(r'^(before|since|after|until|avant|depuis|après|apres|jusqu|in \d{4}|en \d{4})', low):
        return 'temporal'
    if s.endswith('?'):
        return 'question'
    if re.search(r',\s*not\b|\bnot\s+an?\b|\s(pas|non)\s|;|\s:\s|\bbut\b|\bmais\b', low):
        return 'antithesis'
    if re.search(r'\d', s):
        return 'number'
    if re.search(r'\b(is|are|est|sont)\s+(a|an|the|un|une|le|la|l.)\b', low):
        return 'definition'
    return 'other'


def study_fingerprint(study_dir):
    """What Verrou H compares: H2 per language, robustness label, pivot figure, date."""
    fp = {'id': _os.path.basename(_os.path.normpath(study_dir)), 'date': None,
          'h2': {}, 'label': {}, 'pivot': {}, 'figure': None}
    for lang, name in (('EN', 'page_body.html'), ('FR', 'page_fr.html')):
        p = _os.path.join(study_dir, name)
        if not _os.path.exists(p):
            continue
        html = open(p, encoding='utf-8').read()
        fp['h2'][lang] = h2_titles(html)
        low = strip_html(html).lower()
        fp['label'][lang] = next((l for l in ROBUSTNESS_LABELS if re.search(l, low)), None)
    readme = _os.path.join(study_dir, 'README_DELIVERABLE.md')
    if _os.path.exists(readme):
        txt = open(readme, encoding='utf-8').read()
        m = _README_DATE.search(txt)
        if m:
            fp['date'] = '%s-%s-%s' % (m.group(3), m.group(2), m.group(1))
        m = _README_PIVOT.search(txt)
        if m:
            quotes = [q.strip('> ').strip() for q in m.group(2).strip().split('\n') if q.strip('> ').strip()]
            if quotes:
                fp['pivot'] = {'EN': quotes[0], 'FR': quotes[1] if len(quotes) > 1 else None}
                declared = (m.group(1) or '').lower()
                declared = _FIGURE_FR.get(declared, declared)
                fp['figure'] = declared if declared in PIVOT_FIGURES else classify_pivot(quotes[0])
    if not fp['date']:
        body = _os.path.join(study_dir, 'page_body.html')
        if _os.path.exists(body):
            fp['date'] = _dt.datetime.fromtimestamp(_os.path.getmtime(body)).strftime('%Y-%m-%d')
    return fp


def series_corpus(out_dir, exclude=()):
    """Fingerprints of every delivered study in out_dir (has page_body.html), oldest first."""
    fps = []
    for d in sorted(_glob.glob(_os.path.join(out_dir, '*'))):
        if not _os.path.isdir(d) or _os.path.basename(d) in exclude:
            continue
        if not _os.path.exists(_os.path.join(d, 'page_body.html')):
            continue
        fps.append(study_fingerprint(d))
    return sorted(fps, key=lambda f: (f['date'] or '', f['id']))


def _template_of(title):
    low = title.lower().strip()
    for pat in H2_TEMPLATES:
        if re.match(pat, low):
            return pat
    return None


def series_repetition(current, corpus):
    """Verrou H. `current` = study_fingerprint(dir), `corpus` = series_corpus(out, exclude=[id]).

    Returns {'h2_dup': [...], 'h2_template': [...], 'label': [...], 'pivot_figure': [...]};
    every list must be empty. Rules:
      h2_dup        a non-fixed H2 identical (case-insensitive) to any previous study's H2
      h2_template   a Beat H2 built on a gabarit (H2_TEMPLATES) that the IMMEDIATELY
                    previous study also used
      label         robustness label identical to the previous study's, same language
      pivot_figure  pivot sentence figure identical to the previous study's
    An empty corpus (first study of a series) passes by construction.
    """
    out = {'h2_dup': [], 'h2_template': [], 'label': [], 'pivot_figure': []}
    if not corpus:
        return out
    prev = corpus[-1]
    for lang, titles in current['h2'].items():
        seen = {}
        for fp in corpus:
            for t in fp['h2'].get(lang, []):
                seen.setdefault(t.lower().strip(), fp['id'])
        prev_templates = {_template_of(t) for t in prev['h2'].get(lang, [])} - {None}
        for t in titles:
            key = t.lower().strip()
            if key in FIXED_H2 or any(re.search(pat, key) for pat in FIXED_H2_PATTERNS):
                continue
            if key in seen:
                out['h2_dup'].append((lang, t, seen[key]))
            tpl = _template_of(t)
            if tpl and tpl in prev_templates:
                out['h2_template'].append((lang, t, prev['id'], tpl))
        cur_label = current['label'].get(lang)
        if cur_label and cur_label == prev['label'].get(lang):
            out['label'].append((lang, cur_label, prev['id']))
    if current['figure'] and current['figure'] == prev['figure']:
        out['pivot_figure'].append((current['figure'], current['pivot'].get('EN'),
                                    prev['id'], prev['pivot'].get('EN')))
    return out


def assert_series_locks(study_dir, out_dir=None):
    """One-call Verrou H for audit_extract.py: prints the check, raises on any repetition."""
    out_dir = out_dir or _os.path.dirname(_os.path.normpath(study_dir))
    cur = study_fingerprint(study_dir)
    corpus = series_corpus(out_dir, exclude=[cur['id']])
    corpus = [fp for fp in corpus if (fp['date'] or '') <= (cur['date'] or '9999')]
    rep = series_repetition(cur, corpus)
    print('[Verrou H] %s contre %d étude(s) livrée(s) (%s) ; figure pivot = %s'
          % (cur['id'], len(corpus), ', '.join(fp['id'] for fp in corpus) or 'aucune', cur['figure']))
    for k, v in rep.items():
        print('[Verrou H] %-13s %s' % (k, 'clean' if not v else v))
    assert not any(rep.values()), ('Verrou H, répétition de série', rep)
    return rep

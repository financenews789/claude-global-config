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

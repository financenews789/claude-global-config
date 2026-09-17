# -*- coding: utf-8 -*-
"""Specificity guard for the scoped CSS of an Eco3min research study.

Why this exists (found 16/09/2026 on R3, R4, R6 — the "Latest observation"
block rendered dark-on-dark with 17px uppercase labels). The Customizer CSS of
eco3min.fr (`wp-custom-css`) styles paragraphs with

    .entry-content p { font-family; font-size; line-height; color;
                       max-width; margin-bottom; text-align }

Specificity (0,1,1). Every single-class rule of a study, `.eco3-X-obs-value
{color:#fff;font-size:28px}` at (0,1,0), LOSES to it — whatever the order of
the stylesheets, whatever the wp_head priority. The bug is invisible in the
previews (no theme CSS) and only appears on the live page, on every `<p>` that
carries a study class: deck, meta, fig-title, fig-source, obs-label,
obs-value, stat-value…

The rule: any selector whose subject is a paragraph — an explicit `p`, or a
class that the study HTML puts on a `<p>` — must reach at least (0,2,0). This
module does it mechanically, keeping the original selector and adding a
boosted twin:

    .eco3-X-obs-value{…}          -> .eco3-X-obs-value,.eco3-X p.eco3-X-obs-value{…}
    .eco3-X-context p{…}          -> .eco3-X .eco3-X-context p{…}
    .eco3-X p{margin:0 0 16px}    -> .eco3-X .eco3-X-container p{margin:0 0 16px;color:inherit}

The `color:inherit` on the generic rule matters: a <p> whose own rule sets no
colour (obs-label, obs-desc inside the navy block) inherits white from its
parent only if no matching rule sets a colour, and `.entry-content p` does.

Headings, lists and tables are deliberately NOT boosted: `.entry-content h2`,
`ul`, `table`, `th` win on the live studies published so far and that is the
look the site has shipped with. Boosting them would restyle every published
study. That is an editorial decision, not a bug fix.

Use in a build_snippet.py, after the CSS is re-namespaced:

    import os, sys
    sys.path.insert(0, os.path.expanduser(
        '~/.claude/skills/production-research-study/scripts'))
    from css_specificity import boost_paragraph_rules, lint_paragraph_rules, p_classes

    classes = p_classes(page_en_html) | p_classes(page_fr_html)
    css = boost_paragraph_rules(css, NS, classes)          # NS = 'eco3-X'
    assert not lint_paragraph_rules(css, NS, classes), lint_paragraph_rules(css, NS, classes)

`P_CLASS_SUFFIXES` is the union of the class suffixes the series has put on a
`<p>` from R1 to R12: a study copying the CSS of the previous one inherits
boosted rules for all of them, and `lint_paragraph_rules` still catches a new
one that the current pages introduce.
"""
import re

# Every `-suffix` the series R1…R12 has put on a <p class="eco3-X-suffix">,
# union taken on 16/09/2026 over page_body.html + page_fr.html of R1, R2, R3,
# R4, R6, R12. Namespace-agnostic on purpose.
P_CLASS_SUFFIXES = frozenset([
    'caution', 'citation-label', 'context-label', 'deck', 'exec-label',
    'fig-dl', 'fig-permission', 'fig-source', 'fig-subtitle', 'fig-title',
    'footer', 'formula-label', 'interp-range', 'interp-title', 'intro',
    'live-note', 'meta', 'obs-desc', 'obs-label', 'obs-value',
    'related-label', 'share-text', 'share-title', 'stat-label', 'stat-value',
    'takeaway-label',
])

_P_TAG = re.compile(r'<p\b[^>]*\bclass="([^"]*)"', re.I)
# A CSS rule = selector list + declaration block, at any nesting depth. The
# study CSS is minified and never puts a brace inside a string (asserted).
_RULE = re.compile(r'([^{}]+)\{([^{}]*)\}')
_LEADING_TYPE = re.compile(r'^([a-zA-Z][a-zA-Z0-9]*)')
_CLASS = re.compile(r'\.([A-Za-z0-9_-]+)')


def p_classes(html):
    """Set of classes that appear on a <p> in an HTML document."""
    out = set()
    for attr in _P_TAG.findall(html):
        out.update(c for c in attr.split() if c)
    return out


def full_p_classes(ns, html_classes=()):
    """`ns`-prefixed class names to treat as paragraph classes: the series
    union (`P_CLASS_SUFFIXES`) plus whatever the given pages put on a <p>."""
    return {'%s-%s' % (ns, s) for s in P_CLASS_SUFFIXES} | set(html_classes)


def specificity(selector):
    """(ids, classes+attrs+pseudo-classes, types+pseudo-elements) — enough
    for class/type selectors; no :not()/:is() arithmetic (the study CSS has
    none, asserted by `boost_paragraph_rules`)."""
    sel = re.sub(r'::?[a-zA-Z-]+(\([^)]*\))?', lambda m: ' :pc ' if not m.group(0).startswith('::') else ' ::pe ', selector)
    ids = len(re.findall(r'#[A-Za-z0-9_-]+', sel))
    classes = len(re.findall(r'\.[A-Za-z0-9_-]+|\[[^\]]*\]|:pc', sel))
    types = len(re.findall(r'(?:^|[\s>+~(])([a-zA-Z][a-zA-Z0-9]*)', sel)) + sel.count('::pe')
    return (ids, classes, types)


def _subject_is_paragraph(compound, pclasses):
    m = _LEADING_TYPE.match(compound)
    if m:
        return m.group(1) == 'p'
    return any(c in pclasses for c in _CLASS.findall(compound))


def _boost_one(selector, ns, pclasses):
    """Return (boosted_selector or None, replace_original: bool)."""
    root = '.' + ns
    s = selector.strip()
    if not s or s.startswith('@'):
        return None, False
    parts = s.split()
    if any(p in ('>', '+', '~') for p in parts):
        # combinators other than descendant: leave alone, lint will report
        return None, False
    last = parts[-1]
    if not _subject_is_paragraph(last, pclasses):
        return None, False
    if len(parts) == 1 and (last == root or last.startswith(root + '.') or last.startswith(root + ':')):
        return None, False  # the root itself is a div
    explicit_p = _LEADING_TYPE.match(last) is not None
    if parts[0] == root:
        # `.eco3-X p` / `.eco3-X .eco3-X-foo p` : add the container hop
        boosted = ' '.join([root, root + '-container'] + parts[1:])
        return boosted, True          # same match set, just heavier
    if not explicit_p:
        parts = parts[:-1] + ['p' + last]
        return ' '.join([root] + parts), False  # keep the original: the class may also sit on a span
    return ' '.join([root] + parts), True


def boost_paragraph_rules(css, ns, html_classes=()):
    """Rewrite `css` so every paragraph-subject selector reaches (0,2,0)+.
    `ns` is the study namespace ('eco3-nlcorr'); `html_classes` the classes
    seen on <p> in the study pages (see `p_classes`). Idempotent."""
    assert ':not(' not in css and ':is(' not in css and ':where(' not in css, \
        'css_specificity: :not()/:is()/:where() present, specificity arithmetic not supported'
    for q in ('"', "'"):
        for m in re.finditer(q + r'[^' + q + r']*' + q, css):
            assert '{' not in m.group(0) and '}' not in m.group(0), \
                'css_specificity: brace inside a CSS string, the rule splitter would break'
    assert ns + '-container' in css, 'css_specificity: %s-container rule missing, the container hop needs it' % ns
    pclasses = full_p_classes(ns, html_classes)
    root = '.' + ns

    def fix(m):
        sel_list, body = m.group(1), m.group(2)
        lead = sel_list[:len(sel_list) - len(sel_list.lstrip())]
        out = []
        for sel in sel_list.strip().split(','):
            sel = sel.strip()
            if not sel:
                continue
            if sel.startswith(root + ' ') and specificity(sel) >= (0, 2, 0):
                out.append(sel)            # already heavy enough (idempotence)
                continue
            boosted, replace = _boost_one(sel, ns, pclasses)
            if boosted is None:
                out.append(sel)
            elif replace:
                out.append(boosted)
            else:
                out.append(sel)
                if boosted not in out:
                    out.append(boosted)
        # de-duplicate while keeping order (idempotence)
        seen, uniq = set(), []
        for s in out:
            if s not in seen:
                seen.add(s)
                uniq.append(s)
        # The generic paragraph rule of the study must also restore the
        # inherited colour: a <p> whose own rule declares no colour (obs-label,
        # obs-desc in the navy block) still lost it to `.entry-content p`,
        # because inheritance ranks below any matching rule.
        if (root + ' ' + root + '-container p') in uniq and 'color:' not in body:
            body = body.rstrip(';') + ';color:inherit'
        return lead + ','.join(uniq) + '{' + body + '}'

    return _RULE.sub(fix, css)


def lint_paragraph_rules(css, ns, html_classes=()):
    """Selectors whose subject is a paragraph and whose specificity stays
    below (0,2,0) — i.e. rules `.entry-content p` will still beat. Empty list
    = clean. A class that is on a <p> counts as clean when a boosted twin
    `p.<class>` with the same body exists in the same rule."""
    pclasses = full_p_classes(ns, html_classes)
    root = '.' + ns
    bad = []
    for m in _RULE.finditer(css):
        sels = [s.strip() for s in m.group(1).strip().split(',') if s.strip()]
        if sels and sels[0].startswith('@'):
            continue
        for sel in sels:
            parts = sel.split()
            if not parts:
                continue
            last = parts[-1]
            if not _subject_is_paragraph(last, pclasses):
                continue
            if len(parts) == 1 and (last == root or last.startswith(root + '.')):
                continue
            if specificity(sel) >= (0, 2, 0):
                continue
            explicit_p = _LEADING_TYPE.match(last) is not None
            if not explicit_p:
                twin = ' '.join([root] + parts[:-1] + ['p' + last])
                if twin in sels:
                    continue
            bad.append(sel)
    return bad

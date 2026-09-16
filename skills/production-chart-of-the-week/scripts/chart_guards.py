# -*- coding: utf-8 -*-
"""Render guards for Eco3min Chart of the Week PNGs.

Every failure this module catches is silent in matplotlib: a missing brand font
falls back to DejaVu without a warning, a missing glyph is swapped for another
face, a long title is clipped at the canvas edge, two header texts overlap, an
unescaped pair of dollar signs turns a sentence into italic mathtext, a killer
phrase runs past its banner, the watermark lands on a footer line. The PNG is
written either way and looks fine as a thumbnail. Only assertions catch them.

These guards were rewritten by hand in every cycle script (20, 21) and drifted
between copies. They live here now; a cycle script imports them:

    import os, sys
    sys.path.insert(0, os.path.expanduser(
        '~/.claude/skills/production-chart-of-the-week/scripts'))
    from chart_guards import (SERIF, SANS, MONO, load_brand_fonts,
                              assert_escaped_dollars, word_count, run_guards)

    CMAP = load_brand_fonts(FONT_DIR)          # asserts the three families render
    ...
    run_guards(fig, ax, CMAP, killer_text=killer_text, banner=BANNER, mark=mark)
    fig.savefig(out)

`banner` is (x, y, w, h) in figure coordinates. `mark` is the watermark artist.
"""
import glob
import os

import matplotlib
from matplotlib import font_manager as fm
from matplotlib.font_manager import FontProperties
from matplotlib.transforms import Bbox
from fontTools.ttLib import TTFont

SERIF, SANS, MONO = 'Source Serif 4', 'Inter', 'IBM Plex Mono'
_FAMILY_BY_PREFIX = (('SourceSerif', SERIF), ('Inter', SANS), ('IBMPlexMono', MONO))


def load_brand_fonts(font_dir):
    """Register the brand TTFs found in font_dir, assert each family resolves
    by name (no silent DejaVu fallback) and return {family: set(codepoints)}
    so callers can check glyph coverage per artist."""
    files = glob.glob(os.path.join(font_dir, '*.ttf'))
    assert files, 'no brand fonts in %s (run cycle20/setup_fonts.py)' % font_dir
    for path in files:
        fm.fontManager.addfont(path)
    for family in (SERIF, SANS, MONO):
        got = FontProperties(family=family).get_name()
        assert got == family, 'font fallback: asked %r, matplotlib resolved %r' % (family, got)
    cmap = {}
    for path in files:
        base = os.path.basename(path)
        fam = next((f for p, f in _FAMILY_BY_PREFIX if base.startswith(p)), None)
        assert fam, 'unknown font file %s' % base
        cmap.setdefault(fam, set()).update(TTFont(path).getBestCmap().keys())
    return cmap


def assert_escaped_dollars(text, label='text'):
    """An unescaped pair of $ turns the text into mathtext. Every $ must be \\$."""
    assert '$' not in text.replace('\\$', ''), 'unescaped dollar in %s: %r' % (label, text[:60])


def word_count(text):
    """Words = tokens with at least one alphanumeric; '$', ':' and '·' do not count."""
    return len([w for w in text.replace('\\$', ' ').split() if any(ch.isalnum() for ch in w)])


def _artists(fig, ax, extra):
    out = list(fig.texts) + list(ax.texts) + list(ax.get_xticklabels()) + list(ax.get_yticklabels())
    out += list(extra)
    return [a for a in out if a.get_text()]


def run_guards(fig, ax, cmap, killer_text=None, banner=None, mark=None,
               header_y_frac=0.72, max_overlap=0.12, extra_texts=(), margin=1):
    """Draw the canvas and assert: glyph coverage, no overflow, no mathtext,
    watermark clear of every other text, killer phrase inside its banner, no
    real overlap between header texts (title / subtitle / banner / column
    headers, i.e. everything above header_y_frac of the canvas). Returns the
    renderer so callers can add their own checks."""
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    W, H = fig.get_size_inches() * fig.dpi

    for artist in _artists(fig, ax, extra_texts):
        raw = artist.get_text()
        assert_escaped_dollars(raw, 'artist')
        body = raw.replace('\\$', '$')
        fam = artist.get_fontfamily()[0]
        if fam in cmap:
            missing = [ch for ch in body if ch not in ' \n' and ord(ch) not in cmap[fam]]
            assert not missing, 'glyph missing in %s: %r in %r' % (fam, missing, body[:40])
        bb = artist.get_window_extent(renderer=renderer)
        label = body.split('\n')[0][:48]
        assert bb.x0 >= -margin and bb.x1 <= W + margin, 'overflows horizontally: %r' % label
        assert bb.y0 >= -margin and bb.y1 <= H + margin, 'overflows vertically: %r' % label

    if mark is not None:
        mb = mark.get_window_extent(renderer=renderer).expanded(1.15, 1.15)
        for t in fig.texts:
            if t is not mark and t.get_text():
                assert Bbox.intersection(mb, t.get_window_extent(renderer=renderer)) is None, (
                    'watermark collides with %r' % t.get_text()[:40])

    if killer_text is not None and banner is not None:
        kb = killer_text.get_window_extent(renderer=renderer)
        right = (banner[0] + banner[2]) * W
        assert kb.x1 <= right - 6, 'killer phrase overruns its banner by %.0f px' % (kb.x1 - right)
        assert kb.x0 >= banner[0] * W, 'killer phrase starts left of its banner'

    heads = [(t.get_text().split('\n')[0][:40], t.get_window_extent(renderer=renderer))
             for t in fig.texts
             if t.get_text() and t.get_window_extent(renderer=renderer).y0 > header_y_frac * H]
    for i in range(len(heads)):
        for j in range(i + 1, len(heads)):
            (na, a), (nb, b) = heads[i], heads[j]
            inter = Bbox.intersection(a, b)
            if inter is None or a.width * a.height == 0 or b.width * b.height == 0:
                continue
            share = (inter.width * inter.height) / min(a.width * a.height, b.width * b.height)
            assert share < max_overlap, 'header texts overlap (%.0f%%): %r / %r' % (share * 100, na, nb)

    return renderer

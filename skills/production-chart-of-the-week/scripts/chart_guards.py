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


# ---------------------------------------------------------------------------
# Feed-size preview (added 17/09/2026).
#
# The r/dataisbeautiful feed shows the 1920x1080 PNG at roughly 375 CSS px
# wide on a phone (about 2x that on desktop). At that size the title and the
# shape of the data survive; labels, the price column, the killer phrase and
# the sources do not. Q2 (scroll-stop) and Q3 (insight without legend) are
# therefore judged on this preview, never on the full-size PNG. Cycle 21: the
# "second encoding" that passed Q1 was a column of dollar prices, invisible at
# feed size; 522k views converted to 1,100 upvotes (0.21 %), the profile of a
# ranked bar chart, not of the decoupling the chart was meant to show.
#
#     out = os.path.join(HERE, 'cycle22_chart_desktop_16x9.png')
#     fig.savefig(out, facecolor=BG, dpi=150)
#     feed_preview(out)          # writes *_feed375.png and *_feed375_x3.png
#
# Then Read the *_feed375_x3.png (nearest-neighbour upscale of the real feed
# pixels, so the image reader sees exactly what a phone shows) and answer the
# three feed questions of the skill (ETAPE 3, TEST FEED).
# ---------------------------------------------------------------------------

FEED_WIDTH = 375


def feed_preview(png_path, width=FEED_WIDTH, scale_up=3):
    """Downscale the delivered PNG to the feed width with a proper resampling
    filter, then write a nearest-neighbour upscale of that small image so the
    real feed pixels can be inspected. Returns (feed_path, inspect_path)."""
    from PIL import Image  # Pillow is in the cycle venv
    im = Image.open(png_path)
    W, H = im.size
    assert W > width, 'feed_preview expects the full-size PNG, got %dx%d' % (W, H)
    h = round(H * width / W)
    small = im.resize((width, h), Image.LANCZOS)
    stem, _ = os.path.splitext(png_path)
    feed_path = '%s_feed%d.png' % (stem, width)
    inspect_path = '%s_feed%d_x%d.png' % (stem, width, scale_up)
    small.save(feed_path)
    small.resize((width * scale_up, h * scale_up), Image.NEAREST).save(inspect_path)
    return feed_path, inspect_path


def feed_metrics(fig, ax, title_artist, renderer, width=FEED_WIDTH):
    """Numbers to quote in the checklist: cap height of the title once the PNG
    is shown at feed width (in CSS px), and the share of the canvas covered by
    the plot area. Indicative thresholds live in the skill (title >= 8 px,
    plot share >= 0.35); they are not asserted here because a cycle may have a
    written reason to deviate, but the numbers must be looked at."""
    W, H = fig.get_size_inches() * fig.dpi
    tb = title_artist.get_window_extent(renderer=renderer)
    scale = width / W
    # The bbox of a text artist spans ascender to descender; cap height is
    # roughly 70 % of the font size in the brand serif.
    title_cap_px = title_artist.get_fontsize() * fig.dpi / 72 * 0.70 * scale
    pb = ax.get_position()
    return {
        'title_cap_px_at_feed': round(title_cap_px, 1),
        'title_width_share': round(tb.width / W, 2),
        'plot_share': round(pb.width * pb.height, 2),
    }

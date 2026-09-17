# -*- coding: utf-8 -*-
"""Gardes de rendu matplotlib pour tout visuel Eco3min (visuels-eco3min §7 ter).

Chaque défaut attrapé ici est silencieux dans matplotlib : la police de marque
absente retombe sur DejaVu Sans sans avertissement, un glyphe manquant est
rendu par une autre face, un titre long est rogné au bord du PNG, deux textes
d'en-tête se superposent, deux `$` non échappés basculent la phrase en
mathtext italique, la ligne de sources mord la signature. Le PNG sort et
paraît correct en vignette. Seule une assertion dans le script l'attrape.

    import os, sys
    sys.path.insert(0, os.path.expanduser('~/.claude/skills/visuels-eco3min/scripts'))
    from mpl_guards import (SERIF, SANS, MONO, load_brand_fonts,
                            assert_escaped_dollars, run_guards)

    CMAP = load_brand_fonts(FONT_DIR)     # enregistre les TTF, asserte les 3 familles
    ...
    run_guards(fig, ax, CMAP)             # avant fig.savefig(out)

`FONT_DIR` contient les TTF statiques des trois familles (par exemple
`chart_of_the_week/docs/fonts/`, régénéré par `docs/cycle20/setup_fonts.py`).
Les fichiers doivent commencer par `SourceSerif`, `Inter` ou `IBMPlexMono`.

Les cycles Chart of the Week importent `production-chart-of-the-week/scripts/
chart_guards.py`, qui porte les mêmes gardes plus le bandeau de killer phrase ;
ce module est la version générique pour les autres familles (études, datasets,
heros matplotlib).
"""
import glob
import os

from matplotlib import font_manager as fm
from matplotlib.font_manager import FontProperties
from matplotlib.transforms import Bbox

SERIF, SANS, MONO = 'Source Serif 4', 'Inter', 'IBM Plex Mono'
FAMILIES = (SERIF, SANS, MONO)
_FAMILY_BY_PREFIX = (('SourceSerif', SERIF), ('Inter', SANS), ('IBMPlexMono', MONO))
SIGNATURE = 'Eco3min Research'
SOURCES_PREFIX = 'Sources'
OVERLAP_MAX = 0.12
SIGNATURE_GAP = 8


def load_brand_fonts(font_dir):
    """Enregistre les TTF de font_dir, asserte que chaque famille résout par
    son nom (aucun repli DejaVu) et retourne {famille: set(codepoints)}."""
    from fontTools.ttLib import TTFont
    files = glob.glob(os.path.join(font_dir, '*.ttf'))
    assert files, 'aucune police de marque dans %s' % font_dir
    for path in files:
        fm.fontManager.addfont(path)
    assert_fonts_rendered()
    cmap = {}
    for path in files:
        base = os.path.basename(path)
        fam = next((f for p, f in _FAMILY_BY_PREFIX if base.startswith(p)), None)
        assert fam, 'fichier de police inconnu %s' % base
        cmap.setdefault(fam, set()).update(TTFont(path).getBestCmap().keys())
    return cmap


def assert_fonts_rendered(families=FAMILIES):
    """Assertion 1 : la police demandée est bien la police rendue."""
    for family in families:
        got = FontProperties(family=family).get_name()
        assert got == family, 'repli de police : demandé %r, obtenu %r' % (family, got)


def assert_escaped_dollars(text, label='text'):
    """Assertion 4 : aucun `$` non échappé (mathtext)."""
    assert '$' not in text.replace('\\$', ''), 'dollar non échappé dans %s : %r' % (label, text)


def _artists(fig, ax, extra=()):
    arts = list(fig.texts) + list(extra)
    axes = [ax] if ax is not None else []
    for a in axes:
        arts += list(a.texts)
        arts += [a.title]
        arts += a.get_xticklabels() + a.get_yticklabels()
        arts += [a.xaxis.label, a.yaxis.label]
    return [t for t in arts if t.get_text().strip()]


def assert_no_overflow(fig, ax=None, renderer=None, extra=()):
    """Assertion 2 : aucun texte ne déborde du canvas."""
    r = renderer or fig.canvas.get_renderer()
    W, H = fig.get_size_inches() * fig.dpi
    for t in _artists(fig, ax, extra):
        bb = t.get_window_extent(renderer=r)
        assert -1 <= bb.x0 and bb.x1 <= W + 1, 'débordement horizontal : %r' % t.get_text()[:48]
        assert -1 <= bb.y0 and bb.y1 <= H + 1, 'débordement vertical : %r' % t.get_text()[:48]


def assert_no_header_overlap(fig, renderer=None, share_max=OVERLAP_MAX):
    """Assertion 3 : les textes posés en coordonnées figure ne se recouvrent pas
    (tolérance sur la plus petite boîte : deux lignes serrées se touchent sans se gêner)."""
    r = renderer or fig.canvas.get_renderer()
    boxes = [(t.get_text()[:40], t.get_window_extent(renderer=r)) for t in fig.texts if t.get_text().strip()]
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            (na, a), (nb, b) = boxes[i], boxes[j]
            inter = Bbox.intersection(a, b)
            if inter is None:
                continue
            share = (inter.width * inter.height) / min(a.width * a.height, b.width * b.height)
            assert share < share_max, 'chevauchement %.0f%% : %r / %r' % (share * 100, na, nb)


def assert_sources_before_signature(fig, renderer=None, gap=SIGNATURE_GAP):
    """Assertion 5 : la ligne de sources se termine avant la signature (ordre horizontal)."""
    r = renderer or fig.canvas.get_renderer()
    foot = [t for t in fig.texts if t.get_text().startswith(SOURCES_PREFIX)]
    sig = [t for t in fig.texts if t.get_text().startswith(SIGNATURE)]
    if foot and sig:
        x1 = max(t.get_window_extent(renderer=r).x1 for t in foot)
        x0 = min(t.get_window_extent(renderer=r).x0 for t in sig)
        assert x1 < x0 - gap, 'la ligne de sources mord la signature (x1=%.0f, x0=%.0f)' % (x1, x0)


def assert_ascii_or_cmap(fig, ax=None, cmap=None, extra=()):
    """Garde bonus : tout glyphe non ASCII est couvert par le cmap de sa famille
    (IBM Plex Mono n'a ni U+2009 ni U+202F). Sans cmap, exige l'ASCII pur."""
    for t in _artists(fig, ax, extra):
        s = t.get_text()
        if s.isascii():
            continue
        assert cmap, 'glyphe hors ASCII sans cmap pour vérifier : %r' % s
        fam = t.get_fontfamily()
        fam = fam[0] if isinstance(fam, (list, tuple)) else fam
        cov = cmap.get(fam)
        assert cov is not None, 'famille %r sans cmap : %r' % (fam, s)
        bad = [c for c in s if ord(c) > 127 and ord(c) not in cov]
        assert not bad, 'glyphes absents de %s : %r dans %r' % (fam, bad, s)


def run_guards(fig, ax=None, cmap=None, extra=(), check_dollars=True):
    """Les cinq assertions du §7 ter + le garde ASCII/cmap, à appeler avant savefig."""
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    assert_fonts_rendered()
    assert_no_overflow(fig, ax, r, extra)
    assert_no_header_overlap(fig, r)
    if check_dollars:
        for t in _artists(fig, ax, extra):
            assert_escaped_dollars(t.get_text(), 'texte')
    assert_sources_before_signature(fig, r)
    assert_ascii_or_cmap(fig, ax, cmap, extra)
    return True

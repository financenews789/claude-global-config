# -*- coding: utf-8 -*-
"""Chrome canonique matplotlib des visuels Eco3min : pied, signature, tuiles, ajustement.

Complète mpl_guards.py (qui asserte) par ce qui évite d'itérer quatre fois sur un pied
de chart qui déborde (18/09/2026, hero et chart des régimes de l'étude #6). Les tokens
viennent de brand_tokens.py ; aucun hex n'est recopié ici.

    import os, sys
    sys.path.insert(0, os.path.expanduser('~/.claude/skills/brand-kit-eco3min/scripts'))
    sys.path.insert(0, os.path.expanduser('~/.claude/skills/visuels-eco3min/scripts'))
    from mpl_guards import load_brand_fonts, run_guards
    from mpl_chrome import fit_text, footer, stat_tiles, header, char_budget

    CMAP = load_brand_fonts(FONT_DIR)
    fig = plt.figure(figsize=(8, 4.5), dpi=192, facecolor=BACKGROUNDS['white'])
    header(fig, 'Titre en Source Serif 4', 'Sous-titre Inter gris medium, une ou deux lignes')
    stat_tiles(fig, [('13 of 15', 'Fed reversals since 1976', '2-year moved first', True),
                     ('+129 bp', '2-year Treasury in 2026', '27 Feb to 15 Sep', False)])
    ...
    footer(fig, 'Sources: FRED DGS2, FEDFUNDS, 1976-06 to 2026-08, 603 obs., NBER dates. Values rounded',
                'Reversal = pivot rule, 100 bp follow-through within 24 months',
                url='eco3min.fr/en/2y-treasury-leads-fed-pivots/')
    run_guards(fig, ax, CMAP)

Budget de caractères (mono, canvas 8 in à 192 dpi, marges 4,5 %) : voir char_budget().
Un pied qui dépasse le budget se raccourcit, il ne se rétrécit pas sous 5,2 pt.
"""
import os
import sys

sys.path.insert(0, os.path.expanduser('~/.claude/skills/brand-kit-eco3min/scripts'))
from brand_tokens import NEUTRALS, TERRACOTTA, FONTS  # noqa: E402

SERIF, SANS, MONO = FONTS['serif'], FONTS['sans'], FONTS['mono']
INK = NEUTRALS['charcoal']
MID = NEUTRALS['grey_medium']
RULE = NEUTRALS['grey_xlight']
SIGNATURE = 'Eco3min Research'
LEFT, RIGHT = 0.045, 0.965


def char_budget(fig, fontsize, left=LEFT, right=RIGHT, mono=True):
    """Nombre de caractères qui tiennent sur une ligne entre `left` et `right` (fractions
    de la figure) pour un corps mono donné. Approximation 0,6 em par glyphe mono, 0,5 em
    en Inter ; suffisante pour dimensionner un pied avant de le rendre."""
    w_px = fig.get_size_inches()[0] * fig.dpi * (right - left)
    em_px = fontsize / 72.0 * fig.dpi
    return int(w_px / (em_px * (0.6 if mono else 0.5)))


def fit_text(fig, t, right=RIGHT, floor=5.2):
    """Réduit la taille d'un texte jusqu'à ce que son bord droit passe sous `right`.
    Retourne le texte ; s'arrête à `floor` (le garde de mpl_guards attrapera le reste)."""
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    limit = right * fig.get_size_inches()[0] * fig.dpi
    while t.get_fontsize() > floor:
        if t.get_window_extent(renderer=r).x1 <= limit:
            return t
        t.set_fontsize(t.get_fontsize() - 0.4)
        fig.canvas.draw()
        r = fig.canvas.get_renderer()
    return t


def header(fig, title, subtitle=None, y=0.955, size=15.2, sub_size=7.6, left=LEFT):
    """Titre Source Serif 4 600 charcoal, sous-titre Inter 400 gris medium (§0 du brand kit).
    Le sous-titre peut contenir un '\\n' ; il est ajusté à droite sans passer sous 6,4 pt."""
    t = fig.text(left, y, title, fontfamily=SERIF, fontsize=size, fontweight=600, color=INK, va='top')
    fit_text(fig, t, floor=11.0)
    s = None
    if subtitle:
        s = fig.text(left, y - 0.07, subtitle, fontfamily=SANS, fontsize=sub_size, color=MID, va='top')
        fit_text(fig, s, floor=6.4)
    return t, s


def footer(fig, sources, method=None, url=None, size=5.6, left=LEFT, right=RIGHT):
    """Pied canonique : deux lignes mono gris medium à gauche (sources, puis méthode ou
    date), signature `Eco3min Research` à droite et, si `url`, l'URL de la page en
    deuxième ligne. Réserve la largeur de la signature pour que mpl_guards
    (assert_sources_before_signature) passe sans itération : la ligne gauche est
    raccourcie par fit_text jusqu'à laisser 8 px avant la signature."""
    sig1 = fig.text(right, 0.062, SIGNATURE, fontfamily=MONO, fontsize=size, color=MID, va='top', ha='right')
    sig2 = fig.text(right, 0.034, url, fontfamily=MONO, fontsize=size, color=MID, va='top', ha='right') if url else None
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    w = fig.get_size_inches()[0] * fig.dpi
    lim1 = (sig1.get_window_extent(renderer=r).x0 - 8) / w
    lim2 = ((sig2.get_window_extent(renderer=r).x0 - 8) / w) if sig2 else right
    def _line(y, txt, lim):
        t = fig.text(left, y, txt, fontfamily=MONO, fontsize=size, color=MID, va='top')
        fit_text(fig, t, right=lim)
        fig.canvas.draw()
        if t.get_window_extent(renderer=fig.canvas.get_renderer()).x1 > lim * w:
            raise AssertionError('footer : ligne trop longue meme a %.1f pt (%d caracteres, budget ~%d) : raccourcir le texte, pas la police : %r'
                                 % (t.get_fontsize(), len(txt), char_budget(fig, t.get_fontsize(), left, lim), txt[:60]))
        return t

    l1 = _line(0.062, sources, lim1)
    l2 = _line(0.034, method, lim2) if method else None
    return l1, l2, sig1, sig2


def stat_tiles(fig, tiles, y=0.790, left=LEFT, right=RIGHT, big=17, rule_y=0.665):
    """Bandeau de 2 à 4 tuiles KPI (§0 du brand kit) : chiffre Inter 600, libellé Inter,
    sous-libellé IBM Plex Mono gris ; un seul chiffre en terracotta (`focus=True`) ;
    filets #E0E0E0 entre les tuiles et sous le bandeau. `tiles` = liste de
    (chiffre, libellé, sous-libellé, focus)."""
    from matplotlib.lines import Line2D
    n = len(tiles)
    assert 2 <= n <= 4, 'stat_tiles : 2 à 4 tuiles'
    assert sum(1 for t in tiles if t[3]) <= 1, 'stat_tiles : un seul chiffre en terracotta'
    step = (right - left) / n
    xs = [left + i * step for i in range(n)]
    out = []
    for (val, lab, sub, focus), x in zip(tiles, xs):
        out.append(fig.text(x, y, val, fontfamily=SANS, fontsize=big, fontweight=600,
                            color=(TERRACOTTA if focus else INK), va='top'))
        fig.text(x, y - 0.065, lab, fontfamily=SANS, fontsize=6.6, color=INK, va='top')
        fig.text(x, y - 0.097, sub, fontfamily=MONO, fontsize=5.4, color=MID, va='top')
    for x in xs[1:]:
        fig.add_artist(Line2D([x - 0.022, x - 0.022], [rule_y + 0.015, y + 0.005], color=RULE, lw=0.8))
    fig.add_artist(Line2D([left, right], [rule_y, rule_y], color=RULE, lw=0.8))
    return out

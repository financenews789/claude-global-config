# -*- coding: utf-8 -*-
"""Tokens du brand kit Eco3min v2.0 et contrôle de palette.

Source unique des constantes visuelles : un script de chart ou de hero les
importe, il ne recopie pas un hex. Les valeurs sont celles de
~/.claude/skills/brand-kit-eco3min/SKILL.md §0 à §4 ; si les deux divergent,
SKILL.md gagne et ce fichier se corrige.

    import os, sys
    sys.path.insert(0, os.path.expanduser('~/.claude/skills/brand-kit-eco3min/scripts'))
    from brand_tokens import (FONTS, NEUTRALS, BACKGROUNDS, TERRACOTTA, RANKS,
                              REGIMES, SAND, SAND_BORDER, FRAME, SIGNATURE,
                              FORMATS, PALETTE, off_palette, check_source)

    BG = BACKGROUNDS['cream']
    colors = [RANKS[i] for i in range(3)]          # 3 séries nommées = rangs 1-2-3
    zone = REGIMES['desinflationniste']['zone']    # aire pâle d'une série bleu acier
    assert not check_source(__file__), check_source(__file__)

En ligne de commande, bloquant avant livraison (code de sortie 1 si un hex
hors charte apparaît dans un fichier) :

    python brand_tokens.py generate_chart.py hero.svg page.html

`check_source` lit le fichier, extrait chaque `#RRGGBB` (et `#RGB`), et
retourne {hex: occurrences} pour ceux qui ne sont pas dans PALETTE. Un hex
légitime hors charte (un logo tiers imposé, par exemple) se déclare par
`allow=('#ABCDEF',)`, jamais en éditant PALETTE.
"""
import re
import sys

# --- typographie -----------------------------------------------------------
FONTS = {
    'serif': 'Source Serif 4',   # titres, titres de métrique, citations
    'sans': 'Inter',             # sous-titres, annotations, axes, chiffres des tuiles
    'mono': 'IBM Plex Mono',     # codes de série, sources, signature, tags
}
SERIF, SANS, MONO = FONTS['serif'], FONTS['sans'], FONTS['mono']

# --- neutres (§2.1) --------------------------------------------------------
NEUTRALS = {
    'charcoal': '#1A1A1A',
    'grey_medium': '#757575',
    'grey_light': '#C4C4C4',
    'grey_xlight': '#E0E0E0',
    'frame_cream': '#DED7C7',
}
CHARCOAL = NEUTRALS['charcoal']
GREY = NEUTRALS['grey_medium']
FRAME = NEUTRALS['frame_cream']
SAND = '#F2EAD8'          # fond du bandeau killer phrase
SAND_BORDER = '#E5DFD3'   # bordure du bandeau sur crème

# --- fonds (§2.2) ----------------------------------------------------------
BACKGROUNDS = {
    'cream': '#F8F5EE',      # défaut
    'white': '#FFFFFF',      # heros majeur, charts denses
    'charcoal': '#1A1A1A',   # inversé, formats spéciaux
}

# --- accent et palette catégorielle (§2.3, §2.5) ---------------------------
TERRACOTTA = '#B85C3C'
RANKS = ['#B85C3C', '#4A6B8A', '#6B8E5F', '#6B4A6B', '#B8854A', '#4A3F3D', '#C73E2E']
RANK_NAMES = ['terracotta', 'bleu acier', 'vert sourd', 'violet pourpre',
              'ocre sourd', 'charcoal doux', 'rouge sourd']

# --- codes régime (§3) : zone / ligne / label ------------------------------
REGIMES = {
    'inflationniste':      {'zone': '#F4DDD8', 'line': '#C73E2E', 'label': '#8B2A1F'},
    'desinflationniste':   {'zone': '#D8E2EC', 'line': '#4A6B8A', 'label': '#2D4256'},
    'stagflation':         {'zone': '#ECE2D2', 'line': '#B8854A', 'label': '#6E4E2B'},
    'liquidite_abondante': {'zone': '#DCE5D6', 'line': '#6B8E5F', 'label': '#3E5536'},
    'restriction':         {'zone': '#DDD4DD', 'line': '#6B4A6B', 'label': '#3E2A3E'},
    'crise_systemique':    {'zone': '#D8D5D3', 'line': '#4A3F3D', 'label': '#1F1A18'},
}

# --- couleurs web, interdites dans un visuel (§2.4) -------------------------
WEB_ONLY = {'navy': '#1A237E', 'gold': '#C9A84C'}

# --- chrome canonique (§0) ---------------------------------------------------
SIGNATURE = 'Eco3min Research'          # ligne 1 de la signature, bas-droite, jamais de cadratin
SITE_URL = 'eco3min.fr'
SOURCES_PREFIX = 'Sources:'             # ligne 1 du pied bas-gauche
ROUNDED = 'Values rounded for readability'

# --- formats stricts (§4) ----------------------------------------------------
FORMATS = {
    'hero_pilier': (1536, 864),
    'hero_majeur': (1536, 864),
    'hero_article': (1200, 630),
    'chart_of_the_week': (1920, 1080),
    'social_16x9': (1200, 675),
    'social_square': (1080, 1080),
}
MOBILE_TEST_WIDTH = 380

# --- ensemble des hex autorisés ---------------------------------------------
PALETTE = frozenset(
    list(NEUTRALS.values()) + [SAND, SAND_BORDER] + list(BACKGROUNDS.values())
    + [TERRACOTTA] + RANKS
    + [v for fam in REGIMES.values() for v in fam.values()]
)

_HEX = re.compile(r'#(?:[0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})\b')


def _norm(h):
    h = h.upper()
    if len(h) == 4:
        h = '#' + ''.join(c * 2 for c in h[1:])
    return h


def scan_hex(text):
    """Retourne {hex normalisé: occurrences} pour tout #RRGGBB / #RGB du texte."""
    out = {}
    for m in _HEX.findall(text):
        h = _norm(m)
        out[h] = out.get(h, 0) + 1
    return out


def off_palette(colors, allow=()):
    """Sous-ensemble de `colors` (itérable de hex) absent de PALETTE et de `allow`."""
    ok = PALETTE | {_norm(a) for a in allow}
    return sorted({_norm(c) for c in colors} - ok)


def check_source(path_or_text, allow=(), is_text=False):
    """Hex hors charte dans un fichier (script, SVG, HTML) ou un texte.
    Retourne {hex: occurrences}, vide si tout est dans PALETTE."""
    text = path_or_text if is_text else open(path_or_text, encoding='utf-8', errors='replace').read()
    found = scan_hex(text)
    bad = off_palette(found, allow)
    return {h: found[h] for h in bad}


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    rc = 0
    for p in argv:
        bad = check_source(p)
        if bad:
            rc = 1
            print('%s : %d hex hors charte' % (p, len(bad)))
            for h, n in sorted(bad.items(), key=lambda kv: -kv[1]):
                print('  %s x%d' % (h, n))
        else:
            print('%s : OK (palette v2.0)' % p)
    return rc


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

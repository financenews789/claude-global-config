# -*- coding: utf-8 -*-
"""Gate de licence FRED — lit le tag de licence d'une série et tranche.

FRED distingue TROIS niveaux (skill sourcing-donnees-eco3min, section « Cas FRED ») :

    public domain: citation requested   -> CSV CC BY 4.0 possible
    copyrighted: citation required      -> publiable avec attribution, JAMAIS en CC BY 4.0
    copyrighted: pre-approval required  -> rien sans accord écrit du détenteur

Le statut se lit sur fred.stlouisfed.org/series/{ID}, balise <meta name="series-tag">.
Ce module fait la lecture par script, jamais à la main, et REFUSE de conclure
« public domain » par défaut : un ID inconnu, une page illisible ou un tag absent
lèvent FredLicenseError. Un composite hérite du niveau le plus dur de ses intrants.

Import depuis un script de production :

    import os, sys
    sys.path.insert(0, os.path.expanduser('~/.claude/skills/sourcing-donnees-eco3min/scripts'))
    from fred_license import fred_license, check_series, composite_level, can_ccby, publishable
    from fred_license import PUBLIC_DOMAIN, CITATION_REQUIRED, PRE_APPROVAL, FredLicenseError

    levels = check_series(['DGS10', 'RRPONTSYD', 'SP500'])   # {'DGS10': 'public domain', ...}
    lvl = composite_level(levels.values())                   # 'pre-approval required'
    assert publishable(lvl), 'un intrant pre-approval tue le composite'
    assert can_ccby(lvl) or declare_real_licence(...)        # citation required -> eco3_source_rights()

Ligne de commande :

    python fred_license.py GS10 BAA SP500          # table ; code retour 2 si un niveau pre-approval
    python fred_license.py --ccby GS10 BAA         # code retour 1 si un niveau n'est pas public domain
    python fred_license.py --composite DGS10 T10YIE # affiche aussi le niveau hérité par le composite

Réseau : une requête HTTPS par série, User-Agent explicite (annexe B : plusieurs
sources refusent les requêtes sans contact). Un 403 / 503 / timeout est une
FredLicenseError datée par le message, pas une propriété de FRED.
"""
import re
import sys
import time
import urllib.request
import urllib.error

PUBLIC_DOMAIN = 'public domain'
CITATION_REQUIRED = 'citation required'
PRE_APPROVAL = 'pre-approval required'

# du plus libre au plus dur ; composite_level() prend le max
_ORDER = {PUBLIC_DOMAIN: 0, CITATION_REQUIRED: 1, PRE_APPROVAL: 2}

USER_AGENT = 'Eco3min research contact@eco3min.fr'
_TAG_RE = re.compile(r'series-tag"\s+content="(copyrighted[^"]*|public domain[^"]*)"', re.I)


class FredLicenseError(Exception):
    """ID inconnu, page illisible, tag absent ou inattendu : on ne conclut rien."""


def _normalize(tag):
    t = tag.strip().lower()
    if t.startswith('public domain'):
        return PUBLIC_DOMAIN
    if 'pre-approval' in t:
        return PRE_APPROVAL
    if 'citation required' in t:
        return CITATION_REQUIRED
    raise FredLicenseError('tag FRED inattendu : %r' % tag)


def fred_license(series_id, timeout=20, retries=2):
    """Niveau de licence d'une série FRED (une des trois constantes du module)."""
    sid = series_id.strip().upper()
    if not re.fullmatch(r'[A-Z0-9_]+', sid):
        raise FredLicenseError('ID de série invalide : %r' % series_id)
    url = 'https://fred.stlouisfed.org/series/' + sid
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    last = None
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                html = r.read().decode('utf-8', 'replace')
            break
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise FredLicenseError('%s : série inconnue sur FRED (404)' % sid)
            last = 'HTTP %s' % e.code
        except (urllib.error.URLError, OSError) as e:
            last = str(e)
        time.sleep(1.5 * (attempt + 1))
    else:
        raise FredLicenseError('%s : FRED injoignable depuis cet environnement (%s, %s) — tester une autre route, dater le constat'
                               % (sid, last, time.strftime('%Y-%m-%d %H:%M')))
    m = _TAG_RE.search(html)
    if not m:
        raise FredLicenseError('%s : aucun tag series-tag lisible sur la page (format FRED changé ?)' % sid)
    return _normalize(m.group(1))


def check_series(series_ids, timeout=20):
    """{ID: niveau} pour chaque série ; lève à la première série inconnue."""
    return {sid.strip().upper(): fred_license(sid, timeout=timeout) for sid in series_ids}


def hardest(levels):
    levels = list(levels)
    if not levels:
        raise FredLicenseError('composite sans intrant')
    for lv in levels:
        if lv not in _ORDER:
            raise FredLicenseError('niveau inconnu : %r' % lv)
    return max(levels, key=_ORDER.get)


def composite_level(levels):
    """Niveau hérité par un composite : le plus dur de ses intrants. La division ne lave rien."""
    return hardest(levels)


def can_ccby(level):
    """Le CSV peut-il être redistribué en CC BY 4.0 ?"""
    return level == PUBLIC_DOMAIN


def publishable(level):
    """Peut-on publier la série (avec attribution, licence réelle déclarée) ?"""
    return level in (PUBLIC_DOMAIN, CITATION_REQUIRED)


def _main(argv):
    args = [a for a in argv if not a.startswith('--')]
    flags = {a for a in argv if a.startswith('--')}
    if not args:
        print(__doc__)
        return 0
    levels = {}
    rc = 0
    for sid in args:
        try:
            levels[sid.upper()] = fred_license(sid)
        except FredLicenseError as e:
            print('%-14s ERREUR  %s' % (sid.upper(), e))
            rc = max(rc, 3)
    for sid, lv in levels.items():
        verdict = {PUBLIC_DOMAIN: 'CSV CC BY 4.0 possible',
                   CITATION_REQUIRED: 'publiable avec attribution, JAMAIS en CC BY — declarer la licence reelle',
                   PRE_APPROVAL: 'NE PAS PUBLIER — retirer ou re-sourcer'}[lv]
        print('%-14s %-22s %s' % (sid, lv, verdict))
        if lv == PRE_APPROVAL:
            rc = max(rc, 2)
        elif '--ccby' in flags and lv != PUBLIC_DOMAIN:
            rc = max(rc, 1)
    if '--composite' in flags and levels:
        lv = composite_level(levels.values())
        print('composite      %-22s (niveau le plus dur des intrants)' % lv)
        if lv == PRE_APPROVAL:
            rc = max(rc, 2)
        elif '--ccby' in flags and lv != PUBLIC_DOMAIN:
            rc = max(rc, 1)
    return rc


if __name__ == '__main__':
    sys.exit(_main(sys.argv[1:]))

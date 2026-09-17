# -*- coding: utf-8 -*-
"""Test de fred_license.py contre la table « Cas FRED » de SKILL.md (19 séries)
plus les tests négatifs (composite hérite du plus dur, ID inconnu refusé,
tag inattendu refusé). Réseau requis : une requête par série.

    python test_fred_license.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fred_license import (fred_license, check_series, composite_level, can_ccby, publishable,
                          PUBLIC_DOMAIN, CITATION_REQUIRED, PRE_APPROVAL, FredLicenseError, _normalize)

# la table de SKILL.md, section « Cas FRED », colonne Exemples — vérité attendue
EXPECTED = {
    PUBLIC_DOMAIN: ['GS10', 'DGS10', 'USSTHPI', 'HQMCB10YR', 'CPIAUCSL'],
    CITATION_REQUIRED: ['BAA', 'NFCI', 'CFNAI', 'T10Y2Y', 'T5YIE', 'T10YIE', 'RRPONTSYD', 'USREC', 'M2V', 'VIXCLS'],
    PRE_APPROVAL: ['BAMLH0A0HYM2', 'SP500', 'NASDAQCOM', 'CSUSHPINSA'],
}

# --- tests hors réseau -------------------------------------------------------
assert composite_level([PUBLIC_DOMAIN, PUBLIC_DOMAIN]) == PUBLIC_DOMAIN
assert composite_level([PUBLIC_DOMAIN, CITATION_REQUIRED]) == CITATION_REQUIRED
assert composite_level([CITATION_REQUIRED, PRE_APPROVAL, PUBLIC_DOMAIN]) == PRE_APPROVAL
assert can_ccby(PUBLIC_DOMAIN) and not can_ccby(CITATION_REQUIRED) and not can_ccby(PRE_APPROVAL)
assert publishable(PUBLIC_DOMAIN) and publishable(CITATION_REQUIRED) and not publishable(PRE_APPROVAL)
assert _normalize('Copyrighted: Citation Required') == CITATION_REQUIRED
assert _normalize('copyrighted: pre-approval required') == PRE_APPROVAL
assert _normalize('public domain: citation requested') == PUBLIC_DOMAIN
for bad in ('', 'free', 'copyrighted'):
    try:
        _normalize(bad)
    except FredLicenseError:
        pass
    else:
        raise AssertionError('tag %r aurait dû être refusé' % bad)
try:
    composite_level([])
except FredLicenseError:
    pass
else:
    raise AssertionError('composite vide accepté')
try:
    fred_license('pas un id !')
except FredLicenseError:
    pass
else:
    raise AssertionError('ID invalide accepté')
print('tests hors réseau : OK')

# --- tests réseau ------------------------------------------------------------
ids = [s for lst in EXPECTED.values() for s in lst]
got = check_series(ids)
errors = []
for lv, lst in EXPECTED.items():
    for sid in lst:
        if got[sid] != lv:
            errors.append('%s : attendu %r, lu %r' % (sid, lv, got[sid]))
for sid in ids:
    print('%-14s %s' % (sid, got[sid]))
assert not errors, errors
print('%d séries de la table « Cas FRED » : niveau lu = niveau attendu' % len(ids))

# ID inconnu : refus, jamais « public domain » par défaut
try:
    fred_license('ECO3MINZZZ999')
except FredLicenseError as e:
    print('ID inconnu refusé :', e)
else:
    raise AssertionError('ID inconnu accepté')

# composite réel : sp500/gold hérite de SP500
lv = composite_level([got['SP500'], PUBLIC_DOMAIN])
assert lv == PRE_APPROVAL and not publishable(lv)
print('composite SP500/or : hérite de', lv, '-> non publiable')
print('OK')

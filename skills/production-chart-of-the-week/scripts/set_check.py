# -*- coding: utf-8 -*-
"""Set-completeness guard (ÉTAPE 2-QUATER, PÉRIMÈTRE DU SET).

A chart whose population is a named set ("16 OECD countries", "the 10
largest US cities", "G7", "EU-27", "every US state") is attacked on the set
before it is attacked on the numbers. Two documented failures:

- US cities: a "10 largest US cities" post was missing two of the ten. Nobody
  had listed the ten from the source; the set was whatever the data had.
- Cycle 21 (Big Mac): the stated reason for excluding Chile, Colombia,
  Costa Rica and Türkiye ("not in the OECD national-currency wage series")
  was false; they are in it, they lack a 2025 value. Iceland was missing and
  never named. Refutable in 30 seconds on OECD Data Explorer.

The rule this enforces: the universe is enumerated from an authoritative
list, every member is either included or excluded, every exclusion carries a
closed-list reason plus the evidence that makes it true, the count in the
title equals the number included, and a ranked set ("top N") is complete or
the gap is stated in the claim. Nothing is inferred from the dataset; the
manifest is written first, the dataset is checked against it.

Manifest (JSON file or dict):

    {
      "universe": {"name": "OECD member countries",
                   "source": "https://www.oecd.org/en/about/members-partners.html",
                   "as_of": "2026-09-15",
                   "members": ["AUS", "AUT", ...]},
      "rule": "non-euro OECD members with a country-level Big Mac price and a
               2025 value for wages, hours and tax",
      "exclusions": [
        {"id": "AUT", "reason": "rule",
         "source": "The Economist big-mac-full-index.csv",
         "detail": "single euro-area price, no country price"},
        {"id": "ISL", "reason": "no_value_in_source",
         "source": "The Economist big-mac-full-index.csv 2026-07-01",
         "detail": "not among the 54 rows; no McDonald's since 2009"},
        {"id": "TUR", "reason": "no_value_for_vintage",
         "source": "OECD AV_AN_WAGE PRICE_BASE=V, SDMX 2026-09-15",
         "detail": "latest TRY value 2024, reference year is 2025"}
      ],
      "included": ["CHE", "USA", ...],
      "claim": {"n": 16, "wording": "16 OECD countries"},
      "ranking": {                       # only for "top N by X" sets
        "metric": "population, 2024 estimate",
        "source": "US Census Bureau, Vintage 2024",
        "ordered": ["New York", "Los Angeles", ...],
        "gaps_stated": false             # true only if the claim says "N of the top M"
      }
    }

Reasons (closed list):
    rule                  excluded by the stated inclusion rule itself
    no_value_in_source    the source has no observation for this member at all
    no_value_for_vintage  the source has the member but not for the reference period
    methodology_break     the source flags the member's series as not comparable
    other_documented      anything else; `detail` must say what and `source` where

Usage (library, in build_dataset.py before writing the CSV):

    import os, sys
    sys.path.insert(0, os.path.expanduser(
        '~/.claude/skills/production-chart-of-the-week/scripts'))
    from set_check import check_manifest, OECD_MEMBERS, EURO_AREA_OECD
    check_manifest('set_manifest.json', dataset_ids=[r['iso3'] for r in records])

Usage (CLI):

    python set_check.py set_manifest.json                       # manifest only
    python set_check.py set_manifest.json data.csv iso3         # + dataset column

Raises SetError with every problem found (not just the first); prints a
reconciliation line on success: "universe 38 = included 16 + excluded 22".
"""
import csv
import io
import json
import os
import sys

REASONS = ('rule', 'no_value_in_source', 'no_value_for_vintage',
           'methodology_break', 'other_documented')

# Reference universes, ISO3. Verify against the source before each use; the
# as_of date is the last check. Bulgaria, Croatia and Romania are OECD
# accession candidates, not members; Bulgaria is in the euro area since
# 2026-01-01 but not in the OECD.
OECD_MEMBERS = {  # https://www.oecd.org/en/about/members-partners.html, as_of 2026-09-15, 38
    'AUS', 'AUT', 'BEL', 'CAN', 'CHE', 'CHL', 'COL', 'CRI', 'CZE', 'DEU',
    'DNK', 'ESP', 'EST', 'FIN', 'FRA', 'GBR', 'GRC', 'HUN', 'IRL', 'ISL',
    'ISR', 'ITA', 'JPN', 'KOR', 'LTU', 'LUX', 'LVA', 'MEX', 'NLD', 'NOR',
    'NZL', 'POL', 'PRT', 'SVK', 'SVN', 'SWE', 'TUR', 'USA',
}
EURO_AREA_OECD = {  # OECD members using the euro, as_of 2026-09-15, 17
    'AUT', 'BEL', 'DEU', 'ESP', 'EST', 'FIN', 'FRA', 'GRC', 'IRL', 'ITA',
    'LTU', 'LUX', 'LVA', 'NLD', 'PRT', 'SVK', 'SVN',
}
G7 = {'CAN', 'DEU', 'FRA', 'GBR', 'ITA', 'JPN', 'USA'}
assert len(OECD_MEMBERS) == 38 and len(EURO_AREA_OECD) == 17
assert EURO_AREA_OECD <= OECD_MEMBERS


class SetError(AssertionError):
    pass


def _load(manifest):
    if isinstance(manifest, dict):
        return manifest
    with io.open(manifest, encoding='utf-8') as fh:
        return json.load(fh)


def check_manifest(manifest, dataset_ids=None, verbose=True):
    """Reconcile universe, exclusions, included, claim (and ranking if any).
    Collects every problem, raises SetError with all of them."""
    m = _load(manifest)
    problems = []

    uni = m.get('universe') or {}
    members = list(uni.get('members') or [])
    for key in ('name', 'source', 'as_of'):
        if not uni.get(key):
            problems.append('universe.%s missing' % key)
    if len(members) != len(set(members)):
        dup = sorted({x for x in members if members.count(x) > 1})
        problems.append('universe.members has duplicates: %s' % dup)
    universe = set(members)
    if not universe:
        problems.append('universe.members is empty')
    if not m.get('rule'):
        problems.append('rule missing (one sentence: who is in and why)')

    included = list(m.get('included') or [])
    if len(included) != len(set(included)):
        problems.append('included has duplicates')
    inc = set(included)

    excl_ids = []
    for i, e in enumerate(m.get('exclusions') or []):
        eid = e.get('id')
        if not eid:
            problems.append('exclusions[%d] has no id' % i)
            continue
        excl_ids.append(eid)
        if e.get('reason') not in REASONS:
            problems.append('%s: reason %r not in %s' % (eid, e.get('reason'), REASONS))
        if not e.get('source'):
            problems.append('%s: exclusion without source (where is the evidence?)' % eid)
        if not e.get('detail'):
            problems.append('%s: exclusion without detail (what exactly is missing?)' % eid)
    if len(excl_ids) != len(set(excl_ids)):
        problems.append('exclusions list the same id twice')
    exc = set(excl_ids)

    if inc - universe:
        problems.append('included but not in universe: %s' % sorted(inc - universe))
    if exc - universe:
        problems.append('excluded but not in universe: %s' % sorted(exc - universe))
    if inc & exc:
        problems.append('both included and excluded: %s' % sorted(inc & exc))
    silent = universe - inc - exc
    if silent:
        problems.append('SILENT GAP, neither included nor excluded: %s' % sorted(silent))

    claim = m.get('claim') or {}
    n = claim.get('n')
    if n is None or not claim.get('wording'):
        problems.append('claim.n and claim.wording required (what the title says)')
    elif n != len(included):
        problems.append('claim says %s, included has %d' % (n, len(included)))

    rk = m.get('ranking')
    if rk:
        ordered = list(rk.get('ordered') or [])
        for key in ('metric', 'source'):
            if not rk.get(key):
                problems.append('ranking.%s missing' % key)
        if not ordered:
            problems.append('ranking.ordered is empty')
        elif n is not None:
            top = ordered[:n]
            missing_top = [x for x in top if x not in inc]
            below = [x for x in included if x not in top]
            if missing_top and not rk.get('gaps_stated'):
                problems.append('top-%s by %s is incomplete: %s missing; either include them '
                                'or set ranking.gaps_stated=true AND word the claim as '
                                '"N of the top M" (not "the N largest")'
                                % (n, rk.get('metric'), missing_top))
            if below and not missing_top:
                problems.append('included items outside the top %s by %s: %s'
                                % (n, rk.get('metric'), below))
            for x in missing_top:
                if x not in exc:
                    problems.append('%s is in the top %s but neither included nor excluded' % (x, n))

    if dataset_ids is not None:
        ds = list(dataset_ids)
        if len(ds) != len(set(ds)):
            problems.append('dataset has duplicate ids')
        if set(ds) != inc:
            problems.append('dataset ids != manifest.included: extra %s, missing %s'
                            % (sorted(set(ds) - inc), sorted(inc - set(ds))))

    if problems:
        raise SetError('set manifest failed:\n  - ' + '\n  - '.join(problems))
    if verbose:
        print('set ok: universe %d = included %d + excluded %d; claim "%s"'
              % (len(universe), len(inc), len(exc), claim.get('wording')))
    return True


def _cli(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    ids = None
    if len(argv) >= 4:
        col = argv[3]
        with io.open(argv[2], encoding='utf-8') as fh:
            rows = csv.DictReader(ln for ln in fh if not ln.startswith('#'))
            ids = [r[col] for r in rows]
    try:
        check_manifest(argv[1], dataset_ids=ids)
    except SetError as e:
        print(e)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(_cli(sys.argv))

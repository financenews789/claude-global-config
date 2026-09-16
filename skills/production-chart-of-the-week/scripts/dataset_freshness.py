# -*- coding: utf-8 -*-
"""Latest available period per series, straight from the source (ÉTAPE 2,
FRAÎCHEUR DU DATASET). Run before the line-by-line audit and before deploying
any reserve piece: if the source has a newer vintage than the CSV, the CSV is
stale and the audit's green marks mean nothing.

Cycle 21 lesson: a reserve CSV labelled "OECD 2024" was deployed in September
2026 when OECD had published 2025 for all three series, and the 2024 values
themselves had been revised (Mexico wage -15%). Nobody had asked the source.

Usage (library):
    from dataset_freshness import oecd_latest, fred_latest
    info = oecd_latest('OECD.ELS.SAE,DSD_EARNINGS@AV_AN_WAGE,1.0', PRICE_BASE='V')
    info['latest']            # '2025'
    info['by_area']['MEX']    # '2025'
    fred_latest('CPIAUCSL')   # ('2026-08-01', 322.1)

    economist_bigmac()        # {'latest': '2026-07-01', 'dates': [...], 'rows': {iso3: row}}

Usage (CLI):
    python dataset_freshness.py oecd "OECD.ELS.SAE,DSD_EARNINGS@AV_AN_WAGE,1.0" PRICE_BASE=V
    python dataset_freshness.py oecd "OECD.CTP.TPS,DSD_TAX_WAGES_COMP@DF_TW_COMP" MEASURE=NPATR HOUSEHOLD_TYPE=S_C0
    python dataset_freshness.py fred CPIAUCSL
    python dataset_freshness.py bigmac

Second cycle-21 lesson (15/09/2026): freshness applies to EVERY input,
including the ones copied by hand into the build script. The 16 Big Mac
rows were pinned from the January 2026 release; The Economist had published
July 2026 (10 of 16 prices changed, Israel +15%) and nobody had asked the
file. A pinned value is a stale value waiting to happen: fetch, and pin only
the release DATE, never the numbers.

Notes on OECD SDMX (sdmx.oecd.org):
- the dataflow id is "AGENCY,DSD@DF,version"; the version may be omitted to get
  the latest (Taxing Wages moved to 2.1 in 2026, "1.0" then returned nothing);
- the c[REF_AREA]= filter is not honoured on every flow, so this pulls a short
  window (startPeriod = today - 3 years) and filters client-side.
"""
import csv
import datetime
import io
import sys

import requests

SDMX = 'https://sdmx.oecd.org/public/rest/data/'
FRED = 'https://fred.stlouisfed.org/graph/fredgraph.csv?id='


def oecd_rows(flow, years_back=3, timeout=180):
    start = datetime.date.today().year - years_back
    url = SDMX + flow + '/all?startPeriod=%d&format=csvfilewithlabels' % start
    r = requests.get(url, timeout=timeout)
    r.raise_for_status()
    text = r.content.decode('utf-8-sig')
    if text.startswith('NoRecordsFound') or text.startswith('NoResultsFound'):
        raise RuntimeError('no records for %s (wrong id or version? try without version)' % flow)
    return list(csv.DictReader(io.StringIO(text)))


def oecd_latest(flow, areas=None, **filters):
    """Latest TIME_PERIOD overall and per REF_AREA for rows matching filters
    (exact match on SDMX dimension codes, e.g. PRICE_BASE='V')."""
    rows = [r for r in oecd_rows(flow) if all(r.get(k) == v for k, v in filters.items())]
    if areas:
        rows = [r for r in rows if r.get('REF_AREA') in areas]
    by_area = {}
    for r in rows:
        a, t = r.get('REF_AREA'), r.get('TIME_PERIOD')
        if a and t and (a not in by_area or t > by_area[a]):
            by_area[a] = t
    latest = max(by_area.values()) if by_area else None
    lagging = sorted(a for a, t in by_area.items() if t != latest)
    return {'flow': flow, 'filters': filters, 'latest': latest, 'by_area': by_area,
            'lagging': lagging, 'n_rows': len(rows)}


BIGMAC = ('https://raw.githubusercontent.com/TheEconomist/big-mac-data/master/'
          'output-data/big-mac-full-index.csv')


def economist_bigmac(date=None, timeout=60):
    """The Economist Big Mac index, full file. Returns the release dates, the
    latest one, and the rows of `date` (default: latest) keyed by iso_a3.
    Columns: local_price, dollar_ex, dollar_price, ... Fails loudly if the
    file is unreachable: do not fall back to pinned numbers."""
    r = requests.get(BIGMAC, timeout=timeout)
    r.raise_for_status()
    rows = list(csv.DictReader(io.StringIO(r.text)))
    dates = sorted({x['date'] for x in rows})
    use = date or dates[-1]
    assert use in dates, 'no Big Mac release dated %s (have %s .. %s)' % (use, dates[0], dates[-1])
    picked = {x['iso_a3']: x for x in rows if x['date'] == use}
    return {'latest': dates[-1], 'date': use, 'dates': dates, 'rows': picked,
            'stale': use != dates[-1]}


def fred_latest(series_id, timeout=60):
    """(last observation date, value) of a FRED series, no API key needed."""
    r = requests.get(FRED + series_id, timeout=timeout)
    r.raise_for_status()
    rows = [ln for ln in csv.reader(io.StringIO(r.text)) if len(ln) == 2 and ln[1] not in ('.', '')]
    date, value = rows[-1]
    return date, float(value)


def _cli(argv):
    if len(argv) >= 2 and argv[1] == 'bigmac':
        info = economist_bigmac(argv[2] if len(argv) > 2 else None)
        print('bigmac  : latest release %s, %d countries%s'
              % (info['latest'], len(info['rows']), ' (STALE: using %s)' % info['date'] if info['stale'] else ''))
        return 0
    if len(argv) < 3 or argv[1] not in ('oecd', 'fred'):
        print(__doc__)
        return 2
    if argv[1] == 'fred':
        for sid in argv[2:]:
            print('%s: %s = %s' % ((sid,) + fred_latest(sid)))
        return 0
    flow = argv[2]
    filters = dict(a.split('=', 1) for a in argv[3:] if '=' in a)
    areas = None
    for a in argv[3:]:
        if a.startswith('areas:'):
            areas = set(a[6:].split(','))
    info = oecd_latest(flow, areas=areas, **filters)
    print('flow    : %s %s' % (flow, filters))
    print('latest  : %s (%d rows, %d areas)' % (info['latest'], info['n_rows'], len(info['by_area'])))
    if info['lagging']:
        print('lagging : %s' % ', '.join('%s=%s' % (a, info['by_area'][a]) for a in info['lagging']))
    else:
        print('lagging : none')
    return 0


if __name__ == '__main__':
    sys.exit(_cli(sys.argv))

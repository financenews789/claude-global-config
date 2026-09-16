#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Audit de fraicheur des datasets bruts Eco3min.

1. Recense les dataset_id des 8 pipelines (configs JSON + ids codes en dur :
   registry v2, classifier de regime, score).
2. Lit le meta JSON servi (wp-content/dataset-meta/[sousdossier/]{id}.json)
   -> generated_at, latest_date, observations.
3. Classe chaque id : OK / DELAI-NORMAL / A-VERIFIER / PIPELINE-MUET / 404,
   selon la frequence declaree et un delai tolere par frequence.
4. Ecrit un CSV complet + un resume Markdown.

Usage (depuis n'importe ou) :
  python audit_fraicheur.py --repo C:/Users/pauld/eco3min/eco3min-data --out audit.csv
Options :
  --today YYYY-MM-DD   date de reference (defaut : aujourd'hui)
  --pages datasets-inventaire.csv   croise avec l'inventaire des pages (optionnel)
"""
import argparse, csv, json, re, sys, time
import concurrent.futures as cf
from datetime import date, timedelta
from pathlib import Path

import requests

SITE = "https://eco3min.fr"

# Delai tolere entre latest_date et aujourd'hui, par frequence declaree.
# Au-dela -> A-VERIFIER. Calibre sur les delais de publication observes le
# 2026-09-15 (trimestriel : Z.1 ~10 semaines, GDP 2e estimation ~2 mois ;
# mensuel : IMF commodities, JOLTS, PCE, M3 ~ 6-8 semaines ; EIA electricite
# ~ 2,5 mois ; OCDE via FRED ~ 3 mois).
TOLERANCE_DAYS = {
    "daily": 14,
    "weekly": 21,
    "monthly": 90,
    "quarterly": 200,
    "annual": 500,
}
# Series dont la source publie structurellement tard : delai specifique.
SLOW_IDS = {
    "us-electricity-price-residential": 110,
    "us-electricity-price-commercial": 110,
    "us-electricity-price-industrial": 110,
    "japan-10y-government-bond-yield": 110,
    "uk-10y-government-bond-yield": 110,
    "germany-10y-government-bond-yield-fred": 110,
}
# Ids reserves, jamais servis (documente dans pipeline-eco3min).
KNOWN_404 = {"ted-spread"}


def load_registry(repo: Path):
    reg = []

    def cfg(name, pipe, sub):
        c = json.loads((repo / "config" / name).read_text(encoding="utf-8"))
        d = c.get("datasets", c)
        entries = d if isinstance(d, list) else [e for v in d.values() if isinstance(v, list) for e in v]
        for e in entries:
            reg.append(dict(pipeline=pipe, subdir=sub, id=e["id"], slug_en=e.get("slug_en", ""),
                            frequency=e.get("frequency", "")))

    cfg("datasets.json", "FRED", "")
    cfg("ecb_datasets.json", "ECB", "ecb")
    cfg("eia_datasets.json", "EIA", "eia")
    cfg("fr_datasets.json", "FR", "fr")
    cfg("article_datasets.json", "ARTICLES", "")
    src = (repo / "scripts" / "eco3min_updater_v2.py").read_text(encoding="utf-8")
    body = src[src.index("DATASET_REGISTRY = {"):]
    for m in re.finditer(r'^    "([a-z0-9-]+)": \{(.*?)^    \},', body, re.S | re.M):
        slug = re.search(r'"slug_en":\s*"([^"]+)"', m.group(2))
        freq = re.search(r'"frequency":\s*"([^"]+)"', m.group(2))
        reg.append(dict(pipeline="V2", subdir="", id=m.group(1), slug_en=slug.group(1) if slug else "",
                        frequency=freq.group(1) if freq else ""))
    for i in ["cfnai-national-activity-index", "trimmed-mean-pce-inflation", "euro-area-ciss-systemic-stress"]:
        reg.append(dict(pipeline="REGIME", subdir="", id=i, slug_en="", frequency="monthly"))
    reg.append(dict(pipeline="SCORE", subdir="", id="score-eco3min", slug_en="", frequency="monthly"))
    return reg


def fetch_meta(r):
    sub = f"{r['subdir']}/" if r["subdir"] else ""
    url = f"{SITE}/wp-content/dataset-meta/{sub}{r['id']}.json?nc={time.time()}"
    out = dict(r)
    try:
        resp = requests.get(url, timeout=40, headers={"User-Agent": "eco3min-audit/1.0", "Cache-Control": "no-cache"})
        out["http"] = resp.status_code
        if resp.status_code == 200:
            j = resp.json()
            ks = j.get("key_stats") or {}
            out.update(generated_at=(j.get("generated_at") or "")[:10], latest_date=ks.get("latest_date") or "",
                       latest_value=ks.get("latest_value", ""), observations=ks.get("observations", ""),
                       frequency=out["frequency"] or j.get("frequency", ""), slug_en=out["slug_en"] or j.get("slug_en", ""))
    except Exception as e:
        out["http"] = f"ERR {e}"
    return out


def classify(row, today):
    if row["id"] in KNOWN_404 and row.get("http") == 404:
        return "404-CONNU"
    if row.get("http") != 200:
        return "404"
    gen = row.get("generated_at") or ""
    if gen and (today - date.fromisoformat(gen)).days > 3:
        return "PIPELINE-MUET"   # le meta n'a pas ete regenere : dataset skippe ou en erreur
    ld = row.get("latest_date") or ""
    if not ld:
        return "META-VIDE"
    ld = ld[:10]
    if len(ld) == 7:          # pipeline articles : YYYY-MM tolere par le contrat
        ld += "-01"
    age = (today - date.fromisoformat(ld)).days
    tol = SLOW_IDS.get(row["id"]) or TOLERANCE_DAYS.get(row.get("frequency", ""), 75)
    if age <= tol:
        return "OK"
    if age <= tol * 1.5:
        return "DELAI-NORMAL?"
    return "A-VERIFIER"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--out", default="audit_fraicheur.csv")
    ap.add_argument("--today", default=date.today().isoformat())
    args = ap.parse_args()
    today = date.fromisoformat(args.today)
    reg = load_registry(Path(args.repo))
    with cf.ThreadPoolExecutor(12) as ex:
        rows = list(ex.map(fetch_meta, reg))
    for r in rows:
        r["statut"] = classify(r, today)
    cols = ["statut", "pipeline", "subdir", "id", "slug_en", "frequency", "http", "generated_at", "latest_date",
            "latest_value", "observations"]
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader(); w.writerows(rows)
    order = ["404", "META-VIDE", "PIPELINE-MUET", "A-VERIFIER", "DELAI-NORMAL?", "404-CONNU", "OK"]
    print(f"# Audit fraicheur {today} — {len(rows)} ids")
    for st in order:
        sel = [r for r in rows if r["statut"] == st]
        if not sel:
            continue
        print(f"\n## {st} ({len(sel)})")
        if st == "OK":
            continue
        for r in sorted(sel, key=lambda r: (r["pipeline"], r.get("latest_date") or "")):
            print(f"- {r['pipeline']:8} {r.get('frequency',''):9} {r['id']:44} latest={r.get('latest_date','')} gen={r.get('generated_at','')} obs={r.get('observations','')}")


if __name__ == "__main__":
    main()

# pipeline-eco3min — référence : pipelines config-driven, FRED (§3 : schéma datasets.json, piège de `calculation`, `yoy_inputs` / `input_scales` / `scale`) et ECB (§4 : schéma ecb_datasets.json, SDMX)

Extrait VERBATIM de SKILL.md (découpage du 17/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 3. Pipeline FRED — `eco3min_updater.py` (config-driven)

### 3.1 Schéma `config/datasets.json`
Top-level : `fred_api_key_env`, `output_dir`, `wp_meta_dir`, `wp_touch_url`, `wp_touch_secret_env`, `datasets:{simple:[],composite:[]}` (`wp_rest_url` et `update_schedules` sont vestigiaux).

**Entrée `simple`** :
```json
{
  "id": "us-unemployment-rate",
  "name": "US Unemployment Rate (1948–2026)",
  "slug_en": "us-unemployment-rate-dataset",
  "cluster": "labor",
  "frequency": "monthly",          // daily | weekly | monthly | quarterly
  "update_schedule": "monthly",    // vestigial
  "sources": [{"type": "fred", "series": "UNRATE"}],
  "variables": ["date", "unemployment_rate"],
  "unit": "%",
  "description": "…"
}
```
Le builder prend `sources[0].series` (premier source `type=="fred"`), resample selon `frequency`, nomme la colonne `variables[1]`. Si `variables[1]` finit par `_yoy`, calcule le YoY (12 pér. monthly, 4 quarterly, 1 sinon).

**Entrée `composite`** :
```json
{
  "id": "real-fed-funds-rate",
  "calculation": "FEDFUNDS - CPIAUCSL_YOY",   // voir 3.2 — pattern, pas formule exécutée
  "input_series": ["FEDFUNDS", "CPIAUCSL"],
  "variables": ["date", "fed_funds_rate", "cpi_yoy", "real_fed_funds"],
  ...
}
```

### 3.2 ⚠️ Le piège du champ `calculation`
`calculation` n'est **pas exécuté littéralement** : c'est une chaîne de documentation qui déclenche un **pattern matching grossier** dans `build_composite_dataset` :

| Si la chaîne contient… | Le builder fait… |
|---|---|
| `" - "` | `ser_0 − ser_1 − …` (soustraction en chaîne de tous les input_series) |
| `" / "` | `ser_0 / ser_1` (+ variante si `base_cpi` dans la chaîne → déflate par `ser_1/base`) |
| `"overlay"` ou `"direct"` | passe chaque `ser_i` dans une colonne `variables[1+i]` (multi-colonnes, pas de calcul) |
| sinon, 1 seul input | `ser_0` brut |

Conséquences : `"WILL5000PRFC / GDP * 100"` → le `* 100` est **ignoré** (seul `/` compte). `"M2SL_YOY_PCT"` → aucun pattern → passe `ser_0` brut, **pas** de YoY. Toujours vérifier que le CSV produit correspond à la formule annoncée.

### 3.2 bis Les trois champs qui rattrapent le pattern matching

`yoy_inputs`, `input_scales` et `scale` corrigent les limites les plus fréquentes du §3.2. Défauts no-op (`[]`, `[]` et `1`) : invisibles sur les entrées qui ne les portent pas.

| Champ | Effet | Quand il est indispensable |
|---|---|---|
| `yoy_inputs: ["SERIE", …]` | transforme ces `input_series` en variation YoY (%) **AVANT** le calcul, sur `_yoy_periods(freq)` (12 monthly, 4 quarterly, 52 weekly, 252 daily) | tout « taux nominal − inflation ». Sans lui, le pattern `" - "` soustrait l'**indice CPI brut** (~330) au lieu de l'inflation (~3) : c'est ce qui rend `real-fed-funds-rate`, `real-10y-treasury-yield`, `us-real-wages` justes. Rattrape aussi le cas à un seul input (`m2-growth-rate`, `calculation: "M2SL_YOY_PCT"`). |
| `input_scales: [f, f, …]` | multiplie **chaque input** par son facteur, juste après le fetch et **AVANT** le calcul. Liste positionnelle alignée sur `input_series` ; plus courte → complétée par des `1` | mélange d'unités de compte dans une **soustraction**. `net-liquidity-index` (`WALCL - WTREGEN - RRPONTSYD`) : WALCL et WTREGEN sont en **millions**, RRPONTSYD en **milliards** (source NY Fed, pas H.4.1) → `input_scales: [1, 1, 1000]`. Sans lui, le terme RRP est écrasé d'un facteur 1000 : au pic de décembre 2022, net liquidity sortait à 8,12 T$ au lieu de 5,57 T$, **+2 554 Md$ (+46 %)**, et le drainage du RRP — l'essentiel du signal — était invisible. |
| `scale: <float>` | multiplie la **colonne métrique dérivée** (`variables[-1]`) après calcul | homogénéiser les unités FRED. `$M / $B` → `scale: 0.1` pour sortir un % (`fed-balance-sheet-gdp`, `corporate-debt-gdp`) ; `$B / $B` → `scale: 100` (`us-interest-payments-gdp`). Existe aussi sur les entrées `simple`, appliqué à `variables[1]` (`us-initial-claims`, `scale: 0.001` → milliers). |

Règle de contrôle : si `unit` vaut `"%"` et que le calcul est un `" / "` entre deux séries de même unité, il **faut** un `scale: 100`. Son absence est un bug silencieux — le CSV sort un ratio (0.75) affiché comme un pourcentage.

**`scale` ne remplace jamais `input_scales`, et réciproquement.** `scale` est un facteur unique appliqué en sortie : il absorbe un décalage d'unité dans une **division** (`fed-balance-sheet-gdp`, `$M / $B` → `scale: 0.1`), parce que le facteur y est commun aux deux termes. Dans une **soustraction**, il rescale tous les termes ensemble et ne rattrape jamais un terme mal calibré — il faut normaliser en amont, input par input. Corollaire de contrat : `input_scales` corrige aussi la **colonne brute publiée** (`on_rrp` passe en millions, conforme au `unit` déclaré), ce que `scale` ne fait pas.

Règle de contrôle : dès qu'un composite en `" - "` mêle des séries en **niveau** (dollars, personnes, barils) plutôt qu'en points de %, relire l'unité FRED de **chaque** input (§7) avant de committer. Les cinq autres composites en `" - "` de `datasets.json` sont tous en points de % — le risque est concentré sur les séries de niveau.

Restent hors de portée de ces trois champs : pondération, mapping en régimes, transformation custom → **builder dédié** (§6), pas d'entrée composite JSON.

### 3.3 Ajouter un dataset FRED
1. Vérifier le `series_id` sur FRED (§7).
2. Ajouter l'entrée dans `simple` ou `composite`.
3. Ordonner `variables` avec la métrique dérivée **en dernier** (§2.3).
4. Tester : `python scripts/eco3min_updater.py --dataset {id} --no-touch`, vérifier le CSV.
5. Confirmer que l'id n'existe pas déjà ailleurs (§2.1, §10).

---

## 4. Pipeline ECB — `ecb_updater.py` (config-driven, SDMX)

### 4.1 Schéma `config/ecb_datasets.json`
Top-level : `api_base_url`, `output_dir` (`./output/datasets-ecb`), `wp_meta_dir` (`./output/meta-ecb`), `wp_touch_url`, `wp_touch_secret_env`, `datasets:{simple:[],composite:[]}`.

**Simple** : clés SDMX `ecb_dataflow` + `ecb_key`.
```json
{
  "id": "ecb-euro-short-term-rate",
  "slug_en": "euro-short-term-rate-dataset",
  "cluster": "interest-rates",
  "frequency": "daily",
  "ecb_dataflow": "EST",
  "ecb_key": "B.EU000A2X2A25.WT",
  "variables": ["date", "estr_rate"],
  "unit": "%",
  "source_label": "ECB (€STR)"
}
```
Le fetcher appelle `GET {api_base}/{dataflow}/{key}?format=csvdata`, lit `TIME_PERIOD`/`OBS_VALUE`, gère les formats de date `YYYY-MM-DD | YYYY-MM | YYYY-Www | YYYY-Qq`. Pas de clé API.

**Composite** : `input_datasets` (liste d'**ids de simples déjà déclarés**) + `calculation` (`" - "` ou `" / "` uniquement). Alignement par `merge_asof` backward (gère fréquences hétérogènes : taux quotidien vs inflation mensuelle).

### 4.2 Ajouter un dataset ECB
Trouver `dataflow`/`key` sur le ECB Data Portal (data-api.ecb.europa.eu) → entrée `simple`. Pour un spread/ratio : déclarer les deux simples puis une entrée `composite` avec `input_datasets` + `calculation`.

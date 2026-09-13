---
name: pipeline-eco3min
description: "Maintenance et évolution du pipeline de données Eco3min — les scripts qui génèrent les CSV/XLSX/JSON servis par les pages dataset. Trois pipelines : FRED (eco3min_updater.py + datasets.json), ECB (ecb_updater.py + ecb_datasets.json, SDMX), non-FRED (eco3min_updater_v2.py, registry + builders CODÉS EN DUR : CoinGecko, Shiller, World Bank, NY Fed, ENTSO-E, FAO, IMF), plus le composite pondéré score_eco3min.py en hook. Activer pour ajouter ou modifier un dataset, choisir où l'ajouter (config JSON vs builder code), créer un builder ou une source, déboguer un updater, faire évoluer les workflows, vérifier un series_id FRED, ou auditer la dette. Couvre config-driven vs code-driven, les invariants à ne jamais casser (dataset_id stable et unique par pipeline, date en 1re colonne, métrique en DERNIÈRE colonne, fichiers {id}.csv/.xlsx/.json, touch WP), les pièges du calcul composite, les fragilités des fetchers, le SFTP OVH. Couche DONNÉE en amont de production-dataset."
---

# Pipeline de données — Eco3min

> Ce skill couvre la **couche DONNÉE** : les scripts qui produisent les fichiers `{id}.csv`, `{id}.xlsx` et `{id}.json` servis sous `eco3min.fr/dataset/` et `wp-content/dataset-meta/`.
> La **couche PAGE** (rédaction du HTML qui consomme ces fichiers via les shortcodes) relève du skill `production-dataset`. Les deux skills partagent un **contrat** (§2) qu'aucun des deux ne doit casser unilatéralement.
>
> **Source de vérité = le code, pas ce skill.** Le pipeline doit évoluer. Ce skill fige les *invariants* et les *points d'extension* ; pour tout détail d'implémentation, relire la section concernée du script. Si une divergence apparaît entre ce skill et le code, le code gagne — et ce skill doit être patché.

---

## 0. Carte des pipelines (orientation)

Sept pipelines indépendants + un composite hooké. **Avant toute modif, identifier lequel.**

| Pipeline | Script | Workflow | Cron UTC | Config | Modèle d'extension | Clé |
|---|---|---|---|---|---|---|
| **FRED** | `eco3min_updater.py` | `update-datasets.yml` | 08:00 L–S | `config/datasets.json` | **config-driven** (entrée JSON) | `FRED_API_KEY` |
| **ECB** | `ecb_updater.py` | `ecb-update.yml` | 08:00 L–S | `config/ecb_datasets.json` | **config-driven** (entrée JSON) | aucune (SDMX public) |
| **Non-FRED** | `eco3min_updater_v2.py` | `update-datasets-v2.yml` | 09:30 L–S | `DATASET_REGISTRY` **dans le .py** | **code-driven** (builder + entrée registry) | `FRED_API_KEY` (composites mixtes) |
| **EIA** | `eia_updater.py` | `eia-update.yml` | 10:30 L–S | `config/eia_datasets.json` | **config-driven** (entrée JSON) | `EIA_API_KEY` |
| **FR** | `fr_updater.py` | `fr-update.yml` | 10:30 L–S | `config/fr_datasets.json` | **config-driven** (entrée JSON) | aucune (DBnomics public) |
| **Articles** | `eco3min_articles_updater.py` | `update-articles.yml` | 09:00 les 11–19 | `config/article_datasets.json` + registry `BUILDERS` | **hybride** : identité en JSON, schéma de colonnes en code | `FRED_API_KEY` |
| **Régime** | `regime_classifier.py` | `regime-update.yml` | 10:30 tous les jours | `config/thresholds.json` | **code-driven** (pas d'argparse) | `FRED_API_KEY` |
| **Score** (composite pondéré) | `score_eco3min.py` | via FRED workflow | 08:00 | module autonome | hook lazy-import dans `eco3min_updater.py` | `FRED_API_KEY` |

Sorties, par namespace SFTP :

- **`www/dataset` + `www/wp-content/dataset-meta`** ← FRED et non-FRED v2 (`output/datasets` + `output/meta`), score, articles (`output/articles` + `output/articles-meta`) et les 3 séries standalone du régime. **Namespace partagé par 5 pipelines** : c'est le seul endroit où une collision d'id est destructrice (§2.1).
- **`www/dataset/{ecb,eia,fr}`** ← ECB (`output/datasets-ecb`), EIA (`output/datasets-eia`), FR (`output/datasets-fr`), chacun avec son `www/wp-content/dataset-meta/{source}`. Namespaces isolés.
- **`www/wp-content/uploads/eco3min-data/`** ← `regime_current.json`, `regime_lookup.json`, `regime_history.csv/.xlsx`. Hors espace dataset, déployés fichier par fichier (pas de `put *`).

Volumétrie (audit du 2026-08-27) : FRED 108, ECB 25, FR 22, non-FRED v2 19, EIA 13, régime 3, articles 1, score 1 — **192 ids**, dont 129 dans le namespace partagé.

---

## 1. Où ajouter un dataset ? (arbre de décision)

C'est la première question, et elle détermine tout le reste.

1. **La donnée est une série FRED publique** (ou un composite construit uniquement à partir de séries FRED) → **`config/datasets.json`**, pas de code. Voir §3.
2. **La donnée vient de l'ECB** (SDMX) → **`config/ecb_datasets.json`**, pas de code. Voir §4.
3. **La donnée est un prix de l'énergie US publié par l'EIA** (carburants à la pompe, spots produits raffinés, électricité par secteur, utilisation des raffineries) → **`config/eia_datasets.json`**, pas de code. Même squelette config-driven que l'ECB (§4) ; clés d'entrée `eia_route`, `eia_series_id`, `eia_data_col`, `eia_frequency`. WTI, Brent et Henry Hub sont **exclus** de ce pipeline : déjà servis par FRED.
4. **La donnée est française et vit sur DBnomics** (INSEE, Banque de France : IPC, IRL, SMIC, OAT, taux de crédit, prix immobiliers) → **`config/fr_datasets.json`**, pas de code. Config-driven avec deux spécificités : entrées **bilingues** (`name_fr`, `slug_fr`), et `sources` = *liste* de segments DBnomics chaînés par `chain_mode` (`ratio` / `rebase`) pour recoller les changements de base. Chaque entrée porte `licence`, `licence_url` et `commercial_redistribution` — les remplir, c'est ce qui rend le CSV publiable (skill `sourcing-donnees-eco3min`).
5. **La donnée vient d'une autre source** (CoinGecko, Shiller, World Bank Pink Sheet, NY Fed, Damodaran, et les candidates : ENTSO-E, AGSI+, FAO, IMF, BIS…) **OU** est un composite mixant une source non-FRED avec du FRED → **builder Python + entrée `DATASET_REGISTRY`** dans `eco3min_updater_v2.py`. Voir §5.
6. **La donnée est un composite pondéré / scoré** (somme pondérée, mapping en régimes, logique non réductible à `A−B` ou `A/B`) → **module autonome + hook**, modèle `score_eco3min.py`. Voir §6.

**Deux pipelines ne servent pas une page dataset** au sens de `production-dataset`. Ne jamais y router un nouveau dataset par défaut :

- **Articles** — `eco3min_articles_updater.py` + `config/article_datasets.json`. Séries riches multi-colonnes consommées par une page ARTICLE, avec un schéma propre à l'article (une colonne textuelle `regime` est possible). La config ne porte que l'identité, le nom du builder et `metric_column` ; le schéma de colonnes est **codé en dur** dans le registry `BUILDERS`. Deux dérogations assumées au contrat §2 : `key_stats` est calculé sur `metric_column`, **pas** sur la dernière colonne, et la date peut être au format `YYYY-MM`. N'y aller que si la page consommatrice est un article.
- **Régime** — `regime_classifier.py` + `config/thresholds.json`. Le classificateur ; il exporte *en plus* 3 de ses séries d'input en datasets standalone (`cfnai-national-activity-index`, `trimmed-mean-pce-inflation`, `euro-area-ciss-systemic-stress`) via `_save_regime_series`, ids codés en dur. N'ajouter un dataset ici que si la série est déjà un input du classifier. Taxonomie et pages → skill `regime-classifier-eco3min`.
  ⚠️ Ce script écrit dans `output/datasets`, qui part en `put *` : **tout fichier déposé là devient public**. Les inputs sous licence tierce (ICE BofA, Wu-Xia) vont dans `fixtures/`, jamais dans `output/`.

**Cas limite fréquent — une série FRED dont le code n'est pas un ticker googlé** (café `PCOFFOTMUSDM`, fer `PIORECRUSDM`) : côté pipeline, c'est du **FRED simple → §3** (la nature de la source décide du pipeline). Côté page, c'est un Cas A' (concept en H1) → c'est le skill `production-dataset` qui gère ça, pas ici. Ne pas confondre les deux décisions.

---

## 2. Le contrat CSV/meta — invariants à ne JAMAIS casser

Les pages (skill `production-dataset`), les shortcodes WP et le pipeline dépendent tous de ces invariants. Les casser casse silencieusement le site.

### 2.1 Identifiants
- **`dataset_id` immuable.** Une fois publié, il ne change jamais (pages, shortcodes `dataset_id="…"`, fichiers `/dataset/{id}.csv`, liens internes en dépendent).
- **`dataset_id` unique sur l'ensemble des pipelines.** Le même id dans deux pipelines qui publient dans le même namespace = double production, le second run de la journée écrasant le premier. Un id appartient à **un seul** pipeline.
  Vérification concrète : **23 ids ne sont dans aucune config** — les 19 du `DATASET_REGISTRY` v2, les 3 du classifier de régime, `score-eco3min`. Grepper les JSON ne suffit donc pas, il faut aussi lire le code. ECB, EIA et FR ont leurs propres sous-dossiers : leurs ids ne peuvent entrer en collision qu'entre eux.
- **`dataset_id` ≠ `slug_en`.** L'id est court (`excess-cape-yield`), le slug est l'URL (`excess-cape-yield-dataset`). Le CSV/meta porte l'**id** ; la page vit sur le **slug**. Ne pas les confondre.

### 2.2 Fichiers produits (par dataset)
- `output/…/{id}.csv` + `output/…/{id}.xlsx` (même nom, même dossier, `engine="openpyxl"`)
- `output/meta/{id}.json`

### 2.3 Structure du CSV
- **`date` en première colonne** (les `save_dataset` réordonnent pour garantir ça). Format `YYYY-MM-DD`.
- **La métrique principale / dérivée en DERNIÈRE colonne.** `compute_key_stats` prend `val_cols[-1]` comme métrique de référence (latest_value, percentile, hi/lo). Si la headline n'est pas la dernière colonne, les key_stats portent sur la mauvaise série. Pour un composite, ordonner : `date, composante_1, composante_2, …, métrique_dérivée`.
  Deux dérogations explicites, à ne pas généraliser : le pipeline **articles** calcule `key_stats` sur `metric_column` déclaré en config (sa dernière colonne peut être non numérique), et `regime_history` est une table de classification multi-colonnes. Partout ailleurs, `[-1]` fait foi.

### 2.4 Structure du meta JSON
FRED & non-FRED produisent un bloc **`key_stats`** complet :
```json
{"id","name","slug_en","cluster","frequency","generated_at",
 "key_stats":{"latest_value","latest_date","current_percentile",
   "historical_average","historical_high","historical_high_date",
   "historical_low","historical_low_date","observations","unit"}}
```
ECB, EIA et FR produisent le **même bloc `key_stats` riche** (le `compute_key_stats` y est dupliqué à l'identique dans chaque updater — divergence de code, pas de contrat). Le score eco3min ajoute des champs custom (`latest_regime_id`, `latest_components`) **dans** `key_stats`. Le pipeline articles produit la même structure, calculée sur `metric_column`.

### 2.5 Touch WordPress
Après ≥1 dataset mis à jour, `POST {wp_touch_url}` avec `key=WP_TOUCH_SECRET` rafraîchit `dateModified`. `--no-touch` le désactive (test local). Ne pas retirer cet appel — c'est ce qui garde Google à jour.

---

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

---

## 5. Pipeline non-FRED — `eco3min_updater_v2.py` (code-driven)

### 5.1 Modèle : registry + builders, PAS de JSON
`CONFIG_PATH = config/datasets_v2.json` est défini mais **jamais chargé** (variable morte, §10). Tout vit dans le code :
- une **fonction `build_{id}(cfg, keys) -> DataFrame`** par dataset,
- une **entrée dans `DATASET_REGISTRY`** :
```python
"silver-price": {
    "builder": build_silver_price,
    "needs": [],                 # clés requises ; ["fred"] si le builder appelle FRED
    "name": "Silver Price History",
    "slug_en": "silver-price-history-dataset",
    "cluster": "commodities",
    "frequency": "daily",
    "unit": "USD/troy oz",
},
```
`needs` gate l'exécution : si une clé requise manque, le dataset est skippé. Le builder doit retourner un DataFrame `date` + colonnes (métrique principale en dernier, §2.3). Save + meta `key_stats` sont gérés par le `main()` commun.

### 5.2 Fetchers existants et leurs fragilités
| Source | Fetcher | Fragilité à connaître |
|---|---|---|
| World Bank Pink Sheet | `fetch_worldbank_pinksheet()` | **URL annuelle codée en dur** (2026 puis 2025 fallback) → à bumper chaque année. Détecte les colonnes gold/silver par nom. Cache global. |
| CoinGecko | `fetch_coingecko(coin_id, days=365)` | **365 jours max** sur l'API gratuite → BTC/ETH = 1 an glissant seulement, pas d'historique long. |
| Shiller | `fetch_shiller()` | **Scrape `shillerdata.com`** (regex sur les `<a href>` cherchant `ie_data`), fallback ancienne URL Yale. Indices de colonnes du workbook en dur. Cassable si le site change. |
| NY Fed ACM | `fetch_nyfed_term_premium()` | Indices de colonnes (`19`=10y, `11`=2y) en dur, `header=7`. Cassable si le fichier change de format. |
| FRED (composites mixtes) | `fetch_fred_series(series_id, key)` | Standard ; `needs:["fred"]` obligatoire dans le registry. |

### 5.3 Ajouter un dataset non-FRED simple
Écrire un fetcher (si nouvelle source) + un `build_{id}` qui retourne `date` + colonne(s) → entrée registry avec `needs` correct. Tester `--dataset {id} --no-touch`.

### 5.4 Ajouter une NOUVELLE FAMILLE de source (ENTSO-E, AGSI+, FAO, IMF, BIS, World Bank API…)
Décision :
- **Quelques datasets, API hétérogène, one-off** → rester en v2 : un fetcher + des builders + entrées registry. C'est le chemin par défaut pour la plupart des nouveaux de la roadmap.
- **Famille entière, API uniforme, beaucoup de datasets** (comme l'a été l'ECB SDMX) → créer un **pipeline dédié** : nouveau script `{source}_updater.py` config-driven + `config/{source}_datasets.json` + workflow `{source}-update.yml` + dossiers SFTP `www/dataset/{source}` et `dataset-meta/{source}` + cron décalé des autres. Réutiliser le squelette d'`ecb_updater.py` (fetcher + builders simple/composite + save/meta/touch + main).

Dans les deux cas : ne jamais réutiliser un `dataset_id` déjà pris (§2.1), respecter le contrat §2, ajouter le secret/clé éventuel aux workflows.

### 5.5 Sources sous licence
EPEX/Nord Pool (électricité), Caixin PMI, et autres flux payants/sous licence **ne sont pas redistribuables** en CSV public. Ne pas pipeliner avant résolution de la licence (cf. roadmap : statut 🔴).

---

## 6. Composite pondéré / scoré — modèle `score_eco3min.py`

Quand la logique dépasse `A−B` / `A/B` (pondération, mapping en régimes, percentile custom) : **module autonome** exposant `update(datasets_dir, meta_dir) -> dict`, avec son `compute`, son `build_meta` (format `key_stats` + champs custom), ses constantes (poids, seuils). Branché par **hook lazy-import** dans `eco3min_updater.py`, juste avant le log final :
```python
if args.all or args.dataset == "{id}":
    from {module} import update as update_{id}
    r = update_{id}(datasets_dir=output_dir, meta_dir=meta_dir)
    success += 1
```
Avantages : pas d'import au top (pas de dépendance dure), pas de modif de `datasets.json`, isolé et testable seul (`python scripts/{module}.py`). C'est le modèle pour tout indicateur propriétaire futur.

---

## 7. Vérifier un `series_id` FRED avant de l'ajouter

Beaucoup de codes de la roadmap sont **inférés** (statut 🟡) et peuvent ne pas exister. Avant d'ajouter une entrée :
- Vérifier `https://fred.stlouisfed.org/series/{CODE}` (ou `web_search` du code), confirmer existence, fréquence, profondeur d'historique, unité.
- Tester en isolation : `python scripts/eco3min_updater.py --dataset {id} --no-touch` → un DataFrame vide signale un code faux ou une série discontinue.
- Méfiance sur les codes OCDE/IMF mirror (`IRLTLT01..M156N`, `..CPIALLMINMEI`, `P..USDM`) : pattern plausible ≠ existence garantie. Café/cacao confirmés ; le reste à confirmer un par un.

---

## 8. Workflows GitHub Actions

Squelette commun (5 workflows : FRED, ECB, non-FRED, EIA, FR) : `schedule.cron` + `workflow_dispatch` (input optionnel `dataset`) → checkout → setup-python 3.11 → `pip install -r requirements*.txt` → run updater (`--dataset` si input, sinon `--all`) → list files → **SFTP via `sshpass` + `sftp`** (cd dossier serveur, lcd dossier output, `put *`) → job summary.

- FRED, non-FRED, articles et régime : `requirements.txt`. ECB : `requirements-ecb.txt`. EIA : `requirements-eia.txt`. FR : `requirements-fr.txt`.
- Secrets consommés : `FRED_API_KEY`, `EIA_API_KEY`, `WP_TOUCH_SECRET`, `FTP_HOST`, `FTP_USER`, `FTP_PASSWORD`.
- `timeout-minutes: 30` par job.
- **Deux workflows sortent du squelette.** `update-articles.yml` tourne sur une fenêtre mensuelle (`0 9 11-19 * *`), pas en cron quotidien. `regime-update.yml` n'utilise pas `sshpass` + `put *` mais `wlixcc/SFTP-Deploy-Action`, **un step par fichier** (13 steps) : ajouter une sortie au classifier impose d'ajouter ses 3 steps de déploiement à la main, sinon le fichier est produit en CI et jamais servi.
- Créneaux occupés : 08:00 (FRED, ECB), 09:30 (non-FRED), 10:30 (EIA, FR, régime), 09:00 les 11–19 (articles). **10:30 porte déjà trois jobs concurrents sur le même SFTP OVH** — un nouveau pipeline prend un créneau libre, et ce triplet mérite d'être étalé.

---

## 9. Test local (recette)

Toujours **depuis la racine du repo** : les configs portent des chemins relatifs (`./output/datasets`), un lancement depuis `scripts/` écrit à côté.

```bash
export FRED_API_KEY=xxxx          # non requis pour ECB ni FR
export EIA_API_KEY=xxxx           # EIA uniquement
python scripts/eco3min_updater.py          --dataset {id} --no-touch
python scripts/eco3min_updater_v2.py       --dataset {id} --no-touch   # ou --list
python scripts/ecb_updater.py              --dataset {id} --no-touch
python scripts/eia_updater.py              --dataset {id} --no-touch   # ou --list
python scripts/fr_updater.py               --dataset {id} --no-touch   # ou --list
python scripts/eco3min_articles_updater.py --dataset {id} --no-touch
python scripts/score_eco3min.py     # pas d'argparse : écrit toujours tout
python scripts/regime_classifier.py # pas d'argparse, ET touch WP non désactivable
```
Vérifier : `output/.../{id}.csv` (date 1re col, métrique dernière col), `.xlsx` présent, `output/meta/{id}.json` avec `key_stats` peuplé (pas `{"rows":0}` → sinon source vide / code faux). `--no-touch` évite de pinger WP en test.

---

## 10. Dette technique connue (à arbitrer, pas à figer)

1. **`datasets_v2.json` mort** (§5.1) : supprimer la variable ou réellement charger le fichier si on veut passer v2 en config-driven.
2. **CoinGecko 365 j** (§5.2) : historique court ; toute page « depuis 20xx » est fausse tant que l'historique long n'est pas stitché (CSV statique + API pour le récent).
3. **Fetchers à indices/URL en dur** (World Bank, Shiller, NY Fed, Damodaran) : surveiller, ce sont les premiers à casser sur changement amont.
4. **`compute_key_stats` dupliqué 5 fois** (FRED, ECB, EIA, FR, `_save_regime_series`) : les corps sont aujourd'hui identiques, rien ne garantit qu'ils le restent. Candidat à la remontée dans `eco3min_common.py`.
5. **`fixtures/` absent du repo et non suivi par git** : `regime_classifier.py` attend `bamlh0a0hym2_history.csv` et `wu_xia_history.csv` ; le classifier tourne donc en CI sans ces inputs sous licence.

Quand l'un de ces points est résolu, **mettre à jour ce skill et le README**.

---

## 11. Checklist avant de committer une modif pipeline

- [ ] Bon pipeline choisi (arbre §1) ; `dataset_id` unique sur les 7 pipelines (+ score) — dont les 23 ids qui ne vivent que dans le code (§2.1)
- [ ] `dataset_id` ≠ `slug_en` ; id stable (jamais renommé s'il existe déjà)
- [ ] CSV : `date` en 1re colonne, **métrique principale en DERNIÈRE colonne**
- [ ] Composite FRED/ECB/FR : la formule réelle correspond bien à un des patterns supportés (sinon builder dédié §6)
- [ ] Composite « taux − inflation » : `yoy_inputs` renseigné ; ratio annoncé en `%` : `scale` cohérent (§3.2 bis)
- [ ] Composite en `" - "` sur des séries de **niveau** : unité FRED de chaque input relue, `input_scales` posé si elles divergent (§3.2 bis)
- [ ] `variables` cohérent avec les colonnes produites ; `unit` renseigné
- [ ] FRED : `series_id` vérifié (§7) ; non-FRED : `needs` correct
- [ ] Testé en local `--no-touch` ; meta `key_stats` peuplé (pas `rows:0`)
- [ ] Nouveau secret/clé éventuel ajouté au workflow ; cron décalé si nouveau pipeline
- [ ] Contrat §2 respecté (la page `production-dataset` doit pouvoir consommer le fichier)
- [ ] Si la modif touche un point de dette §10, README + ce skill mis à jour
# pipeline-eco3min — référence : pipeline non-FRED v2 (§5 : registry + builders, fetchers et fragilités, nouvelle famille de source, sources sous licence) et composite pondéré / scoré (§6)

Extrait VERBATIM de SKILL.md (découpage du 17/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

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
| ~~CoinGecko~~ → FRED Coinbase (17/09/2026) | `_fred_daily_price("CBBTCUSD" / "CBETHUSD", …)` | `fetch_coingecko` retiré : les API Terms CoinGecko interdisent la redistribution (sourcing-donnees-eco3min, `references/03`). BTC depuis 2014-12, ETH depuis 2016-05, `needs: ["fred"]`, `rights: coinbase-btc / coinbase-eth`. La ligne du dessus est conservée pour l'historique. |
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

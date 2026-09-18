---
name: pipeline-eco3min
description: "Maintenance et évolution du pipeline de données Eco3min (repo eco3min-data) : les scripts GitHub Actions qui génèrent les CSV / XLSX / JSON servis sous eco3min.fr/dataset/ et wp-content/dataset-meta/, en amont des pages dataset. Sept pipelines plus un composite hooké : FRED (eco3min_updater.py + config/datasets.json, entrées simple et composite), ECB (ecb_updater.py + ecb_datasets.json, SDMX), non-FRED v2 (eco3min_updater_v2.py, DATASET_REGISTRY + builders codés en dur : World Bank Pink Sheet, Shiller, NY Fed, FRED Coinbase CBBTCUSD / CBETHUSD, composites mixtes), EIA, FR (DBnomics, INSEE, Banque de France), articles, régime, score_eco3min.py. Activer pour « ajoute un dataset », « nouveau dataset », « où je mets cette série », « config JSON ou builder ? », « crée un builder », « nouvelle source », « nouvelle famille de source », « le CSV est vide », « rows:0 », « key_stats faux », « le workflow a échoué », « relance le workflow », « workflow_dispatch », « series_id », « calculation », « yoy_inputs », « input_scales », « scale », « dataset_id », « slug_en », « needs », « rights », « transform », « source_rights.py », « SERIES_RIGHTS », « onglet Source », « --no-touch », « --list », « SFTP OVH », « cron », « dette pipeline », « datasets_v2.json », « compute_key_stats dupliqué ». SKILL.md = colonne vertébrale (§0 carte des pipelines et namespaces SFTP, §1 arbre de décision, §2 contrat CSV / meta verbatim plus §2.6 droits de la source ajouté le 17/09/2026, règles bloquantes de §3 à §9 sous leurs numéros d'origine, §7 vérification d'un series_id, §10 dette technique, §11 checklist verbatim) ; références dans references/ (à lire quand la section le dit) : 01 pipelines config-driven FRED et ECB (schémas JSON complets, table des patterns de calculation, table yoy_inputs / input_scales / scale, SDMX), 02 pipeline v2 et composite scoré (exemple de registry, table des fetchers et de leurs fragilités, nouvelle famille de source, sources sous licence, hook lazy-import), 03 workflows GitHub Actions et recette de test local ; pas de scripts/ (les gardes vivent dans le repo lui-même). Doctrines : source de vérité = le code, pas ce skill, et le skill se patche quand ils divergent ; identifier le pipeline avant toute modif, un dataset_id appartient à un seul pipeline et 23 ids ne vivent que dans le code ; dataset_id immuable une fois publié et distinct du slug_en ; date en première colonne, métrique principale en DERNIÈRE colonne car compute_key_stats lit val_cols[-1] ; calculation n'est pas exécuté, c'est un pattern matching sur « - », « / », overlay / direct, donc « * 100 » est ignoré et un ratio annoncé en % exige scale: 100 ; « taux − inflation » exige yoy_inputs sinon on soustrait l'indice CPI brut ; soustraction de séries en niveau → input_scales, scale ne le remplace jamais ; pondération ou mapping en régimes → module autonome + hook, jamais une entrée composite JSON ; series_id FRED vérifié sur la page FRED avant toute entrée, jamais de mémoire ; série sous conditions → clé rights (v2) ou SERIES_RIGHTS (FRED) ET miroir eco3_source_rights() dans les snippets 36 et 114, jamais CC BY par défaut, statut lu par fred_license.py, pre-approval = pas d'entrée ; le name du registry nomme la source réelle ; output/datasets part en put * donc tout fichier déposé là est public, les inputs sous licence vont dans fixtures/ ; --no-touch sur tout run local, toujours depuis la racine du repo ; 10:30 UTC porte déjà trois jobs sur le même SFTP. Hors périmètre : la page HTML qui consomme le fichier (H1, cas A / A' / B, 18 blocs) → production-dataset ; la légalité de la source et les routes d'accès → sourcing-donnees-eco3min ; le classificateur de régime → regime-classifier-eco3min. Combiner avec production-dataset, sourcing-donnees-eco3min, regime-classifier-eco3min, revue-datasets-perimes, archi-eco3min."
---

# Pipeline de données — Eco3min

> Ce skill couvre la **couche DONNÉE** : les scripts qui produisent les fichiers `{id}.csv`, `{id}.xlsx` et `{id}.json` servis sous `eco3min.fr/dataset/` et `wp-content/dataset-meta/`.
> La **couche PAGE** (rédaction du HTML qui consomme ces fichiers via les shortcodes) relève du skill `production-dataset`. Les deux skills partagent un **contrat** (§2) qu'aucun des deux ne doit casser unilatéralement.
>
> **Source de vérité = le code, pas ce skill.** Le pipeline doit évoluer. Ce skill fige les *invariants* et les *points d'extension* ; pour tout détail d'implémentation, relire la section concernée du script. Si une divergence apparaît entre ce skill et le code, le code gagne — et ce skill doit être patché.

---

## COMMENT LIRE CE SKILL (découpage du 17/09/2026)

Ce fichier est la colonne vertébrale : la carte des pipelines, l'arbre de décision, le contrat CSV / meta, chaque règle BLOQUANTE de §3 à §9 sous son numéro d'origine, la vérification d'un `series_id`, la dette technique et la checklist. Les schémas JSON, les tables de patterns et de fetchers, les exemples de code et la recette de test ont été déplacés VERBATIM dans `references/` et font foi au même titre que ce fichier ; ils ne servent qu'au moment où l'on touche le pipeline concerné. Chaque section ci-dessous nomme le fichier à lire ; le lire est obligatoire au moment indiqué, pas facultatif. Pas de `scripts/` : les gardes sont dans le repo `eco3min-data` lui-même.

| Fichier | Contenu | À lire |
|---|---|---|
| `references/01-pipelines-config-driven-fred-ecb.md` | §3 FRED : schéma complet de `datasets.json` (simple, composite), table des patterns de `calculation`, table `yoy_inputs` / `input_scales` / `scale` avec leurs cas, procédure §3.3 ; §4 ECB : schéma `ecb_datasets.json`, SDMX, composites par `input_datasets` | avant d'ajouter ou de modifier une entrée de `datasets.json` ou `ecb_datasets.json`, et avant de diagnostiquer un composite FRED faux |
| `references/02-pipeline-v2-et-composite-score.md` | §5 v2 : exemple d'entrée `DATASET_REGISTRY`, table des fetchers et de leurs fragilités, ajout simple, nouvelle famille de source, sources sous licence ; §6 : modèle `score_eco3min.py` et hook lazy-import | avant d'écrire ou modifier un builder, avant de choisir entre v2 et pipeline dédié, avant tout indicateur pondéré |
| `references/03-workflows-et-test-local.md` | §8 : squelette des workflows, requirements par pipeline, secrets, les deux workflows hors squelette, créneaux cron ; §9 : commandes de test local par pipeline et ce qu'il faut vérifier | avant de toucher un `.github/workflows/*.yml`, d'ajouter un secret, et avant tout run local |

---

## 0. Carte des pipelines (orientation)

Sept pipelines indépendants + un composite hooké. **Avant toute modif, identifier lequel.**

| Pipeline | Script | Workflow | Cron UTC | Config | Modèle d'extension | Clé |
|---|---|---|---|---|---|---|
| **FRED** | `eco3min_updater.py` | `update-datasets.yml` | 08:00 L–S | `config/datasets.json` | **config-driven** (entrée JSON) | `FRED_API_KEY` |
| **ECB** | `ecb_updater.py` | `ecb-update.yml` | 08:00 L–S | `config/ecb_datasets.json` | **config-driven** (entrée JSON) | aucune (SDMX public) |
| **Non-FRED** | `eco3min_updater_v2.py` | `update-datasets-v2.yml` | 09:30 L–S | `DATASET_REGISTRY` **dans le .py** | **code-driven** (builder + entrée registry) | `FRED_API_KEY` (composites mixtes) |
| **EIA** | `eia_updater.py` | `eia-update.yml` | 10:30 L–S | `config/eia_datasets.json` | **config-driven** (entrée JSON) | `EIA_API_KEY` |
| **FR** | `fr_updater.py` | `fr-update.yml` | 10:30 L–S | `config/fr_datasets.json` | **config-driven** (entrée JSON) + section `custom` (identité en JSON, `builder` nommé dans `fr_builders_*.py`, depuis le 18/09/2026) | aucune (DBnomics public ; Webstat si `WEBSTAT_API_KEY`) |
| **Articles** | `eco3min_articles_updater.py` | `update-articles.yml` | 09:00 les 11–19 | `config/article_datasets.json` + registry `BUILDERS` | **hybride** : identité en JSON, schéma de colonnes en code | `FRED_API_KEY` |
| **Régime** | `regime_classifier.py` | `regime-update.yml` | 10:30 tous les jours | `config/thresholds.json` | **code-driven** (pas d'argparse) | `FRED_API_KEY` |
| **Score** (composite pondéré) | `score_eco3min.py` | via FRED workflow | 08:00 | module autonome | hook lazy-import dans `eco3min_updater.py` | `FRED_API_KEY` |

Sorties, par namespace SFTP :

- **`www/dataset` + `www/wp-content/dataset-meta`** ← FRED et non-FRED v2 (`output/datasets` + `output/meta`), score, articles (`output/articles` + `output/articles-meta`) et les 3 séries standalone du régime. **Namespace partagé par 5 pipelines** : c'est le seul endroit où une collision d'id est destructrice (§2.1).
- **`www/dataset/{ecb,eia,fr}`** ← ECB (`output/datasets-ecb`), EIA (`output/datasets-eia`), FR (`output/datasets-fr`), chacun avec son `www/wp-content/dataset-meta/{source}`. Namespaces isolés.
- **`www/wp-content/uploads/eco3min-data/`** ← `regime_current.json`, `regime_lookup.json`, `regime_history.csv/.xlsx`. Hors espace dataset, déployés fichier par fichier (pas de `put *`).

Volumétrie (audit du 2026-08-27) : FRED 108, ECB 25, FR 22, non-FRED v2 19, EIA 13, régime 3, articles 1, score 1 — **192 ids**, dont 129 dans le namespace partagé. FR = 25 depuis le 18/09/2026 (3 ids `custom`).

---

## 1. Où ajouter un dataset ? (arbre de décision)

C'est la première question, et elle détermine tout le reste.

1. **La donnée est une série FRED publique** (ou un composite construit uniquement à partir de séries FRED) → **`config/datasets.json`**, pas de code. Voir §3.
2. **La donnée vient de l'ECB** (SDMX) → **`config/ecb_datasets.json`**, pas de code. Voir §4.
3. **La donnée est un prix de l'énergie US publié par l'EIA** (carburants à la pompe, spots produits raffinés, électricité par secteur, utilisation des raffineries) → **`config/eia_datasets.json`**, pas de code. Même squelette config-driven que l'ECB (§4) ; clés d'entrée `eia_route`, `eia_series_id`, `eia_data_col`, `eia_frequency`. WTI, Brent et Henry Hub sont **exclus** de ce pipeline : déjà servis par FRED.
4. **La donnée est française et vit sur DBnomics** (INSEE, Banque de France : IPC, IRL, SMIC, OAT, taux de crédit, prix immobiliers) → **`config/fr_datasets.json`**, pas de code. Config-driven avec deux spécificités : entrées **bilingues** (`name_fr`, `slug_fr`), et `sources` = *liste* de segments DBnomics chaînés par `chain_mode` (`ratio` / `rebase`) pour recoller les changements de base. Chaque entrée porte `licence`, `licence_url` et `commercial_redistribution` — les remplir, c'est ce qui rend le CSV publiable (skill `sourcing-donnees-eco3min`).
   **4 bis. La donnée est française mais ne se réduit ni à un segment DBnomics ni à un `A−B` / `A/B`** (recollage de sources hétérogènes, table de paliers, calcul annuel, constante réglementaire antérieure à la série officielle) → **section `custom` de `fr_datasets.json` + builder codé** dans `scripts/fr_builders_<sujet>.py`, exposé par un dict `BUILDERS = {"nom": fonction}` et nommé par la clé `"builder"` de l'entrée ; `fr_updater.custom_builder()` l'importe paresseusement (liste `CUSTOM_BUILDER_MODULES`). L'entrée garde l'identité et la provenance en JSON (`sources`, `licence`, `attribution`, `provenance_notes`) : c'est le modèle hybride du pipeline articles, dans le namespace `/dataset/fr/`. Signature `build(fetcher, cfg) -> DataFrame` ; le fetcher est le `DBnomicsFetcher` du pipeline (Webstat avec clé, DBnomics sinon), donc une source BdF s'y lit sans nouveau code. **Ne pas router une série française vers v2** pour la seule raison qu'elle demande un builder : v2 vit dans le namespace partagé `www/dataset`, sans préfixe `fr-`, hors du snippet 224. Premier cas (18/09/2026, S009) : `fr-livret-a-rate`, `fr-livret-a-rate-changes`, `fr-livret-a-real-return` dans `fr_builders_livret_a.py` (BdF MIR1 + palier IPP 1960-65 + JORF, inflation INSEE 011813530 lue sur l'API BDM SDMX sans clé — l'INSEE n'offre rien d'annuel avant 1996 sur DBnomics).
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

### 2.6 Droits de la source amont (ajout du 17/09/2026)

Le contrat porte aussi la licence. Une série amont sous conditions (FMI, OCDE, BoE, Coinbase via FRED, toute série FRED « copyrighted: citation required ») ne sort jamais en CC BY 4.0 par défaut : `scripts/source_rights.py` porte `SOURCE_RIGHTS` (clé → holder, attribution, terms_url, notice) et `SERIES_RIGHTS` (series_id FRED → clé). Mécanique :
- **FRED** (`eco3min_updater.py`) : `rights_for_config()` lit les `sources[].series` de l'entrée ; une série présente dans `SERIES_RIGHTS` déclenche l'onglet « Source » du XLSX et le bloc `source_rights` du meta JSON. Rien à déclarer dans `datasets.json`, mais **toute nouvelle série sous conditions doit entrer dans `SERIES_RIGHTS`**, liste explicite, jamais un motif.
- **v2** (`eco3min_updater_v2.py`) : clé `"rights": "<clé>"` dans l'entrée `DATASET_REGISTRY`, plus `"transform": "…"` quand le composite transforme la série (condition d'intégrité du FMI, cf. `copper-gold-ratio`). Sans clé, le fichier part sans onglet Source.
- **Site** : la même clé doit exister dans `eco3_source_rights()` des snippets 36 et 114 (repo `eco3min-wp`), sinon le JSON-LD de la page annonce CC BY 4.0 à tort. Les deux registres sont miroirs, à faire évoluer ensemble (22 pages corrigées le 16/09/2026 pour cette raison).
- Le statut d'une série FRED se lit par script avant toute entrée : `~/.claude/skills/sourcing-donnees-eco3min/scripts/fred_license.py` (trois niveaux ; « pre-approval required » = pas d'entrée du tout, re-sourcer). Doctrine, trois usages d'une donnée et table des sources hors FRED : `sourcing-donnees-eco3min`, section « Cas FRED » et `references/03-licences-sources-pipeline.md`.
- Le `name` du registry nomme la source réelle : « Gold Price History (World Bank Pink Sheet) », pas « (LBMA) » ; « Coinbase via FRED », pas CoinGecko (corrigés le 17/09/2026).
- État au 17/09/2026 : clés `imf-pcps`, `imf-ifs`, `oecd-mei`, `coinbase-btc`, `coinbase-eth`, `boe-ogl` ; 29 séries FRED dans `SERIES_RIGHTS`. Registry v2 : 20 ids (le §0 en compte 19, audit du 27/08). `gold-price` et `silver-price` sont mensuels depuis le commit c6e293f ; l'exemple §5.1 de la référence 02, qui dit `daily`, lui est antérieur.

---

## 3. Pipeline FRED — `eco3min_updater.py` (config-driven) — lire `references/01-pipelines-config-driven-fred-ecb.md` avant toute entrée de `datasets.json`

Bloquant :
- §3.1 Le builder prend `sources[0].series` (premier source `type=="fred"`), resample selon `frequency`, nomme la colonne `variables[1]`. Si `variables[1]` finit par `_yoy`, calcule le YoY (12 pér. monthly, 4 quarterly, 1 sinon).
- §3.2 `calculation` n'est **pas exécuté littéralement** : c'est une chaîne de documentation qui déclenche un **pattern matching grossier** dans `build_composite_dataset` :
  Conséquences : `"WILL5000PRFC / GDP * 100"` → le `* 100` est **ignoré** (seul `/` compte). `"M2SL_YOY_PCT"` → aucun pattern → passe `ser_0` brut, **pas** de YoY. Toujours vérifier que le CSV produit correspond à la formule annoncée.
- §3.2 bis `yoy_inputs`, `input_scales` et `scale` corrigent les limites les plus fréquentes du §3.2. Défauts no-op (`[]`, `[]` et `1`) : invisibles sur les entrées qui ne les portent pas.
  Règle de contrôle : si `unit` vaut `"%"` et que le calcul est un `" / "` entre deux séries de même unité, il **faut** un `scale: 100`. Son absence est un bug silencieux — le CSV sort un ratio (0.75) affiché comme un pourcentage.
  **`scale` ne remplace jamais `input_scales`, et réciproquement.** `scale` est un facteur unique appliqué en sortie : il absorbe un décalage d'unité dans une **division** (`fed-balance-sheet-gdp`, `$M / $B` → `scale: 0.1`), parce que le facteur y est commun aux deux termes. Dans une **soustraction**, il rescale tous les termes ensemble et ne rattrape jamais un terme mal calibré — il faut normaliser en amont, input par input. Corollaire de contrat : `input_scales` corrige aussi la **colonne brute publiée** (`on_rrp` passe en millions, conforme au `unit` déclaré), ce que `scale` ne fait pas.
  Règle de contrôle : dès qu'un composite en `" - "` mêle des séries en **niveau** (dollars, personnes, barils) plutôt qu'en points de %, relire l'unité FRED de **chaque** input (§7) avant de committer. Les cinq autres composites en `" - "` de `datasets.json` sont tous en points de % — le risque est concentré sur les séries de niveau.
  Restent hors de portée de ces trois champs : pondération, mapping en régimes, transformation custom → **builder dédié** (§6), pas d'entrée composite JSON.
- §3.3 Ajouter un dataset FRED :
  1. Vérifier le `series_id` sur FRED (§7).
  2. Ajouter l'entrée dans `simple` ou `composite`.
  3. Ordonner `variables` avec la métrique dérivée **en dernier** (§2.3).
  4. Tester : `python scripts/eco3min_updater.py --dataset {id} --no-touch`, vérifier le CSV.
  5. Confirmer que l'id n'existe pas déjà ailleurs (§2.1, §10).

---

## 4. Pipeline ECB — `ecb_updater.py` (config-driven, SDMX) — lire `references/01-pipelines-config-driven-fred-ecb.md` avant toute entrée de `ecb_datasets.json`

Bloquant :
- §4.1 Le fetcher appelle `GET {api_base}/{dataflow}/{key}?format=csvdata`, lit `TIME_PERIOD`/`OBS_VALUE`, gère les formats de date `YYYY-MM-DD | YYYY-MM | YYYY-Www | YYYY-Qq`. Pas de clé API.
  **Composite** : `input_datasets` (liste d'**ids de simples déjà déclarés**) + `calculation` (`" - "` ou `" / "` uniquement). Alignement par `merge_asof` backward (gère fréquences hétérogènes : taux quotidien vs inflation mensuelle).
- §4.2 Trouver `dataflow`/`key` sur le ECB Data Portal (data-api.ecb.europa.eu) → entrée `simple`. Pour un spread/ratio : déclarer les deux simples puis une entrée `composite` avec `input_datasets` + `calculation`.

---

## 5. Pipeline non-FRED — `eco3min_updater_v2.py` (code-driven) — lire `references/02-pipeline-v2-et-composite-score.md` avant d'écrire ou modifier un builder

Bloquant :
- §5.1 `CONFIG_PATH = config/datasets_v2.json` est défini mais **jamais chargé** (variable morte, §10). Tout vit dans le code : Une **fonction `build_{id}(cfg, keys) -> DataFrame`** par dataset et une **entrée dans `DATASET_REGISTRY`** (exemple complet dans la référence). `needs` gate l'exécution : si une clé requise manque, le dataset est skippé. Le builder doit retourner un DataFrame `date` + colonnes (métrique principale en dernier, §2.3). Save + meta `key_stats` sont gérés par le `main()` commun.
- §5.2 Chaque fetcher a une fragilité connue (URL annuelle du Pink Sheet, scrape de shillerdata.com, indices de colonnes NY Fed en dur) : table dans la référence, à relire avant de toucher un fetcher.
- §5.3 Écrire un fetcher (si nouvelle source) + un `build_{id}` qui retourne `date` + colonne(s) → entrée registry avec `needs` correct. Tester `--dataset {id} --no-touch`.
- §5.4 Nouvelle famille de source :
  - **Quelques datasets, API hétérogène, one-off** → rester en v2 : un fetcher + des builders + entrées registry. C'est le chemin par défaut pour la plupart des nouveaux de la roadmap.
  - **Famille entière, API uniforme, beaucoup de datasets** (comme l'a été l'ECB SDMX) → créer un **pipeline dédié** : nouveau script `{source}_updater.py` config-driven + `config/{source}_datasets.json` + workflow `{source}-update.yml` + dossiers SFTP `www/dataset/{source}` et `dataset-meta/{source}` + cron décalé des autres. Réutiliser le squelette d'`ecb_updater.py` (fetcher + builders simple/composite + save/meta/touch + main).
  Dans les deux cas : ne jamais réutiliser un `dataset_id` déjà pris (§2.1), respecter le contrat §2, ajouter le secret/clé éventuel aux workflows.
- §5.5 EPEX/Nord Pool (électricité), Caixin PMI, et autres flux payants/sous licence **ne sont pas redistribuables** en CSV public. Ne pas pipeliner avant résolution de la licence (cf. roadmap : statut 🔴).

---

## 6. Composite pondéré / scoré — modèle `score_eco3min.py` — lire `references/02-pipeline-v2-et-composite-score.md` avant tout indicateur pondéré

Bloquant :
- Quand la logique dépasse `A−B` / `A/B` (pondération, mapping en régimes, percentile custom) : **module autonome** exposant `update(datasets_dir, meta_dir) -> dict`, avec son `compute`, son `build_meta` (format `key_stats` + champs custom), ses constantes (poids, seuils). Branché par **hook lazy-import** dans `eco3min_updater.py`, juste avant le log final : Squelette du hook dans la référence.

---

## 7. Vérifier un `series_id` FRED avant de l'ajouter

Beaucoup de codes de la roadmap sont **inférés** (statut 🟡) et peuvent ne pas exister. Avant d'ajouter une entrée :
- Vérifier `https://fred.stlouisfed.org/series/{CODE}` (ou `web_search` du code), confirmer existence, fréquence, profondeur d'historique, unité.
- Tester en isolation : `python scripts/eco3min_updater.py --dataset {id} --no-touch` → un DataFrame vide signale un code faux ou une série discontinue.
- Méfiance sur les codes OCDE/IMF mirror (`IRLTLT01..M156N`, `..CPIALLMINMEI`, `P..USDM`) : pattern plausible ≠ existence garantie. Café/cacao confirmés ; le reste à confirmer un par un.

---

## 8. Workflows GitHub Actions — lire `references/03-workflows-et-test-local.md` avant de toucher un workflow ou un secret

Bloquant :
- Squelette commun (5 workflows : FRED, ECB, non-FRED, EIA, FR) : `schedule.cron` + `workflow_dispatch` (input optionnel `dataset`) → checkout → setup-python 3.11 → `pip install -r requirements*.txt` → run updater (`--dataset` si input, sinon `--all`) → list files → **SFTP via `sshpass` + `sftp`** (cd dossier serveur, lcd dossier output, `put *`) → job summary.
- Secrets consommés : `FRED_API_KEY`, `EIA_API_KEY`, `WP_TOUCH_SECRET`, `FTP_HOST`, `FTP_USER`, `FTP_PASSWORD`.
- **Deux workflows sortent du squelette.** `update-articles.yml` tourne sur une fenêtre mensuelle (`0 9 11-19 * *`), pas en cron quotidien. `regime-update.yml` n'utilise pas `sshpass` + `put *` mais `wlixcc/SFTP-Deploy-Action`, **un step par fichier** (13 steps) : ajouter une sortie au classifier impose d'ajouter ses 3 steps de déploiement à la main, sinon le fichier est produit en CI et jamais servi.
- Créneaux occupés : 08:00 (FRED, ECB), 09:30 (non-FRED), 10:30 (EIA, FR, régime), 09:00 les 11–19 (articles). **10:30 porte déjà trois jobs concurrents sur le même SFTP OVH** — un nouveau pipeline prend un créneau libre, et ce triplet mérite d'être étalé.

---

## 9. Test local (recette) — lire `references/03-workflows-et-test-local.md` avant tout run local

Bloquant :
- Toujours **depuis la racine du repo** : les configs portent des chemins relatifs (`./output/datasets`), un lancement depuis `scripts/` écrit à côté.
- Toujours `--no-touch` ; `score_eco3min.py` et `regime_classifier.py` n'ont pas d'argparse et le classifier touche WP à chaque exécution.
- Vérifier : `output/.../{id}.csv` (date 1re col, métrique dernière col), `.xlsx` présent, `output/meta/{id}.json` avec `key_stats` peuplé (pas `{"rows":0}` → sinon source vide / code faux). `--no-touch` évite de pinger WP en test.

---

## 10. Dette technique connue (à arbitrer, pas à figer)

1. **`datasets_v2.json` mort** (§5.1) : supprimer la variable ou réellement charger le fichier si on veut passer v2 en config-driven.
2. **CoinGecko 365 j** (§5.2) : historique court ; toute page « depuis 20xx » est fausse tant que l'historique long n'est pas stitché (CSV statique + API pour le récent). **Réglé le 17/09/2026** par la bascule sur FRED CBBTCUSD / CBETHUSD (§5.2).
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
- [ ] FR `custom` : `builder` présent dans le `BUILDERS` de son module, module listé dans `CUSTOM_BUILDER_MODULES`, `sources` renseigné pour la provenance, `--list` l'affiche
- [ ] Testé en local `--no-touch` ; meta `key_stats` peuplé (pas `rows:0`)
- [ ] Nouveau secret/clé éventuel ajouté au workflow ; cron décalé si nouveau pipeline
- [ ] Contrat §2 respecté (la page `production-dataset` doit pouvoir consommer le fichier)
- [ ] Si la modif touche un point de dette §10, README + ce skill mis à jour

Ajout du 17/09/2026, s'ajoute à la checklist ci-dessus :

- [ ] Série amont sous conditions : clé `rights` posée (v2) ou `series_id` ajouté à `SERIES_RIGHTS` (FRED), ET clé miroir dans `eco3_source_rights()` des snippets 36 et 114 (§2.6)
- [ ] Nouvelle série FRED : statut lu par `fred_license.py` ; « pre-approval required » → pas d'entrée, re-sourcer
- [ ] Le `name` du registry nomme la source réelle (Pink Sheet, pas LBMA ; Coinbase via FRED, pas CoinGecko)

---
name: archi-eco3min
description: Architecture éditoriale et technique de référence pour Eco3min (eco3min.fr) — hiérarchie silo > pilier > sous-pilier > cluster (MAJEUR + satellites), 11 levels, 5 metas WP (`_eco3min_level`, `_eco3min_cluster`, `_eco3min_sub_pilier` slug sous-pilier SOURCE DE VÉRITÉ du maillage, `_eco3min_subpillar` ID dérivé pour le fil d'Ariane — synchro auto, cf metas-eco3min, `_eco3min_parent_major`), parsing URL bilingue (`/en/` `/fr/`). Liste figée des 11 piliers FR / 11 EN avec mapping symétrique, ~40 sous-piliers FR / ~30 EN, MAJEURs, études, outils, hub débutant. Couvre les 10 tables legacy `eco3min_*` + 5 tables mega `e3m_*` avec `translation_group_id` (FR ↔ EN), les conventions de code (préfixes `eco3-` / `Eco3min_*` / `ECO3MIN_*` / `e3m_`, configs JS, nonces, menu slugs), les design tokens du Hub. Activer pour toute tâche touchant la structure du site, le code des plugins, la classification, les slugs/URLs/levels. Plugins → plugins-eco3min ; metas → metas-eco3min ; rédaction → editeur-eco3min.
---

# Architecture Eco3min — référence technique

> Ce skill code en dur la **structure du site Eco3min** et les **conventions techniques** des plugins WordPress + mega-plugin associés. Il couvre **comment c'est structuré**, **où c'est stocké en BDD**, **comment le code l'écrit et le lit**.
>
> Pour le **fonctionnement opérationnel des plugins** (legacy + mega) — workflows, projets Claude associés, bugs connus, méthode Paul — voir `plugins-eco3min`.
> Pour le **cycle de vie des metas** (quoi poser après création/import, snippet SYNC, Subpillar Aligner, registre des plugins avec URLs), voir `metas-eco3min`.
> Pour la **rédaction éditoriale** (style, voix, conformité AMF), voir `editeur-eco3min`. Pour les formats HTML rédactionnels (encarts, TL;DR, FAQ), voir `formats-eco3min`. Pour la production de pages dataset standardisées, voir `production-dataset`. Pour les Q&A, voir `production-q-and-a`.

---

## 1. Hiérarchie éditoriale

### 1.1 Concept de silo

Un **silo** = l'ensemble {pilier + ses sous-piliers + les MAJEURs de ces sous-piliers + les satellites de ces MAJEURs}. C'est un terme englobant pour parler d'une branche thématique entière.

**Le silo n'a aucune réalité technique en BDD** — pas de meta `_eco3min_silo`, pas de table dédiée. C'est un concept de discussion. Ce qui existe en BDD, c'est le pilier (l'article racine de la branche) et tout ce qui s'y rattache via les metas.

### 1.2 Structure

```
Silo (concept englobant, pas en BDD)
└── Pilier (level=pillar)              ← article racine, sommet
    └── Sous-pilier (level=sub_pillar)
        └── Cluster (concept = MAJEUR + satellites)
            ├── MAJEUR (level=major_article)  ← hub du cluster
            └── 10 à 40 satellites (level=satellite)
```

### 1.3 Vocabulaire

| Terme | Sens |
|---|---|
| **Silo** | branche thématique entière (pilier + descendants). Concept éditorial. |
| **Pilier** | article racine de la branche. URL flat à 1 segment (`/pilier-slug/`). Top-level. |
| **Sous-pilier** | spécialisation du pilier. **URL à 2 segments** (`/pilier/sub-pilier/`) — vérifié en base, cf. §2.1. Mid-level. |
| **Cluster** | un MAJEUR + tous ses satellites. Concept éditorial. |
| **MAJEUR** | article central d'un cluster. Hub vers lequel pointent les satellites. Long, beaucoup de liens entrants. |
| **Satellite** | article rattaché à un MAJEUR via `_eco3min_parent_major`. |

**Piège fréquent** : la meta `_eco3min_cluster` stocke en réalité **le slug du pilier d'attache**, pas un identifiant de cluster. Mauvais nommage historique gardé pour ne pas casser les plugins. Le "cluster" au sens éditorial Paul (= MAJEUR + satellites) se matérialise via `_eco3min_parent_major`.

---

## 2. Les 11 levels

`_eco3min_level` peut prendre 11 valeurs (12 avec `uncategorized` qui est l'état de départ avant classification, pas un vrai level cible).

| Level | Description | Indicateurs principaux |
|---|---|---|
| `pillar` | Article racine d'un pilier | URL = 1 segment, ce segment ∈ liste des pillars connus |
| `sub_pillar` | Spécialisation d'un pilier | URL = 2 segments, 1er ∈ pillars. Signal secondaire : son slug est utilisé comme valeur `_eco3min_sub_pilier` par d'autres pages (cf. §2.1) |
| `major_article` | Hub central d'un cluster | word_count ≥ 4500, incoming ≥ 20, ou article racine long |
| `foundation_article` | Fondamentaux/intro/principes | mots-clés "fondamentaux", "introduction", "guide", word_count modéré |
| `deep_study` | Étude approfondie avec données | mots-clés "étude", "historique", "depuis 19xx", shortcodes datasets |
| `case_study` | Étude d'un événement spécifique | mots-clés "crise de", "krach", "Volcker", "Lehman", année dans le titre |
| `dataset` | Page dataset brute | URL contient "dataset" ou "donnees", shortcodes `[eco3min_*]` |
| `faq` | Page Q&A | URL `/qa/` ou `/qr/`, titre commençant par mot interrogatif, ou se terminant par `?` |
| `tool` | Outil interactif | URL contient "outil" ou "tool", mots-clés "calculateur", "simulateur", "diagnostic" |
| `beginner` | Article pédagogique débutant | cluster = `apprendre-investir` ou `investing-for-beginners-hub` |
| `satellite` | Article éditorial rattaché à un MAJEUR | word_count 500-2500, URL pas dans les patterns autres levels |
| `uncategorized` | État de départ (pas un vrai level cible) | aucune meta `_eco3min_level` ou meta vide |

### 2.1 ⚠️ La colonne `url` de `snapshot.csv` est une reconstruction plate — ne jamais s'en servir

**Les URLs de sous-piliers sont IMBRIQUÉES**, à deux segments :
`/{pilier-slug}/{sub-pilier-slug}/` en FR,
`/en/{pilier-slug}/{sub-pilier-slug}/` en EN.

Vérifié en base le 04/09/2026 via l'ability `eco3min/find`, sur 8 sous-piliers
tirés au hasard, 8 sur 8 imbriqués :

- `/politique-monetaire-taux/banques-centrales-actions/`
- `/strategies-dinvestissement/choisir-placements-selon-cycle-macro/`
- `/matieres-premieres-economie-mondiale/matieres-premieres-agricoles/`
- `/macroeconomie-geopolitique/outils-macro/`
- `/en/macro-financial-regimes/crisis-hub/`
- `/en/asset-allocation-strategies-resilient-portfolios-market-regimes/choosing-investments-market-regimes-rate-cycles/`

#### Le piège qui a produit deux erreurs successives

La colonne `url` de `context/snapshot.csv` donne **un seul segment pour les
2979 lignes**, tous levels confondus — y compris les **615 pages `faq`**, dont
les URLs réelles contiennent pourtant `/qr/` en FR et `/qa/` en EN.

Ce n'est pas une donnée : c'est une **reconstruction `https://eco3min.fr/{slug}/`
appliquée uniformément**. Elle ne reflète la réalité que pour les levels qui se
trouvent être à un segment.

Deux conclusions fausses en sont sorties :

1. Le correctif de juillet 2026 du projet A. Architect, qui déclarait la règle
   imbriquée « spéculative et démentie par la BDD » et la remplaçait par « format
   constaté dans le snapshot ». Il s'appuyait sur cette colonne.
2. Une révision de ce skill en septembre 2026, qui a repris la même mesure sur
   97 sous-piliers et en a tiré la même conclusion. **Annulée par le présent
   paragraphe.**

Les deux ont mesuré la reconstruction, pas le site.

#### La règle

- **Le champ `slug` du snapshot est fiable.** Il vient de la base.
- **Le champ `url` ne l'est pas.** Il est reconstruit à plat et se trompe sur
  tout ce qui est parenté hiérarchiquement — sous-piliers, Q&A, hubs.
- Pour une URL réelle : `eco3min/find` ou `eco3min/get-content` renvoient la
  **permalink** calculée par WordPress. C'est la seule source.
- **Ne jamais inférer une structure de permalien**, ni depuis le snapshot, ni
  depuis un pattern supposé.

#### Signal secondaire de classification

Indépendamment de l'URL, un sous-pilier se reconnaît aussi à ce que **son slug
est utilisé comme valeur `_eco3min_sub_pilier` par d'autres pages** : 89 des 97
sont ainsi référencés, et une seule valeur de meta ne correspond à aucune page
`sub_pillar`. Utile en complément du pattern d'URL du §13.1, notamment pour les
8 sous-piliers sans enfants (les pages outils, et des pages du hub débutant EN).

⚠️ Sur une page de niveau `sub_pillar` elle-même, `_eco3min_sub_pilier` est
**vide** et `_eco3min_subpillar` vaut `0` — c'est normal : la meta désigne le
sous-pilier de rattachement, et un sous-pilier ne se rattache pas à lui-même.

**Source** : `eco3min-level-classifier/includes/class-classifier.php::LEVELS` et `Eco3min_Mega_Validator::ALLOWED_LEVELS` (mega) — ne pas inventer de level supplémentaire.

---

## 3. Les metas WordPress (`_eco3min_*`)

Toutes stockées dans `wp_postmeta` (préfixe réel sur le site Paul : `mod441_postmeta`).

| Meta | Type | Contenu |
|---|---|---|
| `_eco3min_level` | string | Un des 11 levels ci-dessus (ou `uncategorized`) |
| `_eco3min_cluster` | string | **Slug du pilier d'attache** (mauvais nom historique) |
| `_eco3min_sub_pilier` | string (slug) | **SOURCE DE VÉRITÉ du rattachement sous-pilier.** Slug de la PAGE sous-pilier. Lue par le classifier mega, le scanner, le mu-analyzer (conseil T1/T2/T3) et l'exporter snapshot ; écrite par l'import cluster/multi-pair, le Tinder mega et le Cleanup. Jamais supprimée ni écrasée par une machine. |
| `_eco3min_subpillar` | int | **Projection DÉRIVÉE du slug** : post_id de la PAGE sous-pilier, consommé par le **fil d'Ariane** et la metabox éditeur « Sous-pilier (Page) ». Maintenu en phase avec le slug par le snippet SUBPILLAR SYNC (hooks + cron daily) ; rattrapage batch via le plugin Subpillar Aligner. La metabox reste le point de saisie humain : l'ID choisi est aussitôt reconverti en slug canonique par SYNC. |
| `_eco3min_parent_major` | int | post_id du MAJEUR auquel le satellite est rattaché |

> ✅ **Doctrine TRANCHÉE (juillet 2026) — les deux clés sont voulues, hiérarchisées, synchronisées.** Le caveat de juin 2026 (« `_eco3min_sub_pilier` non confirmé, à purger ») est **caduc** : le grep du mega v1.0.13.1 a répondu aux deux questions ouvertes. (1) Tout le moteur — classifier (`ALLOWED_META_KEYS`), scanner, mu-analyzer/doctor, importers cluster & multi-pair, Cleanup, exporter snapshot — lit et écrit **le SLUG `_eco3min_sub_pilier`** : c'est la clé maître. (2) Le breadcrumb, lui, consomme **l'ID `_eco3min_subpillar`**, projection dérivée du slug. La mise en phase est automatique (snippet Code Snippets « SUBPILLAR SYNC » : hooks à l'écriture + cron daily), rattrapable en batch (plugin **Subpillar Aligner**, `admin.php?page=eco3min-subpillar-aligner`), arbitrable sur conflit (mega → onglet Réconciliation, suppression réversible de l'ID). **Sur conflit, le slug gagne.** Ne plus jamais « purger » l'une des deux clés : le défaut n'est pas la coexistence, c'est la désynchronisation. Workflows complets, registre des outils et pièges → skill `metas-eco3min`.

### 3.1 Tableau d'écriture des metas par level

| Level | `_eco3min_level` | `_eco3min_cluster` | sous-pilier (`_sub_pilier` slug maître → `_subpillar` ID auto) | `_eco3min_parent_major` |
|---|---|---|---|---|
| `pillar` | ✅ | — | — | — |
| `sub_pillar` | ✅ | slug pilier parent | — | — |
| `major_article` | ✅ | slug pilier parent | slug page sous-pilier parent | — |
| `satellite` | ✅ | slug pilier | slug page sous-pilier | post_id du MAJEUR (systématique sinon orphelin) |
| `deep_study` / `case_study` | ✅ | slug pilier | slug page sous-pilier | parfois |
| `foundation_article` | ✅ | slug pilier | slug page sous-pilier | parfois |
| `faq` / `dataset` / `tool` | ✅ | slug pilier | slug page sous-pilier | parfois |
| `beginner` | ✅ | slug pilier (= `apprendre-investir` ou EN equivalent) | slug page sous-pilier si applicable | rarement |

> Note : la valeur qu'on POSE est le **slug** (`_eco3min_sub_pilier`) — via import cluster, Tinder mega ou Cleanup. L'ID (`_eco3min_subpillar`) suit **automatiquement** (snippet SYNC ; sinon Aligner). En saisie unitaire, la metabox « Sous-pilier (Page) » reste utilisable : elle écrit l'ID, aussitôt reconverti en slug canonique. Détail des outils → `metas-eco3min`.

**Règles fondamentales** :
- Un `pillar` ne reçoit **aucune** meta de catégorie (sommet de hiérarchie).
- Un `sub_pillar` reçoit `_eco3min_cluster` (slug pilier parent) mais **aucune** meta sous-pilier (ni slug ni ID : il *est* un sub-pilier, pas attaché à un autre).
- Un `satellite` est le **seul** level systématiquement relié à un MAJEUR via `_eco3min_parent_major`. S'il n'en a pas, il est orphelin (visible dans Level Classifier > Onglet Arborescence).
- Le code n'écrase **jamais** une meta déjà remplie — le backfill ne touche que les meta vides.

### 3.2 Source de vérité — règle non négociable

Les metas WP `_eco3min_*` sont la **source unique de vérité** de la classification éditoriale. Aucun autre lieu de stockage ne fait foi :
- Le mega-plugin (table `e3m_articles`, voir section 10.3) **mirroite** ces metas pour ses besoins propres mais ne les définit jamais.
- Les writes sur ces metas par le mega passent obligatoirement par `Eco3min_Mega_Classifier::set_meta_safe()` avec garde-fou immutabilité (throw `Eco3min_Mega_Immutability_Exception` en cas de tentative d'écrasement). Voir `plugins-eco3min` section 12.4.
- Pour modifier une classification existante : passer par WP éditeur (Custom Fields) ou Meta Monitor — jamais via SQL direct ni via les plugins automatisés.

---

### 3.1 Catégories WordPress — table vérifiée en base

⚠️ **Le slug de catégorie WP n'est PAS le slug du pilier.** Il est plus court et
structuré différemment, et il **diffère entre FR et EN** — ce n'est pas une
simple recopie. Un import qui réutilise le slug de pilier comme catégorie échoue
avec `Catégorie WP introuvable`.

Vérifiée en base le **04/09/2026** (`ewpa/get-categories`) :

| Pilier | Catégorie FR | `term_id` | Catégorie EN | `term_id` |
|---|---|---|---|---|
| Actions & ETF | `actions-et-etf` | 440 | `equities-etfs` | 550 |
| Crypto-actifs | `crypto-actifs` | 452 | `crypto-assets` | 552 |
| Éducation financière | `education-financiere` | 416 | `financial-education` | 554 |
| Immobilier | `immobilier` | 420 | `real-estate` | 556 |
| Macro & géopolitique | `macro-geopolitique` | 430 | `macroeconomics-geopolitics` | 558 |
| Marchés financiers | `marches` | 413 | `financial-markets-indices` | 8 |
| Matières premières | `matieres-premieres` | 458 | `commodities-global-economy` | 560 |
| Politique monétaire & taux | `politique-monetaire-taux` | 446 | `monetary-policy-rates-liquidity` | 562 |
| Stratégies d'investissement | `investissement-strategies` | 456 | `investment-strategies` | 564 |
| **Hub débutant** (`apprendre-investir`) | **aucune** | — | **aucune** | — |
| **Hub datasets** (`donnees-analyses-...`) | **aucune** | — | **aucune** | — |

**Neuf** catégories par langue, pas onze : les deux hubs n'en ont aucune. C'est
pourquoi la procédure de rattachement autonome les exclut — un sous-pilier dont
la catégorie WP n'est pas résolvable ne peut pas recevoir d'import.

**Piège de collision.** `commodities-global-economy` est le slug de la
**catégorie EN** des matières premières. C'est aussi l'un des slugs de **pilier**
EN obsolètes hardcodés dans `eco3min-site-audit` (cf. §7). Deux objets
différents, même chaîne : ne pas déduire l'un de l'autre.

Résolution toujours **par slug**, jamais par `term_id` codé en dur —
`Eco3min_Mega_Category_Resolver::resolve($slug)`. Les `term_id` ci-dessus sont
donnés pour le diagnostic, pas pour être écrits dans du code.

---

## 4. Parsing d'URL bilingue

Logique implémentée dans `eco3min-level-classifier/includes/class-backfiller.php::detect_branches_from_url()` ainsi que dans `Eco3min_Mega_Polylang_Bridge` (mega).

```
1. Récupérer l'URL via get_permalink($post_id)
2. Extraire le path (wp_parse_url, PHP_URL_PATH)
3. Splitter en segments par "/"
4. SI segment[0] ∈ {'en', 'fr'} → array_shift() (retirer prefix langue)
5. segment[0] = slug pilier candidat (vérifier qu'il ∈ known_pillars)
6. segment[1] = slug sub-pilier candidat (vérifier qu'il ∈ known_sub_pillars)
```

**Cas du `level=pillar`** : retourne toujours `pilier=null, sub_pilier=null` (sommet).

**Cas du `level=sub_pillar`** : retourne `pilier=segment[0]` mais `sub_pilier=null` (lui-même est un sub-pilier).

**Cas autres levels** : `pilier=segment[0], sub_pilier=segment[1]` si tous deux reconnus.

`known_pillars` et `known_sub_pillars` sont chargés en cache statique depuis la BDD (posts avec `_eco3min_level=pillar` ou `sub_pillar`). Ces caches doivent être resetés (`Eco3min_LC_Backfiller::reset_cache()`) entre 2 passes du backfill quand on vient de classifier de nouveaux pillars/sub_pillars.

**Note langue (Polylang)** : la langue d'un post est lue via `pll_get_post_language($id)` (taxonomie Polylang), pas via la postmeta `_eco3min_lang` qui peut être obsolète. Le mega utilise systématiquement `Eco3min_Mega_Polylang_Bridge::get_post_language()` qui encapsule cet appel.

---

## 5. Liste figée des piliers

### 5.1 Piliers FR (11)

| # | Slug | Thème |
|---|---|---|
| 1 | `macroeconomie-geopolitique` | Macro & géopolitique |
| 2 | `politique-monetaire-taux` | Politique monétaire & taux |
| 3 | `marches-financiers` | Marchés financiers |
| 4 | `actions-et-etf` | Actions & ETF |
| 5 | `immobilier-cycles-taux-economie` | Immobilier |
| 6 | `matieres-premieres-economie-mondiale` | Matières premières |
| 7 | `crypto-actifs-comprendre-enjeux-economiques-financiers-monetaires` | Crypto-actifs |
| 8 | `strategies-dinvestissement` | Stratégies d'investissement |
| 9 | `page-education-financiere` | Éducation financière |
| 10 | `apprendre-investir` | Hub débutant FR |
| 11 | `donnees-analyses-macro-financieres` | Hub datasets FR |

### 5.2 Piliers EN (11)

| # | Slug | Thème |
|---|---|---|
| 1 | `macro-financial-regimes` | Macro & geopolitics |
| 2 | `monetary-regimes-interest-rates-liquidity-market-cycles` | Monetary regimes & rates |
| 3 | `market-regimes-liquidity-real-rates-financial-dynamics` | Market regimes |
| 4 | `equity-markets-etfs-structure-valuations-cycles` | Equity & ETFs |
| 5 | `real-estate-credit-rate-cycles` | Real estate |
| 6 | `commodity-regimes-physical-constraints-energy-transition` | Commodities |
| 7 | `crypto-assets-liquidity-cycles-real-rates` | Crypto |
| 8 | `asset-allocation-strategies-resilient-portfolios-market-regimes` | Asset allocation |
| 9 | `financial-education-macroeconomic-regimes` | Financial education |
| 10 | `investing-for-beginners-hub` | Beginner hub EN |
| 11 | `research-data` | Datasets hub EN |

### 5.3 Mapping FR ↔ EN

Le mapping est **symétrique pour les 11 piliers** : à chaque pilier FR correspond un pilier EN au même niveau hiérarchique (et inversement). Pas d'asymétrie — un pilier FR n'est jamais traduit en sub-pilier EN.

| FR | EN |
|---|---|
| `macroeconomie-geopolitique` | `macro-financial-regimes` |
| `politique-monetaire-taux` | `monetary-regimes-interest-rates-liquidity-market-cycles` |
| `marches-financiers` | `market-regimes-liquidity-real-rates-financial-dynamics` |
| `actions-et-etf` | `equity-markets-etfs-structure-valuations-cycles` |
| `immobilier-cycles-taux-economie` | `real-estate-credit-rate-cycles` |
| `matieres-premieres-economie-mondiale` | `commodity-regimes-physical-constraints-energy-transition` |
| `crypto-actifs-comprendre-enjeux-economiques-financiers-monetaires` | `crypto-assets-liquidity-cycles-real-rates` |
| `strategies-dinvestissement` | `asset-allocation-strategies-resilient-portfolios-market-regimes` |
| `page-education-financiere` | `financial-education-macroeconomic-regimes` |
| `apprendre-investir` | `investing-for-beginners-hub` |
| `donnees-analyses-macro-financieres` | `research-data` |

**Note** : les slugs hardcodés dans `eco3min-site-audit/includes/class-installer.php` étaient obsolètes pour 4 piliers EN au moment de la rédaction de ce skill (`real-estate-cycles-rates-economy`, `commodities-global-economy`, `crypto-assets-economic-monetary-financial-stakes`, `financial-education`). **Les bons slugs sont ceux du tableau ci-dessus.** Si on touche au installer, mettre à jour. Le mega utilise les slugs corrects via la table `e3m_referentiel`.

---

## 6. Liste figée des sous-piliers

### 6.1 Sous-piliers FR par pilier

`macroeconomie-geopolitique`
- `cycle-economique`
- `inflation-au-dela-des-chiffres-mensuels`
- `dette-fragilites-systemiques`
- `demondialisation`
- `geopolitique-structurelle`

`politique-monetaire-taux`
- `banques-centrales-actions`
- `liquidite-conditions-financieres`
- `dollar-systeme-mondial`
- `transmission-monetaire-entreprises`

`marches-financiers`
- `dynamiques-marche-microstructure`
- `dynamiques-marche-anticipations`
- `dynamiques-marche-correlations`
- `dynamiques-marche-flux-capitaux`
- `dynamiques-marche-tensions-cachees`
- `devises-forex-comprendre-les-marches-monetaires`
- `innovation-financiere`

`actions-et-etf`
- `revolution-passive-gestion-indicielle`
- `retour-actionnaires`
- `secteurs-thematiques`
- `cycles-anticipations-marche`
- `valorisations-dynamique-profits`
- `entreprises-et-secteurs-dynamiques-economiques`

`immobilier-cycles-taux-economie`
- `inflation-protection`
- `rendement-locatif`
- `cycle-credit`
- `taux-capacite-achat`

`matieres-premieres-economie-mondiale`
- `formation-prix-mecanismes`
- `cycles-transmission-macro`
- `geoeconomie-ressources`
- `energie-matieres-premieres`
- `matieres-premieres-agricoles`

`crypto-actifs-comprendre-enjeux-economiques-financiers-monetaires`
- `bitcoin-actif-monetaire-cycles-liquidite`
- `regulation-risques-structurels-crypto`
- `cycles-volatilite-crypto-comprendre`
- `ethereum-stablecoins-infrastructure-decentralisee`

`strategies-dinvestissement`
- `lire-cycle-ajuster-exposition`
- `pieges-esprit-biais-comportementaux`
- `gerer-risque-portefeuille`
- `fondements-allocation-actifs`
- `choisir-placements-selon-cycle-macro`

`page-education-financiere`
- `methode-principes-financiers`
- `arbitrages-quotidien`
- `anatomie-des-placements`
- `outils-financiers`

`apprendre-investir` et `donnees-analyses-macro-financieres` n'ont pas de sous-piliers — ce sont des hubs qui contiennent des articles directement.

### 6.2 Sous-piliers EN par pilier

`macro-financial-regimes`
- `economic-cycle-phases-signals-market-implications`
- `inflation-regimes-structural-drivers-macro-financial-implications`
- `systemic-fragilities-debt-shadow-banking-financial-stability-risks`
- `deglobalization-fragmentation-geopolitics-supply-chains-trade`
- `geopolitics-macroeconomics-structural-transmission-markets-regimes`

`monetary-regimes-interest-rates-liquidity-market-cycles`
- `central-banks-monetary-policy-rate-cycles-market-transmission`
- `liquidity-financial-conditions-monetary-plumbing-qt-market-impact`
- `us-dollar-systemic-global-monetary-system`
- `monetary-transmission-corporate-earnings-time-lags-margins-rate-cycles`

`market-regimes-liquidity-real-rates-financial-dynamics`
- `market-microstructure-price-formation-mechanics`
- `market-expectations-sentiment-price-formation`
- `asset-class-correlations-regime-shifts`
- `capital-flows-price-formation-markets`
- `systemic-risk-indicators-market-stress-signals`
- `fx-markets-exchange-rates-monetary-regimes`
- `financial-innovation-market-infrastructure-systemic-risk`

`equity-markets-etfs-structure-valuations-cycles`
- `passive-management-etf-market-structure`
- `dividends-share-buybacks-total-shareholder-yield-distribution-cycles`
- `sector-rotation-style-regimes-value-growth-market-cycles`
- `equity-market-valuation-real-rates-multiples-earnings`
- `equity-markets-real-economy-earnings-cycles-monetary-regimes`
- `companies-economic-sectors-structural-drivers-competitiveness-value-creation`

`real-estate-credit-rate-cycles`
- `real-estate-inflation-credit-real-rates-protection-paradox`
- `rental-property-profitability-gross-net-yield-cost-of-capital`
- `real-estate-credit-cycle-price-dynamics`
- `interest-rates-real-estate-purchasing-power-mortgage-capacity-mechanism`

`commodity-regimes-physical-constraints-energy-transition`
- `commodity-price-formation-physical-constraints-financial-flows-structural-drivers`
- `commodities-macroeconomic-regime-signals-cycles-inflation-strategic-power`
- `physical-commodity-markets-oil-gas-copper-critical-minerals-structural-signals`
- `physical-constraints-economy-energy-resources-structural-growth-limits`
- `agricultural-commodities-softs-grains-climate-cycles-food-inflation`

`crypto-assets-liquidity-cycles-real-rates`
- `bitcoin-liquidity-cycles-real-rates-macro-regimes`
- `crypto-regulation-effects-limits-structural-risks`
- `crypto-volatility-structural-drivers-liquidity-regimes`
- `ethereum-stablecoins-digital-dollarization-architecture-risks`

`asset-allocation-strategies-resilient-portfolios-market-regimes`
- `economic-cycle-analysis-portfolio-regime-positioning`
- `behavioral-investing-cognitive-biases-discipline-risk`
- `portfolio-risk-management-survival-before-performance`
- `portfolio-allocation-architectures-regime-assumptions`
- `choosing-investments-market-regimes-rate-cycles`

`financial-education-macroeconomic-regimes`
- `financial-education-framework-principles-economic-regimes`
- `everyday-financial-tradeoffs-economic-regimes`
- `investment-vehicles-real-returns-costs-regime-impact`
- `financial-tools-simulators-test-assumptions-decisions`

> **Ajouts juin 2026 (vérifiés live, HTTP 200)** — deux paires de sous-piliers publiées récemment, ajoutées en fin de bloc de leur pilier :
> - `matieres-premieres-economie-mondiale/matieres-premieres-agricoles` ↔ `commodity-regimes-physical-constraints-energy-transition/agricultural-commodities-softs-grains-climate-cycles-food-inflation`
> - `strategies-dinvestissement/choisir-placements-selon-cycle-macro` ↔ `asset-allocation-strategies-resilient-portfolios-market-regimes/choosing-investments-market-regimes-rate-cycles`

---

## 7. MAJEURs principaux

Liste des slugs des MAJEURs (= articles centraux des clusters). Ces slugs sont relativement stables — la liste évolue avec la production éditoriale (8 articles/mois max).

### 7.1 MAJEURs FR

```
hausse-taux-impact-marches-financiers
taux-interet-moment-dangereux-marches-financiers
marches-hausse-courbe-des-taux-inversee
courbe-des-taux-inversee-signal-lent-regime
courbe-des-taux-inversee-et-marches-actions-comprendre-la-decorrelation
courbe-des-taux-inversee-credit-economie-reelle
surprises-resultats-dispersion-performances-marche
revisions-benefices-faux-signal-stabilite-indices
surprises-resultats-changement-regime-financier
liquidite-etf-continuite-illusoire-marches-sous-jacents
etf-formation-des-prix-liquidite
regime-taux-eleves-fragilisation-liquidite-etf
dollar-fort-duree-sans-crise-financiere
dollar-fort-desequilibres-silencieux-economie-mondiale
dollar-fort-hierarchie-performances-financieres
tensions-mer-rouge-commerce-mondial
risques-etf-intelligence-artificielle
politique-monetaire-action-economie-reelle
discipline-investissement-performance-sans-surperformance
education-financiere-structurer-decisions-dans-le-temps
matieres-premieres-cycles-reels-transmission-macro
crypto-actifs-cycles-liquidite-taux-integration-institutionnelle
cycle-du-credit-immobilier-moteur-prix-immobilier
offre-physique-demande-financiere-prix-matieres-premieres
impact-taux-interet-marches-financiers
courbe-des-taux-recession
revisions-de-benefices-reactions-boursieres
liquidite-des-etf-risque-cache-quand-les-marches-decrochent
dollar-fort-impacts-marches-financiers
ia-transformation-finance-risque-structurel
marches-actions-economie-reelle-divergence
cycle-economique-reel
residence-principale-epargne-investissement-logiques-differentes
politique-monetaire-restrictive-mecanismes-effets-differes
epargne-placement-investissement-difference
inflation-guide-complet
```

### 7.2 MAJEURs EN

```
interest-rates-financial-markets-valuation-asset-allocation
yield-curve-inversion-credit-channel-recession-mechanism
earnings-revisions-market-reversals-leading-signal-equity-cycle
etf-liquidity-market-risk
strong-dollar-structural-regime-market-transmission
artificial-intelligence-systemic-financial-risk
equity-markets-economic-cycle-anticipation-mechanism
real-economic-cycle-investment-productivity-growth
primary-residence-savings-investing-wealth-functions
restrictive-monetary-policy-delayed-effects-credit-transmission
saving-vs-investing-vs-placing-risk-time-liquidity
inflation-complete-guide
```

---

## 8. Études approfondies, articles de fond, études de cas, outils

### 8.1 Datasets — études approfondies (~14)

Ces pages sont produites avec le pipeline "Claude v5 datasets" (voir `production-research-study`). Bilingues FR + EN.

```
real-interest-rates-vs-cape-ratio-dataset / taux-interet-reels-vs-cape-ratio-dataset
yield-curve-inversion-history-2s10s-spread / inversion-courbe-des-taux-historique
net-liquidity-index-dataset / liquidite-nette-us-indice-fed-tga-rrp
us-dollar-global-crises-dataset / dollar-americain-crises-mondiales-dataset-1973-2023
real-interest-rates-history / taux-interet-reels-us-histoire
us-hy-credit-spread-leading-indicator-dataset / spreads-credit-high-yield-indicateur-avance-sp500-dataset
us-inflation-is-not-linear / histoire-inflation-etats-unis
vix-contrarian-almanac-dataset / almanach-contrarian-vix-dataset
fed-funds-rate-track-record-dataset / bilan-fed-funds-rate-decisions-dataset
nfp-revisions-mislead-at-turning-points / nfp-revisions-biais-emploi-recessions
30-year-treasury-duration-risk / taux-30-ans-us-risque-duration
```

### 8.2 Articles de fond (~9 FR + 2 EN)

Articles structurants qui ne sont ni des piliers, ni des MAJEURs, ni de simples satellites — souvent classés `foundation_article`.

FR :
```
politique-monetaire-cadre-limites
phases-sans-signal-exploitable-marches
performance-indices-moins-dependante-entreprises
dispersion-performances-actions-marche-selectif
cycle-credit-immobilier-vrai-cycle-marche
matieres-premieres-politique-economique-indirecte
education-financiere-angles-morts-risque
signaux-financiers-economie-reelle-divergence-durable
```

EN :
```
monetary-policy-incentives-limits-real-economy
markets-without-signal-dispersion-risk
```

### 8.3 Études de cas (~7)

Souvent classées `case_study`. Identifiables par référence à un événement, une crise, une période.

```
stabilite-strategique-inefficience-economique
politique-monetaire-defensive-eviter-le-pire
indicateurs-macro-rassurants-fragilisation-marches
banque-centrale-perte-controle-devise-sans-crise-visible
regulation-stabilisation-implicite-crypto-actifs
discipline-investissement-performance-sans-surperformance / investment-discipline-long-term-performance
innovation-financiere-rigidification-comportements-marche
```

### 8.4 Pages outils (3)

Slugs FR uniquement à ce jour, classés `tool` :

```
lecture-cycle-taux
diagnostic-du-cycle-macro-cadre-danalyse-eco3min
indicateur-economique-trompeur
```

---

## 9. Hub débutant

Articles classés `level=beginner`, attachés au pilier `apprendre-investir` (FR) ou `investing-for-beginners-hub` (EN). URLs imbriquées sous le pilier hub.

### 9.1 FR (`/apprendre-investir/...`)

```
comment-investir-debutant
etf-debutant
pea-vs-cto
combien-investir-par-mois
rendement-reel-vs-nominal
inflation-et-investissement
erreurs-investisseur-debutant
```

### 9.2 EN (`/en/investing-for-beginners-hub/...`)

```
how-to-invest-for-beginners-guide
etf-explained-for-beginners
pea-vs-cto-brokerage-accounts
how-much-to-invest-per-month
real-vs-nominal-returns
```

---

## 10. Tables BDD custom

Toutes les tables sont préfixées par le préfixe WordPress du site (`mod441_` dans le cas de Paul) suivi du nom court ci-dessous. Toutes utilisent `dbDelta()` à l'activation.

### 10.1 Tables LEGACY (préfixe `eco3min_*`)

| Table | Plugin | Rôle | Modifie wp_posts.post_content ? |
|---|---|---|---|
| `eco3min_sa_links` | Site Audit | Cache des liens internes scannés (~13 477 lignes typiques) | non |
| `eco3min_lc_suggestions` | Level Classifier | Suggestions de level avant validation Tinder | non |
| `eco3min_ad_log` | Anchor Diversifier | Log des remplacements d'ancres appliqués | oui (avec backup) |
| `eco3min_ad_backup` | Anchor Diversifier | Snapshot du contenu avant remplacement | — |
| `eco3min_rc_cases` | Redundant Cleaner | Cas de liens dupliqués 3+ fois | oui (avec backup) |
| `eco3min_rc_backup` | Redundant Cleaner | Snapshot du contenu avant nettoyage | — |
| `eco3min_ah_snapshots` | Anchor Health | Snapshots quotidiens de saturation des ancres | non |
| `eco3min_dm_health` | Dataset Monitor | Health check des 75+ datasets | non |
| `eco3min_gsc_data` | GSC Linker | Données GSC importées par session | non |
| `eco3min_gsc_suggestions` | GSC Linker | Suggestions de liens GSC à valider | non |
| `eco3min_audit_pillars` | Maillage Audit | Référentiel piliers (270 rows) | non |

**Aucun plugin de la suite ne modifie `wp_posts.post_content` sans backup**. Les deux qui touchent au contenu (Anchor Diversifier, Redundant Cleaner) ont systématiquement une table backup avec `session_id` permettant un rollback.

### 10.2 Schéma `eco3min_sa_links` (table centrale legacy)

Cette table est lue par 6 autres plugins. Schéma critique :

```sql
CREATE TABLE eco3min_sa_links (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    src_post_id BIGINT UNSIGNED NOT NULL,        -- post source du lien
    target_post_id BIGINT UNSIGNED DEFAULT NULL, -- post cible (NULL si externe)
    target_url_path VARCHAR(512) NOT NULL,       -- path de l'URL cible
    anchor_text TEXT NOT NULL,                   -- texte de l'ancre <a>
    is_external TINYINT(1) NOT NULL DEFAULT 0,   -- 1 si URL externe
    location VARCHAR(32) NOT NULL DEFAULT 'content', -- "content", "excerpt", etc.
    created_at DATETIME NOT NULL,
    PRIMARY KEY (id),
    KEY src_post_id, KEY target_post_id, KEY target_url_path
);
```

**ATTENTION : la colonne s'appelle `src_post_id`, pas `source_post_id`.** Bug existant dans `eco3min-level-classifier/includes/class-classifier.php::detect_parent_major()` ligne ~359 où une query utilise `source_post_id` — la query échoue silencieusement, l'heuristique 1 (analyse des liens sortants) ne marche jamais, le code retombe toujours sur l'heuristique 2 (Jaccard de titre). À fixer si on touche au classifier. Le mega corrige ce bug dans son scanner V0.5+.

### 10.3 Tables MEGA (préfixe `e3m_*`, à partir de V0.1)

Ces 5 tables sont créées à l'activation du mega-plugin et **cohabitent** avec les tables legacy (préfixes différents, pas de conflit).

| Table | Rôle | Particularité |
|---|---|---|
| `e3m_referentiel` | Liste figée piliers/sub_piliers/MAJEURs + catégories WP. Inclut colonnes `wp_category_slug` et `wp_category_id` (résolus par slug, pas par term_id). Migration auto depuis `eco3min_audit_pillars` à l'activation | Seule table modifiable en UI (onglet 1) |
| `e3m_articles` | Miroir des articles WP avec metas Eco3min + état (`green`/`orange`/`red`) + **`translation_group_id`** (lie FR ↔ EN) | Source de vérité reste les metas WP (voir 3.2) |
| `e3m_links` | Graphe des liens internes peuplé par scanner V0.5+. Colonnes : `src_post_id`, `target_post_id`, `is_cross_lang` (TINYINT, 1 si FR linke vers EN ou inversement = à corriger) | Remplace `eco3min_sa_links` à terme |
| `e3m_patches_log` | Log des patches appliqués (anti-doublon par hash SHA256) | Absorbe Maillage Cluster v1.0.2 |
| `e3m_backups` | post_content avant chaque modification — colonnes `trigger_action` + `trigger_ref` permettant rollback batch | Rollback par `backup_id` ou par `trigger_ref` (entire batch) |

Pour les détails opérationnels (cohabitation legacy/mega, drop progressif des tables legacy), voir `plugins-eco3min` section 15.

### 10.4 Concept `translation_group_id` (mega)

Identifiant UUID v4 qui lie une paire FR + EN d'articles. Stocké dans `e3m_articles.translation_group_id`. Généré au moment de l'import cluster bilingue (Format C v1.1) par `Eco3min_Mega_Importer_Cluster`.

```
Paire #001 :
  - FR post_id 5841, slug "nouveau-cluster-fr",            translation_group_id = abc-123-def-...
  - EN post_id 5842, slug "new-cluster-en",                translation_group_id = abc-123-def-...
```

**Polylang câblé en parallèle** via `pll_save_post_translations(['fr' => 5841, 'en' => 5842])`. Les deux mécanismes coexistent : `translation_group_id` côté mega pour requêtes BDD rapides, Polylang côté WP pour le frontend.

**Requête utile** :
```sql
SELECT a1.post_id as fr_id, a1.slug as fr_slug,
       a2.post_id as en_id, a2.slug as en_slug,
       a1.cluster_slug, a1.level
FROM mod441_e3m_articles a1
JOIN mod441_e3m_articles a2
  ON a1.translation_group_id = a2.translation_group_id
  AND a1.lang = 'fr' AND a2.lang = 'en'
ORDER BY a1.post_id DESC;
```

---

## 11. Conventions de code des plugins

### 11.1 Préfixes par plugin LEGACY

| Plugin | Préfixe constantes | Préfixe classes PHP | Config JS | Nonce | Menu slug admin |
|---|---|---|---|---|---|
| Site Audit | `ECO3MIN_SA_` | `Eco3min_SA_*` | `EcoSAConfig` | `eco3min_sa_nonce` | `eco3min-site-audit` |
| Level Classifier | `ECO3MIN_LC_` | `Eco3min_LC_*` | `EcoLCConfig` | `eco3min_lc_nonce` | `eco3min-level-classifier` |
| Anchor Diversifier | `ECO3MIN_AD_` | `Eco3min_AD_*` | `EcoADConfig` | `eco3min_ad_nonce` | `eco3min-anchors` |
| Redundant Cleaner | `ECO3MIN_RC_` | `Eco3min_RC_*` | `EcoRCConfig` | `eco3min_rc_nonce` | `eco3min-redundant` |
| Anchor Health | `ECO3MIN_AH_` | `Eco3min_AH_*` | `EcoAHConfig` | `eco3min_ah_nonce` | `eco3min-anchor-health` |
| Dataset Monitor | `ECO3MIN_DM_` | `Eco3min_DM_*` | `EcoDMConfig` | `eco3min_dm_nonce` | `eco3min-datasets` |
| GSC Linker | `ECO3MIN_GSC_` | `Eco3min_GSC_*` | `EcoGSCConfig` | `eco3min_gsc_nonce` | `eco3min-gsc-linker` |
| Performance Dashboard | `ECO3MIN_PD_` | `Eco3min_PD_*` | — | — | `eco3min-performance` |
| Hub | `ECO3MIN_HUB_` | `Eco3min_Hub_*` | — | — | `eco3min-hub` (top-level) |

**Plugins existants (pré-suite, créés avant)** — pas de constantes/préfixes documentés ici, juste le menu slug :

| Plugin | Menu slug admin |
|---|---|
| Maillage Audit | `eco3min-maillage-audit` |
| Maillage Cluster | `eco3min-maillage` |
| Q&A Importer | `eco3min-q-and-a` |
| Translator Bridge | `eco3min-translator` |

### 11.2 Préfixes du mega-plugin

| Élément | Préfixe / convention |
|---|---|
| Tables BDD | `e3m_` (ex. `e3m_articles`, `e3m_links`) |
| Constantes PHP | `ECO3MIN_MEGA_` (ex. `ECO3MIN_MEGA_VERSION`) |
| Classes PHP | `Eco3min_Mega_*` (ex. `Eco3min_Mega_Classifier`, `Eco3min_Mega_Polylang_Bridge`) |
| Config JS | `EcoMegaConfig` (par onglet : `EcoMegaTab1Config`, etc.) |
| Nonce AJAX | `eco3min_mega_nonce` |
| Action AJAX | `eco3min_mega_*` (ex. `eco3min_mega_validate_cluster`) |
| Cron hook | `eco3min_mega_*` (ex. `eco3min_mega_scan_cron`) |
| Menu slug admin | `eco3min-mega` (top-level) avec sous-menus `eco3min-mega-tab-1`, etc. |
| Préfixe CSS | `eco3-mega-` (ex. `.eco3-mega-tinder-card`) |
| Capability | `manage_options` partout |
| Metas WP | **`_eco3min_*`** CONSERVÉ legacy (jamais `_e3m_*`). Les metas WP sont la source unique de vérité, voir section 3.2 |

**Règles non-négociables du mega** :
- Tous les appels Polylang passent par `Eco3min_Mega_Polylang_Bridge::*`, jamais direct.
- Tous les writes sur metas critiques passent par `Eco3min_Mega_Classifier::set_meta_safe()`.
- Toute résolution de catégorie WP se fait par slug via `Eco3min_Mega_Category_Resolver::resolve($slug)` (jamais par term_id hardcodé).

### 11.3 Conventions PHP

```php
// Check ABSPATH systématique en haut de chaque fichier inclus
if (!defined('ABSPATH')) { exit; }

// Constantes définies dans le entry point
define('ECO3MIN_LC_VERSION', '1.4.1');
define('ECO3MIN_LC_PLUGIN_DIR', plugin_dir_path(__FILE__));
define('ECO3MIN_LC_TABLE_SUGGESTIONS', 'eco3min_lc_suggestions');

// Mega : pareil avec préfixe ECO3MIN_MEGA_
define('ECO3MIN_MEGA_VERSION', '0.1.0');
define('ECO3MIN_MEGA_TABLE_ARTICLES', 'e3m_articles');

// Tables avec $wpdb->prefix pour tenir compte du préfixe site
$table = $wpdb->prefix . ECO3MIN_LC_TABLE_SUGGESTIONS;

// Headers plugin obligatoires
/**
 * Plugin Name: Eco3min XYZ          ← toujours commence par "Eco3min "
 * Version: X.Y.Z
 * Author: Eco3min
 */

// Nonces AJAX systématiques + capability check
check_ajax_referer('eco3min_lc_nonce', 'nonce');  // legacy
check_ajax_referer('eco3min_mega_nonce', 'nonce'); // mega
if (!current_user_can('manage_options')) {
    wp_send_json_error(['message' => 'Permission denied']);
}

// Chunks AJAX ≤ 50 posts pour éviter timeouts
```

### 11.4 Architecture fichiers d'un plugin type

**Plugin legacy** :
```
eco3min-{name}/
├── eco3min-{name}.php          (entry point + headers + require)
├── includes/
│   ├── class-installer.php     (création tables BDD on activate)
│   ├── class-{logic}.php       (logique métier)
│   ├── class-applier.php       (writes vers BDD si applicable)
│   ├── class-tree.php          (read-only views si applicable)
│   └── class-admin.php         (UI WP admin + AJAX handlers)
└── assets/
    ├── css/admin.css
    └── js/admin.js
```

**Mega-plugin** (architecture multi-onglets) :
```
eco3min-mega/
├── eco3min-mega.php
├── includes/
│   ├── class-installer.php          (création des 5 tables e3m_*)
│   ├── class-classifier.php         (set_meta_safe + garde-fou immutabilité)
│   ├── class-polylang-bridge.php    (encapsulation Polylang)
│   ├── class-category-resolver.php  (résolution slug → term_id)
│   ├── class-importer-cluster.php   (Format C v1.1 bilingue)
│   ├── class-scanner.php            (V0.5+ : remplace Site Audit)
│   ├── class-state-machine.php      (V0.5+ : calcul état green/orange/red)
│   ├── class-exporter-full.php      (V0.5+ : Format A descriptif)
│   ├── class-exporter-light.php     (V0.5+ : Format B prescriptif chunked)
│   └── admin/
│       ├── class-tab-1-referentiel.php
│       ├── class-tab-2-classification.php  (V0.5+)
│       ├── class-tab-3-import-cluster.php
│       ├── class-tab-4-maillage.php
│       └── class-tab-5-graph.php           (V1.0+)
└── assets/
    ├── css/admin.css           (préfixe .eco3-mega-)
    └── js/{tab-1,tab-2,...}.js
```

### 11.5 Conventions CSS

```css
/* TOUTES les classes plugin préfixées eco3- pour éviter conflits Blocksy */
.eco3-lc-stat-card { ... }
.eco3-lc-progress-bar { ... }

/* Mega : préfixe .eco3-mega- */
.eco3-mega-tinder-card { ... }
.eco3-mega-state-badge--green { ... }

/* !important souvent nécessaire pour override Blocksy */
.eco3-lc-progress-fill {
    background: var(--gold) !important;
}

/* Pour le Hub : namespace .e3hub-wrap pour scoper TOUT le CSS */
.e3hub-wrap h2 { ... }   /* OK */
h2 { ... }               /* INTERDIT, casserait le WP admin */
```

### 11.6 Conventions JS

```js
(function ($) {
    'use strict';
    // Config injectée par PHP via wp_localize_script
    // EcoLCConfig = { ajaxUrl, nonce, ... };

    $.post(EcoLCConfig.ajaxUrl, {
        action: 'eco3min_lc_backfill_chunk',
        nonce: EcoLCConfig.nonce,
        offset: 0,
        limit: 25
    }, function (resp) {
        if (!resp.success) {
            showError(resp.data && resp.data.message);
            return;
        }
        // ...
    });

    function escHtml(s) { return $('<div>').text(s || '').html(); }
})(jQuery);
```

---

## 12. Design tokens du Hub

Le Hub Eco3min utilise un design system dark cohérent. Si on étend le Hub ou crée un plugin avec UI similaire, réutiliser ces tokens (déclarés dans `eco3min-hub/assets/css/admin.css`).

```css
:root {
    /* Backgrounds */
    --bg: #0a0a0c;
    --bg-elev: #131316;
    --bg-elev-2: #1a1a1e;
    --border: #25252b;
    --border-bright: #3a3a42;

    /* Texte */
    --text: #ece8de;
    --text-dim: #8a8a92;
    --text-muted: #5a5a62;

    /* Accents */
    --gold: #d4a418;
    --gold-soft: #c9a04b;
    --green: #6bc46d;
    --red: #e74c3c;
    --orange: #e88c3a;
    --orange-bg: rgba(232, 140, 58, 0.12);
    --orange-border: rgba(232, 140, 58, 0.4);

    /* Fonts */
    --display: 'Fraunces', Georgia, serif;          /* titres */
    --body: 'IBM Plex Sans', system-ui, sans-serif; /* corps */
    --mono: 'JetBrains Mono', Consolas, monospace;  /* code, badges */
}
```

**Verrouillage de l'état** : dans le Hub, une card avec un prérequis non rempli est marquée `🔒 verrouillé` en orange (border + bg via `--orange-border` + `--orange-bg`). Ne pas réutiliser le rouge `--red` pour ça (réservé aux erreurs critiques).

**Couleurs d'état mega** : `e3m_articles.state_color` prend trois valeurs alignées avec ces tokens — `green` (article complet, maillage OK), `orange` (article complet, maillage à compléter), `red` (article incomplet ou orphelin). Voir `plugins-eco3min` section 12 pour la state machine V0.5+.

---

## 13. Heuristiques de classification (résumé du Level Classifier)

Pour comprendre comment un article est classifié automatiquement, ou pour expliquer pourquoi un article a été classé d'une certaine façon. Source : `eco3min-level-classifier/includes/class-classifier.php`. La même heuristique est portée dans `Eco3min_Mega_Classifier::suggest_level()` à partir de V0.5.

### 13.1 Patterns URL prioritaires

| Pattern URL | Level suggéré (score élevé) |
|---|---|
| 1 segment ∈ pillars | `pillar` (+30) |
| 2 segments avec 1er ∈ pillars | `sub_pillar` (+12) — **règle correcte**, le classifieur travaille sur la permalink WordPress, pas sur la colonne `url` du snapshot (cf. §2.1). Signal d'appoint : le slug est utilisé comme valeur `_eco3min_sub_pilier` par ≥1 autre page |
| URL contient `/qa/` ou `/qr/` | `faq` (+20) |
| URL contient `dataset` ou `donnees` | `dataset` (+8) |
| URL contient `outil` ou `tool` | `tool` (+8) |

### 13.2 Word count

| Range | Bonus |
|---|---|
| ≥ 4500 mots | `major_article` +5 |
| ≥ 3500 et < 4500 | `major_article` +3 |
| ≥ 3000 mots | `deep_study` +2 |
| 500-2500 mots | `satellite` +4 |
| 2500-4000 mots | `satellite` +2 |
| 1500-3500 mots | `foundation_article` +1 |

### 13.3 Mots-clés du titre (insensible aux accents)

| Level | Mots-clés FR | Mots-clés EN |
|---|---|---|
| `foundation_article` | fondamentaux, introduction, principe, comprendre, guide, bases, definition, qu'est-ce | fundamentals, basics, introduction to, understanding, foundations |
| `deep_study` | etude, analyse, historique, histoire, donnees, depuis 19/20, quantitatif | study, analysis, history, since 19/20, quantitative, historical, data series |
| `case_study` | crise de, episode de, cas de, choc de, krach, Volcker, Lehman, COVID, mer rouge | crisis of, shock of, episode of, case of, crash |
| `dataset` | dataset, donnees, serie, data | (idem) |
| `tool` | outil, calculateur, simulateur, diagnostic | tool, calculator, simulator |
| `beginner` | debutant, commencer, pour les nuls, pas a pas | beginner, getting started, how to start, step by step |

### 13.4 Détection FAQ supplémentaire

- Titre commençant par : comment, pourquoi, qu'est-ce, qui, quand, ou / how, why, what, when, where, who, is it, does, can, should
- Titre se terminant par `?` (+3)

### 13.5 Détection MAJEUR via incoming_count

Compté depuis `eco3min_sa_links` (ou `e3m_links` côté mega) :
- `SELECT COUNT(*) WHERE target_post_id = X AND is_external = 0`
- ≥ 20 liens entrants : `major_article` +4
- ≥ 10 liens entrants : `major_article` +2

### 13.6 Détection parent_major (pour les satellites)

Heuristique 1 (prioritaire) : compter les liens sortants du satellite vers chaque MAJEUR du même pilier d'attache, prendre le plus mentionné.

Heuristique 2 (fallback) : Jaccard du titre du satellite avec chaque MAJEUR du pilier (seuil minimum 0.10), prendre le plus proche.

**Note** : H1 est buggée à ce jour côté legacy (utilise `source_post_id` au lieu de `src_post_id`), donc c'est H2 qui tourne en pratique. Le mega corrige ce bug dans son scanner V0.5+. Voir section 10.2.

---

## 14. Exceptions et pièges connus

### 14.1 Sub-piliers : URL de LIEN vs parentage BDD (harmonisé juillet 2026)

Deux couches à ne pas confondre :

- **Couche liens internes (opérationnelle)** : les URLs sub-pilier constatées dans les snapshots 2026 (mai : T10Y3M ; juillet : PER) sont **PLATES** (`https://eco3min.fr/{sub-pilier-slug}/`) et c'est ce format que le maillage utilise. Règle (CI projet B V1.1.0) : format constaté dans le snapshot, jamais inféré ; le champ `slug` du snapshot est fiable, le champ `url` peut être trompeur pour des pages parentées hiérarchiquement ; ambiguïté → vérifier le site live / demander à Paul.
- **Couche parentage BDD (classification)** : une page sub-pilier peut être hiérarchiquement parentée en BDD indépendamment de son URL canonique. Le backfiller URL du legacy ne déduit le rattachement **que** depuis une URL imbriquée → les sub-piliers/satellites à URL plate lui échappent : forcer manuellement `_eco3min_cluster` et `_eco3min_level=sub_pillar` (Custom Fields, ou Tinder mega qui écrit level+cluster+sous-pilier d'un coup ; **le contrat d'import Cleanup accepte désormais `level` en overwrite réversible** en plus de `cluster`+`sub_pilier` fill-only — build juillet 2026, supersede `plugins-eco3min` §14.8, cf `metas-eco3min` §3). Ne PAS « corriger » un slug WP vers une forme imbriquée pour satisfaire le backfiller : cela casserait les liens plats existants (301 en cascade).

### 14.2 Pillars qui peuvent apparaître comme sub-pillars dans les listes

Certains piliers FR sont aussi listés comme sub-piliers d'autres piliers — exemple : `geopolitique-structurelle` est à la fois un pilier (`/geopolitique-structurelle/`) et apparaît imbriqué sous `/macroeconomie-geopolitique/geopolitique-structurelle/`. C'est normal en WordPress quand une page est attachée à plusieurs catégories. Le `_eco3min_level` reste celui défini en BDD (le plus authoritative).

### 14.3 Préfixe BDD non-standard

Le site Paul a un préfixe BDD WP custom `mod441_` (au lieu du standard `wp_`). Toujours utiliser `$wpdb->prefix` dans le code, jamais hardcoder `wp_` ni `mod441_`. Idem pour les tables mega : `$wpdb->prefix . 'e3m_articles'`, jamais `mod441_e3m_articles`.

### 14.4 SFTP / hosting

- Hosting : OVH mutualisé cluster100
- SFTP port 22, paths relatifs (`www/dataset/`)
- Pipelines GitHub Actions cron + SFTP
- Plugins-companions du thème : Blocksy, Code Snippets, RankMath SEO, Polylang (bilingue), Gutenberg
- Mega : impose Polylang actif pour l'import cluster (refus avec message d'erreur si Polylang inactif)

### 14.5 Création de catégorie WP manquante (mega)

Si l'import cluster (Format C v1.1) référence un `wp_category_slug` qui n'existe pas en BDD WP, l'import refuse avec `Catégorie WP introuvable`. Procédure :
1. Créer la catégorie via WP Admin → Articles → Catégories (s'assurer du slug exact).
2. Mega → Onglet 1 (Référentiel) → bouton "Re-résoudre catégories WP" (peuple `wp_category_id` à partir du slug).
3. Re-tenter l'import.

---

## 15. Checklist pré-livraison de code plugin

À cocher mentalement avant de livrer un ZIP de plugin Eco3min (legacy ou mega) :

**Sémantique**
- [ ] Le code respecte la hiérarchie pillar > sub_pillar > MAJEUR > satellite ?
- [ ] Les metas écrites correspondent au tableau de la section 3.1 ?
- [ ] Les `pillar` ne reçoivent **aucune** meta de catégorie ?
- [ ] Le parsing URL retire bien le préfixe `/en/` ou `/fr/` avant d'analyser les segments ?

**Conventions**
- [ ] Classes CSS préfixées `eco3-` (legacy) ou `eco3-mega-` (mega) ?
- [ ] Classes PHP préfixées selon le plugin (`Eco3min_LC_*`, `Eco3min_SA_*`, `Eco3min_Mega_*`, etc.) ?
- [ ] Constantes du plugin déclarées avec le bon préfixe (`ECO3MIN_LC_*`, `ECO3MIN_MEGA_*`, etc.) ?
- [ ] Tables avec `$wpdb->prefix` (jamais `wp_` ni `mod441_` hardcodé) ?
- [ ] Mega : Polylang via `Eco3min_Mega_Polylang_Bridge`, jamais direct ?
- [ ] Mega : metas critiques via `Eco3min_Mega_Classifier::set_meta_safe()` ?
- [ ] Mega : catégories WP résolues par slug via `Eco3min_Mega_Category_Resolver` ?

**Sécurité**
- [ ] Tous les fichiers PHP inclus commencent par `if (!defined('ABSPATH')) exit;` ?
- [ ] Tous les handlers AJAX appellent `check_ajax_referer()` + `current_user_can('manage_options')` ?
- [ ] Toutes les queries SQL avec input utilisateur passent par `$wpdb->prepare()` ?

**Performance**
- [ ] Chunks AJAX ≤ 50 posts par appel pour éviter les timeouts ?
- [ ] Pas de boucle qui appelle `get_post()` ou `get_post_meta()` pour 1000+ posts sans optimisation ?

**Robustesse**
- [ ] Si le plugin modifie `wp_posts.post_content`, il y a une table backup avec `session_id` ou `trigger_ref` (mega) pour rollback ?
- [ ] Validation PHP : `php -l fichier.php` sans erreur ?
- [ ] Validation JS : `node --check admin.js` sans erreur ?

**Conformité projet**
- [ ] Le ZIP final est dans `/mnt/user-data/outputs/` ?
- [ ] Le plugin a été présenté avec `present_files` ?

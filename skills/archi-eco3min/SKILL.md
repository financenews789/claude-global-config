---
name: archi-eco3min
description: "Architecture éditoriale et technique de référence d'Eco3min (eco3min.fr) — état vérifié le 15/09/2026 dans le dépôt eco3min-wp/plugins (mega 1.0.14) et en live (ability eco3min/taxonomy) : hiérarchie silo > pilier > sous-pilier > cluster (MAJEUR + satellites), levels `_eco3min_level` (pillar, sub_pillar, major_article, satellite, foundation_article, deep_study, case_study, dataset, faq, tool, beginner, plus les états exclu et uncategorized), les 5 metas WP (`_eco3min_level`, `_eco3min_cluster` = slug du PILIER d'attache malgré son nom, `_eco3min_sub_pilier` slug de la page sous-pilier SOURCE DE VÉRITÉ, `_eco3min_subpillar` ID dérivé pour le fil d'Ariane, `_eco3min_parent_major`), parsing d'URL bilingue (`/en/` `/fr/`), catégories WP (9 par langue, slug ≠ slug pilier), tables `e3m_*` du mega (10) avec `translation_group_id`, conventions de code (`Eco3min_Mega_*`, `ECO3MIN_MEGA_*`, `eco3-mega-`, `EcoMegaConfig`, `eco3min_mega_nonce`, sous-menus `eco3min-mega-{referentiel,scan,import_cluster,maillage,graph,manuel,diagnostic,conseil,nettoyeur}`), design tokens dark. Activer pour « quel pilier / quel sous-pilier », « c'est quoi le cluster de cette page », « quel level », « slug du sous-pilier », « quelle catégorie WP », « URL réelle d'un sous-pilier », « structure du site », « silo », « MAJEUR », « satellite orphelin », toute écriture ou relecture de code plugin, tout import qui pose des metas, toute question sur snapshot.csv / e3m_articles / e3m_links. SKILL.md = colonne vertébrale (hiérarchie et vocabulaire, table des levels, metas et doctrine slug/ID, mapping des 11 piliers FR ↔ EN, règles bloquantes, pièges, checklist de livraison) ; références dans references/ (à lire quand l'étape le dit) : 01 piège de la colonne url du snapshot, parsing URL, heuristiques réelles du mega et grille historique du Level Classifier ; 02 catégories WP avec term_id ; 03 listes des piliers et des ~97 sous-piliers FR/EN, hubs à level=pillar ; 04 listes historiques des MAJEURs, études, outils, hub débutant ; 05 les 10 tables e3m_* colonne par colonne, translation_group_id, SQL ; 06 conventions de code du mega, arborescence réelle, CSS/JS, tokens. Doctrines : `_eco3min_cluster` porte un slug de pilier, jamais un id de cluster ; le slug `_eco3min_sub_pilier` gagne sur l'ID `_eco3min_subpillar`, on ne purge jamais l'une des deux clés (juillet 2026) ; les URLs de sous-piliers sont IMBRIQUÉES (/pilier/sous-pilier/, la forme plate fait 301) et la colonne url de snapshot.csv est une reconstruction plate à ne jamais lire (deux erreurs successives en juillet et septembre 2026, prouvé dans exporter-snapshot.php) ; un pillar porte `_eco3min_cluster` = son propre slug (sinon le conseil T1/T2/T3 du mega ignore tout le silo — corrigé le 15/09/2026, les 11 piliers EN sont à rattraper) et rien d'autre, un sub_pillar porte le cluster mais pas de sous-pilier ; le slug de catégorie WP n'est pas le slug du pilier, résolution par Eco3min_Mega_Category_Resolver::resolve, jamais par term_id en dur ; jamais de SQL direct sur les 4 metas critiques, écriture via set_meta_safe ; `$wpdb->prefix` partout (préfixe réel mod441_) ; langue via pll_get_post_language, jamais _eco3min_lang ; les listes de majeurs à jour viennent de eco3min/taxonomy, pas d'une liste en dur (333 majeurs live). Level Classifier, Site Audit, Hub, Meta Monitor, Anchor Diversifier, tables eco3min_sa_links et consorts n'existent plus : ne jamais les citer comme outils. Hors périmètre : fonctionnement des plugins et du mega (onglets, imports, patches, rollback) → plugins-eco3min ; cycle de vie des metas et outils pour les poser → metas-eco3min ; rédaction et AMF → editeur-eco3min ; formats HTML → formats-eco3min ; datasets → production-dataset ; Q&A → production-q-and-a. Combiner avec plugins-eco3min, metas-eco3min, editeur-eco3min, eco3min-import-contenu-bilingue, maillage-orphelins-eco3min, patches-maillage-eco3min."
---

# Architecture Eco3min — référence technique

> Ce skill code en dur la **structure du site Eco3min** et les **conventions techniques** du mega-plugin et des plugins WordPress maison. Il couvre **comment c'est structuré**, **où c'est stocké en BDD**, **comment le code l'écrit et le lit**.
>
> Pour le **fonctionnement opérationnel des plugins** (onglets du mega, imports, patches, rollback, projets Claude Code A/B/C, bugs connus) — voir `plugins-eco3min`.
> Pour le **cycle de vie des metas** (quoi poser après création/import, snippet SYNC, Subpillar Aligner, registre des plugins avec URLs), voir `metas-eco3min`.
> Pour la **rédaction éditoriale** (style, voix, conformité AMF), voir `editeur-eco3min`. Pour les formats HTML rédactionnels (encarts, TL;DR, FAQ), voir `formats-eco3min`. Pour la production de pages dataset standardisées, voir `production-dataset`. Pour les Q&A, voir `production-q-and-a`.

---

## COMMENT LIRE CE SKILL (découpage et remise à jour du 15/09/2026)

Ce fichier est la colonne vertébrale : la hiérarchie, la table des levels, les metas et leur doctrine, le mapping des piliers, chaque règle BLOQUANTE, les pièges et la checklist de livraison. Le détail (listes complètes de sous-piliers, majeurs, catégories, colonnes des tables, conventions de code, heuristiques) vit dans `references/` et fait foi au même titre que ce fichier. Chaque section ci-dessous nomme le fichier à lire ; le lire est obligatoire au moment indiqué, pas facultatif.

État de référence : dépôt `~/eco3min/eco3min-wp/plugins/` (mega **1.0.14**) confronté au live via l'ability MCP `eco3min/taxonomy` (scopes `pillars`, `sub_pillars`, `levels`) et à des `curl` de permaliens, le 15/09/2026. Le Level Classifier, Site Audit, Hub, Meta Monitor, Anchor Diversifier, Redundant Cleaner, GSC Linker, Dataset Monitor, Maillage Audit et leurs tables `eco3min_*` **n'existent plus** (désinstallés, tables droppées le 15/09/2026) : ne jamais les citer comme outils ni comme source de code. Deux sections de l'original portaient le numéro « 3.1 » (tableau d'écriture des metas, catégories WP) : les deux titres sont conservés tels quels, la seconde vit dans la référence 02. Les numéros de sections sont ceux de l'original (d'autres skills y renvoient) : les §6-9, 12 et 13 n'apparaissent que dans les références.

| Fichier | Contenu | À lire |
|---|---|---|
| `references/01-levels-url-snapshot-heuristiques.md` | §2.1 intégral (pourquoi la colonne `url` du snapshot a produit deux erreurs), §4 parsing d'URL (algorithme + qui l'implémente aujourd'hui), §13 heuristiques réelles du mega (`suggest_classification`) et grille historique du Level Classifier | avant de classifier une page, d'expliquer un level suggéré, ou de déduire une URL / un rattachement depuis un slug ou un snapshot |
| `references/02-categories-wp.md` | §3.1 catégories WordPress : 9 catégories FR / 9 EN avec `term_id`, hubs sans catégorie, piège de collision `commodities-global-economy` | avant de préparer un import Format C (`wp_category_slug`), de créer une catégorie, ou de diagnostiquer `Catégorie WP introuvable` |
| `references/03-piliers-sous-piliers.md` | §5.1-5.3 piliers FR/EN avec thèmes, §6 les ~97 sous-piliers FR/EN par pilier (ajouts live 15/09/2026 inclus), hubs déclarés `level=pillar` sans silo | avant de poser ou valider un `_eco3min_cluster` / `_eco3min_sub_pilier`, un `cluster` ou `sub_pilier` d'import, ou une liste de pages d'un pilier |
| `references/04-majeurs-etudes-outils-hub.md` | §7-9 listes historiques (juin 2026) des MAJEURs, datasets-études, articles de fond, études de cas, outils, hub débutant | avant de citer un majeur ou une étude par son slug — puis confronter à `eco3min/taxonomy scope=majors` (333 majeurs live) |
| `references/05-tables-bdd.md` | §10 les 10 tables `e3m_*` du mega colonne par colonne, `translation_group_id`, leçon `src_post_id`, requête paires FR/EN | avant toute requête SQL, tout code qui lit `e3m_articles` / `e3m_links`, ou une question sur l'état d'un article dans le mega |
| `references/06-conventions-code-design-tokens.md` | §11 conventions de code (préfixes, constantes, AJAX, arborescence réelle du mega, PHP/CSS/JS), §12 design tokens dark | avant d'écrire, relire ou patcher du code de plugin Eco3min |

Pas de `scripts/` : rien dans cette skill n'est du code recopié de production en production.

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

## 2. Les levels (lire `references/01-levels-url-snapshot-heuristiques.md` avant de classifier)

`_eco3min_level` prend 11 valeurs cibles (table ci-dessous) plus deux états : `uncategorized` (état de départ avant classification) et `exclu` (page volontairement sortie du maillage).

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
| `exclu` | Bruit exclu du maillage (pages système, hubs fonctionnels, archives) — posé par le plugin Cleanup section 1, accepté par Level Setter | 65 pages au 15/09/2026 ; jamais maillé par le conseil |

**Répartition live au 15/09/2026** (`eco3min/taxonomy scope=levels`) : satellite 1260 · faq 615 · major_article 333 · dataset 210 · sub_pillar 97 · exclu 65 · tool 45 · pillar 31 · uncategorized 24 · beginner 13 · foundation_article 10 · case_study 4 · **deep_study 0** (level valide, inutilisé : les études vivent en `major_article`, cf `plugins-eco3min` §14.8).

**Source des valeurs** : `Eco3min_Mega_Validator::VALID_LEVELS` (`includes/helpers/class-eco3min-mega-validator.php:39`) pour l'import Format C — 11 valeurs **sans `satellite`** (un satellite importé est déclaré par son `parent_major_pair_id`) ; `Eco3min_Level_Setter::LEVELS` (12 valeurs, avec `exclu`, sans `satellite`) ; le Tinder du mega propose les 11 levels avec `satellite`. Ne pas inventer de level supplémentaire.

### 2.1 Règle BLOQUANTE — la colonne `url` de `snapshot.csv` est une reconstruction plate

- **Les URLs de sous-piliers sont IMBRIQUÉES** : `/{pilier-slug}/{sub-pilier-slug}/` en FR, `/en/{pilier-slug}/{sub-pilier-slug}/` en EN. Vérifié en base le 04/09/2026 (`eco3min/find`, 8/8) et par `curl` le 15/09/2026 : la forme plate répond **301** vers la forme imbriquée (`/banques-centrales-actions/` → `/politique-monetaire-taux/banques-centrales-actions/` ; `/en/crisis-hub/` → `/en/macro-financial-regimes/crisis-hub/` ; `/etf-debutant/` → `/apprendre-investir/etf-debutant/`).
- **Le champ `slug` du snapshot est fiable.** Il vient de la base.
- **Le champ `url` ne l'est pas sous mega ≤ 1.0.15.** Il est reconstruit à plat et se trompe sur tout ce qui est parenté hiérarchiquement — sous-piliers, Q&A, hubs. Prouvé dans le code : `class-eco3min-mega-exporter-snapshot.php` (`format_article`) construisait `home_url() . '/' . slug . '/'` (ou `/en/` + slug) pour toutes les lignes. **Corrigé dans le mega 1.0.16 (dépôt, 17/09/2026)** : la colonne vaut `get_permalink()`. Un `snapshot.csv` n'est fiable sur `url` que s'il a été exporté par un mega ≥ 1.0.16 (vérifier la version live par `ewpa/get-active-plugins` ; l'en-tête ligne 1 du CSV cite la version du mega). Le 1.0.16 est en ligne depuis le 17/09/2026 au soir et `context/snapshot.csv` a été ré-exporté avec (URL imbriquées vérifiées sur les sous-piliers) ; seuls des exports antérieurs restent plats.
- Pour une URL réelle : `eco3min/find` ou `eco3min/get-content` renvoient la **permalink** calculée par WordPress. C'est la seule source.
- **Ne jamais inférer une structure de permalien**, ni depuis le snapshot, ni depuis un pattern supposé.
- Sur une page `sub_pillar` elle-même, `_eco3min_sub_pilier` est **vide** et `_eco3min_subpillar` vaut `0` — c'est normal.

Historique des deux erreurs (juillet et septembre 2026) et signal secondaire de classification : lire `references/01-levels-url-snapshot-heuristiques.md`.

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
| `pillar` | ✅ | **son propre slug** (requis par le conseil T1/T2/T3 du mega — corrigé le 15/09/2026, cf règles ci-dessous) | — | — |
| `sub_pillar` | ✅ | slug pilier parent | — | — |
| `major_article` | ✅ | slug pilier parent | slug page sous-pilier parent | — |
| `satellite` | ✅ | slug pilier | slug page sous-pilier | post_id du MAJEUR (systématique sinon orphelin) |
| `deep_study` / `case_study` | ✅ | slug pilier | slug page sous-pilier | parfois |
| `foundation_article` | ✅ | slug pilier | slug page sous-pilier | parfois |
| `faq` / `dataset` / `tool` | ✅ | slug pilier | slug page sous-pilier | parfois |
| `beginner` | ✅ | slug pilier (= `apprendre-investir` ou EN equivalent) | slug page sous-pilier si applicable | rarement |

> Note : la valeur qu'on POSE est le **slug** (`_eco3min_sub_pilier`) — via import cluster, Tinder mega ou Cleanup. L'ID (`_eco3min_subpillar`) suit **automatiquement** (snippet SYNC ; sinon Aligner). En saisie unitaire, la metabox « Sous-pilier (Page) » reste utilisable : elle écrit l'ID, aussitôt reconverti en slug canonique. Détail des outils → `metas-eco3min`.

**Règles fondamentales** :
- Un `pillar` porte `_eco3min_cluster` = **son propre slug** et aucune autre meta de rattachement (ni sous-pilier, ni parent_major). **Corrigé le 15/09/2026** : la règle antérieure (« aucune meta de catégorie ») est contredite par le code du conseil — `Eco3min_MU_Analyzer::build_cluster_routing()` (`class-eco3min-mu-analyzer.php:163-169`) ne trouve le `pillar_post_id` d'un cluster que si le pilier lui-même porte `_eco3min_cluster` = ce slug ; sans lui, aucun lien T1 `sub_pillar → pillar`, T2 `major → pillar` ni T3 `pillar → sub_piliers` n'est jamais proposé pour ce silo, et le pilier est ignoré comme source (`if (empty($cluster)) return`, l.222).
- Un `sub_pillar` reçoit `_eco3min_cluster` (slug pilier parent) mais **aucune** meta sous-pilier (ni slug ni ID : il *est* un sub-pilier, pas attaché à un autre).
- Un `satellite` est le **seul** level systématiquement relié à un MAJEUR via `_eco3min_parent_major`. S'il n'en a pas, il est orphelin (visible dans l'onglet Diagnostic du mega, `eco3min/health`, ou `eco3min/taxonomy scope=clusters`).
- Le code n'écrase **jamais** une meta déjà remplie — le backfill ne touche que les meta vides.

> ⚠️ Constat live 15/09/2026 (`eco3min/taxonomy scope=pillars`) : 10 piliers FR sur 11 portent bien leur propre slug (`apprendre-investir` non), **les 11 piliers EN ont `_eco3min_cluster` vide** — le conseil de maillage ne peut donc proposer aucun lien vers ou depuis un pilier EN. **Corrigé le 15/09/2026** via `ewpa/update-post-meta` (11 pages : 10 EN + `apprendre-investir`) ; les 9 hubs fonctionnels restent sans cluster, volontairement. Eco3min MCP 1.1.1 (déployé le 15/09/2026) applique la règle corrigée : `set-metas` accepte `cluster` = slug propre sur un pillar, `health` → `pillar_violations` 0 et `pillar_without_cluster` = les 9 hubs.

### 3.2 Source de vérité — règle non négociable

Les metas WP `_eco3min_*` sont la **source unique de vérité** de la classification éditoriale. Aucun autre lieu de stockage ne fait foi :
- Le mega-plugin (table `e3m_articles`, voir `references/05-tables-bdd.md`) **mirroite** ces metas pour ses besoins propres mais ne les définit jamais.
- Les writes sur ces metas par le mega passent obligatoirement par `Eco3min_Mega_Classifier::set_meta_safe()` avec garde-fou immutabilité (throw `Eco3min_Mega_Immutability_Exception` en cas de tentative d'écrasement). Voir `plugins-eco3min` section 12.4.
- Pour modifier une classification existante : Cleanup (import `attachments`, `level` en overwrite réversible), Tinder du mega, Level Setter, metabox « Sous-pilier (Page) » ou `eco3min/set-metas` — jamais via SQL direct. Outils et ordre → `metas-eco3min`.

### 3.3 Catégories WordPress — règle BLOQUANTE (lire `references/02-categories-wp.md` avant un import)

- **Le slug de catégorie WP n'est PAS le slug du pilier.** Il est plus court, structuré différemment, et **diffère entre FR et EN**. Un import qui réutilise le slug de pilier comme `wp_category_slug` échoue avec `Catégorie WP introuvable`.
- **Neuf** catégories par langue, pas onze : les hubs `apprendre-investir` / `investing-for-beginners-hub` et `donnees-analyses-macro-financieres` / `research-data` n'en ont aucune.
- Résolution toujours **par slug** via `Eco3min_Mega_Category_Resolver::resolve($slug)`, jamais par `term_id` codé en dur. Catégorie manquante → la créer dans WP Admin, puis Mega → Référentiel → « 🔄 Re-résoudre les catégories WP », puis relancer l'import (§14.5).

---

## 4. Parsing d'URL bilingue (lire `references/01-levels-url-snapshot-heuristiques.md` §4)

Règle : retirer le préfixe `/en/` ou `/fr/` **avant** d'analyser les segments ; 1 segment = pilier (ou hub), 2 segments = `pilier/sous-pilier`. Implémenté aujourd'hui dans `Eco3min_Mega_Scanner::suggest_classification()` (`class-eco3min-mega-scanner.php:523`) et dans la détection des hubs du Cleanup (`eco3min-cleanup.php:533`). Un `pillar` retourne `pilier=null, sub_pilier=null` ; un `sub_pillar` retourne `pilier=segment[0]` et `sub_pilier=null`.

**Note langue (Polylang)** : la langue d'un post est lue via `pll_get_post_language($id)` (taxonomie Polylang), pas via la postmeta `_eco3min_lang` qui peut être obsolète. Le mega utilise systématiquement `Eco3min_Mega_Polylang_Bridge::get_post_language()` qui encapsule cet appel.

---

## 5. Les 11 piliers — mapping FR ↔ EN (lire `references/03-piliers-sous-piliers.md` pour les thèmes, les sous-piliers et les hubs)

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

Ces 11 paires sont les piliers **éditoriaux** (silos). Au 15/09/2026, 31 pages portent `level=pillar` : les 22 ci-dessus plus **9 hubs fonctionnels** déclarés pilier par le Cleanup (section 3 : page à 1 segment avec enfants) — `qr`, `qa`, `comparatif`, `compare`, `idees-recues`, `mistakes`, `lectures-eco3min`, `outils-analyse-macroeconomique`, `macroeconomic-analysis-tools`. Ils n'ont ni sous-pilier ni cluster : ne jamais les proposer comme `_eco3min_cluster` d'un contenu maillé (`pillar`, `sub_pillar`, `major_article`, `satellite`, études, datasets, outils). **Doctrine Q&A figée le 17/09/2026** : une page `faq` porte le **pilier thématique** de sa langue en cluster et le sous-pilier dominant de ses liens sortants ; `qa` / `qr` ne sont que le **repli** d'une Q&A sans signal thématique fiable (règle et méthode d'inférence dans `metas-eco3min` §9.4, contrat de création dans `production-q-and-a` §11.6).

Les sous-piliers (97 pages `sub_pillar`, dont 8 sans enfants) sont listés pilier par pilier dans la référence 03 ; `eco3min/taxonomy scope=pillars` donne l'état live avec `attached_count`. Les MAJEURs (333 au 15/09/2026), études, outils et hub débutant : lire `references/04-majeurs-etudes-outils-hub.md` avant de citer un slug, puis confronter à `eco3min/taxonomy scope=majors`.

---

## 10. Tables BDD du mega (lire `references/05-tables-bdd.md` avant tout SQL)

- **10 tables `e3m_*`** créées par `Eco3min_Mega_Installer` : `e3m_referentiel`, `e3m_articles`, `e3m_links`, `e3m_patches_log`, `e3m_backups` (V0.1) + `e3m_qa_clusters`, `e3m_scan_state`, `e3m_imports_log`, `e3m_tinder_queue`, `e3m_multi_import_sessions` (V1.0). Le préfixe `e3m_` est aussi utilisé par six autres plugins (404, 301, Accents, Anchor Doctor, Anchor Retarget, Patch Audit) : ne jamais dropper sur la foi du préfixe.
- Toutes les tables legacy `eco3min_sa_links`, `eco3min_lc_suggestions`, `eco3min_ad_*`, `eco3min_rc_*`, `eco3min_ah_snapshots`, `eco3min_dm_health`, `eco3min_gsc_*`, `eco3min_audit_pillars` ont été **droppées le 15/09/2026**. Le graphe de liens, c'est `e3m_links` (`src_post_id` / `target_post_id`, jamais `source_post_id` ni `from_*`).
- `e3m_articles` est un **miroir** des metas WP (§3.2) : `level`, `cluster_slug`, `sub_pilier_slug`, `parent_major_post_id`, `translation_group_id` (BIGINT, `MAX+1`, pas un UUID), `state` / `state_color`.
- Toujours `$wpdb->prefix . 'e3m_articles'` dans le code (préfixe réel du site : `mod441_`).

---

## 11. Conventions de code (lire `references/06-conventions-code-design-tokens.md` avant d'écrire du code)

Préfixes du mega : tables `e3m_`, constantes `ECO3MIN_MEGA_*` (+ `ECO3MIN_META_PREFIX = '_eco3min_'`), classes `Eco3min_Mega_*` et `Eco3min_MU_*` (maillage ultime), CSS `eco3-mega-`, AJAX `eco3min_mega_*` + nonce `eco3min_mega_nonce`, config JS unique `EcoMegaConfig` (`ajax_url`, `nonce`), cron `eco3min_mega_daily_scan`, capability `manage_options`, menu `eco3min-mega` + sous-menus `eco3min-mega-{referentiel,scan,import_cluster,maillage,graph,manuel,diagnostic,conseil,nettoyeur}`. Les metas restent `_eco3min_*`, jamais `_e3m_*`.

**Règles non-négociables du mega** :
- Tous les appels Polylang passent par `Eco3min_Mega_Polylang_Bridge::*`, jamais direct.
- Tous les writes sur metas critiques passent par `Eco3min_Mega_Classifier::set_meta_safe()`.
- Toute résolution de catégorie WP se fait par slug via `Eco3min_Mega_Category_Resolver::resolve($slug)` (jamais par term_id hardcodé).

---

## 14. Exceptions et pièges connus

### 14.1 Sous-piliers : URL imbriquée, rattachement par meta (corrigé le 15/09/2026)

- L'URL canonique d'un sous-pilier est **imbriquée** (§2.1) ; un lien interne écrit à plat déclenche un **301** — c'est ce que le « Correcteur de liens 301 » répare. Ne jamais écrire un lien vers un sous-pilier depuis la colonne `url` du snapshot : prendre la permalink (`eco3min/find`).
- Le rattachement d'une page à un pilier / sous-pilier ne se déduit **pas** de son URL : il se lit dans `_eco3min_cluster` et `_eco3min_sub_pilier`, et il se pose par import Cleanup (`level` overwrite réversible + `cluster` + `sub_pilier` fill-only), Tinder du mega ou `eco3min/set-metas` (→ `metas-eco3min`). Une page à URL plate (satellite, hub) peut très bien être rattachée en BDD.
- Ne PAS « corriger » un slug WP vers une forme imbriquée pour satisfaire un pattern d'URL : cela casserait les liens existants (301 en cascade).

### 14.2 Une page n'a qu'un level

`geopolitique-structurelle` (post 1663) est un `sub_pillar` de `macroeconomie-geopolitique` (`/macroeconomie-geopolitique/geopolitique-structurelle/`), pas un pilier — la version antérieure de ce skill le décrivait comme les deux. Quand une page apparaît dans deux listes (catégories WP multiples, ancien slug), le `_eco3min_level` en BDD fait foi ; vérifier par `eco3min/taxonomy scope=pillars` avant de trancher.

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
- [ ] Les `pillar` portent `_eco3min_cluster` = leur propre slug et **aucune** meta sous-pilier / parent_major ?
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
- [ ] Le code est dans `~/eco3min/eco3min-wp/plugins/<slug>/` (source déployable, git puis SFTP) et l'en-tête `Version:` est bumpé ?
- [ ] Rien n'est livré vers un chemin claude.ai (`/mnt/user-data/outputs/`, `present_files`) : ces canaux n'existent plus.

---
name: plugins-eco3min
description: "Référence opérationnelle de la suite WordPress Eco3min (eco3min.fr) — état vérifié le 15/09/2026 dans le dépôt eco3min-wp/plugins et en live (ewpa/get-active-plugins). Activer pour toute question sur un plugin maison, un onglet du mega, une table e3m_* ou eco3min_*, une meta _eco3min_*, et pour « lance un scan », « donne-moi le conseil de maillage », « importe le cluster », « applique les patches », « rollback », « passe ces pages en majeur », « rattache ces satellites », « quel plugin fait quoi », « quelle URL wp-admin », « le snippet 226 », « patche ce snippet ». Cœur = Eco3min Mega 1.0.16 (lot du 17/09/2026, en ligne le soir même) : 9 onglets (Référentiel, Scan & Classification/Tinder, Import cluster Format C v1.1 en batch unique par drag & drop — level `satellite` accepté depuis 1.0.15 avec `parent_major_pair_id` obligatoire —, Maillage = snapshot JSON + CSV snapshot/maillage, exports AVEC/SANS HTML, import patches v1.0.2 chunked, rollback, Graphique, Manuel, Diagnostic, Conseil maillage T1/T2/T3, Réconciliation), tables e3m_*, garde-fou d'immutabilité set_meta_safe ; pré-requis du conseil = plugin Cleanup (bruit → exclu, rattachement par import attachments, hubs → pillar). SKILL.md = colonne vertébrale (tableau des 26 plugins actifs + le snippet Fix, avec version, rôle et URL, workflow canonique classer → Cleanup → scan → Conseil, pipeline cluster bilingue snapshot CSV → projet A → projet B bundle → import batch → scan → export AVEC HTML manuel → projet C → import patches, règles non négociables, diagnostic rapide, tables de décision) ; références dans references/ (à lire quand l'étape le dit) : 01 inventaire détaillé, plugins disparus, tables legacy à dropper ; 02 pipeline pas à pas, projets Claude Code A/B/C (dossiers Eco3min Cluster Builder de eco3min-projets ; plus aucun projet claude.ai), cas opérationnels ; 03 versions du mega, immutabilité, Format C v1.1, conventions ; 04 format patches v1.0.2 ; 05 tables, bugs durables, SQL ; 06 promotion en major_article ; 07 pièges Code Snippets. Doctrines : le conseil ne maille QUE pillar/sub_pillar/major_article/satellite et ignore tout article sans _eco3min_cluster ; Cleanup accepte level en overwrite réversible, donc un seul import pose level + cluster + sous-pilier (supersede l'ancien « deux outils Fix + Cleanup », vérifié dans le code le 15/09/2026) ; le Tinder mega et tous les imports écrivent le SLUG _eco3min_sub_pilier, jamais l'ID ; re-scan mega obligatoire entre deux imports (bandeau dirty) ; jamais de SQL direct sur les 4 metas critiques ; new chat Claude entre deux batches ; cap SEO = diversité des ancres ; ewpa/create-code-snippet crée un doublon inactif et ne met rien à jour — un snippet se patche par eco3min/snippet-update (Eco3min MCP 1.2.x, sonde loopback, auto-restauration, rollback), plus jamais par copier-coller wp-admin. Level Classifier, Maillage Audit, Maillage Cluster, Classify Backfill, Site Audit, Hub, GSC Linker, Dataset Monitor, Pillar Audit, SQL Runner, Meta Monitor, Anchor Diversifier, Redundant Cleaner, Performance Dashboard, Anchor Health et les exports LIGHT/Format B n'existent plus : ne jamais les proposer. Hors périmètre : structure éditoriale (silos, levels, sémantique des metas) → archi-eco3min ; cycle de vie des metas et registre des contrats → metas-eco3min ; rédaction et AMF → editeur-eco3min ; bundles d'import de pages → eco3min-import-contenu-bilingue ; rédaction des patches → patches-maillage-eco3min. Combiner avec archi-eco3min, metas-eco3min, patches-maillage-eco3min, maillage-orphelins-eco3min, cluster-ticker-renfort-dataset, eco3min-import-contenu-bilingue."
---

# Suite de plugins Eco3min — référence opérationnelle

> Ce skill code en dur **comment fonctionne la suite de plugins WordPress Eco3min**, le **mega-plugin** qui a absorbé la chaîne de maillage, et les **3 projets Claude** qui orchestrent le pipeline éditorial bilingue.
>
> Pour la structure éditoriale du site (silos, piliers, levels, metas WP), voir `archi-eco3min`. Pour le cycle de vie des metas et le registre détaillé des contrats d'entrée, voir `metas-eco3min`. Pour la rédaction (style, AMF), voir `editeur-eco3min`.

---

## COMMENT LIRE CE SKILL (découpage et remise à jour du 15/09/2026)

Ce fichier est la colonne vertébrale : l'inventaire des plugins **actifs**, le workflow canonique, chaque règle NON NÉGOCIABLE, le diagnostic rapide et les tables de décision. Le détail (rôle de chaque plugin, pipeline pas à pas, versions du mega, formats JSON, SQL, bugs, promotion en majeur, pièges Code Snippets) vit dans `references/` et fait foi au même titre que ce fichier. Chaque section ci-dessous nomme le fichier à lire ; le lire est obligatoire au moment indiqué, pas facultatif.

État de référence : dépôt `~/eco3min/eco3min-wp/plugins/` (source déployable) confronté au live via l'ability MCP `ewpa/get-active-plugins` le 15/09/2026. Tout plugin absent de cette liste **n'existe plus sur le site** : ne pas le proposer, ne pas décrire ses onglets.

| Fichier | Contenu | À lire |
|---|---|---|
| `references/01-inventaire-plugins-actifs.md` | §1.1-1.3, §3, §12.2, §15 : rôle, URL wp-admin, contrat d'entrée et statut de chaque plugin actif ; plugins absorbés ou disparus ; tables en base après le nettoyage du 15/09 (22 vivantes, 19 droppées) | avant de répondre sur le rôle ou le statut d'un plugin, de donner une URL, de désactiver ou de dropper |
| `references/02-pipelines-projets-claude-methode.md` | §2, §13, §14.1-14.7 : pipeline cluster bilingue en 8 étapes (v1.0.14), projets A/B/C, cas opérationnels (optimisation, classification, import raté, rollback) | avant de guider un cycle (cluster bilingue, conseil de maillage, patches, rollback) |
| `references/03-mega-versions-immutabilite-format-c.md` | §10, §12.1, 12.3-12.6 : versions du mega, garde-fou d'immutabilité, Format C v1.1, conventions de code | avant de toucher au code du mega ou de préparer/valider un JSON Format C |
| `references/04-format-patches-v102.md` | §6 : format strict des patches, règles dures, règles soft, variation des ancres | avant de générer ou valider un `patches.json` |
| `references/05-tables-sql-bugs-diagnostic.md` | §4, §5, §7 : tables `e3m_*` et legacy, bugs durables, presets SQL | dès qu'un comportement est bizarre ou qu'une requête SQL est demandée |
| `references/06-promotion-majeur-cleanup-fix.md` | §14.8 : passer des pages en `major_article` — contrat Cleanup (level inclus), Fix, Level Setter, gâches | avant de passer des pages en majeur ou de rattacher des pages neuves |
| `references/07-code-snippets-pieges.md` | §16 : `ewpa/create-code-snippet`, export local vs live, snippet 226 | avant de patcher un snippet Code Snippets ou de toucher au snippet 226 |

Pas de `scripts/` : rien dans cette skill n'est du code recopié de production en production.

---

## 1. Vue d'ensemble — état vérifié le 15/09/2026 (lire `references/01-inventaire-plugins-actifs.md`)

> Toute la chaîne de maillage a été absorbée par le **mega-plugin**. Le **conseil de maillage T1/T2/T3 se fait UNIQUEMENT dans le mega** (onglet 🧭 Conseil maillage), après un passage **obligatoire** par le plugin **Cleanup**. Le Level Classifier, Maillage Audit, Maillage Cluster, Classify Backfill, Site Audit, Hub, GSC Linker, Dataset Monitor, Pillar Audit, SQL Runner, Meta Monitor, Anchor Diversifier, Redundant Cleaner, Performance Dashboard, Anchor Health et les backfills Sub-pilier / Major-EN **n'existent plus sur le site** (ni actifs, ni dans le dépôt) — leurs leçons durables sont conservées en §8 et dans la référence 05.

### 1.1 Plugins ACTIFS (26 extensions maison + le snippet Fix, live 15/09/2026, reconfirmé le 17/09/2026 : versions live = versions du dépôt)

Préfixe des URLs : `https://eco3min.fr/wp-admin/`. `admin.php?page=` = menu principal, `tools.php?page=` = menu Outils. Slugs relevés dans le code (`add_menu_page` / `add_management_page`), jamais inventés.

| Plugin | Version | Rôle | URL |
|---|---|---|---|
| **Eco3min Mega** | **1.0.16** (lot du 17/09/2026, en ligne le soir même) | **Cœur du système.** 9 onglets : 📋 Référentiel · 📡 Scan & Classification (scanner read-only + Tinder set/get du level) · 📥 Import cluster (Format C v1.1, batch unique ou multi-pair, drag & drop ; **`satellite` accepté depuis 1.0.15**, `parent_major_pair_id` obligatoire) · 🔗 Maillage (snapshot JSON + **CSV snapshot/maillage depuis 1.0.14**, exports AVEC/SANS HTML, import patches v1.0.2 chunked, historique + rollback) · 🕸️ Graphique · 📚 Manuel · 🩺 Diagnostic (`pillar_without_cluster` depuis 1.0.15) · 🧭 **Conseil maillage T1/T2/T3** (lit `e3m_links`) · 🧹 Réconciliation (conflits slug/ID, suppression réversible des ID). Tables `e3m_*`. | `admin.php?page=eco3min-mega` puis `eco3min-mega-{referentiel,scan,import_cluster,maillage,graph,manuel,diagnostic,conseil,nettoyeur}` |
| **Eco3min Cleanup** | **1.2.0** (lot du 17/09/2026, en ligne) | **PRÉ-REQUIS du conseil.** 3 sections, tout réversible : (1) **exclut le bruit** (pages système → `level=exclu`) ; (2) **rattache les satellites orphelins** (export JSON → révision par Claude → **Prévisualiser** → import `{"attachments":[{post_id, level?, cluster, sub_pilier, parent_major?}]}` — **`level` accepté en overwrite réversible**, cluster/sub_pilier/parent_major fill-only, résultat ligne par ligne avec raison, backup `_e3mc_bak_pm`, « Restaurer les rattachements importés », cf §14.8) ; (3) **déclare les hubs** (page 1 segment + enfants) en pilier. | `tools.php?page=eco3min-cleanup` |
| **Subpillar Aligner** | 1.3.0 (lot du 17/09/2026, en ligne) | Met l'ID `_eco3min_subpillar` en phase avec le slug `_eco3min_sub_pilier` (slug gagne), FR puis miroir EN, verrou avant breadcrumb ID-only. **Posts + pages depuis 1.3.0** (posts seuls avant), auto-référence signalée. Détail → `metas-eco3min`. | `admin.php?page=eco3min-subpillar-aligner` |
| **Level Setter** | 1.1.0 (lot du 17/09/2026, en ligne) | Pose `_eco3min_level` sur une liste de post_id (13 levels, **`satellite` inclus depuis 1.1.0**), backup `_e3m_lvlset_bak`. | `tools.php?page=eco3min-level-setter` |
| **Fix** (snippet Code Snippets 153, pas un plugin) | — | Onglet 1 « Promote majeur » (→ `major_article` seulement, backup `_e3m_lvl_bak`) ; onglet 2 « Import parent_major » (satellites) ; onglets 3 « Sync sous-pilier » et 4 « Purger des metas » ajoutés le 15/09/2026 → contrat dans `metas-eco3min` §2.4, §3.5. | `admin.php?page=e3m-fix` / `e3m-import-pm` / `e3m-sync-sp` / `e3m-purge-meta` |
| **Eco3min MCP** | **1.2.3** (lot du 17/09/2026, en ligne — 1.2.1 déployée le 16/09 : 5 abilities `snippet-*` ; 1.2.2 : `include_code` sur `snippet-find` ; 1.2.3 : `exclu` reconnu comme level, 13 valeurs, `health` ne le compte plus comme invalide) | 19 abilities `eco3min/*` (find, get-content, taxonomy, links, health, set-metas, set-seo, update-content, create-pair, rollback, mailpoet-*, snippet-find/get/update/create/toggle). Écriture en dry-run par défaut, rollback, sonde loopback + auto-restauration sur les snippets. | `tools.php?page=eco3min-mcp` |
| **Eco3min Import** | 2.3.0 (lot du 17/09/2026, en ligne) | 4 sous-pages : Chart of the Week · Page bilingue · Import dataset · MAJ metas (metas `_eco3min_*` + RankMath sur pages existantes, overwrite réversible, dry run). **Depuis 2.3.0 les trois modes de création acceptent un bloc `eco3min` {level, cluster, sub_pilier, parent_major}** posé à l'import (fill-only, backups `_e3i_bak_eco3min_*`), Import dataset pose `level=dataset` d'office. Bundles → `eco3min-import-contenu-bilingue`. | `admin.php?page=eco3min-import{,-page,-dataset,-metas}` |
| **Import Resumable** | 1.0.0 | Moteur d'import une étape par requête, état persisté, bouton Reprendre. | `tools.php?page=eco3min-import-resumable` |
| **Q&A Importer v2** | 2.0 | Paires FR/EN de pages Q&A depuis JSON, RankMath + Polylang, 2 phases. | `tools.php?page=eco3min-qa-import` |
| **Translator Bridge** | **1.3.0** | FR→EN massif. 5 onglets : EXPORT (FR sans paire EN) · IMPORT (crée EN + Polylang + cats miroirs) · REWRITE LINKS (aligne les liens sur la langue du post, **dans les deux sens**, protège les liens cross-langue volontaires) · FIX CATEGORIES · LIENS CROSS-LANGUE (export CSV/JSON, datasets exclus). | `tools.php?page=eco3min-translator` |
| **EN Mirror Classifier** | 1.0.0 | Reclasse les articles EN en miroir de leur FR (catégorie WP + metas `_eco3min_*`), idempotent, backup + rollback. | `admin.php?page=eco3min-en-mirror` |
| **Polylang Repair** | 1.0.3 | Audit + réparation du mapping Polylang des 80 pages Q&A des batches 7/08/32/33, uniquement là où absent. | `admin.php?page=eco3min-polylang-repair` (même écran sous `tools.php?page=eco3min-polylang-repair-tools`) |
| **Polylang JSON Exporter** | 1.0 | Titres + slugs des pages et articles en JSON séparés FR / EN. | `admin.php?page=pll-json-exporter` |
| **Anchor Doctor** | 1.6.0 | Inventaire de toutes les ancres in-text avec score de suspicion sur la tournure ; auto-correction des élisions ; batches JSON pour relecture ; import de correctifs byte-exact avec garde href ; onglet Auto-liens. | `admin.php?page=e3m-anchor-doctor` |
| **Anchor Retarget** | 1.0.0 | Export des ancres pointant vers une cible + plan de réécriture JSON (dry-run, backup, rollback). | `tools.php?page=eco3min-anchor-retarget` |
| **Link Doctor** | 1.0.5 | Détecte les liens insérés de façon défectueuse (phrase autonome au milieu d'une phrase, orphelin lowercase, cross-lang, self-link), export JSON, import de correctifs. | `admin.php?page=eco3ld` |
| **Patch Audit & Correction** | 2.5.0 | Reconstruit les liens posés par les patches (`e3m_patches_log`), les localise, trie par suspicion, ZIP de batches ; import de paragraphes corrigés (byte-exact, backup mega). | `tools.php?page=eco3min-patch-audit` |
| **Export Liens & Ancres** | 1.0.0 | Inventaire JSON des liens internes du `post_content` stocké (ancre + contexte + cible), sans le contenu. | `tools.php?page=eco3min-liens-export` |
| **Enrobage Fixer** | 1.2.0 | Remplace les enrobages répétitifs des liens externes de sourcing, idempotent, rollback par batch. | `tools.php?page=e3m-enrobage-fixer` |
| **Correcteur de 404** | 2.0.1 | Remplace ou déballe les liens internes en 404, simulation, journal, rollback. | `tools.php?page=e3m-404` |
| **Correcteur de liens 301** | 1.0.0 | Remplace les URL en 301 par leur destination finale, simulation, rollback. | `tools.php?page=e3m-rlf` |
| **Maillage Graph** | 1.8.2 | Visualisation du maillage interne par silo (taille = liens entrants, rouge = sous-maillé). | `admin.php?page=eco3min-maillage-graph` |
| **Accents Fixer** | 1.0.5 | Détecte et corrige entités HTML et texte désaccentué, par batch JSON, rollback. | `tools.php?page=e3m-accents-fixer` |
| **Meta Optimiser** | 1.0.0 | Audit des metas RankMath vides/quasi-vides, export JSON, réimport. | `tools.php?page=mo-meta-optimiser` |
| **Tag Optimizer** | 1.1.0 | Export articles + tags, import `tag-updater.json` / `tag-articles.json`. | `tools.php?page=eco3min-tag-optimizer` |
| **Repair Images** | 1.11.2 | Remplace les images ChatGPT des blocs core/image par de vraies attachments. | `tools.php?page=e3m-repair-images` |
| **Gestionnaire de Mentions AMF** | 1.0 | Recherche/suppression de mentions dans tout le contenu. | `admin.php?page=amf-mentions-manager` |

Les dossiers `plugins/eco3min-level-classifier/`, `eco3min-maillage-audit/`, `eco3min-maillage/` et `eco3min-classify-backfill/` ont été supprimés du dépôt le 15/09/2026 (plugins désactivés sur le site, absorbés par le mega) : la classification des `uncategorized` se fait dans le **Tinder du mega** (onglet Scan & Classification), qui n'enqueue que les articles à metas vides.

### 1.4 WORKFLOW CANONIQUE du conseil de maillage (l'ordre compte)

> **Réflexe figé.** Avant de lire le conseil T1/T2/T3 du mega, il faut que les articles soient **classés ET rattachés**. Sinon le conseil est partiel : il **ignore tout article sans `_eco3min_cluster`** (`if (empty($cluster)) return` — `class-eco3min-mu-analyzer.php:222`), et il ne maille **que 4 niveaux** : `pillar`, `sub_pillar`, `major_article`, `satellite` (ligne 352 de l'analyzer). FAQ, dataset, study, tool, beginner sont **ignorés** par le conseil.

1. **Classer** les `uncategorized` → Tinder du mega (onglet 📡 Scan & Classification ; metas vides uniquement), ou Cleanup import avec `level`, ou Level Setter (`satellite` inclus depuis 1.1.0), ou `eco3min/set-metas`.
2. **Cleanup** (`/wp-admin/tools.php?page=eco3min-cleanup`) :
   - Section 1 : marquer le bruit en `exclu`.
   - Section 3 : déclarer les hubs en pilier.
   - Section 2 : **Exporter le JSON → le donner à Claude → réimporter le JSON renvoyé** (écrit cluster + sous-pilier + level). *Voir le prompt de relance dans l'onglet Conseil du mega.*
3. **Scanner** le site dans le mega (remplit `e3m_links`, frais).
4. **Onglet Conseil** du mega → T1/T2/T3 (filtre « Tous les clusters » ou un cluster, langue FR/EN/les deux) → JSON de conseil pour le projet C.

**Le conseil de rattachement Cleanup côté Claude (ce que fait le prompt) :** sépare les 4 niveaux maillés du reste ; pour satellites/major, valide cluster+sous-pilier suggérés (heuristique des liens) **avec contrôle de langue** (un `/en/` ne va jamais sur un pilier FR) ; re-classe les **études** (`deep_study`/`case_study`/`foundation_article`) en `major_article` + cluster ; écarte les **pages fonctionnelles** (dashboard régime, hubs Macro Watch/Observatoire, méthodo, archives baromètre, datasets, simulateurs) vers `exclu`/`dataset`/`tool` ; signale les **bloqués** (satellites dont ni le titre ni les liens ne portent le sous-pilier — non automatisables sans le contenu).

### 1.5 Mega + 3 projets Claude Code (production éditoriale)

**3 projets Claude Code associés** (voir section 13), dans `~/eco3min/eco3min-projets/` — chacun = un dossier avec `CLAUDE.md` (plomberie), `memoire.md`, `docs/` (contrats de sortie), et pour A/B un `LAUNCH_PROMPT_TEMPLATE.md`. Les anciens projets claude.ai sont abandonnés : ne jamais parler de Knowledge, de custom instructions ni d'UUID de projet.
- **A. Architect** (`Eco3min Cluster Builder — A. Architect`) — blueprint bilingue d'un cluster.
- **B. Writer** (`Eco3min Cluster Builder — B. Writer`) — paires d'articles FR + EN au Format C v1.1, assemblées en un batch unique.
- **C. Maillage optimiser** (`Eco3min Cluster Builder — C. Maillage optimiser`, = « C. Patcher ») — patches.json à appliquer.

**Snapshot commun** : `~/eco3min/eco3min-projets/context/snapshot.csv` et `maillage.csv`, exportés depuis l'onglet Maillage du mega (CSV, 1.0.14), noms fixes, à écraser à chaque régénération.

**Externe** : **Q&A Importer** v2 (plugin, cf §1.1).

---

## 2. Pipeline cluster bilingue — mega 1.0.14 + projets Claude Code (lire `references/02-pipelines-projets-claude-methode.md`)

Bloquant, dans cet ordre (détail pas à pas, signaux des projets, temps par étape et messages d'erreur dans la référence 02) :

1. **Snapshot d'abord** : Mega → Maillage → exports CSV → `~/eco3min/eco3min-projets/context/snapshot.csv` + `maillage.csv` (noms fixes, écraser, dater et annoncer). Sans snapshot à jour, le projet A produit des slugs/H1 en conflit (cannibalisation) ; les projets A et B refusent de démarrer sans lui.
2. **Projet A Architect** (`eco3min-projets/Eco3min Cluster Builder — A. Architect`, `LAUNCH_PROMPT_TEMPLATE.md`) → blueprint bilingue selon `docs/07-architect-blueprint-template.md`, 5 contrôles anti-cannibalisation par programme.
3. **Projet B Writer** (`— B. Writer`) → bootstrap (`docs/08-format-c-v11-json-spec.md`, snapshot) → « paire 1 » … « suivant » → « bundle » = **le JSON d'import unique** (`create_cluster_bilingual`, Format C v1.1) → « snippet » (composant du MAJEUR) → « C » (liste des post_id sources). Les JSON par paire sont des artefacts de revue.
4. **Mega → Import cluster** : drag & drop du batch (`.json`, 10 Mo max, plus de FileZilla) → Sélectionner → « 🔍 Valider sans appliquer (dry run) » → « ✅ Appliquer ». Puis coller/activer le `snippet.php` dans Code Snippets (après l'import, jamais avant).
5. **Mega → Scan** → « Lancer un scan complet » jusqu'à disparition du bandeau rouge « index de maillage obsolète ».
6. **Mega → Maillage → « Format AVEC HTML — manuel »** sur les post_id sources du signal « C » → export « targets manual ». En import batch, le mega ne génère pas ce fichier tout seul.
7. **Projet C Maillage optimiser** (`— C. Maillage optimiser`, NEW CHAT) ← cet export (ou le JSON de l'onglet Conseil) → `outils/extract_anchors.py` → `patches-{cluster}-00N.json` au format v1.0.2.
8. **Mega → Maillage → Import patches** : drag & drop → Sélectionner → dry run → « ✅ Appliquer » (progress bar post par post, reprise possible 1 h).
9. **Re-scan**, puis Diagnostic + Conseil. Sous mega ≥ 1.0.15 les satellites arrivent déjà en `satellite` avec leur `parent_major` (rien à classifier) ; sous 1.0.14 ils arrivent en `uncategorized` et se classifient après (Tinder, Cleanup `level`, Level Setter, `set-metas`).

Les projets claude.ai (Knowledge, custom instructions, UUID), les onglets « Export LIGHT / Format B », les scopes `new_posts` / `cluster:` / `all`, le mode chunked ZIP par tier et le Level Classifier **n'existent plus** : ne jamais les proposer.

---

## 6. Format strict des patches v1.0.2 (lire `references/04-format-patches-v102.md`)

Règles dures (rejet immédiat par l'onglet Maillage du mega) :
- `expected_occurrences` **toujours = 1** ; `anchor_before` **80-200 chars**, plain text, sans balise HTML, **exactement 1 occurrence** dans le `post_content`, hors zone interdite (attribut, `<script>`, `<style>`, commentaire, shortcode, JSON-LD).
- `insert_after_anchor` porte un `<a href>` complet en URL absolue ; un FR ne pointe **jamais** vers `/en/`.

Règles soft (cap 18 patches/cible, 12 liens max par article, 3 max vers le même cluster, 1 par paragraphe, aucun dans les 2 premiers paragraphes sauf pillar parent) et variation des ancres : dans la référence 04. La rédaction des patches elle-même relève de `patches-maillage-eco3min`.

---

## 8. Règles d'opération non négociables

1. **Re-scan mega obligatoire entre chaque import** (cluster ou patches). Sinon `e3m_links` stagne et le conseil remontera les mêmes missing_links. Le mega le signale par un bandeau rouge persistant (dirty flag) : tant qu'il est affiché, ni conseil ni export ne sont fiables.
2. **Ne jamais ré-importer un `patches-{cluster}-{n}.json` déjà appliqué** : le mega l'archive automatiquement en `.applied` après apply et dédoublonne par hash SHA256 (`e3m_patches_log`).
3. **New chat Claude obligatoire entre 2 batches**. Ne jamais réutiliser une conversation pour 2 batches successifs (risque de contamination des règles ancres entre batches).
4. **Toujours lire `source_post_content` avant de générer une `anchor_before`**. La phrase doit exister exactement 1 fois dans le contenu.
5. **Ne jamais inventer un `target_url` ou `target_post_id`** qui ne sont pas dans le JSON reçu.
6. **Cap SEO réel = diversité des ancres, pas le nombre de liens**. 30 liens vers un MAJEUR avec 30 ancres distinctes = OK. 8 liens avec 8 fois la même ancre = pattern.
7. **`post_type IN ('post','page')` partout** dans les requêtes SQL d'analyzer. Sinon les pages structurelles sont invisibles.
8. **Utiliser `pll_get_post_language()`** comme source officielle de la langue (Polylang). Pas la postmeta `_eco3min_lang` qui peut être obsolète.
9. **Toujours vérifier les vrais noms de colonnes** de `e3m_links` : `src_post_id`/`target_post_id`, pas `from_*`/`to_*`.
10. **Backups** : le mega sauvegarde chaque `post_content` avant modification dans `e3m_backups`, avec rollback par `backup_id` ou par `trigger_ref` (batch entier) — bouton Rollback dans les historiques des onglets Import cluster et Maillage. Les écritures MCP (`eco3min/set-metas`, `set-seo`, `update-content`) se restaurent par `eco3min/rollback`.
11. **Mega : NE JAMAIS écrire directement sur `_eco3min_level/_cluster/_sub_pilier/_parent_major`**. Passer par `Eco3min_Mega_Classifier::set_meta_safe()` qui throw `Eco3min_Mega_Immutability_Exception` en cas de tentative d'écrasement. Voir section 12.4.

---

## 9. Diagnostic rapide (lire `references/05-tables-sql-bugs-diagnostic.md` pour les tables `e3m_*`, les bugs durables et les presets SQL)

Quand quelque chose ne va pas, suivre cet ordre :

1. **Le conseil remonte 0 missing_links alors qu'on en attend ?**
   → Vérifier que les articles portent `_eco3min_cluster` (le conseil les ignore sinon) et un level parmi les 4 niveaux maillés. Vérifier `post_type` dans la query SQL. Vérifier `_eco3min_lang` peuplé. Vérifier qu'il y a eu un re-scan mega récent (bandeau rouge absent).

2. **Le patch Claude est rejeté par l'onglet Maillage du mega ?**
   → Erreurs typiques : ANCHOR_NOT_FOUND (ancre absente du contenu), ANCHOR_COUNT_MISMATCH (présente plusieurs fois), `expected_occurrences != 1`. Réviser la sélection d'ancre.

3. **`e3m_links` ne change pas après IMPORT ?**
   → Re-lancer le scan complet (onglet Scan). Le graphe ne se rafraîchit pas tout seul ; le cron daily passe en synchrone.

4. **Site planté ("erreur critique") ?**
   → FileZilla → renommer le dossier du dernier plugin modifié en `_disabled`. WordPress redevient accessible. Diagnostiquer le PHP.

5. **Décompte de satellites incohérent entre 2 endroits ?**
   → Les 3 décomptes (363/150/50) mesurent des sous-ensembles différents. Voir BUG #7. Vérifier directement en SQL ou via `eco3min/health`.

6. **Mega : import cluster bilingue refuse avec "Polylang must be active" ?**
   → Polylang désactivé ou non installé. L'import cluster bilingue de l'onglet 3 nécessite Polylang. Activer d'abord.

7. **Mega : import cluster refuse une paire avec "slug_fr_conflict" ou "slug_en_conflict" ?**
   → Le slug existe déjà en BDD. Soit doublon réel (le post a déjà été importé), soit conflit avec un autre cluster. Vérifier via SQL : `SELECT ID FROM wp_posts WHERE post_name = 'le-slug'`.

8. **Mega : exception `Eco3min_Mega_Immutability_Exception` au runtime ?**
   → Tentative d'écrasement d'une meta classification existante. Logique applicative à revoir : un import cluster ne devrait jamais déclencher ça (posts neufs uniquement). Si ça arrive, vérifier que le post_id n'existait pas déjà avant l'import.

9. **Breadcrumb sans sous-pilier, split-brain slug/ID ?**
   → Onglet Diagnostic du mega → Subpillar Aligner → Réconciliation. Escalade complète dans `metas-eco3min` §5.

---

## 10. Conventions de code (lire `references/03-mega-versions-immutabilite-format-c.md`)

Préfixes `Eco3min_*` / `ECO3MIN_*` / `eco3-`, tables `eco3min_*` (legacy) et `e3m_*` (mega), AJAX `eco3min_mega_*` + nonce `eco3min_mega_nonce`, capability `manage_options`, Polylang uniquement via `Eco3min_Mega_Polylang_Bridge::*`, catégories résolues par slug via `Eco3min_Mega_Category_Resolver::resolve($slug)`. Détail dans la référence 03 ; conventions générales dans `archi-eco3min`.

---

## 11. Quand activer ce skill

Active ce skill quand l'utilisateur :
- Pose une question sur le rôle ou le fonctionnement d'un plugin maison ou du mega.
- Décrit un bug ou un comportement bizarre.
- Demande à modifier ou faire évoluer un plugin.
- Lance un cycle de patches (export → Claude C Patcher → import).
- Lance un cycle de création de cluster bilingue (projet A → projet B → import mega → projet C → import mega).
- Mentionne une table `eco3min_*` ou `e3m_*`, une meta `_eco3min_*`, un onglet d'un de ces plugins, un onglet du mega.
- Pose une question SQL sur les liens internes ou les classifications.
- Demande comment utiliser les projets Claude Code associés (A. Architect / B. Writer / C. Maillage optimiser) et comment enchaîner leurs sorties avec le mega.
- Demande l'URL wp-admin d'un plugin ou d'un onglet.

Ne pas activer pour :
- Questions de structure éditoriale pure (silos, levels, piliers) → `archi-eco3min`.
- Cycle de vie des metas après création ou import (quoi poser, avec quel outil) → `metas-eco3min`.
- Questions de rédaction (style, AMF) → `editeur-eco3min`.
- Production de pages dataset / Q&A → `production-dataset`, `production-q-and-a`.

---

## 12. Mega-plugin Eco3min 1.0.16 (lire `references/03-mega-versions-immutabilite-format-c.md`)

- **Snapshot JSON/CSV, colonne `url`** : depuis 1.0.16 c'est la permalink WordPress (imbriquée pour les sous-piliers, `/qr/` `/qa/` pour les Q&A). Le 1.0.16 est en ligne depuis le 17/09/2026 au soir et `context/snapshot.csv` a été ré-exporté avec (scan 21:59, export 22:07) : un snapshot dont la ligne 1 cite un mega < 1.0.16 porte encore la reconstruction plate (archi-eco3min §2.1).

Bloquant :
- **Garde-fou immutabilité (12.4)** : le travail Tinder humain (615 articles classifiés à la main) ne peut jamais être écrasé par le mega. Scanner read-only ; queue Tinder filtrée sur metas vides ; toute écriture sur `_eco3min_level/_cluster/_sub_pilier/_parent_major` passe par `Eco3min_Mega_Classifier::set_meta_safe()` qui throw `Eco3min_Mega_Immutability_Exception` ; import cluster sur posts neufs uniquement (`wp_insert_post`, refus si slug déjà utilisé).
- **Le Tinder mega écrit le SLUG `_eco3min_sub_pilier`** (`class-eco3min-mega-tab-2-scan.php:467`), jamais l'ID `_eco3min_subpillar` — l'ID est dérivé par le snippet SUBPILLAR SYNC / le Subpillar Aligner (cf `metas-eco3min`).
- **Format C v1.1 (12.5), règles strictes à l'import** : Polylang actif ; slug FR + slug EN uniques dans le batch ET en BDD, slug FR ≠ slug EN ; levels valides parmi `pillar, sub_pillar, major_article, satellite (≥ 1.0.15, exige parent_major_pair_id), foundation_article, case_study, deep_study, dataset, faq, tool, beginner, uncategorized` ; liens FR vers `https://eco3min.fr/SLUG-FR/`, EN vers `https://eco3min.fr/en/SLUG-EN/`, pas de cross-lang ; `wp_category_slug` existant en BDD ; `parent_major_pair_id` déclaré AVANT le satellite qui le référence ; `expected_pairs_count` = `len(articles)`. Les longueurs RankMath (titre ≤ 60, description ≤ 155) ne sont **pas** contrôlées par `Eco3min_Mega_Validator` (vérifié le 17/09/2026) : c'est une règle du projet B Writer, pas un rejet à l'import.
- **Maillage Ultime** : les 4 classes `Eco3min_MU_*` vivent dans `includes/maillage-ultime/` avec `require` protégés `if (!class_exists())`. Ne JAMAIS laisser le plugin « Maillage Ultime » séparé actif en même temps (redéclaration de classe → écran blanc).
- **Réconciliation (onglet 9)** = seul onglet MU qui écrit : suppression réversible des ID sous-pilier en conflit (slug fait foi), bouton Restaurer. Le breadcrumb hybride est un snippet, pas cet onglet.

---

## 13. Les 3 projets Claude Code — dossiers `Eco3min Cluster Builder — A. Architect` / `B. Writer` / `C. Maillage optimiser` dans `~/eco3min/eco3min-projets/` (lire `references/02-pipelines-projets-claude-methode.md`)

### 13.4 Tableau de décision — quel projet Claude Code lancer ?

| Situation | Projet à utiliser |
|---|---|
| Je veux créer un cluster bilingue from scratch | **A. Architect** d'abord, puis **B. Writer** (dossiers `Eco3min Cluster Builder — A. Architect` / `— B. Writer` dans `eco3min-projets`) |
| J'ai un blueprint validé, je veux écrire les articles | **B. Writer** |
| Je veux intégrer de nouveaux articles au maillage existant | **C. Maillage optimiser** (avec l'export « Format AVEC HTML — manuel » de l'onglet Maillage sur les post_id sources livrés par le signal « C » du projet B) |
| Je veux optimiser un cluster existant (mature) | **C. Maillage optimiser** (avec le JSON de l'onglet Conseil filtré sur ce cluster) |
| Je veux optimiser tout le site | **C. Maillage optimiser** batch par batch (onglet Conseil « Tous les clusters », tier par tier, new chat par batch) |
| Je veux juste classifier des articles existants non classifiés | Aucun projet Claude. Tinder du mega (onglet Scan & Classification) ; sinon Cleanup `level`, Level Setter, MCP `eco3min/set-metas` |

---

## 14. Méthode opérationnelle (lire `references/02-pipelines-projets-claude-methode.md`, et `references/06-promotion-majeur-cleanup-fix.md` pour 14.8)

### 14.7 Tableau de décision rapide

| Question utilisateur | Réponse Claude |
|---|---|
| "Comment je crée un cluster bilingue ?" | → 14.1 (snapshot CSV → projet A → projet B « bundle » → import batch → scan → export AVEC HTML manuel → projet C → import patches) |
| "Comment j'optimise mon cluster X ?" | → 14.2 (Cleanup → scan → onglet Conseil → projet C → import patches → re-scan) |
| "Comment j'attaque le maillage de tout le site ?" | → 14.3 (onglet Conseil « Tous les clusters », cluster par cluster, tier par tier) |
| "Comment je classifie un article ?" | → 14.4 (Tinder mega sur metas vides ; sinon Cleanup `level`, Level Setter, MCP `eco3min/set-metas`) |
| "Mon import a foiré, qu'est-ce que je fais ?" | → 14.5 (diagnostic via rapport + logs) |
| "Je veux annuler ce que j'ai fait" | → 14.6 (bouton Rollback des historiques Import cluster / Maillage ; `eco3min/rollback` pour les écritures MCP) |
| "Je veux passer des pages en `major_article` / promouvoir des études" | → 14.8 (**un seul import Cleanup** : `level` + `cluster` + `sub_pilier` ; Fix 153 ou Level Setter pour du level seul) |
| "Quel projet je lance ?" | → 13.4 (table de décision projets) |

### 14.8 Promotion en `major_article` — condensé (lire `references/06-promotion-majeur-cleanup-fix.md`)

- Une étude qui doit vivre dans le moteur de maillage est classée `major_article` : le conseil ignore `deep_study`, `dataset`, `faq`, `tool`, `beginner`.
- **Un seul outil suffit** (vérifié dans `eco3min-cleanup.php` le 15/09/2026) : Cleanup import `{"attachments":[{"post_id":N,"level":"major_article","cluster":"<slug PILIER>","sub_pilier":"<slug PAGE sous-pilier>"}]}`. `level` = overwrite réversible (`_e3mc_bak_level`) ; `cluster` / `sub_pilier` = fill-only, jamais écrasés ; `parent_major` omis sur un majeur ; post `publish` obligatoire ; piloté par post_id. **Pas de prévisualisation** sur cet import : vérifier le JSON avant de cliquer.
- `sub_pilier` en **slug** de la page sous-pilier ; `cluster` = slug du **pilier** parent (jamais le `wp_category_slug`). Valeurs tirées d'`archi-eco3min`.
- Ensuite : re-scan mega ; liens sortants du nouveau majeur (sous-pilier parent + 1-2 majeurs voisins) via Conseil ou projet C.
- Aucun backfill one-shot des metas (Classify Backfill et consorts sont désinstallés) : Cleanup, Tinder mega ou `eco3min/set-metas` uniquement.

---

## 16. Code Snippets — outillage et pièges (lire `references/07-code-snippets-pieges.md`)

Bloquant :
- **Patcher un snippet = `eco3min/snippet-update`** (Eco3min MCP ≥ 1.2.1, en live depuis le 16/09/2026). Cycle : `snippet-get` (code live + `code_sha256`) → `snippet-update` en dry-run avec `replacements[]` byte-exact (`find`, `replace`, `expect_count`) et `expect_sha256` → même appel `dry_run:false` → lire `probe.verdict` (`ok` attendu ; `fatal` = ancien code déjà restauré automatiquement ; `unreachable` = vérifier le site à la main) → rafraîchir le fichier miroir avec `mirror.content` de `snippet-get`. Rollback : `eco3min/rollback` avec le `ref`. Plus de copier-coller dans wp-admin.
- `ewpa/create-code-snippet` **crée un nouveau snippet, toujours inactif, et ne met à jour aucun snippet existant** : s'en servir pour patcher produit un doublon inactif sans erreur. `ewpa/update-code-snippet` et `ewpa/set-code-snippet-active` (opt-in, à laisser décochés) **désactivent** tout snippet actif dont le code change et exigent une réactivation manuelle dans wp-admin : ne jamais les préférer à `eco3min/snippet-update`.
- `~/eco3min-wp/snippets/` est un **miroir** : toujours relire le live par `snippet-get` avant de patcher, et passer `expect_sha256` — l'ability refuse d'écraser si le code a changé depuis la lecture.
- Snippet 226 (moniteur de fraîcheur) : le `post_content` est la voie d'ÉCRITURE (marqueur `<!--e3m-review due="AAAA-MM-JJ" lead="30" do="…"-->`), les metas `_e3m_review_*` la voie de LECTURE — jamais l'inverse. Un seul marqueur lu par page (`preg_match`). Guillemets droits `"` obligatoires ; guillemets typographiés ou date invalide = page disparue de l'écran admin **en silence**. `wp-admin/tools.php?page=e3m-review` derrière authentification : `WebFetch` n'y accède pas.

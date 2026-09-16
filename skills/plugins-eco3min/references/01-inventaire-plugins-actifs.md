# plugins-eco3min — référence : Inventaire des plugins actifs, rôles, URLs, absorptions, tables legacy (§1.1-1.3, §3, §12.2, §15)

Extrait de SKILL.md (découpage du 15/09/2026), remis à jour le même jour contre le dépôt `eco3min-wp/plugins/` et le live (`ewpa/get-active-plugins`). Fait foi avec SKILL.md ; SKILL.md porte la version condensée (tableau §1.1) et le moment où lire ce fichier.

---

## 1.2 Plugins DISPARUS du site (ni actifs, ni dans le dépôt) — ne jamais les proposer

| Plugin | Ce qu'il faisait | Où c'est passé |
|---|---|---|
| **Level Classifier** (1.5.1) | Inférer le level des `uncategorized` par heuristiques, Tinder clavier, backfill par URL, onglet Audit Maillage | Dossier supprimé du dépôt le 15/09/2026 (inactif sur le site). Classification → **Tinder du mega** (onglet Scan & Classification, metas vides), Cleanup `level`, Level Setter, MCP `eco3min/set-metas`. Conseil → onglet Conseil du mega. |
| **Site Audit** (1.0.x) | Scan des liens internes → table `eco3min_sa_links` | **Scanner du mega** → `e3m_links` (mêmes colonnes `src_post_id` / `target_post_id` / `target_url` / `anchor_text`, plus `is_internal`, `is_cross_lang`). |
| **Anchor Diversifier**, **Redundant Cleaner** (1.0.0) | Diversifier les ancres sur-utilisées ; enlever les liens 3+ vers la même cible | Absorbés en **scan-only** dans l'onglet 🕸️ Graphique du mega (`Eco3min_Mega_Anchor_Diversifier`, `Eco3min_Mega_Redundant_Cleaner`). La correction des ancres passe désormais par **Anchor Doctor**, **Anchor Retarget**, **Link Doctor**, **Patch Audit & Correction**. |
| **Hub** (1.2.0) | Menu top-level « Eco3min », statut des plugins | Le mega a son propre menu `eco3min-mega` ; l'inventaire live se lit par `ewpa/get-active-plugins`. |
| **GSC Linker** (1.2.0) | Import CSV Search Console, suggestions de cibles | Plus installé. L'analyse GSC vit dans `audit-seo-eco3min` ; RankMath expose `rank-math/get-top-keywords`. |
| **Dataset Monitor** (1.0.0) | Cron de fraîcheur des datasets, endpoint `touch-datasets` | Plus installé. La fraîcheur des datasets relève du pipeline `eco3min-data` (`pipeline-eco3min`). |
| **Pillar Audit** (1.6.1) | Backfills `_eco3min_sub_pilier` depuis `parent_major`, backfill `_eco3min_lang` | Plus installé. Le mega lit Polylang via `Eco3min_Mega_Polylang_Bridge` ; les metas se posent via Cleanup / Import « MAJ metas » / MCP. |
| **Meta Monitor** (1.0.0) | Rendre visibles les metas `_eco3min_*` dans l'éditeur | Plus installé. Lecture par MCP `eco3min/get-content` ; écriture par Cleanup, Import « MAJ metas », `eco3min/set-metas`. |
| **SQL Runner** (1.0.1) | Console SQL admin avec presets | Plus installé. Requêtes → console SQL de l'hébergeur ; la plupart des questions ont une ability MCP (`eco3min/links`, `health`, `taxonomy`, `find`). |
| **Performance Dashboard**, **Anchor Health** | Vues croisées GSC/liens ; cron d'alerte ancres saturées | Zappés (jamais intégrés), désinstallés. |
| **Sub-pilier Backfill** (1.4.0), **Major-EN Backfill** (1.6.0) | Backfills one-shot | Désinstallés. **Ne jamais réécrire l'ID de sous-pilier par backfill** : cause historique du split-brain `_eco3min_sub_pilier` (slug) vs `_eco3min_subpillar` (ID) — voir `metas-eco3min`. |
| **Maillage Ultime** (plugin séparé) | Diagnostic / Conseil / Réconciliation | Fusionné dans le mega en V1.0.13 (onglets 7, 8, 9). Ne jamais réactiver le plugin séparé (redéclaration de classe → écran blanc). |
| **Chart of the Week** (1.2.0) | Import du bundle chart hebdo | Remplacé par la sous-page « Chart of the Week » d'**Eco3min Import** 2.2.1. |
| **Maillage Audit** (0.3.0) | Référentiel piliers/clusters, scan des liens, exports JSON | Désactivé le 15/09/2026, dossier retiré du dépôt ; référentiel migré dans `e3m_referentiel`, ses 4 tables droppées. |
| **Maillage Cluster** (1.0.2) | Export batch.json + import des patches avec backup/rollback (le premier applicateur de patches) | Désactivé le 15/09/2026, dossier retiré. Absorbé par l'onglet 🔗 Maillage du mega (import patches, `.applied`, `e3m_patches_log`, `e3m_backups`). |
| **Classify Backfill** (1.0.0) | Backfill one-shot des 4 metas depuis un JSON | Désactivé le 15/09/2026, dossier retiré. **Ne jamais réintroduire un backfill d'ID** : cause historique du split-brain slug/ID. Metas → Cleanup, Tinder mega, `eco3min/set-metas`. |

## 1.3 Plugins OBSOLÈTES encore actifs

Aucun au 15/09/2026 : Maillage Cluster, Maillage Audit et Classify Backfill ont été désactivés et retirés du dépôt ce jour-là. Tout plugin maison actif est donc à utiliser ; tout plugin absent de §1.1 n'existe plus.

### 1.5 Mega + 3 projets Claude Code (production éditoriale)

**3 projets Claude Code associés** (voir section 13), dans `~/eco3min/eco3min-projets/` — chacun = un dossier avec `CLAUDE.md` (plomberie), `memoire.md`, `docs/` (contrats de sortie), et pour A/B un `LAUNCH_PROMPT_TEMPLATE.md`. Les anciens projets claude.ai sont abandonnés : ne jamais parler de Knowledge, de custom instructions ni d'UUID de projet.
- **A. Architect** (`Eco3min Cluster Builder — A. Architect`) — blueprint bilingue d'un cluster.
- **B. Writer** (`Eco3min Cluster Builder — B. Writer`) — paires d'articles FR + EN au Format C v1.1, assemblées en un batch unique.
- **C. Maillage optimiser** (`Eco3min Cluster Builder — C. Maillage optimiser`, = « C. Patcher ») — patches.json à appliquer.

**Snapshot commun** : `~/eco3min/eco3min-projets/context/snapshot.csv` et `maillage.csv`, exportés depuis l'onglet Maillage du mega (CSV, 1.0.14), noms fixes, à écraser à chaque régénération.

**Externe** : **Q&A Importer** v2 (plugin, cf §1.1).

---

## 3. Rôle détaillé de chaque plugin actif

### 3.1 Cœur du maillage et des metas

#### Eco3min Mega (1.0.14)
- Voir `references/03-mega-versions-immutabilite-format-c.md` (versions, immutabilité, Format C) et `references/02-pipelines-projets-claude-methode.md` (workflow). Onglets et URLs dans le tableau §1.1 de SKILL.md.
- **Onglet Maillage, section Snapshot (1.0.14)** : deux exports CSV en plus du snapshot JSON — `eco3min-snapshot-{date}.csv` (même périmètre et même requête que le JSON) et `eco3min-maillage-{date}.csv` (1 ligne par lien interne résolu, lu depuis `e3m_links` par pages de 5000 ; reflète le **dernier scan**, dont la date est écrite en 1re ligne en commentaire `#`). Ce sont les fichiers `context/snapshot.csv` et `context/maillage.csv` d'`eco3min-projets`.
- **Route de download** : `eco3min_mega_download_export` (.json) et `eco3min_mega_download_export_csv` (.csv) contournent le `.htaccess` OVH qui bloque le téléchargement direct des `.json`.

#### Eco3min Cleanup (1.1.0 dans le dépôt, 1.0.1 en live tant que non déployé — même code depuis juillet 2026)
- **Rôle** : remise en ordre AVANT le conseil. Section 1 bruit → `level=exclu` (patterns de slug : mentions légales, contact, sitemap, newsletter, méthodologie…), restauration en un clic (`_e3mc_bak_level`). Section 2 export des articles maillables sans cluster/sous-pilier avec suggestion calculée depuis leurs liens dominants (levels « maillables » : `satellite, major_article, foundation_article, deep_study, case_study, dataset, tool, faq, beginner`), puis import. Section 3 hubs à 1 segment d'URL avec enfants → `pillar`.
- **Contrat d'import (section 2)**, piloté par post_id, post `publish` obligatoire :
  ```json
  {"attachments":[{"post_id":123,"level":"major_article","cluster":"<slug PILIER>","sub_pilier":"<slug PAGE sous-pilier>","parent_major":27555}]}
  ```
  `level` : **overwrite autorisé**, backup `_e3mc_bak_level` (12 valeurs : `satellite, major_article, sub_pillar, pillar, deep_study, case_study, foundation_article, dataset, tool, faq, beginner, exclu`). `cluster` / `sub_pilier` : **fill-only** (jamais d'écrasement), backups `_e3mc_bak_cluster` / `_e3mc_bak_sub`, valeurs contrôlées contre les piliers et sous-piliers connus. `parent_major` : fill-only, **sans backup**. Une entrée sans aucun des trois champs, ou avec une valeur inconnue, est `skipped`.
- **Pas de prévisualisation** sur l'import : le bouton « Importer & ecrire les metas » écrit directement.
- Séparé du mega (menu Outils) volontairement : outil one-shot de remise en ordre, exécuté avant le conseil.

#### Subpillar Aligner (1.2.0)
- **Rôle** : consolider les deux clés sous-pilier. Slug `_eco3min_sub_pilier` = source de vérité, jamais supprimé ni écrasé ; ID `_eco3min_subpillar` = fil d'Ariane + admin, rempli/corrigé depuis le slug. Étape 1 FR, étape 2 miroir EN via Polylang, étape 3 verrou avant de déployer le breadcrumb ID-only (snippet `snippet/breadcrumb-subpillar-id-only.php` livré avec le plugin). Backup + rollback par session (table `eco3min_spa_backup`).
- Doctrine et séquence complète → `metas-eco3min` §2.

#### Level Setter (1.0.0)
- Pose `_eco3min_level` sur une liste de post_id (un par ligne ou virgules) + select parmi 12 levels — **`satellite` absent du select**. Preview, backup à la première écriture (`_e3m_lvlset_bak`), Restaurer. Ne touche ni cluster ni sous-pilier.

#### Fix (snippet Code Snippets 153 « Promouvoir en major_article (réversible) »)
- Menu « Eco3min Fix » : onglet 1 « Promote majeur » (`admin.php?page=e3m-fix`) : post_id ou URL, un par ligne, prévisualisation `<level actuel> → major_article`, backup `_e3m_lvl_bak`, bouton Restaurer. Onglet 2 « Import parent_major » (`admin.php?page=e3m-import-pm`) : pour les satellites, valide cible = `major_article` + même langue.

#### Eco3min MCP (1.1.0)
- Expose 14 abilities `eco3min/*` à l'adaptateur MCP : `find` (recherche par slug/titre/langue/level/cluster/sous-pilier, `missing[]` pour les non classés), `get-content` (1 à 20 contenus : contenu, metas `_eco3min_*`, RankMath `rank_math_*`, traductions, compteurs de liens), `taxonomy` (arborescence live), `links` (inbound/outbound/orphans/cross_lang depuis `e3m_links`, date du scan renvoyée), `health` (diagnostic), `set-metas` (dry-run par défaut, mode fill/overwrite, dérive l'ID depuis le slug), `set-seo`, `update-content` (patch byte-exact avec `expect_count`), `create-pair` (paire FR/EN câblée Polylang, draft), `rollback`, `mailpoet-list/get/duplicate/update` (jamais d'envoi).

### 3.2 Import de contenu

#### Eco3min Import (2.2.1)
- Menu « Eco3min Import », 4 sous-pages : **Chart of the Week** (snippet + 2 pages EN/FR + metas + JSON-LD + featured image + cartes de hub), **Page bilingue** (idem sans les hubs, `post_type` page), **Import dataset** (N pages EN seules, Polylang EN sans miroir FR, publication directe), **MAJ metas** (sur pages existantes résolues par slug, sans toucher slug/titre/contenu : metas `_eco3min_*` — level, cluster, sous-pilier slug + ID dérivé, parent_major — et/ou re-push RankMath ; overwrite réversible `_e3i_bak_eco3min_*`, dry run).
- v2.2.1 : clés RankMath `rank_math_*` sans underscore initial, `_rank_math_*` purgés — c'était la cause des SEO « non settées ».
- Un bundle JSON par contenu, idempotent, Preview / Apply. Format des bundles → `eco3min-import-contenu-bilingue`, `production-chart-of-the-week`.

#### Import Resumable (1.0.0)
- Moteur d'import piloté côté client, une étape par requête, état persisté serveur, bouton « Reprendre » (y compris après erreur réseau ou rechargement).

#### Q&A Importer v2 (2.0)
- Paires FR/EN de pages Q&A depuis JSON avec RankMath + Polylang, en 2 phases (création puis liaison des traductions). Format → `production-q-and-a`.

#### Translator Bridge (1.3.0)
- **Rôle** : pipeline FR→EN massif. 5 onglets : EXPORT (JSON des FR sans paire EN) / IMPORT (crée les posts EN traduits + connecte Polylang + mappe les catégories miroirs avec fallback hardcodé) / REWRITE LINKS (aligne les liens internes sur la langue du post, **dans les deux sens**, en protégeant les liens cross-langue volontaires « Version française » / « English version » / 🇫🇷🇬🇧) / FIX CATEGORIES (corrige rétroactivement cats/tags en mauvaise langue) / LIENS CROSS-LANGUE (export CSV/JSON de tous les liens cross-langue, datasets exclus).
- **Status mega** : conservé séparé. Le Format C v1.1 produit FR + EN appariés directement par le projet B Writer, donc Translator Bridge n'est nécessaire que pour les anciens articles FR sans paire EN.

#### EN Mirror Classifier (1.0.0)
- Reclasse les articles EN (`post`) en miroir de la classification de leur FR (catégorie WP + metas `_eco3min_*`), traduction Polylang typée par champ, récap couleur avant application, écriture idempotente, backup + rollback, chunks anti-coupure.

#### Polylang Repair (1.0.3), Polylang JSON Exporter (1.0)
- Repair : audit des 80 pages Q&A des batches 7 / 08 / 32 / 33 (présence, statut, doublons) puis réparation du mapping Polylang **uniquement là où il est absent**. Exporter : titres + slugs des pages et articles en JSON FR / EN séparés.

### 3.3 Qualité des liens (après patches)

#### Anchor Doctor (1.6.0)
- Inventorie toutes les ancres contextuelles in-text (hors boutons/menus/nav/assets) avec phrase entière, bloc HTML éditable unique par lien, score de suspicion sur la tournure (élision « de le », titre brut après préposition, ancre générique, ancre trop longue). Auto-corrige la classe mécanique (élisions). Exporte des batches JSON pour relecture Claude (tri par suspicion, seuil réglable). Applique un JSON de correctifs find/replace byte-exact avec garde href (le lien ne peut être ni supprimé ni modifié), backup et revert. Onglet Auto-liens (liens d'une page vers elle-même).

#### Anchor Retarget (1.0.0)
- Exporte en JSON toutes les ancres internes pointant vers une page cible (contexte verbatim + metas Eco3min), applique un plan de réécriture d'ancres JSON (dry-run, backup, rollback).

#### Link Doctor (1.0.5)
- Scanne posts/pages, détecte les liens internes insérés de façon défectueuse (phrase autonome injectée au milieu d'une phrase, orphelin lowercase après un point, cross-lang, self-link), export JSON, onglet d'import de correctifs find/replace byte-exact avec backup et revert.

#### Patch Audit & Correction (2.5.0)
- (1) EXPORT : reconstruit tous les liens insérés par les patches (`e3m_patches_log`, `status=applied`), les localise dans le contenu actuel par le href réel, extrait le paragraphe hôte, calcule des signaux, trie par suspicion, sort un ZIP de batches JSON. (2) IMPORT CORRECTIONS : remplace un paragraphe hôte par sa version corrigée (match byte-exact, occurrence unique, backup mega, dry-run, validation HTML). Ne modifie le contenu que via l'onglet Import.

#### Export Liens & Ancres (1.0.0)
- Inventaire JSON des liens internes du `post_content` **stocké** (pas le rendu) : ancre + court contexte + métadonnées cible, sans le contenu. Sert à détecter ancres décorrélées, boilerplate, liens cassés, cross-langue.

#### Enrobage Fixer (1.2.0)
- Remplace les enrobages répétitifs des liens externes de sourcing par des formulations variées (`replacements.json`). Idempotent, reprise, dry-run, verrou de concurrence, vérification post-écriture, backup et rollback par batch.

#### Correcteur de 404 (2.0.1), Correcteur de liens 301 (1.0.0)
- 404 : remplace les liens internes en 404 par leur cible retenue, déballe ceux qui n'en ont aucune, exporte l'inventaire des médias. 301 : remplace les URL qui déclenchent une 301 par leur destination finale. Les deux : simulation, reprise après interruption, journal, rollback.

#### Maillage Graph (1.8.2)
- Visualisation dynamique du maillage interne (liens dans le contenu uniquement) classé par silo pilier > sous-pilier ; taille = liens entrants, rouge = sous-maillé ; zoom + filtres.

### 3.4 Contenu et SEO divers

- **Accents Fixer** (1.0.5) : entités HTML et texte désaccentué, scan reprenable, batches JSON, rollback par batch.
- **Meta Optimiser** (1.0.0) : audit des metas RankMath vides / quasi-vides, export JSON avec contenu nettoyé, réimport.
- **Tag Optimizer** (1.1.0) : phase 1 export (H1, SEO title, meta, slug, lang, tags) ; phase 2a `tag-updater.json` (créer/MAJ/supprimer tags) ; phase 2b `tag-articles.json` (affectation).
- **Repair Images** (1.11.2) : remplace les images ChatGPT des blocs `core/image` par de vraies attachments (srcset, alt), par batches.
- **Gestionnaire de Mentions AMF** (1.0) : recherche/suppression de mentions dans tout le contenu.

---

## 12.2 Ce que le mega a absorbé

| Plugin legacy | Devenu | Onglet mega |
|---|---|---|
| Site Audit | scanner read-only → `e3m_links` | 📡 Scan & Classification |
| Maillage Audit | référentiel migré → `e3m_referentiel` | 📋 Référentiel |
| Maillage Cluster | import patches + backup + rollback | 🔗 Maillage |
| Level Classifier | Tinder (metas vides uniquement) | 📡 Scan & Classification |
| Anchor Diversifier, Redundant Cleaner | scan-only | 🕸️ Graphique |
| Maillage Ultime | Diagnostic / Conseil / Réconciliation | 🩺 🧭 🧹 |

Plugins **conservés séparés** parce que hors du scope du mega : tous ceux des §3.2 à §3.4, plus Cleanup, Subpillar Aligner, Level Setter, MCP. Les six absorbés ont tous été désinstallés ou désactivés (dernier lot le 15/09/2026 : Maillage Audit, Maillage Cluster, Classify Backfill).

---

## 15. Tables en base — état après le nettoyage du 15/09/2026

Inventaire relevé par snippet one-shot le 15/09/2026 10:20 (42 tables), vérifié (`ONESHOT-verif-drop-tables-eco3min.php`), puis nettoyé à 10:40 (`ONESHOT-drop-tables-orphelines-eco3min.php`, après sauvegarde UpdraftPlus) : **19 tables droppées, `e3m_backups` vidée**. Il reste 22 tables `eco3min_*` / `e3m_*`. **Le préfixe `e3m_` n'est pas réservé au mega** : 404-fixer, Accents Fixer, Anchor Doctor, Anchor Retarget, Redirect fixer et Patch Audit l'utilisent aussi — ne jamais dropper une table `e3m_*` sur la seule foi du préfixe.

### 15.1 Tables vivantes (22)

| Table | Lignes au 15/09 | Plugin |
|---|---|---|
| `e3m_referentiel` (220), `e3m_articles` (3011), `e3m_links` (39 664), `e3m_patches_log` (7963), `e3m_backups` (**0 après TRUNCATE**, se remplit à chaque apply/import), `e3m_imports_log` (571), `e3m_multi_import_sessions` (15), `e3m_scan_state` (291), `e3m_tinder_queue` (2775), `e3m_qa_clusters` (0) | — | **Eco3min Mega** (10 tables) |
| `e3m_404_log` | 597 | Correcteur de 404 |
| `e3m_rlf_log` | 3073 (78 Mo) | Correcteur de liens 301 |
| `e3m_af_audit`, `e3m_af_findings`, `e3m_af_patch` | 50 / 0 / 28 | Accents Fixer |
| `e3m_anchor_audit`, `e3m_anchor_treated`, `e3m_anchor_selflinks` | 36 791 / 14 977 / 22 | Anchor Doctor |
| `e3m_ar_log` | 6 | Anchor Retarget |
| `e3m_pae_audited` | 5253 | Patch Audit & Correction (`ECO3MIN_PAE_TP = 'e3m_'`) |
| `eco3min_mcp_backups` | 217 | Eco3min MCP (`eco3min/rollback`) |
| `eco3min_enm_backup` | 323 | EN Mirror Classifier |
| `eco3min_spa_backup` | 719 | Subpillar Aligner |

### 15.2 Droppées le 15/09/2026 (ne plus les chercher)

`eco3min_sa_links` (37 302), `eco3min_lc_suggestions`, `eco3min_ad_log`, `eco3min_ad_backup`, `eco3min_rc_cases`, `eco3min_rc_backup`, `eco3min_ah_snapshots` (4531), `eco3min_gsc_data`, `eco3min_gsc_suggestions`, `eco3min_dm_health` — plugins désinstallés ; `e3m_ar_backups`, `e3m_ar_jobs`, `e3m_pad_scan` (25 375), `e3m_pad_backups`, `e3m_redirfix_backup` — anciennes versions d'Anchor Retarget, Patch Audit, Correcteur 301 ; `eco3min_clean_findings`, `eco3min_audit_links` (30 205), `eco3min_audit_imports`, `eco3min_audit_pillars` — Maillage Audit, désactivé le même jour (référentiel déjà migré dans `e3m_referentiel`).

Le mega ne dépend d'aucune d'elles : sa whitelist « drop legacy tables » (onglet Référentiel) et son Diagnostic testent `table_exists` avant de lire. Maillage Cluster ayant été désactivé le même jour, il n'y a plus de second applicateur de patches : l'onglet Maillage du mega est le seul.

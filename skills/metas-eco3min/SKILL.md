---
name: metas-eco3min
description: "Cycle de vie opérationnel des 5 metas éditoriales Eco3min — `_eco3min_level`, `_eco3min_cluster` (slug du PILIER, malgré son nom), `_eco3min_sub_pilier` (slug de la page sous-pilier, SOURCE DE VÉRITÉ), `_eco3min_subpillar` (ID dérivé, fil d'Ariane), `_eco3min_parent_major` — vérifié dans le code et en live le 15/09/2026 : quoi poser, avec quel outil, dans quel ordre, après création manuelle d'une page ou d'un article, après import d'un cluster (Format C v1.1 / multi-pair), ou quand une meta doit être corrigée, écrasée ou VIDÉE. Activer pour « MAJ les metas », « rattache ces pages », « passe X en majeur », « vide le parent_major », « purge cette meta », « liste-moi les plugins et leurs URLs », « split-brain sous-pilier », « le breadcrumb est cassé », « lance l'aligner », « lance la sync », « le verrou », « set-metas », « Import MAJ metas », « Eco3min Fix », « snippet 180 », « snippet 153 », « pages sans ID », et pour toute question sur un contrat d'entrée JSON de ces outils. Doctrine figée juillet 2026 : slug = source de vérité (classifier, scanner, conseil, imports), ID = projection ; sur conflit le slug gagne ; jamais d'ID sans slug ; jamais de SQL direct ; jamais de backfill one-shot (désinstallés le 15/09/2026). Mise en phase auto par le snippet 180 SUBPILLAR SYNC (hooks + cron, étendu aux PAGES le 15/09/2026 : 584 pages portaient un slug sans ID), balayage à la demande et verrou posts + pages par Eco3min Fix onglet 3 (snippet 153), rattrapage batch posts par le Subpillar Aligner 1.2.0, arbitrage des conflits par la Réconciliation du mega 1.0.14. Écriture universelle posts + pages avec dry-run, backup et rollback : ability MCP `eco3min/set-metas` (mode fill/overwrite, dérive l'ID, mais ne recalcule pas l'ID si le slug ne change pas et ne vide jamais une meta) ; pages par slug : Eco3min Import 2.2.1 sous-page « MAJ metas » ; batch fill-only + level overwrite : Cleanup 1.1.0 (un seul import pose level + cluster + sous-pilier, piloté par post_id, parent_major sans backup) ; vider une meta (parent_major résiduel d'un majeur, sub_pilier d'une page sub_pillar, rattachements d'une page exclu) : Eco3min Fix onglet 4 « Purger des metas », seul outil qui efface, réversible. Contient le REGISTRE des outils actifs avec URL wp-admin, contrat d'entrée exact, ce qu'ils écrivent et leur rollback, les pièges (Level Setter sans `satellite`, Diagnostic mega qui compte encore `pillar_with_cluster` comme violation alors qu'un pilier DOIT porter son propre slug, Aligner aveugle aux pages) et le chantier ouvert du 15/09/2026 avec le JSON de purge prêt à coller. Hors périmètre : sémantique des levels et tableau metas-par-level → archi-eco3min ; onglets du mega, scan, conseil, patches, projets A/B/C → plugins-eco3min ; bundles d'import de pages → eco3min-import-contenu-bilingue. Combiner avec archi-eco3min, plugins-eco3min, maillage-orphelins-eco3min, eco3min-import-contenu-bilingue."
---

# Metas Eco3min — cycle de vie & outillage

> Ce skill répond à trois questions récurrentes : **« j'ai créé/importé des pages, quelles metas poser et avec quoi ? »**, **« comment je corrige / je vide une meta ? »** et **« liste-moi les plugins et leurs URLs »**. Il code la doctrine slug/ID **figée juillet 2026**, revérifiée **dans le code et en live le 15/09/2026** (mega 1.0.14, Cleanup 1.1.0, Subpillar Aligner 1.2.0, Level Setter 1.0.0, Eco3min MCP 1.1.1, Eco3min Import 2.2.1, snippets Code Snippets 180 SUBPILLAR SYNC, 153 Eco3min Fix, 18 metabox + breadcrumb, 19 colonne/bulk edit). Le 15/09/2026, le corpus (2 985 contenus publiés) a été passé au crible : les 1 200 articles étaient en phase, **584 pages portaient un slug sans ID** — d'où l'extension du SYNC aux pages et les onglets 3 et 4 du Fix (§2, §3.5, §9).
>
> Sémantique des levels et tableau metas-par-level → `archi-eco3min` §2-3. Workflows mega (scan, conseil, patches, projets A/B/C) → `plugins-eco3min`.

---

## 1. Doctrine figée (juillet 2026) — slug maître, ID dérivé

**Tranche définitivement le débat slug vs ID** ouvert dans `archi-eco3min` §3 (caveat juin 2026) : les deux clés existent, chacune a un rôle, et la hiérarchie est verrouillée.

| Clé | Type | Rôle | Qui la LIT | Qui l'ÉCRIT légitimement |
|---|---|---|---|---|
| `_eco3min_sub_pilier` | **slug** de la page sous-pilier | **SOURCE DE VÉRITÉ** | classifier mega, scanner, mu-analyzer (conseil T1/T2/T3), mu-doctor, Cleanup, exporter snapshot | import cluster / multi-pair, Tinder mega (onglet Scan), Cleanup import, snippet SYNC (2 cas seulement : remonter depuis un ID posé à la main quand le slug est vide, ou convertir un choix humain de metabox) |
| `_eco3min_subpillar` | **ID** de la page sous-pilier | **projection dérivée** — fil d'Ariane + metabox admin | breadcrumb, admin | snippet SYNC (auto), Subpillar Aligner (batch), metabox « Sous-pilier (Page) » (saisie humaine, aussitôt reconvertie en slug par SYNC) |

**Règles non négociables :**
- Le slug n'est **jamais supprimé ni écrasé par une machine**. Le seul chemin qui change un slug existant : un humain choisit une autre page dans la metabox (ID) → SYNC (trigger `id`) pose le slug de cette page comme nouveau canonique. L'ID n'est qu'un **point de saisie anti-typo converti en slug**.
- Sur conflit slug ≠ ID : **le slug gagne**, l'ID est corrigé (SYNC, Aligner) ou supprimé avec backup (Réconciliation mega).
- Ne **jamais** poser l'ID sans slug « pour aller vite » : l'article sortirait du maillage (le conseil et le scanner ne lisent que le slug).
- Ne **jamais** relancer les backfills one-shot obsolètes (Sub-pilier/Major-EN/Classify Backfill) — cause historique du split-brain.

   *(Classify Backfill et les backfills Sub-pilier / Major-EN sont désinstallés depuis le 15/09/2026 ; la règle vaut pour tout script one-shot futur.)*

---

## 2. Les trois mécanismes de mise en phase

Ordre d'escalade — 1 est censé suffire, 2 et 3 sont les filets :

1. **Snippet 180 « SUBPILLAR SYNC » (Code Snippets, auto)** — hooks `updated_post_meta`/`added_post_meta` sur les deux clés : slug écrit (import, Tinder, API WP, `set-metas`, Import MAJ metas) → pose l'ID ; ID écrit (metabox, bulk edit) → slug de cette page devient canonique, ID réaligné. **Cron quotidien `eco3min_sp_cron`** rattrape les écritures SQL brutes. Journal `eco3min_sp_change_log` (200 entrées max) → **bandeau rouge sticky dans l'admin** listant les contenus touchés (lignes ambrées = a ÉCRASÉ un ID manuel), purgé au clic « OK, fermer ». Périmètre : **`post_type` `post` ET `page` depuis le 15/09/2026** (avant : posts seuls — cf pièges §7.3). Garde-fou : un contenu dont le slug résout vers lui-même (page sous-pilier portant son propre slug) n'est jamais touché — c'est une meta à purger (§3.5), pas à synchroniser.

2. **Plugin Subpillar Aligner (batch, à la demande)** — `admin.php?page=eco3min-subpillar-aligner`. Rattrapage massif + migration. Séquence dans l'UI : **Scanner FR → Appliquer FR → Scanner EN → Appliquer EN → Vérifier le verrou**. FR : slug présent → pose/corrige l'ID (slug gagne) ; slug vide + ID posé → remonte le slug (l'article entre dans le maillage). EN : miroir Polylang de la page sous-pilier FR ; remplit l'ID, remplit le slug EN **si vide**, un slug EN divergent est SIGNALÉ (`en_slug_conflict`) jamais écrasé → à trancher en Réconciliation. Backup par session (table `eco3min_spa_backup`), rollback en bas de page. **Verrou (étape 3)** : compte les articles à slug présent mais ID vide/invalide — tant que ≠ 0, ne PAS déployer le breadcrumb ID-only.
3. **Réconciliation mega (arbitrage des conflits)** — `admin.php?page=eco3min-mega-nettoyeur`. Seul onglet MU qui écrit : suppression réversible des ID en conflit (backup `_eco3min_subpillar_backup`, bouton restore). À utiliser quand Aligner/Diagnostic remontent des conflits que « slug gagne » ne doit pas trancher aveuglément.

4. **Eco3min Fix onglet 3 « Sync sous-pilier » (snippet 153, à la demande)** — `admin.php?page=e3m-sync-sp`. Balaye tous les contenus publiés (posts + pages) à slug posé, classe chaque ligne (en phase / ID absent / conflit → slug gagne / slug non résolu / auto-référence), affiche le **verrou posts + pages** (ID absent + conflit) et applique `eco3min_sp_reconcile()` du snippet 180 sur les lignes ID absent et conflit, sans attendre le cron. Réversible : « Annuler la dernière passe » (option `e3m_syncsp_last`). Exige le snippet 180 actif. Les « slug non résolu » (page sous-pilier absente ou dans l'autre langue) et les auto-références demandent une décision humaine.

**État cible** : verrou = 0 → déployer le snippet `breadcrumb-subpillar-id-only.php` (livré dans le ZIP de l'Aligner, dossier `snippet/`) qui retire l'auto-résolution du slug côté breadcrumb — le breadcrumb ne lit plus QUE l'ID, maintenu en phase par SYNC.

Le verrou de l'Aligner ne compte que les posts : **les deux verrous (Aligner ET Fix onglet 3) doivent être à 0**. Au 15/09/2026 le verrou Fix était à 584 (pages) — cf §9.

---

## 3. Workflow A — après CRÉATION MANUELLE d'un article/page

Ce que chaque level doit porter → tableau `archi-eco3min` §3.1. Ce qui suit = **avec quel outil le poser**.

### 3.1 Cas standard (article `post` créé dans l'éditeur)

1. **Sous-pilier** : metabox latérale **« Sous-pilier (Page) »** → choisir la page. Le SYNC convertit en slug maître + réaligne l'ID. C'est TOUT pour le sous-pilier.
2. **Level + cluster (+ parent_major)** : **un seul import Cleanup** suffit désormais (`tools.php?page=eco3min-cleanup`, section 2 Import) :
   ```json
   {"attachments":[{"post_id":27812,"level":"satellite","cluster":"<slug PILIER>","sub_pilier":"<slug PAGE sous-pilier>","parent_major":27555}]}
   ```
   - `level` : **overwrite autorisé** (backup `_e3mc_bak_level`, réversible). 12 valeurs dont `satellite` et `exclu`.
   - `cluster` / `sub_pilier` : **fill-only** (jamais d'écrasement ; backups `_e3mc_bak_cluster` / `_e3mc_bak_sub`).
   - `parent_major` : fill-only, **sans backup** — vérifier le post_id deux fois avant import.
   - Garde-fous : post `publish` obligatoire ; `cluster` ∈ piliers connus ; `sub_pilier` ∈ sous-piliers connus. L'import est **piloté par post_id** — pas besoin que l'article figure dans l'export pending.
3. **Vérifier** : mega Diagnostic (`admin.php?page=eco3min-mega-diagnostic`) → zéro split-brain, metas cohérentes. Puis **re-scan mega** pour que le conseil couvre la page.

*Alternative une-passe* : Tinder mega (onglet Scan) écrit level + cluster + sous-pilier d'un coup via `set_meta_safe` — mais uniquement sur metas vides.

### 3.2 Variantes par level

| Level créé | Spécificité |
|---|---|
| `pillar` | level seul (Level Setter ou Cleanup `level`) ; **aucune** meta de catégorie. |
| `sub_pillar` | level + `cluster` (slug pilier parent) ; **pas** de `sub_pilier`. |
| `major_article` | level + cluster + sub_pilier ; `parent_major` reste **vide**. Puis liens sortants (sous-pilier parent + 1-2 majeurs voisins) via conseil mega ou projet C. |
| `satellite` | les 4 metas. ⚠️ Level Setter ne propose PAS `satellite` → passer par Cleanup `level` ou Tinder. |
| `dataset`/`faq`/`tool`/études | level + cluster + sub_pilier ; parent_major au cas par cas. Rappel : ces levels sont **ignorés par le conseil de maillage** (il ne maille que pillar/sub_pillar/major_article/satellite). |

### 3.3 Level seul, sans toucher au reste

- **Level Setter** (`tools.php?page=eco3min-level-setter`) : post_id un par ligne + select. Préview / Appliquer / Restaurer (backup `_e3m_lvlset_bak`). Ne touche ni cluster ni sous-pilier.
- **Fix onglet 1 « Promote majeur »** (`admin.php?page=e3m-fix`) : uniquement `→ major_article` (backup `_e3m_lvl_bak`).

### 3.4 Outils universels (posts ET pages) — à préférer dès qu'on sort du cas standard

- **Ability MCP `eco3min/set-metas`** (plugin Eco3min MCP 1.1.1) — écrit les 4 metas sur 1 à 50 contenus (post_id ou slug + lang), **dry-run par défaut**, `mode=fill` (défaut, n'écrit que le vide) ou `mode=overwrite`, backup + `eco3min/rollback` par `ref`, purge du cache. Dérive l'ID `_eco3min_subpillar` quand il écrit un slug. Valide : level ∈ 11 valeurs, `cluster` ∈ piliers publiés, `sub_pilier` ∈ sous-piliers publiés (`force=true` pour passer outre), un `pillar` n'accepte que `cluster` = son propre slug et refuse `sub_pilier`/`parent_major`, un `sub_pillar` refuse `sub_pilier`, un `satellite` sans `parent_major` est signalé. Limites : **ne recalcule pas l'ID si le slug ne change pas** (→ Fix onglet 3) et **ignore une valeur vide** (→ Fix onglet 4). C'est l'outil de Claude : un appel dry-run, relecture du plan, puis `dry_run=false`.
- **Eco3min Import 2.2.1 → sous-page « MAJ metas »** (`admin.php?page=eco3min-import-metas`) — **pages uniquement**, résolues par `slug` (+ `parent_slug`/`lang`), bundle `{"import_type":"meta_update","pages":[{lang, slug, level?, cluster?, sub_pilier?, parent_major?, seo?}]}`, `overwrite` défaut `true`, backup `_e3i_bak_eco3min_*`, dry run. Résout l'ID dérivé lui-même. Seul outil qui accepte `parent_major: null` (purge) — sur une page.
- **Cleanup import** (§3.1) reste l'outil du **batch fill-only** après un export pending ; **Level Setter** et **Fix onglet 1** pour du level seul ; **EN Mirror Classifier 1.0.0** (`admin.php?page=eco3min-en-mirror`) pour recopier sur les articles EN la classification de leur miroir FR (catégorie WP + metas), idempotent, backup + rollback, posts uniquement.

### 3.5 Vider une meta — Eco3min Fix onglet 4 « Purger des metas » (snippet 153)

Aucun autre outil n'efface : `set-metas` ignore une valeur vide, Cleanup et Level Setter n'écrivent que des valeurs, Réconciliation ne supprime que l'ID. Cas d'usage : `parent_major` résiduel sur un `major_article` promu, `sub_pilier` sur une page `sub_pillar` (elle en EST un), rattachements d'une page `exclu`, backups `_e3m_rc_bak` du snippet 155 supprimé.

- URL `admin.php?page=e3m-purge-meta`. JSON : `{"items":[{"post_id":123,"keys":["parent_major","sub_pilier"]}]}`. Clés admises : `level`, `cluster`, `sub_pilier`, `subpillar`, `parent_major`, `rc_bak`. Prévisualiser → Appliquer → Restaurer.
- Règle codée : **purger `sub_pilier` purge aussi `subpillar`** (l'ID est une projection du slug ; l'effacement ne déclenche pas les hooks SYNC).
- Backup `_e3m_purge_bak` (JSON `{meta_key: ancienne valeur}`, jamais écrasé) ; Restaurer remet les valeurs sur tous les contenus qui portent ce backup et l'efface — le SYNC repose alors l'ID depuis le slug.
- Après une purge de `level`/`cluster`/`sub_pilier` : re-scan mega (le conseil lit ces metas).

---

## 4. Workflow B — après IMPORT D'UN CLUSTER (mega onglet 3, bundle du projet B au Format C v1.1 ; patches du projet C = maillage, pas de metas)

L'import cluster / multi-pair pose **automatiquement** sur chaque post neuf, via `set_classification_metas` (garde-fou immutabilité) :
`_eco3min_level` + `_eco3min_cluster` + `_eco3min_sub_pilier` (slug), plus `_eco3min_lang`, RankMath, catégorie WP, Polylang, `translation_group_id`. Le `_eco3min_parent_major` est résolu en **2ᵉ passe** depuis les `parent_major_pair_id` du JSON.

**Il ne reste RIEN à poser à la main.** L'ID `_eco3min_subpillar` est posé dans la foulée par le snippet SYNC (les écritures meta de l'import déclenchent les hooks). Checklist post-import :

1. Bandeau rouge SYNC dans l'admin → survoler la liste, « OK, fermer ».
2. **Diagnostic mega** : zéro split-brain, zéro article sans cluster sur les nouvelles paires.
3. **Re-scan mega** (obligatoire) → `e3m_links` frais → conseil T1/T2/T3 couvre le cluster.
4. Si le bundle avait des `parent_major_pair_id` introuvables (log importer) → compléter via Cleanup `parent_major` ou Fix onglet 2.
5. Cas limite : SYNC/cron pas passé (SQL brut, snippet désactivé) → un run **Aligner** FR puis EN remet tout en phase.

---

## 5. Workflow C — désynchronisation constatée (split-brain)

Symptômes : breadcrumb sans sous-pilier alors que le slug est posé ; Diagnostic mega qui liste des conflits ; conseil qui ignore un article pourtant rattaché.

1. **Diagnostic mega** → qualifier : ID manquant (bénin, SYNC/Aligner) vs slug ≠ ID (conflit).
2. ID manquants en masse → **Aligner** (FR → EN → verrou).
3. Conflits slug ≠ ID → **Réconciliation mega** (suppression réversible de l'ID) puis re-run Aligner pour reposer l'ID depuis le slug.
4. `en_slug_conflict` (slug EN divergent du miroir FR) → trancher à la main : soit le slug EN est le bon (page sous-pilier EN différente, légitime) → ne rien faire ; soit erreur → corriger via metabox (le SYNC reconvertit).
5. Jamais de SQL direct sur les 4 metas critiques (règle `archi-eco3min` §3.2) — et le SQL direct ne déclenche pas les hooks SYNC (seul le cron rattrape).

6. **Pages** (datasets, Q&A, outils, imports « Page bilingue ») : l'Aligner ne les voit pas → **Fix onglet 3** (verrou posts + pages, application immédiate) ou attendre le cron du snippet 180. Une page `sub_pillar` qui porte son propre slug en `sub_pilier` apparaît en « auto-référence » : la purger (Fix onglet 4), jamais la synchroniser.

---

## 6. REGISTRE DES PLUGINS — URLs d'ouverture + ce qu'on leur passe

À servir tel quel quand Paul demande « liste-moi les plugins ». Préfixe commun : `https://eco3min.fr/wp-admin/`.

### 6.1 Vérifiés dans le code et en live (15/09/2026)

| Plugin | Version | URL | On lui passe | Il écrit | Rollback |
|---|---|---|---|---|---|
| **Eco3min Mega** (dashboard) | 1.0.14 | `admin.php?page=eco3min-mega` | — | — | — |
| Mega — 📋 Référentiel | — | `admin.php?page=eco3min-mega-referentiel` | édition référentiel, « Re-résoudre catégories WP » | `e3m_referentiel` | — |
| Mega — 📡 Scan & Classification (Tinder) | — | `admin.php?page=eco3min-mega-scan` | validation Tinder (level/cluster/sub_pilier sur metas vides) | 4 metas via `set_meta_safe` | garde-fou immutabilité |
| Mega — 📥 Import cluster | — | `admin.php?page=eco3min-mega-import_cluster` | **bundle JSON Format C v1.1** (projet B) | posts + metas + Polylang + `translation_group_id` | `e3m_backups` |
| Mega — 🔗 Maillage (patches) | — | `admin.php?page=eco3min-mega-maillage` | **patches.json v1.0.2** (projet C) | post_content (liens) | `e3m_backups` par `trigger_ref` |
| Mega — 🕸️ Graphique | — | `admin.php?page=eco3min-mega-graph` | — (export HTML du graphe) | — | — |
| Mega — 📚 Manuel | — | `admin.php?page=eco3min-mega-manuel` | URLs des projets Claude A/B/C (config) | options WP | — |
| Mega — 🩺 Diagnostic | — | `admin.php?page=eco3min-mega-diagnostic` | — (lecture seule : split-brain, cohérence ; ⚠️ compte `pillar_with_cluster` comme violation, cf §7.8) | rien | — |
| Mega — 🧭 Conseil maillage | — | `admin.php?page=eco3min-mega-conseil` | — (lit `e3m_links`, exige scan frais + Cleanup fait) | rien | — |
| Mega — 🧹 Réconciliation | — | `admin.php?page=eco3min-mega-nettoyeur` | validation à l'écran | supprime les ID en conflit (posts + pages) | `_eco3min_subpillar_backup` + restore |
| **Eco3min Cleanup** | 1.1.0 | `tools.php?page=eco3min-cleanup` | JSON `{"attachments":[{post_id, level?, cluster?, sub_pilier?, parent_major?}]}` — cf §3.1 ; posts et pages `publish` ; pas de prévisualisation | `_eco3min_level` (overwrite ok), `_cluster`/`_sub_pilier`/`_parent_major` (fill-only) | `_e3mc_bak_level/_cluster/_sub` (pas parent_major) |
| **Eco3min MCP** — ability `eco3min/set-metas` | 1.1.1 | `tools.php?page=eco3min-mcp` (réglages) ; appel via l'adaptateur MCP | `{"items":[{post_id|slug(+lang), level?, cluster?, sub_pilier?, parent_major?}], "dry_run", "mode":"fill|overwrite", "force"}` — cf §3.4 | les 4 metas + ID dérivé ; posts et pages | backup par `ref` → `eco3min/rollback` |
| **Eco3min Import** — sous-page « MAJ metas » | 2.2.1 | `admin.php?page=eco3min-import-metas` | bundle `{"import_type":"meta_update","pages":[{lang, slug, parent_slug?, level?, cluster?, sub_pilier?, parent_major?|null, seo?}]}`, `overwrite` défaut true — cf §3.4 | les 4 metas + ID dérivé ; **pages uniquement** | `_e3i_bak_eco3min_*` |
| **Eco3min Level Setter** | 1.0.0 | `tools.php?page=eco3min-level-setter` | post_id (un/ligne ou virgules) + level cible — **`satellite` absent du select** | `_eco3min_level` uniquement | `_e3m_lvlset_bak` + Restaurer |
| **Eco3min Subpillar Aligner** | 1.2.0 | `admin.php?page=eco3min-subpillar-aligner` | rien — boutons Scanner/Appliquer FR puis EN, Vérifier le verrou ; **posts uniquement** | `_eco3min_subpillar` (ID) ; slug seulement si vide | table `eco3min_spa_backup`, rollback par session |
| **EN Mirror Classifier** | 1.0.0 | `admin.php?page=eco3min-en-mirror` | rien — recap puis application par chunks | catégorie WP + metas `_eco3min_*` des articles EN, en miroir du FR | backup + rollback intégrés |
| **Eco3min Fix** (snippet Code Snippets **153**, pas un plugin) | — | `admin.php?page=e3m-fix` | onglet 1 « Promote majeur » : post_id ou URL un/ligne (`→ major_article`) | `_eco3min_level` | `_e3m_lvl_bak` + Restaurer |
| ↳ onglet 2 « Import parent_major » | — | `admin.php?page=e3m-import-pm` | `{"items":[{post_id, parent_major}]}` — refuse cible non `major_article` et langues différentes | `_eco3min_parent_major` | `_e3m_pm_bak` + Restaurer |
| ↳ onglet 3 « Sync sous-pilier » (15/09/2026) | — | `admin.php?page=e3m-sync-sp` | rien — verrou posts + pages, Appliquer, Annuler la dernière passe — cf §2.4 | `_eco3min_subpillar` (ID) via snippet 180 | option `e3m_syncsp_last` |
| ↳ onglet 4 « Purger des metas » (15/09/2026) | — | `admin.php?page=e3m-purge-meta` | `{"items":[{post_id, keys:[level|cluster|sub_pilier|subpillar|parent_major|rc_bak]}]}` — cf §3.5 | **efface** les metas listées | `_e3m_purge_bak` + Restaurer |

### 6.2 Autres plugins actifs (live 15/09/2026) qui touchent aux metas ou aux paires

| Plugin | Version | URL | Usage |
|---|---|---|---|
| Translator Bridge | 1.3.0 | `tools.php?page=eco3min-translator` | FR→EN massif (export, import, rewrite links, fix categories, liens cross-langue) |
| Q&A Importer v2 | 2.0 | `tools.php?page=eco3min-qa-import` | paires FR/EN de pages Q&A (metas posées à l'import ; l'ID est désormais dérivé par le SYNC) |
| Polylang Repair | 1.0.3 | `admin.php?page=eco3min-polylang-repair` | mapping Polylang des 80 pages Q&A des batches 7/08/32/33 |

Les 27 plugins maison actifs, avec version, rôle et URL, sont inventoriés dans `plugins-eco3min` §1.1 — ne pas dupliquer ici.

### 6.3 Disparus (ni actifs ni dans le dépôt au 15/09/2026) — ne jamais les proposer

Level Classifier, GSC Linker, Dataset Monitor, Hub, Pillar Audit, SQL Runner, Meta Monitor, Classify Backfill et les backfills Sub-pilier / Major-EN. Anchor Doctor (1.6.0, `admin.php?page=e3m-anchor-doctor`), Link Doctor (1.0.5, `admin.php?page=eco3ld`) et Correcteur de liens 301 (1.0.0, `tools.php?page=e3m-rlf`) existent mais ne touchent pas aux metas. Ne **jamais** inventer une URL de plugin : `ewpa/get-active-plugins` donne l'état live.

### 6.4 Code Snippets liés aux metas (pas des plugins)

| Snippet | ID | Rôle |
|---|---|---|
| **SUBPILLAR SYNC** | 180 | mise en phase auto slug→ID (hooks + cron `eco3min_sp_cron`), posts + pages depuis le 15/09/2026, bandeau admin, journal `eco3min_sp_change_log` |
| **Eco3min Fix** | 153 | 4 onglets : Promote majeur, Import parent_major, Sync sous-pilier, Purger des metas (cf 6.1) |
| Metabox « Sous-pilier (Page) » + breadcrumb (« redir breadcrumbs ») | 18 | saisie humaine de l'ID sur les **posts** (reconvertie en slug par SYNC) ; filtre `rank_math/frontend/breadcrumb/items` : articles = catégorie WP remappée en pilier (libellé court) + sous-pilier lu par l'ID avec **fallback slug** ; **pages depuis le 15/09/2026** = même fil, Accueil > pilier (`_eco3min_cluster` résolu dans la langue, libellé court des articles) > sous-pilier > ancêtres WP restants > page, défaut Rank Math si pas de cluster ou level pillar/exclu ; le JSON-LD BreadcrumbList suit ; la version `breadcrumb-subpillar-id-only.php` (dossier `snippet/` du plugin Aligner) retire ce fallback et ne se déploie que quand les DEUX verrous (Aligner + Fix onglet 3) sont à 0 |
| Colonne + bulk edit + filtre « Sous-pilier » (« edition groupe ss piliers ») | 19 | liste des articles : colonne, bulk edit (écrit l'ID → SYNC reconvertit), filtre par sous-pilier ; posts uniquement |
| ~~Reclassement orphelins~~ | ~~155~~ | one-shot supprimé le 15/09/2026 (19 cibles déjà au level voulu) ; sa fonction = Level Setter / `set-metas` / Cleanup ; ses backups `_e3m_rc_bak` se purgent avec Fix onglet 4 (`rc_bak`) |

---

## 7. Pièges

1. **Level Setter n'a pas `satellite`** dans son select → satellite via Cleanup (`level`) ou Tinder.
2. **`parent_major` importé par Cleanup n'a PAS de backup** — seul champ non réversible du contrat. Vérifier les post_id avant Appliquer.

3. **SYNC couvre posts + pages depuis le 15/09/2026, mais l'Aligner et les snippets 18/19 restent `post_type = post`.** Le verrou de l'Aligner est donc aveugle aux pages : lire aussi le verrou de Fix onglet 3. Sur une page, pas de metabox : le slug se pose par `set-metas`, Import « MAJ metas », Cleanup ou Tinder, et l'ID suit.

4. **Écriture SQL directe** : ne déclenche pas les hooks SYNC → phase rattrapée seulement au cron du lendemain. Raison de plus pour l'interdit SQL d'`archi-eco3min` §3.2.
5. **Dette connue du snippet SYNC** : `register_deactivation_hook(__FILE__)` est inopérant dans Code Snippets (pas de fichier plugin) → si le snippet est désactivé, l'événement cron `eco3min_sp_cron` reste planifié (no-op inoffensif, mais pollue la cron table ; purge manuelle via WP-Crontrol/SQL Runner si besoin).

6. **Contrat Cleanup, aligné dans `plugins-eco3min` §14.8 le 15/09/2026** : le Cleanup accepte `level` (overwrite réversible) → « promouvoir en majeur = deux outils Fix + Cleanup » n'est plus obligatoire, un seul import Cleanup suffit. Fix onglet 1 reste valable pour du level-only rapide. L'import Cleanup est piloté par post_id, pas par l'export pending. Après une promotion `satellite → major_article`, **purger le `parent_major` résiduel** (Fix onglet 4) : Cleanup ne l'efface pas.

7. **Supersede `archi-eco3min` caveat §3 (juin 2026)** : le statut de `_eco3min_sub_pilier` est CONFIRMÉ — c'est la clé maître lue par tout le moteur. Ne plus purger ce « split-brain » : les deux clés sont voulues, c'est la DÉSYNCHRONISATION qui est le défaut, pas la coexistence.

8. **Diagnostic mega 1.0.14 : `pillar_with_cluster` est compté comme violation** dans `meta_coherence()` (tab 7 / mu-doctor) alors que depuis le 15/09/2026 un pilier **doit** porter `_eco3min_cluster` = son propre slug (sinon le conseil de maillage ignore son silo — check `pillar_without_cluster` de `eco3min/health`, 9 piliers concernés ce jour-là). Ignorer ce compteur jusqu'au correctif du mega ; ne jamais « corriger » un pilier en lui retirant son cluster.
9. **`set-metas` ne recalcule pas l'ID si le slug ne change pas** et **ignore une valeur vide** : pour reposer un ID manquant → Fix onglet 3 ; pour effacer → Fix onglet 4. Purger `sub_pilier` sans purger `subpillar` laisserait un ID orphelin : l'onglet 4 l'impose.

---

## 8. Ce que Claude produit quand Paul demande…

- **« MAJ les metas de ces pages »** → (a) tableau post_id × metas cibles (valeurs tirées d'`archi-eco3min` §5-6) ; (b) le JSON `attachments` Cleanup prêt à coller (level inclus si re-classification) ; (c) rappel metabox pour le sous-pilier si saisie unitaire ; (d) séquence : Cleanup → Diagnostic → re-scan mega.
- **« J'ai importé le cluster X, quoi faire côté metas ? »** → checklist §4 (rien à poser, tout vérifier).
- **« Liste-moi les plugins »** → tables §6, URLs complètes, sans inventer les slugs manquants.
- **« Le breadcrumb est cassé / split-brain »** → escalade §5 (Diagnostic → Aligner → Réconciliation), jamais de SQL direct.

- **« Vide / purge cette meta »** → JSON `items[{post_id, keys}]` pour Fix onglet 4, avec la raison par ligne ; rappel que `sub_pilier` entraîne `subpillar` ; séquence : Prévisualiser → Appliquer → re-scan mega si level/cluster/sub_pilier.
- **« Lance la sync / c'est quoi le verrou »** → Fix onglet 3 (posts + pages) puis Aligner (posts, FR → EN) ; les deux verrous à 0 avant le breadcrumb ID-only ; les « non résolus » et « auto-références » sont à trancher à la main, jamais forcés.

---

## 9. Chantier ouvert au 15/09/2026 (état mesuré sur 2 985 contenus publiés via `eco3min/find`)

**Étapes 1 et 2 exécutées le 15/09/2026** (snippets déployés, purge appliquée, sync : verrou Fix 0, verrou Aligner 0, `eco3min/health` → `subpillar_desync` 0 et `dangling_refs` 0 ; les 5 derniers cas étaient des mélanges de langue — slug FR sur contenu EN, slug « — » — corrigés par `set-metas` overwrite, ref `metas-20260915-155129-e1308c`). Restent les étapes 3 et 4. Ordre d'origine, à rejouer tel quel si un import recrée la situation :

1. **Purger** (Fix onglet 4) — 4 pages `sub_pillar` FR portant leur propre slug (747, 1105, 1473, 1663 : sans cette purge, elles sortent en « auto-référence » de l'onglet 3), 10 `major_article` avec `parent_major` résiduel (posts 2131, 8023, 8099, 17162, 17982, 19408, 19412, 19424 ; pages 20555, 20559), et les 19 backups `_e3m_rc_bak` du snippet 155. JSON prêt à coller :
   ```json
   {"items":[{"post_id":20555,"keys":["parent_major"]},{"post_id":20559,"keys":["parent_major"]},{"post_id":1663,"keys":["sub_pilier"]},{"post_id":1473,"keys":["sub_pilier"]},{"post_id":1105,"keys":["sub_pilier"]},{"post_id":747,"keys":["sub_pilier"]},{"post_id":19424,"keys":["parent_major"]},{"post_id":19412,"keys":["parent_major"]},{"post_id":19408,"keys":["parent_major"]},{"post_id":17982,"keys":["parent_major"]},{"post_id":17162,"keys":["parent_major"]},{"post_id":8099,"keys":["parent_major"]},{"post_id":8023,"keys":["parent_major"]},{"post_id":2131,"keys":["parent_major"]},{"post_id":10,"keys":["rc_bak"]},{"post_id":5741,"keys":["rc_bak"]},{"post_id":1323,"keys":["rc_bak"]},{"post_id":5916,"keys":["rc_bak"]},{"post_id":3551,"keys":["rc_bak"]},{"post_id":16527,"keys":["rc_bak"]},{"post_id":17329,"keys":["rc_bak"]},{"post_id":7676,"keys":["rc_bak"]},{"post_id":6736,"keys":["rc_bak"]},{"post_id":15801,"keys":["rc_bak"]},{"post_id":11115,"keys":["rc_bak"]},{"post_id":22333,"keys":["rc_bak"]},{"post_id":25395,"keys":["rc_bak"]},{"post_id":25399,"keys":["rc_bak"]},{"post_id":25400,"keys":["rc_bak"]},{"post_id":7832,"keys":["rc_bak"]},{"post_id":7902,"keys":["rc_bak"]},{"post_id":24334,"keys":["rc_bak"]},{"post_id":24335,"keys":["rc_bak"]}]}
   ```
   (un `rc_bak` « déjà absente » est un rejet normal.)
2. **Synchroniser** (Fix onglet 3) — verrou attendu ≈ 584 pages (237 satellites, 143 majeurs, 139 faq, 25 tools, 18 exclu, 17 datasets, 1 beginner) ; Appliquer ; « OK, fermer » sur le bandeau du 180 (journal plafonné à 200 lignes) ; vérifier verrou = 0 puis Aligner FR → EN → verrou = 0.
3. **Backlog de classification** (pas un défaut d'outillage) : 303 pages sans level (`eco3min/health` → `unclassified`), 161 satellites sans `parent_major` (112 pages, 49 posts), 665 pages classées sans cluster dont 615 `faq`, 19 pages `exclu` encore rattachées (dont la home 10 : cluster + sous-pilier + parent_major). Traiter par `set-metas` (dry-run) ou Cleanup, puis re-scan.
4. **Décision ouverte — doctrine des pages `faq`** : au 15/09/2026, 140 Q&A portent un pilier thématique + sous-pilier (rattachement ancien) et 475 portent le hub `qa`/`qr` (lot Cleanup du 15/09, cluster déduit de l'URL). Leurs liens sortants : 39 % vers le hub, 37 % vers leur thématique dominante, 24 % ailleurs — aucun choix ne l'emporte sur le maillage, mais il en faut un seul. Recommandation : thématique + sous-pilier quand il est fiable, hub sinon ; passage par re-export Cleanup pending puis `set-metas` overwrite (le cluster est fill-only dans Cleanup). Le breadcrumb des pages (snippet 18) affiche dans les deux cas le hub en parent.
5. **Test de cohérence à rejouer après tout rattachement de pages** : sous-pilier en meta ≠ sous-pilier de l'URL (segment 2) → le 15/09/2026 il a sorti 22 pages (crisis-hub / bascules-de-regime rattachées par heuristique de liens à des sous-piliers commodities, corrigées par `set-metas`, ref `metas-20260915-194215-e79a3d`). Cluster ≠ pilier d'URL n'est PAS une erreur pour les satellites thématiques sous un hub (`/comparatif/`, `/compare/`, `/idees-recues/`, `/mistakes/`).
6. **Mega 1.0.15 à prévoir** : retirer `pillar_with_cluster` du Diagnostic (§7.8) ; étendre le verrou de l'Aligner aux pages ou le documenter comme posts-only.

Refaire la mesure avant de rejouer ce chantier : ces chiffres datent du 15/09/2026.

---
name: metas-eco3min
description: Cycle de vie opérationnel des metas Eco3min (`_eco3min_level`, `_eco3min_cluster`, `_eco3min_sub_pilier` slug MAÎTRE, `_eco3min_subpillar` ID dérivé, `_eco3min_parent_major`) : quoi poser, avec quel outil, dans quel ordre, après création manuelle d'une page/article ou après import d'un cluster (Format C v1.1 / multi-pair). Doctrine figée juillet 2026 : slug = source de vérité (classifier, scanner, conseil, imports), ID = projection fil d'Ariane, mise en phase auto par le snippet SUBPILLAR SYNC (hooks + cron), rattrapée en batch par le plugin Subpillar Aligner, arbitrée par la Réconciliation du mega. Contient le REGISTRE des plugins actifs avec URL wp-admin et contrat d'entrée exact (le Cleanup accepte désormais `level` en overwrite réversible — supersede plugins-eco3min §14.8). Activer pour « MAJ les metas », « rattache ces pages », « passe X en majeur », « liste-moi les plugins et leurs URLs », « split-brain sous-pilier », « lance l'aligner ». Sémantique → archi-eco3min ; mega → plugins-eco3min.
---

# Metas Eco3min — cycle de vie & outillage

> Ce skill répond à deux questions récurrentes : **« j'ai créé/importé des pages, quelles metas poser et avec quoi ? »** et **« liste-moi les plugins et leurs URLs »**. Il code la doctrine slug/ID **figée juillet 2026** (vérifiée dans le code du mega v1.0.13.1, du Cleanup v1.0.1 build juillet, du Subpillar Aligner v1.2.0 et du snippet SUBPILLAR SYNC).
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

---

## 2. Les trois mécanismes de mise en phase

Ordre d'escalade — 1 est censé suffire, 2 et 3 sont les filets :

1. **Snippet « SUBPILLAR SYNC » (Code Snippets, auto)** — hooks `updated_post_meta`/`added_post_meta` sur les deux clés : slug écrit (import, Tinder, API WP) → pose l'ID ; ID écrit (metabox) → slug de cette page devient canonique, ID réaligné. **Cron quotidien `eco3min_sp_cron`** rattrape les écritures SQL brutes. Journal `eco3min_sp_change_log` (200 entrées max) → **bandeau rouge sticky dans l'admin** listant les articles touchés (lignes ambrées = a ÉCRASÉ un ID manuel), purgé au clic « OK, fermer ». Périmètre : **`post_type = post` uniquement** (les PAGES ne sont pas couvertes — cf pièges §7).
2. **Plugin Subpillar Aligner (batch, à la demande)** — `admin.php?page=eco3min-subpillar-aligner`. Rattrapage massif + migration. Séquence dans l'UI : **Scanner FR → Appliquer FR → Scanner EN → Appliquer EN → Vérifier le verrou**. FR : slug présent → pose/corrige l'ID (slug gagne) ; slug vide + ID posé → remonte le slug (l'article entre dans le maillage). EN : miroir Polylang de la page sous-pilier FR ; remplit l'ID, remplit le slug EN **si vide**, un slug EN divergent est SIGNALÉ (`en_slug_conflict`) jamais écrasé → à trancher en Réconciliation. Backup par session (table `eco3min_spa_backup`), rollback en bas de page. **Verrou (étape 3)** : compte les articles à slug présent mais ID vide/invalide — tant que ≠ 0, ne PAS déployer le breadcrumb ID-only.
3. **Réconciliation mega (arbitrage des conflits)** — `admin.php?page=eco3min-mega-nettoyeur`. Seul onglet MU qui écrit : suppression réversible des ID en conflit (backup `_eco3min_subpillar_backup`, bouton restore). À utiliser quand Aligner/Diagnostic remontent des conflits que « slug gagne » ne doit pas trancher aveuglément.

**État cible** : verrou = 0 → déployer le snippet `breadcrumb-subpillar-id-only.php` (livré dans le ZIP de l'Aligner, dossier `snippet/`) qui retire l'auto-résolution du slug côté breadcrumb — le breadcrumb ne lit plus QUE l'ID, maintenu en phase par SYNC.

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

---

## 6. REGISTRE DES PLUGINS — URLs d'ouverture + ce qu'on leur passe

À servir tel quel quand Paul demande « liste-moi les plugins ». Préfixe commun : `https://eco3min.fr/wp-admin/`.

### 6.1 Vérifiés dans le code (juillet 2026)

| Plugin | Version | URL | On lui passe | Il écrit | Rollback |
|---|---|---|---|---|---|
| **Eco3min Mega** (dashboard) | 1.0.13.1 | `admin.php?page=eco3min-mega` | — | — | — |
| Mega — 📋 Référentiel | — | `admin.php?page=eco3min-mega-referentiel` | édition référentiel, « Re-résoudre catégories WP » | `e3m_referentiel` | — |
| Mega — 📡 Scan & Classification (Tinder) | — | `admin.php?page=eco3min-mega-scan` | validation Tinder (level/cluster/sub_pilier sur metas vides) | 4 metas via `set_meta_safe` | garde-fou immutabilité |
| Mega — 📥 Import cluster | — | `admin.php?page=eco3min-mega-import_cluster` | **bundle JSON Format C v1.1** (projet B) | posts + metas + Polylang + `translation_group_id` | `e3m_backups` |
| Mega — 🔗 Maillage (patches) | — | `admin.php?page=eco3min-mega-maillage` | **patches.json v1.0.2** (projet C) | post_content (liens) | `e3m_backups` par `trigger_ref` |
| Mega — 🕸️ Graphique | — | `admin.php?page=eco3min-mega-graph` | — (export HTML du graphe) | — | — |
| Mega — 📚 Manuel | — | `admin.php?page=eco3min-mega-manuel` | URLs des projets Claude A/B/C (config) | options WP | — |
| Mega — 🩺 Diagnostic | — | `admin.php?page=eco3min-mega-diagnostic` | — (lecture seule : split-brain, cohérence) | rien | — |
| Mega — 🧭 Conseil maillage | — | `admin.php?page=eco3min-mega-conseil` | — (lit `e3m_links`, exige scan frais + Cleanup fait) | rien | — |
| Mega — 🧹 Réconciliation | — | `admin.php?page=eco3min-mega-nettoyeur` | validation à l'écran | supprime les ID en conflit | `_eco3min_subpillar_backup` + restore |
| **Eco3min Cleanup** | 1.0.1 | `tools.php?page=eco3min-cleanup` | JSON `{"attachments":[{post_id, level?, cluster?, sub_pilier?, parent_major?}]}` — cf §3.1 | `_eco3min_level` (overwrite ok), `_cluster`/`_sub_pilier`/`_parent_major` (fill-only) | `_e3mc_bak_level/_cluster/_sub` (pas parent_major) |
| **Eco3min Level Setter** | 1.0.0 | `tools.php?page=eco3min-level-setter` | post_id (un/ligne ou virgules) + level cible — **`satellite` absent du select** | `_eco3min_level` uniquement | `_e3m_lvlset_bak` + Restaurer |
| **Eco3min Subpillar Aligner** | 1.2.0 | `admin.php?page=eco3min-subpillar-aligner` | rien — boutons Scanner/Appliquer FR puis EN, Vérifier le verrou | `_eco3min_subpillar` (ID) ; slug seulement si vide | table `eco3min_spa_backup`, rollback par session |
| **Eco3min Fix** | — | `admin.php?page=e3m-fix` | onglet 1 : post_id un/ligne (`→ major_article`) ; onglet 2 : import parent_major (satellites) | `_eco3min_level` / `_eco3min_parent_major` | `_e3m_lvl_bak` + Restaurer |

### 6.2 Actifs, URL documentée dans `archi-eco3min` §11.1 (non revérifiée juillet)

| Plugin | URL | Usage |
|---|---|---|
| Level Classifier v1.5.1 | `admin.php?page=eco3min-level-classifier` | **UNIQUEMENT** inférer le level des `uncategorized` (tout le reste du LC est mort) |
| Translator Bridge 1.1.0 | `admin.php?page=eco3min-translator` | traduction EN |
| GSC Linker 1.2.0 | `admin.php?page=eco3min-gsc-linker` | import GSC + suggestions |
| Dataset Monitor 1.0.0 | `admin.php?page=eco3min-datasets` | health check datasets |
| Hub 1.2.0 | `admin.php?page=eco3min-hub` | landing outils |
| Q&A Importer v2 | `admin.php?page=eco3min-q-and-a` | import Q&A |

### 6.3 Actifs, slug de menu À VÉRIFIER (relever dans WP : survoler l'entrée de menu, ou Extensions → nom du dossier)

Pillar Audit 1.6.1, SQL Runner 1.0.1, Anchor Doctor 1.3.x, link-doctor, fix-301. Quand un slug est vérifié, l'ajouter en 6.1/6.2 — ne **jamais** inventer une URL de plugin.

### 6.4 Code Snippets liés aux metas (pas des plugins)

| Snippet | Rôle |
|---|---|
| **SUBPILLAR SYNC** | mise en phase auto slug→ID (hooks + cron `eco3min_sp_cron`), bandeau admin, journal `eco3min_sp_change_log` |
| Metabox « Sous-pilier (Page) » + breadcrumb | saisie humaine de l'ID ; version `breadcrumb-subpillar-id-only.php` (dans le ZIP Aligner) à déployer **seulement** quand le verrou Aligner = 0 |

---

## 7. Pièges

1. **Level Setter n'a pas `satellite`** dans son select → satellite via Cleanup (`level`) ou Tinder.
2. **`parent_major` importé par Cleanup n'a PAS de backup** — seul champ non réversible du contrat. Vérifier les post_id avant Appliquer.
3. **SYNC et Aligner ne traitent que `post_type = post`.** Les PAGES (datasets, sous-piliers, imports « Page bilingue ») sont hors périmètre — normal pour les pages sous-piliers (elles n'ont pas de meta sous-pilier), mais toute page qui porterait ces metas ne sera jamais resynchronisée automatiquement.
4. **Écriture SQL directe** : ne déclenche pas les hooks SYNC → phase rattrapée seulement au cron du lendemain. Raison de plus pour l'interdit SQL d'`archi-eco3min` §3.2.
5. **Dette connue du snippet SYNC** : `register_deactivation_hook(__FILE__)` est inopérant dans Code Snippets (pas de fichier plugin) → si le snippet est désactivé, l'événement cron `eco3min_sp_cron` reste planifié (no-op inoffensif, mais pollue la cron table ; purge manuelle via WP-Crontrol/SQL Runner si besoin).
6. **Supersede `plugins-eco3min` §14.8** : le contrat Cleanup accepte désormais `level` (overwrite réversible) → « promouvoir en majeur = deux outils Fix + Cleanup » n'est plus obligatoire, un seul import Cleanup suffit. Fix reste valable pour du level-only rapide. De même, gâche #1 tranchée : l'import Cleanup est piloté par post_id, pas par l'export pending.
7. **Supersede `archi-eco3min` caveat §3 (juin 2026)** : le statut de `_eco3min_sub_pilier` est CONFIRMÉ — c'est la clé maître lue par tout le moteur. Ne plus purger ce « split-brain » : les deux clés sont voulues, c'est la DÉSYNCHRONISATION qui est le défaut, pas la coexistence.

---

## 8. Ce que Claude produit quand Paul demande…

- **« MAJ les metas de ces pages »** → (a) tableau post_id × metas cibles (valeurs tirées d'`archi-eco3min` §5-6) ; (b) le JSON `attachments` Cleanup prêt à coller (level inclus si re-classification) ; (c) rappel metabox pour le sous-pilier si saisie unitaire ; (d) séquence : Cleanup → Diagnostic → re-scan mega.
- **« J'ai importé le cluster X, quoi faire côté metas ? »** → checklist §4 (rien à poser, tout vérifier).
- **« Liste-moi les plugins »** → tables §6, URLs complètes, sans inventer les slugs manquants.
- **« Le breadcrumb est cassé / split-brain »** → escalade §5 (Diagnostic → Aligner → Réconciliation), jamais de SQL direct.

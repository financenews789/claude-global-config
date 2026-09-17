# plugins-eco3min — référence : Mega-plugin — versions, garde-fou d'immutabilité, Format C v1.1, conventions de code (§10, §12.1, §12.3-12.6)

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026), sauf §12.1 (liste de versions complétée 1.0.14, Réconciliation corrigée) et une phrase de §12.5 (stratégie A : résolution de `parent_major_pair_id` dans le batch ; le multi-pair existe mais n'est pas la route) — corrigés le 15/09/2026 d'après le code. Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

---

## 12. Mega-plugin Eco3min

### 12.1 Vue d'ensemble

Le **mega-plugin Eco3min** unifie 6 plugins legacy en une seule extension WordPress et ajoute 3 modules nouveaux. Il a été conçu pour cohabiter avec les plugins legacy (préfixes BDD distincts `e3m_` vs `eco3min_`, hooks distincts) ; depuis le 15/09/2026 les six absorbés sont tous désinstallés ou désactivés, la question ne se pose plus.

**Versionning** (README du plugin + en-tête `eco3min-mega.php`) :
- **V0.1 (jan 2026)** — MVP minimal : tables + onglets 1/3/4 + garde-fou immutabilité + Format C v1.1
- **V0.5 (fév 2026)** — Scan + Tinder UI + state machine + export chunked + cron daily
- **V1.0 (mar 2026)** — 5 onglets actifs, scanner read-only, exporters, graphique Cytoscape.js, Anchor Diversifier + Redundant Cleaner en scan-only, drop legacy tables, historiques + rollback
- **V1.0.1 → V1.0.9 (mar-mai 2026)** — exporter SNAPSHOT pour les projets A/B ; import multi-pair (sessions reprenables, idempotentes) ; bandeau dirty rouge persistant ; route AJAX de download (bypass `.htaccess` OVH) ; onglet Manuel + UUIDs des projets Claude ; analyzer T1/T2/T3 porté du Level Classifier (abandonné en V1.0.10)
- **V1.0.10 (mai 2026)** — refonte cross-cluster : Format A → « SANS HTML », Format B → « AVEC HTML » filtré sur post_ids ; suppression complète de l'analyzer T1/T2/T3 et de l'exporter LIGHT ; champ `cross_cluster_targets` (phase 2 du projet B) + auto-export en fin d'import multi-pair
- **V1.0.11 (mai 2026)** — drag & drop multi-fichiers (`Eco3min_Mega_Upload_Helper`, hook `eco3min_mega_upload_imports`, `.json` ≤ 10 Mo, anti-collision) dans Import cluster et Maillage : plus besoin de FileZilla
- **V1.0.12 (mai 2026)** — apply des patches chunked + progress bar live post par post (`eco3min_mega_import_patches_apply_start` / `_chunk`, session dans un transient 1 h, reprise) ; spinner sur le dry run
- **V1.0.13 / 1.0.13.1 (juin 2026)** — **Fusion du plugin « Maillage Ultime »** en 3 onglets internes : 🩺 **Diagnostic** (split-brain sous-pilier, cohérence des metas), 🧭 **Conseil** (conseil de maillage T1/T2/T3 read-only sur les tables `e3m_*`, JSON pour le projet C), 🧹 **Réconciliation** (mesure slug_only / conflits slug ≠ ID ; seul onglet MU qui écrit : suppression réversible des ID sous-pilier en conflit, slug fait foi, bouton Restaurer). Les 4 classes MU vivent dans `includes/maillage-ultime/` avec `require` protégés `if (!class_exists())`. **Piège résolu** : ne JAMAIS laisser le plugin « Maillage Ultime » séparé actif en même temps (collision de redéclaration de classe → écran blanc). Le conseil de l'onglet Conseil lit `wp_e3m_links` (`$wpdb->prefix.'e3m_links'`), rempli par le scan mega.
- **V1.0.14 (live au 17/09/2026)** — 2 exports CSV additifs dans l'onglet Maillage, section Snapshot : `eco3min_mega_export_snapshot_csv` → `eco3min-snapshot-{date}.csv` (même périmètre et même requête que le snapshot JSON, inchangé) ; `eco3min_mega_export_maillage_csv` → `eco3min-maillage-{date}.csv` (1 ligne par lien interne résolu, lu depuis `e3m_links` par pages de 5000, date du dernier scan en 1re ligne). Route de download jumelle `eco3min_mega_download_export_csv`. Helper `Eco3min_Mega_CSV` (BOM UTF-8, 1 record = 1 ligne).
- **V1.0.15 (dépôt, 17/09/2026 — jamais mis en ligne seul, embarqué dans 1.0.16)** — Format C v1.1 : `satellite` ajouté à `Eco3min_Mega_Validator::VALID_LEVELS`, avec la règle 4f « un `satellite` exige un `parent_major_pair_id` » ; le projet B livre les satellites classés, plus de Tinder post-import. Diagnostic (mu-doctor) : `pillar_with_cluster` (faux positif) devient `pillar_without_cluster`, aligné sur `eco3min/health` ; texte du split-brain (SUBPILLAR SYNC) et de la « Fracture B » (le conseil lit `e3m_links`, tables legacy droppées) mis à jour. Aucun changement de table ni d'onglet.
- **V1.0.16 (live depuis le 17/09/2026 au soir)** — Snapshot JSON et CSV : `format_article()` (`class-eco3min-mega-exporter-snapshot.php`) prend `get_permalink($post_id)` au lieu de `home_url + langue + slug` ; repli plat si la permalink est vide. La colonne `url` devient fiable (imbriquée pour les sous-piliers, `/qr/` `/qa/` pour les Q&A). Lecture seule, aucune écriture en base, même requête SQL qu'avant.
- **V2.0 (prévu)** — Reclassification UI + WP-CLI + webhooks

**Auto-migration** : au boot, si `get_option('eco3min_mega_db_version') !== ECO3MIN_MEGA_VERSION`, `Installer::activate()` relance `dbDelta` sur toutes les tables. Plus besoin de désactiver/réactiver le plugin pour upgrader : remplacer les fichiers via SFTP suffit.

> Le **plugin Cleanup** (1.1.0, live depuis le 15/09/2026) est **séparé** du mega (extension à part, menu Outils), pas un onglet. C'est volontaire : c'est un outil one-shot de remise en ordre, exécuté avant le conseil.

### 12.2 Mapping legacy → mega — voir `references/01-inventaire-plugins-actifs.md` §12.2

### 12.3 Tables BDD du mega — voir section 4.2 (`references/05-tables-sql-bugs-diagnostic.md`)

10 tables `e3m_*` créées ou migrées à l'activation et à chaque changement de version (`dbDelta`, idempotent). La table `eco3min_audit_pillars` est migrée vers `e3m_referentiel` automatiquement (idempotent).

### 12.4 Garde-fou immutabilité de la classification

**Principe non-négociable** : le travail Tinder humain de Paul (615 articles classifiés à la main) ne peut jamais être écrasé par le mega.

**5 couches de défense** :

1. **Scan read-only** — Le scanner V0.5 LIT les metas mais n'ÉCRIT JAMAIS dessus.
2. **Queue Tinder filtrée** — Le Tinder V0.5 n'enqueue que les articles avec metas vides.
3. **`set_meta_safe()`** — Toute écriture sur `_eco3min_level/_cluster/_sub_pilier/_parent_major` passe par `Eco3min_Mega_Classifier::set_meta_safe($post_id, $key, $value, $strict=true)`. Throw `Eco3min_Mega_Immutability_Exception` si la meta existe déjà avec une valeur différente. Idempotent si valeur identique.
4. **Import cluster sur posts neufs** — `Eco3min_Mega_Importer_Cluster` crée des posts via `wp_insert_post()` (jamais d'update sur posts existants). Refuse l'import si slug déjà utilisé.
5. **Tests unitaires** (à écrire en V0.5).

**Conséquence pratique** : le mega ne fournit PAS d'UI de reclassification en V0.1-V1.0 (réservé V2.0 avec triple confirmation). Pour modifier une classification existante : Cleanup import (`level` en overwrite réversible), `eco3min/set-metas` en `mode=overwrite`, Level Setter ou Fix — jamais Custom Fields ni SQL (les hooks du snippet SUBPILLAR SYNC ne se déclencheraient pas). Meta Monitor n'existe plus (cf référence 01 §1.2).

### 12.5 Format C v1.1 bilingue (input de l'onglet 3)

Format JSON consommé par l'onglet 3 du mega. Produit par le **projet B Writer**. Chaque entrée `articles[]` contient une paire FR + EN appariée (sous-objets imbriqués). **Le JSON importable est le batch unique du cluster** (toutes les paires en `articles[]`, `operation: create_cluster_bilingual`, stratégie A — c'est ce que le projet B livre sur « bundle ») ; sur ce chemin d'import, `parent_major_pair_id` est résolu dans le batch : un satellite livré dans un fichier importé seul ne se rattache pas. Le mode « multi-pair » du mega (un fichier `create_pair_bilingual` par paire, résolution au niveau de la session, auto-export cross-cluster) existe mais n'est pas la route retenue. `expected_pairs_count` (dans `validation_metadata`) doit égaler `len(articles)`.

```json
{
  "operation": "create_cluster_bilingual",
  "format_version": "1.1.0",
  "cluster_metadata": {
    "fr": { "pillar_slug": "...", "sub_pilier_slug": "...", "wp_category_slug": "..." },
    "en": { "pillar_slug": "...", "sub_pilier_slug": "...", "wp_category_slug": "..." }
  },
  "articles": [
    {
      "translation_pair_id": "art-001",
      "blueprint_role": "MAJEUR",
      "parent_major_pair_id": null,
      "fr": { "level": "...", "post_title": "...", "post_name": "...", "post_content": "...", "rank_math_title": "...", "rank_math_description": "...", "wp_category_slug": "..." },
      "en": { ... même structure mais en anglais ... }
    }
  ],
  "validation_metadata": { "expected_pairs_count": 26, ... }
}
```

**Règles strictes au moment de l'import** :
- Polylang doit être actif (sinon refus).
- Slug FR + slug EN uniques dans le batch ET en BDD WP.
- Slug FR ≠ slug EN.
- Levels valides : `pillar`, `sub_pillar`, `major_article`, `satellite` (≥ 1.0.15 ; exige `parent_major_pair_id`), `foundation_article`, `case_study`, `deep_study`, `dataset`, `faq`, `tool`, `beginner`, `uncategorized`. Ni `exclu` ni longueur RankMath ne sont contrôlés à l'import.
- Liens FR pointent vers `https://eco3min.fr/SLUG-FR/`, liens EN vers `https://eco3min.fr/en/SLUG-EN/`. Pas de cross-lang.
- `wp_category_slug` doit exister en BDD WP (résolu via slug).
- `parent_major_pair_id` doit avoir été déclaré AVANT le satellite qui le référence (ordre dans le tableau `articles`).

### 12.6 Workflow opérationnel mega — voir section 14

---

## 10. Conventions de code

Voir `archi-eco3min` section "Conventions de code" — depuis le découpage du 15/09/2026, `references/06-conventions-code-design-tokens.md` — pour le détail (préfixes `Eco3min_Mega_*` / `ECO3MIN_MEGA_*` / `eco3-mega-`, config JS `EcoMegaConfig`, nonce AJAX, sous-menus `eco3min-mega-{clé}`, arborescence réelle, design tokens).

**Spécifique à la suite plugins legacy** :
- Toute table custom : préfixe `eco3min_` (sans le préfixe BDD WP qui est ajouté par `$wpdb->prefix`).
- Toute classe : préfixe `Eco3min_` puis abréviation 2-3 lettres du plugin (`Eco3min_LC_*`, `Eco3min_AD_*`, `Eco3min_RC_*`, etc.).
- Toute constante : préfixe `ECO3MIN_` puis abréviation (`ECO3MIN_LC_VERSION`, `ECO3MIN_AD_TABLE_LOG`, etc.).
- Tout AJAX action : préfixe `eco3min_<plugin>_<action>` + nonce + `manage_options` capability.
- Cron hook : préfixe `eco3min_<plugin>_<action>` (`eco3min_ah_daily_snapshot`, `eco3min_dm_daily_check`).

**Spécifique au mega** :
- Préfixe BDD : `e3m_` (cohabite avec legacy `eco3min_*`).
- Préfixe metas WP : `_eco3min_*` (CONSERVÉ legacy, source de vérité).
- Préfixe AJAX : `eco3min_mega_*` + nonce `eco3min_mega_nonce`.
- Préfixe CSS : `eco3-mega-`.
- Capability : `manage_options` partout.
- Polylang : tous les appels passent par `Eco3min_Mega_Polylang_Bridge::*`, jamais direct.
- WP categories : résolution par slug (pas par term_id) via `Eco3min_Mega_Category_Resolver::resolve($slug)`.

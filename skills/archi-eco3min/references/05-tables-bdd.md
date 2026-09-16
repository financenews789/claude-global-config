# archi-eco3min — référence : Tables BDD du mega (§10)

Réécrit le 15/09/2026 à partir de `eco3min-mega/includes/class-eco3min-mega-installer.php` (mega 1.0.14) et de l'inventaire des tables après nettoyage (`plugins-eco3min` `references/01-inventaire-plugins-actifs.md` §15). Les anciens §10.1 (11 tables legacy) et §10.2 (schéma `eco3min_sa_links`) décrivaient des tables **droppées le 15/09/2026** : supprimés, lignes loggées dans `skills-backups/archi-eco3min.deleted-lines.2026-09-15.md`. §10.4 (exemple, Polylang, requête) est VERBATIM à une phrase près (`translation_group_id` n'est pas un UUID). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

---

## 10. Tables BDD custom

Toutes les tables sont préfixées par le préfixe WordPress du site (`mod441_` dans le cas de Paul) suivi du nom court ci-dessous. Toutes utilisent `dbDelta()` à l'activation (`Eco3min_Mega_Installer::create_tables`, préfixe `$wpdb->prefix . ECO3MIN_MEGA_TABLE_PREFIX` = `…e3m_`).

### 10.1 Tables legacy `eco3min_*` — droppées

`eco3min_sa_links`, `eco3min_lc_suggestions`, `eco3min_ad_log`, `eco3min_ad_backup`, `eco3min_rc_cases`, `eco3min_rc_backup`, `eco3min_ah_snapshots`, `eco3min_dm_health`, `eco3min_gsc_data`, `eco3min_gsc_suggestions`, `eco3min_audit_pillars` (migrée dans `e3m_referentiel` à l'activation du mega) ont été droppées le 15/09/2026 avec leurs plugins. Restent, hors mega, trois tables de backup de plugins actifs : `eco3min_mcp_backups` (Eco3min MCP, `eco3min/rollback`), `eco3min_enm_backup` (EN Mirror Classifier), `eco3min_spa_backup` (Subpillar Aligner). Le préfixe `e3m_` est partagé avec 404-fixer (`e3m_404_log`), Correcteur 301 (`e3m_rlf_log`), Accents Fixer (`e3m_af_*`), Anchor Doctor (`e3m_anchor_*`), Anchor Retarget (`e3m_ar_log`), Patch Audit (`e3m_pae_audited`) : **ne jamais dropper une table `e3m_*` sur la seule foi du préfixe.**

### 10.2 Leçon `src_post_id` (héritée de `eco3min_sa_links`)

Le graphe de liens est `e3m_links`. Ses colonnes s'appellent **`src_post_id`** et **`target_post_id`** — jamais `source_post_id`, `from_post_id` ou `to_post_id`. Le Level Classifier avait une requête sur `source_post_id` qui échouait en silence (son heuristique de `parent_major` par liens sortants ne tournait jamais) : toute requête nouvelle se vérifie contre `SHOW COLUMNS` avant d'être livrée. **Aucun plugin de la suite ne modifie `wp_posts.post_content` sans backup** : le mega écrit dans `e3m_backups` avant chaque patch/import, les autres plugins ont leur propre table (§10.1).

### 10.3 Les 10 tables MEGA (préfixe `e3m_*`)

Cinq tables V0.1 et cinq tables V1.0, créées ensemble par l'installer. Colonnes relevées dans le code le 15/09/2026 (les index sont omis).

| Table | Rôle | Colonnes |
|---|---|---|
| `e3m_referentiel` | Liste figée piliers / sous-piliers / MAJEURs + catégories WP, FR et EN. Seule table modifiable en UI (onglet Référentiel). Migration auto depuis `eco3min_audit_pillars` à l'activation. | `ref_id`, `type` ENUM(pillar, sub_pillar, major_article), `slug`, `lang` ENUM(fr, en), `parent_slug`, `parent_lang`, `cluster_slug`, `display_label`, `resolved_post_id`, `wp_category_slug`, `wp_category_id` (résolu par slug, pas par term_id), `is_active`, `created_at`, `updated_at` — clé unique `(slug, lang)` |
| `e3m_articles` | **Miroir** des articles WP avec metas Eco3min + métriques + état. Source de vérité = les metas WP (SKILL.md §3.2) ; le scanner y fait un UPSERT « métriques only », jamais level/cluster/sub_pilier/parent_major depuis ici. | `post_id` (PK), `slug`, `lang`, `level` VARCHAR(40), `cluster_slug`, `sub_pilier_slug`, `parent_major_post_id`, `translation_group_id` BIGINT, `word_count`, `outgoing_internal_count`, `incoming_internal_count`, `state` ENUM(created, meshed_internal, exported, patched_inbound, done, dirty), `state_color` ENUM(green, orange, red), `last_scan_at`, `post_modified`, `needs_rescan` |
| `e3m_links` | Graphe des liens internes peuplé par le scanner (remplace `eco3min_sa_links`, droppée). | `link_id`, `src_post_id`, `target_post_id` (NULL si non résolu), `target_url` (2048), `target_url_path`, `anchor_text`, `location` ENUM(content, menu, footer, widget), `is_internal`, `is_cross_lang` (1 si FR → EN ou inverse = à corriger), `scanned_at` |
| `e3m_patches_log` | Log des patches appliqués, anti-doublon par hash SHA256. | `patch_id`, `batch_id`, `post_id`, `patch_hash` CHAR(64) unique, `anchor_before_excerpt`, `target_url`, `applied_at`, `status` ENUM(applied, skipped, failed, rolled_back), `rejection_reason`, `comment` |
| `e3m_backups` | `post_content` avant chaque modification ; rollback par `backup_id` ou par `trigger_ref` (batch entier). Vidée le 15/09/2026, se remplit à chaque apply/import. | `backup_id`, `post_id`, `trigger_action` ENUM(patches_apply, cluster_import, manual_edit, anchor_diversify, redundant_clean), `trigger_ref`, `post_content_backup` LONGTEXT, `post_modified_at`, `created_at`, `rolled_back_at` |
| `e3m_qa_clusters` | Pages Q&A structurelles (0 ligne au 15/09). | `qa_id`, `post_id` unique, `qa_cluster_slug`, `qa_cluster_type` ENUM(pillar, satellite), `qa_translation_group_id`, `qa_lang` |
| `e3m_scan_state` | Historique des scans (un enregistrement par scan). | `scan_id`, `scan_started_at`, `scan_finished_at`, `total_posts`, `total_links`, `scan_duration_seconds`, `scan_trigger` ENUM(manual, cron, post_save, cluster_import, patches_apply), `scan_scope` ENUM(all, cluster, single_post), `scan_scope_value`, `errors_count` |
| `e3m_imports_log` | Historique des imports cluster et patches (rapport JSON inclus). | `import_id`, `import_type` ENUM(cluster, patches), `filename`, `json_hash`, `total_items`, `applied_items`, `skipped_items`, `failed_items`, `imported_by`, `imported_at`, `report` LONGTEXT |
| `e3m_tinder_queue` | Queue des articles à classifier dans le Tinder (metas vides uniquement). | `queue_id`, `post_id`, `priority` (1 si aucun level), `reason` ENUM(new_post, no_level, no_cluster, no_sub_pilier, no_parent_major), `added_at`, `resolved_at`, `resolved_by` — clé unique `(post_id, reason)` |
| `e3m_multi_import_sessions` | Sessions d'import multi-pair (V1.0.3), 1 session = N fichiers `pair-*.json` d'un même cluster ; `cross_cluster_*` depuis V1.0.10. Route non retenue depuis le batch unique (cf `plugins-eco3min`). | `session_id`, `session_uid` unique, `cluster_label`, `status` ENUM(pending, running, paused, completed, failed), `total_pairs`, `processed_pairs`, `created_pairs`, `skipped_pairs`, `failed_pairs`, `cluster_metadata_json`, `items_json`, `error_log`, `cross_cluster_export_filename`, `cross_cluster_targets_count`, `created_by`, `created_at`, `updated_at`, `completed_at`, `import_log_id` |

Volumes au 15/09/2026 : `e3m_referentiel` 220, `e3m_articles` 3011, `e3m_links` 39 664, `e3m_patches_log` 7963, `e3m_imports_log` 571, `e3m_scan_state` 291, `e3m_tinder_queue` 2775, `e3m_multi_import_sessions` 15.

**État et couleur** (`Eco3min_Mega_State_Machine::compute_state`, seuils `THRESHOLDS`) : `dirty` (rouge) si `needs_rescan` ; `uncategorized` → `created` (rouge) ; `done` (vert) quand `incoming ≥ in` **et** `outgoing ≥ out` — `pillar` in 5 (pas d'outgoing requis), `sub_pillar` 3/5, `major_article` 8/4, `satellite` / `foundation_article` / `deep_study` / `case_study` 1/3, `beginner` 1/2, `dataset` / `faq` / `tool` 1/1 ; `created` (rouge) si 0 entrant et 0 sortant ; sinon `meshed_internal` (orange). `on_post_save` marque l'article `dirty` à chaque enregistrement publié.

Pour les détails opérationnels (scan, dirty flag, rollback, presets SQL), voir `plugins-eco3min` et sa référence 05.

### 10.4 Concept `translation_group_id` (mega)
Identifiant entier (`BIGINT UNSIGNED`) qui lie une paire FR + EN d'articles. Stocké dans `e3m_articles.translation_group_id`. Généré au moment de l'import cluster bilingue (Format C v1.1) par `Eco3min_Mega_Importer_Cluster` via `Eco3min_Mega_DB::generate_translation_group_id()` = `MAX(translation_group_id) + 1` (`class-eco3min-mega-db.php:109`) — ce n'est **pas** un UUID v4, malgré ce que disait la version antérieure de ce skill.

```
Paire #001 :
  - FR post_id 5841, slug "nouveau-cluster-fr",            translation_group_id = 412
  - EN post_id 5842, slug "new-cluster-en",                translation_group_id = 412
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

# plugins-eco3min — référence : Tables BDD, bugs durables, presets SQL (§4, §5, §7)

Extrait de SKILL.md (découpage du 15/09/2026). §4.2, §5.2, §5.7 et les requêtes SQL conservées sont VERBATIM ; §5.5-5.6 ont été reformulés (Site Audit → scan mega) ; §4.1 et l'en-tête de §7 ont été réécrits le 15/09/2026 (Site Audit, Level Classifier, SQL Runner et Pillar Audit n'existent plus), et les bugs #1, #3, #4 — propres à ces plugins — ont été retirés, leurs leçons vivant dans SKILL.md §8 (règles 7, 8, 9). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

---

## 4. Tables BDD custom

### 4.1 Tables LEGACY (préfixe `mod441_eco3min_*`) et tables `e3m_*` hors mega

État après le nettoyage du 15/09/2026 (22 tables vivantes, 19 droppées, `e3m_backups` vidée) dans `references/01-inventaire-plugins-actifs.md` §15. Le préfixe `e3m_` est partagé par le mega et six autres plugins actifs (404-fixer, Redirect fixer, Accents Fixer, Anchor Doctor, Anchor Retarget, Patch Audit) : ne jamais dropper une table `e3m_*` sur la seule foi du préfixe.

### 4.2 Tables MEGA (préfixe `mod441_e3m_*` ou `wp_e3m_*`)

| Table | Rôle | Cohabite avec legacy ? |
|---|---|---|
| `e3m_referentiel` | Liste figée piliers/sub_piliers/MAJEURs + catégories WP (FR + EN). Inclut colonnes `wp_category_slug` et `wp_category_id` (résolus par slug, pas par term_id) | Oui (cohabite avec `eco3min_audit_pillars` jusqu'au drop manuel) |
| `e3m_articles` | Miroir des articles WP avec metas Eco3min + état (`green`/`orange`/`red`) + `translation_group_id` (lie FR ↔ EN) | Pas d'équivalent legacy |
| `e3m_links` | Graphe des liens internes (peuplé par scanner V0.5). Colonnes : `src_post_id`, `target_post_id`, `is_cross_lang` | Doublon avec `eco3min_sa_links` jusqu'à drop V0.5 |
| `e3m_patches_log` | Log des patches appliqués (anti-doublon par hash SHA256) | Pas d'équivalent legacy en BDD chez Paul |
| `e3m_backups` | post_content avant chaque modification (rollback) | Pas d'équivalent legacy |

**Règle** : ne JAMAIS toucher manuellement aux 4 metas critiques `_eco3min_level/_cluster/_sub_pilier/_parent_major` via SQL. Si tu dois absolument modifier une meta, passe par Custom Fields dans l'éditeur WP, ou appelle `Eco3min_Mega_Classifier::set_meta_safe()` en PHP. Voir section 12.4.

**Tables `e3m_*` ajoutées après V0.1** (README du mega) : `e3m_qa_clusters` (Q&A pages structurelles), `e3m_scan_state` (état courant du scan : running/idle, dernier chunk, progress), `e3m_imports_log` (historique des imports cluster + patches ; `e3m_patches_log` y pointe par FK), `e3m_tinder_queue` (queue des articles à classifier via l'UI Tinder), `e3m_multi_import_sessions` (sessions multi-pair V1.0.3+, avec `cross_cluster_export_filename` et `cross_cluster_targets_count` depuis V1.0.10). Colonnes de `e3m_links` : `src_post_id`, `target_post_id`, `target_url`, `anchor_text`, `is_internal`, `is_cross_lang`.

---

## 5. Bugs durables (toujours valables)

### 5.2 BUG #2 — meta `_eco3min_lang` à 0% partout
- **Symptôme** : analyzer Level Classifier ne savait pas router par cluster+lang.
- **Cause** : Polylang stocke la langue en **taxonomie** (`pll_post_lang`), pas en postmeta.
- **Fix Pillar Audit v1.6.1** : bouton de backfill qui lit `pll_get_post_language($id)` et écrit `_eco3min_lang`.
- **Résultat** : 1020 posts mis à jour (603 FR + 417 EN).
- **Note mega** : le mega utilise `Eco3min_Mega_Polylang_Bridge::get_post_language()` qui lit Polylang en source officielle, et écrit `_eco3min_lang` en miroir lors de l'import cluster.

### 5.5 BUG #5 — patch v2 a appliqué seulement 20/45 patches
- **Symptôme** : le scan montrait +20 liens au lieu de +45 attendus.
- **Cause** : skips Claude (cap 5/cible saturait sous la 1re version des règles du projet C) ou rejets plugin (ANCHOR_NOT_FOUND, ANCHOR_COUNT_MISMATCH).
- **Fix** : règles du projet C v2 (cap 18 + variation stricte des ancres), aujourd'hui dans `patches-maillage-eco3min`.
- **Vérification** : toujours lire les compteurs appliqués / skipped / failed du rapport d'apply, puis comparer les liens entrants (`eco3min/links mode=inbound` ou `e3m_links`) avant/après re-scan.

### 5.6 BUG #6 — exports T1 successifs avec 30 posts en commun
- **Symptôme** : doublons apparents entre exports T1 #2 et #3.
- **Cause** : pas de re-scan entre les IMPORTs → le graphe de liens stagne.
- **Fix** : re-scan obligatoire entre chaque cycle ; le mega le force par son bandeau dirty rouge.

### 5.7 BUG #7 — décompte 363 vs 50 vs 150 incohérent
Les 3 chiffres mesurent des choses différentes :
- **363** = satellites sans `_eco3min_sub_pilier` (peu importe parent_major).
- **50** = satellites avec parent_major mais sans sub_pilier.
- **150** = satellites sans parent_major du tout.
- 363 = 50 + 150 + 163 (mystère : satellites avec `parent_major = '0'` ou string vide, comptés différemment selon la requête).

---

## 7. Presets SQL utiles

Le plugin SQL Runner n'existe plus : exécuter dans la console SQL de l'hébergeur. Pour la plupart des questions, une ability MCP répond sans SQL : `eco3min/links` (entrants, sortants, orphelins, cross-lang — reflète le dernier scan), `eco3min/health` (diagnostic), `eco3min/taxonomy` (arborescence et répartition par level / cluster), `eco3min/find` (`missing[]` pour les non classés).

```sql
-- Satellites sans sub_pilier
SELECT p.ID, p.post_title, pm_level.meta_value as level
FROM mod441_posts p
JOIN mod441_postmeta pm_level ON p.ID = pm_level.post_id AND pm_level.meta_key = '_eco3min_level'
LEFT JOIN mod441_postmeta pm_sp ON p.ID = pm_sp.post_id AND pm_sp.meta_key = '_eco3min_sub_pilier'
WHERE pm_level.meta_value = 'satellite'
  AND p.post_status = 'publish'
  AND (pm_sp.meta_value IS NULL OR pm_sp.meta_value = '');

-- Distribution post_type vs level (utile pour debugger les bugs analyzer)
SELECT p.post_type, pm.meta_value as level, COUNT(*) as n
FROM mod441_posts p
JOIN mod441_postmeta pm ON p.ID = pm.post_id AND pm.meta_key = '_eco3min_level'
WHERE p.post_status = 'publish'
GROUP BY p.post_type, pm.meta_value
ORDER BY n DESC;

-- Compter les liens internes par source (top sources) — graphe du dernier scan mega
SELECT src_post_id, COUNT(*) as n_links
FROM mod441_e3m_links
GROUP BY src_post_id
ORDER BY n_links DESC LIMIT 30;

-- Liens entrants d'un post précis
SELECT src_post_id, anchor_text, COUNT(*) as occurrences
FROM mod441_e3m_links
WHERE target_post_id = ?
GROUP BY src_post_id, anchor_text
ORDER BY occurrences DESC;

-- Articles importés via le mega (état)
SELECT post_id, slug, lang, level, cluster_slug, state, state_color
FROM mod441_e3m_articles
ORDER BY post_id DESC LIMIT 60;

-- Patches mega appliqués sur un post
SELECT * FROM mod441_e3m_patches_log
WHERE post_id = ? ORDER BY applied_at DESC;

-- Backups mega récents
SELECT backup_id, post_id, trigger_action, trigger_ref, created_at, rolled_back_at
FROM mod441_e3m_backups
ORDER BY created_at DESC LIMIT 50;

-- Référentiel mega : entrées sans wp_category_id résolu
SELECT * FROM mod441_e3m_referentiel
WHERE wp_category_slug IS NOT NULL AND wp_category_id IS NULL;

-- Paires bilingues importées (FR + EN liées par translation_group_id)
SELECT a1.post_id as fr_id, a1.slug as fr_slug,
       a2.post_id as en_id, a2.slug as en_slug,
       a1.cluster_slug, a1.level
FROM mod441_e3m_articles a1
JOIN mod441_e3m_articles a2
  ON a1.translation_group_id = a2.translation_group_id
  AND a1.lang = 'fr' AND a2.lang = 'en'
ORDER BY a1.post_id DESC;
```

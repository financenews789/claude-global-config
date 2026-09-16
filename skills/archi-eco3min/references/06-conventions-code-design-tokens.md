# archi-eco3min — référence : Conventions de code des plugins et design tokens (§11, §12)

Réécrit le 15/09/2026 sur le code de `eco3min-mega` 1.0.14 (`eco3min-mega.php`, `includes/admin/class-eco3min-mega-admin-menu.php`, `class-eco3min-mega-admin.php`, `assets/css/admin.css`). L'ancien §11.1 (préfixes de neuf plugins legacy), l'arborescence « plugin legacy » de §11.4 et les exemples `ECO3MIN_LC_` / `EcoLCConfig` / `.eco3-lc-` / `.e3hub-wrap` de §11.3-11.6 décrivaient des plugins désinstallés : supprimés, lignes loggées dans `skills-backups/archi-eco3min.deleted-lines.2026-09-15.md`. Les « Règles non-négociables du mega » et les tokens de §12 sont VERBATIM. Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

---

## 11. Conventions de code des plugins

### 11.1 Plugins actifs hors mega

Les préfixes, nonces et slugs de menu des plugins legacy (Site Audit, Level Classifier, Anchor Diversifier, Redundant Cleaner, Anchor Health, Dataset Monitor, GSC Linker, Performance Dashboard, Hub, Maillage Audit, Maillage Cluster) n'ont plus d'objet : ces plugins sont désinstallés. Pour les 27 plugins actifs (version, rôle, URL wp-admin lue dans `add_menu_page` / `add_management_page`), la table de référence est `plugins-eco3min` SKILL.md §1.1 — ne pas la dupliquer ici. Deux slugs souvent demandés : Q&A Importer v2 = `tools.php?page=eco3min-qa-import`, Translator Bridge = `tools.php?page=eco3min-translator`.

Convention commune à tous les plugins maison, vérifiée dans le dépôt : en-tête `Plugin Name: Eco3min …` (ou nom français explicite), préfixe de classes `Eco3min_*` ou `E3M_*`, préfixe CSS `eco3-` (jamais une classe nue qui casserait Blocksy ou le wp-admin), tables via `$wpdb->prefix`, capability `manage_options`, nonce propre au plugin (`eco3min_<abrégé>_nonce`).

### 11.2 Préfixes du mega-plugin

Constantes définies dans `eco3min-mega.php:49-74` ; rien d'autre n'est inventé.

| Élément | Préfixe / convention |
|---|---|
| Tables BDD | `e3m_` — `ECO3MIN_MEGA_TABLE_PREFIX` (ex. `e3m_articles`, `e3m_links`) |
| Constantes PHP | `ECO3MIN_MEGA_*` : `_VERSION` (`1.0.14`), `_FILE`, `_PATH`, `_URL`, `_TEXTDOMAIN` (`eco3min-mega`), `_TABLE_PREFIX`, `_AJAX_PREFIX`, `_CSS_PREFIX`, `_CAPABILITY`, `_EXPORT_CHUNK_SIZE` (100), `_FORMAT_C_MIN_VERSION` (`1.1.0`) ; plus `ECO3MIN_META_PREFIX = '_eco3min_'` et, pour le maillage ultime, `ECO3MIN_MU_CAP` / `ECO3MIN_MU_VERSION` (alias) |
| Classes PHP | `Eco3min_Mega_*` (ex. `Eco3min_Mega_Classifier`, `Eco3min_Mega_Polylang_Bridge`, `Eco3min_Mega_Tab_4_Maillage`) ; `Eco3min_MU_*` pour les quatre classes maillage ultime (`Advisor`, `Analyzer`, `Doctor`, `Reconcile`) ; `Eco3min_Mega_Immutability_Exception` |
| Config JS | **une seule** : `EcoMegaConfig = { ajax_url, nonce }`, injectée par `wp_localize_script('jquery', …)` (`class-eco3min-mega-admin.php:115`). Pas de config par onglet ; le JS des onglets est inline dans les classes `Tab_N` (`assets/js/` ne contient qu'un `.keep`) |
| Nonce AJAX | `eco3min_mega_nonce` — `check_ajax_referer('eco3min_mega_nonce', 'nonce')` puis `current_user_can(ECO3MIN_MEGA_CAPABILITY)` dans chaque handler |
| Action AJAX | `eco3min_mega_*` (`ECO3MIN_MEGA_AJAX_PREFIX`, ex. `eco3min_mega_validate_cluster`) |
| Cron hook | `eco3min_mega_daily_scan` (planifié `daily` à l'activation) ; hook applicatif `eco3min_mega_after_patches_applied` (state machine) |
| Menu slug admin | `eco3min-mega` (top-level, `dashicons-admin-network`, position 58) ; sous-menus `eco3min-mega-` + clé d'onglet : `referentiel`, `scan`, `import_cluster`, `maillage`, `graph`, `manuel`, `diagnostic`, `conseil`, `nettoyeur` (`Eco3min_Mega_Admin::TABS`, rendu par `Eco3min_Mega_Admin_Menu::register_menu`). **Pas** de `eco3min-mega-tab-1` |
| Préfixe CSS | `eco3-mega-` (`ECO3MIN_MEGA_CSS_PREFIX`, ex. `.eco3-mega-wrap`, `.eco3-mega-card`) ; `.eco3-doc__*` pour le Diagnostic (maillage ultime) |
| Capability | `manage_options` partout (`ECO3MIN_MEGA_CAPABILITY`) |
| Metas WP | **`_eco3min_*`** CONSERVÉ legacy (jamais `_e3m_*`). Les metas WP sont la source unique de vérité, voir SKILL.md §3.2 ; metas protégées = `Eco3min_Mega_Classifier::PROTECTED_METAS` (`_eco3min_level`, `_eco3min_cluster`, `_eco3min_sub_pilier`, `_eco3min_parent_major`) |

**Règles non-négociables du mega** :
- Tous les appels Polylang passent par `Eco3min_Mega_Polylang_Bridge::*`, jamais direct.
- Tous les writes sur metas critiques passent par `Eco3min_Mega_Classifier::set_meta_safe()`.
- Toute résolution de catégorie WP se fait par slug via `Eco3min_Mega_Category_Resolver::resolve($slug)` (jamais par term_id hardcodé).

### 11.3 Conventions PHP

```php
// Check ABSPATH systématique en haut de chaque fichier inclus
if ( ! defined( 'ABSPATH' ) ) { exit; }

// Constantes définies dans le entry point (eco3min-mega.php)
define( 'ECO3MIN_MEGA_VERSION',      '1.0.14' );
define( 'ECO3MIN_MEGA_PATH',         plugin_dir_path( __FILE__ ) );
define( 'ECO3MIN_MEGA_TABLE_PREFIX', 'e3m_' );
define( 'ECO3MIN_META_PREFIX',       '_eco3min_' );

// Tables avec $wpdb->prefix pour tenir compte du préfixe site (mod441_)
$table = $wpdb->prefix . ECO3MIN_MEGA_TABLE_PREFIX . 'articles';   // ou Eco3min_Mega_DB::table('articles')

// Headers plugin obligatoires
/**
 * Plugin Name: Eco3min XYZ          ← toujours commence par "Eco3min "
 * Version: X.Y.Z
 * Author: Paul / Eco3min
 */

// Nonces AJAX systématiques + capability check
check_ajax_referer( 'eco3min_mega_nonce', 'nonce' );
if ( ! current_user_can( ECO3MIN_MEGA_CAPABILITY ) ) {
    wp_send_json_error( [ 'message' => 'Permission denied' ] );
}

// Chunks AJAX ≤ 50 posts pour éviter timeouts (scan : limit 50 par requête ; export CSV : 5000 lignes par fetch côté SQL)
```

### 11.4 Architecture fichiers du mega-plugin (état réel 1.0.14)

```
eco3min-mega/
├── eco3min-mega.php                  (constantes, require_once dans l'ordre helpers → db → installer → core → admin → maillage-ultime, hooks cron)
├── README.md · readme.txt · uninstall.php
├── includes/
│   ├── class-eco3min-mega-db.php           (accès tables, generate_translation_group_id, enqueue_tinder, mark_dirty)
│   ├── class-eco3min-mega-installer.php    (création des 10 tables e3m_*, migration eco3min_audit_pillars, cron)
│   ├── helpers/
│   │   ├── class-eco3min-mega-logger.php
│   │   ├── class-eco3min-mega-category-resolver.php   (résolution slug → term_id)
│   │   ├── class-eco3min-mega-polylang-bridge.php     (encapsulation Polylang : get_post_language, save_translations)
│   │   ├── class-eco3min-mega-validator.php           (VALID_LEVELS, validation Format C v1.1, patches v1.0.2)
│   │   ├── class-eco3min-mega-backup.php
│   │   ├── class-eco3min-mega-scan-dirty.php          (bandeau rouge « index obsolète »)
│   │   ├── class-eco3min-mega-upload-helper.php       (drag & drop, 10 Mo)
│   │   └── class-eco3min-mega-csv.php
│   ├── core/
│   │   ├── class-eco3min-mega-classifier.php          (set_meta_safe + garde-fou immutabilité, PROTECTED_METAS)
│   │   ├── class-eco3min-mega-importer-cluster.php    (Format C v1.1 bilingue, batch unique)
│   │   ├── class-eco3min-mega-importer-multi-pair.php (sessions multi-pair, route non retenue)
│   │   ├── class-eco3min-mega-importer-patches.php    (patches v1.0.2, chunked)
│   │   ├── class-eco3min-mega-scanner.php             (e3m_links, e3m_articles métriques, suggest_classification, auto_enqueue_tinder)
│   │   ├── class-eco3min-mega-state-machine.php       (THRESHOLDS, compute_state, on_post_save)
│   │   ├── class-eco3min-mega-exporter-full.php       (Format AVEC HTML)
│   │   ├── class-eco3min-mega-exporter-avec-html.php  (export manuel « targets manual »)
│   │   ├── class-eco3min-mega-exporter-snapshot.php   (snapshot JSON — colonne url reconstruite à plat, cf §2.1)
│   │   ├── class-eco3min-mega-exporter-maillage-csv.php (snapshot.csv + maillage.csv, 1.0.14)
│   │   ├── class-eco3min-mega-anchor-diversifier.php
│   │   └── class-eco3min-mega-redundant-cleaner.php
│   ├── admin/
│   │   ├── class-eco3min-mega-admin.php               (TABS, enqueue CSS, EcoMegaConfig, notices Polylang)
│   │   ├── class-eco3min-mega-admin-menu.php          (menu + sous-menus eco3min-mega-{clé})
│   │   ├── class-eco3min-mega-tab-1-referentiel.php
│   │   ├── class-eco3min-mega-tab-2-scan.php          (scanner + Tinder ; écrit le SLUG _eco3min_sub_pilier, l.467)
│   │   ├── class-eco3min-mega-tab-3-import-cluster.php
│   │   ├── class-eco3min-mega-tab-4-maillage.php
│   │   ├── class-eco3min-mega-tab-5-graph.php
│   │   ├── class-eco3min-mega-tab-6-manuel.php
│   │   ├── class-eco3min-mega-tab-7-diagnostic.php
│   │   ├── class-eco3min-mega-tab-8-conseil.php
│   │   └── class-eco3min-mega-tab-9-nettoyeur.php     (Réconciliation)
│   └── maillage-ultime/
│       ├── class-eco3min-mu-analyzer.php              (T1/T2/T3 ; 4 levels maillés, ignore les articles sans cluster)
│       ├── class-eco3min-mu-advisor.php
│       ├── class-eco3min-mu-doctor.php                (Diagnostic ; tokens dark inline l.397)
│       └── class-eco3min-mu-reconcile.php
└── assets/
    ├── css/admin.css             (préfixe .eco3-mega-, 395 lignes)
    └── js/.keep                  (le JS vit inline dans les onglets)
```

Les autres plugins maison sont mono-fichier (`eco3min-<slug>/eco3min-<slug>.php`) ou `includes/` + `assets/` selon la même logique ; aucun n'est un « plugin legacy » au sens de l'ancienne arborescence `class-installer / class-applier / class-tree`.

### 11.5 Conventions CSS

```css
/* TOUTES les classes plugin préfixées eco3- pour éviter conflits Blocksy et wp-admin */
.eco3-mega-wrap { ... }
.eco3-mega-card { ... }
.eco3-mega-state-badge--green { ... }

/* !important parfois nécessaire pour override les styles wp-admin / Blocksy (admin.css l.194-210) */
.eco3-mega-future {
    background: #fffbeb !important;
    border-color: #fde68a !important;
}

/* Diagnostic (maillage ultime) : tout est scopé sous .eco3-doc, variables déclarées dans ce scope */
.eco3-doc__card h2 { color: var(--gold); }   /* OK */
h2 { ... }                                    /* INTERDIT, casserait le WP admin */
```

### 11.6 Conventions JS

```js
(function ($) {
    'use strict';
    // Config injectée par PHP via wp_localize_script('jquery', 'EcoMegaConfig', …)
    // EcoMegaConfig = { ajax_url, nonce };

    $.post(EcoMegaConfig.ajax_url, {
        action: 'eco3min_mega_scan_chunk',
        nonce: EcoMegaConfig.nonce,
        offset: 0,
        limit: 50
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

> Note du 15/09/2026 : le plugin Hub (`eco3min-hub/assets/css/admin.css`) est désinstallé. Ces tokens survivent tels quels, déclarés inline, dans le Diagnostic du mega (`includes/maillage-ultime/class-eco3min-mu-doctor.php:397` : `--tx`, `--dim`, `--muted`, `--gold`, `--green`, `--red`, `--orange`) et restent la palette à réutiliser pour toute UI admin dark Eco3min. Ne pas les confondre avec le brand kit du site public (`brand-kit-eco3min`).

**Couleurs d'état mega** : `e3m_articles.state_color` prend trois valeurs alignées avec ces tokens — `green` (`done` : seuils entrants/sortants atteints), `orange` (`meshed_internal`, `exported`, `patched_inbound` : maillage à compléter), `red` (`created` sans aucun lien, `uncategorized`, ou `dirty` à re-scanner). Seuils par level dans `references/05-tables-bdd.md` (§10.3, `Eco3min_Mega_State_Machine::THRESHOLDS`).

---
name: plugins-eco3min
description: Référence opérationnelle de la suite WordPress Eco3min — ÉTAT FIGÉ juin 2026. Cœur = mega-plugin v1.0.13.1 : classification Tinder + conseil de maillage T1/T2/T3 + onglets Maillage Ultime fusionnés (Diagnostic/Conseil/Réconciliation). PRÉ-REQUIS du conseil = plugin Cleanup v1.0.1 : exclut le bruit, rattache les satellites orphelins (export→Claude→import cluster+sous-pilier ; l'import NE pose PAS le level — cf §14.8), déclare les hubs en pilier — réversible. Level Classifier v1.5.1 OBSOLÈTE SAUF la classification (inférer le level des uncategorized). Site Audit, Maillage Cluster/Audit, Anchor Diversifier, Redundant Cleaner et les backfills one-shot sont OBSOLÈTES. Couvre le workflow canonique (classer→cleanup→scan mega→conseil), le conseil ne maille QUE 4 niveaux (pillar/sub_pillar/major_article/satellite), tables e3m_*, format patches v1.0.2, Format C v1.1, projets Claude A/B/C, bugs, règles d'opération. Structure éditoriale (silos, levels, metas) → archi-eco3min.
---

# Suite de plugins Eco3min — référence opérationnelle

> Ce skill code en dur **comment fonctionne la suite de plugins WordPress Eco3min**, le **mega-plugin** qui absorbe 6 d'entre eux, et les **3 projets Claude** qui orchestrent le pipeline éditorial bilingue.
>
> Pour la structure éditoriale du site (silos, piliers, levels, metas WP), voir `archi-eco3min`. Pour la rédaction (style, AMF), voir `editeur-eco3min`.

---

## 1. Vue d'ensemble — ÉTAT FIGÉ (consolidation juin 2026)

> **⚠️ Cet inventaire reflète l'état RÉEL ET FIGÉ après la consolidation de juin 2026.**
> Toute la chaîne de maillage a été absorbée par le **mega-plugin**. Le **conseil de maillage T1/T2/T3 se fait UNIQUEMENT dans le mega**, après un passage **obligatoire** par le plugin **Cleanup**. Tout ce qui est marqué OBSOLÈTE doit être désactivé. Le Level Classifier n'est plus conservé que pour **une seule** fonction (voir 1.2).

### 1.1 Plugins ACTIFS

| Plugin | Version | Rôle | post_content |
|---|---|---|---|
| **Eco3min Mega** | **1.0.13.1** | **Cœur du système.** Onglets : 🃏 Classification (Tinder set/get du level), 🧭 **Conseil de maillage T1/T2/T3** (lit `e3m_links`), + 3 onglets *Maillage Ultime* fusionnés (juin 2026) : 🩺 Diagnostic / 🧭 Conseil / 🧹 Réconciliation. Onglet patches (import des patches.json). Lit/écrit les tables `e3m_*`. | via patches (backup) |
| **Eco3min Cleanup** | **1.0.1** | **PRÉ-REQUIS du conseil.** 3 sections, tout réversible (backup avant écriture, jamais d'écrasement) : (1) **exclut le bruit** (pages système → `level=exclu`) ; (2) **rattache les satellites orphelins** (export JSON → révision par Claude → import `{attachments:[{post_id,cluster,sub_pilier,parent_major?}]}` qui écrit `_eco3min_cluster` + `_eco3min_sub_pilier` (+ `parent_major`) — **PAS `_eco3min_level`** : le contrat d'import v1.0.1 n'a aucun champ level ; le level n'est posé que par (1) exclu et (3) hubs, vers des valeurs fixes. Promotion en `major_article` → cf §14.8) ; (3) **déclare les hubs** (page 1 segment + enfants) en pilier. URL : `/wp-admin/tools.php?page=eco3min-cleanup`. | non (metas only) |
| **Translator Bridge** | 1.1.0 | Traduction EN (écrit le post_content EN). | post_content EN |
| **GSC Linker** | 1.2.0 | Google Search Console. | non |
| **Dataset Monitor** | 1.0.0 | Surveillance datasets (cron daily). | non |
| **Pillar Audit** | 1.6.1 | Audit des pages piliers. | metas only |
| **Hub** | 1.2.0 | Menu / landing (intégré au mega). | non |
| **SQL Runner** | 1.0.1 | Console SQL admin (debug). | non |

### 1.2 Level Classifier (v1.5.1) — statut SPÉCIAL : obsolète SAUF la classification

Le LC **n'est conservé que pour UNE chose : la CLASSIFICATION**, c'est-à-dire **inférer** le `_eco3min_level` des articles `uncategorized` via ses heuristiques (URL, word count, mots-clés du titre, liens entrants). Le mega **ne sait pas** faire cette inférence — son « classifier » est un Tinder manuel set/get. C'est l'unique raison de garder le LC.

**Tout le reste du LC est MORT — ne PAS l'utiliser :**
- ❌ Son onglet **« Audit Maillage / conseil »** lit la table `eco3min_sa_links`, peuplée par **Site Audit** (désormais désactivé). Table vide ou périmée → le conseil du LC **crache des faux positifs** (il croit chaque article isolé et repropose tout le maillage). *Constat de juin 2026 : table vidée → 126 reco fantômes ; table pleine → l'écart avec le mega s'effondre à +1/+2.* **Le conseil se fait dans le mega, point.**
- ❌ Son **backfill par URL** (`class-backfiller.php`) ne déduit le pilier/sous-pilier **que depuis une URL imbriquée** (`/pilier/sous-pilier/article/`). Les satellites à **URL plate** (la majorité du fond) lui échappent structurellement → c'est le **plugin Cleanup** qui les rattache.

### 1.3 Plugins OBSOLÈTES (à désactiver / désinstaller)

| Plugin | Pourquoi obsolète |
|---|---|
| **Site Audit** (1.0.x) | Sa table `eco3min_sa_links` ne servait qu'au conseil du LC (abandonné). **Table morte.** Le désactiver = un point de scan en moins. |
| **Maillage Cluster** (1.0.2) | Absorbé dans le mega (application des patches). |
| **Maillage Audit** (0.3.0) | Absorbé (référentiel mega). |
| **Anchor Diversifier** (1.0.0) | Absorbé dans le mega. |
| **Redundant Cleaner** (1.0.0) | Absorbé dans le mega. |
| **Performance Dashboard**, **Anchor Health**, **Meta Monitor** | Zappés (jamais intégrés). |
| **LC v1.4.1 / v1.5.0** | Remplacés par v1.5.1. |
| **Sub-pilier Backfill** (1.4.0), **Major-EN Backfill** (1.6.0), **Classify Backfill** (1.0.0) | Backfills one-shot. **Ne plus relancer pour écrire l'ID de sous-pilier** : c'est ce qui avait créé le split-brain `_eco3min_sub_pilier` (slug) vs `_eco3min_subpillar` (ID) — voir `archi-eco3min`. |

### 1.4 WORKFLOW CANONIQUE du conseil de maillage (l'ordre compte)

> **Réflexe figé.** Avant de lire le conseil T1/T2/T3 du mega, il faut que les articles soient **classés ET rattachés**. Sinon le conseil est partiel : il **ignore tout article sans `_eco3min_cluster`** (`if empty(cluster) return`), et il ne maille **que 4 niveaux** : `pillar`, `sub_pillar`, `major_article`, `satellite` (ligne ~352 de l'analyzer). FAQ, dataset, study, tool, beginner sont **ignorés** par le conseil.

1. **Classer** les `uncategorized` → Level Classifier (Tinder/heuristiques) ou Tinder mega.
2. **Cleanup** (`/wp-admin/tools.php?page=eco3min-cleanup`) :
   - Section 1 : marquer le bruit en `exclu`.
   - Section 3 : déclarer les hubs en pilier.
   - Section 2 : **Exporter le JSON → le donner à Claude → réimporter le JSON renvoyé** (écrit cluster + sous-pilier + level). *Voir le prompt de relance dans l'onglet Conseil du mega.*
3. **Scanner** le site dans le mega (remplit `e3m_links`, frais).
4. **Onglet Conseil** du mega → T1/T2/T3.

**Le conseil de rattachement Cleanup côté Claude (ce que fait le prompt) :** sépare les 4 niveaux maillés du reste ; pour satellites/major, valide cluster+sous-pilier suggérés (heuristique des liens) **avec contrôle de langue** (un `/en/` ne va jamais sur un pilier FR) ; re-classe les **études** (`deep_study`/`case_study`/`foundation_article`) en `major_article` + cluster ; écarte les **pages fonctionnelles** (dashboard régime, hubs Macro Watch/Observatoire, méthodo, archives baromètre, datasets, simulateurs) vers `exclu`/`dataset`/`tool` ; signale les **bloqués** (satellites dont ni le titre ni les liens ne portent le sous-pilier — non automatisables sans le contenu).

### 1.5 Mega + 3 projets Claude (production éditoriale)

**3 projets Claude associés** (voir section 13) :
- **A. Architect** — blueprint bilingue d'un cluster.
- **B. Writer** — paires d'articles FR + EN au Format C v1.1.
- **C. Patcher** (= projet "Maillage Optimizer" existant) — patches.json à appliquer.

**Externe** : **Q&A Importer** v2 (existant chez Paul).

---

## 2. Pipelines canoniques

**Deux pipelines coexistent** depuis V0.1 du mega : le pipeline legacy (existant, encore valide pour optimisation de clusters existants), et le pipeline mega (nouveau, pour création de clusters bilingues from scratch).

### 2.1 Pipeline LEGACY (optimisation de cluster existant, ce que Paul utilise depuis 2026)

```
1. Site Audit          → scan complet AJAX (~30-60s pour 1020 posts)
                         peuple eco3min_sa_links

2. Level Classifier    → Onglet Backfill (pilier+sub_pilier)
                         puis Onglet Tinder (UI clavier Y/Enter/S/Esc)
                         écrit _eco3min_level / _cluster / _sub_pilier / _parent_major

3. Level Classifier    → Onglet Audit Maillage (analyzer)
   (analyzer)            export JSON optimisations T1/T2/T3

4. Projet Claude       → input: JSON Level Classifier
   "Maillage Optimizer"  output: patches-{cluster}-{n}.json
   (= projet C Patcher)  Custom Instructions v2 (cap 18 + variation ancres)

5. Maillage Cluster    → Onglet IMPORT
                         upload patches.json via FileZilla d'abord
                         dans /wp-content/uploads/eco3min-maillage/imports/
                         backup auto + apply + statut visuel 🔴🟠🟢

6. Site Audit          → RE-SCAN OBLIGATOIRE
                         sinon eco3min_sa_links stagne et l'analyzer
                         remontera les mêmes missing_links

7. (loop)              → re-export Level Classifier → Claude → import
                         jusqu'à T1=T2=T3=0
```

### 2.2 Pipeline MEGA (création nouveau cluster bilingue, V0.1+)

```
A. Toi → Projet Claude "A. ARCHITECT"
        Input : pillar/sub_pilier FR + EN, question centrale, volume
        Output : blueprint_cluster.md bilingue
                 (1 paire MAJEUR + N paires satellites avec slugs FR/EN,
                  meta titles, titres, intentions, maillage tissé)

B. Toi → Projet Claude "B. WRITER"
        Input : blueprint bilingue
        Output : N JSONs Format C v1.1 (1 par paire FR + EN)
                 Workflow tour par tour : "Démarre avec la paire 1" → JSON →
                 "OK suivant" → JSON → ... jusqu'à fin du blueprint.

C. Mega → Onglet 3 "Import cluster"
         Upload des JSONs via FileZilla dans /uploads/eco3min-mega/imports/
         Validate (dry run) → Apply
         Le mega crée 2 posts WP par paire (FR + EN), set catégories WP
         différentes par lang, câble Polylang auto, archive le JSON en .applied

D. Mega → Onglet 4 "Export pour Patcher" (V0.5+)
         Format LIGHT (Format B), scope=new_posts:[ids des nouveaux posts]
         Télécharge le JSON vers projet C

E. Toi → Projet Claude "C. PATCHER" (= projet Maillage Optimizer existant)
        Génère patches-{cluster}-{n}.json

F. Mega → Onglet 4 "Import patches"
         Upload + validate + apply (= absorbe Maillage Cluster v1.0.2)

G. Mega → re-scan auto (V0.5+) ou re-scan Site Audit manuel (V0.1)
```

### 2.3 Pipeline MEGA — Optimisation site complet (Cas C bis, V0.5+)

```
Mega → Onglet 4 → Export LIGHT (Format B), scope=all, tier=T1 only
       Mode chunked auto : ZIP de N fichiers de max 100 optims chacun

Pour chaque chunk :
  Toi → Projet C Patcher → patches-chunk-N.json
  Toi → Mega → Import patches → Apply

Recommandation : commencer tier=T1, observer qualité, puis T2, puis T3.
```

**En continu / parallèle** (legacy) :
- Anchor Health : cron daily snapshot (alerte si ancre saturée).
- Dataset Monitor : cron daily check fraîcheur datasets.
- Performance Dashboard : consultation à la demande (roadmap).
- GSC Linker : cycle hebdo CSV import → suggestions cibles.

**Correction post-patch (si saturation détectée)** (legacy) :
- Anchor Diversifier : diversifier les ancres sur-utilisées.
- Redundant Cleaner : enlever les liens 3+ vers même cible.
- Migration mega V1.0 : ces 2 outils seront absorbés.

---

## 3. Rôle détaillé de chaque plugin legacy

### 3.1 Foundation (sans modif de post_content)

#### Site Audit (v1.0.0)
- **Rôle** : la source de vérité des liens internes du site.
- **Ce qu'il fait** : parcourt tous les posts publiés en AJAX par chunks, extrait chaque `<a href>` interne, peuple la table `eco3min_sa_links`.
- **Colonnes table** : `src_post_id`, `target_post_id`, `target_url`, `anchor_text`, etc. ⚠ Ce ne sont PAS `from_post_id`/`to_post_id` (erreur classique).
- **Quand le relancer** : après chaque IMPORT de patches Maillage Cluster, sinon le cache stagne.
- **Status mega** : sera absorbé en V0.5 (`Eco3min_Mega_Scanner`, lecture seule sur metas, garde-fou).

#### Maillage Audit (v0.3.0)
- **Rôle** : ancêtre partiellement supplanté par Site Audit. Garde le rôle "Référentiel piliers/clusters" (table de correspondance des 267 pages structurelles).
- **Onglets** : Référentiel / Import / À classifier / Scanner / Export / Cross-Lang / Stats.
- **Status mega** : la table `eco3min_audit_pillars` est migrée en `e3m_referentiel` à l'activation du mega (one-shot, idempotent). Le rôle Référentiel passe à l'onglet 1 du mega.

#### Level Classifier (v1.5.1)
- **Rôle** : classifier les posts dans la hiérarchie Eco3min via heuristiques (URL, word count, keywords titre, liens entrants).
- **UI Tinder** : raccourcis clavier Y/Enter pour accepter, S/Esc pour skip. Vide ~572 uncategorized en ~30 min.
- **Écrit 4 metas** : `_eco3min_level`, `_eco3min_cluster`, `_eco3min_sub_pilier`, `_eco3min_parent_major`.
- **Onglet Audit Maillage (analyzer, ajouté v1.5.0)** : produit le JSON `optimizations[]` avec les missing_links T1/T2/T3 destiné au projet Claude C Patcher.
- **v1.5.1 fix critique** : analyzer filtre maintenant `post_type IN ('post','page')`.
- **Status mega** : sera absorbé en V0.5 dans l'onglet 2 du mega, AVEC garde-fou immutabilité (ne peut plus écraser une classification existante).

#### Translator Bridge (v1.1.0)
- **Rôle** : pipeline FR→EN. 3 onglets : EXPORT (JSON des FR sans pair EN) / IMPORT (crée posts EN + connecte Polylang + map catégories miroirs) / REWRITE LINKS (convertit liens FR vers EN dans posts EN).
- **Status mega** : conservé séparé. Le mega utilise une logique différente : Format C v1.1 produit FR + EN appariés directement par le projet B Writer, donc Translator Bridge n'est nécessaire que pour les anciens articles FR sans paire EN.

#### Pillar Audit (v1.6.1, hors suite mais critique)
- **Rôle** : utilitaire de backfill metas Eco3min.
- **v1.6.0** : Étape 2 = héritage `_eco3min_sub_pilier` depuis le `parent_major`.
- **v1.6.1** : bouton de backfill `_eco3min_lang` qui lit `pll_get_post_language()` (Polylang stocke la langue en taxonomie, pas en postmeta).
- **Status mega** : conservé séparé. Le mega ne réécrit pas ses fonctionnalités de backfill rétroactif.

#### Meta Monitor (v1.0.0, hors suite officielle)
- **Rôle** : rendre visibles les metas `_eco3min_*` que WordPress masque par défaut.
- **Features** : metabox vert/rouge, colonnes Liste posts, filtres dropdowns, save direct via update_post_meta.
- **Status mega** : conservé séparé. Utile pour debug et édition manuelle.

### 3.2 Production (read-only, génère des suggestions)

#### GSC Linker (v1.2.0)
- **Rôle** : importer un CSV Google Search Console, identifier les top performers parmi les satellites/FAQ/datasets, suggérer des cibles structurelles thématiquement liées.
- **2 outputs** :
  - `gsc-shortlist-XXX.txt` (slugs à coller dans Maillage Cluster).
  - `gsc-suggestions-XXX.json` (knowledge file pour le projet Claude C Patcher).
- **Status mega** : conservé séparé. Pas dans le scope du mega.

### 3.3 Correction (modifie post_content avec backup)

#### Maillage Cluster (v1.0.2)
- **Rôle** : appliquer les patches générés par le projet Claude C Patcher.
- **Workflow** :
  1. Coller liste de slugs → EXPORT batch.json.
  2. Coller batch.json dans projet Claude → patches.json.
  3. Upload patches.json via FileZilla dans `/wp-content/uploads/eco3min-maillage/imports/`.
  4. IMPORT depuis admin → backup auto + apply.
- **Statut** : 🔴 jamais traité / 🟠 exporté / 🟢 patché.
- **Format strict patches** : voir section 6.
- **Status mega** : **absorbé en V0.1** dans l'onglet 4 du mega. Désactiver le legacy une fois confiance acquise. Le mega utilise les mêmes règles strictes (validation triple + backup) mais avec table `e3m_patches_log` (préfixe e3m_).

#### Anchor Diversifier (v1.0.0)
- **Rôle** : find/replace contextuel sur post_content pour diversifier les ancres `<a>` sur-utilisées.
- **Différence avec Maillage Cluster** : ne crée pas de nouveaux liens, modifie le texte d'ancre des liens existants.
- **Input** : `ancres-replacement-plan.json`. Idempotent + backup.
- **Status mega** : sera absorbé en V1.0 dans l'onglet 5.

#### Redundant Cleaner (v1.0.0)
- **Rôle** : détecter les cas où un article cite la même cible 3+ fois (over-linking) et transformer les `<a>` excédentaires en simple texte.
- **Skip auto** : pillars (légitimes structurellement).
- **Status mega** : sera absorbé en V1.0 dans l'onglet 5.

### 3.4 Diagnostic (read-only)

#### Performance Dashboard (v1.0.0)
- **Rôle** : croiser GSC + Site Audit + post_meta pour produire 6 vues prêtes à l'emploi.
- **Vues** : `view_update_opportunities` / `view_under_linked` / `view_zombies` / `view_top_traffic` / tendances cluster / distribution par level.
- **Usage** : ta roadmap éditoriale data-driven.
- **Status mega** : exclu. Décision Paul : zappé.

### 3.5 Monitoring (cron daily)

#### Anchor Health (v1.0.0)
- **Cron hook** : `eco3min_ah_daily_snapshot`.
- **Seuils par défaut** : warning ≥ 8 occurrences vers même cible, critical ≥ 15.
- **Alerte** : automatique au `save_post` si une ancre franchit le seuil.
- ⚠ **Faux positifs connus** : TOC interne des Q&A pages qui résolvent en `/`. À ignorer.
- **Status mega** : exclu. Décision Paul : zappé.

#### Dataset Monitor (v1.0.0)
- **Cron hook** : `eco3min_dm_daily_check`.
- **Détection** : datasets périmés via `post_modified > seuil`.
- **Bouton** : "Trigger refresh" appelle l'endpoint `/wp-json/eco3min/v1/touch-datasets` pour rafraîchir les `dateModified` JSON-LD.
- **Discovery** : auto via `_eco3min_level=dataset` ou présence de shortcodes Eco3min.
- **Status mega** : conservé séparé. Pipeline de datasets distinct.

### 3.6 Meta

#### Hub (v1.2.0)
- **Menu top-level "Eco3min"** dans la sidebar admin.
- **Détecte le statut** (actif/inactif/non installé) de chaque plugin.
- **v1.2.0** : ajout d'un diagramme SVG visuel du pipeline en haut de la page.
- **Status mega** : conservé. À terme deviendra le menu parent du mega.

---

## 4. Tables BDD custom

### 4.1 Tables LEGACY (préfixe `mod441_eco3min_*` ou `wp_eco3min_*`)

| Table | Plugin | Rôle | Status mega |
|---|---|---|---|
| `eco3min_audit_pillars` | Maillage Audit | Référentiel piliers (270 rows) | **Migrée → e3m_referentiel** à l'activation |
| `eco3min_sa_links` | Site Audit | Liens internes scannés. Cols : `src_post_id`, `target_post_id`, `target_url`, `anchor_text` | **Sera dropée** quand mega V0.5 scanne (le mega recrée `e3m_links`) |
| `eco3min_lc_suggestions` | Level Classifier | Propositions Tinder en attente | **Sera dropée** V0.5 (recalculable) |
| `eco3min_gsc_data` | GSC Linker | CSV GSC importé | Conservée (plugin séparé) |
| `eco3min_gsc_suggestions` | GSC Linker | Cibles thématiquement liées | Conservée |
| `eco3min_ad_log` | Anchor Diversifier | Ops appliquées | Conservée jusqu'à V1.0 |
| `eco3min_ad_backup` | Anchor Diversifier | Rollback | Conservée jusqu'à V1.0 |
| `eco3min_rc_cases` | Redundant Cleaner | Cas détectés | Conservée jusqu'à V1.0 |
| `eco3min_rc_backup` | Redundant Cleaner | Rollback | Conservée jusqu'à V1.0 |
| `eco3min_ah_snapshots` | Anchor Health | Historique cron | À dropper (plugin zappé) |
| `eco3min_dm_health` | Dataset Monitor | État fraîcheur datasets | Conservée |
| `eco3min_maillage_*` | Maillage Cluster | (introuvables en BDD chez Paul) | Le mega crée ses propres `e3m_patches_log`/`e3m_backups` |
| `eco3min_clean_findings` | (origine inconnue) | 1169 rows mystère | À investiguer puis drop |

### 4.2 Tables MEGA (préfixe `mod441_e3m_*` ou `wp_e3m_*`)

| Table | Rôle | Cohabite avec legacy ? |
|---|---|---|
| `e3m_referentiel` | Liste figée piliers/sub_piliers/MAJEURs + catégories WP (FR + EN). Inclut colonnes `wp_category_slug` et `wp_category_id` (résolus par slug, pas par term_id) | Oui (cohabite avec `eco3min_audit_pillars` jusqu'au drop manuel) |
| `e3m_articles` | Miroir des articles WP avec metas Eco3min + état (`green`/`orange`/`red`) + `translation_group_id` (lie FR ↔ EN) | Pas d'équivalent legacy |
| `e3m_links` | Graphe des liens internes (peuplé par scanner V0.5). Colonnes : `src_post_id`, `target_post_id`, `is_cross_lang` | Doublon avec `eco3min_sa_links` jusqu'à drop V0.5 |
| `e3m_patches_log` | Log des patches appliqués (anti-doublon par hash SHA256) | Pas d'équivalent legacy en BDD chez Paul |
| `e3m_backups` | post_content avant chaque modification (rollback) | Pas d'équivalent legacy |

**Règle** : ne JAMAIS toucher manuellement aux 4 metas critiques `_eco3min_level/_cluster/_sub_pilier/_parent_major` via SQL. Si tu dois absolument modifier une meta, passe par Custom Fields dans l'éditeur WP, ou appelle `Eco3min_Mega_Classifier::set_meta_safe()` en PHP. Voir section 12.4.

---

## 5. Bugs critiques connus et fixes

### 5.1 BUG #1 — analyzer Level Classifier filtrait `post_type='post'` seulement
- **Symptôme** : T2 = 0 dans l'audit malgré 285+ vrais missing_links T2 en SQL.
- **Cause** : `class-maillage-analyzer.php` filtrait `WHERE p.post_type = 'post'`. Or 90 sub_pillars + 20 pillars + 11 MAJEURs étaient en `post_type='page'`.
- **Fix LC v1.5.1** : `WHERE p.post_status = 'publish' AND p.post_type IN ('post', 'page')`.
- **Impact** : bug silencieux qui aurait pu rester invisible des mois. Toujours vérifier le post_type quand un analyzer remonte 0.

### 5.2 BUG #2 — meta `_eco3min_lang` à 0% partout
- **Symptôme** : analyzer Level Classifier ne savait pas router par cluster+lang.
- **Cause** : Polylang stocke la langue en **taxonomie** (`pll_post_lang`), pas en postmeta.
- **Fix Pillar Audit v1.6.1** : bouton de backfill qui lit `pll_get_post_language($id)` et écrit `_eco3min_lang`.
- **Résultat** : 1020 posts mis à jour (603 FR + 417 EN).
- **Note mega** : le mega utilise `Eco3min_Mega_Polylang_Bridge::get_post_language()` qui lit Polylang en source officielle, et écrit `_eco3min_lang` en miroir lors de l'import cluster.

### 5.3 BUG #3 — meta `_eco3min_*` invisibles dans WP éditeur
- **Symptôme** : impossible de voir/modifier les metas Eco3min dans la zone "Champs personnalisés" standard.
- **Cause** : WordPress masque par défaut toutes les metas préfixées `_underscore`.
- **Fix** : plugin **Meta Monitor v1.0.0** qui ajoute metabox + colonnes Liste posts + filtres.

### 5.4 BUG #4 — colonnes SQL erronées dans presets
- **Symptôme** : `Unknown column 'sa.from_post_id'` dans SQL Runner.
- **Cause** : table `eco3min_sa_links` utilise `src_post_id`/`target_post_id`, pas `from_*`/`to_*`.
- **Fix SQL Runner v1.0.1** : tous les presets corrigés.

### 5.5 BUG #5 — patch v2 a appliqué seulement 20/45 patches
- **Symptôme** : Site Audit montrait +20 liens au lieu de +45 attendus.
- **Cause** : skips Claude (cap 5/cible saturait sous Custom Instructions v1) ou rejets plugin (ANCHOR_NOT_FOUND, ANCHOR_COUNT_MISMATCH).
- **Fix** : Custom Instructions v2 (cap 18 + variation stricte des ancres).
- **Vérification** : toujours comparer le compteur de liens dans Site Audit avant/après IMPORT.

### 5.6 BUG #6 — exports T1 successifs avec 30 posts en commun
- **Symptôme** : doublons apparents entre exports T1 #2 et #3.
- **Cause** : pas de re-scan Site Audit entre les IMPORTs → cache stagne.
- **Fix** : re-scan Site Audit obligatoire entre chaque cycle.

### 5.7 BUG #7 — décompte 363 vs 50 vs 150 incohérent
Les 3 chiffres mesurent des choses différentes :
- **363** = satellites sans `_eco3min_sub_pilier` (peu importe parent_major).
- **50** = satellites avec parent_major mais sans sub_pilier.
- **150** = satellites sans parent_major du tout.
- 363 = 50 + 150 + 163 (mystère : satellites avec `parent_major = '0'` ou string vide, comptés différemment selon la requête).

---

## 6. Format strict des patches Maillage Cluster v1.0.2+

Le plugin Maillage Cluster (et l'onglet 4 du mega) rejette tout patch qui ne respecte pas exactement ce format :

```json
{
  "batch_id": "patches-{cluster_slug}-{n}",
  "generated_at": "2026-05-07T10:30:00+02:00",
  "cluster": "{cluster_slug}",
  "patches": [
    {
      "post_id": 4521,
      "anchor_before": "...",
      "insert_after_anchor": " ...<a href=\"...\">...</a>...",
      "expected_occurrences": 1,
      "comment": "..."
    }
  ]
}
```

**Règles dures** (rejet immédiat sinon) :
- `expected_occurrences` **toujours = 1** (le plugin vérifie que `mb_substr_count($content, $anchor)` = 1).
- `anchor_before` **80-200 chars** (mb_strlen), plain text, **exactement 1 occurrence** dans `source_post_content`.
- Pas de balises HTML dans `anchor_before` (`<a>`, `<strong>`, etc.).
- Pas dans une zone interdite : attribut HTML, `<script>`, `<style>`, `<!-- -->`, shortcode `[...]`, JSON-LD.
- `insert_after_anchor` doit avoir un `<a href>` complet avec URL absolue.
- Cohérence linguistique stricte : un FR ne pointe **jamais** vers `/en/`.

**Règles soft** (Claude doit respecter, sinon le patch est sous-optimal) :
- 12 liens internes max par article après ajout.
- 3 liens max vers le même cluster dans un article.
- 1 lien par paragraphe max.
- Pas de lien dans les 2 premiers paragraphes (sauf vers pillar parent).
- Cap 18 patches/cible par batch (Custom Instructions v2).

**Variation des ancres `<a>...</a>`** (anti-spam SEO) :
- **Le vrai signal SEO suspect = diversité des ancres, pas le nombre de liens.**
- Pour une même cible, varier syntaxiquement, lexicalement, positionnellement, par registre.
- Mots-pivots à varier : étude, analyse, cadre, dynamique, mécanisme, données, observation, etc.
- Sur 21 patches vers même cible : max ~5 fois le même mot-pivot (sinon spam pattern).

---

## 7. Presets SQL utiles (via SQL Runner)

```sql
-- Compter les liens internes par source (top sources)
SELECT src_post_id, COUNT(*) as n_links
FROM mod441_eco3min_sa_links
GROUP BY src_post_id
ORDER BY n_links DESC LIMIT 30;

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

-- Liens entrants d'un post précis
SELECT src_post_id, anchor_text, COUNT(*) as occurrences
FROM mod441_eco3min_sa_links
WHERE target_post_id = ?
GROUP BY src_post_id, anchor_text
ORDER BY occurrences DESC;

-- Posts sans _eco3min_lang (avant fix v1.6.1)
SELECT p.ID, p.post_title
FROM mod441_posts p
LEFT JOIN mod441_postmeta pm ON p.ID = pm.post_id AND pm.meta_key = '_eco3min_lang'
WHERE p.post_status = 'publish' AND p.post_type IN ('post', 'page')
  AND (pm.meta_value IS NULL OR pm.meta_value = '');

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

---

## 8. Règles d'opération non négociables

1. **Re-scan Site Audit obligatoire entre chaque IMPORT** Maillage Cluster (legacy). Sinon `eco3min_sa_links` stagne et l'analyzer Level Classifier remontera les mêmes missing_links. Idem pour le mega : entre 2 imports patches, re-scanner (V0.1 : Site Audit legacy, V0.5+ : scanner du mega).
2. **Renommer l'ancien `patches-{cluster}-{n}.json` en `.applied`** sur FileZilla avant d'uploader le nouveau (évite collision de nom). Le mega le fait automatiquement après apply.
3. **New chat Claude obligatoire entre 2 batches**. Ne jamais réutiliser une conversation pour 2 batches successifs (risque de contamination des règles ancres entre batches).
4. **Toujours lire `source_post_content` avant de générer une `anchor_before`**. La phrase doit exister exactement 1 fois dans le contenu.
5. **Ne jamais inventer un `target_url` ou `target_post_id`** qui ne sont pas dans le JSON reçu.
6. **Cap SEO réel = diversité des ancres, pas le nombre de liens**. 30 liens vers un MAJEUR avec 30 ancres distinctes = OK. 8 liens avec 8 fois la même ancre = pattern.
7. **`post_type IN ('post','page')` partout** dans les requêtes SQL d'analyzer. Sinon les pages structurelles sont invisibles.
8. **Utiliser `pll_get_post_language()`** comme source officielle de la langue (Polylang). Pas la postmeta `_eco3min_lang` qui peut être obsolète.
9. **Toujours vérifier les vrais noms de colonnes** de `eco3min_sa_links` : `src_post_id`/`target_post_id`, pas `from_*`/`to_*`.
10. **Backups** : Maillage Cluster, Anchor Diversifier, Redundant Cleaner ont tous backup auto + rollback. Ne pas hésiter à appliquer puis rollback si besoin. Mega : table `e3m_backups` avec rollback par `backup_id` ou par `trigger_ref` (batch entier).
11. **Mega : NE JAMAIS écrire directement sur `_eco3min_level/_cluster/_sub_pilier/_parent_major`**. Passer par `Eco3min_Mega_Classifier::set_meta_safe()` qui throw `Eco3min_Mega_Immutability_Exception` en cas de tentative d'écrasement. Voir section 12.4.

---

## 9. Diagnostic rapide

Quand quelque chose ne va pas, suivre cet ordre :

1. **L'analyzer remonte 0 missing_links alors qu'on en attend ?**
   → Vérifier `post_type` dans la query SQL. Vérifier `_eco3min_lang` peuplé. Vérifier qu'il y a eu un re-scan Site Audit récent.

2. **Le patch Claude est rejeté par Maillage Cluster (legacy) ou par l'onglet 4 du mega ?**
   → Erreurs typiques : ANCHOR_NOT_FOUND (ancre absente du contenu), ANCHOR_COUNT_MISMATCH (présente plusieurs fois), `expected_occurrences != 1`. Réviser la sélection d'ancre.

3. **Site Audit ne change pas après IMPORT ?**
   → Re-lancer le scan complet. Le cache `eco3min_sa_links` ne se rafraîchit pas tout seul.

4. **Anchor Health crie au scandale avec score 0/100 ?**
   → Probablement faux positifs Q&A TOC. Vérifier la liste des ancres "critical" : si elles correspondent à des fragments `#section`, ignorer.

5. **Site planté ("erreur critique") ?**
   → FileZilla → renommer le dossier du dernier plugin modifié en `_disabled`. WordPress redevient accessible. Diagnostiquer le PHP.

6. **Décompte de satellites incohérent entre 2 endroits ?**
   → Les 3 décomptes (363/150/50) mesurent des sous-ensembles différents. Voir BUG #7. Utiliser SQL Runner pour vérifier directement.

7. **Mega : import cluster bilingue refuse avec "Polylang must be active" ?**
   → Polylang désactivé ou non installé. L'import cluster bilingue de l'onglet 3 nécessite Polylang. Activer d'abord.

8. **Mega : import cluster refuse une paire avec "slug_fr_conflict" ou "slug_en_conflict" ?**
   → Le slug existe déjà en BDD. Soit doublon réel (le post a déjà été importé), soit conflit avec un autre cluster. Vérifier via SQL : `SELECT ID FROM wp_posts WHERE post_name = 'le-slug'`.

9. **Mega : exception `Eco3min_Mega_Immutability_Exception` au runtime ?**
   → Tentative d'écrasement d'une meta classification existante. Logique applicative à revoir : un import cluster ne devrait jamais déclencher ça (posts neufs uniquement). Si ça arrive, vérifier que le post_id n'existait pas déjà avant l'import.

---

## 10. Conventions de code

Voir `archi-eco3min` section "Conventions de code" pour le détail (préfixes `Eco3min_*` / `ECO3MIN_*` / `eco3-`, configs JS `EcoXXConfig`, nonces AJAX, menu slugs admin, design tokens Hub).

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

---

## 11. Quand activer ce skill

Active ce skill quand l'utilisateur :
- Pose une question sur le rôle ou le fonctionnement d'un plugin de la suite legacy ou du mega.
- Décrit un bug ou un comportement bizarre.
- Demande à modifier ou faire évoluer un plugin.
- Lance un cycle de patches (export → Claude C Patcher → import).
- Lance un cycle de création de cluster bilingue (projet A → projet B → import mega → projet C → import mega).
- Mentionne une table `eco3min_*` ou `e3m_*`, une meta `_eco3min_*`, un onglet d'un de ces plugins, un onglet du mega.
- Pose une question SQL sur les liens internes ou les classifications.
- Demande comment utiliser les projets Claude associés (A. Architect / B. Writer / C. Patcher).
- Demande quel pipeline (legacy ou mega) utiliser dans une situation donnée.

Ne pas activer pour :
- Questions de structure éditoriale pure (silos, levels, piliers) → `archi-eco3min`.
- Questions de rédaction (style, AMF) → `editeur-eco3min`.
- Production de pages dataset / Q&A → `production-dataset`, `production-q-and-a`.

---

## 12. Mega-plugin Eco3min (V0.1 MVP, mai 2026)

### 12.1 Vue d'ensemble

Le **mega-plugin Eco3min** unifie 6 plugins legacy en une seule extension WordPress et ajoute 3 modules nouveaux. Il vit en cohabitation avec les plugins legacy : tu peux activer le mega sans désactiver le legacy. Les conflits sont évités par préfixes BDD distincts (`e3m_` vs `eco3min_`) et hooks distincts.

**Versionning** :
- **V0.1 (mai 2026, livré)** — MVP minimal : tables + onglets 1/3/4 + garde-fou immutabilité + Format C v1.1
- **V0.5** — Scan + Tinder UI + Export FULL/LIGHT chunked + state machine + cron daily
- **V1.0** — Graphique Cytoscape.js + Anchor Diversifier + Redundant Cleaner absorbés + drop legacy tables
- **v1.0.13.1 (juin 2026, ACTUEL)** — **Fusion du plugin « Maillage Ultime »** en 3 onglets internes : 🩺 **Diagnostic** (split-brain sous-pilier, cohérence des metas), 🧭 **Conseil** (conseil de maillage T1/T2/T3 read-mostly sur les tables `e3m_*`), 🧹 **Réconciliation** (breadcrumb hybride : lit l'ID `_eco3min_subpillar` si présent, sinon résout le slug `_eco3min_sub_pilier`). Les 4 classes MU vivent dans `includes/maillage-ultime/` avec `require` protégés `if (!class_exists())`. **Piège résolu** : ne JAMAIS laisser le plugin « Maillage Ultime » séparé actif en même temps (collision de redéclaration de classe → écran blanc). Le conseil de l'onglet Conseil lit `wp_e3m_links` (`$wpdb->prefix.'e3m_links'`), rempli par le scan mega.
- **V2.0 (prévu)** — Reclassification UI + WP-CLI + webhooks

> Le **plugin Cleanup** (v1.0.1) est **séparé** du mega (extension à part, menu Outils), pas un onglet. C'est volontaire : c'est un outil one-shot de remise en ordre, exécuté avant le conseil.

### 12.2 Mapping legacy → mega

| Plugin legacy | Absorbé en | Onglet mega | Statut migration |
|---|---|---|---|
| Site Audit | V0.5 | onglet 2 (`Scanner`) | DONT use legacy après V0.5 |
| Maillage Audit | V0.1 | onglet 1 (`Référentiel`) | Référentiel migré auto à activation |
| Maillage Cluster | V0.1 | onglet 4 (`Maillage`) | **Désactiver legacy** une fois V0.1 testé |
| Level Classifier | V0.5 | onglet 2 (`Tinder + Analyzer`) | DONT use legacy après V0.5 |
| Anchor Diversifier | V1.0 | onglet 5 (`Cleanup`) | DONT use legacy après V1.0 |
| Redundant Cleaner | V1.0 | onglet 5 (`Cleanup`) | DONT use legacy après V1.0 |

**Plugins legacy CONSERVÉS** (cohabitent avec le mega indéfiniment) :
- Hub (devient le menu parent du mega à terme)
- Translator Bridge (utile pour articles FR existants sans paire EN)
- GSC Linker (cycle GSC séparé)
- Pillar Audit (backfill rétroactif quand nécessaire)
- Meta Monitor (édition manuelle des metas dans WP éditeur)
- Dataset Monitor (cycle datasets séparé)
- SQL Runner (debug)

**Plugins legacy ZAPPÉS** (à désinstaller) :
- Performance Dashboard (peu utilisé)
- Anchor Health (faux positifs Q&A)

### 12.3 Tables BDD du mega — voir section 4.2

5 tables `e3m_*` créées à l'activation. La table `eco3min_audit_pillars` est migrée vers `e3m_referentiel` automatiquement (idempotent).

### 12.4 Garde-fou immutabilité de la classification

**Principe non-négociable** : le travail Tinder humain de Paul (615 articles classifiés à la main) ne peut jamais être écrasé par le mega.

**5 couches de défense** :

1. **Scan read-only** — Le scanner V0.5 LIT les metas mais n'ÉCRIT JAMAIS dessus.
2. **Queue Tinder filtrée** — Le Tinder V0.5 n'enqueue que les articles avec metas vides.
3. **`set_meta_safe()`** — Toute écriture sur `_eco3min_level/_cluster/_sub_pilier/_parent_major` passe par `Eco3min_Mega_Classifier::set_meta_safe($post_id, $key, $value, $strict=true)`. Throw `Eco3min_Mega_Immutability_Exception` si la meta existe déjà avec une valeur différente. Idempotent si valeur identique.
4. **Import cluster sur posts neufs** — `Eco3min_Mega_Importer_Cluster` crée des posts via `wp_insert_post()` (jamais d'update sur posts existants). Refuse l'import si slug déjà utilisé.
5. **Tests unitaires** (à écrire en V0.5).

**Conséquence pratique** : si tu veux modifier une classification existante, passe par Custom Fields dans l'éditeur WP (ou Meta Monitor). Le mega ne fournit PAS d'UI de reclassification en V0.1-V1.0 (réservé V2.0 avec triple confirmation).

### 12.5 Format C v1.1 bilingue (input de l'onglet 3)

Format JSON consommé par l'onglet 3 du mega. Produit par le **projet B Writer**. Chaque entrée `articles[]` contient une paire FR + EN appariée (sous-objets imbriqués). **Le JSON importable est le batch unique du cluster** (toutes les paires en `articles[]`, stratégie A — l'import paire par paire est obsolète : `parent_major_pair_id` n'est résolu qu'intra-batch) ; `expected_pairs_count` (dans `validation_metadata`) doit égaler `len(articles)`.

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
- Levels valides : `pillar`, `sub_pillar`, `major_article`, `foundation_article`, `case_study`, `deep_study`, `dataset`, `faq`, `tool`, `beginner`, `uncategorized`.
- Liens FR pointent vers `https://eco3min.fr/SLUG-FR/`, liens EN vers `https://eco3min.fr/en/SLUG-EN/`. Pas de cross-lang.
- `wp_category_slug` doit exister en BDD WP (résolu via slug).
- `parent_major_pair_id` doit avoir été déclaré AVANT le satellite qui le référence (ordre dans le tableau `articles`).

### 12.6 Workflow opérationnel mega — voir section 14

---

## 13. Les 3 projets Claude associés au mega

### 13.1 Projet A — "Eco3min Cluster Builder — A. Architect (blueprint)"

**À utiliser quand** : tu démarres un nouveau cluster bilingue from scratch.

**Knowledge files attendus** :
- `01-arborescence-piliers-clusters.md` (mapping FR ↔ EN des piliers + sub_piliers + catégories WP)
- `02-levels-glossary.md`
- `03-editorial-guidelines-eco3min.md`
- `05-inflation-master-mapping.md` (référence)
- `06-matrice-maillage-inflation-existante.md` (référence)
- `07-architect-blueprint-template.md` (template du blueprint cible bilingue)

**Input** : pillar_slug FR + EN, post_id FR + EN, sub_pilier_slug FR + EN, wp_category_slug FR + EN, question éditoriale, volume cible.

**Output** : un document markdown bilingue contenant l'architecture complète du cluster (1 paire MAJEUR + N paires satellites avec titres, slugs, meta titles, intentions, anti-cannibalisation, maillage tissé) prêt à passer au projet B.

**Durée typique** : 15-25 min, 1 conversation.

### 13.2 Projet B — "Eco3min Cluster Builder — B. Writer (JSON output)"

**À utiliser quand** : tu as un blueprint validé du projet A et tu veux produire les articles du cluster (revue paire par paire, import en batch unique).

**Knowledge files attendus** :
- `01-arborescence-piliers-clusters-CORRIGE.md`
- `02-levels-glossary.md`
- `03-editorial-guidelines-eco3min.md`
- `08-format-c-v11-json-spec.md` (la spec Format C v1.1)
- `regle_de_redaction_ARTICLE_MAJEUR.md` et `regle_de_redaction_ARTICLE_SATELLITE.md` (règles éditoriales autoritatives, FR + EN)
- `eco3min-snapshot-*.json` (frais, à réuploader à chaque cluster)

**Workflow (CI V1.1.0)** :
1. Coller le blueprint bilingue complet en 1er message.
2. "Paire 1" / "go" → bootstrap (lecture spec + snapshot) puis 1 JSON Format C v1.1 de REVUE (paire FR + EN + cross_cluster_targets) + recap compact.
3. "suivant" → paire suivante (variation MODE + encart).
4. "bundle" → assemblage du **JSON batch unique importable** (N paires, stratégie A) + validation cluster-wide programmatique.
5. "C" → inputs Projet C (CSV de routage, IDs sources, prompt de lancement).

**Output** : N JSONs de revue + **1 JSON batch importable** pour un cluster de N paires.

**Durée typique** : 6-10h pour 26 paires, étalable sur plusieurs jours.

### 13.3 Projet C — "Eco3min Maillage Optimizer — C. Patcher" (= projet existant)

**À utiliser quand** : tu veux générer des patches pour intégrer de nouveaux articles au maillage existant, OU optimiser le maillage d'un cluster existant, OU faire une optimisation site complet (tier=T1).

**Statut** : RÉUTILISE le projet existant chez Paul. Pas de modification de Custom Instructions.

**Knowledge files** : conservés tels quels.
- `01-arborescence-piliers-clusters.md`
- `02-levels-glossary.md`
- `03-editorial-guidelines-eco3min.md`
- `04-format-patches-plugin-spec.md`
- `05-inflation-master-mapping.md`
- `06-matrice-maillage-inflation-existante.md`

**Input** : Format B (export LIGHT du mega ou de Level Classifier legacy), avec ou sans `chunk_info`.

**Output** : `patches-{cluster}-{n}.json` au format strict v1.0.2 (voir section 6).

**Durée typique** : 15-30 min pour un cluster (60 patches), 20-40 min par chunk (100 optims).

### 13.4 Tableau de décision — quel projet Claude lancer ?

| Situation | Projet à utiliser |
|---|---|
| Je veux créer un cluster bilingue from scratch | **A. Architect** d'abord, puis **B. Writer** |
| J'ai un blueprint validé, je veux écrire les articles | **B. Writer** |
| Je veux intégrer de nouveaux articles au maillage existant | **C. Patcher** (avec export `new_posts` du mega) |
| Je veux optimiser un cluster existant (mature) | **C. Patcher** (avec export `cluster:{slug}`) |
| Je veux optimiser tout le site | **C. Patcher** chunk par chunk (avec export `all` chunked du mega) |
| Je veux juste classifier des articles existants non classifiés | Aucun projet Claude. Onglet 2 Tinder du mega (V0.5) ou Tinder du Level Classifier legacy |

---

## 14. Méthode opérationnelle Paul (process)

> Cette section est ce que Claude utilise pour te guider précisément quand tu lui demandes "comment faire X". Si la situation matche un cas, Claude doit renvoyer la séquence exacte.

### 14.1 Cas "Je veux créer un nouveau cluster bilingue de N articles"

**Pré-requis** : pillar et sub_pilier de rattachement existent en FR ET EN dans le référentiel mega ou WordPress.

**Séquence** :

1. **Préparer les inputs** (~20 min) :
   - Vérifier dans WP que les piliers/sub_piliers cibles existent en FR + EN
   - Récupérer les slugs FR + EN, post_id FR + EN, wp_category_slug FR + EN
   - Formuler la question éditoriale centrale
   - Décider du volume (typiquement 15-30 paires satellites + 1 paire MAJEUR)

2. **Lancer projet A Architect** (~20 min) :
   - Nouvelle conversation dans projet "Eco3min Cluster Builder — A. Architect"
   - Coller le prompt de lancement (template section 11.1 de la spec v1.1) avec tous les inputs
   - Récupérer le blueprint bilingue produit
   - Vérifier complétude : tous les slugs présents FR + EN, matrice de maillage cohérente

3. **Lancer projet B Writer** (~6-10h, étalable) :
   - Nouvelle conversation dans projet "Eco3min Cluster Builder — B. Writer"
   - Coller le blueprint complet en 1er message
   - "Démarre avec la paire 1" → JSON → vérifier valide → sauver localement comme `cluster-001-pair-001.json`
   - "OK suivant" → JSON paire 2 → ... → fin
   - Étaler sur plusieurs jours si besoin (NEW CHAT par session, recoller le blueprint)

4. **Importer dans le mega via onglet 3** (~10 min) :
   - Upload tous les JSONs via FileZilla dans `/wp-content/uploads/eco3min-mega/imports/`
   - WP Admin → Eco3min Mega → Import cluster → Rafraîchir
   - Pour chaque fichier : Sélectionner → Validate (dry run) → si OK Apply
   - Le mega crée les paires FR + EN, set Polylang, archive en `.applied`

5. **Exporter pour le maillage entrant** (V0.5+ : depuis le mega ; V0.1 : via Level Classifier legacy + filtrage `new_posts`) :
   - Onglet 4 → Export LIGHT, scope=`new_posts:[ids des nouveaux posts]`
   - Télécharger le JSON

6. **Lancer projet C Patcher** (~30-60 min) :
   - Nouvelle conversation dans projet "Eco3min Maillage Optimizer — C. Patcher"
   - Coller le JSON Format B
   - Récupérer `patches-{cluster}-{n}.json`

7. **Importer les patches dans le mega via onglet 4** (~5 min) :
   - Upload via FileZilla dans `/imports/`
   - Onglet 4 → Sélectionner → Validate → Apply
   - Les nouveaux articles sont maintenant intégrés au maillage existant

8. **Vérification** : passer Site Audit (legacy) ou re-scan mega (V0.5+) pour voir les nouveaux liens en BDD.

**Durée totale** : ~7-12h sur plusieurs jours.

### 14.2 Cas "Je veux optimiser le maillage d'un cluster existant"

**Pipeline** : LEGACY ou MEGA (au choix, le mega n'a pas d'export V0.1, donc en V0.1 : utilise legacy ; en V0.5+ : tu peux tout faire dans le mega).

**Séquence V0.1 (utilise legacy)** :

1. Site Audit → re-scan complet (vérifier que les liens du cluster sont à jour).
2. Level Classifier → onglet Audit Maillage → Export pour le cluster cible (filtre par cluster) → JSON Format B.
3. Projet C Patcher → patches.json.
4. Mega onglet 4 (ou Maillage Cluster legacy v1.0.2) → Import patches.
5. Site Audit → re-scan complet.

**Séquence V0.5+ (tout dans le mega)** :

1. Mega onglet 2 → Scan complet du cluster.
2. Mega onglet 4 → Export LIGHT, scope=`cluster:{slug}`, tier=T1+T2+T3 → JSON.
3. Projet C Patcher → patches.json.
4. Mega onglet 4 → Import patches.
5. Mega → re-scan auto déclenché.

**Durée totale** : ~90 min.

### 14.3 Cas "Je veux faire une optimisation site complet"

**Disponible uniquement en mega V0.5+** (mode chunked). En V0.1 : utiliser legacy avec exports manuels par cluster.

**Séquence V0.5+** :

1. Mega onglet 4 → Export LIGHT, scope=`all`, tier=T1 only (recommandé première passe).
2. Le mega split automatiquement en chunks de 100 optims → ZIP.
3. Pour chaque chunk (séquentiellement) :
   - NEW CHAT projet C Patcher (impératif entre 2 batches).
   - Coller le chunk → patches-chunk-N.json.
   - Mega onglet 4 → Import patches-chunk-N.json → Apply.
   - Re-scan mega entre chunks.
4. Une fois T1 terminé, recommencer avec tier=T2, puis tier=T3.

**Durée totale** : ~30 min × N chunks. Pour 10 chunks → ~5h, étalable sur plusieurs jours.

### 14.4 Cas "Un article existant n'est pas classifié, je veux le classifier"

**V0.1** : utiliser Level Classifier legacy → onglet Tinder. Le mega n'a pas encore d'UI de classification en V0.1 (arrive V0.5).

**V0.5+** : Mega onglet 2 → Tinder UI (avec garde-fous immutabilité, ne montre que les articles avec metas vides).

**Règle** : ne JAMAIS modifier `_eco3min_*` directement via SQL ou via Custom Fields sur des articles déjà classifiés. Le boulot Tinder humain est sacré.

### 14.5 Cas "Mon import cluster a fail / un slug en conflit / Polylang pas câblé"

**Diagnostic** :

1. Vérifier le rapport d'import dans l'UI onglet 3 → liste des `failed_details` et `skipped_details`.
2. Vérifier les logs : Eco3min Mega → Tableau de bord → "Logs récents".
3. Erreurs courantes :
   - `slug_fr_conflict` ou `slug_en_conflict` → le slug existe déjà en BDD. Vérifier via SQL : `SELECT ID, post_status FROM wp_posts WHERE post_name = 'le-slug'`. Si c'est un brouillon abandonné, supprimer puis re-tenter. Si c'est un conflit avec un autre cluster, modifier le slug dans le JSON.
   - `Catégorie WP introuvable` → la catégorie WP avec le slug donné n'existe pas. Créer la catégorie d'abord, puis re-tenter (et bouton "Re-résoudre catégories WP" dans onglet 1).
   - `Polylang inactif` → activer Polylang.
   - `Lien cross-lang dans paire X FR/EN` → le projet B Writer a produit un lien dans le HTML qui pointe vers la mauvaise langue. Corriger dans le JSON ou retourner au projet B avec un message d'erreur ciblé.

### 14.6 Cas "Je veux rollback un import / des patches"

**Patches** :
- SQL pour identifier le batch : `SELECT DISTINCT batch_id FROM wp_e3m_patches_log ORDER BY applied_at DESC LIMIT 5`.
- Identifier les `backup_id` correspondants : `SELECT * FROM wp_e3m_backups WHERE trigger_action='patches_apply' AND trigger_ref='{batch_id}'`.
- Restaurer chaque backup via `Eco3min_Mega_Backup::restore($backup_id)` (UI rollback en V1.0, en V0.1 : passer par PHP/WP-CLI ou SQL Runner avec un snippet).

**Import cluster** : V0.1 ne fournit PAS de rollback en 1 clic. Pour annuler un import : supprimer manuellement les posts FR + EN concernés via WP éditeur (poubelle puis vider la poubelle), Polylang nettoiera ses tables automatiquement. La table `e3m_articles` peut garder des entrées orphelines (à nettoyer via SQL si gênant).

### 14.7 Tableau de décision rapide

| Question utilisateur | Réponse Claude |
|---|---|
| "Comment je crée un cluster bilingue ?" | → 14.1 (process A → B → import → C → import) |
| "Comment j'optimise mon cluster X ?" | → 14.2 (export LIGHT → projet C → import patches) |
| "Comment j'attaque le maillage de tout le site ?" | → 14.3 (export chunked T1 → boucle projet C par chunk) |
| "Comment je classifie un article ?" | → 14.4 (Tinder legacy V0.1, mega V0.5+) |
| "Mon import a foiré, qu'est-ce que je fais ?" | → 14.5 (diagnostic via logs + rapport) |
| "Je veux annuler ce que j'ai fait" | → 14.6 (rollback backups) |
| "Je veux passer des pages en `major_article` / promouvoir des études" | → 14.8 (Fix onglet 1 = level ; Cleanup import = cluster+sous-pilier ; **Cleanup ≠ level**) |
| "Quel projet Claude je lance ?" | → 13.4 (table de décision projets) |
| "Quel pipeline je suis : legacy ou mega ?" | Mega = création nouveau cluster bilingue. Legacy = optimisation cluster existant en V0.1 (en V0.5+ tout passe au mega) |

---

### 14.8 Cas « Je veux passer des pages en `major_article` (promouvoir des études — ou autres — en MAJEUR) »

**Quand.** Une ou plusieurs pages `uncategorized` (ou `deep_study` / `case_study` / `foundation_article`) doivent devenir des MAJEURs maillables — typiquement des études cross-cluster à fort potentiel de citation, fraîchement importées par le projet B (qui importe en `uncategorized`).

**POURQUOI `major_article` et pas `deep_study`.** *(vérifié)* Le conseil du mega ne maille QUE 4 niveaux — `pillar / sub_pillar / major_article / satellite` (cf §1.4). `deep_study`, `dataset`, `faq`, `tool`, `beginner` sont **ignorés** (`if empty(cluster) return` + filtre 4 niveaux, analyzer ~L352). Une étude laissée en `deep_study` ne recevra **jamais** de conseil de lien entrant, et ses satellites entrants ne seront pas maintenus aux re-scans. C'est la convention Eco3min (cf §1.4, review Cleanup côté Claude qui « re-classe les études en major_article ») : une étude qui doit vivre dans le moteur de maillage est classée `major_article`.

**LE PIÈGE CENTRAL — deux metas, deux outils. Cleanup NE POSE PAS le level.** *(vérifié sur l'export v1.0.1 — corrige la formulation de §1.1)* Le contrat d'import Cleanup est :

```json
{"attachments":[{"post_id":123,"cluster":"<slug PILIER>","sub_pilier":"<slug PAGE sous-pilier>","parent_major":<optionnel>}]}
```

→ il écrit **`_eco3min_cluster` + `_eco3min_sub_pilier`** (+ `_eco3min_parent_major` si fourni). **Il n'y a AUCUN champ `level` dans ce contrat** → Cleanup **ne peut pas** mettre `major_article`. Promouvoir = **deux étapes, deux outils** :

| Meta à écrire | Outil | Ce qu'on y met |
|---|---|---|
| `_eco3min_level = major_article` | **Eco3min Fix → onglet 1 « Promote majeur »** (utilitaire Paul, `/wp-admin/admin.php?page=e3m-fix`) | Les **post_id, un par ligne**. Prévisualiser (doit afficher `<level actuel> → major_article`), Appliquer. Écrit **UNIQUEMENT `_eco3min_level`**, avec backup (`_e3m_lvl_bak`) + bouton Restaurer. |
| `_eco3min_cluster` + `_eco3min_sub_pilier` | **Eco3min Cleanup → import** (`/wp-admin/tools.php?page=eco3min-cleanup`) | Le JSON `attachments` ci-dessus. `cluster` = **slug du PILIER parent** (cf `archi-eco3min` §arborescence — PAS le `wp_category_slug`). `sub_pilier` = **slug de la PAGE sous-pilier** (cf `archi-eco3min` §sub_piliers). `parent_major` = **omis**. |

**GÂCHES à connaître (toutes vérifiées) :**

1. **Les `uncategorized` ne sont PAS dans l'export pending Cleanup.** Cleanup ne liste que les articles **classés-mais-orphelins de silo** (level posé, cluster vide) — sur un export réel : 0 `uncategorized` sur 780 items. Donc tu **n'attends pas** de voir tes pages neuves dans l'export : tu écris le JSON `attachments` **à la main**, par post_id. *(L'import est piloté par post_id, pas par appartenance à l'export — à CONFIRMER au **Prévisualiser** : si Cleanup rejette « hors pending », pose le level d'abord via Fix → **re-scan Cleanup** → elles apparaissent alors, classées-sans-cluster → réimporte.)*
2. **`sub_pilier` écrit en SLUG, pas en ID.** Cleanup écrit `_eco3min_sub_pilier` (slug). La Réconciliation du mega le résout (lit l'ID `_eco3min_subpillar` si présent, sinon résout le slug) → breadcrumb OK **tant que seul le slug existe**. Le split-brain n'apparaît que si slug ET ID divergent (cf `archi-eco3min`). Variante ID-propre : le Tinder mega (onglet 2) écrit l'ID — mais il ne montre que les metas vides, donc **avant** de poser le level via Fix.
3. **`parent_major` reste VIDE sur un majeur.** Un `major_article` n'a pas de MAJEUR parent. L'onglet 2 « Import parent_major » du plugin Fix ne concerne PAS ces pages ; il sert plus tard, pour les satellites créés **sous** ces nouveaux majeurs (il valide : cible = `major_article` + même langue).
4. **NE PAS utiliser** les backfills one-shot obsolètes (Classify / Sub-pilier / Major-EN Backfill) — cause historique du split-brain slug/ID (cf §1.3).

**Ordre recommandé :** (1) **Fix onglet 1** (level) → (2) **Cleanup import** (cluster + sous-pilier), en vérifiant au Prévisualiser Cleanup.
*Alternative une-passe :* le **Tinder mega** écrit level + cluster + subpillar-**ID** d'un coup (via `set_meta_safe`, cf §12.4) **si** les pages apparaissent (metas vides). Mais si `uncategorized` est une valeur posée plutôt qu'un défaut vide, il peut les masquer → dans le doute, **Fix + Cleanup est déterministe**.

**Le reste qui en découle (obligatoire) :**
1. **Re-scan mega** → le conseil couvre enfin ces pages ; les liens entrants satellite→MAJEUR déjà posés deviennent la couche canonique T1 (au lieu d'un one-shot).
2. **Liens SORTANTS du nouveau majeur** : un `major_article` doit pointer vers son **sous-pilier parent** + **1-2 majeurs voisins** du cluster (règle de silo, cf `archi-eco3min`). Le conseil mega les propose au scan ; ou générer le batch via le **projet C Maillage Optimizer**.
3. `parent_major` des majeurs reste vide.

**Ce que Claude produit quand Paul dit « passe ces pages en majeur » :**
(a) la **liste des post_id** (à coller dans Fix onglet 1) ;
(b) le **JSON `attachments`** rempli (à importer dans Cleanup) — `cluster` = slug pilier, `sub_pilier` = slug page sous-pilier (valeurs tirées d'`archi-eco3min`), `parent_major` omis ;
(c) la **séquence** Fix → Cleanup + re-scan mega ;
(d) le rappel des **liens sortants** à générer ensuite.

**Template minimal :**

```
# Fix onglet 1 (level) — un post_id par ligne :
27555
27557
27562
...

# Cleanup import (cluster + sous-pilier) :
{"attachments":[
  {"post_id":27555,"cluster":"commodity-regimes-physical-constraints-energy-transition","sub_pilier":"commodities-macroeconomic-regime-signals-cycles-inflation-strategic-power"},
  {"post_id":27557,"cluster":"matieres-premieres-economie-mondiale","sub_pilier":"cycles-transmission-macro"}
]}
```

---

## 15. Migration & cohabitation

### 15.1 Activation du mega — checklist

1. **Backup BDD complet** (le mega ne touche pas au legacy mais on prend pas de risque).
2. **Tester sur staging d'abord** (minimum : activer + import 1 cluster fictif de 1 paire + vérifier Polylang câblé).
3. **Activer Eco3min Mega** dans WP Extensions.
4. À l'activation :
   - Les 5 tables `e3m_*` sont créées.
   - La table `eco3min_audit_pillars` est migrée (idempotent) vers `e3m_referentiel`.
   - Les `wp_category_id` sont résolus à partir des `wp_category_slug` du référentiel.
   - Les dossiers `/uploads/eco3min-mega/{imports,exports,backups,logs}/` sont créés.
5. **Vérifier dans le dashboard** : tables créées, référentiel migré, Polylang actif.
6. **Tester un import** sur 1 paire fictive (cluster bidon).
7. **Désactiver les plugins legacy absorbés** progressivement :
   - V0.1 : désactiver **Maillage Cluster v1.0.2** une fois confiance acquise sur l'onglet 4.
   - V0.5 : désactiver **Site Audit, Maillage Audit, Level Classifier**.
   - V1.0 : désactiver **Anchor Diversifier, Redundant Cleaner**.

### 15.2 Cohabitation pendant la transition

Tant que tu n'as pas désactivé un plugin legacy absorbé :
- Aucun conflit fonctionnel (tables différentes, hooks différents, AJAX actions différentes).
- Mais : faire attention à ne pas faire le même import 2 fois (legacy + mega → doublons SQL).
- Recommandation : choisir UNE source pour chaque type d'opération (par ex. en V0.1, utiliser SEULEMENT le mega pour les imports de patches une fois testé).

### 15.3 Drop des tables legacy obsolètes

**À dropper après V0.5** (le scanner mega les remplace) :
- `eco3min_sa_links` (Site Audit) — drop manuel via SQL Runner.
- `eco3min_lc_suggestions` (Level Classifier) — drop manuel via SQL Runner.

**À dropper après V1.0** :
- `eco3min_ad_log`, `eco3min_ad_backup` (Anchor Diversifier).
- `eco3min_rc_cases`, `eco3min_rc_backup` (Redundant Cleaner).

**À dropper toujours** (plugins zappés) :
- `eco3min_ah_snapshots` (Anchor Health, plugin zappé).

**Tables conservées indéfiniment** :
- `eco3min_audit_pillars` (référentiel legacy, gardée comme backup même après migration).
- `eco3min_gsc_*` (GSC Linker conservé).
- `eco3min_dm_*` (Dataset Monitor conservé).

V1.0 du mega ajoutera un bouton "Drop legacy tables" dans l'onglet 1, avec confirmation triple.

---

## 16. Code Snippets — outillage et pieges

### `ewpa/create-code-snippet` ne met a jour aucun snippet

L'ability **cree un nouveau snippet, toujours inactif**. Elle **ne met pas a
jour** un snippet existant.

S'en servir pour patcher un snippet en place produit un **doublon inactif**,
sans erreur : on croit avoir deploye, rien n'a bouge, et le site porte desormais
deux versions du meme code dont une dormante.

**Le deploiement d'un patch de snippet est manuel**, par l'interface Code
Snippets. Un projet qui prepare un patch de snippet ne peut pas clore sa propre
boucle : il livre le patch, quelqu'un le colle.

### L'export local n'est pas la version live

`~/eco3min-wp/snippets/` est un **export**. Avant de proposer un patch, relire la
version en base dans wp-admin : l'export peut avoir pris du retard sur une
modification faite directement dans l'interface.

### Snippet 226 — moniteur de fraicheur editoriale

`0226-eco3min-date-alerte-moniteur-de-fra-cheur-ditoriale.php`.

Il lit un commentaire HTML place dans le `post_content` :

```
<!--e3m-review due="2027-01-10" lead="30" do="ce qu'il faut faire"-->
```

et le projette a l'enregistrement du post en trois metas : `_e3m_review_due`,
`_e3m_review_lead`, `_e3m_review_do`.

**Les metas sont la voie de LECTURE rapide ; le `post_content` est la voie
d'ECRITURE.** Jamais l'inverse : ecrire la meta sans toucher au marqueur serait
ecrase au prochain `save_post`.

Etats calcules, `days = due − aujourd'hui` : `overdue` si negatif (non
masquable), `soon` si dans le preavis, `ok` sinon. Ecran :
`wp-admin/tools.php?page=e3m-review`, derriere authentification — **`WebFetch`
n'y accede pas**, l'inventaire se reconstruit par le MCP.

⚠️ **Le snippet ne lit que le PREMIER marqueur d'une page** — `preg_match`, pas
`preg_match_all`. Une page qui en porte deux n'est surveillee que par le
premier ; le second est du bruit qui fait croire a une surveillance.

⚠️ **Les guillemets du marqueur sont des `"` droits.** Un editeur qui les
typographie casse le parsing **silencieusement** : la page disparait de l'ecran
admin sans erreur. Une date invalide produit le meme effet.

Le pilotage complet — triage, classification du travail, repose de l'echeance —
vit dans le `CLAUDE.md` du projet « Eco3min Keep Content Fresh ».

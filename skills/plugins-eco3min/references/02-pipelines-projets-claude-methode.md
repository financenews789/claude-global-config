# plugins-eco3min — référence : Pipeline cluster bilingue, projets Claude Code A/B/C, méthode opérationnelle (§2, §13, §14.1-14.7)

Extrait de SKILL.md (découpage du 15/09/2026), **réécrit le 15/09/2026** : les projets A/B/C ne sont plus des projets claude.ai (Knowledge, custom instructions, UUID) mais des projets **Claude Code** dans `~/eco3min/eco3min-projets/`, dont les `CLAUDE.md` font foi sur leur plomberie ; les pipelines V0.1-V0.5 du mega (Site Audit, Level Classifier, export LIGHT/Format B, scopes, chunks ZIP, FileZilla) n'existent plus (code du mega 1.0.14, `class-eco3min-mega-tab-3/4`, `importer-cluster`, `importer-multi-pair`, `mu-advisor`). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

---

## 2. Pipelines canoniques (mega 1.0.14, projets Claude Code)

### 2.1 Création d'un nouveau cluster bilingue

```
1. Mega → Maillage → section Snapshot → exports CSV (1.0.14) :
     eco3min-snapshot-{date}.csv  → ~/eco3min/eco3min-projets/context/snapshot.csv
     eco3min-maillage-{date}.csv  → ~/eco3min/eco3min-projets/context/maillage.csv
   (noms fixes, écraser ; maillage.csv porte la date du dernier scan en 1re ligne,
    snapshot.csv n'en a pas → date de modification du fichier)
   ⚠️ Sans snapshot à jour, le projet A génère des slugs/H1 en conflit → cannibalisation.
   Les projets A et B refusent de démarrer sans lui (« mode dégradé » seulement si
   Paul l'autorise nommément).

2. Projet A — Claude Code, dossier "Eco3min Cluster Builder — A. Architect"
   Entrée : question centrale FR + nombre de paires (+ rattachement pilier/sous-pilier
   si Paul le fournit, sinon procédure autonome). Message d'ouverture :
   LAUNCH_PROMPT_TEMPLATE.md.
   Sortie : blueprint bilingue selon docs/07-architect-blueprint-template.md
   (rattachement, architecture, 1 paire MAJEUR, N-1 satellites, stats de maillage,
   vérifications) après les 5 contrôles anti-cannibalisation exécutés par programme
   contre le snapshot. Sauvegarder le blueprint : c'est l'entrée du projet B.

3. Projet B — Claude Code, dossier "Eco3min Cluster Builder — B. Writer"
   Bootstrap obligatoire (lire docs/08-format-c-v11-json-spec.md, dater le snapshot,
   croiser blueprint / spec / snapshot). Puis, sur signal :
     « paire 1 » / « go » → gate de données du composant + paire MAJEUR (JSON de revue)
     « suivant »          → paire suivante (variation MODE + encart)
     « bundle » / « batch » → LE JSON D'IMPORT UNIQUE du cluster
                             (operation create_cluster_bilingual, Format C v1.1)
                             + validation cluster-wide
     « snippet »          → snippet.php du composant interactif du MAJEUR
     « C »                → inputs de la phase C : CSV de routage, liste des post_id
                            sources (cross_cluster_targets), prompt de lancement
   Les JSON par paire sont des artefacts de revue ; seul le batch s'importe.

4. Mega → Import cluster
   Option A ⭐ drag & drop du batch (.json ≤ 10 Mo) ; option B fichier déjà déposé via
   FileZilla dans /uploads/eco3min-mega/imports/.
   → « Sélectionner » → « 🔍 Valider sans appliquer (dry run) » → « ✅ Appliquer ».
   Crée les paires FR+EN (wp_insert_post), câble Polylang, pose level / cluster /
   sub_pilier (slug) / lang / RankMath / catégorie, résout parent_major_pair_id
   dans le batch, archive le fichier en .applied, journalise dans e3m_imports_log
   (rollback par bouton dans l'historique).
   (Le mode « 🔗 Import multi-pair » — un fichier create_pair_bilingual par paire,
    session reprenable, auto-export cross-cluster — existe mais n'est pas la route
    retenue : le projet B livre un batch.)

5. Snippet du composant interactif : coller et activer dans Code Snippets APRÈS
   l'import (il est gardé sur les deux post_name du MAJEUR). ewpa/create-code-snippet
   crée un snippet inactif et ne met rien à jour (§16).

6. Mega → Scan → « Lancer un scan complet (progressif) »
   (~30-60 s pour 1000 posts ; le bandeau rouge « index de maillage obsolète » disparaît)

7. Mega → Maillage → « 📦 Format AVEC HTML — manuel (export sur liste de post_ids) »
   Coller les post_id sources livrés par le signal « C » du projet B
   → eco3min-targets-…json (post_content + cible + raison) = export « targets manual ».
   (En import batch, le mega ne génère PAS ce fichier tout seul.)

8. Projet C — Claude Code, dossier "Eco3min Cluster Builder — C. Maillage optimiser"
   NEW CHAT. Coller / joindre l'export → outils/extract_anchors.py sélectionne les
   anchor_before byte-exactes → patches-{cluster}-00N.json (format v1.0.2, 20 patches
   max par fichier, un fichier par langue si bilingue, cap 18/cible).
   Doctrine de rédaction : patches-maillage-eco3min.

9. Mega → Maillage → drag & drop patches-*.json → « Sélectionner »
   → « 🔍 Valider sans appliquer (dry run) » (15-45 s pour ~30 patches)
   → « ✅ Appliquer les patches (avec backup auto) » (progress bar post par post,
      compteurs appliqués / skipped / failed ; session gardée 1 h → « Appliquer »
      reprend au dernier post traité)

10. Re-scan → vérification (Diagnostic, Conseil, ou MCP eco3min/links mode=inbound)
    → metas : rien à poser (metas-eco3min §4). Mega ≥ 1.0.15 : les satellites
    arrivent en `satellite` avec parent_major (le validator exige le
    parent_major_pair_id) ; mega 1.0.14 : ils arrivent en uncategorized et Paul
    les classifie après import.
```

### 2.2 Optimisation du maillage d'un cluster existant (conseil T1/T2/T3)

```
1. Cleanup (tools.php?page=eco3min-cleanup) : bruit → exclu ; hubs → pillar ;
   export pending → Claude → import attachments (level + cluster + sub_pilier).
2. Mega → Scan complet (e3m_links frais).
3. Mega → 🧭 Conseil maillage : filtre cluster (ou "Tous les clusters") + langue
   (FR / EN / les deux) → "Generer le conseil" → totaux par tier T1/T2/T3 →
   textarea "JSON de conseil — pour « Maillage Optimizer »" (optimizations[]).
4. Projet C (NEW CHAT) ← ce JSON → patches-{cluster}-{n}.json.
5. Import des patches : tools/wp_push.py <fichier> puis ability eco3min/mega-patches
   {file, dry_run:true} puis dry_run:false (SKILL.md §5 étape 8) ; repli onglet Maillage.
6. Re-scan. Boucler jusqu'à T1 = T2 = T3 = 0.
```

Le conseil est **read-only** (lit les metas + `e3m_links`), ne propose rien pour un article sans `_eco3min_cluster`, ne maille que `pillar / sub_pillar / major_article / satellite`, et refuse le cross-lang. Règles de siloing (`class-eco3min-mu-analyzer.php`) : **T1** satellite → son MAJEUR parent (`parent_major`), sub_pillar → son pilier ; **T2** satellite → son sous-pilier, MAJEUR → son sous-pilier, MAJEUR → son pilier ; **T3** pilier → ses sous-piliers, sous-pilier → ses MAJEURs.

### 2.3 Optimisation site complet

Même mécanique que 2.2 avec « Tous les clusters » dans l'onglet Conseil, ou cluster par cluster. Recommandation : traiter T1 d'abord, observer la qualité, puis T2, puis T3 ; un batch (et un new chat projet C) par cluster ou par tranche de ~100 optimisations.

### 2.4 Rattrapage d'orphelins / pages isolées (« targets manual »)

Sélection des cibles et des sources côté Claude (`maillage-orphelins-eco3min`), puis Mega → Maillage → « Format AVEC HTML — manuel » sur la liste des post_id sources → projet C → patches → import. Les post_id des cibles ne sont pas dans cet export : les résoudre par `eco3min/find` ou le snapshot.

---

## 13. Les 3 projets Claude Code

Tous dans `~/eco3min/eco3min-projets/`. Leur `CLAUDE.md` ne porte que la plomberie (entrées, sorties, signaux, validations) ; la doctrine vit dans les skills qu'ils chargent. Chaque projet a un `memoire.md` à lire au bootstrap et un dossier `docs/` pour ses contrats de sortie. **La skill gagne sur la doctrine, le `CLAUDE.md` du projet gagne sur le format de sortie et la plomberie.**

### 13.1 Projet A — « Eco3min Cluster Builder — A. Architect »

**À utiliser quand** : tu démarres un nouveau cluster bilingue from scratch.

**Fichiers** : `CLAUDE.md`, `memoire.md` (clusters déjà construits, arbitrages), `docs/07-architect-blueprint-template.md` (**le contrat de sortie**), `LAUNCH_PROMPT_TEMPLATE.md`. Skills chargées : `archi-eco3min`, `editeur-eco3min`, `formats-eco3min`, `cluster-ticker-renfort-dataset` (si ticker/dataset), `maillage-orphelins-eco3min`, `metas-eco3min`.

**Input** : question centrale FR + nombre de paires satellites (6-30) — obligatoires ; rattachement (pillar/sub_pilier slugs + post_id FR et EN, `wp_category_slug`) — optionnel, sinon procédure autonome ; contexte, cibles cross-cluster T3, volumes cibles — recommandés. `context/snapshot.csv` bloquant.

**Output** : blueprint markdown bilingue en 5 sections (rattachement ; architecture avec catégories FONDATION / MÉCANISME / APPLICATION / MISE EN GARDE / FRONTIÈRE, matrice S↔S, satellites SINK ; paire MAJEURE ; satellites ; statistiques ; vérifications), après les 5 contrôles anti-cannibalisation par programme. Metas comptées (titre ≤ 60, description ≤ 155), zéro cadratin, ancres natives par langue, liens de même langue (exception datasets EN-only en URL plate), un seul MAJEUR.

**Durée typique** : 10-25 min.

### 13.2 Projet B — « Eco3min Cluster Builder — B. Writer »

**À utiliser quand** : tu as un blueprint validé du projet A et tu veux produire les articles du cluster (revue paire par paire, import en batch unique).

**Fichiers** : `CLAUDE.md`, `memoire.md`, `docs/08-format-c-v11-json-spec.md` (**la spec du format de sortie, fait foi**), `LAUNCH_PROMPT_TEMPLATE.md`. Skills chargées au bootstrap : `editeur-eco3min`, `formats-eco3min`, `archi-eco3min`, `cluster-ticker-renfort-dataset` (si ticker), `metas-eco3min`, `eco3min-import-contenu-bilingue` (section « Composant interactif » seulement).

**Workflow** : bootstrap (spec lue, snapshot daté, écarts blueprint/spec consignés dans `blueprint_deviations`) → « paire 1 » (MAJEUR, gate de données du composant) → « suivant » → … → « bundle » (JSON d'import unique + validation cluster-wide) → « snippet » (composant du MAJEUR) → « C » (inputs de la phase C).

**Output** : N JSONs de revue + **1 JSON batch importable** (`create_cluster_bilingual`, Format C v1.1) + `snippet.php` + liste des post_id sources pour la phase C. Levels : MAJEUR en `major_article`, satellites en `satellite` avec `parent_major_pair_id` (mega ≥ 1.0.15, 17/09/2026) — en `uncategorized` seulement si le mega live est encore 1.0.14 (Paul classifie alors après import).

**Durée typique** : 1-2 h pour 25 paires, étalable (NEW CHAT par session, recoller le blueprint).

### 13.3 Projet C — « Eco3min Cluster Builder — C. Maillage optimiser » (= C. Patcher)

**À utiliser quand** : tu veux générer des patches pour intégrer de nouveaux articles au maillage existant, OU optimiser le maillage d'un cluster existant (conseil T1/T2/T3), OU rattraper des orphelins (« targets manual »).

**Fichiers** : `CLAUDE.md`, `memoire.md`, `docs/04-format-patches-plugin-spec.md` (**le contrat du plugin, fait foi**), `outils/extract_anchors.py` (sélection programmatique des `anchor_before`, jamais à l'œil), `patches_historiques/`. Skills chargées : `patches-maillage-eco3min` (tout le pipeline de rédaction), `maillage-orphelins-eco3min` (amont), `editeur-eco3min`, `archi-eco3min`, `plugins-eco3min`.

**Input** : JSON `optimizations[]` de l'onglet Conseil du mega, OU export « Format AVEC HTML — manuel » / « targets manual » (`articles[]`) de l'onglet Maillage. Il démarre dès que Paul colle le JSON, sans question préalable.

**Output** : `patches-{cluster}-{n}.json` au format strict v1.0.2 (voir section 6) — `expected_occurrences` = 1, 20 patches max par fichier, fichiers séparés par langue, mécanisme APPEND après `anchor_before`.

**Durée typique** : 15-30 min pour un cluster (60 patches).

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

## 14. Méthode opérationnelle Paul (process)

> Cette section est ce que Claude utilise pour te guider précisément quand tu lui demandes "comment faire X". Si la situation matche un cas, Claude doit renvoyer la séquence exacte.

### 14.1 Cas "Je veux créer un nouveau cluster bilingue de N articles"

**Pré-requis** : pillar et sub_pilier de rattachement existent en FR ET EN dans le référentiel mega ou WordPress ; `context/snapshot.csv` et `maillage.csv` régénérés depuis l'onglet Maillage du mega.

**Séquence** : §2.1 ci-dessus, étape par étape. Récapitulatif :

1. **Snapshot** (~5 min) : exports CSV du mega → `eco3min-projets/context/`.
2. **Projet A Architect** (~10-25 min) : question centrale + nombre de paires (+ rattachement), blueprint bilingue, 5 contrôles anti-cannibalisation.
3. **Projet B Writer** (~1-2 h pour 25 paires, étalable ; NEW CHAT par session, recoller le blueprint) : paires de revue → « bundle » → batch unique + `snippet.php` + « C ».
4. **Import** (~5 min) : onglet Import cluster, drag & drop du batch, Sélectionner → dry run → Appliquer. Puis coller/activer le snippet du composant.
5. **Scan** (~5 min) : onglet Scan, bandeau rouge disparu.
6. **Export cibles** (~2 min) : onglet Maillage → « Format AVEC HTML — manuel » sur les post_id sources du signal « C ».
7. **Projet C** (~15-30 min, NEW CHAT) : `patches-{cluster}-00N.json`.
8. **Import patches** (~5 min) : onglet Maillage, dry run, apply.
9. **Vérification** : re-scan, Diagnostic (zéro split-brain, zéro article sans cluster sur les nouvelles paires), Conseil ; sous mega 1.0.14 seulement, classification des satellites `uncategorized` (Tinder mega ou Cleanup `level`).

**Durée totale** : ~2-3 h.

### 14.2 Cas "Je veux optimiser le maillage d'un cluster existant"

**Séquence** : §2.2. Cleanup → scan → onglet Conseil (cluster, langue) → JSON → projet C (NEW CHAT) → import patches → re-scan → boucle.

**Durée totale** : ~60-90 min par cluster.

### 14.3 Cas "Je veux faire une optimisation site complet"

**Séquence** : §2.3. Onglet Conseil « Tous les clusters », tier par tier, un new chat projet C par batch, re-scan entre chaque import.

**Durée totale** : ~30 min × N batches, étalable sur plusieurs jours.

### 14.4 Cas "Un article existant n'est pas classifié, je veux le classifier"

- **Tinder du mega** (onglet Scan & Classification) : ne montre que les articles dont une des 4 metas critiques est vide ; écrit level + cluster + sub_pilier (slug) + parent_major via `set_meta_safe`. Raccourcis clavier Y/Enter accepter, S/Esc skip.
- **Cleanup import** avec `level` (overwrite réversible) + `cluster` + `sub_pilier` : un seul import, piloté par post_id — cf §14.8.
- **Level Setter** (level seul ; `satellite` depuis 1.1.0) ; **Fix 153** (→ `major_article` seul).
- **MCP `eco3min/set-metas`** : dry-run par défaut, `mode=fill` (défaut) ou `overwrite`, validation des 13 levels (`exclu` depuis 1.2.3) et des slugs de rattachement, rollback par `eco3min/rollback`.

**Règle** : ne JAMAIS modifier `_eco3min_*` directement via SQL sur des articles déjà classifiés. Le boulot Tinder humain est sacré. Le SQL direct ne déclenche pas non plus les hooks du snippet SUBPILLAR SYNC (cf `metas-eco3min`).

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

**Patches** : onglet Maillage → « 📋 Historique des imports patches » → bouton **Rollback** sur la ligne du batch (restaure chaque `post_content` depuis `e3m_backups` par `trigger_ref` = batch). En SQL pour identifier : `SELECT DISTINCT batch_id FROM wp_e3m_patches_log ORDER BY applied_at DESC LIMIT 5` puis `SELECT * FROM wp_e3m_backups WHERE trigger_action='patches_apply' AND trigger_ref='{batch_id}'`.

**Import cluster** : onglet Import cluster → « 📋 Historique des imports cluster » → bouton **Rollback** sur l'import (supprime les posts FR + EN ; Polylang nettoie ses tables). La table `e3m_articles` peut garder des entrées orphelines jusqu'au prochain scan. Le snippet du composant, lui, se désactive à la main dans Code Snippets.

**Écritures MCP** (`eco3min/set-metas`, `set-seo`, `update-content`) : `eco3min/rollback` avec le `ref` renvoyé par l'ability (dry-run par défaut). Ne supprime jamais un contenu créé par `create-pair` (corbeille manuelle).

**Cleanup** : Restaurer (section 1) ; les backups `_e3mc_bak_*` de la section 2 se restaurent à la main (pas de bouton) — `parent_major` n'a pas de backup.

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

# plugins-eco3min — référence : Passer des pages en `major_article` — Cleanup, Fix, Level Setter (§14.8)

Extrait de SKILL.md (découpage du 15/09/2026), **réécrit le 15/09/2026** contre `eco3min-cleanup.php` (build juillet 2026), `class-eco3min-mega-tab-2-scan.php` et le snippet 153 : l'ancienne doctrine « deux metas, deux outils — Cleanup ne pose pas le level » est fausse depuis le build de juillet (le contrat d'import accepte `level`), et « le Tinder mega écrit l'ID » était faux (il écrit le slug). Aligné sur `metas-eco3min` §3 et §7.6. Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

---

### 14.8 Cas « Je veux passer des pages en `major_article` (promouvoir des études — ou autres — en MAJEUR) »

**Quand.** Une ou plusieurs pages `uncategorized` (ou `deep_study` / `case_study` / `foundation_article`) doivent devenir des MAJEURs maillables — typiquement des études cross-cluster à fort potentiel de citation, fraîchement importées par le projet B (qui importe en `uncategorized`).

**POURQUOI `major_article` et pas `deep_study`.** *(vérifié)* Le conseil du mega ne maille QUE 4 niveaux — `pillar / sub_pillar / major_article / satellite` (cf §1.4). `deep_study`, `dataset`, `faq`, `tool`, `beginner` sont **ignorés** (`if empty(cluster) return` + filtre 4 niveaux, analyzer ~L352). Une étude laissée en `deep_study` ne recevra **jamais** de conseil de lien entrant, et ses satellites entrants ne seront pas maintenus aux re-scans. C'est la convention Eco3min (cf §1.4, review Cleanup côté Claude qui « re-classe les études en major_article ») : une étude qui doit vivre dans le moteur de maillage est classée `major_article`.

**UN SEUL OUTIL SUFFIT — le contrat d'import Cleanup pose les trois metas.** *(vérifié dans le code le 15/09/2026 — `eco3min-cleanup.php` lignes 449-505)* :

```json
{"attachments":[{"post_id":123,"level":"major_article","cluster":"<slug PILIER>","sub_pilier":"<slug PAGE sous-pilier>"}]}
```

| Champ | Écrit | Politique | Backup |
|---|---|---|---|
| `level` | `_eco3min_level` | **overwrite autorisé** (re-classification) parmi `satellite, major_article, sub_pillar, pillar, deep_study, case_study, foundation_article, dataset, tool, faq, beginner, exclu` | `_e3mc_bak_level` (première écriture, réversible) |
| `cluster` | `_eco3min_cluster` | **fill-only** : n'écrit que si vide, jamais d'écrasement ; doit être un **slug de PILIER** connu (cf `archi-eco3min` §arborescence — PAS le `wp_category_slug`) | `_e3mc_bak_cluster` |
| `sub_pilier` | `_eco3min_sub_pilier` | **fill-only** ; doit être le **slug de la PAGE sous-pilier** connue (cf `archi-eco3min` §sub_piliers) | `_e3mc_bak_sub` |
| `parent_major` | `_eco3min_parent_major` | fill-only ; **omis** sur un majeur | **aucun** |

Garde-fous : post en `publish` obligatoire (sinon `skipped`) ; entrée sans aucun des trois champs → `skipped` ; valeur inconnue → `skipped`. L'import est **piloté par post_id** : les pages n'ont pas besoin de figurer dans l'export pending (qui ne liste que les classés-mais-orphelins de silo — sur un export réel : 0 `uncategorized` sur 780 items). **Cleanup 1.2.0 (lot du 17/09/2026)** : bouton « Previsualiser » (aucune écriture), résultat ligne par ligne avec la raison de chaque skip, backup `_e3mc_bak_pm`, « Restaurer les rattachements importés » → toujours Prévisualiser avant Importer. **Sous 1.1.0 (live)** : pas de prévisualisation, le bouton « Importer & ecrire les metas » écrit directement et le résultat n'affiche que `written` / `skipped` → relire le JSON avant de cliquer, et vérifier ensuite par `eco3min/get-content` ou le Diagnostic mega.

**Alternatives pour le level seul** (quand cluster + sous-pilier sont déjà posés) :

| Outil | URL | Ce qu'il fait |
|---|---|---|
| **Fix** (snippet 153) → onglet 1 « Promote majeur » | `admin.php?page=e3m-fix` | post_id ou URL, un par ligne ; Prévisualiser (`<level actuel> → major_article`) ; Appliquer ; écrit **uniquement `_eco3min_level`** vers `major_article`, backup `_e3m_lvl_bak`, bouton Restaurer |
| **Level Setter** | `tools.php?page=eco3min-level-setter` | n'importe lequel des 13 levels (`satellite` inclus depuis 1.1.0, absent en 1.0.0), backup `_e3m_lvlset_bak`, Restaurer |
| **MCP `eco3min/set-metas`** | — | dry-run par défaut, `mode=overwrite`, validation des levels et des slugs, rollback par `eco3min/rollback` |

**GÂCHES à connaître (vérifiées 15/09/2026) :**

1. **`sub_pilier` s'écrit en SLUG, jamais en ID.** Cleanup, le Tinder du mega (`class-eco3min-mega-tab-2-scan.php:467`) et l'import cluster écrivent tous `_eco3min_sub_pilier` (slug). L'ID `_eco3min_subpillar` (fil d'Ariane) est **dérivé** par le snippet SUBPILLAR SYNC (hooks + cron) ou rattrapé par le Subpillar Aligner. Ne jamais poser l'ID sans slug : l'article sortirait du maillage (conseil et scanner ne lisent que le slug). Doctrine complète → `metas-eco3min` §1-2.
2. **`parent_major` reste VIDE sur un majeur.** Un `major_article` n'a pas de MAJEUR parent. L'onglet 2 « Import parent_major » du snippet Fix ne concerne PAS ces pages ; il sert plus tard, pour les satellites créés **sous** ces nouveaux majeurs (il valide : cible = `major_article` + même langue).
3. **Le Tinder du mega ne montre que les articles à metas vides** : si `uncategorized` est une valeur posée plutôt qu'un défaut vide, il les masque → Cleanup est le chemin déterministe.
4. **NE PAS réintroduire** de backfill one-shot des metas (Classify Backfill, désactivé le 15/09/2026, et ses prédécesseurs) — cause historique du split-brain slug/ID (cf `references/01-inventaire-plugins-actifs.md` §1.2).

**Ordre :** (1) **Cleanup import** (level + cluster + sous-pilier) → (2) **Diagnostic mega** (zéro split-brain, zéro article sans cluster) → (3) **re-scan mega**.

**Le reste qui en découle (obligatoire) :**
1. **Re-scan mega** → le conseil couvre enfin ces pages ; les liens entrants satellite→MAJEUR déjà posés deviennent la couche canonique T1 (au lieu d'un one-shot).
2. **Liens SORTANTS du nouveau majeur** : un `major_article` doit pointer vers son **sous-pilier parent** + **1-2 majeurs voisins** du cluster (règle de silo, cf `archi-eco3min`). Le conseil mega les propose au scan ; ou générer le batch via le **projet C Maillage Optimizer**.
3. `parent_major` des majeurs reste vide.

**Ce que Claude produit quand Paul dit « passe ces pages en majeur » :**
(a) le **JSON `attachments`** rempli, `level` inclus (à importer dans Cleanup) — `cluster` = slug pilier, `sub_pilier` = slug page sous-pilier (valeurs tirées d'`archi-eco3min`), `parent_major` omis ;
(b) la **séquence** Cleanup → Diagnostic → re-scan mega ;
(c) le rappel des **liens sortants** à générer ensuite (Conseil mega ou projet C).

**Template minimal :**

```
# Cleanup import (level + cluster + sous-pilier) :
{"attachments":[
  {"post_id":27555,"level":"major_article","cluster":"commodity-regimes-physical-constraints-energy-transition","sub_pilier":"commodities-macroeconomic-regime-signals-cycles-inflation-strategic-power"},
  {"post_id":27557,"level":"major_article","cluster":"matieres-premieres-economie-mondiale","sub_pilier":"cycles-transmission-macro"}
]}
```

# archi-eco3min — référence : piège de la colonne `url` du snapshot, parsing d'URL, heuristiques de classification (§2.1, §4, §13)

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026) pour §2.1, l'algorithme de §4, la note Polylang et §13.1-13.6 ; les en-têtes de §4 et §13 ont été réécrits le 15/09/2026 parce que le Level Classifier n'existe plus (le code réel est `Eco3min_Mega_Scanner::suggest_classification()`). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

---

### 2.1 ⚠️ La colonne `url` de `snapshot.csv` est une reconstruction plate — ne jamais s'en servir

**Les URLs de sous-piliers sont IMBRIQUÉES**, à deux segments :
`/{pilier-slug}/{sub-pilier-slug}/` en FR,
`/en/{pilier-slug}/{sub-pilier-slug}/` en EN.

Vérifié en base le 04/09/2026 via l'ability `eco3min/find`, sur 8 sous-piliers
tirés au hasard, 8 sur 8 imbriqués :

- `/politique-monetaire-taux/banques-centrales-actions/`
- `/strategies-dinvestissement/choisir-placements-selon-cycle-macro/`
- `/matieres-premieres-economie-mondiale/matieres-premieres-agricoles/`
- `/macroeconomie-geopolitique/outils-macro/`
- `/en/macro-financial-regimes/crisis-hub/`
- `/en/asset-allocation-strategies-resilient-portfolios-market-regimes/choosing-investments-market-regimes-rate-cycles/`

#### Le piège qui a produit deux erreurs successives

La colonne `url` de `context/snapshot.csv` donne **un seul segment pour les
2979 lignes**, tous levels confondus — y compris les **615 pages `faq`**, dont
les URLs réelles contiennent pourtant `/qr/` en FR et `/qa/` en EN.

Ce n'est pas une donnée : c'est une **reconstruction `https://eco3min.fr/{slug}/`
appliquée uniformément**. Elle ne reflète la réalité que pour les levels qui se
trouvent être à un segment.

Deux conclusions fausses en sont sorties :

1. Le correctif de juillet 2026 du projet A. Architect, qui déclarait la règle
   imbriquée « spéculative et démentie par la BDD » et la remplaçait par « format
   constaté dans le snapshot ». Il s'appuyait sur cette colonne.
2. Une révision de ce skill en septembre 2026, qui a repris la même mesure sur
   97 sous-piliers et en a tiré la même conclusion. **Annulée par le présent
   paragraphe.**

Les deux ont mesuré la reconstruction, pas le site.

#### La règle

- **Le champ `slug` du snapshot est fiable.** Il vient de la base.
- **Le champ `url` ne l'est pas.** Il est reconstruit à plat et se trompe sur
  tout ce qui est parenté hiérarchiquement — sous-piliers, Q&A, hubs.
- Pour une URL réelle : `eco3min/find` ou `eco3min/get-content` renvoient la
  **permalink** calculée par WordPress. C'est la seule source.
- **Ne jamais inférer une structure de permalien**, ni depuis le snapshot, ni
  depuis un pattern supposé.

#### Signal secondaire de classification

Indépendamment de l'URL, un sous-pilier se reconnaît aussi à ce que **son slug
est utilisé comme valeur `_eco3min_sub_pilier` par d'autres pages** : 89 des 97
sont ainsi référencés, et une seule valeur de meta ne correspond à aucune page
`sub_pillar`. Utile en complément du pattern d'URL du §13.1, notamment pour les
8 sous-piliers sans enfants (les pages outils, et des pages du hub débutant EN).

⚠️ Sur une page de niveau `sub_pillar` elle-même, `_eco3min_sub_pilier` est
**vide** et `_eco3min_subpillar` vaut `0` — c'est normal : la meta désigne le
sous-pilier de rattachement, et un sous-pilier ne se rattache pas à lui-même.

**Source des valeurs de level** : `Eco3min_Mega_Validator::VALID_LEVELS` (`includes/helpers/class-eco3min-mega-validator.php:39`, 11 valeurs sans `satellite`), `Eco3min_Level_Setter::LEVELS` (12 valeurs avec `exclu`), liste du Tinder mega (`class-eco3min-mega-tab-2-scan.php:284`, 11 valeurs avec `satellite`). L'ancienne constante `class-classifier.php::LEVELS` du Level Classifier n'existe plus — ne pas inventer de level supplémentaire.

---

## 4. Parsing d'URL bilingue

Logique implémentée aujourd'hui à deux endroits, vérifiés le 15/09/2026 :

- `Eco3min_Mega_Scanner::suggest_classification()` (`includes/core/class-eco3min-mega-scanner.php:523-580`) — `get_permalink` → `parse_url(PHP_URL_PATH)` → `explode('/')` → `array_shift` si `segments[0] ∈ {en, fr}` → 1 segment = `pillar`, 2 segments = `sub_pillar` avec `cluster = segments[0]`, sinon `cluster = segments[0]`, `sub_pilier = segments[1]`. Le mega **ne vérifie pas** que `segments[0]` appartient à une liste de piliers connus : une page hub à 1 segment est donc suggérée `pillar` (d'où les 9 hubs fonctionnels à `level=pillar`, cf référence 03).
- `eco3min-cleanup.php:533-534` (détection des hubs, section 3) — même retrait du préfixe langue, puis « hub = exactement 1 segment ET au moins un enfant à 2 segments commençant par ce slug ».

Algorithme de référence (inchangé depuis le Level Classifier) :

```
1. Récupérer l'URL via get_permalink($post_id)
2. Extraire le path (wp_parse_url, PHP_URL_PATH)
3. Splitter en segments par "/"
4. SI segment[0] ∈ {'en', 'fr'} → array_shift() (retirer prefix langue)
5. segment[0] = slug pilier candidat (vérifier qu'il ∈ known_pillars)
6. segment[1] = slug sub-pilier candidat (vérifier qu'il ∈ known_sub_pillars)
```

**Cas du `level=pillar`** : retourne toujours `pilier=null, sub_pilier=null` (sommet).

**Cas du `level=sub_pillar`** : retourne `pilier=segment[0]` mais `sub_pilier=null` (lui-même est un sub-pilier).

**Cas autres levels** : `pilier=segment[0], sub_pilier=segment[1]` si tous deux reconnus.

Il n'y a plus de cache statique `known_pillars` / `known_sub_pillars` à réinitialiser : la liste de référence des piliers et sous-piliers est `e3m_referentiel` (onglet Référentiel du mega) et, en live, `eco3min/taxonomy`.

**Note langue (Polylang)** : la langue d'un post est lue via `pll_get_post_language($id)` (taxonomie Polylang), pas via la postmeta `_eco3min_lang` qui peut être obsolète. Le mega utilise systématiquement `Eco3min_Mega_Polylang_Bridge::get_post_language()` qui encapsule cet appel.

---

## 13. Heuristiques de classification

### 13.0 Ce qui tourne réellement (mega 1.0.14)

Il n'existe **pas** de `Eco3min_Mega_Classifier::suggest_level()`. La seule heuristique en service est `Eco3min_Mega_Scanner::suggest_classification($post_id)`, appelée par le Tinder pour pré-remplir la carte — elle **suggère**, ne classifie jamais :

| Condition (dans cet ordre) | Suggestion |
|---|---|
| URL à 1 segment (hors préfixe langue) | `pillar` |
| URL à 2 segments | `sub_pillar`, `cluster = segments[0]` |
| sinon, `cluster = segments[0]`, `sub_pilier = segments[1]`, puis : | |
| `word_count ≥ 4500` | `major_article` |
| `2500 ≤ word_count < 4500` | `satellite` (« satellite long ») |
| `word_count < 800` et URL contient `/qa/` ou `/qr/` | `faq` |
| `word_count < 800` sinon | `satellite` (« satellite court ») |
| `800 ≤ word_count < 2500` | `satellite` (défaut) |

Pas de scoring, pas de mots-clés de titre, pas de Jaccard, pas de détection de `parent_major` : `foundation_article`, `deep_study`, `case_study`, `dataset`, `tool`, `beginner` ne sont **jamais** suggérés par le code — ils se posent à la main (Tinder, Cleanup, Level Setter). Le Tinder n'enqueue que les articles à metas vides (`auto_enqueue_tinder`, raisons `new_post` / `no_level` / `no_cluster` / `no_sub_pilier` / `no_parent_major`).

### Grille historique du Level Classifier (plugin désinstallé) — conservée comme grille de lecture humaine

Ce qui suit décrit le scoring de `eco3min-level-classifier/includes/class-classifier.php`, **qui n'existe plus** (plugin désactivé, dossier supprimé du dépôt le 15/09/2026, table `eco3min_lc_suggestions` droppée). Il n'a jamais été porté dans le mega. On le garde parce que la colonne « Indicateurs principaux » de la table des levels (SKILL.md §2) en dérive et qu'il reste la meilleure grille pour classifier une page **à la main**. Les mentions de `eco3min_sa_links` et du bug `source_post_id` sont historiques : cette table est droppée, `e3m_links` utilise `src_post_id`.

### 13.1 Patterns URL prioritaires

| Pattern URL | Level suggéré (score élevé) |
|---|---|
| 1 segment ∈ pillars | `pillar` (+30) |
| 2 segments avec 1er ∈ pillars | `sub_pillar` (+12) — **règle correcte**, le classifieur travaille sur la permalink WordPress, pas sur la colonne `url` du snapshot (cf. §2.1). Signal d'appoint : le slug est utilisé comme valeur `_eco3min_sub_pilier` par ≥1 autre page |
| URL contient `/qa/` ou `/qr/` | `faq` (+20) |
| URL contient `dataset` ou `donnees` | `dataset` (+8) |
| URL contient `outil` ou `tool` | `tool` (+8) |

### 13.2 Word count

| Range | Bonus |
|---|---|
| ≥ 4500 mots | `major_article` +5 |
| ≥ 3500 et < 4500 | `major_article` +3 |
| ≥ 3000 mots | `deep_study` +2 |
| 500-2500 mots | `satellite` +4 |
| 2500-4000 mots | `satellite` +2 |
| 1500-3500 mots | `foundation_article` +1 |

### 13.3 Mots-clés du titre (insensible aux accents)

| Level | Mots-clés FR | Mots-clés EN |
|---|---|---|
| `foundation_article` | fondamentaux, introduction, principe, comprendre, guide, bases, definition, qu'est-ce | fundamentals, basics, introduction to, understanding, foundations |
| `deep_study` | etude, analyse, historique, histoire, donnees, depuis 19/20, quantitatif | study, analysis, history, since 19/20, quantitative, historical, data series |
| `case_study` | crise de, episode de, cas de, choc de, krach, Volcker, Lehman, COVID, mer rouge | crisis of, shock of, episode of, case of, crash |
| `dataset` | dataset, donnees, serie, data | (idem) |
| `tool` | outil, calculateur, simulateur, diagnostic | tool, calculator, simulator |
| `beginner` | debutant, commencer, pour les nuls, pas a pas | beginner, getting started, how to start, step by step |

### 13.4 Détection FAQ supplémentaire

- Titre commençant par : comment, pourquoi, qu'est-ce, qui, quand, ou / how, why, what, when, where, who, is it, does, can, should
- Titre se terminant par `?` (+3)

### 13.5 Détection MAJEUR via incoming_count

Compté depuis `eco3min_sa_links` (ou `e3m_links` côté mega) :
- `SELECT COUNT(*) WHERE target_post_id = X AND is_external = 0`
- ≥ 20 liens entrants : `major_article` +4
- ≥ 10 liens entrants : `major_article` +2

### 13.6 Détection parent_major (pour les satellites)

Heuristique 1 (prioritaire) : compter les liens sortants du satellite vers chaque MAJEUR du même pilier d'attache, prendre le plus mentionné.

Heuristique 2 (fallback) : Jaccard du titre du satellite avec chaque MAJEUR du pilier (seuil minimum 0.10), prendre le plus proche.

**Note** : H1 est buggée à ce jour côté legacy (utilise `source_post_id` au lieu de `src_post_id`), donc c'est H2 qui tourne en pratique. Le mega corrige ce bug dans son scanner V0.5+. Voir section 10.2.

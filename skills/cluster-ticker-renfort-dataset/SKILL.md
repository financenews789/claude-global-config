---
name: cluster-ticker-renfort-dataset
description: Création d'un cluster éditorial bilingue (7 paires FR+EN) autour d'un ticker FRED (T10Y3M, BAMLH0A0HYM2, T10YIE, WALCL, DGS10, ACMTP10, VIXCLS, DFF, etc.) pour capter les requêtes humaines composées sans menacer le trafic IA/bot capté par le dataset brut existant. À activer pour création ou renfort d'un cluster centré sur un ticker FRED ou un dataset macro-financier suivi. Couvre sélection du ticker, stratégie SEO pure ou hybride, architecture standard 7 paires (MAJEUR + 6 satellites typés), pré-validation snapshot bloquante, templates des launch prompts projets A et B, workflow d'import multi-pair mega-plugin, pipeline projet C de patches d'enrichissement cross-cluster, et pièges critiques (URLs plates, Format C v1.1 imbriqué, conformité AMF, parent_major_pair_id, cross-lang masqué). À combiner avec archi-eco3min, editeur-eco3min, formats-eco3min, plugins-eco3min, production-dataset.
---

# Création d'un cluster ticker / renfort dataset Eco3min

## 1. QUAND ACTIVER CE SKILL

Activer ce skill pour toute conversation impliquant :
- Création d'un nouveau cluster éditorial bilingue centré sur un ticker FRED (T10Y3M, BAMLH0A0HYM2, T10YIE, WALCL, DGS10, ACMTP10, VIXCLS, DFF, CPIAUCSL, U6RATE, etc.)
- Renforcement d'un dataset Eco3min existant par un cluster éditorial sémantique
- Production d'un launch prompt projet A pour ce type de cluster
- Audit d'un blueprint ou de JSONs Format C v1.1 issus de ce type de cluster
- Génération de patches projet C pour le maillage cross-cluster post-import

Ne PAS activer ce skill pour :
- Création d'un cluster thématique classique non lié à un ticker FRED (voir le template B writer standard à la place)
- Production d'un dataset brut (skill `production-dataset`)
- Production d'une étude de recherche (skill `production-research-study`)
- Rédaction d'une page Q&A (skill `production-q-and-a`)

## 2. VUE D'ENSEMBLE DU PATTERN

### Le problème stratégique résolu

Eco3min publie des datasets bruts (pages dataset standardisées avec graphique, métadonnées, exemples de code, méthodologie) qui rankent en SEO **bot/IA** sur des requêtes URL-style (`T10Y3M csv`, `WALCL historical data`, `BAMLH0A0HYM2 daily`). Ce trafic IA est précieux mais ne capte pas les requêtes humaines **composées** qui ont du volume (`T10Y3M recession signal`, `WALCL QT runoff 2024`, `HY OAS vs IG OAS comparison`, etc.).

Le ticker pur en humain (`T10Y3M`, `WALCL`) est trop concurrentiel (FRED, Bloomberg, Investopedia dominent). Mais les **requêtes composées** intégrant le ticker sont plus accessibles SEO et qualifient mieux le trafic.

Le pattern résolu : créer un cluster éditorial de **7 paires bilingues** autour du ticker, sans menacer le trafic IA actuel du dataset brut. Le dataset reste **protégé** (non re-produit, non modifié significativement) et devient le **satellite canonique** auquel le cluster maille pour servir les utilisateurs qui veulent les données brutes.

### Vocabulaire

- **Ticker cluster** = cluster éditorial centré sur 1 ticker FRED, 7 paires bilingues neuves + 10-20 articles existants intégrés via maillage.
- **Dataset canonique** = page dataset existante FRED-style à protéger (trafic IA), au cœur du cluster.
- **Satellites externes** = articles existants liés au sujet intégrés par maillage entrant + sortant (jamais re-produits).
- **Préfixe cluster** = `{ticker-lowercase}-` (ex `t10y3m-`, `hy-oas-`, `walcl-`). Tous les 14 slugs du cluster commencent par ce préfixe.

### Le pipeline complet

```
SÉLECTION TICKER → PRÉ-VALIDATION SNAPSHOT → LAUNCH PROMPT PROJET A → BLUEPRINT
↓
LAUNCH PROMPT PROJET B + BLUEPRINT → 7 JSONs Format C v1.1 (1 batch unique recommandé)
↓
IMPORT MULTI-PAIR mega-plugin → 14 articles créés + auto-génération fichier targets
↓
PROJET C (input = fichier targets) → patches.json
↓
IMPORT PATCHES mega-plugin → dry run → apply → cluster bouclé
```

## 3. ÉTAPE 0 — SÉLECTION DU TICKER CANDIDAT

### Critères de sélection (4 critères à valider)

1. **Dataset Eco3min existant** : le ticker doit déjà avoir une page dataset Eco3min publiée et idéalement déjà visible en GSC sur des requêtes bot/IA. C'est la fondation du cluster — sans dataset existant, ce skill ne s'applique pas (créer le dataset d'abord via skill `production-dataset`).
2. **Audience qualifiée** : analystes macro-finance, gérants institutionnels, économistes, investisseurs particuliers macro-aware. Le ticker doit avoir une communauté qui le suit en humain (pas juste un code FRED obscur sans audience).
3. **Territoire SEO partiellement libre** : vérifier dans le snapshot qu'il n'existe pas déjà un MAJEUR Eco3min qui cible la même requête centrale (risque de cannibalisation). Idéalement 5-15 articles existants liés au sujet, mais pas de MAJEUR centré sur le ticker en tant que requête humaine.
4. **Complémentarité conceptuelle** avec les clusters existants : le ticker doit ajouter une dimension macro distincte. Pour Eco3min les dimensions couvertes par les 5 clusters existants sont : pente courbe (T10Y3M), risque crédit (HY OAS), anticipations inflation (T10YIE), liquidité Fed (WALCL), coût de financement (DGS10). Tout nouveau ticker doit soit ajouter une dimension, soit affiner une dimension déjà couverte.

### Anti-patterns de sélection

- ❌ Ticker sans dataset Eco3min existant
- ❌ Ticker qui chevauche un cluster existant (ex : créer un cluster `T10Y2Y` alors que T10Y3M est déjà publié et couvre la pente)
- ❌ Ticker ultra-niche académique sans audience humaine (ex : ACMTP10 prime de terme : techniquement défendable mais audience trop restreinte pour 7 paires)
- ❌ Ticker FRED sans pendant analytique éditorial (ex : un identifiant interne de mise à jour technique)

### Cas concrets Eco3min (mai 2026)

| Ticker | Statut | Dimension macro | Sub-pilier rattachement |
|---|---|---|---|
| T10Y3M | Publié (1er cluster) | Pente courbe taux | `banques-centrales-actions` |
| BAMLH0A0HYM2 (HY OAS) | En production | Risque crédit | `dynamiques-marche-tensions-cachees` |
| T10YIE | En production | Anticipations inflation | `inflation-au-dela-des-chiffres-mensuels` |
| WALCL | En production | Liquidité Fed | `liquidite-conditions-financieres` |
| DGS10 | En production | Coût de financement | `transmission-monetaire-entreprises` |

Candidats Phase 2+ envisageables : VIXCLS (volatilité — partiellement saturé), DFF (Fed Funds Rate — concurrentiel), CPIAUCSL (CPI — déjà bien couvert via études inflation). À évaluer cas par cas après mesure SEO 3-6 mois post-publication des 5 premiers.

## 4. ÉTAPE 1 — PRÉ-VALIDATION SNAPSHOT (BLOQUANT)

Avant de produire le launch prompt projet A, charger le snapshot Eco3min le plus récent (`eco3min-snapshot-YYYYMMDD-HHMMSS.json`) et exécuter ces vérifications **bloquantes**. Aucune ne peut être skippée.

### Check 1 — Récupération des 4 post_id de rattachement

Le launch prompt projet A doit contenir 4 post_id confirmés :
- Pillar FR + post_id FR
- Pillar EN + post_id EN
- Sub-pilier FR + post_id FR
- Sub-pilier EN + post_id EN

Procédure :
1. Lire `01-arborescence-piliers-clusters-CORRIGE.md` (source de vérité de la structure) pour identifier les slugs cohérents.
2. Croiser avec le snapshot : `articles[].slug` + `articles[].post_id` + `articles[].lang` + `articles[].level == "sub_pillar"`.
3. Vérifier que les 4 post_id existent bien dans le snapshot. Si manquant, refuser de produire le launch prompt et alerter l'utilisateur.

### Check 2 — Anti-cannibalisation des 14 slugs proposés

Proposer 14 slugs FR + EN (7 paires). Pour chaque slug :
- Vérifier que `slug NOT IN articles[].slug` du snapshot (recherche exacte, langue confondue)
- Vérifier qu'aucun slug existant ne partage 3+ mots communs en début de chaîne
- Tous les 14 slugs DOIVENT commencer par `{ticker-lowercase}-` (ex : `t10y3m-`, `hy-oas-`, `walcl-`)

### Check 3 — Anti-cannibalisation H1 + mots-clés

Pour chaque H1 proposé :
- Vérifier qu'aucun H1 existant n'a les 4-5 premiers mots identiques (`articles[].post_title`)
- Vérifier qu'aucun MAJEUR existant ne cible le même mot-clé principal (`articles[].rank_math_title` pour les articles `level == "major_article"`)

Tous les H1 DOIVENT commencer par le ticker en majuscules (ex : "T10Y3M : ...", "WALCL : ...", "DGS10 : ...").

### Check 4 — Identification des articles existants à intégrer

Pour chaque ticker, identifier dans le snapshot tous les articles existants liés au sujet :
- Datasets adjacents (`level == "dataset"`)
- FAQ liées (`level == "faq"`)
- Deep studies liées (`level == "deep_study"`)
- MAJEURs ou pillars adjacents (`level == "major_article"`)
- Autres satellites adjacents (`level == "satellite"` ou `"uncategorized"`)

Volume typique : 10-20 articles à intégrer. Pour chacun, noter `post_id`, `slug`, `lang`, `level`, et son **rôle** dans le cluster (source canonique / comparaison / mécanisme / etc.).

### Check 5 — Identification des risques de cannibalisation lourde

Si le territoire est dense (ex : WALCL avec 1 MAJEUR existant `drainage-on-rrp-compensation-quantitative-tightening` + 2 deep studies Net Liquidity), **identifier explicitement** les 1-3 zones de risque de cannibalisation et formuler la différenciation à respecter dans le blueprint. Cette différenciation devient une instruction explicite du launch prompt projet A pour que le blueprint la documente en §2.3 bis (Dérivation explicite).

## 5. ÉTAPE 2 — STRATÉGIE SEO DU CLUSTER

### Architecture standard 7 paires

Tous les ticker clusters Eco3min suivent cette architecture standardisée :

| Pair | Catégorie | Cible SEO type | Exemple T10Y3M |
|---|---|---|---|
| art-001 | **MAJEUR** | "TICKER signal récession" / "TICKER usage central" | T10Y3M signal récession |
| art-002 | **FONDATION** | "TICKER signification" / "TICKER meaning" | T10Y3M signification |
| art-003 | **COMPARAISON** | "TICKER vs autre ticker connexe" | T10Y3M vs T10Y2Y |
| art-004 | **MODÈLE / MÉCANISME** | "TICKER + modèle officiel" / "TICKER décomposition" | T10Y3M modèle NY Fed probit |
| art-005 | **HISTORIQUE** | "TICKER + épisode marquant" | T10Y3M inversion 2022-2024 |
| art-006 | **CAS LIMITE / DIVERGENCE** | "TICKER faux positif" / "TICKER + cas limite" | T10Y3M faux positif 1998 |
| art-007 | **ACTUALITÉ** | "TICKER + phase courante" | T10Y3M dés-inversion 2024 |

Cette architecture peut légèrement varier selon le ticker (par ex pour WALCL : 1=MAJEUR, 2=FONDATION, 3=COMPOSITION, 4=RATIO INTERNATIONAL, 5=HISTORIQUE RÉGIMES, 6=QT ACTUEL, 7=LIMITE DU SIGNAL) mais le **squelette 7 paires** reste constant.

### Stratégie pure vs hybride

Selon la notoriété humaine du ticker, choisir :

**Stratégie pure** (1:1 ticker) : tous les 7 articles ciblent une requête contenant `{ticker}`. À utiliser quand le ticker est universellement tapé en humain (T10Y3M, par exemple, est suffisamment connu des analystes pour qu'on l'utilise comme racine de toutes les requêtes).

**Stratégie hybride** : MAJEUR + FONDATION ciblent le ticker pur (`HY OAS recession signal`, `BAMLH0A0HYM2 explained`), les 5 autres satellites ciblent des variantes humaines plus accessibles (`high yield credit spread`, `IG vs HY`, `credit breaks first`). À utiliser quand le ticker FRED est moins universellement tapé en humain (BAMLH0A0HYM2, WALCL, T10YIE, DGS10).

Cas concrets :
- T10Y3M → pure
- BAMLH0A0HYM2 / HY OAS → hybride
- T10YIE → hybride
- WALCL → hybride
- DGS10 → hybride

### Signaux de cohérence cluster (NON NÉGOCIABLES)

- **Tous les 14 slugs commencent par `{ticker-lowercase}-`**. Aucune exception. Signal de cohérence cluster fort pour Google.
- **Tous les 14 H1 commencent par "{TICKER}"** (en majuscules). Aucune exception. Même signal SEO.
- **Volume cible MAJEUR** : fourchette fixée par le blueprint (défaut 2500-4000 mots par langue ; un hub de renfort peut viser plus haut si confirmé par Paul).
- **Volume cible satellite** : fourchette du blueprint (défaut 1500-2500 mots par langue). Comptage regex du pipeline : surcompte de ~5-8 % → viser regex ≥ borne_basse × 1,07.

## 6. ÉTAPE 3 — PRODUCTION DU LAUNCH PROMPT PROJET A

### Format et livraison

Produire le launch prompt en fichier **`.txt` pur**, pas dans un bloc code markdown. Le bloc code peut se perdre lors du copier-coller dans l'UI claude.ai (faille observée mai 2026). Le fichier doit commencer par `Salut Claude. Je lance le blueprint bilingue...` et finir par `Suis tes instructions et produis le blueprint bilingue complet.`

### Structure obligatoire du launch prompt A

1. **PILLAR DE RATTACHEMENT** : slug FR + post_id FR + slug EN + post_id EN + WP category FR + WP category EN
2. **SUB_PILIER DE RATTACHEMENT** : slug FR + post_id FR + slug EN + post_id EN
3. **QUESTION CENTRALE** : reformulation FR + EN, 1-2 phrases analytiques posant la thèse du cluster
4. **VOLUME** : "1 paire MAJEURE + 6 paires de satellites = 7 paires bilingues = 14 articles"
5. **STRATÉGIE SEO DU CLUSTER** : contexte du push "ticker clusters" Eco3min, position du cluster dans la séquence, stratégie pure ou hybride
6. **LES 7 PAIRES VISÉES** : tableau pré-validé des 14 slugs FR + EN avec catégorie, mot-clé cible FR + EN, slug FR + slug EN
7. **ARTICLES EXISTANTS À INTÉGRER COMME SATELLITES EXTERNES** : tableau avec post_id, slug, lang, level, rôle dans le cluster
8. **ZONES DE CANNIBALISATION** (si applicable) : différenciation explicite à respecter
9. **CONTEXTE THÉMATIQUE DÉTAILLÉ** : 10-20 lignes incluant repères chiffrés (sources : FRED, NBER, BIS, etc.), phase actuelle, audiences cibles
10. **LESSONS LEARNED** : 10 règles de cohérence à appliquer (préfixe slug, H1, URLs plates, slug FR≠EN, AMF, etc.)
11. **LIVRABLE ATTENDU** : sections critiques à produire dans le blueprint
12. **GO** : signal de démarrage avec instruction d'autonomie

### Template minimal (à enrichir avec les données pré-validées)

```
Salut Claude. Je lance le blueprint bilingue d'un cluster Eco3min stratégique : "{TICKER} / {NOM HUMAIN}".

═══════════════════════════════════════════════════════════════════
PILLAR DE RATTACHEMENT
═══════════════════════════════════════════════════════════════════
- Slug FR : {pillar-fr}
- Post ID FR : {nnnn}
- Slug EN : {pillar-en}
- Post ID EN : {nnnn}
- WP category FR : {wp-cat-fr}
- WP category EN : {wp-cat-en}

═══════════════════════════════════════════════════════════════════
SUB_PILIER DE RATTACHEMENT
═══════════════════════════════════════════════════════════════════
- Slug FR : {sub-pilier-fr}
- Post ID FR : {nnnn}
- Slug EN : {sub-pilier-en}
- Post ID EN : {nnnn}

[...]

Suis tes instructions (custom instructions projet A V1.0.2 ou supérieure) et produis le blueprint bilingue complet en un seul bloc markdown.
```

Référence directe pour les exemples complets : `/mnt/user-data/outputs/launch-prompt-A-cluster-{hy-oas,t10yie,walcl,dgs10}.txt` produits en mai 2026.

## 7. ÉTAPE 4 — VÉRIFICATION DU BLUEPRINT PRODUIT PAR PROJET A

Projet A produit un blueprint markdown de 6000-8000 mots. Avant de passer au projet B, vérifier :

### Critères de relecture bloquants

- [ ] Les 4 post_id (pillar + sub-pilier × 2 langues) sont correctement repris dans §0 RATTACHEMENT
- [ ] Les 14 slugs proposés dans le launch prompt sont **tous repris à l'identique** dans §1.4 (pas de variation)
- [ ] Tous les H1 commencent par "{TICKER}" en majuscules
- [ ] Tous les slugs commencent par `{ticker-lowercase}-`
- [ ] §2.3 (Réserve architecturale) signale les rattachements alternatifs éventuels
- [ ] §2.3 bis (Dérivation explicite) documente la différenciation contre les articles existants signalés comme zones de cannibalisation
- [ ] Les introductions FR et EN ne sont PAS des traductions littérales
- [ ] Aucune intention éditoriale ne contient de prescription AMF
- [ ] La matrice de proximité S↔S est cohérente (pas de boucle A→B→C→A)
- [ ] Les liens cross-cluster T3 pointent vers des slugs confirmés dans le snapshot

### Critères de relecture non bloquants

- [ ] Volume du blueprint dans la fourchette 6000-8000 mots
- [ ] Sourcing intégré (institution + date dans le texte des introductions)
- [ ] Réserve architecturale formulée avec arguments contradictoires (pas juste mentionnée)

Si un critère bloquant échoue, retourner au projet A avec demande de correction ciblée, ne PAS passer au projet B.

## 8. ÉTAPE 5 — PRODUCTION DU LAUNCH PROMPT PROJET B

### Format

Idem projet A : fichier `.txt` pur. Court (~10-15 lignes) car la majorité du contenu est dans le blueprint que Paul va coller. Le launch prompt B ne fait que poser les URLs canoniques + WP categories à plat pour que Claude B y accède rapidement sans parser le blueprint.

### Template strict du launch prompt B

```
Salut Claude. Je lance la rédaction bilingue du cluster "{nom court ticker}".

[FICHIER BLUEPRINT JOINT — sortie du projet A Architect, bilingue]

URL DU MAJEUR FR : https://eco3min.fr/{slug-majeur-fr}/
URL DU MAJEUR EN : https://eco3min.fr/en/{slug-majeur-en}/

URL DU SOUS-PILIER FR : https://eco3min.fr/{sub-pilier-slug-fr}/
URL DU SOUS-PILIER EN : https://eco3min.fr/en/{sub-pilier-slug-en}/

CATÉGORIE WP FR : {wp-cat-fr}
CATÉGORIE WP EN : {wp-cat-en}

[COLLER ICI LE BLUEPRINT MARKDOWN COMPLET]

Suis tes instructions. Tu commences quand je dis "Démarre avec la paire 1".
```

### ⚠️ URLs PLATES — RÈGLE CRITIQUE

Les URLs sub-pilier sont **PLATES**, jamais imbriquées sous le pillar :

```
✅ JUSTE  : https://eco3min.fr/banques-centrales-actions/
❌ FAUX   : https://eco3min.fr/politique-monetaire-taux/banques-centrales-actions/
```

Cette règle est vérifiée dans le snapshot Eco3min mai 2026 : 100% des 90 sub-piliers ont une URL plate (champ `articles[].url`). Une version imbriquée serait un 404. Cette règle vaut pour TOUS les liens internes du cluster — articles du cluster vers sub-pilier, articles du cluster vers articles existants, etc.

Cette règle est intégrée aux custom instructions du projet B depuis V1.0.5 (V1.1.0 courante) : format constaté dans le snapshot, jamais inféré.

### Stratégie d'import : A (batch unique) — SEULE STRATÉGIE PERMISE (juillet 2026)

L'ancienne « Option B » (import paire par paire) est **OBSOLÈTE et INTERDITE** : le mega résout `parent_major_pair_id` uniquement intra-batch, un satellite isolé échoue avec `"art-001"` et laisse `_eco3min_parent_major` vide avec `null` (24 metas à patcher à la main). Workflow en vigueur (CI projet B V1.1.0) :

- **Production** : les JSONs par paire produits pendant la session sont des **artefacts de REVUE** (relecture humaine), pas d'import — avec 1 seule entrée `articles[]` et `expected_pairs_count = N`, ils échoueraient à la validation mega.
- **Livrable importable** : sur « bundle », le B assemble **1 seul JSON** `create_cluster_bilingual` avec les N paires en `articles[]`, `parent_major_pair_id: null` sur le MAJEUR et `"art-001"` sur tous les satellites, puis exécute une **validation cluster-wide programmatique** (slugs uniques et absents du snapshot, ancres uniques par langue sur tout le cluster, zéro `/en/` en FR, AMF, CCT vérifiés, zéro cadratin, rank_math dans les limites) AVANT livraison — le batch mega est tout-ou-rien.
- Le mega résout `_eco3min_parent_major` automatiquement à l'import. Pas de dette post-import.

## 9. ÉTAPE 6 — IMPORT MULTI-PAIR VIA MEGA-PLUGIN

### Procédure stricte

1. WP admin → **Eco3min Mega → Import cluster**
2. Section **"Import multi-pair (V1.0.3)"** (PAS la section "Action sur output_paire1.json" en haut de page — celle-là ne génère PAS le fichier targets nécessaire au projet C)
3. Drag & drop du **JSON batch unique** du cluster dans la zone bleue (le multi-fichiers reste supporté depuis V1.0.11, mais les JSONs de revue par paire ne sont PAS importables)
4. Cliquer **"Rafraîchir la liste pour multi-pair"** → vérifier que les fichiers apparaissent
5. **Cocher la checkbox d'en-tête** (sélectionner tous)
6. Cliquer **"Démarrer l'import multi-pair"**
7. Suivre la progression live (~1-3s par paire)
8. À la fin : message *"✅ Session terminée. N paires créées. 0 failed."*
9. Le bandeau de fin affiche un **lien direct vers `eco3min-targets-{cluster}-{date}.json`** — c'est l'input du projet C

### Vérifications post-import

- Vérifier dans WP que les 14 articles sont en `publish` (ou draft selon config)
- Vérifier que les slugs sont conformes à ceux du JSON
- Vérifier qu'au moins 1 satellite a `_eco3min_parent_major` correctement renseigné (résolution automatique intra-batch)

### Si pas de fichier targets auto-généré

Si le bandeau de fin n'affiche pas de lien `eco3min-targets-{cluster}-{date}.json`, c'est que le projet B n'a pas inclus les `cross_cluster_targets` dans les JSONs (phase 2 V1.0.3 oubliée). Procédure de secours :

1. Onglet **Maillage** du mega
2. Section **"Format AVEC HTML — Génération manuelle"**
3. Coller la liste des post_id des articles existants à patcher (récupérée du blueprint §1.3 ou du launch prompt projet A)
4. Cliquer **"Générer Format AVEC HTML"**
5. Télécharger le fichier produit — c'est l'input du projet C

## 10. ÉTAPE 7 — PROJET C : PATCHES D'ENRICHISSEMENT CROSS-CLUSTER

### Input

Le fichier `eco3min-targets-{cluster}-{date}.json` auto-généré (ou son équivalent secours). Il contient les **post_content complets** des articles existants à patcher, sans mapping cible.

### Prompt projet C

Le projet C choisit lui-même les cibles éditoriales parmi les 14 articles neufs du cluster. Prompt type :

```
Génère les patches d'enrichissement cross-cluster. Format patches v1.0.2.
Pour chaque article du fichier joint, ajoute 1 patch qui insère un lien sortant
pertinent vers le bon nouvel article du cluster {TICKER} (cf. le champ targeting_reason).

Plafonds par level :
- satellite, uncategorized : 12 max
- faq, deep_study : 20 max
- major_article : 22 max
- dataset : 12 max

Consigne d'insertion : pour chaque insertion, choisir un paragraphe d'insertion
qui contient au maximum 1 lien sortant existant. Si tous les paragraphes pertinents
éditorialement contiennent déjà 2+ liens, skip ce patch et le signaler dans le rapport
au lieu d'insérer dans une zone saturée.

En intro, donner le mapping source→cible que tu as choisi pour chaque patch,
pour validation/correction avant apply.
```

### Audit du patches.json produit

Avant l'apply, vérifier :
- 1 patch par source (= 1 article existant)
- Toutes les URLs cibles correspondent à des slugs du cluster neuf (14 slugs valides)
- Aucun cross-lang (source FR → cible FR uniquement, source EN → cible EN uniquement)
- Toutes les ancres `<a>` sont uniques (pas 2 patches avec la même ancre dans le cluster)
- Aucune ancre générique ("cliquez ici", "voir", "click here", "read more")
- `expected_occurrences: 1` partout

### Apply

1. WP admin → Eco3min Mega → **Maillage**
2. Section **"Import patches"** (V1.0.12 chunked)
3. Drag & drop `patches-{CLUSTER}-001.json`
4. Cliquer **"Dry run"** (validation sans modifier la BDD)
5. Rapport : N/N patches matchent leur `anchor_before` ?
6. Si OK → cliquer **"Apply"**
7. À la fin : N appliqués / N skipped (ancre non trouvée) / N failed

Le mega crée un backup automatique du `post_content` dans `e3m_backups` avant chaque apply. Rollback possible 24-48h.

## 11. PIÈGES CRITIQUES — ANTI-PATTERNS À ÉVITER

Liste des erreurs commises lors des 5 premiers ticker clusters Eco3min (mai 2026), à éviter explicitement :

### URLs imbriquées au lieu de plates

**Symptôme** : tous les liens sub-pilier en `eco3min.fr/{pillar}/{sub-pilier}/` au lieu de `eco3min.fr/{sub-pilier}/`. Résultat : 14 liens potentiellement 404 par cluster.

**Source** : règle V1.0.4 des custom instructions projet B (faussement issue d'une lecture du knowledge `01-arborescence` mal interprétée). Corrigée en V1.0.5 mai 2026.

**Mitigation** : intégrer EXPLICITEMENT dans le launch prompt projet B la règle URLs PLATES + un exemple visuel ✅/❌. Toujours vérifier contre `articles[].url` du snapshot avant de figer une règle d'URL.

### Format JSON aplati au lieu de Format C v1.1 imbriqué

**Symptôme** : `articles: [{lang: "fr", ...}, {lang: "en", ...}]` (2 entrées plates avec champ lang) au lieu de `articles: [{translation_pair_id, fr: {...}, en: {...}, cross_cluster_targets}]` (1 entrée avec sous-objets `fr` et `en`).

**Conséquence** : le mega-plugin rejette le JSON avec erreurs `Champ 'operation' manquant ou invalide` + `Paire #N : translation_pair_id manquant`.

**Mitigation** : custom instructions projet B V1.0.4+ contiennent un template JSON complet à recopier verbatim. Le format `operation: "create_pair_bilingual"` est déprécié, toujours utiliser `create_cluster_bilingual` même pour 1 paire.

### Cross-lang masqué dans les liens internes

**Symptôme** : un article FR contient un `<a href>` vers un slug qui n'existe qu'en `lang=en` dans le snapshot (ex : article FR maille vers `ny-fed-recession-probability-model-2` qui n'existe qu'en EN, alors que l'équivalent FR est `modele-probabilite-recession-ny-fed`).

**Mitigation** : avant chaque insertion de lien, vérifier dans le snapshot que `articles[slug=X].lang == articles[slug=Y].lang` où Y est l'article source.

### Sub-pilier sans pillar dans les meta

**Symptôme** : `articles[].cluster == "politique-monetaire-taux"` mais `articles[].sub_pilier == null` sur des articles supposés rattachés à un sub-pilier. Conséquence : pas de cohérence dans le mega Tinder de classification.

**Mitigation** : remplir explicitement `sub_pilier` dans le JSON Format C v1.1 (champ optionnel mais recommandé).

### Anti-cannibalisation tardive avec un MAJEUR existant

**Symptôme** : produire 1 cluster qui chevauche fortement avec un MAJEUR existant sans documentation §2.3 bis. Conséquence : 2 articles qui se cannibalisent en SEO.

**Mitigation** : pré-validation snapshot Check 5 (zones de risque) AVANT le launch prompt projet A. Documenter explicitement la différenciation dans le launch prompt.

### Conformité AMF oubliée dans les intentions du blueprint

**Symptôme** : intentions éditoriales avec "Acheter X quand T10Y3M passe sous -50bp", "Allocation 60% obligations / 40% actions si HY OAS > 800bp", FAQ "Faut-il vendre les actions ?".

**Mitigation** : 6 règles AMF rappelées explicitement dans le launch prompt projet A + cross-référence avec `editeur-eco3min`. Pas de prescription, pas de timing, pas de pourcentages d'allocation, pas de FAQ binaire.

### Mauvais onglet d'import dans le mega

**Symptôme** : utiliser "Action sur output_paire1.json" (section single-file en haut de page) au lieu de "Import multi-pair (V1.0.3)" (section plus bas). Résultat : 0 items importés ET pas d'auto-génération du fichier targets pour le projet C.

**Mitigation** : procédure d'import explicitement documentée (§9 de ce skill). Toujours utiliser "Import multi-pair".

## 12. MÉTRIQUES DE SUCCÈS POST-PUBLICATION

Un cluster ticker réussi se mesure 3-6 mois post-publication sur :

1. **GSC impressions** sur les requêtes long-tail composées (`{ticker} {variant}`) : doit dépasser le seuil de 100/mois cumulé sur le cluster
2. **GSC positions** : au moins 3 des 7 paires en top 20 sur leur requête principale dans la langue cible
3. **Trafic IA/bot préservé** : pas de chute >20% du trafic GPT/Claude/Perplexity sur le dataset canonique (vérification via GSC + analytics)
4. **Backlinks externes** : au moins 1-2 backlinks naturels reçus par le MAJEUR ou la deep_study du cluster sur 6 mois
5. **Cohérence interne renforcée** : les ~10-20 articles existants désormais maillés vers le cluster gagnent en pertinence topique (pas de chute SEO sur leurs propres pages)

Si après 6 mois le cluster ne décolle pas sur la majorité de ces métriques, le pattern "ticker cluster" est à reconsidérer pour les futurs tickers candidats. Au moment de la rédaction de ce skill (mai 2026), seul le cluster T10Y3M est publié — les 4 autres clusters sont en pipeline, mesure réelle attendue à T+6 mois.

## 13. WORKFLOW RÉCAPITULATIF — CHEAT SHEET

Pour un nouveau ticker `{TICKER}` :

```
1. Vérifier critères de sélection (§3) — 4 checks
2. Charger snapshot Eco3min le plus récent
3. Pré-valider snapshot (§4) — 5 checks bloquants
4. Définir architecture 7 paires (§5) + stratégie pure/hybride
5. Produire launch prompt projet A en .txt pur (§6)
6. Lancer projet A (nouvelle conversation) → blueprint markdown 6-8K mots
7. Vérifier blueprint (§7) — bloquants + non bloquants
8. Produire launch prompt projet B en .txt pur (§8)
9. Lancer projet B (nouvelle conversation) → 7 JSONs Format C v1.1 (ou 1 batch unique)
10. Import multi-pair via mega-plugin (§9) → fichier targets auto-généré
11. Lancer projet C avec fichier targets → patches.json
12. Audit patches.json (§10)
13. Import patches via mega-plugin → dry run → apply
14. Mesurer à T+3 et T+6 mois (§12)
```

Durée totale de bout en bout : ~3-5 heures pour un cluster, étalées sur 1-2 sessions de travail.

## 14. RÉFÉRENCES CROISÉES

Ce skill se combine avec :

- **`archi-eco3min`** : structure du site, hiérarchie pillar/sub_pilier, levels, metas WP
- **`editeur-eco3min`** : style FR/EN, 6 règles AMF, anti-patterns éditoriaux
- **`formats-eco3min`** : encarts HTML (chapeau, intro, lecture eco3min, à retenir, etc.)
- **`plugins-eco3min`** : mega-plugin onglets, Format C v1.1, custom instructions projets A/B/C
- **`production-dataset`** : production du dataset brut (étape préalable à un ticker cluster)
- **`production-research-study`** : si une deep_study du cluster doit être produite en parallèle
- **`visuels-eco3min`** + **`brand-kit-eco3min`** : visuels du MAJEUR et hero du cluster

Tout choix qui n'est pas spécifiquement couvert par ce skill se réfère par défaut à `editeur-eco3min` (règles éditoriales) ou `archi-eco3min` (règles structurelles).

---

**Version V1.0** — mai 2026. À réviser en V1.1 après mesure GSC des 4 clusters restants (HY OAS, T10YIE, WALCL, DGS10) en production, soit à horizon octobre-novembre 2026. Cibles de la V1.1 : ajustement des critères de sélection ticker selon les performances SEO réelles, raffinement des plafonds de patches projet C selon le retour terrain, éventuelle scission du skill si un pattern "renfort dataset existant" se distingue suffisamment du pattern "nouveau ticker cluster".

# production-research-study — référence : Le système de verrous A→G, dix règles d'écriture, périmètre compute_stats.py, Steps 6.5a et 6.5b (§18)

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 18. Le système de verrous A→G

Les §7 et §12 à §14 posent les règles d'écriture et l'audit extractif. Cette
section les **nomme** et ajoute les contrôles mécaniques qui manquaient. Chaque
verrou est né d'une erreur réelle livrée en production (§24).

### 18.1 Les dix règles d'écriture (avant le Step 5)

1. **Le CSV est la source unique de vérité.** HTML ≠ CSV → c'est le HTML qui a
   tort.
2. **Calculer avant d'écrire.** Toute valeur quantitative de tout livrable a été
   calculée en Python et imprimée sur stdout, puis copiée. Jamais de mémoire,
   jamais estimée à l'œil sur un chart.
3. **« Approximately / roughly / about / around / ~ » est interdit** pour toute
   valeur calculable depuis le CSV. Autorisé uniquement pour : valeurs externes
   non récupérables (`<!-- SOURCE -->`), vérification en attente
   (`<!-- VERIFY -->`), arrondi narratif documenté (« ten-fold » pour 10,36×, le
   chiffre exact énoncé à proximité). Chaque occurrence exige une entrée dans
   `hedge_justifications.json` avec son motif : `external_unverifiable`,
   `verify_pending` ou `narrative_rounding`.
4. **Claims « X of top N »** : classement Python explicite → filtre → comptage →
   impression → copie.
5. **Claims de comptage** (« N events / onsets / observations dans [période] ») :
   assertion Python sur filtre explicite. Sans exception.
6. **Filtres temporels en prose** (« excluding X », « pre-Y », « ex-COVID ») :
   définition formelle dans un dict `FILTERS` canonique en tête de
   compute_stats.py **et** dans le bloc « Filter Definitions » du HTML.
7. **Formulation concept-cohérente** : un nombre juste attribué au mauvais
   concept est une erreur. Longueur de série ≠ délai d'avance. Motifs suspects :
   « only N consecutive [units] » contre « N [units] lead/ahead of » — vérifier
   que la formule correspond au concept énoncé en prose.
8. **Points de retournement historiques** : lookups ligne à ligne
   `df[df.date>=...].iloc[0]`, impression de tous les composants, **piège des
   deux dates** — chaque date traitée séparément.
9. **Claims de direction de régime** : variation de niveau (`df[end]>df[start]`)
   ≠ direction du YoY (`yoy>0`). Vérifier celle qui est réellement affirmée.
10. **Cohérence inter-livrables** : HTML, JSON-LD du PHP, snippets sociaux,
    textes alt et annotations de chart portent les MÊMES valeurs. Une statistique
    fausse se propage 6 fois ou plus. L'audit balaie **tous** les livrables, pas
    seulement le HTML. (Voir §13.)

### 18.2 compute_stats.py — périmètre imprimé obligatoire

`[LATEST OBSERVATION]` · `[EXECUTIVE SUMMARY VALUES]` · `[STATS PANEL]` ·
`[FORWARD RETURNS TABLE]` — par régime **plus chaque union de régimes et chaque
sous-période mentionnée où que ce soit en prose**, plus les variantes ex-COVID si
elles sont mentionnées · `[CHART ANNOTATIONS]` — chaque valeur datée de chaque
chart · `[TURNING POINTS]` — dumps de lignes complètes · `[INTERP-GRID VALUES]` —
chaque comptage et pourcentage de chaque carte · `[SURVEILLANCE BLOCK]` ·
`[COUNTING STATISTICS]` — chaque comptage en prose via filtre explicite et
assertion · `[METHODOLOGY]` — sorties de sensibilité · plus le bloc `FILTERS`
canonique en tête.

**Une section absente de stdout → le Step 6 ÉCHOUE.**

### 18.3 Les sept verrous

| Verrou | Ce qu'il bloque | Où il s'exécute |
|---|---|---|
| **A** | Un fichier intermédiaire qui sert de source de vérité à l'audit | Step 6, PASS 2 |
| **B** | Un nombre juste attribué au mauvais concept | Step 6.5c |
| **C** | Une statistique dérivée hors périmètre de calcul (unions, sous-périodes) | Step 4 |
| **D** | Un hedge interdit utilisé quand même | Step 6.5d |
| **E** | Un comptage lu à l'œil sur un chart | Step 6.5e |
| **F** | Un filtre temporel ambigu | Step 6.5f |
| **G** | Une règle éditoriale de `editeur-eco3min` violée sans que rien ne la signale | Step 6.5g |

**Verrou A — la règle la plus importante.** Au PASS 2, chaque valeur extraite doit
être adossée à une assertion Python **recalculée depuis le CSV brut**, avec
tolérance explicite. **Aucun fichier intermédiaire** — `locked_stats.json`, dumps
de stdout, `intermediate_stats.json` — ne peut servir de source de vérité à
l'audit : **l'audit ne charge que le CSV brut.** Sinon une valeur fausse
s'auto-valide. C'est exactement ce qui a produit 14 copies d'une même erreur à
l'étude #20.

**Verrou B — appariement concept-nombre (Step 6.5c).** Pour chaque nombre en prose
analytique — Beats, méthodologie, FAQ, surveillance ; les cellules de tableau sont
exemptes, leur concept est l'en-tête de colonne — déclarer
`(number, concept_label, python_formula_str, expected)` dans `CONCEPT_PAIRINGS`,
exécuter la formule, apparier la valeur, et vérifier heuristiquement la
compatibilité concept ↔ contexte de la phrase par correspondance de mots-clés sur
les motifs suspects de la règle 7.

**Verrou C — unions et sous-périodes.** Toute union de régimes et toute
sous-période mentionnée en prose est calculée dans compute_stats.py, jamais de
tête.

**Verrou D — scan des hedges (Step 6.5d).** Grep automatique de
`approximately|roughly|about|around|~|close to` suivi d'un chiffre. Chaque
occurrence justifiée dans `hedge_justifications.json`, ou ÉCHEC.

**Verrou E — claims de comptage (Step 6.5e).** Grep automatique de
`N events / occurrences / observations / onsets / episodes / recessions /
false positives / triggers / crossings / cases / instances / times / weeks /
months / years`, ainsi que `N/M` et `N of M`. Chaque occurrence exige une
assertion dans compute_stats.py qui produit exactement ce N.

**Verrou F — formalité des filtres (Step 6.5f).** Grep automatique des expressions
de filtre temporel ; chacune doit exister dans le dict `FILTERS` **et** dans le
bloc « Filter Definitions » du HTML.

**Verrou G — verrous éditoriaux (Step 6.5g).** Les six verrous ci-dessus ne
regardent que des nombres. Les règles de `editeur-eco3min` sont invisibles pour
eux, et ne se dérivent d'aucun CSV : rien ne les signale, ni à l'écriture, ni à
la relecture. Elles se grepent, comme les hedges.

- **Zéro cadratin ( — )** dans tout livrable destiné au site — corps HTML,
  package social, metas, alt et title. Ruptures : virgule, deux-points,
  parenthèses, ou deux phrases. Les plages gardent le demi-cadratin (`1959–2007`)
  et les valeurs négatives le signe moins (`−0,013`). Règle durcie juillet 2026,
  validée programmatiquement côté pipeline B.
- **Zéro tic IA** de la liste de `editeur-eco3min` §5, versant EN compris :
  `worth noting`, `delve`, `dive into`, `ever-evolving`, `paradigm shift`,
  `as we navigate`, `in conclusion,`, `truly`, `literally`, `undeniably`,
  `fundamentally`.
- **Zéro verbe prescriptif** appliqué à un profil (`should`, `must`, `need to`,
  `ought to`, `we recommend`) et **zéro langage d'action ou de timing**
  (`buy`, `sell`, `entry point`, `price target`, `now is the time`,
  `overweight`, `underweight`). Règles AMF 2, 3 et 6.

Mesuré sur l'étude R1 (08/09/2026) : **43 cadratins dans le corps et 18 dans le
package social**, alors que l'audit extractif passait à 100 % sur 163 claims et
que les trois autres scans étaient propres. Un audit numérique ne voit pas une
règle de doctrine.

### 18.4 Step 6.5a — audit post-production

Relire le document du Step 1.5 et vérifier que **chaque défense est présente**.
Scan des termes chargés (§11). Citabilité : le hook est-il au-dessus de la ligne
de flottaison, en premier bullet de l'Executive Summary, et dans la TL;DR ?
Sortie : défenses N/N · termes trouvés/corrigés · hook visible OUI/NON ·
PASS/FAIL.

### 18.5 Step 6.5b — tripwire de direction narrative

Chaque date `YYYY-MM` en prose devient un tuple
`(label, date, csv_column, expected, tol)` dans `NARRATIVE_EVENTS`, ou une entrée
justifiée dans `WHITELISTED_NO_CLAIM`. Exécuter
`narrative_audit.run_narrative_checks(...)` en mode strict.

Attrape : les erreurs de direction, les valeurs datées de pic ou de creux fausses,
les étiquettes de régime fausses, les dates en prose absentes du CSV.
N'attrape pas : les claims de tendance non datés, les claims causaux, les erreurs
internes au CSV.

### 18.6 Périmètre du Step 6 — les sections historiquement oubliées

L'extraction du PASS 1 couvre explicitement : les **sous-titres de charts**, les
**comptages des interp-grids**, les **encarts takeaway**, les **bullets de
surveillance**, et les **textes alt et title des images**. Ce sont précisément
celles que les audits déclaratifs sautent.

### 18.7 Ce que le système ne couvre pas — limites assumées

- Les erreurs **à l'intérieur du CSV** (bugs de `build_csv`). La protection reste
  le Step 1.5 et une passe manuelle de bon sens sur le CSV.
- La **mésinterprétation économique** : corrélation prise pour causalité, seuils
  ad hoc choisis pour maximiser la performance. C'est le travail du Step 1.5.
- Les erreurs **dans un chiffre externe légitimement cité** : leur exactitude
  repose sur la source.

Quand une erreur est découverte après livraison : ajouter son motif au registre
(§24) et son verrou au workflow. Les motifs inconnus futurs exigeront leurs
propres verrous.

---

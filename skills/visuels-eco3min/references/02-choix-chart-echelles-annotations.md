# visuels-eco3min — référence : Choix du type de chart selon la donnée, direct labeling, anti-patterns absolus, échelles et axes, annotations recommandées (§3, §4, §5)

Extrait VERBATIM de SKILL.md (découpage du 17/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 3. Choix du type de chart selon la donnée

Règles standard de data viz finance — Claude doit choisir le type qui sert la donnée, pas le type qui fait joli.

| Donnée | Chart approprié | À éviter |
|---|---|---|
| Série temporelle longue (taux, indices, ratios dans le temps) | Line chart | Bar chart, pie chart |
| Comparaison ponctuelle entre N catégories | Bar chart (horizontal si labels longs) | Line chart, pie chart |
| Composition d'un total à un instant | Bar chart empilé OU table | Pie chart au-delà de 3 segments |
| Évolution d'une composition dans le temps | Stacked area chart, stacked bar | Pie chart séquentiel |
| Corrélation entre deux variables | Scatter plot, avec ligne de régression si pertinent | Bar chart |
| Distribution d'une variable | Histogram, boxplot, density plot | Bar chart trié |
| Comparaison de distributions par catégorie | Kernel density / ridge plot, violin plot | Bar chart de moyennes seules |
| Matrice de relations (corrélations, exposition sectorielle) | Heatmap | Multiple bar charts juxtaposés |
| Comparaison rang temporel (qui dépasse qui dans le temps) | Bump chart, slope chart | Line chart standard |
| Coût combiné de 2 dimensions continues | Heatmap avec gradient continu + isocourbes | Bar chart multi-dimensions |
| **Comparaison multi-entités dans le temps** (pays, actifs, secteurs, indicateurs — 2 à 6 séries) | Line chart multi-séries en palette catégorielle (`brand-kit-eco3min` §2.5), labels directs en bout de ligne | Légende détachée ; couleurs ad hoc ; >6 séries pleines |
| Comparaison multi-entités >6 séries | Spaghetti focus : N séries grises en arrière-plan + 1-2 séries accentuées (rangs 1-2) | 8+ couleurs pleines simultanées |

Le format **multi-entités** (le format signature OWID/FT) est historiquement sous-utilisé chez Eco3min — le mobiliser dès que la donnée est comparative par nature, plutôt que N charts mono-série juxtaposés.

### Direct labeling — règle générale (v1.2)

Pour tout chart à ≤6 séries : **chaque série est labellisée directement en bout de ligne** (ou au point le plus dégagé), dans la couleur de sa série, en Inter 11-12 px. **Légende détachée bannie** — elle force des allers-retours œil-légende, casse la lecture 5 secondes, et pénalise les lecteurs daltoniens (le label direct désambiguïse ce que la couleur seule ne garantit pas). Au-delà de 6 séries (spaghetti focus), seules les séries accentuées sont labellisées ; le nuage gris reçoit un label collectif unique (« autres pays OCDE », etc.).

### Anti-patterns absolus

**Pie charts** : à éviter en macro-finance. Mauvaise lisibilité au-delà de 3 segments, lecture des proportions imprécise. Préférer un bar chart trié décroissant.

**3D** : jamais. Distorsion de perception, aucune valeur ajoutée.

**Double axe Y** : à éviter sauf nécessité réelle (deux variables fortement corrélées dont les unités diffèrent). Si utilisé, mentionner explicitement le risque de manipulation visuelle dans la légende. Cas validé : BBB-share (axe gauche, %) + BBB OAS spread (axe droit, bps) sur même chart — corrélation économique forte, deux unités, légende explicite.

**Gradient décoratif** : pas de gradient sans signification. Une couleur = une catégorie, ou un gradient = une dimension continue (ex : intensité d'inflation par pays, coût d'accessibilité du logement).

---

## 4. Échelles et axes

**Axe Y commence à zéro** : obligatoire pour les bar charts. Optionnel — souvent indésirable — pour les line charts de prix, ratios, indices (couper l'axe rend la dynamique lisible).

**Échelle logarithmique** : à utiliser pour
- Séries de prix ou indices sur plus de 10 ans (un S&P 500 sur 100 ans en linéaire est illisible)
- Ratios à très grande dynamique
- Comparaison de croissances en %

Toujours indiquer `(échelle log)` dans le titre ou la légende.

**Étiquettes d'axes** : unités explicites systématiquement (`%`, `points de base`, `milliards EUR`, `% du PIB`, `index 100 = janv. 2020`).

**Période** : titre du chart inclut la période (`PIB américain 1970-2026`). Pas de chart sans cadrage temporel.

---

## 5. Annotations recommandées

Un visuel macro gagne en valeur quand il contextualise.

- **Récessions** : zones grisées (NBER pour USA, datations OFCE/INSEE pour France, CEPR pour zone euro)
- **Événements clés** : annotations textuelles datées (`mars 2020 — COVID`, `oct. 2008 — Lehman`, `févr. 2022 — invasion Ukraine`)
- **Moyennes historiques** : ligne horizontale en pointillé avec label (`moyenne 1980-2020 : 4,2 %`)
- **Régimes nommés** : zones ombrées en couleur du code régime correspondant (voir `brand-kit-eco3min` section 3)
- **Marqueur principal** : 1 accent terracotta `#B85C3C` sur le moment-clé (voir `brand-kit-eco3min` section 2.3 pour la règle d'unicité)

---
name: visuels-eco3min
description: Standards de production et révision des visuels Eco3min (eco3min.fr) — charts macro-financiers, infographies, images sociales, illustrations. Couvre : sourcing intégré au visuel (institution + date dans le graphique), conformité AMF en data viz (pas de flèches achat/vente, zones prescriptives, cibles de prix), choix du type de chart selon la donnée, anti-patterns finance (pie charts, double axe Y, axes manipulés), cohérence chiffrée article/visuel, qualité technique, copyright. v1.2 : direct labeling en bout de ligne (légende détachée bannie si 6 séries ou moins) et famille multi-entités (pays/actifs/secteurs en palette catégorielle du brand kit, spaghetti focus au-delà de 6 séries). À combiner systématiquement avec brand-kit-eco3min qui définit typo, palette catégorielle 7 rangs, 3 registres de fond et codes régime. Ce skill porte les règles de fond (AMF, sourcing, qualité, choix de chart) qui s'appliquent en complément du brand kit.
---

# Standards visuels Eco3min

> **Philosophie.** Le système de design Eco3min repose sur deux couches complémentaires :
>
> 1. **Le brand kit (`brand-kit-eco3min`)** définit le minimum commun figé — palette, 3 familles typographiques (Source Serif 4 + Inter + IBM Plex Mono), fond crème, accent terracotta unique, codes couleurs régime, format sourcing, watermark. Il garantit la cohérence perçue cross-canal : un lecteur de r/economics qui voit 4 visuels Eco3min très différents doit toujours percevoir « même publication ».
>
> 2. **Ce skill (`visuels-eco3min`)** couvre les règles de fond qui s'appliquent à TOUS les visuels indépendamment du brand kit : conformité AMF, sourcing intégré, choix de chart selon la nature de la donnée, anti-patterns data viz, cohérence article/visuel, qualité technique, copyright. Ces règles sont des invariants — elles existaient avant le brand kit et continueraient d'exister sans lui.
>
> **Ce qui reste libre** : type de chart (line, histogram, kernel density, scatter, heatmap, matrix…), densité chromatique (sobre 1 accent OU multi-couleurs catégorielles OU gradient continu selon ce que sert la donnée), format/ratio (hors heros piliers à 1536×864 strict), composition. La diversité visuelle est un atout — c'est l'angle d'analyse qui varie, pas la marque.
>
> Pour la voix éditoriale et l'AMF côté texte, voir `editeur-eco3min`. Pour les patterns rédactionnels HTML, voir `formats-eco3min`. Pour les heros piliers spécifiquement, voir `production-hero-pilier`. Pour les charts viraux Reddit DIB, voir `production-chart-of-the-week`.

---

## 1. Sourcing intégré dans le visuel

Même règle qu'en rédactionnel : la source apparaît **dans le visuel lui-même**, pas seulement dans la légende d'article. Un graphique extrait du contexte (capture, repost, AI Overview) doit rester attribuable.

**Position standard** : coin inférieur (gauche ou droite), petite taille, mais lisible.

**Format type**
- Données brutes d'une institution : `Source : BCE — T4 2025`
- Calculs Eco3min : `Calculs Eco3min sur données FRED` ou `Calculs Eco3min — sources : BCE, BRI, INSEE`
- Estimation : `≈ estimation Eco3min — méthode dans l'article`

**Mention Eco3min** : présence systématique, discrète, en bas du visuel. Pas de logo géant. Le but est l'attribution, pas le branding.

**Date du visuel** : si la donnée évolue (taux, indices), inclure la date d'extraction (`données au 28 avril 2026`). Évite les visuels périmés repartagés sans contexte.

Pour le format canonique 2 lignes en IBM Plex Mono, voir `brand-kit-eco3min` section 6.

---

## 2. Conformité AMF visuelle — 7 interdictions

Toutes les règles AMF du skill `editeur-eco3min` ont une équivalence visuelle. Un graphique peut violer la conformité AMF même si le texte de l'article ne la viole pas.

### 2.1 Pas de flèches achat/vente

❌ Flèche verte montante avec texte "Buy", "Acheter", "Long"
❌ Flèche rouge descendante avec texte "Sell", "Vendre", "Short"
❌ Flèche neutre + label "Opportunité" / "Point d'entrée"

✅ Si tu veux signaler un événement : annotation neutre datée (`27 oct. 2024 — annonce BCE`), sans direction prescriptive.

### 2.2 Pas de zones colorées prescriptives

❌ Bande verte "zone d'achat", bande rouge "zone de vente"
❌ Zone "survendu" / "suracheté" présentée comme actionnable

✅ Zones grisées pour marquer **régimes économiques** (récessions NBER, cycles d'inflation, etc.) — descriptif, pas prescriptif. Légende explicite : `Zones grisées : récessions NBER`.

✅ Zones colorées via codes régime du brand kit (inflationniste, désinflationniste, stagflation, etc.) — descriptif par nature, jamais prescriptif.

### 2.3 Pas de cibles ou objectifs de prix

❌ Ligne pointillée projetée vers une cible avec label "Objectif 5 800 pts"
❌ Fourchette d'arrivée colorée
❌ Annotation "Cible technique" sur un graphique

✅ Projections d'institutions tierces, attribuées et nommées : `Projection FMI WEO oct. 2025 (zone grisée = bande de confiance)`. Le lecteur sait qui projette quoi.

### 2.4 Pas de scénarios sans dispositif de nuance

❌ Une seule trajectoire prospective tracée fermement, sans cadrage
❌ "Si X alors Y dans 12 mois" matérialisé en ligne ferme

✅ Scénarios multiples (au moins 2, idéalement 3 — central, optimiste, pessimiste) tous tracés avec la même fermeté visuelle. Légende explicite : `Scénarios hypothétiques — non prédictifs`.

### 2.5 Pas d'allocations recommandées en visuel

❌ Pie chart "Allocation prudente : 30 % actions / 70 % obligations"
❌ Bar chart comparatif "Profil dynamique vs prudent"

✅ Allocations historiques observées, sourcées : `Allocations moyennes des fonds 60/40 — données Vanguard 2010-2024`. Descriptif, pas normatif.

### 2.6 Pas de comparaisons géographiques avec ranking visuel

❌ Bar chart trié décroissant "Pays les plus attractifs pour investir"
❌ Carte chloroplèthe avec gradient "Performance" et podium implicite

✅ Bar chart trié, mais légende neutre (`PER prospectif par marché — données Bloomberg, 28 avril 2026`). Pas de mot normatif dans le titre, juste des chiffres.

### 2.7 Pas de timing matérialisé visuellement

❌ Annotation "Bon moment pour entrer" / "Sortir maintenant"
❌ Zone colorée "Fenêtre tactique"

✅ Annotation factuelle datée. Le lecteur tire ses propres conclusions.

---

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

---

## 6. Cohérence article ↔ visuel — vérification obligatoire

**Tout chiffre affiché dans le visuel doit matcher exactement le chiffre cité dans le texte.** Une discordance sape la crédibilité de l'ensemble et expose à des critiques AMF.

**Vérifications systématiques**
- Périodes citées identiques (un chart "1970-2024" ne va pas avec un texte qui parle de "1970-2023")
- Chiffres clés identiques (si le texte dit "+3,2 %", le visuel ne montre pas "+3,1 %")
- Sources identiques (un chart "Source : BCE" ne va pas avec un texte qui dit "selon les données de la BRI")
- Méthode de calcul identique (si le texte parle de "moyenne mobile 12 mois", le chart doit afficher une MM12, pas une MM6)

**Si écart détecté en révision** : c'est l'article qui est généralement à corriger sur le chiffre du visuel (les visuels sont produits depuis les données brutes), mais vérifier au cas par cas.

---

## 7. Qualité technique — non négociable

Une seule de ces erreurs disqualifie le visuel pour publication.

- **Pas de chevauchement** texte sur texte, texte sur courbe, label sur logo
- **Pas de troncature** : aucun mot coupé, aucun chiffre coupé
- **Pas de fautes d'orthographe** (français correct, accentuation correcte sur les majuscules — "É", pas "E")
- **Pas de pixellisation** : exporter en SVG quand possible, sinon PNG haute résolution (≥2x la taille d'affichage)
- **Lisibilité en miniature** : pour les exports sociaux, vérifier que le titre et au moins une donnée clé sont lisibles à 25 % de la taille (test feed mobile)
- **Contraste suffisant** : texte sombre sur fond clair ou inverse, jamais texte gris clair sur fond gris foncé
- **Cohérence des unités** : pas de mélange `M€` et `Md€` dans le même chart sans raison

---

## 7 bis. Rendu PNG — recette Playwright

Le rendu de référence des visuels codés (heros, charts HTML/SVG) passe
par **Chromium via Playwright**, pas par une capture manuelle ni par matplotlib :
c'est le seul chemin qui garantit les trois familles typographiques réelles.

### Le piège des polices

Chromium rend la page **avant** que les Google Fonts soient chargées si on ne
l'attend pas explicitement. Le résultat est un PNG en police de repli —
**sans erreur, sans avertissement**, exactement comme la retombée silencieuse
de matplotlib sur DejaVu Sans. Un visuel entier peut partir en production dans la
mauvaise typo sans que rien ne le signale.

### Séquence obligatoire — aucune étape n'est facultative

1. `set_content(html, wait_until="load")`
2. `await page.evaluate("document.fonts.ready")`
3. `wait_for_timeout(650)` — 650 à 700 ms ; en dessous, le rendu part trop tôt
4. exécuter l'auto-ajustement de titre (voir plus bas)
5. `wait_for_timeout(150)`
6. `screenshot(..., clip={...})`

Sauter l'étape 2 **ou** l'étape 3 suffit à produire le repli silencieux.

### Réglages

- `viewport` aux dimensions cibles, `device_scale_factor=2` — on rend en
  rétine, puis on redescend aux dimensions exactes par PIL/LANCZOS.
- `screenshot` avec un `clip` **explicite**
  `{"x":0,"y":0,"width":W,"height":H}` : sans lui, une marge parasite ou un
  débordement d'un pixel change les dimensions du fichier.
- SVG : géométrie **pré-calculée en Python** puis embarquée en
  SVG inline dans le HTML. Un SVG chargé en ressource externe déclenche des
  blocages cross-origin. Full-canvas en `viewBox="0 0 W H"`,
  `position:absolute; inset:0`, le texte HTML par-dessus en `z-index`.

### Auto-ajustement du titre

Boucle JS qui décrémente la taille de police depuis ~44 px jusqu'à un
plancher de 24-26 px tant que le titre déborde de son budget de deux lignes.

**Doit tourner après confirmation du chargement des polices** — mesurer
avant, c'est mesurer la police de repli, donc calculer un mauvais palier.

L'exposer en `window.__fit()`, l'appeler par `page.evaluate()`, et attendre
`window.__fit_done` via `wait_for_function()` plutôt que par un timeout fixe.

### Vérification

Vérifier explicitement la police rendue sur le **premier visuel d'une
série** — même consigne que pour matplotlib. Un zoom sur un mot en
Source Serif 4 suffit : si le rendu est en sans-serif, toute la série est
à refaire.

### Repli

Si Chromium est indisponible, l'installer (`playwright install chromium`). En
dernier recours seulement, rendre un SVG pur via `cairosvg` — mais la
fidélité typographique y est moins bonne.

---

## 7 ter. Rendu matplotlib — quatre assertions avant `savefig`

Le §7 bis couvre le chemin Playwright, qui est celui des heros et des charts
HTML. Les charts codés en matplotlib — Chart of the Week, visuels de dataset,
séries longues — passent par un autre chemin, avec ses propres échecs
silencieux. Aucun d'eux ne lève d'exception : le PNG sort, il a l'air correct
sur une vignette, et le défaut ne se voit qu'agrandi ou pas du tout.

**Les quatre assertions se posent dans le script, pas dans la relecture.** Une
inspection visuelle rapide a laissé passer les trois premières au moins une fois
chacune, sur des scripts écrits par quelqu'un qui connaissait le piège.

### 1. La police demandée est bien la police rendue

Matplotlib retombe sur DejaVu Sans **sans erreur ni avertissement** quand la
famille n'est pas enregistrée. Voir la recette d'instanciation en mémoire de
projet ; le contrôle, lui, tient en trois lignes.

```python
from matplotlib.font_manager import FontProperties
for family in ('Source Serif 4', 'Inter', 'IBM Plex Mono'):
    got = FontProperties(family=family).get_name()
    assert got == family, 'repli de police : demandé %r, obtenu %r' % (family, got)
```

### 2. Aucun texte ne déborde du canvas

Un titre trop long est **rogné au bord du PNG**, pas mis à la ligne, pas réduit.
Sur un rendu 1920×1080 examiné en vignette, un titre amputé de ses trois
derniers mots passe inaperçu.

```python
fig.canvas.draw()
r = fig.canvas.get_renderer()
W, H = fig.get_size_inches() * fig.dpi
for t in list(fig.texts) + list(ax.texts):
    bb = t.get_window_extent(renderer=r)
    assert -1 <= bb.x0 and bb.x1 <= W + 1, 'débordement horizontal : %r' % t.get_text()[:48]
    assert -1 <= bb.y0 and bb.y1 <= H + 1, 'débordement vertical : %r' % t.get_text()[:48]
```

### 3. Les textes d'en-tête ne se recouvrent pas

Titre, sous-titre, badge d'unité et bandeau de killer phrase sont posés en
coordonnées figure. Il suffit qu'un titre s'allonge d'un mot pour que le badge
en haut à droite lui passe dessus. Le recouvrement est parfaitement lisible en
plein écran et invisible sur une vignette.

La tolérance n'est pas cosmétique : les boîtes englobantes de texte incluent
toute la hauteur de ligne, donc deux lignes empilées serré se touchent sans se
gêner. Seule une vraie morsure compte.

```python
from matplotlib.transforms import Bbox
boxes = [(t.get_text()[:40], t.get_window_extent(renderer=r)) for t in fig.texts]
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        (na, a), (nb, b) = boxes[i], boxes[j]
        inter = Bbox.intersection(a, b)
        if inter is None:
            continue
        share = (inter.width * inter.height) / min(a.width * a.height, b.width * b.height)
        assert share < 0.12, 'chevauchement %.0f%% : %r / %r' % (share * 100, na, nb)
```

### 4. Les `$` sont échappés

**Deux `$` non échappés dans une même chaîne basculent tout le texte intermédiaire
en mathtext**, rendu en italique mathématique, espacement cassé, sans le moindre
avertissement. C'est le piège le plus vicieux de la liste parce qu'il ne frappe
que les visuels en dollars, et qu'une killer phrase du type
`"Refunds averaged $0.4bn a month. In June the Treasury paid back $49.2bn."`
part entièrement en italique : le lecteur voit une phrase bizarre, pas une erreur.

Dans une chaîne Python, écrire `\\$`. Et asserter :

```python
assert '$' not in TEXTE.replace('\\$', ''), 'dollar non échappé : %r' % TEXTE
```

Le même piège existe sur les libellés d'axe construits à la volée : un
`'$%d bn' % v` isolé passe, deux `$` dans le même libellé basculent.

### 5. Le pied de source ne mord pas le watermark (ajouté le 16/09/2026)

La troisième assertion tolère 12 % de recouvrement de la plus petite boîte,
et c'est le bon seuil pour deux lignes empilées. Mais sur une ligne de sources
longue, une morsure de fin de ligne sur le watermark reste sous 12 % de la boîte
du watermark et passe. Vu sur R6, chart ladder FR : « …rendement total du
marché US)Eco3min Research ». Asserter l'ordre horizontal, pas seulement le
recouvrement.

```python
foot = [t for t in fig.texts if t.get_text().startswith('Sources')]
wm = [t for t in fig.texts if t.get_text().startswith('Eco3min Research')]
if foot and wm:
    assert foot[0].get_window_extent(renderer=r).x1 < wm[0].get_window_extent(renderer=r).x0 - 8,         'the source line runs into the watermark'
```

Même famille que le garde étendu aux graduations et libellés d'axe (R2, R4) :
chaque niveau de texte oublié par le balayage se rejoue.

### Bonus, même famille : les glyphes hors ASCII

IBM Plex Mono n'a **ni U+2009 ni U+202F**. Une espace fine insécable dans un
« 2 499 » à la française est rendue par une police de substitution, en silence.
Le contrôle le moins coûteux est de rester en ASCII dans tout texte de visuel et
de l'asserter ; sinon, vérifier le cmap de la police demandée pour chaque
caractère non ASCII.

```python
for t in list(fig.texts) + list(ax.texts):
    assert t.get_text().isascii(), 'glyphe hors ASCII, vérifier le cmap : %r' % t.get_text()
```

---

## 8. Copyright et droits visuels

**Interdit**
- Logos de médias concurrents (Bloomberg Terminal, TradingView, Refinitiv Eikon, Koyfin)
- Captures d'écran d'articles tiers, de pages web, de newsletters
- Images générées contenant marques, logos, personnages IP (Disney, Marvel, mascottes de banques, etc.)
- Reproduction de graphiques publiés ailleurs (FT, Bloomberg, etc.) — toujours reproduire à partir des données brutes
- Photos de personnalités identifiables sans droits
- Sheet music, paroles de chansons (cas rare mais peut survenir en illustration d'article culturel/économique)

**Autorisé**
- Données brutes des sources publiques (FRED, BCE, INSEE, BRI, etc.) — c'est de la donnée, pas de l'image protégée
- Graphiques produits par Eco3min à partir de ces données (output original)
- Visuels génératifs créés en propre, à condition d'être originaux et de ne reproduire aucune IP identifiable

**Données fournisseurs payants** (Bloomberg, Refinitiv, S&P) : vérifier les droits d'usage avant publication. Souvent licence personnelle, redistribution interdite.

---

## 9. Critère de publication d'un visuel

Avant chaque publication, poser ces questions :

- Le visuel apporte-t-il **quelque chose que le texte seul ne fournit pas** (forme, échelle, dynamique, comparaison) ? Si la même information passe mieux dans une phrase, supprimer le visuel.
- Le visuel est-il **compréhensible en standalone** (sans lire l'article) ? Titre, source, axes lisibles, légende suffisante.
- Le visuel **survit-il à un repartage hors contexte** (capture sur X, AI Overview) avec sourcing et attribution intacts ?
- Le visuel est-il **distinctif** ? Si un lecteur aurait pu trouver exactement le même graphique dans la presse généraliste, il n'apporte rien à Eco3min.

---

## 10. Checklist pré-publication

**Conformité AMF visuelle**
- [ ] Aucune flèche achat/vente
- [ ] Aucune zone colorée prescriptive
- [ ] Aucune cible de prix matérialisée
- [ ] Scénarios prospectifs au pluriel + cadrés comme hypothétiques
- [ ] Allocations descriptives sourcées, jamais recommandées
- [ ] Comparaisons géographiques en chiffres neutres, sans ranking normatif
- [ ] Aucune annotation de timing actionnable

**Sourcing**
- [ ] Source intégrée dans le visuel (institution + date)
- [ ] Mention Eco3min discrète mais présente
- [ ] Date d'extraction si donnée vivante
- [ ] Format conforme à `brand-kit-eco3min` section 6

**Conformité brand kit**
- [ ] Typographie : Source Serif 4 + Inter + IBM Plex Mono (cf. `brand-kit-eco3min` section 1)
- [ ] Fond = un des 3 registres (`brand-kit-eco3min` §2.2), choix justifié
- [ ] Mode chromatique identifié (sobre / catégoriel / gradient — `brand-kit-eco3min` §5.2)
- [ ] Mode sobre : accent terracotta `#B85C3C` à 1 occurrence maximum
- [ ] Mode catégoriel : rangs §2.5 dans l'ordre, ≤6-7 séries, labels directs en bout de ligne (pas de légende détachée)
- [ ] Si régime nommé : code régime utilisé (cf. `brand-kit-eco3min` section 3)
- [ ] Aucune teinte ad hoc inventée

**Data viz**
- [ ] Type de chart adapté à la donnée (pas de pie chart, pas de 3D)
- [ ] Échelle d'axe Y justifiée (zéro pour bar, libre pour line, log si nécessaire)
- [ ] Unités explicites sur tous les axes
- [ ] Période cadrée dans le titre
- [ ] Annotations contextuelles si pertinentes (récessions, événements)

**Cohérence**
- [ ] Tous les chiffres du visuel matchent les chiffres du texte
- [ ] Périodes identiques entre texte et visuel
- [ ] Sources identiques

**Qualité technique**
- [ ] Aucun chevauchement, aucune troncature
- [ ] Aucune faute d'orthographe (accents sur majuscules inclus)
- [ ] Lisibilité en miniature testée (pour exports sociaux)
- [ ] Contraste suffisant
- [ ] Résolution suffisante (SVG ou PNG ≥2x)
- [ ] Si rendu Playwright : polices réellement chargées, vérifiées à l'œil sur le premier visuel de la série (cf. §7 bis)

**Copyright**
- [ ] Aucun logo média tiers
- [ ] Aucune capture de graphique tiers reproduite
- [ ] Aucun élément IP non libre
- [ ] Si données fournisseur payant, droits vérifiés

**Critère final**
- [ ] Le visuel apporte quelque chose que le texte ne fournit pas
- [ ] Le visuel est compréhensible en standalone

---

## Versioning

- **v1.0** (création initiale) — corpus de règles AMF, sourcing, data viz, qualité technique. Philosophie initiale : « aucune charte graphique imposée ».
- **v1.1** (mai 2026) — alignement avec `brand-kit-eco3min v1.0`. La philosophie est révisée : le minimum commun (typo, palette, codes régime, accent) est désormais fourni par le brand kit ; ce skill garde son rôle de référence sur les règles de fond (AMF, sourcing, qualité, choix de chart). Aucune règle de fond modifiée.
- **v1.2** (juillet 2026) — alignement avec `brand-kit-eco3min v1.1` (diversité chromatique contrôlée). Ajouts : famille de charts multi-entités (palette catégorielle §2.5) + pattern spaghetti focus au tableau de choix ; règle générale de direct labeling en bout de ligne, légende détachée bannie ≤6 séries ; checklist mise à jour (3 registres de fond, mode chromatique). Aucune règle AMF, sourcing ou qualité modifiée.
- **v1.3** (septembre 2026) — ajout du §7 bis « Rendu PNG — recette Playwright » : séquence de chargement des polices, auto-ajustement de titre, SVG inline. Extrait du projet « repair image », où cette connaissance était piégée depuis la V3. Aucune règle AMF, sourcing ou qualité modifiée.
- **v1.5** (16 septembre 2026, étude R6) — §7 ter, cinquième assertion : la ligne de sources se termine avant le watermark (test d'ordre horizontal, le seuil de 12 % laissant passer une morsure de fin de ligne). Aucune règle modifiée.
- **v1.4** (septembre 2026, cycle 20 Chart of the Week) — ajout du §7 ter « Rendu matplotlib — quatre assertions avant `savefig` » : repli de police, débordement de canvas, chevauchement des textes d'en-tête, échappement des `$` (mathtext), plus le garde ASCII sur le cmap. Le §7 bis ne couvrait que le chemin Playwright ; les charts matplotlib ont leurs propres échecs silencieux, et les trois premières assertions ont chacune attrapé un défaut réel sur un script écrit par quelqu'un qui connaissait le piège. Le point U+202F d'IBM Plex Mono, jusqu'ici seulement en mémoire de projet, trouve ici son foyer. Aucune règle AMF, sourcing ou qualité modifiée.

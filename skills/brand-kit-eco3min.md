---
name: brand-kit-eco3min
description: Système de design Eco3min v1.1 — palette, typo, codes régime, palette catégorielle, fonds — pour toute production visuelle (heros, charts, illustrations, datasets, social). Activer pour toute création ou révision d'un visuel Eco3min, FR ou EN. Socle figé : 3 familles typo (Source Serif 4 + Inter + IBM Plex Mono), 3 registres de fond (crème #F8F5EE défaut / blanc majeurs et charts denses / charcoal inversé), accent terracotta #B85C3C, sourcing 2 lignes mono, watermark. v1.1 : palette catégorielle 7 rangs dérivée des familles régime, pour TOUTE série nommée (pays, actifs, secteurs, époques), plus seulement les régimes ; identité par la structure, variété par la couleur ; terracotta = unicité en mode sobre, rang 1 en catégoriel ; direct labeling en bout de ligne. Définit 6 codes régime sur 2 axes (macro/monétaire), 3 teintes chacun, priorité sémantique sur les rangs. Combiner avec visuels-eco3min (AMF, sourcing, qualité).
---

# Brand kit Eco3min v1.1

> Système de design pour la production visuelle d'Eco3min. Document de référence amont — toutes les productions visuelles (heros piliers, charts, illustrations, datasets, social) s'y conforment.
>
> **Philosophie** : un minimum commun figé (typo + sourcing + watermark + chrome de chart) qui garantit la cohérence perçue, des libertés encadrées sur le reste (type de chart, densité, intensité chromatique, fond, format) qui préservent la diversité éditoriale. Un lecteur de r/economics doit voir « 4 angles d'analyse, même publication » — pas « 4 charts identiques ».
>
> **Doctrine v1.1 — identité par la structure, variété par la couleur.** L'autorité visuelle des références du genre (OWID, FT, Urban Institute) ne vient pas d'une monochromie : elle vient d'un **chrome de chart uniforme** (typographie, hiérarchie titre/sous-titre, footer source, attribution, direct labeling) appliqué à des palettes catégorielles variées mais sourdes. Chez Eco3min, le squelette invariant est : les 3 familles typo, le sourcing footer 2 lignes mono, le watermark, les règles AMF. La couleur, le fond et le format sont des axes de variété **encadrés** — la monotonie chromatique est un défaut au même titre que l'incohérence de marque. Corollaire : le mode « charcoal + 1 terracotta » est UN registre parmi trois (voir §5.2), pas le défaut universel.

---

## 1. Typographie — 3 familles fixes

### 1.1 Serif éditorial : Source Serif 4

**Usage** : titres, sous-titres italiques, titres descriptifs de métrique, citations.

**Pourquoi** : dessin moderne, large amplitude de poids (200 à 900), excellent rendu à toute taille, italic distinctif qui sert les sous-titres analytiques. Téléchargeable gratuitement sur Google Fonts.

**Configurations canoniques** :
- Titre principal hero : 38–48 px, weight 600
- Sous-titre italique éditorial : 17–22 px, weight 400, italic
- Titre descriptif métrique (en small multiples) : 14–16 px, weight 500
- Citations en blockquote : 18–22 px, weight 400, italic

**Fallback chain CSS** : `"Source Serif 4", "Source Serif Pro", Georgia, "Times New Roman", serif`

### 1.2 Sans-serif : Inter

**Usage** : annotations chiffrées dans le chart, labels d'axes, légendes, callouts de données, texte de UI sur les visuels riches (Affordability matrix, etc.).

**Pourquoi** : optimisé pour les écrans ET le print, lisibilité parfaite à petite taille (12 px), chiffres tabulaires disponibles (`font-variant-numeric: tabular-nums`).

**Configurations canoniques** :
- Annotations chiffrées (« $3.05 remaining », « 2019 peak: 51% ») : 11–13 px, weight 500
- Labels d'axes : 10–11 px, weight 400
- Légendes : 11–12 px, weight 400
- Callouts d'événement (« mars 2020 — COVID ») : 11 px, weight 500

**Chiffres tabulaires obligatoires** sur les axes (sinon les alignements verticaux dansent).

**Fallback chain CSS** : `Inter, "Helvetica Neue", Arial, -apple-system, BlinkMacSystemFont, sans-serif`

### 1.3 Monospace : IBM Plex Mono

**Usage** : codes de série (FRED `DFII10`, ICE `BAMLH0A0HYM2`), sources en pied de visuel, captions, labels catégoriels uppercase (`PROPRIÉTÉ 01 · COÛT DU CAPITAL`), tags piliers (`PILIER 03 / 10`).

**Pourquoi** : signature visuelle d'Eco3min — la ligne sources en mono uppercase est ton trait distinctif le plus reconnaissable. Plex Mono est plus chaud qu'un courrier monospace générique.

**Configurations canoniques** :
- Sources footer ligne 1 : 9–10 px, weight 400, letter-spacing 0.5
- Sources footer ligne 2 (méthodo) : 9 px, weight 400, letter-spacing 0.5
- Labels catégoriels uppercase : 10–11 px, weight 500, letter-spacing 1.2–2.5
- Tag pilier / numéro : 10 px, weight 500, letter-spacing 1.5
- Codes série dans le chart : 9–10 px, weight 400

**Casse** : uppercase systématique pour labels catégoriels et tags. Sentence case ou mixte pour le contenu des sources.

**Fallback chain CSS** : `"IBM Plex Mono", "SF Mono", Menlo, Consolas, monospace`

### 1.4 Dualité web vs export — assumée

Le site web (CSS v3.4) utilise une autre triade : **Libre Baskerville + DM Sans + JetBrains Mono**. Cette dualité est volontaire et documentée :

- Le web a ses contraintes (chargement, hinting écran, accessibilité) — Libre Baskerville et DM Sans y sont plus performants.
- Les visuels exportés ont les leurs (compression PNG/WEBP, lisibilité au repartage) — Source Serif 4, Inter, Plex Mono y sont supérieurs.

Aucune règle ne demande d'unifier. Si une refonte typographique globale est décidée plus tard (par exemple lors d'une collaboration designer), on basculera des deux côtés en même temps. D'ici là, la dualité est un trait d'usage, pas une dette.

---

## 2. Palette principale

### 2.1 Couleurs neutres

| Rôle | Hex | Usage |
|---|---|---|
| Charcoal | `#1A1A1A` | Texte primaire, traits de séries principales |
| Gris medium | `#757575` | Texte secondaire, séries d'arrière-plan, labels d'axes |
| Gris light | `#C4C4C4` | Lignes de grille, séparateurs, bordures discrètes |
| Gris très light | `#E0E0E0` | Zones secondaires ombrées, axes |
| Filet crème | `#DED7C7` | Cadre en inset des heros d'article (V3), séparateurs sur fond crème. Neutre **chaud**, accordé au fond crème, là où les quatre gris ci-dessus sont neutres froids |

### 2.2 Fond — 3 registres officiels (v1.1)

| Registre | Hex | Usage |
|---|---|---|
| Crème éditorial | `#F8F5EE` | **Défaut** : heros piliers, **heros d'article (V3)**, charts d'articles, datasets, illustrations — cohérent avec le web |
| Blanc pur | `#FFFFFF` | **Convention gravée : fond des heros MAJEUR** (cf. `production-hero-majeur`). Aussi : charts à richesse chromatique élevée (palette catégorielle ≥4 séries, heatmaps, matrices) qu'un fond teinté écraserait — registre « academic working paper » |
| Charcoal inversé | `#1A1A1A` | Formats spéciaux assumés : Time Machine, certains cycles chart-of-the-week (registre « terminal ») — usage parcimonieux, jamais pour la série des heros piliers |

Le fond crème reste le défaut. Le blanc signale un majeur ou un chart chromatiquement dense. Le charcoal inversé est un registre d'exception délibéré (texte crème/gris light dessus, contraste vérifié). Ces 3 registres remplacent les doctrines de fond divergentes qui coexistaient entre `production-hero-majeur` (blanc), `production-chart-of-the-week` (fond libre) et ce brand kit (crème) — ils sont désormais la référence commune des trois skills.

### 2.3 Accent terracotta

| Rôle | Hex | Usage |
|---|---|---|
| Accent terracotta | `#B85C3C` | Double rôle selon le mode chromatique (voir §5.2). **Mode sobre** : UN marqueur principal par chart (ligne verticale, point annoté, OU zone — pas plusieurs simultanément) + son label nominal éventuel. **Mode catégoriel** : couleur du rang 1 de la palette catégorielle (§2.5) — la série focus/principale. |

**Règle stricte de non-cluster (mode sobre)** : si tu peux retirer 2 occurrences de terracotta sans dégrader la lecture de la thèse, elles dispersent l'accent — retire-les. Empiriquement validé sur 3 piliers livrés (mai 2026) : 1 ligne terracotta isolée a plus d'impact que 5 occurrences cluster, même cohérentes éditorialement.

**Portée de la règle d'unicité (clarifiée v1.1)** : l'unicité vaut pour le terracotta **en rôle d'accent** (mode sobre : 1 série + 1 marqueur). En mode catégoriel, le terracotta est une couleur de série au même titre que les autres rangs — une ligne terracotta complète sur un chart 5 séries n'est pas un « cluster ». En revanche, même en mode catégoriel, un chart à thèse doit désigner UN focus visuel (la série terracotta, ou un marqueur unique), pas cinq.

### 2.5 Palette catégorielle Eco3min — 7 rangs (NOUVEAU v1.1)

Palette générale pour tout chart distinguant **N séries nommées** : pays, actifs, secteurs, scénarios, époques, indicateurs. Elle est **dérivée des teintes « ligne » des familles régime** (§3) — donc zéro teinte nouvelle, cohérence automatique avec tous les visuels régime existants. Elle n'est **plus réservée aux régimes nommés** : c'est la levée de la restriction v1.0 qui produisait la monotonie « charcoal + 1 accent » sur ~90 % des visuels.

| Rang | Nom | Hex | Note |
|---|---|---|---|
| 1 | Terracotta | `#B85C3C` | Série focus / principale — toujours en premier |
| 2 | Bleu acier | `#4A6B8A` | Paire par défaut avec le rang 1 (contraste daltonisme-safe) |
| 3 | Vert sourd | `#6B8E5F` | |
| 4 | Violet pourpre | `#6B4A6B` | |
| 5 | Ocre sourd | `#B8854A` | |
| 6 | Charcoal doux | `#4A3F3D` | |
| 7 | Rouge sourd | `#C73E2E` | Dernier rang délibéré : proximité perceptuelle avec le terracotta — n'entre en jeu qu'à N=7 ou en remplacement sémantique (régime inflationniste) |

**Règles d'usage** :
- **Priorité sémantique des codes régime** : si une série EST un régime nommé (dans le titre, la légende ou le label), elle prend la couleur de son code régime (§3), quel que soit son rang. Les autres séries prennent les rangs restants dans l'ordre.
- **Ordre des rangs respecté** : un chart à 3 séries utilise les rangs 1-2-3, pas une sélection ad hoc. Garantit qu'un chart 2 séries et un chart 5 séries du même article restent cohérents entre eux.
- **Plafond : 6-7 séries distinctes.** Au-delà, basculer en pattern « spaghetti focus » : N séries en gris light `#C4C4C4`/medium `#757575` en arrière-plan + 1-2 séries accentuées aux rangs 1-2.
- **Direct labeling obligatoire (≤6 séries)** : chaque série est labellisée en bout de ligne dans sa couleur (mécanique OWID/FT). Légende détachée bannie — elle force des allers-retours et casse la lecture 5 secondes. Détail dans `visuels-eco3min` §3.
- **Garde-fou daltonisme** : rouge `#C73E2E` et vert `#6B8E5F` ne doivent jamais être la SEULE distinction entre deux séries adjacentes ou entrelacées — le direct labeling est le filet, mais espacer les rangs si possible. Paire par défaut pour 2 séries : terracotta + bleu acier.
- **Zones pâles associées** : pour les aplats/aires d'une série, utiliser la teinte « zone » de la famille régime correspondante (§3) — ex. aire sous une ligne bleu acier `#4A6B8A` → zone `#D8E2EC`.
- **Saturation** : la palette reste sourde (FT/Bloomberg). Aucune teinte pop, aucun néon, aucune couleur ad hoc hors de ces 7 rangs + neutres + codes régime.

### 2.4 Couleurs secondaires éditoriales (web uniquement, pas en visuel)

| Rôle | Hex | Notes |
|---|---|---|
| Navy éditorial | `#1A237E` | Liens, titres bleus sur le web. **Pas utilisé dans les visuels exportés.** |
| Or éditorial | `#C9A84C` | Soulignement menu sur le web, séparateurs Q&A. **Pas utilisé dans les visuels exportés.** |

Ces deux teintes existent dans le CSS v3.4 mais sont réservées aux composants UI du site. Un chart Eco3min ne doit pas en contenir, pour éviter la confusion entre identité éditoriale (texte web) et identité analytique (data viz).

---

## 3. Codes couleurs régime — 6 codes sur 2 axes

Chaque code régime se décline en 3 teintes pour 3 usages canoniques dans un chart :
- **Zone** : couleur de fond/rectangle ombré (saturation faible, opacité haute) pour marquer la période du régime
- **Ligne** : couleur intermédiaire pour les bordures, lignes verticales de transition, courbe principale du régime
- **Label** : couleur foncée pour le texte du nom du régime (lisible sur fond crème ou blanc)

### 3.1 Axe macro

#### Inflationniste — famille rouge sourd

| Teinte | Hex | Usage |
|---|---|---|
| Zone | `#F4DDD8` | Rectangle ombré pour la période inflationniste (cf. ton Image 1 : zones WWI, WWII, Great Inflation, post-COVID) |
| Ligne | `#C73E2E` | Délimitation, courbe principale d'un chart d'inflation |
| Label | `#8B2A1F` | Texte du nom (« WWI: +21% », « Great Inflation 1970s ») |

#### Désinflationniste — famille bleu acier

| Teinte | Hex | Usage |
|---|---|---|
| Zone | `#D8E2EC` | Rectangle ombré pour la période désinflationniste (typiquement 1985–2020) |
| Ligne | `#4A6B8A` | Délimitation, courbe principale |
| Label | `#2D4256` | Texte du nom |

#### Stagflation — famille ocre sourd

| Teinte | Hex | Usage |
|---|---|---|
| Zone | `#ECE2D2` | Rectangle ombré pour la période stagflation (typiquement 1973–1982) |
| Ligne | `#B8854A` | Délimitation |
| Label | `#6E4E2B` | Texte du nom |

### 3.2 Axe monétaire

#### Liquidité abondante — famille vert sourd

| Teinte | Hex | Usage |
|---|---|---|
| Zone | `#DCE5D6` | Rectangle ombré pour la période de liquidité abondante (QE, 2009–2021) |
| Ligne | `#6B8E5F` | Délimitation |
| Label | `#3E5536` | Texte du nom |

#### Restriction — famille violet pourpre

| Teinte | Hex | Usage |
|---|---|---|
| Zone | `#DDD4DD` | Rectangle ombré pour la période de restriction monétaire (QT, hausses de taux) |
| Ligne | `#6B4A6B` | Délimitation |
| Label | `#3E2A3E` | Texte du nom |

#### Crise systémique — famille charcoal

| Teinte | Hex | Usage |
|---|---|---|
| Zone | `#D8D5D3` | Rectangle ombré pour la période de crise (2008–2009, mars 2020, etc.) |
| Ligne | `#4A3F3D` | Délimitation |
| Label | `#1F1A18` | Texte du nom |

### 3.3 Logique de design des familles

- **Macro** : axe chromatique chaud → froid (rouge inflationniste → ocre stagflation → bleu désinflationniste). Lecture intuitive de la « température » du régime.
- **Monétaire** : axe abondance → contraction → rupture (vert liquidité → violet restriction → noir crise).
- **Saturation** : toutes les familles sont sourdes (jamais des couleurs pop). C'est la cohérence FT/Bloomberg.
- **Évitement de collision** : aucun code régime n'est sur la teinte exacte du terracotta accent `#B85C3C`. L'inflationniste `#C73E2E` est plus rouge, plus saturé — l'œil les distingue.

### 3.4 Règle d'usage

**Si le visuel nomme explicitement un régime dans son texte** (titre, sous-titre, annotation, légende), il **doit** utiliser la couleur de ce régime. Ne pas inventer une teinte ad hoc.

**Si le visuel ne nomme pas de régime**, la palette catégorielle §2.5 s'applique pour toute série nommée, et les règles générales (section 5) pour le reste. (v1.1 : la restriction « multi-couleurs réservée aux régimes nommés » est levée — c'est elle qui verrouillait la diversité chromatique du site.)

**Cas particulier des charts qui mobilisent plusieurs régimes simultanément** (ex : un chart historique des cycles de taux qui distingue 4 régimes successifs) : utiliser le code de chaque régime pour sa portion respective. Cohérence garantie avec d'autres visuels du site qui invoqueraient les mêmes régimes individuellement.

---

## 4. Formats canoniques par type de visuel

| Type de visuel | Ratio | Dimensions | Usage |
|---|---|---|---|
| Hero pilier | 16:9 | 1536×864 | Toutes les pages piliers (skill `production-hero-pilier`) |
| Hero d'article (V3) | 1.91:1 | 1200×630 | Articles courants et satellites (skill `production-hero-article-eco3min`) |
| Chart of the week (Reddit DIB) | Variable | Souvent 1200×675 ou 1600×900 | Production hebdomadaire viral (skill `production-chart-of-the-week`) |
| Chart d'article majeur / étude | Variable | Adapté au contenu | Études, research pages |
| Chart d'article satellite | Variable | Embedded width WordPress (~720 px) | Articles courants |
| Image sociale (LinkedIn, X) | 16:9 ou 1.91:1 | 1200×675 | Distribution social |
| Image sociale (Instagram, X carré) | 1:1 | 1080×1080 | Distribution social carrée |
| Dataset page chart | Variable | Embedded responsive | Pages dataset (skill `production-dataset`) |

**Note** : les deux formats de hero sont stricts — **1536×864** pour les piliers et les majeurs, **1200×630** pour les heros d'article. Ils alimentent des gabarits WordPress et des cartes de partage : y déroger casse le cadrage en aval. Pour tout le reste, les dimensions sont libres ; ce qui compte est le ratio et la lisibilité au repartage.

---

## 5. Règles d'usage (libertés encadrées)

### 5.1 Type de chart

**Libre** selon ce qui sert la donnée. Pas de hiérarchie de prestige : un histogram peut être plus juste qu'un line chart, une heatmap peut être plus juste qu'une matrice de bars.

**Inspiration des références internes Eco3min (mai 2026)** :
- Line chart minimaliste avec zones ombrées (US Inflation 113 Years) → standard sobre, idéal pour les séries longues à régimes
- Line chart + spread sur double axe Y (BBB-ification) → exception au principe « jamais double axe », autorisée si les deux séries sont fortement corrélées et si la légende le mentionne
- Heatmap avec gradient continu (Affordability Matrix) → autorisée pour coder une dimension continue
- Kernel density / ridge plot (Spread WTI–Brent) → idéal pour comparer des distributions par catégorie

Pour les règles fines de choix de chart selon la donnée, voir le skill `visuels-eco3min` section 3.

### 5.2 Densité chromatique — 3 modes (révisé v1.1)

**Mode sobre** (charcoal + 1 accent terracotta) : pour les charts à 1 série et les visuels dont la thèse tient dans UN moment/marqueur. Ce n'est **plus le défaut universel** — c'est le mode adapté aux données mono-série.

**Mode catégoriel** (palette §2.5) : dès que le chart distingue N séries ou catégories **nommées** — régimes, ères, scénarios, mais aussi pays, actifs, secteurs, indicateurs. C'est le mode naturel des comparaisons multi-entités (le format signature OWID/FT), historiquement sous-utilisé chez Eco3min.

**Gradient continu** : quand le chart code une dimension continue (intensité, score, prix, accessibilité). Jamais pour distinguer des catégories.

**Anti-monotonie (règle de série)** : au sein d'une même famille de visuels (série des heros piliers, cycles chart-of-the-week, charts d'un même cluster), ne pas enchaîner plus de 2-3 productions consécutives dans le même mode chromatique. La rotation opérationnelle est codée dans les skills de production (`production-hero-pilier` rotation bloquante, `production-chart-of-the-week` ÉTAPE 3-BIS).

### 5.3 Annotations

**Recommandées** :
- Récessions NBER : zones grises light (`#E0E0E0` avec opacité 30-50 %)
- Événements clés : annotations texte datées, en Inter 11 px weight 500
- Moyennes historiques : ligne horizontale pointillée gris medium avec label
- Régimes nommés : zones ombrées en couleur du code régime

**Interdites** :
- Flèches achat/vente
- Zones « buy/sell zone »
- Cibles de prix matérialisées
- Annotations de timing actionnable
- Symboles ↗ ↘ sans contexte numérique

Cf. checklist AMF complète dans `visuels-eco3min` section 2.

### 5.4 Accent terracotta — la règle critique

**En mode sobre : 1 occurrence par chart** (1 ligne verticale, OU 1 point annoté, OU 1 zone unique). Son label nominal peut être en terracotta (il complète le marqueur, il ne le duplique pas). En mode catégoriel (§2.5), le terracotta est la couleur pleine de la série rang 1 — l'unicité ne s'applique pas à la série, mais le chart garde UN focus visuel.

**Anti-pattern cluster** : 4–5 occurrences de terracotta sur des éléments connexes (ligne + zone + label-régime + bullet décoratif + label-chiffre) sous prétexte de « cohérence narrative ». Empiriquement, ça dilue l'impact.

**Test** : si tu peux retirer 2 occurrences sans dégrader la lecture de la thèse, retire-les.

---

## 6. Sourcing intégré au visuel — format obligatoire

**Position** : pied de visuel, généralement bas-droite ou bas-centre.

**Format à 2 lignes** (canon hero pilier) :

```
Ligne 1 — Sources: [Institution] ([codes série]); [Institution] ([série]); …
Ligne 2 — Updated [mois année] · [méthodologie résumée en 1 ligne] · Values rounded for readability
```

**Format à 1 ligne** (charts moins denses, social) :

```
Sources: [Institution] ([codes série]) · Chart: Eco3min Research — [mois année]
```

**Typo** : IBM Plex Mono, 9–10 px, gris medium `#757575`, letter-spacing 0.5.

**Casse** : sentence case dans le contenu des sources. Le mot « Sources » initial peut être en regular ou en uppercase selon densité.

**Mention Eco3min obligatoire** : « Chart: Eco3min Research » OU « Eco3min Research » seul. Toujours présent, même discret. Survit au repartage hors contexte (capture X, AI Overview).

**Date** : si donnée vivante, inclure date d'extraction (« data as of May 12, 2026 »). Si donnée stable, mois + année suffisent.

---

## 7. Watermark Eco3min

**Position** : bas-gauche standard, ou bas-droite si le sourcing prend la gauche.

**Texte** : `Eco3min — Research` ligne 1, URL de la page ligne 2 (si applicable, sur heros piliers et études).

**Typo** : IBM Plex Mono, 9–10 px, gris medium.

**Pas de logo géant** : l'attribution, pas le branding.

---

## 8. Anti-patterns visuels (non négociables)

Renvoi au skill `visuels-eco3min` section 2 (7 interdictions AMF), section 3 (anti-patterns data viz : pas de 3D, pas de pie chart au-delà de 3 segments, pas de gradient décoratif), section 7 (qualité technique).

Ces règles sont gravées et indépendantes du brand kit — elles s'appliquent à tout visuel Eco3min.

---

## 9. Articulation avec les autres skills

| Skill | Relation au brand kit |
|---|---|
| `production-hero-pilier` | Implémentation stricte du brand kit pour la série des ~10 piliers. La règle « accent terracotta unique » du skill devient une règle générale du brand kit. |
| `production-hero-article-eco3min` | Spécialise le brand kit pour le troisième registre de hero (article, 1200×630, crème, cadre `#DED7C7`). Le brand kit reste la source de vérité charte. |
| `visuels-eco3min` | Conserve les règles AMF, sourcing, qualité technique, choix de chart. Le brand kit fournit le minimum commun (typo + palette + codes régime) qu'il imposait précédemment de façon variable. |
| `formats-eco3min` | Indépendant. Aucun chevauchement (HTML/structurel). |
| `production-chart-of-the-week` | La **typo** reste obligatoire (signature cross-canal). Le **fond** se choisit parmi les 3 registres §2.2 (crème / blanc / charcoal inversé) selon le registre éditorial du cycle. La **palette du chart** est libre par registre (règle de diversité propre au skill), avec la palette catégorielle §2.5 comme port d'attache par défaut ; seuls les éléments récurrents (watermark, sourcing) restent fixés. Résout la contradiction v1.0 (« fond crème obligatoire » vs sa propre règle de diversité de palette). |
| `production-research-study`, `production-dataset`, `production-q-and-a` | Indépendants pour le contenu textuel (suivent `editeur-eco3min`). Pour les visuels qu'ils contiennent, ils suivent le brand kit. |

---

## 10. Checklist pré-livraison d'un visuel

**Typographie**
- [ ] Source Serif 4 utilisé pour titre / sous-titre
- [ ] Inter utilisé pour annotations et chiffres
- [ ] IBM Plex Mono utilisé pour sources et codes série
- [ ] Pas d'autre famille de polices

**Palette**
- [ ] Fond = un des 3 registres §2.2 (crème défaut / blanc / charcoal inversé), choix justifié par la famille de visuel
- [ ] Texte primaire en charcoal `#1A1A1A` (ou crème sur fond charcoal inversé)
- [ ] Mode chromatique identifié : sobre / catégoriel / gradient (§5.2)
- [ ] Mode sobre : accent terracotta `#B85C3C` à 1 occurrence MAX
- [ ] Mode catégoriel : rangs de la palette §2.5 respectés dans l'ordre, ≤6-7 séries, direct labeling en bout de ligne
- [ ] Si régime nommé : couleur du code régime utilisée (priorité sémantique sur les rangs)
- [ ] Rouge `#C73E2E` / vert `#6B8E5F` jamais seule distinction entre 2 séries adjacentes
- [ ] Aucune teinte ad hoc inventée hors rangs, neutres et codes régime

**Sourcing**
- [ ] Source intégrée dans le visuel (pied)
- [ ] Codes série explicites (pas seulement « Federal Reserve »)
- [ ] Mention « Eco3min Research » ou équivalent
- [ ] Date d'extraction si donnée vivante

**Anti-patterns AMF**
- [ ] Aucune flèche achat/vente
- [ ] Aucune cible de prix
- [ ] Aucune zone prescriptive
- [ ] Annotations descriptives uniquement

**Qualité technique**
- [ ] Aucun chevauchement texte / texte / courbe
- [ ] Aucune troncature
- [ ] Lisibilité testée à 380 px de largeur (mobile feed)
- [ ] Accents corrects sur majuscules (« É », « À »)

---

## Versioning

- **v1.0** (mai 2026) — première formalisation après audit transversal des 3 skills design existants (`production-hero-pilier`, `visuels-eco3min`, `formats-eco3min`) et observation de la diversité visuelle déjà en place (US Inflation 113 Years, BBB-ification, Affordability Matrix, Spread WTI-Brent).
- **v1.1** (juillet 2026) — « diversité chromatique contrôlée », après audit anti-monotonie (constat : ~90 % des visuels en mode charcoal + 1 terracotta, heros piliers convergents ; cause racine : palette catégorielle verrouillée sur les régimes nommés). Changements : (1) palette catégorielle générale à 7 rangs (§2.5) dérivée des familles régime — aucune teinte nouvelle ; (2) 3 registres de fond officiels (§2.2), convention « blanc = hero majeur » gravée ; (3) doctrine « identité par la structure, variété par la couleur » (mécaniques OWID/FT : chrome uniforme + palettes catégorielles + direct labeling) ; (4) règle terracotta clarifiée (unicité = mode sobre uniquement) ; (5) mode sobre déclassé de défaut universel à mode adapté mono-série ; (6) contradiction fond/palette avec `production-chart-of-the-week` résolue. Le squelette identitaire (typo, sourcing, watermark, AMF, saturation sourde) est inchangé — c'est lui qui a gagné les citations FT Alphaville / Ritholtz, il ne bouge pas.
- **v1.2** (septembre 2026) — intégration du registre « hero d'article » (V3), qui tournait en production hors brand kit : format 1200×630 gravé au §4, token de filet crème `#DED7C7` ajouté au §2.1, fond crème étendu explicitement à ce registre au §2.2. Aucune règle existante modifiée.

À actualiser quand :
- Une nouvelle famille de visuel demande une convention non prévue
- Une mauvaise lisibilité émerge sur un code régime particulier
- Un brand kit étendu (illustration, motion, print) devient nécessaire

---

## Note d'usage interne

Ce skill définit le brand kit Eco3min v1.0. Pour la voix éditoriale, voir `editeur-eco3min`. Pour les règles AMF data viz et qualité technique, voir `visuels-eco3min`. Pour les patterns spécifiques aux heros piliers, voir `production-hero-pilier`. Pour les charts viraux Reddit, voir `production-chart-of-the-week` — ce dernier ne suit pas la totalité du brand kit (palette du chart libre par registre éditorial, watermark simplifié sur les distributions externes) mais conserve la typographie et choisit son fond parmi les 3 registres §2.2.

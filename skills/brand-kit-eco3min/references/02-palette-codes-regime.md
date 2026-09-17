# brand-kit-eco3min — référence : Palette principale, 3 registres de fond, terracotta, palette catégorielle 7 rangs, couleurs web, 6 codes régime en 3 teintes (§2, §3)

Extrait VERBATIM de SKILL.md (découpage du 17/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée, le chrome canonique §0 et le moment où lire ce fichier.

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

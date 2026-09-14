---
name: production-hero-pilier
description: Production des heros de pages piliers eco3min.fr (~10 piliers, série template-driven). Activer pour toute création ou itération d'un hero de pilier, FR ou EN. Couvre : règle UNE idée visuelle dominante (4 formats : série anchor, comparaison, diagramme conceptuel, small multiples 2x2 — jamais empilés), process 4 étapes, audit data bloquant (couverture période, symétrie N catégories), rigueur métrique (proxy = standard académique du concept), patterns Option SM (labels uppercase, dual-anchor, pillar tag), ROTATION SÉRIE BLOQUANTE v1.2 (jamais 2 piliers consécutifs sur le même format ; max 2 heros consécutifs en mode sobre, alterner avec le mode catégoriel du brand kit ; input = format + mode des 2 derniers heros), AMF, sourcing par codes de série, terracotta (unicité en mode sobre), 3 tests (comptage non-initié, mobile 380px, lecture 5 s). Format 1536x864. Combiner avec brand-kit-eco3min, visuels-eco3min, formats-eco3min, editeur-eco3min, archi-eco3min.
---

# Production — Hero visuel pour page pilier Eco3min

## Mission opérationnelle

Générer le visuel hero placé en tête d'une page pilier de eco3min.fr (site bilingue macro-financier, benchmark éditorial FT / Bloomberg / Les Échos). Ce hero appartient à une série template-driven d'~10 piliers — penser **template transférable**, pas one-off.

## Fonction du hero

- Transmettre LA thèse structurante de la page en **5 secondes**, comprise pleinement en 15-30 secondes.
- Établir la crédibilité data-driven dès le premier regard.
- Rester lisible si partagé seul sur X / LinkedIn / Reddit.
- NE PAS dupliquer le contenu texte de la page — l'**amplifier visuellement**.

---

## Règle bloquante : UNE idée visuelle dominante

Un hero ≠ infographie de manuel. Choisir **UN** format parmi :

**(A) Série temporelle anchor** — un graphique unique (taux, ratio, indice) avec ≤4 annotations descriptives. Données réelles, source citée, axes chiffrés.

**(B) Comparaison binaire/ternaire** — deux ou trois régimes/états mis en regard sur des dimensions quantifiées. Max 4 lignes de comparaison.

**(C) Diagramme conceptuel non-trivial** — ≤7 éléments, relations non-linéaires (boucles, rétroactions, asymétries). Refusé si la structure est une simple chaîne A→B→C.

**(SM) Small multiples 2×2** — grille de 4 mini-charts indépendants partageant le même axe temporel et le même moment-pivot. Chaque cellule = UNE propriété distincte d'un concept structurel multi-dimensionnel. Verticale terracotta cohérente à la même date sur les 4 cellules (redondance contrôlée acceptée : elle sert la thèse « N propriétés convergent »). À choisir UNIQUEMENT quand la thèse mentionne explicitement N propriétés/dimensions distinctes ET qu'aucune métrique unique ne peut capturer le basculement. Layout enrichi spécifique — voir section Layout canonique.

**INTERDIT** : empiler (A) + (B) + (C) + (SM) dans le même visuel. Si hésitation entre formats, demander à Paul de trancher avant de coder.

---

## Règle bloquante : rotation série (anti-monotonie, v1.2)

Les heros piliers forment une **série** — c'est comme série qu'ils sont perçus (page d'accueil, navigation inter-piliers, partages groupés). La monotonie observée sur les premiers piliers livrés (convergence vers l'Option A + mode sobre crème + 1 ligne terracotta) était flaguée comme risque en v1.1 ; elle devient une règle en v1.2.

**Deux rotations obligatoires, vérifiées AVANT l'étape Options** :

1. **Rotation de format** : le format retenu (A / B / C / SM) doit différer de celui du **pilier précédent**. Sur 4 piliers consécutifs, aucun format ne peut apparaître plus de 2 fois. Si la donnée du pilier n'appelle *vraiment* qu'un format déjà utilisé au pilier précédent, le signaler à Paul comme dérogation explicite — jamais trancher en silence.

2. **Rotation de mode chromatique** : pas plus de **2 heros consécutifs en mode sobre** (charcoal + 1 terracotta). Le troisième bascule en **mode catégoriel** (palette `brand-kit-eco3min` §2.5 — pertinent dès que le pilier compare des régimes, des époques, des pays ou des classes d'actifs) ou en gradient si la donnée est continue. Le mode catégoriel n'est pas une baisse de sobriété : c'est le registre FT/OWID des comparaisons multi-entités, saturation sourde inchangée.

**Ce qui ne tourne JAMAIS (squelette identitaire de la série)** : layout 6 zones, fond crème (le blanc et le charcoal inversé sont réservés aux majeurs et formats spéciaux — cf. brand kit §2.2), triade typo, sourcing footer 2 lignes, watermark, tag pilier, direct labeling. La variété se joue dans le format et la couleur À L'INTÉRIEUR de ce squelette — identité par la structure, variété par la couleur.

**Input requis** : format + mode chromatique des 2 derniers heros livrés (cf. section Input attendu). Sans cet input, demander avant de proposer les options.

---

## Process en 4 étapes

### Étape 1 — Thèse + AUDIT DE FAISABILITÉ DATA

**1.1 — Thèse en une phrase.** Identifier en UNE phrase la thèse structurante de la page. Si la page n'a pas de thèse claire et univoque, signaler le problème éditorial AVANT toute production visuelle.

**1.2 — Audit de faisabilité data (étape critique, ne pas sauter).**

- Pour chaque série mobilisable, vérifier qu'elle couvre la période visée par la thèse. Exemple : thèse sur 3 régimes 1990-2026 mais TIPS commencent en 2003 → flaguer.

- Si une série principale ne couvre pas la période complète, proposer une stratégie de résolution AVANT de coder :
  - Proxy pre-période (ex: nominal − core CPI YoY) avec disclosure
  - Recadrage de la thèse pour matcher la période disponible
  - Chart court + annotation textuelle pour la période non-couverte

  Ne pas trancher silencieusement — demander à Paul.

- Si la thèse mentionne N catégories (régimes, scénarios, secteurs), vérifier que chacune sera visuellement représentable de façon symétrique. Si non, flaguer comme choix éditorial à confirmer.

**1.3 — Rigueur métrique (étape critique, après l'audit faisabilité).**

Pour chaque cellule/courbe du hero, la métrique choisie doit être **LE proxy académique standard** du concept énoncé dans le titre/sous-titre — pas un proxy adjacent qui « marche aussi ».

Mappings rigoureux de référence :

| Concept énoncé | Proxy standard | Code/source |
|---|---|---|
| Cost of capital / Taux réels | TIPS 10Y yield | FRED `DFII10` |
| Stock-bond correlation | Rolling 24m correlation S&P 500 / 10Y Treasury monthly returns | calcul Eco3min sur S&P + FRED `DGS10` |
| Duration risk premium / Prime de duration | ACM 10Y term premium | NY Fed (modèle Adrian-Crump-Moench) |
| Credit risk premium / Prime crédit | HY OAS | ICE BofA `BAMLH0A0HYM2` |
| Volatility / Volatilité | VIX niveau brut OU 12m MA selon focus | CBOE `VIXCLS` |
| Real activity / Activité réelle | Industrial production, employment, ou GDP growth | FRED (selon angle) |

**Test de validation : la métrique choisie doit faire ce qu'elle prétend faire SUR LA PÉRIODE COMPLÈTE de la thèse.** Contre-exemple à éviter (observé sur pilier `marches-financiers`, test mai 2026) : choisir HY OAS pour illustrer « primes de risque dans le nouveau régime », alors que les HY spreads se sont re-comprimés à leur plancher historique (~300 bps) en 2024-2026. La métrique contredit alors la thèse. Le proxy rigoureux était l'ACM term premium qui montre, lui, une réelle reconstitution.

Si plusieurs proxies sont défendables :
1. Choisir celui cité explicitement dans la page (priorité absolue)
2. Sinon : celui le plus immédiatement reconnu par un lecteur expert (Bloomberg-ready)
3. Sinon : celui sourçable via FRED ou source institutionnelle gratuite (pour reproductibilité)

En cas de doute, demander à Paul AVANT de coder.

### Étape 2 — Options (2 ou 3)

Présenter 2-3 options visuelles distinctes (A/B/C). Pour chacune, livrer une **carte structurée** :

- **Titre court** de l'option (ex: « Série temporelle anchor »)
- **Mockup SVG basse fidélité** OU description structurée
- **Ce que l'œil capte en 3 secondes** (1 phrase)
- **Données mobilisées** (sources + séries spécifiques avec codes)
- **Compromis** (1 phrase honnête sur ce que cette option sacrifie)

Présenter en canvas Figma-style si l'environnement le permet (sinon en texte structuré). Paul arbitre après lecture comparative.

### Étape 3 — Production SVG finale

Sur l'option retenue, produire le SVG complet, autonome, prêt à export PNG/WEBP en **1536×864**. Code propre et commenté pour itération.

**Structurer le code SVG en blocs modulaires par locale et par option** :
- Zones 1/2/3 (tag pilier / titre / sous-titre) — texte FR/EN paramétrable
- Zone 4 (chart-block) — invariant entre FR et EN, swappable entre options A/B/C
- Zones 5/6 (watermark / sourcing) — texte FR/EN paramétrable

Permet : (a) pivot rapide vers une option alternative sans tout refaire, (b) production de la variante linguistique en swappant uniquement le texte des zones 1/2/3/5/6.

### Étape 4 — Variante linguistique

Produire **systématiquement** la variante EN (ou FR si la base est EN). Strictement même structure visuelle, mêmes données — seul le texte change. Le titre traduit doit conserver le rythme et la précision du titre source, **pas une traduction littérale qui sonne plat**.

---

## Contraintes éditoriales (non négociables)

### Sourcing intégré au visuel

- Sources institutionnelles citées en **bas-droite** (Fed, BCE, BIS, FMI…)
- **Codes de série explicites** (DFII10, DGS10, etc.) — pas seulement « Federal Reserve » générique
- Méthodologie résumée en une ligne, ex : « TIPS 10Y from 2003 · pre-2003 proxy = DGS10 − sticky core CPI YoY · Values rounded for readability »
- « Updated [mois année] »
- Watermark « Eco3min — Research » + URL pilier en **bas-gauche**

### AMF compliance (visuel)

- Aucune flèche achat/vente, aucune zone colorée prescriptive
- Aucune cible de prix, aucune ligne « buy zone / sell zone »
- Annotations descriptives uniquement (« real rates turned positive Oct 2022 »), **jamais prescriptives**
- Aucun terme dramaturgique : pas de « collapse », « explosion », « destruction », « failed »

### Honnêteté data

- Axes chiffrés. Pas d'axe tronqué qui amplifie artificiellement.
- Pas de label « indicative » sur série chiffrable.
- Si série composite ou proxy : méthodologie en footer **ET** signalisation visuelle DANS le chart (pointillé vs plein, label de transition, etc.). **Footer seul ne suffit pas.**

### Symétrie de traitement des catégories

- Si la thèse mentionne N régimes/scénarios/catégories, les N doivent avoir un cue visuel équivalent (zone ombrée, ligne verticale, label délimité).
- Asymétrie volontaire acceptable SI éditorialement justifiée (ex: rupture sharp + transition graduelle), mais à **signaler comme choix délibéré** dans la livraison.

---

## Charte visuelle

**Palette, typographie, codes régime → voir `brand-kit-eco3min` (v1.1+).** Le brand kit fournit la source de vérité commune à toutes les productions visuelles Eco3min :
- 3 familles typo fixes (Source Serif 4 + Inter + IBM Plex Mono)
- Palette principale (charcoal `#1A1A1A` + gris medium `#757575` + accent terracotta `#B85C3C`)
- Fond crème `#F8F5EE` (registre fixe de la série heros piliers — blanc et charcoal inversé réservés à d'autres familles, brand kit §2.2)
- **Palette catégorielle 7 rangs (brand kit §2.5)** — pour les heros en mode catégoriel (comparaisons multi-régimes, multi-époques, multi-actifs), avec direct labeling en bout de ligne
- 6 codes couleurs régime sur 2 axes (3 macro + 3 monétaire) — priorité sémantique : à utiliser quand le hero nomme explicitement un régime
- Règle terracotta clarifiée : **unicité en mode sobre** (1 occurrence, label inclus) ; en mode catégoriel, terracotta = couleur de la série rang 1, l'unicité ne s'applique pas — mais le hero garde UN focus visuel

### Règles spécifiques aux heros piliers (en complément du brand kit)

**Densité** — information dense mais épurée. Aucun élément qui n'enseigne pas. Si un élément peut être retiré sans perte d'information, le retirer.

**Format**
- Ratio 16/9, dimensions **1536×864** strict pour la série hero pilier (contrairement au reste du brand kit qui laisse les ratios libres selon contexte).
- Test mobile : tout lisible à **380px** de large. Police mini ≈ équivalent 14px à 1536px de largeur.

**Anti-pattern terracotta cluster — version durcie pour les heros** : la règle d'unicité du brand kit s'applique avec une vigilance particulière sur les heros piliers, qui sont les visuels les plus exposés du site. Empiriquement validé sur 3 piliers livrés (mai 2026) : le pilier `politique-monetaire-taux` avec 1 ligne terracotta isolée a plus d'impact que `macroeconomie-geopolitique` avec 5 occurrences cluster. **Test** : si tu peux retirer 2 occurrences de terracotta sans dégrader la lecture de la thèse, retire-les.

**Cas Option SM** : la verticale terracotta se répète sur les 4 cellules à la même date — redondance contrôlée acceptée parce qu'elle sert la thèse « N propriétés convergent », pas un cluster.

---

## Layout canonique

Structure confirmée par les piliers `politique-monetaire-taux` et `macroeconomie-geopolitique` (mai 2026). À reproduire comme défaut sur les piliers suivants, sauf raison éditoriale spécifique signalée à Paul.

### Architecture 6 zones

1. **Tag pilier** (haut-gauche) — uppercase petit en mono, ex : `POLITIQUE MONÉTAIRE & TAUX — PILIER` / `MONETARY POLICY & RATES — PILLAR`
2. **Titre** (serif large, ≤8 mots) — porte la thèse de façon dense, rythme conservé en traduction
3. **Sous-titre** (sans-serif, 2 phrases max) — phrase 1 décrit ce que montre le chart, phrase 2 porte la thèse
4. **Chart pleine largeur** — le visuel dominant, contient toute la donnée
5. **Watermark** (bas-gauche) — `Eco3min — Research` ligne 1 + URL pilier ligne 2 (FR ou EN selon variante)
6. **Sourcing** (bas-droite) — bloc 2 lignes (format ci-dessous)

### Variante : signalétique régimes en barre inférieure

Quand la **géométrie naturelle de la courbe** raconte déjà les phases (climb → plateau → cassure, ou équivalent), la signalétique des régimes peut être déportée en **barre annotative sous le chart** plutôt qu'imposée par 3 zones ombrées superposées.

**Pattern observé sur `macroeconomie-geopolitique`** :
- Chart : une seule courbe, une seule zone ombrée terracotta pour le régime accent
- Barre inférieure : 3 cellules horizontales avec libellés `RÉGIME 1 · 1990-2008 · Coûts décroissants` / `RÉGIME 2 · 2010-2019 · Soutien monétaire` / `RÉGIME 3 · 2020-? · Résilience coûteuse`
- Avantage : chart aéré, la géométrie reste lisible, le test de comptage passe via la barre textuelle
- Condition d'usage : la courbe DOIT raconter visuellement les phases (sinon la barre devient un cosmétique déconnecté)

À utiliser quand le chart est "geom-led" (la forme parle). À éviter quand la donnée est plate ou erratique et que les régimes n'apparaîtraient qu'en zones ombrées.

### Variante Layout — Option SM (small multiples 2×2)

Layout enrichi spécifique au format SM. **Ne se substitue pas** à l'architecture 6 zones de référence — il l'étend avec une **structure interne par cellule** et 2 conventions d'annotation propres.

**Structure dans chaque cellule (4 niveaux, du haut vers le bas)** :

1. **Label catégoriel uppercase terracotta** (mono, ~11px, letterspacing 2.5) — reframe la métrique par son rôle macro. **PAS** le nom descriptif de la métrique seul.
   Ex FR : `PROPRIÉTÉ 01 · COÛT DU CAPITAL` · `PROPRIÉTÉ 02 · CORRÉLATION` · `PROPRIÉTÉ 03 · PRIMES DE RISQUE` · `PROPRIÉTÉ 04 · VOLATILITÉ`
   Ex EN : `PROPERTY 01 · COST OF CAPITAL` · `PROPERTY 02 · CORRELATION` · `PROPERTY 03 · RISK PREMIA` · `PROPERTY 04 · VOLATILITY`

2. **Titre descriptif de la métrique** (serif léger ou sans-serif medium, ~15px, charcoal)
   Ex : `Taux réels — Treasury TIPS 10 ans (%)` / `Real rates — 10Y Treasury TIPS yield (%)`

3. **Chart area** avec verticale terracotta unique à la même date sur les 4 cellules (cohérence cross-cells = signal homogène, redondance contrôlée).

4. **Bottom annotations dual-anchor avant/après** — pattern obligatoire en Option SM. Split gauche/droite sous le chart :
   - **Gauche** (gris medium, casse normale) : `[période pré-rupture] ≈ [valeur moyenne]`
   - **Droite** (terracotta uppercase pour la valeur post-rupture) : `[période post-rupture] ≈ [valeur moyenne]`

   Exemples bruts :
   - `2009 - 2021 ≈ −0,3 %` / `2022 - 2026 ≈ +2,0 %`

   Variante éditoriale avec label de régime nommé (recommandée quand le régime a une identité économique claire) :
   - `RÉGIME DÉSINFLATIONNISTE ≈ −0,40` / `RÉGIME INFLATIONNISTE ≈ +0,45`
   - `2013 - 2019 SUPPRIMÉE moy. ≈ 14` / `2022 - 2026 STRUCTURELLE moy. ≈ 20`

   **Pourquoi dual-anchor obligatoire** : le test 5 secondes échoue avec des annotations point-précises (« −1,19 % août 2021 → +2,40 % oct. 2023 »), qui demandent au lecteur de reconstruire la temporalité. La moyenne par régime se capte instantanément sans connaître les milestones. Pattern observé décisif sur `marches-financiers` (mai 2026).

**Pillar number tag** (recommandé, haut-droite du visuel) : `PILIER 03 / 10` / `PILLAR 03 / 10` en mono uppercase, gris medium. Inscrit l'image dans une série et facilite la mémorisation.

**Titre adapté à Option SM** : porter dans le titre LES DEUX axes structurants (nombre de régimes + nombre de propriétés/dimensions). Ex : `Two regimes, four properties reversed in 2022` / `Deux régimes, quatre propriétés inversées en 2022`. Pattern `N éléments, M propriétés, rupture en YYYY` plus dense que `N éléments, un basculement structurel`.

**Sous-titre adapté à Option SM** : phrase 1 liste les N propriétés + verbe de mouvement simultané ; phrase 2 porte la thèse compressée. Ex : « As real rates turn positive, stock-bond correlation, duration risk premia and volatility flip in sync — the 2009-2021 decade was a regime anomaly, not a baseline. »

**À utiliser quand** la thèse mentionne explicitement N propriétés/dimensions distinctes ET aucune métrique unique ne peut capturer le basculement.

### Format sourcing footer canonique

- **Ligne 1** — `Sources: [Institution] ([codes de série]); [Institution] ([série]); …`
- **Ligne 2** — `Updated [mois année] · [méthodologie résumée en 1 ligne] · Values rounded for readability`

Exemple (politique-monetaire-taux) :
- `Sources: Federal Reserve (FRED, DFII10, DGS10); Atlanta Fed (sticky core CPI); BLS`
- `Updated May 2026 · TIPS 10Y from 2003 · pre-2003 proxy = DGS10 − sticky core CPI YoY · Values rounded for readability`

**Le timestamp `Updated [mois année]` apparaît UNIQUEMENT dans la ligne 2 du sourcing footer.** Ne pas le dupliquer en haut-droite du visuel ni ailleurs.

### Hiérarchie des signaux intra-chart

Ordre **décroissant** de poids visuel à respecter strictement :

1. **Accent terracotta** (1 marqueur principal — voir règle Palette dans `brand-kit-eco3min`) — le moment-clé / la rupture
2. **Zone ombrée medium grey** — la durée d'une catégorie centrale
3. **Pointillé vertical fin** — transition méthodologique OU frontière de catégorie secondaire
4. **Zone ombrée light beige** (ou équivalent très clair) — catégorie périphérique
5. **Annotations textuelles courtes** — bord supérieur, ≤4 par chart

**Redondance contrôlée acceptable** : 2 signaux pour la même information (ex: light shading + pointillé pour une même frontière de catégorie) si la redondance sert la robustesse de lecture. **Interdite** si elle relève du remplissage ou de la symétrie cosmétique.

---

## Anti-patterns explicitement proscrits

- Diagramme de flux linéaire trivial (chaque flèche évidente)
- Empilement timeline + colonnes texte + chart + diagramme dans le même hero
- Bullets points multiples qui dupliquent la TOC de l'article
- Chart « indicatif » non chiffré sur axes
- Titre + sous-titre + 3 colonnes + mini-chart + watermark (surcharge classique)
- Symboles ↗ ↘ sans contexte numérique
- Légende détachée du graphique forçant des allers-retours
- Transition de séries (proxy ↔ donnée réelle) cachée uniquement en footer — doit AUSSI être visible dans le chart
- **Redondance forcée du signalement** — chercher artificiellement un 2e pointillé / une 2e zone ombrée parce que « ça marchait bien sur un pilier précédent », alors qu'il n'y a qu'une seule transition réelle à marquer. La redondance est un outil de robustesse, pas un pattern à reproduire mécaniquement
- **Doublon timestamp** — `Updated [mois année]` apparaissant à 2 endroits (ex: haut-droite du visuel ET ligne 2 du sourcing footer). Choisir UN seul emplacement, par défaut la ligne 2 du sourcing footer
- **Accent terracotta cluster** — 4 ou 5 occurrences de terracotta sur des éléments connexes (ligne verticale + shading + label-régime + bullet décoratif + label-chiffre) en argumentant qu'elles servent la même narration. Même cohérentes, ces occurrences multiples diluent l'impact visuel. Voir règle Palette pour le test de validation
- **Proxy métrique adjacent** — choisir une métrique connexe « qui marche aussi » (ex : HY OAS pour illustrer un duration risk premium, alors que l'ACM term premium existe) au lieu du proxy académique standard du concept énoncé. Risque : la métrique adjacente peut raconter une histoire DIFFÉRENTE de la thèse et la contredire silencieusement. Cas observé sur le test direct `marches-financiers` (mai 2026) : HY OAS choisi pour « primes de risque » → courbe redescendue à son plancher historique en 2024-2026, contredisant la thèse « primes reconstituées ». Voir Étape 1.3 Rigueur métrique
- **Bottom annotations point-précises au lieu de dual-anchor en Option SM** — `−1,19 % août 2021 → +2,40 % oct. 2023` est précis mais demande au lecteur de reconstruire la temporalité. Pour les small multiples, utiliser systématiquement le format moyenne-par-régime avant/après (voir Variante Layout Option SM)

---

## Tests de validation embarqués

**Test 1 — Comptage non-initié.** Si le titre mentionne N éléments (« trois régimes », « deux scénarios »…), Paul doit pouvoir montrer le hero à quelqu'un sans contexte et lui demander de compter N éléments. Si la personne compte ≠ N, itérer sur la signalétique.

**Test 2 — Mobile 380px.** Avant livraison, simuler le rendu à 380px de large : aucun chevauchement d'annotations, labels méthodo restent lisibles, sourcing footer toléré moins lisible.

**Test 3 — Lecture 5 secondes.** Masquer mentalement le titre/sous-titre et regarder uniquement le chart pendant 5 secondes. La thèse se capte ? Si non, elle est portée par le texte plutôt que par la donnée — revoir.

---

## Livraison attendue

1. **Audit thèse + faisabilité data** (réponses à Étape 1)
2. **2-3 options visuelles** (Étape 2) avec briefs structurés
3. **SVG final FR** (après arbitrage de Paul)
4. **SVG final EN** (variante stricte)
5. **Checklist « ce qui tient et ne doit pas être cassé »** — 3 à 5 points du squelette à reproduire sur les piliers suivants

---

## Input attendu de Paul

- Contenu intégral de la page pilier (FR ou EN)
- Slug et URL de la page
- **Format (A/B/C/SM) et mode chromatique (sobre/catégoriel/gradient) des 2 derniers heros piliers livrés** — requis pour la rotation série (règle bloquante v1.2). Si absent, demander avant de proposer les options.
- Éventuelles contraintes spécifiques (chiffres prioritaires, cohérence avec un autre hero déjà produit)

---

## Articulation avec autres skills

- **`brand-kit-eco3min`** — source de vérité pour palette, typographie, codes régime, fond crème, accent terracotta, format sourcing, watermark. Ce skill spécialise pour le cas hero pilier (format 1536×864 strict, layout 6 zones, hiérarchie 5 signaux intra-chart, variantes A/B/C/SM).
- **`visuels-eco3min`** — règles générales de data viz Eco3min (AMF, sourcing, types de chart, anti-patterns finance, qualité technique). Ce skill spécialise pour le cas hero pilier.
- **`formats-eco3min`** — catalogue des formats HTML pour les pages. Ce skill ne traite que du hero, pas du corps de la page.
- **`editeur-eco3min`** — règles éditoriales (ton, AMF, sourcing, anti-patterns IA) qui s'appliquent aussi au texte du hero (titre + sous-titre).
- **`archi-eco3min`** — structure des piliers et URLs (pour les slugs FR/EN et le watermark URL).
- **`production-chart-of-the-week`** — différent objectif (chart viral DIB) mais palette et typo cohérentes via le brand kit. Ne pas confondre les deux missions.

---

## Note d'usage

Skill créé après itération complète sur les piliers `politique-monetaire-taux` et `macroeconomie-geopolitique` (mai 2026, FR + EN livrés pour chacun), enrichi après le test direct sur `marches-financiers` (mai 2026, comparaison workflow direct vs Claude Design + skill). Patché en v1.1 (mai 2026) pour intégrer `brand-kit-eco3min` comme source de vérité de la charte visuelle. Patché en v1.2 (juillet 2026, audit anti-monotonie) : le risque de monotonie flagué en v1.1 (« déjà observé sur les 2 premiers ») devient la **règle bloquante de rotation série** (format + mode chromatique), adossée à la palette catégorielle du brand kit v1.1 §2.5.

### Confirmé canonique après ces trois premiers piliers

- **Layout 6 zones** (tag / titre / sous-titre / chart / watermark / sourcing) — voir section Layout canonique
- **Format sourcing footer 2 lignes** avec codes de série explicites
- **Hiérarchie de 5 signaux intra-chart** (accent terracotta principal → medium grey → pointillé → light beige → annotations)
- **Redondance contrôlée acceptable** quand 2 signaux convergent sur la même frontière (shading + pointillé) pour servir la robustesse de lecture
- **Bilingue strict** : EN produit en parallèle, slug `/en/` côté URL, structure visuelle 100% identique
- **Variante « barre régimes en pied »** acceptable quand la géométrie de la courbe raconte naturellement les phases (voir Layout canonique > Variante)
- **Variante « small multiples 2×2 »** acceptable quand la thèse mentionne N propriétés/dimensions distinctes (voir Layout canonique > Variante SM)
- **Code SVG modulaire par locale** (zones 1/2/3/5/6 paramétrables / zone 4 chart-block invariant) — permet pivot rapide entre options et entre langues

### Arbitrages tranchés (mai 2026)

- **Règle accent terracotta** : durcie après le pilier macro-géopo qui empilait 5 occurrences cluster. La règle actuelle (1 marqueur principal + son label) est la version stricte, alignée sur le pilier monétaire (1 seule ligne terracotta). En Option SM, l'accent se répète sur les 4 cellules à la même date — redondance contrôlée acceptée, pas un cluster. Règle désormais centralisée dans `brand-kit-eco3min` section 2.3.
- **Emplacement timestamp** : ligne 2 du sourcing footer uniquement. Pas de duplication en haut-droite.
- **Rigueur métrique** : règle ajoutée après le test `marches-financiers`. Le proxy doit être LE standard académique du concept énoncé, pas un proxy adjacent qui « marche aussi ». Le test « la métrique fait-elle ce qu'elle prétend faire SUR LA PÉRIODE COMPLÈTE » est bloquant.
- **Bottom-annotation Option SM** : pattern dual-anchor moyenne-par-régime imposé (split gauche/droite, terracotta uppercase pour la valeur post-rupture). Les annotations point-précises sont inférieures pour le test 5 secondes.
- **Labels catégoriels uppercase** : pattern `PROPRIÉTÉ NN · CONCEPT MACRO` au-dessus du nom de métrique dans chaque cellule SM. Reframe la métrique par son rôle, élève le visuel d'un dashboard à une thèse argumentée.

### Workflow : Claude Design + skill vs production directe

Le test mai 2026 sur `marches-financiers` a comparé les deux workflows. Verdict empirique :

- **Claude Design + prompts dérivés du skill** = supérieur pour le rendu typographique (Source Serif 4 chargée native), pour les patterns éditoriaux émergents (dual-anchor, labels catégoriels) que le skill ne pré-imposait pas, et pour la rigueur métrique apparemment renforcée par le canvas visuel.
- **Production directe (SVG via outils Claude)** = utile pour itération immédiate sans copier-coller, pour cohérence inter-piliers automatique (skill chargé en mémoire conversationnelle), pour produire des fichiers SVG bruts éditables. Limite : rendu typo dépend des fallbacks navigateur, polylines qualitatives sauf à fetcher les CSV FRED.

**Recommandation par défaut** : Claude Design + prompts dérivés de ce skill. Production directe réservée aux cas d'itération rapide ou de data-fetch explicite avec polylines reconstruites depuis CSV.

### À actualiser après production de 2-3 piliers supplémentaires si

- ~~Des règles transversales émergent sur la **diversité des formats A/B/C/SM** entre piliers (risque réel de monotonie si chaque pilier prend l'Option A — déjà observé sur les 2 premiers)~~ → **traité en v1.2** (règle bloquante de rotation série). Reste à surveiller : si la rotation produit des formats forcés qui ne servent pas la donnée, assouplir vers « dérogation sur signalement » plus fréquente
- Une **nouvelle famille de pilier** (sans transition méthodologique, sans 3 catégories, données pré-1990, etc.) demande un sous-pattern non prévu ici
- Claude Design révèle un comportement de rendu spécifique non anticipé (typo, échelle, export)
- Le **test « comptage non-initié »** échoue sur un pilier malgré le respect des règles — signal qu'il manque une règle de signalisation

### Prochains piliers candidats naturels

- **`page-courbe-des-taux`** — DGS10/DGS2 remontent à 1976, pas de proxy nécessaire, thèse claire (inversion = signal récessif), candidat A
- **`dollar-systeme-mondial`** — DXY ou TWEXBGS depuis 1973, thèse hégémonie / cycle, candidat A ou B
- **`immobilier-cycles-taux-economie`** — Case-Shiller + mortgage rates, candidat B (comparaison cycles)

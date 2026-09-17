# production-hero-pilier — référence : Layout canonique : architecture 6 zones, variante barre régimes, variante Option SM (labels catégoriels, dual-anchor), format sourcing footer, hiérarchie des 5 signaux

Extrait VERBATIM de SKILL.md (découpage du 17/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## Layout canonique

Structure confirmée par les piliers `politique-monetaire-taux` et `macroeconomie-geopolitique` (mai 2026). À reproduire comme défaut sur les piliers suivants, sauf raison éditoriale spécifique signalée à Paul.

### Architecture 6 zones

1. **Tag pilier** (haut-gauche) — uppercase petit en mono, ex : `POLITIQUE MONÉTAIRE & TAUX — PILIER` / `MONETARY POLICY & RATES — PILLAR`
2. **Titre** (serif large, ≤8 mots) — porte la thèse de façon dense, rythme conservé en traduction
3. **Sous-titre** (sans-serif, 2 phrases max) — phrase 1 décrit ce que montre le chart, phrase 2 porte la thèse
4. **Chart pleine largeur** — le visuel dominant, contient toute la donnée
5. **Signature** (bas-droite) — `Eco3min Research` ligne 1 + URL pilier ligne 2 (FR ou EN selon variante) — chrome canonique `brand-kit-eco3min` v2.0 §0
6. **Sourcing** (bas-gauche) — bloc 2 lignes (format ci-dessous)

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

**Pillar number tag** : **interdit** depuis le 17/09/2026 (`brand-kit-eco3min` v2.0 §0). Les tables de piliers recopiées dans les projets ont divergé de `archi-eco3min` et produit des numéros faux (constat `production-hero-article-eco3min`) ; le tag pilier haut-gauche suffit à inscrire l'image dans la série.

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

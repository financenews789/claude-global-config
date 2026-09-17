# brand-kit-eco3min — référence : Formats canoniques, règles d'usage (type de chart, 3 modes chromatiques, annotations, terracotta), sourcing et watermark (§4 à §7)

Extrait VERBATIM de SKILL.md (découpage du 17/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée, le chrome canonique §0 et le moment où lire ce fichier.

## 4. Formats canoniques par type de visuel

| Type de visuel | Ratio | Dimensions | Usage |
|---|---|---|---|
| Hero pilier | 16:9 | 1536×864 | Toutes les pages piliers (skill `production-hero-pilier`) |
| Hero d'article (V3) | 1.91:1 | 1200×630 | Articles courants et satellites (skill `production-hero-article-eco3min`) |
| Chart of the week (Reddit DIB) | 16:9 | 1920×1080 (décision figée 29/08/2026, un seul rendu) | Production hebdomadaire viral (skill `production-chart-of-the-week`) |
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

**Position** : pied de visuel, **bas-gauche** (chrome canonique v2.0, SKILL.md §0) ; la signature Eco3min occupe le bas-droite.

**Format à 2 lignes** (canon hero pilier) :

```
Ligne 1 — Sources: [Institution] ([codes série]); [Institution] ([série]); …
Ligne 2 — Updated [mois année] · [méthodologie résumée en 1 ligne] · Values rounded for readability
```

**Format à 1 ligne** (charts moins denses, social) :

```
Sources: [Institution] ([codes série]) · [mois année]
```

**Typo** : IBM Plex Mono, 9–10 px, gris medium `#757575`, letter-spacing 0.5.

**Casse** : sentence case dans le contenu des sources. Le mot « Sources » initial peut être en regular ou en uppercase selon densité.

**Mention Eco3min obligatoire** : « Chart: Eco3min Research » OU « Eco3min Research » seul. Toujours présent, même discret. Survit au repartage hors contexte (capture X, AI Overview).

**Date** : si donnée vivante, inclure date d'extraction (« data as of May 12, 2026 »). Si donnée stable, mois + année suffisent.

---

## 7. Watermark Eco3min

**Position** : **bas-droite**, toujours (chrome canonique v2.0) ; le sourcing occupe le bas-gauche.

**Texte** : `Eco3min Research` ligne 1 (sans cadratin : zéro cadratin dans un visuel), URL de la page ligne 2 sur les heros (pilier, majeur, article) et les études ; ligne 1 seule sur les charts distribués hors site (Chart of the Week, social).

**Typo** : IBM Plex Mono, 9–10 px, gris medium.

**Pas de logo géant** : l'attribution, pas le branding.

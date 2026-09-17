# production-hero-pilier — référence : Process en 4 étapes : thèse, audit de faisabilité data, rigueur métrique (table des proxies), cartes d'options, production SVG modulaire, variante linguistique

Extrait VERBATIM de SKILL.md (découpage du 17/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

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

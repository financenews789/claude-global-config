# visuels-eco3min — référence : Copyright et droits visuels, historique des versions (§8, Versioning)

Extrait VERBATIM de SKILL.md (découpage du 17/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

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

## Versioning

- **v1.0** (création initiale) — corpus de règles AMF, sourcing, data viz, qualité technique. Philosophie initiale : « aucune charte graphique imposée ».
- **v1.1** (mai 2026) — alignement avec `brand-kit-eco3min v1.0`. La philosophie est révisée : le minimum commun (typo, palette, codes régime, accent) est désormais fourni par le brand kit ; ce skill garde son rôle de référence sur les règles de fond (AMF, sourcing, qualité, choix de chart). Aucune règle de fond modifiée.
- **v1.2** (juillet 2026) — alignement avec `brand-kit-eco3min v1.1` (diversité chromatique contrôlée). Ajouts : famille de charts multi-entités (palette catégorielle §2.5) + pattern spaghetti focus au tableau de choix ; règle générale de direct labeling en bout de ligne, légende détachée bannie ≤6 séries ; checklist mise à jour (3 registres de fond, mode chromatique). Aucune règle AMF, sourcing ou qualité modifiée.
- **v1.3** (septembre 2026) — ajout du §7 bis « Rendu PNG — recette Playwright » : séquence de chargement des polices, auto-ajustement de titre, SVG inline. Extrait du projet « repair image », où cette connaissance était piégée depuis la V3. Aucune règle AMF, sourcing ou qualité modifiée.
- **v1.5** (16 septembre 2026, étude R6) — §7 ter, cinquième assertion : la ligne de sources se termine avant le watermark (test d'ordre horizontal, le seuil de 12 % laissant passer une morsure de fin de ligne). Aucune règle modifiée.
- **v1.4** (septembre 2026, cycle 20 Chart of the Week) — ajout du §7 ter « Rendu matplotlib — quatre assertions avant `savefig` » : repli de police, débordement de canvas, chevauchement des textes d'en-tête, échappement des `$` (mathtext), plus le garde ASCII sur le cmap. Le §7 bis ne couvrait que le chemin Playwright ; les charts matplotlib ont leurs propres échecs silencieux, et les trois premières assertions ont chacune attrapé un défaut réel sur un script écrit par quelqu'un qui connaissait le piège. Le point U+202F d'IBM Plex Mono, jusqu'ici seulement en mémoire de projet, trouve ici son foyer. Aucune règle AMF, sourcing ou qualité modifiée.

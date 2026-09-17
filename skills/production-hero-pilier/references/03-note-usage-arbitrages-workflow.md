# production-hero-pilier — référence : Note d'usage : genèse, confirmé canonique, arbitrages tranchés (mai 2026), workflow Claude Design vs code, à actualiser, prochains piliers candidats

Extrait VERBATIM de SKILL.md (découpage du 17/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

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

**Recommandation par défaut (révisée le 17/09/2026)** : production en **code** depuis le CSV réel — HTML/SVG → Playwright (`visuels-eco3min` §7 bis) ou matplotlib avec `mpl_guards` (§7 ter) — parce que les gardes bloquantes (police rendue, débordement, chevauchement, palette `brand_tokens.check_source`) ne s'assertent qu'en code, et parce que le gate données interdit de toute façon la polyline eyeballed. Claude Design reste l'outil de l'**Étape 2** (mockups des 2-3 options) ; le verdict de mai 2026 ci-dessus reste vrai pour l'exploration, plus pour la livraison.

### À actualiser après production de 2-3 piliers supplémentaires si

- ~~Des règles transversales émergent sur la **diversité des formats A/B/C/SM** entre piliers (risque réel de monotonie si chaque pilier prend l'Option A — déjà observé sur les 2 premiers)~~ → **traité en v1.2** (règle bloquante de rotation série). Reste à surveiller : si la rotation produit des formats forcés qui ne servent pas la donnée, assouplir vers « dérogation sur signalement » plus fréquente
- Une **nouvelle famille de pilier** (sans transition méthodologique, sans 3 catégories, données pré-1990, etc.) demande un sous-pattern non prévu ici
- Claude Design révèle un comportement de rendu spécifique non anticipé (typo, échelle, export)
- Le **test « comptage non-initié »** échoue sur un pilier malgré le respect des règles — signal qu'il manque une règle de signalisation

### Prochains piliers candidats naturels

- **`page-courbe-des-taux`** — DGS10/DGS2 remontent à 1976, pas de proxy nécessaire, thèse claire (inversion = signal récessif), candidat A
- **`dollar-systeme-mondial`** — DXY ou TWEXBGS depuis 1973, thèse hégémonie / cycle, candidat A ou B
- **`immobilier-cycles-taux-economie`** — Case-Shiller + mortgage rates, candidat B (comparaison cycles)

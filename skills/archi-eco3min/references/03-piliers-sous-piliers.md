# archi-eco3min — référence : Liste figée des piliers et des sous-piliers (§5, §6)

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026) pour §5.1-5.3 et §6.1-6.2, complété le 15/09/2026 par l'état live (`eco3min/taxonomy scope=pillars` et `scope=sub_pillars`) : §6.3 ajouts de sous-piliers absents de la liste de juin, §5.4 hubs fonctionnels à `level=pillar`. Fait foi avec SKILL.md ; SKILL.md porte le mapping FR ↔ EN et le moment où lire ce fichier.

---

## 5. Liste figée des piliers

### 5.1 Piliers FR (11)

| # | Slug | Thème |
|---|---|---|
| 1 | `macroeconomie-geopolitique` | Macro & géopolitique |
| 2 | `politique-monetaire-taux` | Politique monétaire & taux |
| 3 | `marches-financiers` | Marchés financiers |
| 4 | `actions-et-etf` | Actions & ETF |
| 5 | `immobilier-cycles-taux-economie` | Immobilier |
| 6 | `matieres-premieres-economie-mondiale` | Matières premières |
| 7 | `crypto-actifs-comprendre-enjeux-economiques-financiers-monetaires` | Crypto-actifs |
| 8 | `strategies-dinvestissement` | Stratégies d'investissement |
| 9 | `page-education-financiere` | Éducation financière |
| 10 | `apprendre-investir` | Hub débutant FR |
| 11 | `donnees-analyses-macro-financieres` | Hub datasets FR |

### 5.2 Piliers EN (11)

| # | Slug | Thème |
|---|---|---|
| 1 | `macro-financial-regimes` | Macro & geopolitics |
| 2 | `monetary-regimes-interest-rates-liquidity-market-cycles` | Monetary regimes & rates |
| 3 | `market-regimes-liquidity-real-rates-financial-dynamics` | Market regimes |
| 4 | `equity-markets-etfs-structure-valuations-cycles` | Equity & ETFs |
| 5 | `real-estate-credit-rate-cycles` | Real estate |
| 6 | `commodity-regimes-physical-constraints-energy-transition` | Commodities |
| 7 | `crypto-assets-liquidity-cycles-real-rates` | Crypto |
| 8 | `asset-allocation-strategies-resilient-portfolios-market-regimes` | Asset allocation |
| 9 | `financial-education-macroeconomic-regimes` | Financial education |
| 10 | `investing-for-beginners-hub` | Beginner hub EN |
| 11 | `research-data` | Datasets hub EN |

### 5.3 Mapping FR ↔ EN

Le mapping est **symétrique pour les 11 piliers** : à chaque pilier FR correspond un pilier EN au même niveau hiérarchique (et inversement). Pas d'asymétrie — un pilier FR n'est jamais traduit en sub-pilier EN.

| FR | EN |
|---|---|
| `macroeconomie-geopolitique` | `macro-financial-regimes` |
| `politique-monetaire-taux` | `monetary-regimes-interest-rates-liquidity-market-cycles` |
| `marches-financiers` | `market-regimes-liquidity-real-rates-financial-dynamics` |
| `actions-et-etf` | `equity-markets-etfs-structure-valuations-cycles` |
| `immobilier-cycles-taux-economie` | `real-estate-credit-rate-cycles` |
| `matieres-premieres-economie-mondiale` | `commodity-regimes-physical-constraints-energy-transition` |
| `crypto-actifs-comprendre-enjeux-economiques-financiers-monetaires` | `crypto-assets-liquidity-cycles-real-rates` |
| `strategies-dinvestissement` | `asset-allocation-strategies-resilient-portfolios-market-regimes` |
| `page-education-financiere` | `financial-education-macroeconomic-regimes` |
| `apprendre-investir` | `investing-for-beginners-hub` |
| `donnees-analyses-macro-financieres` | `research-data` |

**Note** : les slugs hardcodés dans `eco3min-site-audit/includes/class-installer.php` étaient obsolètes pour 4 piliers EN au moment de la rédaction de ce skill (`real-estate-cycles-rates-economy`, `commodities-global-economy`, `crypto-assets-economic-monetary-financial-stakes`, `financial-education`). **Les bons slugs sont ceux du tableau ci-dessus.** Si on touche au installer, mettre à jour. Le mega utilise les slugs corrects via la table `e3m_referentiel`.

> Note du 15/09/2026 : `eco3min-site-audit` n'existe plus (désinstallé, dossier supprimé). Le seul référentiel de slugs de piliers en base est `e3m_referentiel` (Mega → Référentiel) ; le tableau ci-dessus reste exact (22 pages `pillar` vérifiées live).

### 5.4 Hubs fonctionnels à `level=pillar` (état live 15/09/2026)

`eco3min/taxonomy scope=pillars` renvoie **31** pages `level=pillar` : les 22 piliers éditoriaux ci-dessus plus 9 pages déclarées pilier par le Cleanup (section 3 : « page à 1 segment avec enfants ») — elles n'ont ni sous-pilier ni `_eco3min_cluster`, `attached_count = 0`, et ne sont jamais une valeur valide de `_eco3min_cluster` :

| Slug | Langue | Rôle |
|---|---|---|
| `qr` | fr | hub des Q&A FR (`/qr/…`) |
| `qa` | en | hub des Q&A EN (`/en/qa/…`) |
| `comparatif` | fr | hub comparatifs |
| `compare` | en | hub comparatifs |
| `idees-recues` | fr | hub idées reçues |
| `mistakes` | en | hub misconceptions |
| `lectures-eco3min` | fr | cadres de lecture |
| `outils-analyse-macroeconomique` | fr | hub outils |
| `macroeconomic-analysis-tools` | en | hub outils |

---

## 6. Liste figée des sous-piliers

### 6.1 Sous-piliers FR par pilier

`macroeconomie-geopolitique`
- `cycle-economique`
- `inflation-au-dela-des-chiffres-mensuels`
- `dette-fragilites-systemiques`
- `demondialisation`
- `geopolitique-structurelle`

`politique-monetaire-taux`
- `banques-centrales-actions`
- `liquidite-conditions-financieres`
- `dollar-systeme-mondial`
- `transmission-monetaire-entreprises`

`marches-financiers`
- `dynamiques-marche-microstructure`
- `dynamiques-marche-anticipations`
- `dynamiques-marche-correlations`
- `dynamiques-marche-flux-capitaux`
- `dynamiques-marche-tensions-cachees`
- `devises-forex-comprendre-les-marches-monetaires`
- `innovation-financiere`

`actions-et-etf`
- `revolution-passive-gestion-indicielle`
- `retour-actionnaires`
- `secteurs-thematiques`
- `cycles-anticipations-marche`
- `valorisations-dynamique-profits`
- `entreprises-et-secteurs-dynamiques-economiques`

`immobilier-cycles-taux-economie`
- `inflation-protection`
- `rendement-locatif`
- `cycle-credit`
- `taux-capacite-achat`

`matieres-premieres-economie-mondiale`
- `formation-prix-mecanismes`
- `cycles-transmission-macro`
- `geoeconomie-ressources`
- `energie-matieres-premieres`
- `matieres-premieres-agricoles`

`crypto-actifs-comprendre-enjeux-economiques-financiers-monetaires`
- `bitcoin-actif-monetaire-cycles-liquidite`
- `regulation-risques-structurels-crypto`
- `cycles-volatilite-crypto-comprendre`
- `ethereum-stablecoins-infrastructure-decentralisee`

`strategies-dinvestissement`
- `lire-cycle-ajuster-exposition`
- `pieges-esprit-biais-comportementaux`
- `gerer-risque-portefeuille`
- `fondements-allocation-actifs`
- `choisir-placements-selon-cycle-macro`

`page-education-financiere`
- `methode-principes-financiers`
- `arbitrages-quotidien`
- `anatomie-des-placements`
- `outils-financiers`

`apprendre-investir` et `donnees-analyses-macro-financieres` n'ont pas de sous-piliers — ce sont des hubs qui contiennent des articles directement.

### 6.2 Sous-piliers EN par pilier

`macro-financial-regimes`
- `economic-cycle-phases-signals-market-implications`
- `inflation-regimes-structural-drivers-macro-financial-implications`
- `systemic-fragilities-debt-shadow-banking-financial-stability-risks`
- `deglobalization-fragmentation-geopolitics-supply-chains-trade`
- `geopolitics-macroeconomics-structural-transmission-markets-regimes`

`monetary-regimes-interest-rates-liquidity-market-cycles`
- `central-banks-monetary-policy-rate-cycles-market-transmission`
- `liquidity-financial-conditions-monetary-plumbing-qt-market-impact`
- `us-dollar-systemic-global-monetary-system`
- `monetary-transmission-corporate-earnings-time-lags-margins-rate-cycles`

`market-regimes-liquidity-real-rates-financial-dynamics`
- `market-microstructure-price-formation-mechanics`
- `market-expectations-sentiment-price-formation`
- `asset-class-correlations-regime-shifts`
- `capital-flows-price-formation-markets`
- `systemic-risk-indicators-market-stress-signals`
- `fx-markets-exchange-rates-monetary-regimes`
- `financial-innovation-market-infrastructure-systemic-risk`

`equity-markets-etfs-structure-valuations-cycles`
- `passive-management-etf-market-structure`
- `dividends-share-buybacks-total-shareholder-yield-distribution-cycles`
- `sector-rotation-style-regimes-value-growth-market-cycles`
- `equity-market-valuation-real-rates-multiples-earnings`
- `equity-markets-real-economy-earnings-cycles-monetary-regimes`
- `companies-economic-sectors-structural-drivers-competitiveness-value-creation`

`real-estate-credit-rate-cycles`
- `real-estate-inflation-credit-real-rates-protection-paradox`
- `rental-property-profitability-gross-net-yield-cost-of-capital`
- `real-estate-credit-cycle-price-dynamics`
- `interest-rates-real-estate-purchasing-power-mortgage-capacity-mechanism`

`commodity-regimes-physical-constraints-energy-transition`
- `commodity-price-formation-physical-constraints-financial-flows-structural-drivers`
- `commodities-macroeconomic-regime-signals-cycles-inflation-strategic-power`
- `physical-commodity-markets-oil-gas-copper-critical-minerals-structural-signals`
- `physical-constraints-economy-energy-resources-structural-growth-limits`
- `agricultural-commodities-softs-grains-climate-cycles-food-inflation`

`crypto-assets-liquidity-cycles-real-rates`
- `bitcoin-liquidity-cycles-real-rates-macro-regimes`
- `crypto-regulation-effects-limits-structural-risks`
- `crypto-volatility-structural-drivers-liquidity-regimes`
- `ethereum-stablecoins-digital-dollarization-architecture-risks`

`asset-allocation-strategies-resilient-portfolios-market-regimes`
- `economic-cycle-analysis-portfolio-regime-positioning`
- `behavioral-investing-cognitive-biases-discipline-risk`
- `portfolio-risk-management-survival-before-performance`
- `portfolio-allocation-architectures-regime-assumptions`
- `choosing-investments-market-regimes-rate-cycles`

`financial-education-macroeconomic-regimes`
- `financial-education-framework-principles-economic-regimes`
- `everyday-financial-tradeoffs-economic-regimes`
- `investment-vehicles-real-returns-costs-regime-impact`
- `financial-tools-simulators-test-assumptions-decisions`

> **Ajouts juin 2026 (vérifiés live, HTTP 200)** — deux paires de sous-piliers publiées récemment, ajoutées en fin de bloc de leur pilier :
> - `matieres-premieres-economie-mondiale/matieres-premieres-agricoles` ↔ `commodity-regimes-physical-constraints-energy-transition/agricultural-commodities-softs-grains-climate-cycles-food-inflation`
> - `strategies-dinvestissement/choisir-placements-selon-cycle-macro` ↔ `asset-allocation-strategies-resilient-portfolios-market-regimes/choosing-investments-market-regimes-rate-cycles`

### 6.3 Sous-piliers présents en live et absents de la liste ci-dessus (vérifié 15/09/2026)

97 pages `level=sub_pillar` en base ; 89 sont référencées comme `_eco3min_sub_pilier` par au moins une page, une seule valeur de meta (`—`, 2 pages) ne correspond à aucune page. La liste de juin en manque 9 :

`macroeconomie-geopolitique` (8 sous-piliers, pas 5)
- `bascules-de-regime` (post 17432 — « onze crises, de 1929 à 2022 », miroir de `crisis-hub`)
- `geopolitique-economique-fragmentation-mondiale` (post 4386)
- `outils-macro` (post 17615 — page outils, sans enfant)

`macro-financial-regimes` (7 sous-piliers, pas 5)
- `crisis-hub` (post 17433 — miroir de `bascules-de-regime`)
- `macro-tools` (post 17618 — page outils, sans enfant)

`apprendre-investir` (1 sous-pilier — la phrase « n'ont pas de sous-piliers » de §6.1 n'est plus vraie pour ce hub)
- `pourquoi-marches-montent-baissent` (post 8943)

`investing-for-beginners-hub` (3 sous-piliers)
- `inflation-impact-on-savings-investments` (post 8964)
- `ira-401k-vs-taxable-brokerage` (post 9507)
- `biggest-investing-mistakes-beginners` (post 8967)

`donnees-analyses-macro-financieres` et `research-data` n'ont toujours aucun sous-pilier.

Les 9 piliers thématiques FR/EN (§6.1-6.2) sont conformes au live, à ces ajouts près. Pour un état à jour : `eco3min/taxonomy scope=pillars` (sous-piliers par pilier avec `post_id`) ou `scope=sub_pillars` (slugs référencés, `count`, `page_exists`).

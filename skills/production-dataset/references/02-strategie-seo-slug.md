# production-dataset — référence : Stratégie SEO par cas, anti-patterns, territoires, convention de slug (§3, §4)

Extrait VERBATIM de SKILL.md (découpage du 16/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 3. Stratégie SEO par cas — H1, meta, focus keyword

### 3.1 Cas A — ticker googlé en tête

H1 : `{TICKER}: {Description analytique}`. Le ticker ouvre le H1 et la meta title.

| Élément | Exemple |
|---|---|
| H1 | `DGS10: 10-Year US Treasury Yield Daily Since 1962` |
| Meta title | `DGS10: 10-Year Treasury Yield Daily Data Since 1962` |
| Focus keyword | `dgs10` (ou `10 year treasury yield`) |

Cas A typiques : DGS10, DGS2, FEDFUNDS, VIXCLS (VIX), WALCL, T10Y2Y, CPIAUCSL, et les FX à ticker reconnu (`DEXJPUS` → mais attention, voir note FX ci-dessous).

> **Note FX :** un cross devise se google sous sa forme humaine (`USD/JPY`, `EUR/USD`), pas sous le code FRED (`DEXJPUS`). Le H1 vise donc le pair humain : `USD/JPY Exchange Rate: Daily Yen per Dollar Since 1971`. C'est techniquement un Cas A (ticker humain googlé), mais le « ticker » est le pair, pas le code FRED.

### 3.2 Cas A' — concept canonique en tête (source FRED ou non)

H1 : `{Concept canonique}: {Description}`. Le code source (FRED ou autre) **n'apparaît jamais** en tête.

| Source | Exemple H1 | Focus keyword |
|---|---|---|
| FRED non-googlé (commodity) | `Arabica Coffee Price: Monthly Global Spot Price Since 1980` | `arabica coffee price` |
| FRED non-googlé (métal) | `Iron Ore Price: Monthly Global Benchmark Since 1980` | `iron ore price` |
| Non-FRED (enquête) | `ISM Manufacturing PMI: Monthly Survey Data Since 1948` | `ism manufacturing pmi` |
| FRED via Coinbase (crypto, `CBBTCUSD`) | `Bitcoin Price History (BTC-USD): Daily Coinbase Prices Since 2014` | `bitcoin price history` |
| Non-FRED (métal précieux, World Bank Pink Sheet) | `Silver Price History: Monthly Average in USD Since 1960 (World Bank Data)` | `silver price history` |

Les deux dernières lignes ont été corrigées le 17/09/2026 : les anciens exemples nommaient une source (LBMA Fix) ou une profondeur (2010) que la donnée servie n'a pas. Un H1 ne promet que ce que le CSV contient (§12.4).

La source réelle est nommée dans le bloc Sources et la Methodology, **pas** dans le H1.

### 3.3 Cas B — composite, concept canonique + construction

H1 : `{Concept canonique}: {Construction analytique}`. Le **code interne** (NET_LIQ, SP500_M2, WALCL_GDP…) n'apparaît **0 fois** dans H1 / meta title / meta description.

| Sous-type composite | Exemple H1 |
|---|---|
| Ratio simple | `Copper-Gold Ratio: Daily Industrial Metals Spread as Growth and Risk Indicator (1990–2026)` |
| Réel (déflaté) | `Real Interest Rates: 10-Year US Treasury Yield Minus CPI Inflation Daily Since 1962` |
| Indicateur propriétaire | `Net Liquidity Index: Fed Balance Sheet Minus TGA and Reverse Repos Daily Since 2008` |
| Indicateur propriétaire | `Excess CAPE Yield: Inverse CAPE Minus Real 10-Year Yield Monthly Since 1881` |
| Long historique fusionné | `S&P 500 Total Returns: Annual Equity Returns Including Dividends and Inflation Since 1928` |

**Meta description (Cas B, non négociable)** : concept dans les 30 premiers caractères + construction explicite (composante 1 + composante 2 + opération) + mention **« Eco3min composite/calculation »** + couverture + signal d'usage (CSV, Python/R, daily/monthly, free). Cible 140-165 c.

> `Net Liquidity Index daily data: Fed balance sheet minus Treasury General Account and reverse repos. Eco3min composite from 2008. CSV, Python/R, free.`

### 3.4 Anti-patterns SEO (tous cas)

- ❌ Code interne en tête : `NETLIQ: Net Liquidity Index Data`, `SP500_M2: Liquidity-Adjusted Ratio`
- ❌ H1 éditorial = territoire d'une étude : `Net Liquidity Index Crashes Markets: What the Data Shows`
- ❌ Marketing creux : `The Ultimate Guide to Real Interest Rates in 2026`
- ❌ Trop large / ultra-concurrencé : `S&P 500: Complete Historical Returns Data`
- ❌ Déduire le H1 de la source : café FRED → `PCOFFOTMUSDM` en tête (faux : Cas A', concept)

### 3.5 Quatre territoires SEO à ne pas chevaucher

| Couche | Cible mot-clé | Territoire de la page dataset ? |
|---|---|---|
| **Page dataset (toi)** | le concept en tant que **DONNÉE** : « où la trouver, comment elle est construite, comment la télécharger » | ✅ |
| **Étude evergreen** | le concept en tant qu'**ANALYSE** : « que dit l'indicateur, ses limites, ses signaux historiques » | ❌ ne pas reprendre l'angle |
| **Cluster MAJEUR** | le composé éditorial humain : « comprendre la Fed », « le marché immobilier US » | ❌ |
| **Sub-pilier** | la catégorie conceptuelle : « liquidité monétaire », « valorisation actions » | ❌ |

Si une étude porte un nom proche du dataset (`net liquidity illusion` vs `net liquidity index`), on **maille l'étude depuis Related Research en bas**, jamais on ne reprend son angle dans le corps. Séparation DONNÉE (toi) vs ANALYSE (étude).

---

## 4. Convention de slug et identifiants

| Élément | Format | Exemple |
|---|---|---|
| `dataset_id` (slug interne shortcodes) | kebab-case, court, evergreen | `nasdaq-composite`, `excess-cape-yield` |
| URL EN | `/en/[slug-en]-dataset/` | `/en/us-10y-treasury-yield-dataset/` |
| URL FR | convention site (souvent racine) | `/credit-spreads-recession-risk-dataset/` |
| URL CSV brute | `/dataset/{slug}.csv` | `/dataset/nasdaq-composite.csv` |
| URL JSON brute | `/dataset/{slug}.json` | `/dataset/nasdaq-composite.json` |
| Code source | FRED majuscules / clé ECB SDMX / code IMF / **code interne composite** | `NASDAQCOM`, `DGS10`, `IRLTLT01JPM156N`, `NET_LIQ`, `SP500_M2` |

**Règle filename immuable** : une fois le `dataset_id` fixé, il ne change JAMAIS. Pages HTML, pipelines, liens internes en dépendent. Renommer casse tout.

**Code source vs code SEO** : le code source (`data-series` du canvas, `dataset_id` des shortcodes) est un identifiant **technique**. Pour les composites c'est un **code interne** (`NET_LIQ`) qui n'est ni un ticker FRED ni un mot-clé. Il ne doit jamais migrer vers le H1 / meta / focus keyword.

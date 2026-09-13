---
name: production-dataset
description: Production et révision des pages dataset Eco3min, bilingues FR/EN — séries d'une source primaire (FRED, ECB SDMX, IMF, BIS, BLS, Eurostat, Shiller, World Bank, CoinGecko, LBMA, ENTSO-E, AGSI, FAO…) ET composites construits par Eco3min (ratios, séries réelles déflatées, indicateurs propriétaires type Net Liquidity Index ou Excess CAPE Yield). Pages standardisées : graphique dynamique, métadonnées, exemples Python/R, méthodologie, régimes historiques, maillage interne. Pilote les trois cas SEO — A (ticker googlé en H1), A' (concept canonique en H1, source FRED ou non), B (composite : concept + sections Construction & Components / What This Index Captures / Data Quality). Couvre les shortcodes eco3min_latest / key_stats / download, conventions de slug et code source, AMF. À distinguer des études approfondies (hypothèse, narrative) et de la création du CSV (skill pipeline séparé). À activer pour toute création ou révision de page dataset.
---

# Production de pages dataset — Eco3min

> Ce skill couvre les **pages dataset** : séries d'une source primaire (FRED, ECB SDMX, IMF, BIS, BLS, Eurostat, Shiller, World Bank, CoinGecko, LBMA, ENTSO-E, AGSI+, FAO…) **et** composites construits par Eco3min (ratios, séries réelles déflatées, indicateurs propriétaires). Format standardisé : graphique, tableau, méthodologie, régimes.
>
> Pour les **études approfondies** (research studies avec hypothèse, narrative, analyse adversariale), voir le prompt dédié en Custom Instructions de projet — ces deux formats ne se confondent pas.
>
> La **création du fichier CSV/JSON** (codage du pipeline, vérification du series_id, fréquence cron) relève d'un **skill pipeline séparé**. Ici, on suppose que le CSV `/dataset/{slug}.csv` existe déjà ou est en cours de production ; la page n'en mentionne que la cadence de mise à jour.
>
> Voir aussi `editeur-eco3min` (identité éditoriale, AMF), `formats-eco3min` (patterns rédactionnels), `visuels-eco3min` (data viz).

---

## 0. Avant de produire — identifier le CAS

Toute page dataset relève d'un des trois cas. **Le cas pilote le H1, la meta, le bloc d'accès aux données, et la présence ou non des sections composites.** On ne devine pas : le cas vient du mapping (`seo_subtype`) ou, pour les nouveaux datasets, d'une décision explicite selon la grille §3.

| Cas | `seo_subtype` (mapping) | Source réelle | H1 commence par | Sections composites |
|---|---|---|---|---|
| **A** | `fred_ticker` | FRED, **ticker réellement googlé** (DGS10, VIX, WALCL) | le **ticker** | non |
| **A'** | `non_fred_keyword` | FRED **non-googlé** OU non-FRED (Shiller, CoinGecko, ISM, IMF mirror…) | le **concept canonique** | non |
| **B** | `composite_no_ticker` | multi-source / dérivé (ratio, réel, propriétaire) | le **concept canonique** | **oui** (Construction & Components + What This Index Captures + Data Quality) |

⚠️ **Source et stratégie SEO sont deux axes orthogonaux.** Une série peut être FRED-sourcée et rester Cas A' : `PCOFFOTMUSDM` (café arabica) est confirmé sur FRED mais personne ne google ce code — le H1 vise `Arabica Coffee Price`, pas le code. Ne **jamais** déduire le H1 de la source. La question n'est pas « est-ce du FRED ? » mais « le code est-il un ticker que des gens tapent dans Google ? ». DGS10/VIX/WALCL → oui (Cas A). PCOFFOTMUSDM/PCOCOUSDM/PIORECRUSDM → non (Cas A').

---

## 1. Positionnement éditorial — pourquoi ces pages existent

Une page dataset Eco3min n'est **pas un miroir** de la source primaire (FRED, ECB, IMF, Shiller…). Elle apporte des éléments qu'on ne trouve pas sur le site amont :

1. **Macro Takeaway analytique** : ce que la série dit du régime macro actuel et de ses interactions (taux, inflation, dollar, crédit). C'est l'angle Eco3min — la donnée mise en relation.
2. **Historical Regimes** : décomposition datée et nommée, avec le mécanisme macro de chaque régime. Une page FRED/ECB ne fait pas ça.
3. **Accès programmatique unifié** : URL CSV stable Eco3min (`/dataset/{slug}.csv`) + exemples Python/R prêts à l'emploi.

**Pour un composite (Cas B), la différenciation va plus loin** : la valeur ajoutée n'est pas « enrichir une série existante » mais **construire une série qui n'existe nulle part en natif**. Net Liquidity Index, Excess CAPE Yield, Copper-Gold Ratio ne sont disponibles ni sur FRED ni sur Bloomberg en série prête à l'emploi. La section **Construction & Components** (§7) est l'élément différenciant SEO de ces pages : c'est exactement ce que les gens googlent (« how is net liquidity index calculated », « real interest rate formula »).

**Test de qualité (Cas A / A')** : si la page peut être remplacée par un lien vers la source primaire sans perte d'information, elle ne mérite pas d'être publiée.
**Test de qualité (Cas B)** : le test ci-dessus est trivial (un composite n'existe pas en série native). Le vrai test : la section Construction explique-t-elle la formule, les composantes et leur réconciliation de fréquence de façon reproductible ? Sinon, retravailler.

---

## 2. Sources de données — FRED et au-delà

Le réseau s'étend au-delà de FRED. Trois familles de sources, qui changent la rédaction du bloc d'accès aux données (§5, position « Source Data Access ») et du bloc Sources final.

| Famille | Sources | Bloc d'accès CSV public ? | Spinner / canvas |
|---|---|---|---|
| **FRED (public, CSV direct)** | FRED + ses miroirs (IMF Primary Commodity Prices, OECD via FRED, etc.) | Oui — `fredgraph.csv?id=CODE` | `data-series` = code FRED majuscules |
| **Non-FRED à API/CSV** | ECB SDMX, Eurostat, IMF (PCP, COFER), BIS, World Bank, AGSI+/GIE, ENTSO-E, FAO, CoinGecko | Pas de fredgraph — pointer la **page source** (pas forcément un CSV direct) ou seulement le CSV Eco3min | `data-series` = code source réel ; si le script de chart global ne sait pas lire cette source, le graphique peut être omis (voir §14.1) |
| **Composite (dérivé)** | Construit par Eco3min à partir de 2+ séries (FRED et/ou non-FRED) | **Pas de fredgraph unique.** Si toutes les composantes sont FRED-publiques → lister les séries composantes. Sinon → CSV Eco3min uniquement | `data-series` = **code interne** (NET_LIQ, SP500_M2…) — jamais en SEO |

**Conséquences directes :**
- Le texte du spinner est **`Loading data…`** (générique), pas `Loading FRED data…` — il sert pour toutes les sources.
- La méthodologie ne dit `pull from the FRED API` que si la source EST FRED. Pour ECB → « pull from the ECB SDMX API », pour Shiller → « pull Shiller's ie_data.xls workbook », pour un composite → « recomputed by an Eco3min pipeline that combines… ».
- Ne **jamais** citer « FRED » comme source unique d'un composite qui a une composante non-FRED (Shiller, Damodaran, CoinGecko, LBMA).

---

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
| Non-FRED (crypto) | `Bitcoin Price History (BTC-USD): Daily Data Since 2010` | `bitcoin price history` |
| Non-FRED (métal précieux) | `Silver Price History: Daily Spot Price Since 1968 (LBMA Fix)` | `silver price history` |

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

---

## 5. Structure HTML complète

Le template ci-dessous est l'anatomie standard, **alignée sur l'anatomie cible de l'optimiseur Phase 2** : une page produite ainsi n'a pas à être re-restructurée. Les sections marquées **[COMPOSITE]** n'apparaissent **que pour le Cas B**. La section d'accès aux données s'adapte à la source (§2).

```html
<section class="eco3min-dataset">

<!-- 1. INTRO ÉDITORIALE -->
<p class="eco3min-intro">
  [Cas A/A' : 2-3 phrases. Phrase 1 = ce qu'est l'indicateur. Phrase 2 = couverture/source. Optionnel : particularité.]
  [Cas B : 4-5 phrases denses. Nommer le concept canonique 2×. Mention explicite "an Eco3min composite" / "Eco3min calculation". Formule simplifiée. Couverture précise.]
</p>

<!-- 2. LIGNE META — date dynamique -->
<p style="font-size: 13px; color: #64748b; margin-top: 6px;">
  Dataset: [Nom complet] ([période]) &middot; Updated [eco3min_latest dataset_id="[slug]" field="latest_date"]
</p>

<!-- 3. KEY STATS + DOWNLOAD (shortcodes) -->
[eco3min_key_stats dataset_id="[slug]"]
[eco3min_download dataset_id="[slug]"]

<hr />

<!-- 4. GRAPHIQUE DYNAMIQUE — spinner GÉNÉRIQUE, source-agnostique -->
<!-- Si le data-series n'est pas lisible par le script de chart global (code interne composite, source non supportée), voir §14.1 : adapter le script ou OMETTRE ce bloc. -->
<div style="margin:28px 0 36px;position:relative;background:#fff;border:1px solid #e2e0dc;padding:20px 16px 12px;min-height:280px;">
  <div class="eco3min-ds-loading" style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;background:rgba(255,255,255,.92);font-family:'JetBrains Mono',monospace;font-size:.75rem;color:#7a7a7a;z-index:2;gap:10px;">
    <span style="width:22px;height:22px;border:2px solid #e2e0dc;border-top-color:#1a237e;border-radius:50%;animation:ds-spin .8s linear infinite;display:inline-block;"></span>
    Loading data…
  </div>
  <canvas data-series="[CODE SOURCE ou CODE INTERNE]" data-start="[YYYY-MM-DD]" data-label="[Nom indicateur]" data-unit="[unité]" data-color="#1a237e" style="width:100%;max-height:300px;"></canvas>
</div>
<p style="font-size:.65rem;color:#b3b3b3;font-family:'JetBrains Mono',monospace;margin:-28px 0 28px;">Source: [Source primaire] &middot; [Institution complète]</p>
<style>@keyframes ds-spin{to{transform:rotate(360deg)}}</style>

<hr />

<!-- 5. MACRO TAKEAWAY (cœur éditorial) -->
<h2>Macro Takeaway</h2>
<div style="border-left: 3px solid #0f204b; padding: 16px 20px; background: #f8fafc; margin: 16px 0 24px;">
  <p style="margin: 0 0 10px; font-size: 15px; line-height: 1.65;">[§1 — mécanisme macro + interactions, AVEC un lien interne contextuel]</p>
  <p style="margin: 0; font-size: 15px; line-height: 1.65;">[§2 — épisode historique récent daté, chiffres sourcés]</p>
</div>

<hr />

<!-- 5bis. [COMPOSITE] CONSTRUCTION & COMPONENTS — section centrale Cas B -->
<h2>Construction &amp; Components</h2>
<p>[Logique du composite en 2-3 lignes : ce qu'il isole, quelles distorsions il retire.]</p>
<p><strong>Formula:</strong></p>
<pre>[Formule en notation simple, une ligne]
e.g.  Net Liquidity = WALCL − TGA − RRP
      Real Rate     = DGS10 − CPI YoY
      Copper-Gold Ratio = Copper (HG) / Gold (GOLDPMGBD228NLBM)</pre>
<p><strong>Components:</strong></p>
<ul>
  <li><strong>[Composante 1]</strong> — [code/source] — [fréquence native]. [Rôle dans la formule].</li>
  <li><strong>[Composante 2]</strong> — [code/source] — [fréquence]. [Rôle].</li>
</ul>
<p><strong>Frequency reconciliation:</strong> [Comment Eco3min réconcilie les fréquences. Ex : "WALCL is weekly H.4.1; TGA and RRP are daily; the composite forward-fills WALCL between releases." Ou : "All components are monthly; no interpolation."]</p>
<p><strong>Coverage:</strong> [Plage + raison des limites historiques. Ex : "1962-present, limited by DGS10 daily start on FRED."]</p>

<hr />

<!-- 6. DATASET OVERVIEW -->
<h2>Dataset Overview</h2>
<table class="eco3min-table"><tbody>
  <tr><th>Indicator</th><td>[Nom complet] ([période])</td></tr>
  <tr><th>Geography</th><td>[Zone]</td></tr>
  <tr><th>Frequency</th><td>[Daily / Weekly / Monthly / Quarterly]</td></tr>
  <tr><th>Period</th><td>[YYYY–YYYY]</td></tr>
  <tr><th>Variables</th><td>[colonnes CSV]</td></tr>
  <tr><th>Format</th><td>CSV, Excel (XLSX)</td></tr>
  <tr><th>Sources</th><td>[Source(s) primaire(s) — toutes les composantes si composite]</td></tr>
  <tr><th>Last updated</th><td>[eco3min_latest dataset_id="[slug]" field="end_date"]</td></tr>
</tbody></table>

<hr />

<!-- 7. DATASET VARIABLES -->
<h2>Dataset Variables</h2>
<p>The CSV and Excel files contain the following columns.</p>
<table class="eco3min-table">
<thead><tr><th>Column</th><th>Type</th><th>Description</th></tr></thead>
<tbody>
  <tr><td><code>date</code></td><td>Date (YYYY-MM-DD)</td><td>Observation date</td></tr>
  <tr><td><code>[colonne]</code></td><td>[Float / Integer]</td><td>[Description]</td></tr>
</tbody></table>
<p style="font-size: 13px; color: #64748b;">Column names match the CSV headers exactly.</p>

<hr />

<!-- 8. DOWNLOAD -->
<h2>Download the Complete Dataset</h2>
<p>The full [Nom] dataset is available in CSV and Excel formats.</p>
[eco3min_download dataset_id="[slug]"]

<hr />

<!-- 9. ACCÈS DONNÉES — DÉPEND DE LA SOURCE (voir §2) -->
<!-- Cas A / A' FRED-public : -->
<h2>FRED Direct CSV Access</h2>
<p>The underlying data is available from FRED under series code <strong>[CODE]</strong>:</p>
<pre>https://fred.stlouisfed.org/graph/fredgraph.csv?id=[CODE]</pre>

<!-- Cas B composite 100% FRED-public : remplacer le titre par "Source FRED Series Used for This Composite" + lister chaque composante (1 fredgraph par composante). -->
<!-- Cas A' non-FRED (Shiller, CoinGecko, ISM, LBMA…) OU composite à composante non-FRED : SUPPRIMER le bloc FRED ci-dessus. Garder uniquement le bloc Eco3min ci-dessous (et, optionnellement, un lien vers la page source amont — pas forcément un CSV direct). -->

<h3>Direct CSV Access — Eco3min Structured Dataset</h3>
<pre>https://eco3min.fr/dataset/[slug].csv</pre>
<p style="font-size: 13px; color: #64748b;">This URL returns the complete dataset in CSV format. It can be used directly in pandas, R, curl, or any data tool.</p>

<hr />

<!-- 10. PYTHON -->
<h2>Using the Dataset in Python</h2>
<pre>import pandas as pd

url = "https://eco3min.fr/dataset/[slug].csv"
df = pd.read_csv(url, parse_dates=["date"])

print(df.head())
print(df.describe())
</pre>

<!-- 11. R -->
<h2>Using the Dataset in R</h2>
<pre>library(readr)

url &lt;- "https://eco3min.fr/dataset/[slug].csv"
df &lt;- read_csv(url)

head(df)
summary(df)
</pre>
<p style="font-size: 13px; color: #64748b;">Both examples load the dataset directly from the URL &mdash; no download or API key required.</p>

<hr />

<!-- 12. METHODOLOGY — décrit le PIPELINE (pas la formule, qui est en Construction) -->
<h2>Methodology</h2>
<p>[§1 — comment Eco3min produit la donnée : source amont, cadence, alignement. Adapter la source : "pull from the FRED API" / "from the ECB SDMX API" / "from Shiller's ie_data.xls". Pour un composite : "recomputed by an Eco3min pipeline that combines [composantes] according to the formula above".]</p>
<p>[§2 — base de calcul, fenêtre, fréquence de publication amont, validation. Cas B : ne PAS recopier la formule.]</p>

<hr />

<!-- 12bis. [COMPOSITE] DATA QUALITY & PROVIDER NOTES -->
<h2>Data Quality &amp; Provider Notes</h2>
<p>[Latence dictée par la composante la plus lente. Ex : "Latency is set by the weekly H.4.1 release; the composite cannot be fresher than one week."]</p>
<p>[Révisions : chaque composante révisée propage au composite. Ex : "When CPI is revised, the full Real Interest Rates series upstream of the revision changes; Eco3min replaces the entire CSV on each release."]</p>
<p>[Sources alternatives : le plus souvent AUCUNE source native (Bloomberg n'a pas ce composite). C'est le point de différenciation. Si une alternative payante existe, la nommer factuellement.]</p>

<hr />

<!-- 12ter. [COMPOSITE] WHAT THIS INDEX CAPTURES (AND WHAT IT DOESN'T) -->
<h2>What This Index Captures (And What It Doesn't)</h2>
<p>[1-2 lignes d'intro : indicateur structurel, pas outil de market-timing.]</p>
<p><strong>What it captures:</strong></p>
<ul>
  <li>[Aspect 1 que le composite isole bien]</li>
  <li>[Aspect 2]</li>
  <li>[Aspect 3]</li>
</ul>
<p><strong>What it does NOT capture (common misinterpretations):</strong></p>
<ul>
  <li><strong>[Misinterprétation 1].</strong> [2-3 phrases factuelles, jamais prescriptives].</li>
  <li><strong>[Misinterprétation 2].</strong> [Idem].</li>
  <li><strong>[Misinterprétation 3].</strong> [Idem].</li>
  <li><strong>[Misinterprétation 4 — optionnel].</strong> [Idem].</li>
</ul>
<p>[Phrase de clôture : usage responsable, factuel — ex : "most useful as a regime-classification tool, not a tactical allocation trigger".]</p>

<hr />

<!-- 13. HISTORICAL REGIMES (signature Eco3min) — <p> OU <ul>, au choix -->
<h2>Historical Regimes</h2>
<p><strong>[Période — Nom du régime].</strong> [Caractérisation macro + chiffre clé + mécanisme.]</p>
<p><strong>[Période — Nom].</strong> [Idem.]</p>
<!-- 4 à 6 régimes. Variante <ul><li><strong>…</strong></li></ul> acceptée (cf. page Excess CAPE Yield de référence). -->

<hr />

<!-- 14. RELATED MACROECONOMIC DATASETS -->
<h2>Related Macroeconomic Datasets</h2>
<div class="eco3min-dataset-nav"><ul>
  <li><a href="[URL dataset 1]">[Nom]</a> — [raison du lien, optionnel]</li>
  <li><a href="[URL dataset 2]">[Nom]</a></li>
  <li><a href="[URL dataset 3]">[Nom]</a></li>
  <li><a href="[URL dataset 4]">[Nom]</a></li>
</ul></div>

<!-- 15. RELATED RESEARCH (vers études) — inclut l'étude au nom proche (DONNÉE vs ANALYSE) -->
<h2>Related Research</h2>
<div class="eco3min-dataset-nav"><ul>
  <li><a href="[URL étude 1]">[Titre étude]</a></li>
</ul></div>

<!-- 15bis. [Si info.cluster != null] bloc "Deep analytical framework" vers le MAJEUR du cluster -->

<hr />

<!-- 16. CTA HUB -->
<h2>Macroeconomic Dataset Hub</h2>
<p>This dataset is part of the Eco3min macro-financial data repository.</p>
<a href="https://eco3min.fr/en/research-data/" style="display:inline-block; padding:12px 20px; background:#0f204b; color:#ffffff; text-decoration:none; font-size:13px; text-transform:uppercase; letter-spacing:0.5px; font-weight:bold; border-radius:4px;">Explore the Eco3min Dataset Hub</a>

<hr />

<!-- 17. SOURCES — toutes les composantes nommées si composite -->
<h2>Sources</h2>
<ul>
  <li>[Source 1] — [précision]</li>
  <li>[Source 2] — [précision]</li>
</ul>

<hr />

<!-- 18. DATASET REFERENCE -->
<h2>Dataset Reference</h2>
<textarea style="width:100%; height:80px; font-size:13px; font-family:monospace; background:#f8fafc; padding:10px; border:1px solid #cbd5e1; border-radius:4px;" readonly="readonly">Eco3min Research. ([année]). [Nom complet] ([période]).
https://eco3min.fr[URL canonique]</textarea>

</section>
```

**Ordre des sections (immuable).** Cas A/A' : 1→18 en sautant les blocs [COMPOSITE]. Cas B : tous les blocs, l'ordre canonique étant intro → shortcodes → chart → Macro Takeaway → **Construction & Components** → Overview → Variables → Download → accès données → Python/R → Methodology → **Data Quality** → **What This Index Captures** → Historical Regimes → Related → Hub → Sources → Reference (anatomie identique à la page Excess CAPE Yield de référence).

### 5.1 Préservation byte-level (révision d'une page existante)

Ne **jamais** réécrire ni supprimer : les shortcodes `[eco3min_latest|key_stats|download …]`, le `<canvas data-series="…">` (**même si data-series contient un code interne** `NET_LIQ`/`SP500_M2` — identifiant technique JS), le `<style>@keyframes ds-spin{…}</style>`, les `<pre>` Python/R, les tableaux Overview et Variables.

---

## 6. Macro Takeaway — section critique

Valeur ajoutée vs un miroir de la source. Positionne la série dans le système macro et illustre un mécanisme par un épisode daté.

**Paragraphe 1 — mécanisme structurel.** Rôle de la série dans la lecture macro ; variables avec lesquelles elle interagit (taux, inflation, dollar, crédit) ; **au moins un lien interne contextuel** ; 3-4 phrases denses. Cas B : nommer le concept canonique, et si une étude porte un nom proche, mailler l'étude sans reprendre son angle.

**Paragraphe 2 — illustration récente.** Épisode daté précis, chiffres datés, mécanisme expliqué (le pourquoi, pas que le combien) ; 3-4 phrases.

**Conformité AMF — descriptif, jamais prescriptif :**
- ✅ « The 2022 correction illustrated this duration sensitivity: the Nasdaq fell 33% as the 10-year yield rose from 1.5% to above 4%. »
- ❌ « Investors should reduce Nasdaq exposure when the 10-year yield rises. »
- Pas de prédiction matérialisée (« the index will likely… », « the next move should… »). Tout au passé descriptif ou présent factuel.

---

## 7. Construction & Components — [COMPOSITE], section centrale

200-300 mots. C'est l'élément différenciant SEO du Cas B : ce que les gens googlent (« how is X calculated », « X formula »). Quatre blocs imposés (cf. template §5, 5bis) :

1. **Formula** — notation mathématique simple, sur une ligne (`A − B`, `A / B`), jamais en prose.
2. **Components** — chaque composante : nom canonique + code/source + **fréquence native** + rôle. Nommer par la source canonique (« Fed Funds Effective Rate (FEDFUNDS) », pas « the Fed Funds rate »).
3. **Frequency reconciliation** — comment Eco3min aligne des fréquences hétérogènes (interpolation, forward-fill, ou « all monthly, no interpolation »).
4. **Coverage** — plage précise + raison des bornes historiques.

Distinction stricte avec Methodology : **Construction = la formule et les composantes** ; **Methodology = le pipeline** (comment Eco3min produit techniquement la donnée). Ne pas dupliquer la formule en Methodology.

---

## 8. What This Index Captures (And What It Doesn't) — [COMPOSITE]

250-350 mots. Combine pédagogie + AMF + différenciation. Remplace le « Common Pitfalls » des datasets bruts, plus adapté aux composites interprétables.

- **What it captures** : 3 aspects que le composite isole bien. Rester descriptif — ❌ « use this indicator to time… ».
- **What it does NOT capture** : 3-4 misinterprétations, chacune en `<strong>` + 2-3 phrases factuelles. Cibles fréquentes : confusion stock vs variation, causalité présumée vers les prix d'actifs, périmètre géographique, qualité vs quantité, décalage d'un proxy (CPI trailing vs anticipations).
- Clôture factuelle sur l'usage responsable (outil de classification de régime ≠ déclencheur tactique).

AMF renforcé : les composites sont **plus interprétables** donc plus risqués (« Net Liquidity tombe → vendre »). Vigilance maximale, voir §16.

---

## 9. Data Quality & Provider Notes — [COMPOSITE]

Trois angles spécifiques aux composites :
- **Latence dictée par la composante la plus lente** (une composante weekly H.4.1 plafonne la fraîcheur à une semaine).
- **Propagation des révisions** : toute composante révisée (CPI, earnings Shiller) change le composite en amont de la révision → Eco3min remplace le CSV entier à chaque release.
- **Sources alternatives** : le plus souvent **aucune** série native équivalente (point de différenciation). Si une alternative payante existe (ex. GMO 7-Year Forecast pour Excess CAPE Yield), la nommer factuellement.

---

## 10. Historical Regimes — signature Eco3min

4 à 6 régimes datés et nommés. Format `<p><strong>[Période] — [Nom].</strong> …</p>` **ou** `<ul><li><strong>…</strong></li></ul>` (les deux acceptés ; la page Excess CAPE Yield de référence utilise `<ul>`).

- **Nom distinctif** : « Dot-com bubble », « Zero real-rate era », « AI and concentration » — pas « Period 1 ».
- **Chiffres datés systématiquement** : « surged from 1,000 to 5,048 in five years », pas « rose strongly ».
- **Mécanisme exprimé** : pourquoi ce régime.
- **Cohérence cross-régime** : enchaînement logique, paramètre de transition visible.
- Cas B : concept canonique mentionné 3-4× dans la section ; 2-3 liens datasets + 1-2 liens études.

AMF : ✅ « Many stocks lost 90-99% of their value » (factuel) · ❌ « Investors who held growth stocks regretted not diversifying » (jugement rétroactif).

---

## 11. Intro éditoriale

`<p class="eco3min-intro">` en ouverture.

**Cas A/A'** — 2-3 phrases : (1) ce qu'est l'indicateur ; (2) couverture/source ; (3 optionnel) particularité. Pas de « Welcome », « In this page », « Discover ». On entre dans la définition.

**Cas B** — 4-5 phrases denses : concept canonique nommé **2×** + mention explicite **« an Eco3min composite »/« Eco3min calculation »** + composantes principales (formule simplifiée) + couverture précise.

---

## 12. Sourcing — règles strictes

### 12.1 Sources primaires nommées
Au minimum **2 sources nommées** dans le bloc Sources : l'éditeur de la donnée + l'agrégateur via lequel Eco3min extrait. Pour un composite, **toutes** les composantes.
Cas miroir (commodities) : nommer la source d'origine ET le miroir — « IMF Primary Commodity Prices (via FRED series PCOFFOTMUSDM) ».

### 12.2 Format dans le texte
Sources intégrées au flux, jamais en bibliographie : « FRED series NASDAQCOM », « ECB SDMX, BSI dataset », « ENTSO-E Transparency Platform », « Robert Shiller, Yale (ie_data.xls) », « CoinGecko API ».

### 12.3 Whitelist des sources autorisées
FRED, NBER, BIS, BEA, BLS, Shiller (Yale ie_data), ECB SDW / SDMX, Eurostat, Banque de France, INSEE, IMF (WEO, Primary Commodity Prices, COFER), OECD, World Bank, Damodaran (NYU Stern), Kenneth French data library, S&P Dow Jones Indices, MSCI, CBOE, **CoinGecko, LBMA, AGSI+/GIE, ENTSO-E Transparency Platform, FAO**.

Toute autre source nommée doit être **web_search-vérifiée** avant publication. Les sources sous licence/paywall (EPEX/Nord Pool électricité, Caixin PMI, etc.) ne sont pas redistribuables : si une donnée en dépend, NE PAS produire la page avant résolution de la licence.

---

## 13. Maillage interne

| Section | Liens | Cohérence linguistique |
|---|---|---|
| Macro Takeaway | 1-2 liens contextuels vers datasets/piliers connexes | EN→EN, FR→FR strict |
| Related Macroeconomic Datasets | 4-6 liens vers autres datasets | Idem |
| Related Research | 1-3 liens vers études (dont l'étude au nom proche, Cas B) | Idem |
| Deep analytical framework | 1 lien vers le MAJEUR si `info.cluster != null` | Idem |
| CTA Hub | 1 lien vers `/en/research-data/` ou `/research-data/` | Idem |

**Total** : minimum 6 liens, idéalement 8-10, jamais plus de 12. Test silencieux par lien : « le lecteur de cette page veut probablement aussi [lien] parce que [raison précise] » ; sinon on retire. **Pas d'auto-référence.**

---

## 14. Conventions techniques

### 14.1 Canvas (graphique dynamique)

```html
<canvas data-series="[CODE]" data-start="[YYYY-MM-DD]" data-label="[Nom]"
        data-unit="[unit]" data-color="#1a237e" style="width:100%;max-height:300px;"></canvas>
```

- `data-series` = code source en MAJUSCULES (FRED : `NASDAQCOM` ; ECB/IMF/OECD : clé native) **ou code interne composite** (`NET_LIQ`). Ce n'est jamais le mot-clé SEO.
- `data-start` = `YYYY-MM-DD` de la première observation. `data-unit` = `$`, `%`, `bp`, `index 100 = 2015`… `data-color` = `#1a237e` par défaut.
- **Lisibilité par le script de chart** : le canvas est rendu par un script global du site. Si ce script ne sait lire qu'une source (ex. FRED) et que le `data-series` est un code interne composite ou une source non supportée, **le graphique ne se chargera pas**. Deux options : (a) le script de chart sait lire le CSV Eco3min `/dataset/{slug}.csv` → garder le canvas ; (b) sinon → **omettre le bloc graphique** (c'est le choix de la page Excess CAPE Yield de référence, qui n'a pas de canvas). Trancher selon ce que supporte réellement le script global — ne pas laisser un canvas mort.

### 14.2 Shortcodes Eco3min

| Shortcode | Usage |
|---|---|
| `[eco3min_latest dataset_id="[slug]" field="latest_date"]` | Date de la dernière observation |
| `[eco3min_latest dataset_id="[slug]" field="end_date"]` | Date d'extraction du pipeline |
| `[eco3min_key_stats dataset_id="[slug]"]` | Stats résumées (min, max, moyenne, dernière valeur) |
| `[eco3min_download dataset_id="[slug]"]` | Boutons CSV / XLSX |

Le `dataset_id` matche toujours exactement le slug `/dataset/{slug}.csv`.

### 14.3 Pipeline de données (référence légère)

La page reflète un CSV/JSON mis à jour automatiquement. **Le détail du pipeline (codage, series_id, cron, connecteur API) relève du skill pipeline séparé.** Ici, on ne retient que la cadence pour la Methodology :
- Pipeline FRED : daily cron (Mon–Sat) via GitHub Actions, SFTP OVH.
- Pipeline ECB : daily cron décalé du FRED.
- Pipelines spécifiques (Shiller ie_data, CoinGecko, World Bank Pink Sheet, IMF, ENTSO-E, AGSI…) : fréquence variable, souvent mensuelle ou alignée sur la release amont.
- WordPress touch endpoint rafraîchit `dateModified` pour l'indexation Google.

La Methodology mentionne brièvement la cadence, adaptée à la source (« updated daily via automated pull from the FRED API » / « monthly, after Shiller refreshes ie_data.xls »).

---

## 15. Bilingue FR/EN

Pour une paire FR/EN du même dataset :
- **Structure HTML strictement identique** entre langues.
- **Même `dataset_id`** (même CSV sous-jacent).
- **Liens internes différents** : EN→URLs EN, FR→URLs FR.
- **Macro Takeaway, Construction, What This Captures, Historical Regimes traduits intelligemment**, pas calques littéraux. Le concept canonique se traduit ou reste en anglais selon l'usage googlé FR (souvent « ratio CAPE », « taux réels » côté FR).
- **Codes Python/R inchangés.** **Sources identiques** (FRED reste FRED).

> Note opérationnelle : l'optimiseur Phase 2 composites travaille **EN-first** (focus keywords et exemples anglais). Si tu optimises seulement l'EN, surveille la dérive des paires FR — produire/réviser les deux dans la même passe quand c'est possible.

---

## 16. Conformité AMF

Les 6 règles de `editeur-eco3min` s'appliquent. Spécificités datasets :

| Règle | Application |
|---|---|
| 1 — Pas de % d'allocation | Aucune mention de « X% allocation to this index », même en exemple |
| 2 — Pas de « should/devrait » | Macro Takeaway, Historical Regimes, What This Captures en descriptif |
| 3 — Pas de « Buy when Y » | Aucun signal d'entrée matérialisé |
| 4 — N/A (pas de FAQ ici) | — |
| 5 — Comparaisons géographiques en chiffres | OK si statistique, pas prescriptif |
| 6 — Timing en observation empirique datée | « The 2022 correction saw… », pas « The next correction will… » |

**Vigilance renforcée Cas B.** Anti-patterns composites :
❌ « When Net Liquidity drops below X, sell equities » · ❌ « Investors should monitor Real Interest Rates closely » · ❌ « A high Excess CAPE Yield signals attractive equity allocation » · ❌ « Use Mortgage Spread to time the housing cycle ».
✅ « Between 2020 and 2022, periods of rapid Net Liquidity expansion coincided with… » · ✅ « Historically, Real Interest Rates above 4% preceded equity drawdowns ≥20% in N of M cases since 1962 ».

---

## 17. Pas de JavaScript

Aucun `<script>`, `onclick`, event handler dans la page. Le graphique dynamique est rendu par le script global du site lisant le `<canvas>`. Aucun JS/CSS inline hors le `<style>@keyframes ds-spin>` du template.

---

## 18. Critère de publication

- **Cas A/A'** : la page apporte-t-elle quelque chose qu'un lien direct vers la source ne fournit pas ? (Macro Takeaway + Historical Regimes répondent oui.)
- **Cas B** : la section Construction explique-t-elle formule + composantes + réconciliation de fréquence de façon reproductible ? La séparation DONNÉE/ANALYSE vs l'étude homonyme est-elle tenue ?
- Le H1 respecte-t-il le cas (A : ticker ; A'/B : concept canonique ; jamais le code interne) ?
- Le Macro Takeaway lie au moins une autre série ou un pilier ?
- Au moins 4 régimes historiques avec chiffres datés ?
- Au moins 6 liens internes, tous justifiés ?
- Le bloc d'accès aux données correspond-il à la **source réelle** (pas de « FRED » sur une page Shiller/CoinGecko ; pas de spinner « Loading FRED data ») ?
- Le `dataset_id` est stable et matche le CSV en production ?

Si une seule condition échoue, retravailler.

---

## 19. Checklist pré-publication

**Cas & SEO**
- [ ] Cas identifié (A / A' / B) ; H1 conforme (ticker pour A, concept canonique pour A'/B)
- [ ] Code interne (NET_LIQ, SP500_M2…) absent du H1 / meta title / meta description
- [ ] Source ≠ stratégie SEO : un FRED non-googlé (café, fer) est bien traité en Cas A'
- [ ] [Cas B] mention « Eco3min composite/calculation » dans intro et/ou methodology
- [ ] Meta title commence par le ticker (A) ou le concept (A'/B), longueur acceptable
- [ ] Focus keyword = ticker (A) ou concept canonique en minuscules (A'/B)

**Source & accès données**
- [ ] Spinner = `Loading data…` (générique), pas `Loading FRED data…`
- [ ] Bloc d'accès données adapté : FRED fredgraph gardé si FRED-public ; supprimé/adapté sinon
- [ ] [Cas B] composantes FRED listées si 100% FRED-public ; sinon CSV Eco3min seul
- [ ] `data-series` = code source/interne ; canvas rendu OU omis selon support du script (§14.1)
- [ ] Sources finales = toutes les composantes (Cas B) + éditeur + agrégateur (≥2)

**Sections composites [Cas B]**
- [ ] Construction & Components présente (Formula + Components + Frequency reconciliation + Coverage)
- [ ] What This Index Captures présente (3-4 misinterprétations)
- [ ] Data Quality & Provider Notes présente (latence composante lente + propagation révisions)
- [ ] Concept canonique mentionné ≥ 5× au total

**Macro Takeaway**
- [ ] 2 paragraphes (mécanisme + illustration datée), ≥1 lien interne, AMF-compliant

**Historical Regimes**
- [ ] 4-6 régimes datés/nommés, chiffre + mécanisme par régime, enchaînement logique

**Métadonnées & code**
- [ ] Overview complet ; Variables = colonnes CSV exactes ; `[eco3min_latest]` pour la date
- [ ] Exemple Python (pandas) + R (readr) avec URL CSV Eco3min

**Maillage**
- [ ] ≥6 liens internes, cohérence linguistique stricte, Related Datasets ≠ Related Research, CTA Hub
- [ ] [si cluster] bloc « Deep analytical framework » vers le MAJEUR ; pas d'auto-référence

**AMF**
- [ ] Aucun « should », « advised », « buy when » ; descriptif ; pas de prédiction (vigilance renforcée Cas B)

**Citation**
- [ ] Année courante + URL canonique `/en/{slug}/`

---

## RAPPEL BLOQUANT — Zéro commentaire HTML dans le contenu publié

Les marqueurs de section en commentaire HTML utilisés dans les templates de ce skill
(`<!-- 1. INTRO -->`, `<!-- 5. MACRO TAKEAWAY -->`, etc.) sont des **repères d'assemblage**.
Ils ne survivent pas dans le HTML livré : on les retire avant de coller le contenu ou d'émettre
le bundle.

Motif : Autoptimize scanne `<script>` / `<style>` en regex **sans ignorer les commentaires HTML**.
Une balise littérale citée en prose dans un commentaire fait avaler du texte au minifieur JS,
provoque une fatale dans le callback de buffer et renvoie un **HTTP 500 avec le corps complet** —
page normale dans le navigateur, invisible pour Google. Incident du 27 août 2026, 8 pages
désindexées. `wpautop` mutile en plus ces commentaires (enveloppe en `<p>`, saut de ligne inséré
au milieu dès qu'un nom de balise bloc y figure).

Règle canonique, vérifications mécaniques et alternative (commentaire PHP dans le snippet) :
voir `eco3min-import-contenu-bilingue`, section « RÈGLE FIGÉE (août 2026) ».

Contrôle avant livraison :

```python
import re
assert not re.findall(r'<!--.*?-->', html, re.S), "commentaire HTML dans le contenu"
```

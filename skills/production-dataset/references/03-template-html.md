# production-dataset — référence : Template HTML complet des 18 blocs, ordre des sections, préservation byte-level (§5, §5.1)

Extrait VERBATIM de SKILL.md (découpage du 16/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

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

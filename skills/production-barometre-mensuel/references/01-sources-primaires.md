# production-barometre-mensuel — référence : Sources primaires par indicateur (§1.1 à §1.11)

Extrait VERBATIM de SKILL.md (découpage du 16/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 1. Protocole de recherche — sources primaires par section

### 1.1 Indicateurs de cycle (NFCI, Sahm, SOS)

**NFCI (Chicago Fed National Financial Conditions Index)**
```
Recherche : web_fetch https://fred.stlouisfed.org/graph/fredgraph.csv?id=NFCI&vintage_date=[AAAA-MM-JJ]
OU : web_search "NFCI Chicago Fed latest week [mois] [année]"
Source primaire : Federal Reserve Bank of Chicago / FRED series NFCI
Format attendu : valeur à deux décimales, date de la semaine se terminant le [date]
Note : préciser les sous-indices si disponibles (NFCIRISK, NFCICREDIT, NFCILEVERAGE)
```

**Sahm Rule (temps réel)**
```
Recherche : web_fetch https://fred.stlouisfed.org/graph/fredgraph.csv?id=SAHMREALTIME
Source primaire : FRED series SAHMREALTIME (temps réel, pas SAHMCURRENT)
Format attendu : valeur à deux décimales, mois de référence
Note dans le texte : "Source: FRED, series SAHMREALTIME"
```

**SOS (Richmond Fed / Philadelphia Fed)**
```
Recherche : web_fetch https://www.richmondfed.org/research/national_economy/sos_recession_indicator
Source primaire : Federal Reserve Bank of Richmond
Format attendu : valeur, date de la semaine se terminant le [date], "last updated [date]"
```

**ICSA (inscriptions chômage)**
```
Recherche : web_fetch https://fred.stlouisfed.org/graph/fredgraph.csv?id=ICSA
Source primaire : FRED series ICSA / U.S. Employment and Training Administration
Format attendu : valeur en milliers, date de la semaine
```

### 1.2 Données Fed / FOMC

**Décision FOMC**
```
Recherche : web_search "FOMC statement [mois] [année] Federal Reserve"
OU : web_fetch https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
Source primaire : Federal Reserve Board, communiqué officiel
Collecter : taux décidé (fourchette), résultat du vote (X-Y), dissidents nommés, formulation
exacte sur l'inflation dans le communiqué
⚠ AMF : citer uniquement ce qui figure dans le communiqué officiel. Aucune interprétation
directionnelle ("le Fed va baisser" = interdit). "Le communiqué décrit désormais l'inflation
comme [citation exacte]" = correct.
```

**Fed Funds, taux directeurs**
```
Recherche : web_fetch https://fred.stlouisfed.org/graph/fredgraph.csv?id=FEDFUNDS
Source : FRED series FEDFUNDS
```

### 1.3 BCE / ECB

**Décision BCE**
```
Recherche : web_search "ECB monetary policy decisions [mois] [année]"
OU : web_fetch https://www.ecb.europa.eu/press/pr/date/[année]/html/index.en.html
Source primaire : ECB Press Release officiel
Collecter : trois taux (deposit facility, main refinancing, marginal lending), vote,
formulation exacte du communiqué sur les risques
⚠ AMF : citation exacte uniquement, pas de paraphrase directionnelle
```

### 1.4 Inflation

**CPI US**
```
Recherche : web_search "BLS CPI [mois] [année] year-over-year"
OU : web_fetch https://www.bls.gov/news.release/cpi.nr0.htm
Source primaire : Bureau of Labor Statistics, Consumer Price Index Summary
Collecter : headline YoY, core YoY, variation mensuelle, composante énergie si notable
Date du communiqué à citer obligatoirement
```

**PCE / Trimmed Mean PCE**
```
Recherche : web_search "Dallas Fed Trimmed Mean PCE [mois] [année]"
OU : web_fetch https://www.dallasfed.org/research/pce
Source primaire : Federal Reserve Bank of Dallas
Série FRED : PCETRIM12M159SFRBDAL
```

**HICP zone euro**
```
Recherche : web_search "Eurostat HICP flash estimate [mois] [année]"
OU : web_fetch https://ec.europa.eu/eurostat/web/inflation
Source primaire : Eurostat flash estimate
Collecter : headline YoY, core, énergie, pays si notable
```

### 1.5 Croissance

**PIB US**
```
Recherche : web_search "BEA GDP advance estimate Q[X] [année]"
OU : web_fetch https://www.bea.gov/news/schedule
Source primaire : Bureau of Economic Analysis, GDP release
Collecter : taux SAAR, numéro d'estimation (advance/second/third), décomposition si publiée
(consommation, investissement, exports/imports)
Note : préciser "advance estimate" / "second estimate" / "third estimate"
```

**PIB zone euro**
```
Recherche : web_search "Eurostat GDP flash estimate Q[X] [année]"
Source primaire : Eurostat preliminary flash estimate
Format : taux trimestriel (q/q) + qualification (preliminary/flash)
```

### 1.6 Emploi

**NFP**
```
Recherche : web_search "BLS employment situation [mois] [année] nonfarm payrolls"
Source primaire : Bureau of Labor Statistics, The Employment Situation
Collecter : NFP du mois, révisions des 2 mois précédents (obligatoire — les révisions font partie
du récit), taux de chômage
```

### 1.7 Marchés financiers — taux

```
Toutes les séries FRED suivantes — récupérer la dernière valeur disponible au 1er du mois cible :

DGS2    → US Treasury 2Y
DGS10   → US Treasury 10Y
T10Y2Y  → Spread 10Y−2Y
MORTGAGE30US → Taux hypothécaire 30Y (Freddie Mac)
BAMLH0A0HYM2 → HY OAS (ICE BofA) — ⚠ voir note truncation FRED ci-dessous
VIXCLS  → VIX (CBOE)
T5YIFR  → 5Y5Y forward breakeven
T10YIE  → 10Y breakeven
DFII10  → Real rate 10Y

Recherche batch : web_fetch https://fred.stlouisfed.org/graph/fredgraph.csv?id=[CODE]&vintage_date=[AAAA-MM-JJ]

⚠ BAMLH0A0HYM2 : depuis avril 2026, FRED tronque à 3 ans glissants. Pour la valeur courante,
la série reste utilisable. Pour la calibration percentile de l'overlay stress, voir thresholds_spec.json.
```

### 1.8 Marchés actions

```
⚠ Note AMF et sourcing : Yahoo Finance est un agrégateur dont les CGU interdisent la redistribution
commerciale. Pour le baromètre Eco3min (site commercial), utiliser des sources officielles quand
disponibles (Euronext, NYSE, CBOE) ou mentionner explicitement "données indicatives" dans la note
de bas de tableau. La note actuelle du baromètre ("Arrows reflect the directional trend... carry no
predictive value") est conforme — la conserver.

Pour chaque indice — chercher le cours de clôture du dernier jour ouvré du mois N :
web_search "[nom indice] closing price [date]"
OU : web_fetch source officielle de la bourse concernée

Indices requis : CAC 40, Euro Stoxx 50, DAX, FTSE 100, S&P 500, Nasdaq Composite, Dow Jones
Format : valeur exacte (2 décimales), date de clôture
Flèche de tendance mensuelle : ↑ hausse / ↓ baisse / → stable (basé sur comparaison début/fin de mois)

⚠ DAX et Euro Stoxx 50 : aucune source primaire datée accessible (Deutsche Börse et STOXX inaccessibles, cycles
août et septembre 2026). Publier "n.d." et le signaler dans le rapport de cycle ; ne jamais combler par une source
secondaire.
```

### 1.9 Matières premières

```
Brent :
  web_search "Brent crude oil price [date] ICE close"
  Source : ICE Futures Europe, cours de clôture
  ⚠ Ne jamais écrire "~$108" si la valeur exacte est disponible — approximation tolérée
  uniquement si la source donne une fourchette

WTI :
  web_search "WTI crude oil price [date] NYMEX close"
  Source : NYMEX

Or :
  web_search "gold spot price [date] London Bullion"
  Source : London Bullion Market Association (LBMA)
```

### 1.10 Liquidité nette (WALCL, TGA, RRP)

```
FRED series :
  WALCL     → Fed total assets (hebdomadaire)
  WTREGEN   → Treasury General Account
  RRPONTSYD → Overnight Reverse Repo

web_fetch https://fred.stlouisfed.org/graph/fredgraph.csv?id=WALCL
(idem pour WTREGEN et RRPONTSYD)

Calcul : Net Liquidity = WALCL − WTREGEN − RRPONTSYD
Variation mensuelle = valeur fin de mois N vs valeur fin de mois N-1
```

### 1.11 Énergie — contexte géopolitique

```
Si un choc énergétique est en cours (ex. Hormuz, OPEC+, sanctions) :
  web_search "[sujet] latest [mois] [année]"
  Sources acceptables : Reuters, AP, AFP (agences de presse — faits, pas opinions)
  Source primaire préférée : communiqués officiels des gouvernements concernés, EIA
  
⚠ AMF : décrire uniquement les faits vérifiables (prix, événement, date).
"Le Brent a clôturé à $108 le 1er mai" = fact ✓
"Le conflit maintient les prix élevés" = interprétation causale → cadrer comme "selon [source]"
"Les prix pourraient monter" = prévision → INTERDIT
```

---
name: production-barometre-mensuel
description: >
  Protocole de mise à jour mensuelle du baromètre macroéconomique Eco3min (FR + EN).
  Prend le HTML du mois N en entrée, produit le HTML du mois N+1.
  Activer pour toute mise à jour mensuelle du baromètre. Couvre toutes les sections sans exception.
  Règle cardinale : zéro donnée inventée, approximée ou issue de la mémoire de l'IA —
  chaque chiffre est recherché via web_search sur source primaire institutionnelle avant d'être
  écrit. Conformité AMF intégrale. Même niveau qualitatif que le baromètre de référence.
---

# Skill — Mise à jour mensuelle du baromètre Eco3min

> **Règle absolue, non négociable.**  
> Aucun chiffre n'est écrit sans avoir été vérifié par web_search ou web_fetch sur une source
> primaire institutionnelle dans cette conversation. Ni la mémoire de l'IA ni des valeurs
> approximatives ne sont acceptables. Si une donnée n'est pas encore publiée → marqueur
> `[DONNÉE NON PUBLIÉE — à compléter après publication du XX/XX]`, jamais une estimation.

---

## 0. Déclenchement et pré-requis

### 0.1 Ce que Paul fournit
- Le HTML complet du baromètre du mois N (copié-collé ou fichier joint)
- Le mois cible (ex. "mois N = mai, produire juin")
- Optionnel : toute donnée déjà collectée (libère des recherches)

### 0.2 Ce que le skill produit
Le HTML complet du baromètre mis à jour, **toutes sections**, prêt à coller dans Gutenberg.

### 0.3 Vérification de disponibilité des données

Avant de commencer, établir la matrice de disponibilité selon la date cible.
Exemple pour un baromètre "données arrêtées au 1er juin" :

| Donnée | Disponible ? | Date de publication |
|---|---|---|
| NFP avril | ✓ | ~8 mai |
| CPI avril US | ✓ | ~13 mai |
| PIB Q1 (2e estimation) | ✓ | ~29 mai |
| FOMC juin | ✗ | 16–17 juin |
| BCE juin | ✗ | 11 juin |
| NFP mai | ✗ | ~6 juin |
| CPI mai US | ✗ | ~11 juin |

Les éléments non disponibles vont dans "Key items to watch", jamais dans les tableaux de données.

---

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

---

## 2. Protocole section par section

Appliquer dans cet ordre. Ne passer à la section suivante qu'une fois les données de la section
courante vérifiées et écrites.

### SECTION 1 — Header

**Ce qui change :**
- `baro-header__title` : "Barometer — [Mois N+1] [Année]"
- `baro-header__date span` : "1er [mois N+1], [année]" (ou date d'arrêté réelle)

**Ce qui ne change pas :** brand line, countdown div, KPI strip.

**Vérification AMF :** aucune.

---

### SECTION 2 — Commentaire shortcode [eco3min_regime]

**Ce qui change :**
- Ligne "Ce mois-ci ([mois]) : flag ACTIF/INACTIF" : mettre à jour selon Brent YoY du mois
- Ligne "Repo : github.com/[à compléter]/regime-classifier" : compléter si repo créé

**Règle flag `headline_underlying_divergence` :**
- Calculer Brent YoY au 1er du mois N+1 : `(Brent actuel / Brent il y a 12 mois − 1) × 100`
- Si YoY > +20% → flag ACTIF dans le commentaire
- Si YoY ≤ +20% → flag INACTIF

Le shortcode lui-même gère l'affichage automatiquement via le JSON — le commentaire sert
uniquement de documentation pour le prochain rédacteur.

---

### SECTION 3 — Synthèse (bloc navy)

**Rôle éditorial :** résumé de ~3 paragraphes sur les faits marquants du mois écoulé.
Structure du mois de référence (à maintenir) :
1. Fait dominant du mois (inflation, croissance, banques centrales) avec chiffres clés
2. Contre-signal ou nuance (pourquoi ce n'est pas la catastrophe ou l'euphorie)
3. Phrase de sourcing / cadrage légal

**Protocole :**
1. Collecter d'abord TOUTES les données (sections 4 à 13) avant d'écrire ce bloc
2. Identifier le fait dominant : quelle donnée a le plus bougé par rapport au mois précédent ?
3. Identifier le contre-signal : quelle donnée va dans le sens inverse ?
4. Rédiger en Libre Baskerville style (sobre, factuel, pas de jugement directionnel)

**⚠ AMF — interdits stricts dans ce bloc :**
- "l'économie va [mieux/pire]" sans ancrage empirique chiffré
- "les marchés anticipent" sans source explicite (FOMC minutes, breakevens, etc.)
- "il faut surveiller" avec implication d'action pour l'investisseur
- Toute formulation qui implique une recommandation d'allocation

**Template de structure (à adapter selon les faits du mois) :**
```
[Fait dominant avec chiffres clés vérifiés et sourcing inline]
[Contre-signal avec chiffres vérifiés — "Cependant, [indicateur] reste [description factuelle]"]
[Phrase de cadrage : "Toutes les données ci-dessous sont issues de sources institutionnelles
publiques. Aucune prévision ni recommandation d'investissement n'est formulée."]
```

**Note sur les citations :** les formulations *italiques* dans la synthèse (ex. *soft stagflation
pattern*) doivent soit être des citations directes d'une source identifiée, soit des descriptions
purement factuelles. Jamais une opinion non sourcée présentée comme un fait.

---

### SECTION 4 — Signaux de cycle (NFCI, Sahm, SOS)

Pour chaque indicateur, mettre à jour :
- La valeur numérique (`.baro-index-score__value`)
- Le texte de description (`.baro-index-reading`) : dates précises, valeurs des sous-composantes si disponibles
- La largeur de la barre (`.baro-index-bar__fill`) : calculée comme `(valeur / seuil) × 100%` pour Sahm et SOS ; pour NFCI, `(valeur + 3) / 9 × 100%` sur une échelle −3 à +6 (ajuster si la plage change)

**NFCI :** préciser la semaine exacte, le mouvement (s'est resserré / s'est assoupli), et si
disponibles les sous-indices risk/credit/leverage qui expliquent le mouvement.

**Sahm :** préciser le mois de référence, la comparaison avec le mois précédent, et rappeler
le seuil de 0.50. Sourcer `SAHMREALTIME` (pas `SAHMCURRENT`).

**SOS :** préciser la semaine exacte, "last updated [date]". Ne pas écrire "bien en dessous" sans
la valeur — toujours la valeur + le seuil.

**Note de bas de section :** conserver la note AMF actuelle (les indicateurs sont pour la
détection, pas des signaux de trading). Ne pas la modifier.

---

### SECTION 5 — Description graphique Yield curve / Sahm

Mettre à jour uniquement les valeurs explicitement mentionnées dans le texte descriptif
(`.baro-chart-desc`). Conserver le titre, les codes FRED, les liens internes.

**⚠ Règle :** si le texte descriptif dit "pour la semaine du [date], X = Y", mettre la valeur
réelle du mois. Si le texte est générique (il décrit le mécanisme, pas une valeur ponctuelle),
ne rien changer.

---

### SECTION 6 — Description graphique NFCI

Mettre à jour les valeurs ponctuelles dans `.baro-chart-desc` si elles y figurent.
Codes FRED (NFCI, NFCIRISK, NFCICREDIT, NFCILEVERAGE) : inchangés.

---

### SECTION 7 — Faits marquants (baro-signal)

**Label :** "Factual highlights — [Mois écoulé] [Année]" (le mois dont on a les données)

**Structure à maintenir :** 4–5 blocs thématiques, chacun avec `<strong>` pour le titre du fait.
Thèmes récurrents : FOMC, BCE, Inflation, Croissance, Énergie/Géopolitique.

**Pour chaque fait :**
1. Chercher le communiqué officiel de l'événement
2. Citer uniquement des chiffres présents dans ce communiqué
3. Source en fin de paragraphe : "Source: [Institution], [type de document], [date]."

**⚠ AMF — contrôle par paragraphe :**

FOMC : ✓ "Le Fed a maintenu les taux à [X]–[Y]% par un vote [A]-[B]"
       ✓ "[Nom] a voté en faveur d'une [hausse/baisse] de [X] bp"
       ✓ "Le communiqué décrit désormais l'inflation comme [citation exacte entre guillemets]"
       ✗ "Le Fed devrait baisser en [mois]" — prévision
       ✗ "Le Fed a envoyé un signal" — interprétation

BCE :  Mêmes règles. Citer exactement le communiqué de presse officiel.

Inflation : ✓ "Le CPI de [mois] ressort à [X]% en glissement annuel (publié le [date])"
            ✓ "Le composante essence a progressé de [X]% sur le mois"
            ✗ "L'inflation reste préoccupante" — jugement
            ✗ "Les prix pourraient continuer à monter" — prévision

Croissance : ✓ "Le PIB du T[X] [année] s'établit à +[X]% SAAR selon l'estimation [advance/second]
               du BEA publiée le [date]"
             ✓ Préciser le type d'estimation et si elle sera révisée
             ✗ "La croissance est solide" — jugement non ancré

Énergie : ✓ Prix de clôture avec source et date
          ✓ Événement factuel (décision OPEC, incident, accord)
          ✗ "Les prix restent sous pression" — jugement
          ✗ "Le marché craint" — attribution de sentiment au marché

---

### SECTION 8 — Description graphique Emploi (ICSA)

Mettre à jour la valeur ICSA la plus récente disponible :
- Valeur en milliers
- Date de la semaine

---

### SECTION 9 — Tableau indices boursiers

**Pour chaque ligne :** niveau de clôture (2 décimales), date de clôture, flèche mensuelle.

**Calcul de la flèche :** comparer le cours de clôture du dernier jour du mois N au cours de
clôture du dernier jour du mois N-1. ↑ = hausse, ↓ = baisse, → = variation < 0.5%.

**Date :** utiliser la date de clôture réelle (le dernier jour de bourse du mois, pas le 30 ou 31
automatiquement — vérifier si fin de mois tombe un weekend).

**Note de bas de tableau :** conserver la note sur le caractère indicatif et l'absence de valeur
prédictive des flèches. Ne pas la modifier.

---

### SECTION 10 — Tableau taux / matières premières / volatilité

Pour chaque ligne : valeur, date.

**Check de cohérence T10Y2Y :** la valeur dans ce tableau doit correspondre au signe mentionné
dans la description du graphique yield curve. Si T10Y2Y = +0.51% ici, le texte du graphique
ne peut pas dire "la courbe est inversée".

**Note de bas de tableau :** ajuster si le contexte énergétique a changé (ex. si le Brent a
repassé sous son niveau pré-conflit, la note sur "+60% au-dessus des niveaux pré-conflit" serait
fausse et doit être mise à jour ou supprimée).

---

### SECTION 11 — Description graphique Taux

Mettre à jour les valeurs ponctuelles dans `.baro-chart-desc` si elles y figurent.
Codes FRED : inchangés.

---

### SECTION 12 — Description graphique Credit Spread (HY OAS)

Mettre à jour la valeur et la date. Conserver la note sur le niveau historiquement serré si elle
est toujours exacte — vérifier le contexte percentile (la valeur est-elle toujours basse ?) en
comparant à la moyenne historique HY OAS ~5.5% ; si la valeur est autour de 3%, "historiquement
serré" reste correct.

---

### SECTION 13 — Cartes macro (US + Zone euro)

**Carte États-Unis — mettre à jour :**
- PIB : dernier chiffre publié (avec type d'estimation : advance/second/third)
- CPI : headline YoY du mois le plus récent
- Core CPI
- Fed funds (fourchette cible)
- NFP du mois le plus récent
- NFP du mois précédent avec révision si elle a eu lieu
- Taux de chômage
- NFCI dernière valeur avec date
- Sahm Rule

**Carte Zone euro — mettre à jour :**
- PIB : dernière estimation publiée (q/q)
- HICP : headline YoY
- Core HICP
- Énergie YoY si notable
- Trois taux BCE
- Prochaine décision BCE (date exacte)
- Données nationales si mentionnées (inflation France, etc.)

**⚠ Règle de sourcing :** chaque valeur doit avoir une source identifiable. Les cartes macro
sont le cœur du contenu factuel — aucune approximation tolérée. Si une donnée n'a pas encore
été publiée, laisser la valeur du mois précédent avec "(révision attendue le [date])".

---

### SECTION 14 — Description graphique Inflation et anticipations

**Valeurs à mettre à jour :**
- T10YIE (breakeven 10Y) : valeur + date
- T5YIFR (5Y5Y forward) : valeur + date
- DFII10 (taux réel 10Y) : valeur + date

**Note sur le T5YIFR :** le baromètre le décrit comme "the Fed's preferred gauge of long-run
expectations anchoring". Vérifier que cette formulation reste exacte (c'est une description
largement acceptée dans la littérature Fed — stable).

---

### SECTION 15 — Framework (bloc ambré baro-regime)

**Rôle :** analyse factuelle du mois, 4–5 paragraphes thématiques.
Thèmes récurrents : activité, emploi, inflation, banques centrales.

**Protocole :**
1. Ne rédiger ce bloc qu'après avoir collecté toutes les données
2. Chaque paragraphe est ancré sur au moins un chiffre vérifié
3. Les "nuances" (ex. "le rebond du PIB doit être lu avec prudence") sont autorisées si elles
   s'appuient sur des données (ex. "une part significative vient de [composante X]")
4. Structure suggérée : un paragraphe d'introduction de la "configuration du mois" + un
   paragraphe par thème

**⚠ AMF — contrôle de chaque paragraphe :**
- Aucune phrase commençant par "les marchés devraient" / "il faut surveiller X car Y pourrait"
- Aucune association régime → allocation (ex. "en période de stagflation, les matières premières
  surperforment" → INTERDIT même présentée comme "observation historique" sans ancrage empirique)
- Les formulations `<strong>` en bleu navy doivent souligner des faits, pas des jugements
  ("both the Fed and the ECB held rates in April" = fact ✓ ;
   "central banks are losing the battle against inflation" = opinion ✗)

---

### SECTION 16 — Key items to watch

**Label :** "Key items — [Mois N+1]–[Mois N+2] [Année] calendar"

**Structure : 5–6 items numérotés**

Chaque item = un événement futur avec date précise ou une question ouverte avec date d'éclairage.

**Sources pour le calendrier :**
```
FOMC : web_fetch https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
BCE : web_fetch https://www.ecb.europa.eu/press/calendars/mgcgc/html/index.en.html
BLS : web_fetch https://www.bls.gov/schedule/news_release/cpi.htm
BEA : web_fetch https://www.bea.gov/news/schedule
Eurostat : web_search "Eurostat release calendar [mois] [année]"
```

**Types d'items récurrents :**
- NFP du mois suivant : date précise, question analytique spécifique au contexte
- CPI du mois suivant : date précise, ce qu'on surveille (base effect, composante énergie, etc.)
- Prochaine réunion FOMC : date, contexte (SEP ou pas, dissents attendus ou pas)
- Prochaine réunion BCE : date, contexte
- Événements géopolitiques ou structurels en cours : formuler comme "situation à surveiller" avec
  les indicateurs mesurables qui l'encadrent, jamais comme prévision

**⚠ AMF :**
- "Markets will closely monitor X" = OK (description d'un comportement marché, pas une consigne)
- "You should watch X" = INTERDIT (adresse le lecteur comme investisseur)
- "X could push inflation higher" = limite ; cadrer comme "selon [institution], X pourrait..."
  si la formulation citée vient d'une source institutionnelle. Sinon : supprimer.

---

### SECTION 17 — Description graphique Liquidité nette

**Mettre à jour :**
- WALCL : dernière valeur hebdomadaire (en milliards $)
- TGA (WTREGEN) : dernière valeur
- RRP (RRPONTSYD) : dernière valeur
- Net liquidity calculée = WALCL − TGA − RRP
- Variation mensuelle approximative (différence fin de mois N vs fin de mois N-1)
- Date de référence ("As of [date]")

**Note sur le RRP :** si le RRP est proche de zéro (comme en mai 2026), le dire explicitement.
Si le RRP remonte significativement, mettre à jour la note analytique en conséquence.

---

### SECTIONS INCHANGÉES (vérification uniquement)

Ces sections ne changent normalement pas de mois en mois. Les lire pour s'assurer qu'elles
restent exactes dans le nouveau contexte.

**Baro-internal-links :** vérifier que les URLs cibles existent encore (web_fetch rapide sur
les liens internes eco3min.fr). Si une page a changé de slug, mettre à jour.

**Baro-promesse :** ne pas modifier. Si la liste des sources institutionnelles citées change
(ex. nouvelle source ajoutée), mettre à jour la liste.

**Baro-disclaimer :** NE PAS MODIFIER. Texte juridique figé.

**CSS + fonts import :** NE PAS MODIFIER.

**Descriptions de graphiques génériques (mécanisme)** : ne modifier que les valeurs ponctuelles
datées, jamais la description du mécanisme (ex. la description du mécanisme NFCI "Composite of
105 variables" est stable — vérifier seulement les chiffres ponctuels).

---

## 3. Ordre d'exécution recommandé

```
1. Lire le HTML du mois N fourni — identifier toutes les valeurs datées (liste exhaustive)
2. Établir la matrice de disponibilité (§0.3) pour le mois N+1
3. Lancer les recherches par batch selon les sections :
   Batch A (cycle) : NFCI, Sahm, SOS, ICSA
   Batch B (banques centrales) : FOMC, BCE — communiqués officiels
   Batch C (macro US) : CPI, NFP, PIB, Fed Funds
   Batch D (macro EZ) : HICP, PIB zone euro, taux BCE
   Batch E (marchés) : T-notes, spread, HY OAS, VIX, or, Brent, WTI
   Batch F (actions) : 7 indices — dernière clôture du mois
   Batch G (liquidité) : WALCL, TGA, RRP
   Batch H (calendrier) : FOMC, BCE, BLS, BEA dates du mois N+2
4. Vérifier la matrice : toutes les données sont-elles disponibles ou marquées PENDING ?
5. Produire section par section dans l'ordre : 1 → 2 → 3 (après tout le reste) → 4 → 5... → 17
6. Passer la checklist AMF (§4)
7. Passer la checklist qualité (§5)
8. Sortir le HTML complet
```

---

## 4. Checklist AMF (à passer avant livraison)

Cocher chaque point. Si un point échoue, corriger avant de livrer.

**Prohibitions absolues (6 règles AMF Eco3min) :**
- [ ] Aucun pourcentage d'allocation de portefeuille dans le texte
- [ ] Aucun "devrait" / "should" adressé à un type d'investisseur
- [ ] Aucun "acheter X quand Y" / "buy X when Y"
- [ ] Aucune FAQ prescriptive (toute FAQ est descriptive : "historiquement, on observe que...")
- [ ] Les comparaisons géographiques sont des observations statistiques, pas des recommandations
- [ ] Tout timing/sélection ancré sur un fait empirique vérifiable, jamais sur un jugement

**Contrôle de chaque chiffre publié :**
- [ ] Chaque valeur numérique dans les tableaux a une source identifiée (FRED code, institution, date)
- [ ] Aucune valeur approximée sans le tilde "~" et une note ("données indicatives")
- [ ] Les révisions de données antérieures sont signalées (ex. "NFP février révisé à −133k")
- [ ] Les estimations préliminaires sont qualifiées ("advance estimate", "flash estimate")

**Contrôle narratif :**
- [ ] La synthèse (bloc navy) contient ≥ 3 chiffres vérifiés par web_search dans cette session
- [ ] Le Framework contient ≥ 1 chiffre vérifié par paragraphe
- [ ] Les "Key items" décrivent uniquement des événements futurs datés, pas des prévisions de marché
- [ ] Aucune association régime → classe d'actifs sans ancrage empirique explicite (Atlas uniquement)

**Disclaimer :**
- [ ] Présent et non modifié

---

## 5. Checklist qualité éditoriale

- [ ] Toutes les sections du mois N sont présentes dans le mois N+1 (aucune perte)
- [ ] Le shortcode `[eco3min_regime]` est présent avec son commentaire mis à jour
- [ ] Le commentaire du shortcode reflète le statut du flag divergence du mois
- [ ] Les dates dans les titres de sections sont cohérentes avec le mois traité
- [ ] Les liens internes eco3min.fr fonctionnent (web_fetch de vérification)
- [ ] La note sur les flèches du tableau actions est conservée
- [ ] Les labels de section (baro-section-title) utilisent le bon mois
- [ ] "Factual highlights — [Mois écoulé]" correspond aux données reportées
- [ ] "Key items — [Mois N+1]–[Mois N+2]" correspond aux événements futurs au moment de la publication
- [ ] Aucune donnée du mois précédent non mise à jour (scan de toutes les dates dans le HTML)

---

## 6. Règles de typographie et format à maintenir

- Valeurs négatives : `−` (tiret demi-cadratin U+2212), pas `-` (trait d'union)
- Milliers avec virgule EN : `7,230.12` / espace fine FR : `7 230,12`
- Pourcentages : `3.3%` sans espace avant le signe EN / `3,3 %` avec espace fine FR
- Fourchettes Fed funds : `3.50–3.75%` avec tiret demi-cadratin
- Dates tableau : `MM/DD/YYYY` format EN / `JJ/MM/AAAA` format FR
- Sources in-text : "Source: [Institution], [document], [date]." — point final obligatoire
- Italique éditorial : réservé aux emprunts terminologiques ou citations courtes, jamais aux opinions

---

## 7. Gestion des données non disponibles

| Situation | Action |
|---|---|
| Donnée non encore publiée | Conserver la valeur du mois précédent avec "(révision attendue le [date])" |
| Événement non encore survenu | Mettre dans "Key items to watch", jamais dans les tableaux |
| Source inaccessible temporairement | Utiliser la valeur FRED la plus récente disponible, noter la date |
| Valeur FRED marquée "." (manquante) | Ne pas écrire la valeur — noter "[données non disponibles, prochaine publication : date]" |
| Révision majeure d'une donnée antérieure | Mettre à jour la valeur révisée ET signaler la révision dans les Faits marquants |

---

## 8. Note pour la version française du baromètre

Si la version FR du baromètre existe (`/barometre-macroeconomique-feuille-de-route/`), appliquer
le même protocole en traduisant les sections éditoriales. Les données chiffrées et sources sont
identiques. Points de vigilance :
- "advance estimate" → "estimation préliminaire" ou "estimation avancée"
- "year-over-year" → "en glissement annuel" ou "sur un an"
- Flèches du tableau actions : inchangées (symboles universels)
- Label "RÉGIME MACRO" dans le shortcode card : auto-géré par Polylang

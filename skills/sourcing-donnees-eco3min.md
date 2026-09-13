---
name: sourcing-donnees-eco3min
description: Doctrine de sourcing des données PUBLIÉES sur eco3min.fr (charts, datasets, études) — provenance, licence, légalité. Activer pour toute décision de source à publier, ou doute légal sur une donnée. Cadre FR/UE + nuances US ; PAS un avis juridique. Règle cardinale : footer = source RÉELLE des chiffres, jamais relabelliser vers une source plus propre. Interdit ferme : Yahoo/yfinance et agrégateurs scrapés comme source d'un CSV publié — le problème est leurs CGU, pas les chiffres. Hiérarchie des sources propres : (1) primaires publiques (FRED, ECB, BIS, IMF, BLS…) ; (2) émetteur du fonds (iShares/BlackRock) ; (3) API licenciée (Tiingo…) ; (4) indices sous licence (MSCI/Russell/S&P) : tracer le PRIX d'un ETF, pas l'indice. Couvre les TROIS niveaux de licence FRED (public domain / citation required / PRE-APPROVAL required), faits non protégés (Feist) vs droit sui generis UE, marques, traçabilité, cross-check. Combiner avec pipeline-eco3min, visuels-eco3min.
---

# Sourcing des données Eco3min — provenance, licence, légalité

## Statut & portée

Doctrine de sourcing pour **toute donnée publiée** sur eco3min.fr : charts, heros, pages dataset, études. Couche transverse, **en amont de `pipeline-eco3min`** (au moment du fetch) et **de `visuels-eco3min` / `production-dataset` / `production-hero-*`** (au moment de la publication : footer, label).

**Pas un avis juridique** — ni Paul ni Claude ne sont juristes. Cadre de raisonnement : droit **FR/UE** (site `.fr`, hébergement OVH, éditeur français) avec nuances US. C'est un repérage opérationnel pour rester du bon côté et garder une chaîne data propre, pas une garantie légale.

## Règle cardinale

**Le footer / la source affichée = la source RÉELLE des chiffres tracés.** Jamais relabelliser une donnée vers une source plus « propre » que celle réellement utilisée — c'est la faute « méthode Damodaran » transposée à la source. **La source et le label bougent ensemble** : on ne change pas l'attribution sans re-sourcer réellement la donnée.

## Interdiction ferme

- **JAMAIS Yahoo Finance (yfinance, scraping)** comme source d'un CSV **publié** sur le site commercial. Idem agrégateurs scrapés : investing.com, MarketBeat, et Stooq pour un usage commercial.
- Raison : ce ne sont **pas les chiffres** le problème (un cours est un fait, non protégeable). Ce sont **leurs CGU** qui interdisent l'extraction automatisée et/ou l'usage commercial. C'est du **contractuel** → ça te suit partout, France comme US ; déménager ne le règle pas, seul changer de source le règle.
- Yahoo & co restent OK pour **exploration / brouillon privé non publié**. Le basculement interdit, c'est la **publication commerciale**.

## Hiérarchie des sources propres (par ordre de préférence)

1. **Primaire / institutionnelle publique** — FRED (séries gouvernementales US non copyrightées), ECB SDMX, BIS, IMF, World Bank, BLS, Eurostat, Banque de France, US Treasury. Gratuites, citables, conçues pour ça. **Défaut pour les séries macro.**
2. **Émetteur / producteur primaire** — iShares/BlackRock, Vanguard, SPDR pour la donnée de **leur** fonds, via le **téléchargement officiel** (NAV + distributions, ou performance total return publiée). Source primaire + canal prévu = posture la plus solide en gratuit.
3. **API de données sous licence** — Tiingo, Twelve Data, EOD Historical Data, Alpha Vantage. Vérifier que **le plan choisi couvre l'usage** (souvent commercial avec attribution sur les paliers payants). Route « propre de bout en bout » pour un site qui monétise ; route recommandée si eco3min monte en audience.
4. **Indices sous licence (MSCI, FTSE Russell, S&P)** — la **donnée d'indice** est sous licence, à **ne pas redistribuer** sans contrat. Contournement légitime : tracer le **prix d'un ETF** qui réplique l'indice (fait de marché) et **nommer l'ETF, pas l'indice**. (Cas vécu : pas d'ETF MSCI World Growth gratuit → proxy Russell 1000 IWF/IWD nommé comme tel.)

## Cas FRED — les TROIS niveaux, et ce que chacun permet

⚠️ **Corrigé le 10/09/2026.** Ce skill décrivait deux états — « marquée
Copyright » = usage personnel. C'est faux : FRED en distingue **trois**, et
l'intermédiaire autorise en réalité ce que cette formulation interdisait. Une
version antérieure a fait reconstruire des colonnes sans nécessité, et surtout
n'a pas empêché de publier de la donnée du niveau le plus dur.

Le statut se lit sur `fred.stlouisfed.org/series/{ID}`, tag `series-tag`, et se
grep en une ligne :

```bash
curl -s "https://fred.stlouisfed.org/series/$ID" | grep -o -E 'series-tag" content="(copyrighted[^"]*|public domain[^"]*)"'
```

| Statut FRED | Usage commercial | CSV redistribué en CC BY 4.0 | Exemples |
|---|---|---|---|
| **Public domain: citation requested** | oui, avec attribution | **oui** | `GS10`, `DGS10`, `USSTHPI`, `HQMCB10YR`, `CPIAUCSL` |
| **Copyrighted: citation required** | **oui**, avec attribution à la source ET à FRED (termes FRED, section IV : « internal commercial uses », affichage « in textbooks, newsletters, or reports to clients ») | **NON** | Moody's `BAA`, Chicago Fed `NFCI`/`CFNAI`, `T10Y2Y`, `T5YIE`, `T10YIE`, `RRPONTSYD`, `USREC`, `M2V`, `VIXCLS` |
| **Copyrighted: pre-approval required** | **non**, rien sans accord écrit du détenteur | non | toutes les séries ICE BofA (`BAML*`), `SP500`, `NASDAQCOM`, `CSUSHPINSA` |

**Pourquoi « citation required » interdit quand même le CC BY 4.0.** FRED
autorise Eco3min à publier la donnée. Il ne l'autorise pas à **sous-licencier** :
CC BY 4.0 dirait au téléchargeur qu'il peut redistribuer et remixer librement,
ce qu'Eco3min ne détient pas. C'est exactement le raisonnement déjà écrit pour
le FMI dans le snippet 36 d'`eco3min-wp` : « CC BY dirait au téléchargeur
l'inverse de ce que le FMI impose ». La sortie n'est donc **pas** de retirer la
page, c'est de **déclarer la vraie licence** — `eco3_source_rights()` porte le
mécanisme, avec `usageInfo`, `copyrightHolder`, `citation` et une notice visible.

**Le niveau « pre-approval », lui, ne se contourne pas** par une déclaration :
il n'y a rien à déclarer, la republication est interdite. Deux issues seulement :
retirer le dataset, ou re-sourcer (pour un indice actions, le **prix d'un ETF**,
règle 4 de la hiérarchie ci-dessus).

**Le contrôle de licence est un GATE, pas une ligne de checklist finale.** Il se
fait **avant** de mesurer la profondeur d'une série et avant d'écrire quoi que ce
soit : « pre-approval required » tue une étude que l'historique le plus long ne
sauverait pas. Vécu sur l'étude R5, série GENERIQUE, 10/09/2026.

**Un composite hérite du niveau le plus dur de ses intrants.** Publier
`sp500/gold` en CC BY 4.0 redistribue `SP500` : la division ne lave rien, et une
colonne `sp500` brute dans le fichier ne se défend pas du tout.

**Route d'accès.** Utiliser le **téléchargement ou l'API officielle**. Les
termes interdisent « data mining, mirroring, robots, scraping, or similar
data-gathering or extraction methods **except as expressly allowed by the terms
of use applicable to the FRED API** » — or `fredgraph.csv?id=…` en curl, en
boucle et en CI, **n'est pas l'API**. C'est le point d'exposition réel du
pipeline, plus que la clause suivante.

**Clause IA, à ne pas sur-lire.** Depuis **début mai 2024** (absente au 01/05,
présente au 08/05, vérifié au Wayback — donc rien de nouveau), les termes
interdisent d'utiliser FRED « in connection with the **development or training**
of any software program or system or machine learning, including... large
language models ». Les deux mots qui portent sont *development* et *training* :
lire une série pour produire une analyse n'est ni l'un ni l'autre, et la même
page autorise expressément « Create an app using a subset of FRED data through
the free API ».

## Principes légaux (rationale — pas un avis)

- **Les faits ne sont pas protégeables par le copyright** (US : arrêt *Feist*, pas de « sweat of the brow »). En UE/France : idem pour les faits **isolés**, MAIS il existe un **droit sui generis des bases de données** (Dir. 96/9/CE ; CPI art. L341-1 s.) qui protège l'extraction d'une **part substantielle** d'une base. Quelques dizaines de points dans un chart dérivé ≠ part substantielle → **risque faible**.
- **Le vrai risque = les CGU / le contrat** de la source (Yahoo), pas le copyright. Contractuel → indépendant de l'endroit où tu te trouves physiquement.
- **Marques** (noms d'indices / ETF) : usage **nominatif / référentiel** admis des deux côtés (US nominative fair use ; UE usage référentiel « pratiques honnêtes »). Citer « Russell 1000 Growth via IWF » = OK. **Ne pas** suggérer un parrainage ou un endossement par le fournisseur.
- **Échelle de risque** : pour un chart éditorial, on est en **civil** (au pire mise en demeure / retrait), **pas pénal**. Le pénal vise la contrefaçon commerciale massive — hors sujet ici.
- **US vs France** : les US sont **plus permissifs** sur la donnée (pas de droit sui generis + fair use large). S'établir aux US allégerait cet axe, ne l'alourdirait pas.

## Traçabilité de provenance

Pour chaque dataset / série publié, **consigner** : source exacte + code de série + URL + licence/termes + méthode de fetch + date. Permet de **reconstruire et de prouver la chaîne**, et d'auditer en cas de doute. S'intègre naturellement au registry de `pipeline-eco3min` (champ provenance par dataset).

## Cross-check obligatoire

Vérifier les niveaux/chiffres contre une **2e source** ou contre une performance connue avant publication. Cas observé (mai 2026) : écart d'un **facteur ~4 sur le niveau absolu** d'un ETF entre deux agrégateurs — la source primaire tranche. Ne jamais publier un chiffre point-précis non recoupé. (Lien avec `production-q-and-a`, `production-research-study`.)

## Checklist pré-publication d'un visuel / dataset

- [ ] Source = primaire / institutionnelle / licenciée — **pas** Yahoo ni agrégateur scrapé
- [ ] Footer nomme la **source réelle** (label = source)
- [ ] Si FRED : statut de licence lu **avant** tout le reste. *Public domain* → CSV CC BY 4.0 ; *citation required* → publiable avec attribution mais **jamais** en CC BY 4.0, déclarer la vraie licence ; *pre-approval required* → ne pas publier, re-sourcer ou retirer
- [ ] Si composite : **chaque** intrant passé au même test, la série hérite du plus dur
- [ ] Si indice sous licence : on trace le **prix ETF**, pas la donnée d'indice ; l'ETF est nommé
- [ ] Attribution présente ; **aucune** implication d'endossement par le fournisseur
- [ ] Chiffres **recoupés** vs 2e source / performance connue
- [ ] **Provenance consignée** (source, code, URL, licence, méthode, date)

## Annexe — sources macro mondiales gratuites (équivalents FRED par zone)

**Principe de lecture** : la **macro/officiel** (taux, inflation, PIB, crédit, change officiel, immobilier, balance des paiements) est ouverte et gratuite quasi partout. Les **cotations de marché** (cours d'actions, indices boursiers en niveau) sont sous licence d'affichage de bourse → **payantes partout, toutes zones** → parade = prix d'ETF (émetteur) ou rendement académique (Fama-French, versions régionales gratuites). Cette annexe ne couvre QUE la macro/officiel.

### Mondial / multi-pays (à privilégier — un seul point d'entrée, plusieurs pays)
| Source | Couvre | Licence | Accès |
|---|---|---|---|
| **World Bank Open Data** | tous pays, macro/dev | **CC-BY** (commercial OK + attribution) | API + CSV |
| **IMF** (IFS, BoP, WEO) | tous pays, macro/dette/BoP | usage large, attribution | API SDMX + CSV |
| **BIS** | banques centrales, crédit, taux, prix immo, FX transfrontalier | attribution | CSV / API |
| **OECD.Stat** | pays OECD + partenaires | attribution (vérifier série) | API SDMX + CSV |
| **DBnomics** (CEPREMAP, FR) | **agrège** FRED, ECB, Eurostat, INSEE, IMF, BIS… | hérite de la source | **API unique** + Python |
| **UN Data / Comtrade** | démographie, commerce | attribution | API + CSV |

> DBnomics = souvent le point d'entrée le plus efficace : une API pour des dizaines de sources, licence héritée de la source d'origine (à tracer quand même).

### Europe
| Zone | Institution | Note |
|---|---|---|
| Zone euro | **ECB Data Portal (SDMX)** | équivalent FRED zone euro — déjà dans le pipeline |
| UE | **Eurostat** | toute l'UE, harmonisé |
| France | **Banque de France Webstat**, **INSEE** | libre |
| Allemagne | **Bundesbank** | libre |
| Italie / Espagne | **Banca d'Italia** / **Banco de España** | libre |
| UK | **ONS**, **Bank of England** | libre |

### Inde
| Source | Note |
|---|---|
| **RBI — DBIE** (Database on Indian Economy) | macro/monétaire officiel, gratuit |
| **MoSPI** | statistiques nationales officielles |
| ⚠️ CEIC / Trading Economics | **payant/licencié** — PAS comme source publiée |

### Chine (prudence — confiance moyenne)
| Source | Note |
|---|---|
| **NBS** (National Bureau of Statistics), **PBoC** | officiel gratuit, mais accès programmatique inégal, anglais partiel |
| **Voie recommandée : World Bank / IMF / BIS** | retraitent les séries chinoises avec méthodo homogène et comparable |
| ⚠️ Sourcer explicitement « données officielles chinoises » ; ne pas sur-interpréter (fiabilité/comparabilité débattues) |

### Autres zones
| Zone | Institution |
|---|---|
| US emploi/prix | **BLS** |
| Japon | **Bank of Japan**, e-Stat |
| Brésil | **Banco Central do Brasil (SGS)** |
| Canada | **Statistics Canada** |
| Afrique / Amérique latine / Asie (général) | **World Bank + DBnomics** (meilleure couverture homogène) |

### Marché (actions/indices) — rappel parade
Pas de source gratuite ET commerciale pour les cotations, **aucune zone**. Utiliser : **prix d'ETF** (donnée d'émetteur, attribuée) ou **Kenneth French Data Library** — versions régionales gratuites : **Europe, Japan, Asia-Pacific ex-Japan, North America, Emerging Markets, Developed** (portefeuilles value/growth/size, total return, © Fama & French).

**Réflexe transversal** : licences variables (World Bank CC-BY très permissif ; banques centrales = attribution ; quelques séries hébergées portent des restrictions de tiers). Toujours vérifier les conditions de LA série avant publication ; footer = source réelle.

## Annexe B — points d'entrée opérationnels (testés)

L'annexe A dit quelle institution est propre. Celle-ci dit **par où l'atteindre,
et où ça casse**. À corriger dès qu'un endpoint change — un
endpoint mort ici coûte une session.

### Comment atteindre une source — l'ordre des routes

Il y a trois routes vers une source, de la plus rapide à la plus lente. **Les
essayer dans cet ordre**, et ne descendre d'un cran qu'après un échec constaté.

1. **`curl` depuis le Bash** — la plus rapide, et elle rend le fichier brut.
   Testé le 04/09/2026 : FRED (`fredgraph.csv`), BLS, BEA, Chicago Fed, Richmond
   Fed, ECB SDMX et LBMA répondent tous **HTTP 200** depuis l'environnement
   Claude Code.
2. **`WebFetch`** — quand on veut une lecture de page plutôt qu'un fichier.
   Testé le même jour sur `fred.stlouisfed.org/series/{ID}` : rend la dernière
   observation et sa date.
3. **Le Browser pane** (`navigate`, `get_page_text`, `javascript_tool`) — le
   repli quand les deux premières échouent, et **la seule route pour une page
   derrière authentification** (un écran wp-admin, par exemple).

⚠️ **Ne pas inverser cet ordre.** Le Browser pane coûte plusieurs tours par
lecture ; `curl` en coûte un.

#### Les échecs sont datés et locaux, jamais une propriété de la source

Trois observations opposées coexistent dans l'historique de ce site :

| Constat | Origine | Statut au 04/09/2026 |
|---|---|---|
| `fredgraph.csv` renvoie **503** | projet Héro V3 | non reproduit |
| `curl fredgraph.csv` « peu fiable, egress resets / 403 » | projet Research Study | non reproduit |
| `WebFetch` **403** sur FRED, BLS, BEA, Chicago Fed, Richmond Fed ; Bash sans réseau | projet Baromètre, 02/09/2026 | **non reproduit — 7 sources sur 7 en 200** |

Ces trois notes étaient vraies dans leur environnement et à leur date. Aucune
n'est une propriété de l'institution.

**La règle** : un 403, un 503 ou un timeout se **teste** avant d'être conclu, et
se **date** quand il est consigné. Ne jamais écrire « cette source est bloquée » —
écrire « bloquée depuis tel environnement, le tel jour », et passer à la route
suivante. Une note d'échec non datée fait perdre plus de temps qu'elle n'en fait
gagner : elle détourne durablement de la route la plus rapide.

#### Gestes utiles du Browser pane, quand on y est

- ⚠️ **`get_page_text` repart toujours du haut de la page.** Pour lire un passage
  plus bas, passer par `javascript_tool` et découper `document.body.innerText`.
- ⚠️ **`browser_batch` s'interrompt après environ trois actions par appel.**
  Batcher court.
- **FRED, `fetch` same-origin** : depuis une page FRED déjà ouverte,
  `fetch('fredgraph.csv?id={ID}&cosd={AAAA-MM-JJ}&coed={AAAA-MM-JJ}')` rend le
  CSV daté. Utile quand on est déjà dans le navigateur, et **une seule série à la
  fois** — le multi-séries renvoie un ZIP.

#### Cours de clôture — sources datées connues

| Marché | Source |
|---|---|
| S&P 500, Dow Jones | FRED (`SP500`, `DJIA`) |
| Nasdaq Composite | `api.nasdaq.com/api/quote/COMP/historical` |
| Places Euronext | `live.euronext.com` — affiche un « Previous Close » daté |
| Or | `prices.lbma.org.uk/json/gold_pm.json` — fixing PM, historique complet |
| **DAX, Euro Stoxx 50** | **aucune source primaire datée connue** — Deutsche Börse et STOXX sont restés inaccessibles |

#### ⚠️ Le piège de fin de mois

**Vérifier le calendrier de chaque place avant de dater une clôture.** Les
bourses ne ferment pas les mêmes jours.

Cas vécu : le **31 août 2026** était le Summer Bank Holiday britannique. Ni
clôture FTSE 100, ni fixing LBMA ce jour-là — alors que Paris, Francfort et
New York cotaient. Une valeur « au 31 » aurait été fausse sur deux lignes d'un
même tableau, sans qu'aucun contrôle ne le signale.

#### FRED — replis si l'accès direct échoue

Dans l'ordre : la **route en deux temps** (charger la page de la série, puis
`fred.stlouisfed.org/data/{SERIES_ID}.txt`) · les **miroirs Eco3min**
(`https://eco3min.fr/dataset/{id}.csv` — ce que servent réellement les pages du
site, donc ce qu'il faut auditer) · l'**émetteur direct** (US Treasury pour les
CMT, BLS pour l'IPC, NY Fed pour l'ACM — souvent plus frais que FRED) · l'API
FRED officielle avec clé.

Ne jamais conclure « la donnée n'existe pas » sur un seul échec d'accès.

### Endpoints par domaine

| Domaine | Point d'entrée |
|---|---|
| BCE — taux, MIR, SDMX | `data-api.ecb.europa.eu/service/data/{FLOW}/{KEY}?format=csvdata` |
| Eurostat | `ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/{dataset}?format=JSON` |
| US Treasury — CMT | `home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/{ANNEE}/all` |
| BLS — IPC | `api.bls.gov/publicAPI/v1/timeseries/data/` — sans clé, mais **fenêtre de 10 ans maximum** par appel |
| BRI — crédit | `stats.bis.org/api/v1/data/WS_TC/{key}/all?format=csv` |
| LBMA — or / argent | `prices.lbma.org.uk/json/gold_pm.json` et `silver.json` |
| NY Fed — prime de terme ACM | téléchargement Excel direct depuis le site NY Fed |
| FMI — PortWatch | `portwatch.imf.org/api/download/v1/items/{id}/csv?layers=0` |
| Banque mondiale — matières premières | Pink Sheet XLSX sur `thedocs.worldbank.org` — **l'URL change chaque année**, la localiser par recherche web plutôt que la mettre en dur |
| Banque mondiale — CPI | API `FP.CPI.TOTL` (1960→T-1, base 2010=100) |
| FAO — FFPI | classeur en téléchargement direct, CC BY 4.0 |
| EIA (énergie US) | fichiers bulk |
| USDA NASS (agriculture US) | API Quick Stats |
| Fed d'Atlanta — microdonnées DCPC | archive ZIP en téléchargement direct |

### En-têtes et formats exigés

Trois sources refusent les requêtes sans `User-Agent` explicite. Le
symptôme n'est pas une erreur claire : c'est un refus ou une réponse vide,
qu'on met du temps à attribuer à l'en-tête.

| Source | Contrainte |
|---|---|
| **BLS** (fichiers plats) | `User-Agent` explicite **obligatoire**, avec un contact réel : `Eco3min research contact@eco3min.fr`. Sans lui, refus. |
| **World Bank WDI** (API) | `User-Agent` explicite obligatoire lui aussi. |
| **OECD** (SDMX) | via curl avec `format=csvfilewithlabels` — sinon les libellés de dimension manquent et la série est inexploitable. |
| **BLS v1** (API) | **ignore les filtres d'année** (parser par année soi-même), sauter `M13`, sauter les valeurs `'-'`. Une moyenne d'année partielle se divulgue comme telle. |
| **Robert Shiller** (`ie_data.xls`) | se parse avec `xlrd==1.2.0`. Les versions ultérieures ont retiré le support du `.xls` : l'installation par défaut échoue. |
| **Jacks 1850–2025** (XLSX) | **bloqué par captcha** à toute récupération automatisée. Un clic humain passe : demander le fichier. |
| **World Bank Pink Sheet** | feuilles d'indices annuels : **les données commencent ligne 10**. Nominal et réel MUV, colonnes Fertilizers et Precious Metals incluses, plus le déflateur MUV. |

### Règle d'arrêt

Si une source nécessaire est bloquée : **s'arrêter et demander les
fichiers à Paul.** Ne jamais substituer la mémoire du modèle à une
récupération ratée.

### Réflexe

Tout endpoint mis en dur périme. Avant d'en déclarer un mort,
vérifier que ce n'est pas simplement l'année ou le nom de fichier qui a
tourné — c'est le cas le plus fréquent, notamment sur le Pink Sheet.

## Fond (décalé) vs live (temps réel) — piège de fraîcheur

Les sources gratuites propres sont **décalées**, par nature :
- **Fama-French** : portefeuilles **mensuels** (parfois daily), publiés **~1 mois après** la fin du mois (ex. en mai, dernier point = mars/avril).
- **Macro officielle** (FRED, ECB, World Bank…) : fréquence et délai variables (mensuel/trimestriel, parfois plusieurs mois de retard).

Conséquence :
- **Étude / hero structurel / dataset historique** → parfait, le décalage est sans importance (on lit des régimes sur des années).
- **Page « live » / chart du jour / suivi quotidien** → **inadapté**. Il faut alors une donnée de marché temps réel, qui est **licenciée et payante** (mur cotations). Pas de gratuit propre pour le live.

Règle : ne jamais promettre du « temps réel » sur une page alimentée par une source de fond décalée. Si une page implique de la fraîcheur (régime en direct), soit elle affiche honnêtement la date du dernier point disponible, soit elle exige une source licenciée.

## Séries dérivées maison (composites « à la Fama-French »)

Eco3min construit ses propres séries (Net Liquidity Index, Excess CAPE Yield, séries réelles déflatées…) — c'est légitime et stratégique (citabilité, backlink : un indicateur nommé se cite, un cours non).

**Règle cardinale du dérivé : une série dérivée est aussi publiable que sa source la MOINS libre.** Construire ne « lave » pas un intrant sale.
- Intrants 100 % propres (FRED, ECB, World Bank…) → série propre, publiable/diffusable sans réserve. **Cas idéal.**
- Un seul intrant sous licence restrictive (cours Yahoo scrapé…) → la série **hérite de la restriction**, interdite à la publication commerciale, même reformulée.
- Faits libres (cours = faits) via un **canal propre** (pas Yahoo) + transformation substantielle → série défendable comme œuvre propre. Le problème n'est jamais les chiffres-faits, c'est le **canal d'acquisition** (contrat de la source).

**Plus la transformation est lourde, plus la série est défendable comme création originale** : un indice repondéré (Fama-French) est plus solide qu'un simple `A − B`. Vérifier que **chaque intrant** passe la doctrine de sourcing AVANT de publier le composite. (Lien `pipeline-eco3min` : le champ provenance doit lister les intrants de chaque composite, pas seulement la série finale.)

## Articulation avec les autres skills

- **`pipeline-eco3min`** — applique cette doctrine **au fetch** (choix de la source dans les builders, champ provenance du registry). Si une source est interdite ici, elle ne rentre pas dans le pipeline.
- **`visuels-eco3min` / `production-dataset` / `production-hero-pilier` / `production-hero-majeur` / `production-hero-article-eco3min`** — appliquent **à la publication** : footer, label, sourcing intégré au visuel.
- **`editeur-eco3min`** — sourcing intégré au texte (mêmes principes pour les chiffres cités en prose).

## Note d'usage

Créé mai 2026 après l'épisode Yahoo → iShares sur le hero majeur Growth/Value (Russell 1000 IWF/IWD). **Pas un avis juridique.** À actualiser quand : une source change ses CGU ; tu souscris une API licenciée (consigner le plan + les droits qu'il ouvre) ; un nouveau type de source apparaît dans le pipeline ; un endpoint de l'annexe B change ou meurt (le Pink Sheet de la Banque mondiale change d'URL chaque année) ; une source se met à exiger un `User-Agent` ou change de format d'export — le symptôme est un refus silencieux ou une réponse vide, pas une erreur explicite.

# sourcing-donnees-eco3min — référence : Annexe B, points d'entrée opérationnels (routes, échecs datés, cours de clôture, endpoints, en-têtes, règle d'arrêt)

Extrait VERBATIM de SKILL.md (découpage du 17/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

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

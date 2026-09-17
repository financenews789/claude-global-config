---
name: sourcing-donnees-eco3min
description: "Doctrine de sourcing de toute donnée PUBLIÉE sur eco3min.fr (charts, heros, pages dataset, études, chiffres en prose) : provenance, licence, légalité, routes d'accès. Activer pour toute décision de source, tout doute légal sur une donnée, et dès qu'une demande contient « quelle source », « c'est publiable ? », « on peut redistribuer ? », « licence », « CC BY », « citation required », « pre-approval », « copyrighted », « domaine public », « CGU », « scraping », « yfinance », « Yahoo », « FRED », « series-tag », « DBnomics », « Pink Sheet », « endpoint », « 403 », « User-Agent », « provenance », « cross-check », « composite », « intrant », « prix d'ETF », « proxy », « indice sous licence », « MSCI », « S&P », « LBMA », « CoinGecko », « footer », « label de source », « source réelle ». Cadre FR/UE avec nuances US ; PAS un avis juridique. SKILL.md = colonne vertébrale (règle cardinale, interdiction ferme, hiérarchie des sources, section « Cas FRED » complète avec ses trois niveaux, principes légaux, traçabilité, cross-check, checklist verbatim, fond vs live, séries dérivées, condensés des annexes A et B, ajout du 17/09/2026 sur les trois usages d'une donnée) ; références dans references/ (à lire quand la section le dit) : 01 annexe A, sources macro gratuites par zone (mondial, Europe, Inde, Chine, autres, marché) ; 02 annexe B, points d'entrée opérationnels (ordre des routes curl puis WebFetch puis Browser pane, échecs datés, cours de clôture, piège de fin de mois, replis FRED, endpoints par domaine, User-Agent et formats, règle d'arrêt) ; 03 licences des sources réellement en pipeline hors FRED (CoinGecko, LBMA, Pink Sheet, IMF, OECD, BoE, ECB, Eurostat, BIS, ENTSO-E, AGSI+, Shiller, Fama-French, Nasdaq, Euronext) avec l'usage autorisé et la date de vérification ; scripts/fred_license.py = lecture du tag de licence FRED par série, niveau hérité par un composite, refus si ID inconnu (testé sur les 19 séries de la table). Doctrines : footer = source RÉELLE des chiffres, la source et le label bougent ensemble, jamais relabelliser vers une source plus propre (épisode Yahoo → iShares, mai 2026 ; « LBMA » sur une donnée Pink Sheet, 17/09/2026) ; Yahoo, yfinance et agrégateurs scrapés interdits comme source d'un CSV publié, le problème est leurs CGU pas les chiffres, contractuel donc portable partout ; hiérarchie (1) primaires publiques (2) émetteur du fonds (3) API licenciée (4) indice sous licence → tracer le PRIX d'un ETF nommé, pas l'indice ; FRED distingue TROIS niveaux (corrigé le 10/09/2026) : public domain → CSV CC BY 4.0, citation required → publiable avec attribution mais JAMAIS sous-licencié en CC BY, déclarer la vraie licence par eco3_source_rights(), pre-approval required (BAML*, SP500, NASDAQCOM, DJIA, CSUSHPINSA) → retirer ou re-sourcer, rien ne se déclare ; le contrôle de licence est un GATE avant de mesurer la profondeur d'une série (étude R5, 10/09/2026), lu par script ; un composite hérite du niveau le plus dur de ses intrants, la division ne lave rien ; fredgraph.csv en boucle n'est pas l'API ; un 403 se teste et se date, jamais « cette source est bloquée » ; source bloquée → s'arrêter et demander les fichiers, jamais la mémoire du modèle ; cross-check contre une 2e source avant tout chiffre point-précis ; ne jamais promettre du temps réel sur une source de fond décalée ; trois usages distincts (cotation ponctuelle en prose, série tracée, CSV redistribué), les CGU peuvent autoriser le premier et interdire le dernier (CoinGecko : redistribution interdite, route propre FRED CBBTCUSD / CBETHUSD ; LBMA : historique sous licence IBA, route propre Pink Sheet). Hors périmètre : le code des fetchers et le registry → pipeline-eco3min ; le footer et le sourcing intégré au visuel → visuels-eco3min et brand-kit-eco3min ; la page dataset elle-même → production-dataset ; les chiffres cités en prose → editeur-eco3min. Combiner avec pipeline-eco3min, visuels-eco3min, production-dataset, production-research-study, production-chart-of-the-week, production-hero-pilier, production-hero-majeur, production-hero-article-eco3min, editeur-eco3min, revue-datasets-perimes."
---

# Sourcing des données Eco3min — provenance, licence, légalité

## Statut & portée

Doctrine de sourcing pour **toute donnée publiée** sur eco3min.fr : charts, heros, pages dataset, études. Couche transverse, **en amont de `pipeline-eco3min`** (au moment du fetch) et **de `visuels-eco3min` / `production-dataset` / `production-hero-*`** (au moment de la publication : footer, label).

**Pas un avis juridique** — ni Paul ni Claude ne sont juristes. Cadre de raisonnement : droit **FR/UE** (site `.fr`, hébergement OVH, éditeur français) avec nuances US. C'est un repérage opérationnel pour rester du bon côté et garder une chaîne data propre, pas une garantie légale.

## COMMENT LIRE CE SKILL (découpage du 17/09/2026)

Ce fichier est la colonne vertébrale : la règle cardinale, l'interdiction ferme, la hiérarchie des sources, la section « Cas FRED » complète (c'est le gate), les principes légaux, la traçabilité, le cross-check, la checklist, le piège de fraîcheur et les séries dérivées. Les deux annexes (catalogue des institutions par zone, points d'entrée opérationnels) ont été déplacées VERBATIM dans `references/` et font foi au même titre que ce fichier ; elles ne servent qu'au moment du fetch. Chaque section ci-dessous nomme le fichier à lire ; le lire est obligatoire au moment indiqué, pas facultatif. `scripts/fred_license.py` remplace la lecture manuelle du tag FRED.

| Fichier | Contenu | À lire |
|---|---|---|
| `references/01-sources-macro-par-zone.md` | Annexe A : principe de lecture (macro ouverte, cotations sous licence), sources mondiales (World Bank, IMF, BIS, OECD, DBnomics, UN), Europe, Inde, Chine, autres zones, parade marché (prix d'ETF, Kenneth French) | avant de choisir une institution pour une série hors FRED / ECB, et pour toute zone hors US et zone euro |
| `references/02-points-entree-endpoints.md` | Annexe B : ordre des trois routes (curl, WebFetch, Browser pane), échecs datés et locaux, gestes du Browser pane, cours de clôture datés, piège de fin de mois, replis FRED, endpoints par domaine, User-Agent et formats exigés, règle d'arrêt, réflexe | avant tout fetch, et dès qu'un accès échoue (403, 503, timeout, réponse vide) |
| `references/03-licences-sources-pipeline.md` | AJOUT 17/09/2026 : les trois usages d'une donnée (cotation ponctuelle, série tracée, CSV redistribué), table des sources réellement en pipeline hors FRED avec conditions, attribution, usage autorisé et date de vérification, ce que ça change (CoinGecko, LBMA, clés source_rights) | avant de publier un CSV ou un visuel d'une source hors FRED, et avant d'ajouter une famille de source au pipeline |
| `scripts/fred_license.py` | lecture du tag `series-tag` par série, trois niveaux, niveau hérité par un composite, refus si ID inconnu ou page illisible (jamais « public domain » par défaut), CLI avec codes retour | au gate de licence, sur chaque série destinée à une colonne publiée et chaque intrant d'un composite ; à chaque revue de datasets |

Utilisation du script :

    sys.path.insert(0, os.path.expanduser('~/.claude/skills/sourcing-donnees-eco3min/scripts'))
    from fred_license import check_series, composite_level, can_ccby, publishable
    python scripts/fred_license.py --composite --ccby DGS10 T10YIE   # code retour 1 : pas CC BY ; 2 : pre-approval

Test : `python scripts/test_fred_license.py` (19 séries de la table « Cas FRED » + tests négatifs, réseau requis).

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

## Trois usages d'une donnée, et les sources hors FRED (ajout du 17/09/2026) — lire `references/03-licences-sources-pipeline.md` avant de publier un CSV ou un visuel d'une source hors FRED

Ce que la section « Cas FRED » fait pour FRED, cette référence le fait pour les autres sources du pipeline. Ajout du 17/09/2026, après lecture des conditions LBMA et CoinGecko et des tags FRED de 25 séries.

Bloquant :
- **Trancher l'usage avant de choisir la source.** (a) cotation ponctuelle citée en prose ou dans un tableau daté (baromètre, bulletin) ; (b) série tracée dans un visuel ; (c) CSV / XLSX redistribué (page dataset, fichier d'étude). Les CGU d'une source autorisent souvent (a) et interdisent (c). Une source « OK » pour le baromètre n'est pas « OK » pour une page dataset.
- **Le tag FRED se lit par script**, `scripts/fred_license.py`, sur chaque série destinée à une colonne publiée et chaque intrant d'un composite. Un ID inconnu, une page illisible ou un tag absent = échec, jamais « public domain » par défaut.
- **CoinGecko** : intégration commerciale autorisée avec « Powered by CoinGecko », **redistribution des données interdite** (API Terms §4.1.6 et §6.2, lus le 17/09/2026). Pas de CSV construit depuis CoinGecko. Route propre pour BTC / ETH : FRED `CBBTCUSD` / `CBETHUSD` (Coinbase, « citation required » lu le 17/09/2026 → publiable avec attribution, jamais CC BY, historique depuis 2014 / 2016).
- **LBMA** : le JSON `prices.lbma.org.uk` sert une clôture datée (usage a). Un historique redistribué exige une licence IBA (« A licence from IBA is required in order to obtain, use or redistribute real-time or historical benchmark data », lu le 17/09/2026). Route propre or / argent : le Pink Sheet de la Banque mondiale (CC BY 4.0, moyenne mensuelle du fixing PM), déjà celle du pipeline. Le label doit le dire ; « LBMA » seul sur une donnée Pink Sheet est un relabellisage (règle cardinale).
- **Toute source publiée en (c) a sa clé** dans `eco3min-data/scripts/source_rights.py` et son miroir `eco3_source_rights()` (snippets 36 et 114) ; sans clé, le défaut CC BY 4.0 du snippet s'applique à tort (22 pages corrigées le 16/09/2026).
- **Une ligne « à vérifier » de la table n'autorise rien** : relire les conditions à la source, dater la lecture, puis publier.
- Le tag FRED d'une série peut changer : relire les tags des séries publiées à chaque revue de datasets, pas seulement à la création de la page.

S'ajoute à la checklist ci-dessous : usage (a / b / c) tranché et écrit ; tags FRED lus par script ; clé `source_rights` présente pour toute source hors défaut ; label = source réelle y compris pour or / argent (Pink Sheet, pas « LBMA »).

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

## Annexe — sources macro mondiales gratuites (équivalents FRED par zone) — lire `references/01-sources-macro-par-zone.md` avant de choisir une institution hors FRED / ECB

Bloquant :
- **Principe de lecture** : la **macro/officiel** (taux, inflation, PIB, crédit, change officiel, immobilier, balance des paiements) est ouverte et gratuite quasi partout. Les **cotations de marché** (cours d'actions, indices boursiers en niveau) sont sous licence d'affichage de bourse → **payantes partout, toutes zones** → parade = prix d'ETF (émetteur) ou rendement académique (Fama-French, versions régionales gratuites). Cette annexe ne couvre QUE la macro/officiel.
- DBnomics = souvent le point d'entrée le plus efficace : une API pour des dizaines de sources, licence héritée de la source d'origine (à tracer quand même).
- Marché (actions / indices) : Pas de source gratuite ET commerciale pour les cotations, **aucune zone**. Utiliser : **prix d'ETF** (donnée d'émetteur, attribuée) ou **Kenneth French Data Library** — versions régionales gratuites : **Europe, Japan, Asia-Pacific ex-Japan, North America, Emerging Markets, Developed** (portefeuilles value/growth/size, total return, © Fama & French).
- **Réflexe transversal** : licences variables (World Bank CC-BY très permissif ; banques centrales = attribution ; quelques séries hébergées portent des restrictions de tiers). Toujours vérifier les conditions de LA série avant publication ; footer = source réelle.

## Annexe B — points d'entrée opérationnels (testés) — lire `references/02-points-entree-endpoints.md` avant tout fetch, et dès qu'un accès échoue

Bloquant :
- Il y a trois routes vers une source, de la plus rapide à la plus lente. **Les essayer dans cet ordre**, et ne descendre d'un cran qu'après un échec constaté. 1. **`curl` depuis le Bash** — la plus rapide, et elle rend le fichier brut. 2. **`WebFetch`** — quand on veut une lecture de page plutôt qu'un fichier. 3. **Le Browser pane** (`navigate`, `get_page_text`, `javascript_tool`) — le repli quand les deux premières échouent, et **la seule route pour une page derrière authentification** (un écran wp-admin, par exemple). ⚠️ **Ne pas inverser cet ordre.** Le Browser pane coûte plusieurs tours par lecture ; `curl` en coûte un.
- **La règle** : un 403, un 503 ou un timeout se **teste** avant d'être conclu, et se **date** quand il est consigné. Ne jamais écrire « cette source est bloquée » — écrire « bloquée depuis tel environnement, le tel jour », et passer à la route suivante. Une note d'échec non datée fait perdre plus de temps qu'elle n'en fait gagner : elle détourne durablement de la route la plus rapide.
- **Vérifier le calendrier de chaque place avant de dater une clôture.** Les bourses ne ferment pas les mêmes jours. Cas vécu : le **31 août 2026** était le Summer Bank Holiday britannique. Ni clôture FTSE 100, ni fixing LBMA ce jour-là — alors que Paris, Francfort et New York cotaient. Une valeur « au 31 » aurait été fausse sur deux lignes d'un même tableau, sans qu'aucun contrôle ne le signale.
- FRED, replis si l'accès direct échoue. Dans l'ordre : la **route en deux temps** (charger la page de la série, puis `fred.stlouisfed.org/data/{SERIES_ID}.txt`) · les **miroirs Eco3min** (`https://eco3min.fr/dataset/{id}.csv` — ce que servent réellement les pages du site, donc ce qu'il faut auditer) · l'**émetteur direct** (US Treasury pour les CMT, BLS pour l'IPC, NY Fed pour l'ACM — souvent plus frais que FRED) · l'API FRED officielle avec clé. Ne jamais conclure « la donnée n'existe pas » sur un seul échec d'accès.
- Trois sources refusent les requêtes sans `User-Agent` explicite. Le symptôme n'est pas une erreur claire : c'est un refus ou une réponse vide, qu'on met du temps à attribuer à l'en-tête. BLS et World Bank WDI exigent un `User-Agent` avec un contact réel (`Eco3min research contact@eco3min.fr`) ; OECD SDMX exige `format=csvfilewithlabels` ; BLS v1 ignore les filtres d'année et plafonne à 10 ans par appel ; Shiller `ie_data.xls` se parse avec `xlrd==1.2.0` ; Jacks 1850–2025 est bloqué par captcha (demander le fichier) ; Pink Sheet : données à partir de la ligne 10, URL qui change chaque année.
- Cours de clôture datés : S&P 500 et Dow via FRED (`SP500`, `DJIA`, usage cotation ponctuelle seulement, cf. ajout du 17/09/2026), Nasdaq via `api.nasdaq.com`, Euronext via `live.euronext.com`, or via LBMA ; **DAX, Euro Stoxx 50** : **aucune source primaire datée connue** — Deutsche Börse et STOXX sont restés inaccessibles.
- Règle d'arrêt : Si une source nécessaire est bloquée : **s'arrêter et demander les fichiers à Paul.** Ne jamais substituer la mémoire du modèle à une récupération ratée.
- Réflexe : Tout endpoint mis en dur périme. Avant d'en déclarer un mort, vérifier que ce n'est pas simplement l'année ou le nom de fichier qui a tourné — c'est le cas le plus fréquent, notamment sur le Pink Sheet.

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

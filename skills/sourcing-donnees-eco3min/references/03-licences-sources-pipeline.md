# sourcing-donnees-eco3min — référence : licences des sources réellement en pipeline, hors FRED

AJOUT du 17/09/2026 (pas un extrait de SKILL.md). Fait foi avec SKILL.md ; SKILL.md porte
la version condensée et le moment où lire ce fichier. Chaque ligne porte son statut de
vérification : **vérifié JJ/MM/AAAA** = conditions relues ce jour à la source ; **connu** =
déjà écrit dans le skill ou dans `eco3min-data/scripts/source_rights.py` ; **à vérifier** =
présomption, à relire avant toute publication d'un CSV de cette source. Une ligne « à
vérifier » n'autorise rien.

## Les trois usages d'une donnée, à trancher avant de choisir la source

Les CGU d'une source distinguent presque toujours ces trois usages, et le pipeline les
confondait :

| Usage | Exemple Eco3min | Ce qui compte |
|---|---|---|
| **(a) Cotation ponctuelle** citée en prose ou dans un tableau daté | baromètre mensuel, bulletin, « clôture au 31 » | un fait de marché, attribué ; la source peut interdire le scraping en boucle, pas la citation d'un chiffre lu |
| **(b) Série tracée** dans un visuel publié | hero, chart d'étude, Chart of the Week | reproduction d'une part d'une base : attribution, et la source ne doit pas interdire l'usage commercial |
| **(c) CSV / XLSX redistribué** au téléchargement | page dataset, fichier d'étude | **redistribution** : c'est l'usage que la plupart des CGU d'API interdisent, même quand (a) et (b) sont permis ; la licence affichée doit être celle de la source, jamais CC BY par défaut |

Une source « OK » pour le baromètre n'est pas « OK » pour une page dataset. La question à
poser n'est pas « la source est-elle propre ? » mais « propre **pour lequel des trois** ? ».

## Table des sources

| Source | Famille | Conditions | Attribution | (a) prose | (b) visuel | (c) CSV | Statut | Clé `source_rights` |
|---|---|---|---|---|---|---|---|---|
| **FRED — public domain: citation requested** | primaire US | domaine public, citation demandée | source + « retrieved from FRED » | oui | oui | **oui, CC BY 4.0** | vérifié 17/09/2026 (`scripts/fred_license.py`, 19 séries) | défaut du snippet |
| **FRED — copyrighted: citation required** (Chicago Fed, St. Louis Fed, NY Fed, Dallas Fed, Moody's `BAA`, `T10Y2Y`, `T5YIE`, `T10YIE`, `RRPONTSYD`, `USREC`, `M2V`, `VIXCLS`, `PCOPPUSDM`, `CBBTCUSD`, `CBETHUSD`) | via FRED | usage commercial et affichage OK, **pas de sous-licence** | source ET FRED | oui | oui | oui, **jamais CC BY** : licence FRED déclarée | vérifié 17/09/2026 | `chicago_fed`, `stlouis_fed`, `ny_fed`, `dallas_fed` (snippet 36) — ajouter la clé de tout nouveau producteur |
| **FRED — copyrighted: pre-approval required** (`BAML*`, `SP500`, `NASDAQCOM`, `DJIA`, `CSUSHPINSA`, Case-Shiller) | via FRED | rien sans accord écrit du détenteur | — | **non** (pas de niveau brut) | **non** | **non** | vérifié 17/09/2026 | aucune : retirer ou re-sourcer (prix d'ETF, Shiller, French) |
| **World Bank** (WDI, Pink Sheet or / argent / cuivre / énergie, `FP.CPI.TOTL`) | primaire multi-pays | CC BY 4.0 | « World Bank » + jeu de données | oui | oui | oui, CC BY 4.0 | connu (skill, annexe A) | défaut |
| **IMF** (PCPS, IFS, WEO, PortWatch) | primaire multi-pays | IMF Terms and Conditions (11/10/2024) : attribution, intégrité, **mêmes conditions en aval** | « Source: International Monetary Fund, … » | oui | oui | oui, **jamais CC BY** | connu (`source_rights.py`) ; PortWatch **à vérifier** | `imf-pcps`, `imf-ifs` |
| **OECD** (MEI, SDMX) | primaire multi-pays | CC BY 4.0 par défaut (Open by Default) ; **vérifier la série** (quelques séries hébergées portent des restrictions de tiers) | « OECD » | oui | oui | oui, CC BY 4.0 | connu (`source_rights.py`) | `oecd-mei` |
| **Bank of England** (IADB) | primaire UK | Open Government Licence v3.0 | « Bank of England » | oui | oui | oui | connu (`source_rights.py`) | `boe-ogl` |
| **ECB Data Portal** (SDMX) | primaire zone euro | reproduction autorisée avec mention de la source | « Source: ECB » | oui | oui | oui, attribution | **à vérifier** (termes ECB non relus le 17/09/2026) | à créer si un CSV ECB se déclare autrement que CC BY |
| **Eurostat** | primaire UE | CC BY 4.0 (politique de réutilisation Eurostat) | « Eurostat » | oui | oui | oui | **à vérifier** | — |
| **INSEE**, **Banque de France Webstat** | primaire FR | INSEE : Licence Ouverte Etalab 2.0 ; BdF : attribution | « Insee » / « Banque de France » | oui | oui | oui | **à vérifier** (BdF) | — |
| **BLS**, **US Treasury**, **BEA**, **EIA**, **USDA NASS**, **Board (H.4.1, GSW `feds200805.csv`)** | primaire US, administration fédérale | domaine public US | citation demandée | oui | oui | oui, CC BY 4.0 sur la compilation | connu (études R1, R6 ; EIA « domaine public déclaré ») | défaut |
| **BIS** | primaire multi-pays | reproduction autorisée avec attribution | « BIS » | oui | oui | oui, attribution | **à vérifier** (termes BIS non relus) | — |
| **NY Fed** direct (ACM, modèle de récession, Damodaran hébergé ailleurs) | primaire US | libre avec citation | « Federal Reserve Bank of New York » | oui | oui | oui, attribution | connu (via FRED : `ny_fed` citation required) | `ny_fed` |
| **Robert Shiller** (`ie_data.xls`) | académique | **aucune licence déclarée** ; usage académique de fait ; le classeur contient des **niveaux S&P composite** (Cowles + S&P) | « Robert J. Shiller, Yale » | oui | oui | dérivés (CAPE, rendements) oui ; **niveaux d'indice : à statuer** — même logique que `SP500` pre-approval | **à statuer** (décision Paul) | — |
| **Kenneth French Data Library** (Fama-French, versions régionales) | académique | © Fama & French, usage libre avec citation | « Kenneth R. French Data Library » | oui | oui | oui, attribution | connu (skill, annexe A) | — |
| **CoinGecko** (API publique) | agrégateur crypto | intégration commerciale autorisée (§4.1.6) ; **redistribution des données interdite** (§4.1.6, §6.2) ; attribution « Powered by CoinGecko » ≥ 10 pt (§4.4) ; cache ≤ 24 h | « Powered by CoinGecko » | oui | oui, avec « Powered by CoinGecko » | **NON** | vérifié 17/09/2026 (coingecko.com/en/api_terms) | aucune — les CSV `bitcoin-price` / `ethereum-price` étaient en défaut, **corrigés le 17/09/2026** : FRED `CBBTCUSD` / `CBETHUSD` (Coinbase, citation required, clés `coinbase-btc` / `coinbase-eth`, historique depuis 2014 / 2016 contre 365 jours) |
| **LBMA** (`prices.lbma.org.uk/json/gold_pm.json`, `silver.json`) | benchmark sous licence | « A licence from IBA is required in order to obtain, use or redistribute real-time or historical benchmark data » | « LBMA Gold Price, administered by ICE Benchmark Administration » | oui (une clôture datée, baromètre) | **à vérifier** | **NON** sans licence IBA | vérifié 17/09/2026 (lbma.org.uk/prices-and-data) | aucune — l'historique or / argent du site vient du **Pink Sheet** (CC BY 4.0, moyenne mensuelle du fixing PM) : le label doit le dire, « LBMA » seul est un relabellisage |
| **ENTSO-E Transparency Platform** | primaire énergie UE | données de la liste ouverte sous CC BY 4.0, attribution ENTSO-E ; **vérifier que la série précise est sur la liste ouverte** | « ENTSO-E Transparency Platform » | oui | oui | oui si liste ouverte | recherche 17/09/2026, termes complets non relus (**à vérifier** par série) | — |
| **AGSI+ / ALSI** (GIE) | primaire énergie UE | **non relu** ; présomption d'attribution GIE requise | « GIE AGSI+ » | oui | à vérifier | **à vérifier** | **à vérifier** (17/09/2026 : page de termes injoignable) | — |
| **FAO** (FFPI) | primaire | CC BY 4.0 | « FAO » | oui | oui | oui | connu (skill, annexe B) | — |
| **Nasdaq** (`api.nasdaq.com`), **Euronext** (`live.euronext.com`) | place de marché | CGU de site non relues le 17/09/2026 ; **forte présomption** d'interdiction du scraping et de la redistribution | nom de la place | **oui, une clôture datée** | non | **NON** | **à vérifier** avant tout autre usage que (a) | — |
| **DBnomics** | agrégateur institutionnel | hérite de la source d'origine | la source d'origine, pas DBnomics | selon source | selon source | selon source | connu (skill, annexe A) | celle de la source |
| **Yahoo Finance, yfinance, investing.com, MarketBeat, Stooq, CEIC, Trading Economics** | agrégateurs scrapés / payants | CGU : extraction automatisée et/ou usage commercial interdits | — | non | **non** | **non** | connu (skill, interdiction ferme) | aucune |

## Ce que cette table change concrètement

1. **BTC / ETH** : le pipeline construisait `bitcoin-price` et `ethereum-price` depuis
   CoinGecko et les servait en CSV. **Corrigé le 17/09/2026** : builders v2 sur FRED
   `CBBTCUSD` / `CBETHUSD`, clés `coinbase-btc` / `coinbase-eth` (pipeline) et
   `coinbase_btc` / `coinbase_eth` (snippets 36 et 114), pages 10869 et 10870 réécrites,
   CSV servis depuis 2014-12-01 et 2016-05-18. Le raisonnement reste valable pour toute
   autre source d'API : lire les termes avant de servir un CSV. C'est l'usage (c), interdit par les API Terms. Route
   propre : FRED `CBBTCUSD` (Coinbase Bitcoin, depuis 2014-12) et `CBETHUSD` (depuis
   2016-05), « copyrighted: citation required » lus le 17/09/2026 → publiable avec
   attribution Coinbase + FRED, licence FRED déclarée par `eco3_source_rights()`, jamais
   CC BY. Bonus : dix ans d'historique contre 365 jours glissants (§5.2 de
   `pipeline-eco3min`). À remonter côté pipeline ; hors périmètre de ce skill.
2. **Or / argent** : la donnée servie est le Pink Sheet (CC BY 4.0). Le nom de dataset
   « Gold Price History (LBMA) » dans `DATASET_REGISTRY` et tout label « LBMA » seul
   contredisent la règle cardinale (le label = la source réelle). **Corrigé le
   17/09/2026** : registry renommé « Gold / Silver Price History (World Bank Pink
   Sheet) » ; les pages 10874 et 10881 attribuaient déjà le Pink Sheet (LBMA n'y est
   cité que comme marché sous-jacent ou référence alternative, ce qui est exact) ; la
   phrase « public domain » de la page argent remplacée par CC BY 4.0. Label attendu :
   « World Bank Pink Sheet — London PM fix, monthly average ». À remonter côté
   `production-dataset` / pipeline.
3. **Une clôture du baromètre** (Nasdaq, Euronext, LBMA) reste un usage (a) : un chiffre
   daté, attribué, lu une fois. Ne jamais en faire une série tracée ni un CSV sans
   relire les CGU.
4. **Toute nouvelle famille de source** entre dans le pipeline avec sa clé dans
   `eco3min-data/scripts/source_rights.py` ET son miroir `eco3_source_rights()`
   (snippets 36 et 114). Sans clé, le défaut CC BY 4.0 du snippet s'applique à tort :
   c'est exactement le défaut corrigé sur 22 pages le 16/09/2026
   (`out/licence-fix-2026-09-16/RAPPORT.md` du projet GENERIQUE).
5. **Le tag FRED d'une série peut changer.** Relire les tags des séries publiées à chaque
   revue de datasets (`python scripts/fred_license.py <IDs>`, code retour 2 si un
   niveau pre-approval apparaît), pas seulement à la création de la page.

## Attributions : où vivent les chaînes

Les chaînes d'attribution et les notices ne se recopient pas ici : elles vivent dans
`eco3min-data/scripts/source_rights.py` (onglet « Source » du XLSX, bloc `attribution`
du meta JSON) et dans `eco3_source_rights()` (JSON-LD `license`, `usageInfo`,
`copyrightHolder`, `citation`, notice visible). Une source citée dans cette table sans
clé et publiée en (c) doit d'abord recevoir sa clé.

## Sources relues le 17/09/2026

- LBMA : https://www.lbma.org.uk/prices-and-data/precious-metal-prices
- CoinGecko : https://www.coingecko.com/en/api_terms
- FRED : tags `series-tag` de 25 séries lus par `scripts/fred_license.py`
- ENTSO-E : recherche web (liste de données ouvertes CC BY 4.0, Regulation 543/2013) ;
  termes complets à relire sur transparency.entsoe.eu (« Terms and Conditions »)
- AGSI+, Nasdaq, Euronext, ECB, Eurostat, BIS, Banque de France : **non relus**

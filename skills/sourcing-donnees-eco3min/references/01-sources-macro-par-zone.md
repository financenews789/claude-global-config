# sourcing-donnees-eco3min — référence : Annexe A, sources macro mondiales gratuites (équivalents FRED par zone)

Extrait VERBATIM de SKILL.md (découpage du 17/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

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

# production-dataset — référence : Positionnement éditorial, tests de qualité, familles de sources (§1, §2)

Extrait VERBATIM de SKILL.md (découpage du 16/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

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

> Mise à jour du 17/09/2026 : CoinGecko retiré des familles vivantes (ses API Terms interdisent la redistribution des données). BTC / ETH relèvent désormais de la famille FRED (Coinbase `CBBTCUSD` / `CBETHUSD`, « citation required » → licence FRED déclarée par `rights`, jamais CC BY). LBMA ne sert qu'une clôture citée, jamais un CSV ; l'historique or / argent est le World Bank Pink Sheet. Voir §12.4.

**Conséquences directes :**
- Le texte du spinner est **`Loading data…`** (générique), pas `Loading FRED data…` — il sert pour toutes les sources.
- La méthodologie ne dit `pull from the FRED API` que si la source EST FRED. Pour ECB → « pull from the ECB SDMX API », pour Shiller → « pull Shiller's ie_data.xls workbook », pour un composite → « recomputed by an Eco3min pipeline that combines… ».
- Ne **jamais** citer « FRED » comme source unique d'un composite qui a une composante non-FRED (Shiller, Damodaran, CoinGecko, LBMA).

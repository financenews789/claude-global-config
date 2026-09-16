# production-dataset — référence : Sourcing, maillage interne, canvas, shortcodes, pipelines, paire FR/EN (§12 à §15)

Extrait VERBATIM de SKILL.md (découpage du 16/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

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

La page reflète un CSV/JSON mis à jour automatiquement. **Le détail du pipeline (codage, series_id, cron, connecteur API) relève de la skill `pipeline-eco3min`.** Ici, on ne retient que la cadence pour la Methodology :
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

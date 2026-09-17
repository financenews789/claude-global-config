# production-dataset — référence : Sourcing, maillage interne, canvas, shortcodes, pipelines, paire FR/EN (§12 à §15)

Extrait VERBATIM de SKILL.md (découpage du 16/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 12. Sourcing — règles strictes

### 12.1 Sources primaires nommées
Au minimum **2 sources nommées** dans le bloc Sources : l'éditeur de la donnée + l'agrégateur via lequel Eco3min extrait. Pour un composite, **toutes** les composantes.
Cas miroir (commodities) : nommer la source d'origine ET le miroir — « IMF Primary Commodity Prices (via FRED series PCOFFOTMUSDM) ».

### 12.2 Format dans le texte
Sources intégrées au flux, jamais en bibliographie : « FRED series NASDAQCOM », « ECB SDMX, BSI dataset », « ENTSO-E Transparency Platform », « Robert Shiller, Yale (ie_data.xls) », « CoinGecko API ».

### 12.3 Whitelist des sources autorisées
Depuis le 17/09/2026, la liste plate est remplacée par la table de `sourcing-donnees-eco3min/references/03-licences-sources-pipeline.md`, qui distingue trois usages : (a) cotation citée en prose, (b) série tracée dans un visuel, (c) CSV redistribué. **Une page dataset relève de (c).** Oui pour (c), avec la licence réelle déclarée : FRED public domain et citation required, ECB, Eurostat, BIS, BLS, BEA, NBER, INSEE, Banque de France, IMF, OECD, World Bank (dont Pink Sheet), FAO, Shiller (dérivés seulement), Kenneth French, Damodaran. Citables en (a) mais **pas de CSV** : CoinGecko, LBMA, S&P Dow Jones Indices, MSCI, CBOE hors séries FRED (VIXCLS est citation required via FRED), Nasdaq, Euronext — c'était la liste des pages en défaut corrigées les 16 et 17/09/2026. AGSI+/GIE et ENTSO-E : ligne « à vérifier » dans la table, donc pas de page tant qu'elle n'est pas datée.

Toute autre source nommée doit être **web_search-vérifiée** avant publication, puis ajoutée à la table avec sa date. Les sources sous licence/paywall (EPEX/Nord Pool électricité, Caixin PMI, etc.) ne sont pas redistribuables : si une donnée en dépend, NE PAS produire la page avant résolution de la licence.

### 12.4 Licence affichée = conditions réelles de la source (ajout du 17/09/2026)

La page dit de la licence exactement ce que la source permet, ni plus ni moins.
- **Ce que la prose peut écrire.** « CC BY 4.0 » ou « public domain » seulement si la source l'est (FRED public domain, World Bank, OECD, FAO, EIA, BLS). Une série FRED « copyrighted: citation required » (Chicago Fed, NY Fed, Moody's `BAA`, `T10YIE`, `RRPONTSYD`, `VIXCLS`, `PCOPPUSDM`, Coinbase `CBBTCUSD` / `CBETHUSD`), une série IMF ou BoE se décrit comme réutilisable **avec attribution à la source et à FRED**, jamais sous Creative Commons. Une série « pre-approval required » (`SP500`, `NASDAQCOM`, `DJIA`, `BAML*`, Case-Shiller) n'a pas de page dataset qui redistribue : re-sourcer (prix d'ETF, Shiller, French) ou n'embarquer que le graphique servi par FRED en le disant.
- **Ce que le snippet déclare.** La ligne du dataset dans le snippet 36 (US) ou 114 (non-US) porte `'rights' => '<clé>'` quand la source l'exige (`imf`, `imf_ifs`, `chicago_fed`, `stlouis_fed`, `ny_fed`, `dallas_fed`, `boe`, `oecd`, `coinbase_btc`, `coinbase_eth` au 17/09/2026). C'est elle qui met `license` / `usageInfo` / `copyrightHolder` / `citation` dans le JSON-LD et la notice « Source terms » sous la page. Sans clé, le JSON-LD annonce CC BY 4.0 à tort : 22 pages corrigées le 16/09/2026 pour cette raison. La clé vit en miroir dans `eco3min-data/scripts/source_rights.py` (`pipeline-eco3min` §2.6) : les deux registres évoluent ensemble.
- **Ce que le H1 et l'Overview promettent.** La source réelle (Pink Sheet, pas « LBMA Fix » ; Coinbase via FRED, pas CoinGecko), la profondeur réelle (2014 pour `CBBTCUSD`, pas 2010), les formats réellement servis (une page qui n'embarque qu'un graphique FRED ne dit pas « CSV, Excel »). Le `name` du registry pipeline et le H1 disent la même source.
- **Le statut se lit par script**, jamais de mémoire : `python ~/.claude/skills/sourcing-donnees-eco3min/scripts/fred_license.py <ID>` (code retour 2 = pre-approval).
- **Test sur la page rendue** : `curl -s <url> | grep -o '"license":"[^"]*"'` et la phrase de la prose disent la même chose ; une page « citation required » affiche la notice « Source terms » ; `grep -c 'CC BY'` vaut 0 sur une page dont la source n'est pas CC BY.

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
- Mise à jour du 17/09/2026 : BTC / ETH ne viennent plus de CoinGecko mais de FRED (`CBBTCUSD` / `CBETHUSD`, pipeline v2, quotidien) ; or / argent sont mensuels (Pink Sheet). La Methodology dit « pulled from the FRED API (Coinbase series CBBTCUSD) », pas « CoinGecko ».
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

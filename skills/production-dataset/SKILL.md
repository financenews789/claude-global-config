---
name: production-dataset
description: "Production et révision des pages dataset Eco3min (eco3min.fr) : la page qui expose une série, en anglais par défaut (FR seul pour les séries françaises INSEE / Banque de France, paire FR/EN sur décision explicite) — séries d'une source primaire (FRED, ECB SDMX, IMF, BIS, BLS, Eurostat, Shiller, World Bank, CoinGecko, LBMA, ENTSO-E, AGSI+, FAO…) et composites construits par Eco3min (ratios, séries réelles déflatées, indicateurs propriétaires type Net Liquidity Index, Excess CAPE Yield). Activer pour « crée la page dataset », « révise la page DGS10 », « page dataset du composite », « quel H1 pour ce ticker », « Cas A ou A' ? », « Macro Takeaway », « Historical Regimes », « eco3min_latest », « eco3min_key_stats », « eco3min_download », « data-series », « dataset_id », « /dataset/{slug}.csv », et pour toute page dont l'URL finit en -dataset/. SKILL.md = colonne vertébrale (§0 table des trois cas A / A' / B verbatim, règles bloquantes §1 à §15 sous leurs numéros d'origine, anti-patterns SEO, AMF, critère de publication, checklist et rappel zéro commentaire HTML verbatim) ; références dans references/ (à lire quand la section le dit) : 01 positionnement et familles de sources, 02 stratégie SEO par cas et convention de slug, 03 template HTML complet des 18 blocs et préservation byte-level, 04 sections éditoriales (Macro Takeaway, Construction, What This Index Captures, Data Quality, Historical Regimes, intro), 05 sourcing, maillage, canvas et shortcodes, paire FR/EN ; pas de scripts/. Doctrines : source et stratégie SEO sont deux axes orthogonaux, le H1 ne se déduit jamais de la source (PCOFFOTMUSDM est FRED mais Cas A') ; Cas A = ticker googlé en H1, A' et B = concept canonique, code interne (NET_LIQ, SP500_M2) 0 fois dans H1 / meta / focus keyword ; Cas B = sections Construction & Components + What This Index Captures + Data Quality obligatoires, Construction = formule et composantes, Methodology = pipeline, jamais dupliquées ; ordre des 18 sections immuable ; spinner « Loading data… » générique, jamais « Loading FRED data… » ; jamais FRED cité comme source unique d'un composite à composante non-FRED ; dataset_id immuable une fois fixé ; préservation byte-level en révision (shortcodes, canvas, pre Python/R) ; canvas rendu ou omis selon le script global, jamais de canvas mort ; 4 à 6 régimes datés et chiffrés ; 6 à 12 liens internes, EN→EN FR→FR, pas d'auto-référence ; whitelist de sources, paywall = pas de page ; langue = langue de la donnée, pas de doublage FR systématique (décision du 16/09/2026) ; AMF descriptif jamais prescriptif, vigilance renforcée Cas B ; zéro script, zéro commentaire HTML dans le contenu publié (incident Autoptimize du 27 août 2026). Hors périmètre : création du CSV, series_id, cron → pipeline-eco3min ; études avec hypothèse et narrative → production-research-study ; pages « Every X since Y » → production-every-x-record ; charts DIB → production-chart-of-the-week ; cluster éditorial autour d'un ticker → cluster-ticker-renfort-dataset ; identité éditoriale et six règles AMF → editeur-eco3min. Combiner avec editeur-eco3min, formats-eco3min, visuels-eco3min, brand-kit-eco3min, pipeline-eco3min, archi-eco3min, eco3min-import-contenu-bilingue, cluster-ticker-renfort-dataset."
---

# Production de pages dataset — Eco3min

> Ce skill couvre les **pages dataset** : séries d'une source primaire (FRED, ECB SDMX, IMF, BIS, BLS, Eurostat, Shiller, World Bank, CoinGecko, LBMA, ENTSO-E, AGSI+, FAO…) **et** composites construits par Eco3min (ratios, séries réelles déflatées, indicateurs propriétaires). Format standardisé : graphique, tableau, méthodologie, régimes.
>
> Pour les **études approfondies** (research studies avec hypothèse, narrative, analyse adversariale), voir la skill `production-research-study` — ces deux formats ne se confondent pas.
>
> La **création du fichier CSV/JSON** (codage du pipeline, vérification du series_id, fréquence cron) relève de la skill `pipeline-eco3min`. Ici, on suppose que le CSV `/dataset/{slug}.csv` existe déjà ou est en cours de production ; la page n'en mentionne que la cadence de mise à jour.
>
> Voir aussi `editeur-eco3min` (identité éditoriale, AMF), `formats-eco3min` (patterns rédactionnels), `visuels-eco3min` (data viz).

---

## COMMENT LIRE CE SKILL (découpage du 16/09/2026)

Ce fichier est la colonne vertébrale : le périmètre, la table des trois cas (§0, verbatim : elle pilote tout), puis pour chaque section les règles BLOQUANTES sous leurs numéros d'origine (§3.4, §5.1, §14.1… : d'autres skills et des CLAUDE.md de projets y renvoient), enfin AMF, critère de publication, checklist et rappel zéro commentaire HTML, verbatim. Les tableaux d'exemples, le template HTML complet, les rationales et les conventions détaillées ont été déplacés VERBATIM dans `references/` et font foi au même titre que ce fichier. Chaque section ci-dessous nomme le fichier à lire ; le lire est obligatoire au moment indiqué, pas facultatif. Pas de `scripts/` : le seul contrôle Python tient en deux lignes et reste ici.

| Fichier | Contenu | À lire |
|---|---|---|
| `references/01-positionnement-sources.md` | §1, §2 : ce que la page apporte vs la source, tests de qualité A/A' et B, tableau des trois familles de sources, conséquences sur spinner, Methodology et bloc Sources | avant de rédiger le Macro Takeaway et le bloc d'accès aux données |
| `references/02-strategie-seo-slug.md` | §3, §4 : H1, meta title, focus keyword par cas avec exemples, note FX, meta description Cas B, anti-patterns SEO, quatre territoires, tableau slug / URL / codes | avant de fixer H1, meta, focus keyword et `dataset_id` |
| `references/03-template-html.md` | §5, §5.1 : template HTML complet des 18 blocs avec les blocs [COMPOSITE], ordre immuable, préservation byte-level | avant d'assembler la page, et avant toute révision d'une page existante |
| `references/04-sections-editoriales.md` | §6 à §11 : Macro Takeaway, Construction & Components, What This Index Captures, Data Quality & Provider Notes, Historical Regimes, intro éditoriale | avant d'écrire chacune de ces sections |
| `references/05-sourcing-maillage-technique-bilingue.md` | §12 à §15 : whitelist des sources, format des sources, tableau de maillage, canvas, shortcodes, cadence des pipelines, paire FR/EN | avant le bloc Sources, le maillage, le canvas, et avant toute paire FR/EN |

---

## 0. Avant de produire — identifier le CAS

Toute page dataset relève d'un des trois cas. **Le cas pilote le H1, la meta, le bloc d'accès aux données, et la présence ou non des sections composites.** On ne devine pas : le cas vient du mapping (`seo_subtype`) ou, pour les nouveaux datasets, d'une décision explicite selon la grille §3.

| Cas | `seo_subtype` (mapping) | Source réelle | H1 commence par | Sections composites |
|---|---|---|---|---|
| **A** | `fred_ticker` | FRED, **ticker réellement googlé** (DGS10, VIX, WALCL) | le **ticker** | non |
| **A'** | `non_fred_keyword` | FRED **non-googlé** OU non-FRED (Shiller, CoinGecko, ISM, IMF mirror…) | le **concept canonique** | non |
| **B** | `composite_no_ticker` | multi-source / dérivé (ratio, réel, propriétaire) | le **concept canonique** | **oui** (Construction & Components + What This Index Captures + Data Quality) |

⚠️ **Source et stratégie SEO sont deux axes orthogonaux.** Une série peut être FRED-sourcée et rester Cas A' : `PCOFFOTMUSDM` (café arabica) est confirmé sur FRED mais personne ne google ce code — le H1 vise `Arabica Coffee Price`, pas le code. Ne **jamais** déduire le H1 de la source. La question n'est pas « est-ce du FRED ? » mais « le code est-il un ticker que des gens tapent dans Google ? ». DGS10/VIX/WALCL → oui (Cas A). PCOFFOTMUSDM/PCOCOUSDM/PIORECRUSDM → non (Cas A').

---

## 1. Positionnement éditorial (lire `references/01-positionnement-sources.md`)

Bloquant :
- Une page dataset Eco3min n'est **pas un miroir** de la source primaire. Elle apporte trois éléments absents du site amont : le Macro Takeaway analytique (la donnée mise en relation avec le régime macro), les Historical Regimes (décomposition datée et nommée, avec mécanisme), l'accès programmatique unifié (URL CSV stable `/dataset/{slug}.csv` + exemples Python/R).
- Cas B : la valeur ajoutée est de **construire une série qui n'existe nulle part en natif** ; la section Construction & Components (§7) est l'élément différenciant SEO (« how is net liquidity index calculated », « real interest rate formula »).
- **Test de qualité (Cas A / A')** : si la page peut être remplacée par un lien vers la source primaire sans perte d'information, elle ne mérite pas d'être publiée.
- **Test de qualité (Cas B)** : le test ci-dessus est trivial (un composite n'existe pas en série native). Le vrai test : la section Construction explique-t-elle la formule, les composantes et leur réconciliation de fréquence de façon reproductible ? Sinon, retravailler.

## 2. Sources de données (lire `references/01-positionnement-sources.md`)

Bloquant :
- Trois familles, qui changent le bloc d'accès aux données (§5, position « Source Data Access ») et le bloc Sources final : **FRED public** (CSV `fredgraph.csv?id=CODE`, `data-series` = code FRED majuscules) ; **non-FRED à API/CSV** (ECB SDMX, Eurostat, IMF, BIS, World Bank, AGSI+/GIE, ENTSO-E, FAO, CoinGecko : pas de fredgraph, pointer la page source ou seulement le CSV Eco3min ; graphique omis si le script global ne lit pas la source, §14.1) ; **composite** (pas de fredgraph unique : si toutes les composantes sont FRED-publiques → lister les séries composantes, sinon CSV Eco3min uniquement ; `data-series` = code interne NET_LIQ, SP500_M2… — jamais en SEO).
- Le texte du spinner est **`Loading data…`** (générique), pas `Loading FRED data…` — il sert pour toutes les sources.
- La méthodologie ne dit `pull from the FRED API` que si la source EST FRED. Pour ECB → « pull from the ECB SDMX API », pour Shiller → « pull Shiller's ie_data.xls workbook », pour un composite → « recomputed by an Eco3min pipeline that combines… ».
- Ne **jamais** citer « FRED » comme source unique d'un composite qui a une composante non-FRED (Shiller, Damodaran, CoinGecko, LBMA).

## 3. Stratégie SEO par cas — H1, meta, focus keyword (lire `references/02-strategie-seo-slug.md`)

Bloquant :
- **Cas A** : H1 `{TICKER}: {Description analytique}` ; le ticker ouvre le H1 et la meta title ; focus keyword = ticker (`dgs10`). Note FX : un cross devise se google sous sa forme humaine (`USD/JPY`, `EUR/USD`), pas sous le code FRED (`DEXJPUS`) ; le H1 vise le pair humain.
- **Cas A'** : H1 `{Concept canonique}: {Description}` ; le code source (FRED ou autre) **n'apparaît jamais** en tête ; la source réelle est nommée dans le bloc Sources et la Methodology, **pas** dans le H1 ; focus keyword = concept en minuscules (`arabica coffee price`).
- **Cas B** : H1 `{Concept canonique}: {Construction analytique}` ; le **code interne** (NET_LIQ, SP500_M2, WALCL_GDP…) apparaît **0 fois** dans H1 / meta title / meta description.
- **Meta description (Cas B, non négociable)** : concept dans les 30 premiers caractères + construction explicite (composante 1 + composante 2 + opération) + mention **« Eco3min composite/calculation »** + couverture + signal d'usage (CSV, Python/R, daily/monthly, free). Cible 140-165 c.
- Quatre territoires (§3.5) : la page dataset vise le concept en tant que **DONNÉE** (« où la trouver, comment elle est construite, comment la télécharger ») ; l'étude evergreen (ANALYSE), le cluster MAJEUR et le sub-pilier ne sont pas son territoire. Une étude au nom proche (`net liquidity illusion` vs `net liquidity index`) se **maille depuis Related Research en bas**, jamais son angle n'est repris dans le corps.

### 3.4 Anti-patterns SEO (tous cas)

- ❌ Code interne en tête : `NETLIQ: Net Liquidity Index Data`, `SP500_M2: Liquidity-Adjusted Ratio`
- ❌ H1 éditorial = territoire d'une étude : `Net Liquidity Index Crashes Markets: What the Data Shows`
- ❌ Marketing creux : `The Ultimate Guide to Real Interest Rates in 2026`
- ❌ Trop large / ultra-concurrencé : `S&P 500: Complete Historical Returns Data`
- ❌ Déduire le H1 de la source : café FRED → `PCOFFOTMUSDM` en tête (faux : Cas A', concept)

## 4. Convention de slug et identifiants (lire `references/02-strategie-seo-slug.md`)

Bloquant :
- `dataset_id` (slug interne des shortcodes) : kebab-case, court, evergreen ; URL EN `/en/[slug-en]-dataset/` ; URL FR convention site (souvent racine) ; CSV `/dataset/{slug}.csv` ; JSON `/dataset/{slug}.json` ; code source = FRED majuscules / clé ECB SDMX / code IMF / code interne composite.
- **Règle filename immuable** : une fois le `dataset_id` fixé, il ne change JAMAIS. Pages HTML, pipelines, liens internes en dépendent. Renommer casse tout.
- **Code source vs code SEO** : le code source (`data-series` du canvas, `dataset_id` des shortcodes) est un identifiant **technique**. Pour les composites c'est un **code interne** (`NET_LIQ`) qui n'est ni un ticker FRED ni un mot-clé. Il ne doit jamais migrer vers le H1 / meta / focus keyword.

## 5. Structure HTML complète (lire `references/03-template-html.md`)

Bloquant :
- Le template de la référence est l'anatomie standard, **alignée sur l'anatomie cible de l'optimiseur Phase 2** : une page produite ainsi n'a pas à être re-restructurée. Les sections marquées **[COMPOSITE]** n'apparaissent **que pour le Cas B**. La section d'accès aux données s'adapte à la source (§2).
- **Ordre des sections (immuable).** Cas A/A' : 1→18 en sautant les blocs [COMPOSITE]. Cas B : tous les blocs, l'ordre canonique étant intro → shortcodes → chart → Macro Takeaway → **Construction & Components** → Overview → Variables → Download → accès données → Python/R → Methodology → **Data Quality** → **What This Index Captures** → Historical Regimes → Related → Hub → Sources → Reference (anatomie identique à la page Excess CAPE Yield de référence).
- Les marqueurs `<!-- 1. INTRO ÉDITORIALE -->` … du template sont des repères d'assemblage : ils sont retirés avant livraison (RAPPEL BLOQUANT en fin de fichier).

### 5.1 Préservation byte-level (révision d'une page existante)

Ne **jamais** réécrire ni supprimer : les shortcodes `[eco3min_latest|key_stats|download …]`, le `<canvas data-series="…">` (**même si data-series contient un code interne** `NET_LIQ`/`SP500_M2` — identifiant technique JS), le `<style>@keyframes ds-spin{…}</style>`, les `<pre>` Python/R, les tableaux Overview et Variables.

## 6. Macro Takeaway — section critique (lire `references/04-sections-editoriales.md`)

Bloquant :
- **Paragraphe 1 — mécanisme structurel** : rôle de la série dans la lecture macro, variables avec lesquelles elle interagit (taux, inflation, dollar, crédit), **au moins un lien interne contextuel**, 3-4 phrases denses. Cas B : nommer le concept canonique ; étude au nom proche maillée sans reprendre son angle.
- **Paragraphe 2 — illustration récente** : épisode daté précis, chiffres datés, mécanisme expliqué (le pourquoi, pas que le combien), 3-4 phrases.
- Conformité AMF — descriptif, jamais prescriptif. Pas de prédiction matérialisée (« the index will likely… », « the next move should… »). Tout au passé descriptif ou présent factuel.

## 7. Construction & Components — [COMPOSITE], section centrale (lire `references/04-sections-editoriales.md`)

Bloquant :
- 200-300 mots. Quatre blocs imposés (template §5, 5bis) : **Formula** (notation mathématique simple, sur une ligne, jamais en prose) ; **Components** (chaque composante : nom canonique + code/source + **fréquence native** + rôle ; nommer par la source canonique, « Fed Funds Effective Rate (FEDFUNDS) ») ; **Frequency reconciliation** (interpolation, forward-fill, ou « all monthly, no interpolation ») ; **Coverage** (plage précise + raison des bornes).
- Distinction stricte avec Methodology : **Construction = la formule et les composantes** ; **Methodology = le pipeline** (comment Eco3min produit techniquement la donnée). Ne pas dupliquer la formule en Methodology.

## 8. What This Index Captures (And What It Doesn't) — [COMPOSITE] (lire `references/04-sections-editoriales.md`)

Bloquant :
- 250-350 mots. **What it captures** : 3 aspects, descriptifs (❌ « use this indicator to time… »). **What it does NOT capture** : 3-4 misinterprétations, chacune en `<strong>` + 2-3 phrases factuelles. Clôture factuelle sur l'usage responsable (outil de classification de régime ≠ déclencheur tactique).
- AMF renforcé : les composites sont **plus interprétables** donc plus risqués (« Net Liquidity tombe → vendre »). Vigilance maximale, voir §16.

## 9. Data Quality & Provider Notes — [COMPOSITE] (lire `references/04-sections-editoriales.md`)

Bloquant :
- Trois angles : **latence dictée par la composante la plus lente** ; **propagation des révisions** (toute composante révisée change le composite en amont → Eco3min remplace le CSV entier à chaque release) ; **sources alternatives** (le plus souvent **aucune** série native équivalente ; si une alternative payante existe, la nommer factuellement).

## 10. Historical Regimes — signature Eco3min (lire `references/04-sections-editoriales.md`)

Les bornes d'épisodes et les événements nommés dans cette section viennent de `~/eco3min/eco3min-knowledge/``chronologie/events.csv` (mêmes dates, mêmes libellés de régime d'une page dataset à l'autre) ; un épisode cité mais absent y est ajouté avant publication.

Bloquant :
- 4 à 6 régimes datés et nommés, format `<p><strong>[Période] — [Nom].</strong> …</p>` **ou** `<ul><li><strong>…</strong></li></ul>`. **Nom distinctif** (pas « Period 1 ») ; **chiffres datés systématiquement** (« surged from 1,000 to 5,048 in five years », pas « rose strongly ») ; **mécanisme exprimé** ; **cohérence cross-régime**. Cas B : concept canonique mentionné 3-4× ; 2-3 liens datasets + 1-2 liens études.
- AMF : ✅ « Many stocks lost 90-99% of their value » (factuel) · ❌ « Investors who held growth stocks regretted not diversifying » (jugement rétroactif).

## 11. Intro éditoriale (lire `references/04-sections-editoriales.md`)

Bloquant :
- `<p class="eco3min-intro">` en ouverture. **Cas A/A'** : 2-3 phrases (ce qu'est l'indicateur ; couverture/source ; particularité optionnelle). Pas de « Welcome », « In this page », « Discover ». **Cas B** : 4-5 phrases denses, concept canonique nommé **2×** + mention explicite **« an Eco3min composite »/« Eco3min calculation »** + formule simplifiée + couverture précise.

## 12. Sourcing — règles strictes (lire `references/05-sourcing-maillage-technique-bilingue.md`)

Bloquant :
- Au minimum **2 sources nommées** dans le bloc Sources (éditeur de la donnée + agrégateur) ; composite : **toutes** les composantes ; miroir : origine ET miroir (« IMF Primary Commodity Prices (via FRED series PCOFFOTMUSDM) »).
- Sources intégrées au flux, jamais en bibliographie (« FRED series NASDAQCOM », « ECB SDMX, BSI dataset »).
- Whitelist des sources autorisées dans la référence (§12.3). Toute autre source nommée doit être **web_search-vérifiée** avant publication. Les sources sous licence/paywall (EPEX/Nord Pool, Caixin PMI…) ne sont pas redistribuables : NE PAS produire la page avant résolution de la licence.

## 13. Maillage interne (lire `references/05-sourcing-maillage-technique-bilingue.md`)

Bloquant :
- Macro Takeaway 1-2 liens contextuels ; Related Macroeconomic Datasets 4-6 ; Related Research 1-3 (dont l'étude au nom proche, Cas B) ; Deep analytical framework 1 lien vers le MAJEUR si `info.cluster != null` ; CTA Hub 1 lien vers `/en/research-data/` ou `/research-data/`. Cohérence linguistique EN→EN, FR→FR strict.
- **Total** : minimum 6 liens, idéalement 8-10, jamais plus de 12. Test silencieux par lien : « le lecteur de cette page veut probablement aussi [lien] parce que [raison précise] » ; sinon on retire. **Pas d'auto-référence.**

## 14. Conventions techniques (lire `references/05-sourcing-maillage-technique-bilingue.md`)

Bloquant :
- §14.1 `data-series` = code source en MAJUSCULES ou code interne composite ; ce n'est jamais le mot-clé SEO. `data-start` = `YYYY-MM-DD` de la première observation ; `data-color` = `#1a237e` par défaut. **Lisibilité par le script de chart** : si le script global ne lit pas la source ou le code interne, **le graphique ne se chargera pas** ; garder le canvas seulement si le script lit le CSV Eco3min, sinon **omettre le bloc graphique** (choix de la page Excess CAPE Yield de référence). Ne pas laisser un canvas mort.
- §14.2 Shortcodes : `[eco3min_latest dataset_id="[slug]" field="latest_date"]` (dernière observation), `field="end_date"` (date d'extraction), `[eco3min_key_stats dataset_id="[slug]"]`, `[eco3min_download dataset_id="[slug]"]`. Le `dataset_id` matche toujours exactement le slug `/dataset/{slug}.csv`.
- §14.3 Le détail du pipeline relève de `pipeline-eco3min` ; la Methodology ne retient que la cadence, adaptée à la source (« updated daily via automated pull from the FRED API » / « monthly, after Shiller refreshes ie_data.xls »).

## 15. Langue et paire FR/EN (lire `references/05-sourcing-maillage-technique-bilingue.md`)

Bloquant :
- **Langue = langue de la donnée (décision du 16/09/2026).** Une page dataset est produite en **EN** pour les séries globales (le ticker et le concept se googlent en anglais, le trafic dataset est largement machine) et en **FR seul** pour les séries françaises (INSEE, Banque de France : SMIC, IRL, PEL, crédit habitat…). Une **paire FR/EN** n'est produite que sur décision explicite : concept réellement googlé en FR (« taux réels », « ratio CAPE ») ou besoin de maillage d'un cluster FR. État au 16/09/2026 dans `snapshot.csv` : 196 datasets EN, 22 FR, aucune paire.
- Quand une paire existe : **structure HTML strictement identique** ; **même `dataset_id`** ; **liens internes différents** (EN→URLs EN, FR→URLs FR) ; Macro Takeaway, Construction, What This Captures, Historical Regimes **traduits intelligemment**, pas calques ; **codes Python/R inchangés**, **sources identiques**.

---

## 16. Conformité AMF

Les 6 règles de `editeur-eco3min` s'appliquent. Spécificités datasets :

| Règle | Application |
|---|---|
| 1 — Pas de % d'allocation | Aucune mention de « X% allocation to this index », même en exemple |
| 2 — Pas de « should/devrait » | Macro Takeaway, Historical Regimes, What This Captures en descriptif |
| 3 — Pas de « Buy when Y » | Aucun signal d'entrée matérialisé |
| 4 — N/A (pas de FAQ ici) | — |
| 5 — Comparaisons géographiques en chiffres | OK si statistique, pas prescriptif |
| 6 — Timing en observation empirique datée | « The 2022 correction saw… », pas « The next correction will… » |

**Vigilance renforcée Cas B.** Anti-patterns composites :
❌ « When Net Liquidity drops below X, sell equities » · ❌ « Investors should monitor Real Interest Rates closely » · ❌ « A high Excess CAPE Yield signals attractive equity allocation » · ❌ « Use Mortgage Spread to time the housing cycle ».
✅ « Between 2020 and 2022, periods of rapid Net Liquidity expansion coincided with… » · ✅ « Historically, Real Interest Rates above 4% preceded equity drawdowns ≥20% in N of M cases since 1962 ».

---

## 17. Pas de JavaScript

Aucun `<script>`, `onclick`, event handler dans la page. Le graphique dynamique est rendu par le script global du site lisant le `<canvas>`. Aucun JS/CSS inline hors le `<style>@keyframes ds-spin>` du template.

---

## 18. Critère de publication

- **Cas A/A'** : la page apporte-t-elle quelque chose qu'un lien direct vers la source ne fournit pas ? (Macro Takeaway + Historical Regimes répondent oui.)
- **Cas B** : la section Construction explique-t-elle formule + composantes + réconciliation de fréquence de façon reproductible ? La séparation DONNÉE/ANALYSE vs l'étude homonyme est-elle tenue ?
- Le H1 respecte-t-il le cas (A : ticker ; A'/B : concept canonique ; jamais le code interne) ?
- Le Macro Takeaway lie au moins une autre série ou un pilier ?
- Au moins 4 régimes historiques avec chiffres datés ?
- Au moins 6 liens internes, tous justifiés ?
- Le bloc d'accès aux données correspond-il à la **source réelle** (pas de « FRED » sur une page Shiller/CoinGecko ; pas de spinner « Loading FRED data ») ?
- Le `dataset_id` est stable et matche le CSV en production ?

Si une seule condition échoue, retravailler.

---

## 19. Checklist pré-publication

**Cas & SEO**
- [ ] Cas identifié (A / A' / B) ; H1 conforme (ticker pour A, concept canonique pour A'/B)
- [ ] Code interne (NET_LIQ, SP500_M2…) absent du H1 / meta title / meta description
- [ ] Source ≠ stratégie SEO : un FRED non-googlé (café, fer) est bien traité en Cas A'
- [ ] [Cas B] mention « Eco3min composite/calculation » dans intro et/ou methodology
- [ ] Meta title commence par le ticker (A) ou le concept (A'/B), longueur acceptable
- [ ] Focus keyword = ticker (A) ou concept canonique en minuscules (A'/B)

**Source & accès données**
- [ ] Spinner = `Loading data…` (générique), pas `Loading FRED data…`
- [ ] Bloc d'accès données adapté : FRED fredgraph gardé si FRED-public ; supprimé/adapté sinon
- [ ] [Cas B] composantes FRED listées si 100% FRED-public ; sinon CSV Eco3min seul
- [ ] `data-series` = code source/interne ; canvas rendu OU omis selon support du script (§14.1)
- [ ] Sources finales = toutes les composantes (Cas B) + éditeur + agrégateur (≥2)

**Sections composites [Cas B]**
- [ ] Construction & Components présente (Formula + Components + Frequency reconciliation + Coverage)
- [ ] What This Index Captures présente (3-4 misinterprétations)
- [ ] Data Quality & Provider Notes présente (latence composante lente + propagation révisions)
- [ ] Concept canonique mentionné ≥ 5× au total

**Macro Takeaway**
- [ ] 2 paragraphes (mécanisme + illustration datée), ≥1 lien interne, AMF-compliant

**Historical Regimes**
- [ ] 4-6 régimes datés/nommés, chiffre + mécanisme par régime, enchaînement logique

**Métadonnées & code**
- [ ] Overview complet ; Variables = colonnes CSV exactes ; `[eco3min_latest]` pour la date
- [ ] Exemple Python (pandas) + R (readr) avec URL CSV Eco3min

**Maillage**
- [ ] ≥6 liens internes, cohérence linguistique stricte, Related Datasets ≠ Related Research, CTA Hub
- [ ] [si cluster] bloc « Deep analytical framework » vers le MAJEUR ; pas d'auto-référence

**AMF**
- [ ] Aucun « should », « advised », « buy when » ; descriptif ; pas de prédiction (vigilance renforcée Cas B)

**Citation**
- [ ] Année courante + URL canonique `/en/{slug}/`

---

## RAPPEL BLOQUANT — Zéro commentaire HTML dans le contenu publié

Les marqueurs de section en commentaire HTML utilisés dans les templates de ce skill
(`<!-- 1. INTRO -->`, `<!-- 5. MACRO TAKEAWAY -->`, etc.) sont des **repères d'assemblage**.
Ils ne survivent pas dans le HTML livré : on les retire avant de coller le contenu ou d'émettre
le bundle.

Motif : Autoptimize scanne `<script>` / `<style>` en regex **sans ignorer les commentaires HTML**.
Une balise littérale citée en prose dans un commentaire fait avaler du texte au minifieur JS,
provoque une fatale dans le callback de buffer et renvoie un **HTTP 500 avec le corps complet** —
page normale dans le navigateur, invisible pour Google. Incident du 27 août 2026, 8 pages
désindexées. `wpautop` mutile en plus ces commentaires (enveloppe en `<p>`, saut de ligne inséré
au milieu dès qu'un nom de balise bloc y figure).

Règle canonique, vérifications mécaniques et alternative (commentaire PHP dans le snippet) :
voir `eco3min-import-contenu-bilingue`, section « RÈGLE FIGÉE (août 2026) ».

Contrôle avant livraison :

```python
import re
assert not re.findall(r'<!--.*?-->', html, re.S), "commentaire HTML dans le contenu"
```

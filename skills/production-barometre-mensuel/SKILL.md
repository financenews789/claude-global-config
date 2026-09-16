---
name: production-barometre-mensuel
description: "Mise à jour mensuelle du baromètre macroéconomique Eco3min, FR (page 2093, /barometre-macroeconomique-feuille-de-route/) et EN (page 7920, /en/macroeconomic-barometer-markets-rates-macro-regime/) : prend le HTML du mois N lu sur WordPress, produit le HTML du mois N+1, toutes sections sans exception, prêt pour Gutenberg. Activer pour « mise à jour du baromètre », « produis le baromètre de {mois} », « le mois en ligne est X, produis Y », « matrice de disponibilité », « Key items to watch », « Factual highlights », « bloc navy », « synthèse », « Framework », « cartes macro », « flag divergence », « [eco3min_regime] », NFCI, Sahm, SOS, ICSA, FOMC, BCE, CPI, PCE, HICP, NFP, PIB, WALCL/TGA/RRP, DGS2, DGS10, T10Y2Y, HY OAS, VIX, T5YIFR, T10YIE, DFII10, Brent, WTI, or, CAC 40, Euro Stoxx 50, DAX, FTSE 100, S&P 500, Nasdaq, Dow Jones. SKILL.md = colonne vertébrale (règle absolue, §0 déclenchement et matrice de disponibilité, règles bloquantes par source et par section, §3 ordre d'exécution en 8 batchs, §4 checklist AMF, §5 checklist qualité, §6 typographie, §7 données non disponibles, §8 version FR) ; références dans references/ (à lire quand l'étape le dit) : 01 sources primaires par indicateur (URL FRED, requêtes, formats attendus, notes AMF, troncature BAMLH0A0HYM2, Yahoo interdit), 02 protocole section par section (SECTION 1 à 17 + sections inchangées) ; pas de scripts/. Doctrines : zéro chiffre issu de la mémoire de l'IA, chaque valeur vérifiée sur source primaire institutionnelle dans la session, sinon marqueur [DONNÉE NON PUBLIÉE] et jamais une estimation ; le HTML ne porte aucun <h1> ni titre de header, le H1 est le titre WordPress mis à jour via ewpa/update-post (apprentissage septembre 2026 : deux H1 sur la page) ; SAHMREALTIME et pas SAHMCURRENT ; révisions NFP des deux mois précédents obligatoires ; FOMC et BCE cités mot pour mot, aucune lecture directionnelle ; jamais « ~$108 » si la valeur exacte existe ; Yahoo Finance interdit en redistribution ; DAX et Euro Stoxx 50 en n.d. tant qu'aucune source primaire datée n'est accessible ; date de clôture réelle en vérifiant weekends ET jours fériés de place (31/08/2026, Londres fermé) ; synthèse et Framework rédigés après toutes les données ; disclaimer et CSS jamais modifiés ; 6 règles AMF Eco3min ; EN d'abord, FR ensuite en français natif. Hors périmètre : la plomberie WordPress (archivage, duplication, Polylang, RankMath, patches update-content) vit dans le CLAUDE.md du projet « Eco3min baromètre update » ; les routes d'accès aux sources (curl, WebFetch, Browser pane, calendriers de place) dans sourcing-donnees-eco3min annexe B ; la carte du bulletin dans production-bulletin-mensuel. Combiner avec production-bulletin-mensuel, regime-classifier-eco3min, editeur-eco3min, sourcing-donnees-eco3min."
---

# Skill — Mise à jour mensuelle du baromètre Eco3min

> **Règle absolue, non négociable.**  
> Aucun chiffre n'est écrit sans avoir été vérifié par web_search ou web_fetch sur une source
> primaire institutionnelle dans cette conversation. Ni la mémoire de l'IA ni des valeurs
> approximatives ne sont acceptables. Si une donnée n'est pas encore publiée → marqueur
> `[DONNÉE NON PUBLIÉE — à compléter après publication du XX/XX]`, jamais une estimation.

---

COMMENT LIRE CE SKILL (découpage du 16/09/2026)

Ce fichier est la colonne vertébrale : la règle absolue, le déclenchement, chaque règle BLOQUANTE par source et par section, l'ordre d'exécution, les checklists AMF et qualité, la typographie, les données non disponibles et la version FR. Le texte complet du protocole de recherche (§1) et du protocole section par section (§2) a été déplacé VERBATIM dans `references/` et fait foi au même titre que ce fichier. Chaque étape ci-dessous nomme le fichier à lire ; le lire est obligatoire au moment indiqué, pas facultatif. Pas de `scripts/` : aucun code n'est recopié de cycle en cycle. La plomberie WordPress (pages 7920 / 2093, archivage, Polylang, RankMath, patches `update-content`) vit dans le CLAUDE.md du projet « Eco3min baromètre update », pas ici.

| Fichier | Contenu | À lire |
|---|---|---|
| `references/01-sources-primaires.md` | §1.1 à §1.11 : pour chaque indicateur, URL FRED ou requête web_search, source primaire, format attendu, ce qu'il faut collecter, notes AMF, troncature BAMLH0A0HYM2, note Yahoo Finance, DAX / Euro Stoxx n.d. | avant de lancer les batchs A à H du §3, puis à chaque batch |
| `references/02-protocole-sections.md` | §2 : SECTION 1 à 17 + SECTIONS INCHANGÉES — ce qui change, ce qui ne change pas, formules de barres, templates, contrôles AMF par paragraphe | avant de produire chaque section, dans l'ordre du §3 étape 5 |

---

## 0. Déclenchement et pré-requis

Lire `~/eco3min/eco3min-knowledge/``chronologie/events.csv` sur le mois écoulé avant les batchs A à H : c'est la liste des événements que le baromètre doit au minimum situer, dans le vocabulaire de régime déjà posé. Les événements du mois qui manquent y entrent (`knowledge.add_event`) en fin de production.

### 0.1 Ce que Paul fournit
- Le HTML complet du baromètre du mois N, lu sur WordPress via `eco3min/get-content` (pages 7920 EN / 2093 FR) — pas les exemples locaux du projet, qui sont un instantané figé
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

## 1. Protocole de recherche — sources primaires par section (lire `references/01-sources-primaires.md` avant de lancer les batchs A à H)

Bloquant :
- Chaque valeur vient d'une source primaire institutionnelle (FRED, Federal Reserve Board, ECB, BLS, BEA, Eurostat, Dallas Fed, Chicago Fed, Richmond Fed, ICE, NYMEX, LBMA) récupérée dans la session. La référence donne, indicateur par indicateur, l'URL `fredgraph.csv?id=[CODE]&vintage_date=[AAAA-MM-JJ]` ou la requête web_search, le format attendu et ce qu'il faut collecter : s'y tenir.
- Sahm : « FRED series SAHMREALTIME (temps réel, pas SAHMCURRENT) », sourcé comme tel dans le texte. NFCI : sous-indices NFCIRISK, NFCICREDIT, NFCILEVERAGE si disponibles. SOS : « last updated [date] ».
- FOMC et BCE : « citer uniquement ce qui figure dans le communiqué officiel. Aucune interprétation directionnelle ("le Fed va baisser" = interdit). "Le communiqué décrit désormais l'inflation comme [citation exacte]" = correct. » Collecter taux (fourchette / trois taux BCE), vote (X-Y), dissidents nommés, formulation exacte sur l'inflation et les risques.
- PIB US : « préciser "advance estimate" / "second estimate" / "third estimate" ». PIB zone euro : taux q/q + qualification (preliminary/flash). CPI : date du communiqué citée obligatoirement.
- NFP : « révisions des 2 mois précédents (obligatoire — les révisions font partie du récit), taux de chômage ».
- Taux : DGS2, DGS10, T10Y2Y, MORTGAGE30US, BAMLH0A0HYM2, VIXCLS, T5YIFR, T10YIE, DFII10 — dernière valeur disponible au 1er du mois cible. « BAMLH0A0HYM2 : depuis avril 2026, FRED tronque à 3 ans glissants. Pour la valeur courante, la série reste utilisable. Pour la calibration percentile de l'overlay stress, voir thresholds_spec.json. »
- Actions : « Yahoo Finance est un agrégateur dont les CGU interdisent la redistribution commerciale » — sources officielles (Euronext, NYSE, CBOE) ou « données indicatives » en note de bas de tableau. Sept indices (CAC 40, Euro Stoxx 50, DAX, FTSE 100, S&P 500, Nasdaq Composite, Dow Jones), valeur exacte à 2 décimales + date de clôture. DAX et Euro Stoxx 50 : aucune source primaire datée accessible (cycles août et septembre 2026) → publier « n.d. », le signaler dans le rapport de cycle, ne jamais combler par une source secondaire.
- Matières premières : « Ne jamais écrire "~$108" si la valeur exacte est disponible — approximation tolérée uniquement si la source donne une fourchette. » Brent ICE Futures Europe, WTI NYMEX, or LBMA.
- Liquidité : « Net Liquidity = WALCL − WTREGEN − RRPONTSYD » ; variation mensuelle = valeur fin de mois N vs fin de mois N-1.
- Énergie / géopolitique : faits vérifiables seulement (prix, événement, date) ; agences (Reuters, AP, AFP) pour les faits, communiqués officiels et EIA en source primaire ; interprétation causale cadrée « selon [source] » ; « "Les prix pourraient monter" = prévision → INTERDIT ».
- Routes d'accès (curl, puis WebFetch, puis Browser pane) et calendriers de place : `sourcing-donnees-eco3min`, annexe B. Un 403 se teste avant d'être conclu.

---

## 2. Protocole section par section (lire `references/02-protocole-sections.md` avant de produire chaque section)

Appliquer dans cet ordre. Ne passer à la section suivante qu'une fois les données de la section
courante vérifiées et écrites.

Bloquant, par section (le détail, les formules et les templates sont dans la référence) :
- SECTION 1 — Header : le HTML ne porte **ni `<h1>` ni `baro-header__title`** ; le titre du mois est le titre WordPress de la page, mis à jour via `ewpa/update-post` `title` (septembre 2026 : deux H1). Seule `baro-header__date span` change ; countdown div et KPI strip inchangés. `assert '<h1' not in html`.
- SECTION 2 — Commentaire shortcode `[eco3min_regime]` : flag `headline_underlying_divergence` = Brent YoY au 1er du mois N+1 `(Brent actuel / Brent il y a 12 mois − 1) × 100` ; « Si YoY > +20% → flag ACTIF », « Si YoY ≤ +20% → flag INACTIF ». Ligne repo `github.com/eco3min/macro-regime-classifier` présente et exacte. Le shortcode affiche, le commentaire documente.
- SECTION 3 — Synthèse (bloc navy) : « Collecter d'abord TOUTES les données (sections 4 à 13) avant d'écrire ce bloc » ; ~3 paragraphes : fait dominant chiffré, contre-signal chiffré, phrase de cadrage. Interdits : « l'économie va [mieux/pire] » sans chiffre, « les marchés anticipent » sans source, « il faut surveiller » avec implication d'action, toute recommandation d'allocation. Les italiques sont une citation sourcée ou un fait, jamais une opinion.
- SECTION 4 — Signaux de cycle : valeur, description datée, barre `(valeur / seuil) × 100%` pour Sahm et SOS, `(valeur + 3) / 9 × 100%` pour NFCI (échelle −3 à +6). Sahm sourcé `SAHMREALTIME`, seuil 0.50 rappelé. SOS : « toujours la valeur + le seuil », jamais « bien en dessous » seul. Note AMF de bas de section inchangée.
- SECTIONS 5, 6, 8, 11, 12, 14 — Descriptions de graphiques : ne changer que les valeurs ponctuelles datées dans `.baro-chart-desc` ; titre, codes FRED, liens internes et description du mécanisme inchangés. HY OAS : « historiquement serré » conservé seulement si la valeur reste basse face à la moyenne historique ~5.5% (correct autour de 3%). T5YIFR : formulation « the Fed's preferred gauge of long-run expectations anchoring » stable.
- SECTION 7 — Faits marquants : label « Factual highlights — [Mois écoulé] [Année] » ; 4–5 blocs avec `<strong>` ; « Citer uniquement des chiffres présents dans ce communiqué » ; « Source: [Institution], [type de document], [date]. » en fin de paragraphe. ✗ prévision, ✗ « a envoyé un signal », ✗ « reste préoccupante », ✗ « la croissance est solide », ✗ « le marché craint ».
- SECTION 9 — Tableau indices : clôture à 2 décimales, date de clôture réelle (weekend OU jour férié de place — 31/08/2026, Londres fermé, FTSE 100 et LBMA datés du 28), flèche vs dernier jour du mois N-1 : « ↑ = hausse, ↓ = baisse, → = variation < 0.5% ». Note de bas de tableau conservée.
- SECTION 10 — Tableau taux / matières premières / volatilité : « la valeur dans ce tableau doit correspondre au signe mentionné dans la description du graphique yield curve » (T10Y2Y positif ≠ « courbe inversée »). Note de bas de tableau réévaluée si le contexte énergétique a changé.
- SECTION 13 — Cartes macro US et zone euro : liste de champs de la référence ; « aucune approximation tolérée » ; donnée non publiée = valeur du mois précédent avec « (révision attendue le [date]) ».
- SECTION 15 — Framework (bloc ambré) : rédigé après toutes les données ; « Chaque paragraphe est ancré sur au moins un chiffre vérifié » ; interdits : « les marchés devraient », « il faut surveiller X car Y pourrait », toute association régime → allocation « même présentée comme "observation historique" sans ancrage empirique » ; les `<strong>` soulignent des faits.
- SECTION 16 — Key items : label « Key items — [Mois N+1]–[Mois N+2] [Année] calendar » ; 5–6 items datés depuis les calendriers officiels (FOMC, BCE, BLS, BEA, Eurostat). « "Markets will closely monitor X" = OK », « "You should watch X" = INTERDIT », « X could push inflation higher » cadré « selon [institution] » ou supprimé.
- SECTION 17 — Liquidité nette : WALCL, TGA (WTREGEN), RRP (RRPONTSYD), net = WALCL − TGA − RRP, variation mensuelle, « As of [date] » ; RRP proche de zéro → le dire explicitement.
- SECTIONS INCHANGÉES : liens internes vérifiés (web_fetch) ; promesse non modifiée sauf si la liste des sources change ; « Baro-disclaimer : NE PAS MODIFIER. Texte juridique figé. » ; « CSS + fonts import : NE PAS MODIFIER. »

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
- [ ] Aucun `<h1` dans le HTML livré (`assert '<h1' not in html`) — le H1 est le titre WordPress de la page, mis à jour via `ewpa/update-post`, jamais dans le bloc HTML

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

La version FR du baromètre existe (page 2093, `/barometre-macroeconomique-feuille-de-route/`) et se produit à chaque
cycle, **EN d'abord, FR ensuite** : appliquer
le même protocole en réécrivant les sections éditoriales en français natif (pas une traduction mot à mot). Les données chiffrées et sources sont
identiques. Points de vigilance :
- "advance estimate" → "estimation préliminaire" ou "estimation avancée"
- "year-over-year" → "en glissement annuel" ou "sur un an"
- Flèches du tableau actions : inchangées (symboles universels)
- Label "RÉGIME MACRO" dans le shortcode card : auto-géré par Polylang

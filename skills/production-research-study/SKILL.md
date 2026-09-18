---
name: production-research-study
description: "Doctrine éditoriale et pipeline complet de production d'une étude de recherche Eco3min (research study, étude approfondie, killer study, série GENERIQUE R1…R12, codes C1…C6, études #20 #22), de l'angle au jeu de 14-18 livrables prêts pour WordPress. Déclencheurs : « produce study X », « produis l'étude », « nouvelle étude », « lance R13 », « backlink hook », « pre-review adverse », « verrous », « audit extractif », « compute_stats », « fact_check_audit », « provenance.md », « chart interactif », « package social », « snippet autonome », « structure 28 blocs », « registre des erreurs ». Structure : SKILL.md = colonne vertébrale (workflow Step 0→10 verbatim, règles bloquantes par step, checklists §16 et §21 verbatim, rappel zéro commentaire HTML) ; références dans references/ (01 hook et pre-review, 02 Beats et anti-editorializing, 03 exactitude des données, 04 charts statique et interactif, 05 audit extractif et patterns à haut risque, 06 livrables et CSV, 07 verrous A→G, 08 structure de page, 09 déploiement WordPress, 10 social et pre-flight r/economics, 11 acquisition des données, 12 registre des motifs d'erreur, 13 rafraîchissement d'une étude publiée : audit d'entrée, gel / extension, byline datée), à lire quand le step le dit ; scripts/live_module.js et .css = module interactif de référence (data-extra, data-markers, data-lang) ; gardes réutilisables dans scripts/study_locks.py (Verrou D hedges, Verrou E comptages, Verrou G cadratins, tics IA et verbes prescriptifs, Verrou H anti-répétition de série, zéro commentaire HTML, tolérances §12.5, collecteur de claims et rapport §12.6). Doctrines qui définissent la skill : le Backlink Hook ≤25 mots s'écrit avant tout le reste et sans hook validé la production ne commence pas ; quatre reviewers hostiles avant de fetch la donnée, Thesis Pivot quand la donnée contredit le brief ; Beat 1 loyal, Beat 2 chiffré, Beat 3 obligatoire au plus deux sections après ; le CSV est la source unique de vérité, calculer avant d'écrire, jamais de mémoire ; l'audit est extractif et CSV-led (le CSV énumère les claims, pas Claude) et recalcule depuis le CSV brut uniquement (Verrou A, étude #20 : une erreur, quatorze copies) ; zéro fail toléré, tout échec en Step 6 ou 6.5a-g = HALT ; approximately/roughly interdits sans hedge_justifications.json ; contrôle de licence FRED (trois statuts) au Step 0, pas au Step 10 (R5 tuée au Step 0, 10/09/2026) ; zéro cadratin, zéro tic IA, zéro verbe prescriptif dans tout livrable (Verrou G, R1 08/09/2026 : 43 cadratins malgré 163 claims à 100 %) ; le squelette des 28 blocs est fixe mais la phrase tourne d'une étude à l'autre (Verrou H, 17/09/2026 : phrase-pivot en antithèse et « Robustness, disclosed » verbatim sur R3→R9, gabarit de Beat 1 deux fois de suite) ; chart interactif SVG JS natif sans bibliothèque, repli picture testé réseau coupé ; le corps HTML n'a ni style ni script ni commentaire HTML (incident 27/08/2026, 8 pages désindexées) ; le nom de base d'un asset n'est jamais le slug de la page ; une règle de doctrine non chargée n'existe pas : charger les skills compagnes avant le Step 1. Hors périmètre : identité éditoriale et six règles AMF (editeur-eco3min), data viz et assertions matplotlib (visuels-eco3min), légalité et endpoints des sources (sourcing-donnees-eco3min, autorité unique annexe B), pages dataset brutes (production-dataset), Q&A (production-q-and-a), bilinguisation et import du bundle (eco3min-import-contenu-bilingue), chart Reddit DIB autonome (production-chart-of-the-week), cartes hub (hub-card-etude). Combiner avec editeur-eco3min, visuels-eco3min, brand-kit-eco3min, sourcing-donnees-eco3min, eco3min-import-contenu-bilingue, hub-card-etude, formats-eco3min, archi-eco3min."
---

# Principes éditoriaux — Eco3min Research Studies

> Ce skill code la **couche éditoriale ET le pipeline de production** des études killer Eco3min. La couche éditoriale (§1-16) est transférable au-delà des research studies : tout article pilier majeur, dataset à fort potentiel ou Q&A à enjeu viral peut en bénéficier. Le pipeline (§17-24) est spécifique aux études.
>
> Ce qui reste dans les Custom Instructions du projet : le fichier de mapping et son registre de statuts, les codes d'étude, les chemins locaux. Rien d'autre.
>
> Voir aussi `editeur-eco3min` (identité + AMF), `visuels-eco3min` (data viz), `production-dataset` (pages dataset brutes), `production-q-and-a` (Q&A).

---

## 1. Double objectif éditorial

Tout contenu visant le rang research-study doit réussir **simultanément** sur deux fronts :

1. **Viralité Reddit** — High-effort OC avec un "aha moment" visible en 3 secondes
2. **Backlinks journalistiques** — Insight citation-ready, zéro friction cognitive pour un journaliste sur deadline

Ces objectifs ne sont **pas en conflit**. Les mêmes données servent les deux si la structure est correcte. Reddit récompense l'effort visible et le pattern frappant. Les journalistes récompensent une phrase qu'ils peuvent copier-coller en attribution.

---

COMMENT LIRE CE SKILL (découpage du 15/09/2026)

Ce fichier est la colonne vertébrale : le workflow Step 0 → Step 10 verbatim, chaque règle BLOQUANTE par step, les checklists §16 et §21 et le rappel zéro commentaire HTML. Le texte complet de chaque section (rationale, exemples, tableaux, templates, post-mortems) a été déplacé VERBATIM dans `references/` et fait foi au même titre que ce fichier. Chaque step ci-dessous nomme le fichier à lire ; le lire est obligatoire au moment indiqué, pas facultatif. Les numéros de section d'origine (§2 … §24) sont conservés dans les références : les renvois « §N » de ce fichier, du CLAUDE.md du projet GENERIQUE et de son memoire.md y pointent. `scripts/` porte les gardes que chaque `audit_extract.py` réécrivait avec dérive : on les importe, on ne les recopie plus.

| Fichier | Contenu | À lire |
|---|---|---|
| `references/01-hook-prereview-pivot.md` | §2 Backlink Hook (critères, exemples ✅❌, règle d'arrêt), §3 Pre-Review adverse (4 reviewers, format de sortie, Thesis Pivot Doctrine) | avant d'écrire le hook (Step 0), puis avant de fetch la donnée (Step 1.5) |
| `references/02-beats-anti-editorializing-scan.md` | §4 Beats 1→2→3, §5 termes proscrits, Yield Curve Lesson, robustesse, §6 Citation Readiness Test, §11 loaded-terms scan | avant d'écrire le HTML (Step 5), puis au Step 6.5a |
| `references/03-data-accuracy-forward-surveillance.md` | §7 CSV vérité, deux dates, direction vs niveau, colonnes forward, §8 forward distributions, §9 Key Levels to Watch | avant de construire le CSV (Step 3) et avant d'écrire les sections forward et surveillance (Step 5) |
| `references/04-charts-statique-interactif.md` | §10 choix du type, justification d'échelle, chart DIB, discipline de génération, chart interactif (contrats technique, audit, AMF, dégradation) | avant les charts (Step 8) et le module interactif (Step 8b) |
| `references/05-audit-extractif-coherence-patterns.md` | §12 audit extractif CSV-led (énumération, format d'assertion, tolérances, reporting), §13 cohérence multi-livrables, §14 cinq patterns à haut risque | avant d'écrire le verifier (Step 6) |
| `references/06-livrables-csv-workflow.md` | §17.1 tableau des 18 livrables, §17.2 le CSV pierre angulaire, §17.4 mode opératoire | au Step 0.5 (inventaire) et avant de construire le CSV (Step 3) |
| `references/07-verrous-a-g.md` | §18 dix règles d'écriture, périmètre imprimé de compute_stats.py, les huit verrous dont H (anti-répétition de série, figures de phrase-pivot, menu des labels de robustesse), Steps 6.5a et 6.5b, sections oubliées, limites | avant compute_stats.py (Step 4), avant d'écrire (Step 5), puis au Step 6.5a-h |
| `references/08-structure-page-28-blocs.md` | §19 les 28 blocs dans l'ordre + exigences à l'échelle de la page | avant d'écrire le HTML (Step 5) |
| `references/09-deploiement-wordpress.md` | §20 namespace CSS, snippet autonome, règles WordPress dures, discipline de slug et origine du `-2`, FAQ, chemins | au Step 0.5 (slug) et au Step 10 (assemblage) |
| `references/10-social-preflight-upload.md` | §15 pre-flight r/economics, §22 package social et guide d'upload des images | avant le package social (Step 7) et le guide d'upload (Step 9) |
| `references/11-acquisition-donnees.md` | §23 playbook par source, gate de licence FRED à trois statuts, règle d'arrêt | au Step 0 (licence) et avant de récupérer la donnée (Step 2) |
| `references/12-registre-erreurs.md` | §24 post-mortems #22, #20, #6, R1 et leçon transversale | dès qu'une erreur est découverte après livraison, et avant d'alléger un verrou |
| `references/13-rafraichissement-etude-publiee.md` | §25 rafraîchir une étude déjà en ligne : audit d'entrée des études d'avant R1 (garde FR, contentUrl, citation, h1, spécificité), ce qui se gèle et ce qui s'étend, section « en temps réel », byline datée, ordre des réécritures page / snippet / RankMath / claims | dès qu'un événement daté teste une étude publiée, avant de toucher au texte |
| `scripts/live_module.js` + `scripts/live_module.css` | Module interactif de référence (18/09/2026, étude #6) : le module générique du `snippet_model.php` étendu de `data-extra` (colonnes lues au survol, dont un régime traduit), `data-markers` (événements datés cliquables, épinglage), `data-lang` (libellés et formats FR/EN), fenêtres en années, bandes d'épisodes | au Step 8b, copié dans le snippet sous la garde bilingue ; harnais de test dans `references/04` §10.7 |
| `scripts/study_locks.py` | Verrou D (hedges), Verrou E (comptages), Verrou G (cadratins, tics IA, prescriptif, action), Verrou H (anti-répétition de série : H2 de Beat, gabarits, label de robustesse, figure de la phrase-pivot, contre les études livrées dans `out/`), zéro commentaire HTML, tolérances §12.5, collecteur de claims + rapport §12.6 | importé par `audit_extract.py` de chaque étude (Steps 6 et 6.5d-h) |
| `scripts/css_specificity.py` | Spécificité du CSS scopé : `p_classes()`, `boost_paragraph_rules()`, `lint_paragraph_rules()` — tout sélecteur à sujet `<p>` atteint (0,2,0), sinon `.entry-content p` du Customizer gagne | importé par `build_snippet.py` (Step 10), après le re-namespace |

Utilisation du script depuis un dossier d'étude :

    sys.path.insert(0, os.path.expanduser('~/.claude/skills/production-research-study/scripts'))
    from study_locks import (Claims, TOLERANCE, close, scan_hedges, scan_counting_claims,
                             editorial_locks, assert_no_html_comments)

Les dossiers `out/R1` à `out/R4` du projet GENERIQUE sont les implémentations de référence (build_csv.py, compute_stats.py, audit_extract.py, make_charts.py, build_snippet.py, build_bundle.py). Leurs `audit_extract.py` sont livrés et ne se réécrivent pas ; les études suivantes importent `study_locks`.

### 17.2 Base de connaissance (eco3min-knowledge)

Avant le Step 0 : `grep -i` du sujet dans `~/eco3min/eco3min-knowledge/``sujets/backlog.csv` (déjà rejeté ? pourquoi ?) et lecture de `chronologie/events.csv` sur la fenêtre de l'étude. Les lignes `origine=veille, statut=idee` du backlog (déposées le lundi par la tâche planifiée `veille-eco3min`) sont des pistes en plus — une aide qui ne remplace pas la recherche d'angle habituelle et n'est pas nécessairement la meilleure ; le sujet retenu passe en `en_prod`, une piste réellement examinée puis écartée en `rejete` avec sa raison, le reste demeure en `idee`. Au Step 6 (audit extractif) : chaque chiffre validé devient une ligne de `faits/claims.jsonl` via `knowledge.add_claim` (added_by = `fact_check_audit`) ; si le même claim y figure déjà avec une autre valeur, c'est une incohérence inter-pages à traiter avant publication. À la livraison : `add_topic(statut=publie, page_id=…)`. Schémas et énumérations dans le `CLAUDE.md` de la base.

### 17.3 Workflow Step 0 → Step 10

```
Step 0     → BACKLINK HOOK (§2)
Step 0.5   → PRE-FLIGHT DU SLUG : choisir le slug, vérifier sa disponibilité
             dans WP (le motif de collision « -2 » a frappé au moins 3 études).
             Vérifier le dossier du mois d'upload [YYYY]/[MM]. Vérifier chaque
             slug de lien interne prévu contre le snapshot du site.
             Verrouiller l'INVENTAIRE DES CHARTS et leurs noms de fichiers.
Step 1     → Lire le brief dans le fichier de mapping (statut + cannibalisation)
Step 1.5   → PRE-REVIEW ADVERSE (§3) — c'est un livrable
Step 2     → Récupérer la donnée, y compris les séries défensives issues du 1.5 (§23)
Step 3     → Construire le CSV, colonnes défensives comprises
Step 4     → compute_stats.py — TOUTES les statistiques qui apparaîtront où que
             ce soit, organisées par section (périmètre imposé en §18.2), bloc
             FILTERS canonique en tête, imprimées sur stdout.
             Sauver intermediate_stats.json POUR LA PRODUCTION UNIQUEMENT —
             jamais comme source d'audit (Verrou A).
Step 5     → Écrire le HTML : défenses intégrées, valeurs copiées DEPUIS stdout,
             formulation concept-cohérente (Verrou B), chaque filtre temporel
             formellement défini (Verrou F)
Step 6     → AUDIT EXTRACTIF (§12) : EXTRACT → VERIFY (recalcul depuis le CSV
             brut uniquement) → GATE (couverture 100 %)
Step 6.5a  → Scan des termes chargés + vérification des défenses + citabilité
Step 6.5b  → Tripwire de direction narrative (claims datés contre CSV)
Step 6.5c  → Audit d'appariement concept-nombre (Verrou B)
Step 6.5d  → Scan automatique des hedges + hedge_justifications.json (Verrou D)
Step 6.5e  → Contrôle d'assertion des claims de comptage (Verrou E)
Step 6.5f  → Contrôle de formalité des filtres (Verrou F)
Step 6.5h  → Anti-répétition de série (Verrou H) : H2 de Beat, gabarit,
             label de robustesse et figure de phrase-pivot contre out/*
Step 6.5g  → Verrous éditoriaux (Verrou G) : zéro cadratin, zéro tic IA,
             zéro verbe prescriptif, zéro langage d'action ou de timing
Step 7     → Snippets sociaux (§15 pre-flight r/economics)
Step 8     → Specs des charts (justification d'échelle) + vérification visuelle
Step 8b    → CHART INTERACTIF (§10.6) : module SVG en JS natif alimenté par le
             CSV publié, markup data-* dans le corps, JS dans le snippet, repli
             <picture> testé réseau coupé, clavier et 380 px vérifiés
Step 9     → Guide d'upload des images
Step 10    → Assembler et livrer le jeu complet, résumé d'audit inclus
```

**Tout échec en 6 ou 6.5a-h → HALT. Pas de livraison.**


RÈGLES BLOQUANTES PAR STEP

Avant le Step 1 — charger les skills compagnes. « Une règle de doctrine non chargée n'existe pas. Le premier verrou du pipeline n'est pas le Step 6, c'est le chargement des skills avant le Step 1 » (§24, étude R1 : 2 skills chargées sur 9, 4 défauts non dérivables d'un CSV). Combiner avec editeur-eco3min, visuels-eco3min, brand-kit-eco3min, sourcing-donnees-eco3min, eco3min-import-contenu-bilingue, hub-card-etude, formats-eco3min, archi-eco3min. Le CLAUDE.md du projet GENERIQUE impose le bilingue et gagne sur le format de livraison.


Step 0 — BACKLINK HOOK et gate de licence (lire `references/01-hook-prereview-pivot.md` avant d'écrire le hook ; lire `references/11-acquisition-donnees.md` avant de mesurer la profondeur d'une série)

Bloquant :
- Hook ≤ 25 mots, contient une statistique frappante, compréhensible par quelqu'un qui n'a jamais entendu parler du sujet, copy-pasteable comme « According to Eco3min, [phrase]. »
- « Si tu ne peux pas produire un hook fort, l'angle de l'étude n'est pas prêt. » Ne jamais commencer la production sans hook validé. Le hook devient le premier bullet de l'Executive Summary, le texte du TL;DR, le titre Reddit, la base du social snippet package.
- Le contrôle de licence est un GATE du Step 0, pas une vérification de fin de production : avant de mesurer la profondeur d'une série, sur chaque série destinée à une colonne publiée et sur chaque intrant d'un composite (une série dérivée hérite du niveau le plus dur). FRED distingue trois statuts : public domain: citation requested → CSV CC BY 4.0 possible ; copyrighted: citation required → publiable avec attribution mais jamais en CC BY 4.0 ; copyrighted: pre-approval required → rien sans accord écrit du détenteur. Autorité unique : `sourcing-donnees-eco3min`, section « Cas FRED » et annexe B (endpoints) ; ne pas les redocumenter ici.
- yfinance et agrégateurs scrapés interdits comme source d'un CSV publié ; le footer nomme la vraie source. Source bloquée → s'arrêter et demander les fichiers, jamais substituer la mémoire du modèle.
- **Verrou L, colonnes publiées (ajouté le 16/09/2026).** Un fichier d'étude ne contient JAMAIS un niveau brut d'une série « pre-approval required » (`SP500`, `NASDAQCOM`, `DJIA`, toute série `BAML*`, `CSUSHPINSA` et les indices Case-Shiller) : ni comme colonne de comparaison, ni comme « S&P 500 close (nearest day) » ajouté pour le contexte. Le comparateur actions est un rendement dérivé d'une source libre (Shiller, bibliothèque Kenneth French) ou un prix d'ETF sourcé chez l'émetteur. Un fichier qui porte une colonne brute d'une série « citation required » (`RRPONTSYD`, `T10Y2Y`, `T5YIE`, `T10YIE`, `USREC`, `M2V`, `VIXCLS`, `BAA`, `NFCI`, `CFNAI`) n'est PAS annoncé CC BY 4.0 : la page, la barre de téléchargement, la FAQ, le package social et le JSON-LD `license` portent la licence réelle (URL FRED du niveau, `copyrightHolder` = émetteur), ou la colonne est recalculée depuis des intrants domaine public (`DGS10 − DGS2`, `DGS5 − DFII5`, `GDP / M2SL`, chronologie NBER) et la méthodologie le dit. Constaté le 16/09/2026 : quatre majeurs (net liquidity, ON RRP, EN et FR) redistribuaient `SP500` en niveau et `RRPONTSYD` sous CC BY 4.0 alors que les pages dataset appariées avaient déjà la notice ; huit autres fichiers d'études du hub macro US portent un niveau `sp500` ou `nasdaq`.


Step 0.5 — PRE-FLIGHT DU SLUG (lire `references/09-deploiement-wordpress.md` §20.4 et `references/06-livrables-csv-workflow.md` §17.1)

Bloquant :
- Slug vérifié disponible dans WP avant production ; chaque slug de lien interne prévu vérifié contre le snapshot ; dossier d'upload [YYYY]/[MM] du mois courant vérifié ; inventaire des charts et noms de fichiers verrouillés.
- Une pièce jointe occupe l'espace de noms des slugs de page : le nom de base des assets n'est jamais le slug de la page, et le bundle s'importe avant l'upload des données (autorité : `eco3min-import-contenu-bilingue`, section « Le slug de page ne doit JAMAIS être le nom de base d'un asset »). Si WP attribue quand même un `-2`, le propager à la fonction de garde, au `@id` / `mainEntityOfPage` / `url` du JSON-LD, à l'`og:url`, à l'encart de citation, au package social.


Step 1.5 — PRE-REVIEW ADVERSE (lire `references/01-hook-prereview-pivot.md` avant de fetch la donnée)

Bloquant :
- Après lecture du brief, avant de fetch les données : quatre reviewers hostiles (r/economics Moderator Rule IV, FT Data Journalist méthodologie, Quant rigueur statistique, Macro Economist steelman), sortie au format §3.5 avec CHANGEMENTS DE DESIGN. C'est un livrable (n°16), pas une note interne ; les séries défensives qu'il exige entrent dans le CSV.
- Chaque attaque pré-semée du brief se CALCULE avant d'être défendue, et on se demande si elle n'est pas la thèse (R6, 16/09/2026 : « corréler les variations, pas les niveaux » était listée comme défense n° 1 ; c'était l'étude entière). Toute étude qui publie une corrélation de niveaux publie d'abord la corrélation des variations, cf. `references/01-hook-prereview-pivot.md` §3.7.
- Thesis Pivot Doctrine : quand la donnée principale contredit le cadrage du brief, vérifier la contradiction contre au moins deux références indépendantes, identifier le noyau défendable, signaler le pivot à Paul avec les preuves, produire sur la thèse pivotée, cadrer l'inversion de façon transparente sur la page, mettre à jour l'entrée du fichier de mapping et son Thesis Pivot Registry.
- Mode opératoire (§17.4) : une étude à la fois, Step 0 → Step 10 dans une seule conversation, sans s'arrêter pour approbation, puis livrer le jeu complet. Sortie canonique unique : un slug, un H1, un jeu de metas. Pas de variantes.


Steps 2 et 3 — DONNÉE ET CSV (lire `references/11-acquisition-donnees.md` avant de récupérer, `references/06-livrables-csv-workflow.md` §17.2 et `references/03-data-accuracy-forward-surveillance.md` §7 avant de construire le CSV)

Bloquant :
- Le CSV est produit en premier, source unique de vérité, CC BY 4.0. Si on réutilise la donnée d'une autre page Eco3min : récupérer la série sous-jacente et recalculer, jamais recopier une approximation.
- Au moins une variable qui n'existe dans aucune source publique (composite, classification de régime, série décalée, métrique inter-datasets).
- Colonnes de forward return obligatoires, benchmark substitué selon le mapping : `fwd_6m_pct`, `fwd_12m_pct`, plus `fwd_12m_mdd` là où le drawdown a un sens, horizons 5 ans / 10 ans en annuel ; jours de bourse pour les séries quotidiennes, périodes calendaires sinon, préciser lequel ; NaN quand la fenêtre n'est pas écoulée.
- Dates cohérentes (YYYY-MM-DD, YYYY-MM ou `year`), aucune valeur manquante dans les colonnes calculées, chaque colonne documentée (nom, type, unité, source, calcul).
- `provenance.md` (livrable 17b) : par série, la source réelle, le code, l'URL de fetch, la licence et ses marqueurs, la méthode, la date ; cross-check contre l'émetteur, pas contre le canal de redistribution ; liste des séries de contrôle jamais republiées.


Step 4 — compute_stats.py (lire `references/07-verrous-a-g.md` §18.2 avant d'écrire le script)

Bloquant :
- Périmètre imprimé obligatoire : `[LATEST OBSERVATION]` · `[EXECUTIVE SUMMARY VALUES]` · `[STATS PANEL]` · `[FORWARD RETURNS TABLE]` par régime plus chaque union de régimes et chaque sous-période mentionnée où que ce soit en prose, variantes ex-COVID comprises · `[CHART ANNOTATIONS]` · `[TURNING POINTS]` · `[INTERP-GRID VALUES]` · `[SURVEILLANCE BLOCK]` · `[COUNTING STATISTICS]` · `[METHODOLOGY]` · bloc `FILTERS` canonique en tête. « Une section absente de stdout → le Step 6 ÉCHOUE. »
- Toute union de régimes et toute sous-période mentionnée en prose est calculée ici, jamais de tête (Verrou C). Le filtre EXACT est imprimé à côté de chaque comptage (§14.3).
- `intermediate_stats.json` sert à la production uniquement, jamais comme source d'audit (Verrou A).


Step 5 — ÉCRIRE LE HTML (lire `references/07-verrous-a-g.md` §18.1, `references/02-beats-anti-editorializing-scan.md`, `references/03-data-accuracy-forward-surveillance.md` §8-§9 et `references/08-structure-page-28-blocs.md` avant d'écrire)

Bloquant :
- Les dix règles d'écriture (§18.1) : le CSV est la source unique de vérité (HTML ≠ CSV → c'est le HTML qui a tort) ; calculer avant d'écrire, toute valeur imprimée sur stdout puis copiée, jamais de mémoire ni à l'œil sur un chart ; « approximately / roughly / about / around / ~ » interdit pour toute valeur calculable, autorisé uniquement avec entrée dans `hedge_justifications.json` (motifs `external_unverifiable`, `verify_pending`, `narrative_rounding`) ; claims « X of top N » par classement Python explicite ; claims de comptage par assertion sur filtre explicite ; filtres temporels définis dans le dict `FILTERS` de compute_stats.py ET dans le bloc « Filter Definitions » du HTML ; formulation concept-cohérente (longueur de série ≠ délai d'avance) ; points de retournement par lookups ligne à ligne, piège des deux dates ; direction de régime : variation de niveau ≠ direction du YoY ; cohérence inter-livrables.
- Beat 1 énoncé fairly, Beat 2 = contradiction empirique chiffrée, Beat 3 OBLIGATOIRE et dans les 2 sections suivant Beat 2, avec au moins un élément de §4.2. Encart de contexte obligatoire dans la première séquence analytique (ce que le dataset ne mesure pas, contre-fait concret).
- Termes proscrits (§5.1) : destruction, tax (inflation), manipulation, failed, should / must, will, obviously / clearly, undeniably / proves that. H1 sans jugement normatif ; 3 premiers paragraphes 100 % factuels. Critique par accumulation de faits, pas par adjectifs.
- Robustesse comme blindage (§5.5) : quand un résultat dépend d'un choix méthodologique, divulguer l'alternative, y compris quand le signe s'inverse, en trois endroits : une phrase dans la TL;DR, le développement dans le Beat 3, le détail dans la méthodologie.
- Anti-répétition de série (Verrou H, `references/07-verrous-a-g.md` §18.3) : avant d'écrire les titres de Beat, la phrase-pivot et le label de robustesse, lire ceux de l'étude livrée juste avant (`out/*/README_DELIVERABLE.md`, H2 de `page_body.html`). Pas le même gabarit de titre de Beat deux études de suite (« What the [X] story says », « Where the reading … », « What this does not settle », « Pick any … »), pas la même figure de phrase-pivot (antithèse, temporel, chiffre, question, définition), pas le même label de robustesse ; la figure se déclare dans le README (« **Phrase-pivot**, native par langue, figure : antithèse »). Le squelette des 28 blocs, lui, ne varie pas : c'est la phrase qui tourne, pas la structure. Constaté sur R3→R9 (17/09/2026) : antithèse sur chaque pivot, « Robustness, disclosed: » verbatim sept fois.
- Chiffres hors CSV marqués `<!-- SOURCE: [référence] -->` ou `<!-- VERIFY: [description] -->` pendant l'assemblage ; ces repères sont retirés avant livraison (cf. RAPPEL BLOQUANT).
- Forward distribution : tableau régime, n, médiane 6m, médiane 12m, IQR (P25–P75), % positifs 12m, MDD médian ; note fenêtres glissantes ; caveat si n < 15 ; disclaimer « Past distributions are not predictive of future outcomes. Regime-conditional statistics describe historical patterns, not expected returns. »
- Key Levels to Watch : trois éléments exactement (invalidation threshold, confirmation signal, calendar catalyst), motif « Si [condition observable], alors [le régime change vers Z], ce qui historiquement a été associé avec [résultat factuel] », JAMAIS buy / sell / should, marqueur `<!-- UPDATEABLE -->`.
- Structure : 28 blocs dans l'ordre de §19 ; H1 dans le champ titre de WP ; ancres du sommaire = id de section ; au moins 3 encarts takeaway, au moins 2 tableaux de données, au moins 8 liens internes dans la prose, jamais un slug absent du snapshot ; FAQ 5-6 dont une défensive et une de périmètre, reprise verbatim dans le FAQPage ; le corps HTML ne contient ni `<style>` ni `<script>`.


Step 6 — AUDIT EXTRACTIF (lire `references/05-audit-extractif-coherence-patterns.md` avant d'écrire le verifier ; `references/07-verrous-a-g.md` §18.3 Verrou A et §18.6 ; importer `scripts/study_locks.py`)

Bloquant :
- Le CSV mène la check-list : le verifier énumère les statistiques depuis le CSV (§12.3 : latest, médianes, moyennes, min/max datés, comptages par filtre, pourcentages, spreads, forward par régime, volatilités, distances aux seuils, sensibilités, « X of top N »), pas depuis ce que Claude pense devoir vérifier. EXTRACT → VERIFY → GATE (couverture 100 %).
- Chaque assertion : `add_claim(description, expected_text_in_html, verifier)`. Tolérances (§12.5) : pourcentage absolu ±0.005 % ; pourcentage relatif ±0.05 % absolu ; pp ±0.005 ; bp ±1 ; comptages exact ; ratios ±0.015 ; moyennes / médianes ±0.01. Plus large = arrondi optimiste.
- Verrou A, la règle la plus importante : l'audit ne charge que le CSV brut. Aucun fichier intermédiaire (`locked_stats.json`, dumps de stdout, `intermediate_stats.json`) ne sert de source de vérité, sinon une valeur fausse s'auto-valide (étude #20 : 14 copies d'une même erreur).
- Le PASS 1 couvre explicitement les sous-titres de charts, les comptages des interp-grids, les encarts takeaway, les bullets de surveillance, les textes alt et title des images (§18.6).
- « Si fail > 0 → BLOQUER la livraison. » Aucun seuil tolérable. Obligatoire pour toute étude avec CSV, tout article pilier citant plus de 5 valeurs, tout dataset page avec plus de 3 stats panel, tout contenu où une erreur a un coût de réputation.
- Verrou L au Step 6 : l'audit lit l'en-tête du CSV publié et échoue si une colonne porte le nom d'une série pre-approval (`sp500`, `spx`, `nasdaq`, `djia`, `hy_oas`, `ig_oas`, `bbb_oas`, `baml`, `case_shiller`) en niveau ; si une colonne citation-required est présente, il vérifie que « CC BY 4.0 » n'apparaît nulle part dans les corps, les metas, le package social ni le JSON-LD, et que la notice de licence réelle est présente dans les deux langues.
- Patterns à haut risque (§14) couverts explicitement : « within X of Y » vérifié par `|value - reference|` ; « highest since X » par recherche de la dernière occurrence ≥ V (aucune → all-time) ; comptage strictement apparié à son filtre exact ; arrondi sans biais directionnel ; tout « approximately X » justifié dans `hedge_justifications.json`.
- Cohérence multi-livrables (§13) : table maître unique en début de session ; après production, grep de chaque claim répété dans TOUS les fichiers (HTML, PHP, MD, verifiers) ; après toute correction, grep IMMÉDIAT de la nouvelle ET de l'ancienne valeur dans tous les fichiers, puis re-run du verifier.


Steps 6.5a-h — VERROUS (lire `references/07-verrous-a-g.md` §18.3-18.5 et `references/02-beats-anti-editorializing-scan.md` §11 ; `scripts/study_locks.py` porte D, E, G, H et le contrôle des commentaires HTML)

Bloquant :
- 6.5a : chaque défense du Step 1.5 présente ; scan des termes chargés ; hook above the fold, premier bullet de l'Executive Summary et dans la TL;DR ; sortie défenses N/N · termes trouvés/corrigés · hook visible OUI/NON · PASS/FAIL.
- 6.5b tripwire narratif : chaque date `YYYY-MM` en prose devient un tuple `(label, date, csv_column, expected, tol)` dans `NARRATIVE_EVENTS` ou une entrée justifiée dans `WHITELISTED_NO_CLAIM`, mode strict.
- 6.5c Verrou B : pour chaque nombre en prose analytique, `(number, concept_label, python_formula_str, expected)` dans `CONCEPT_PAIRINGS`, formule exécutée, compatibilité concept ↔ contexte vérifiée.
- 6.5d Verrou D : grep de `approximately|roughly|about|around|~|close to` suivi d'un chiffre ; chaque occurrence justifiée dans `hedge_justifications.json`, ou ÉCHEC.
- 6.5e Verrou E : grep de `N events / occurrences / observations / onsets / episodes / recessions / false positives / triggers / crossings / cases / instances / times / weeks / months / years`, `N/M`, `N of M` ; chaque occurrence exige une assertion dans compute_stats.py qui produit exactement ce N.
- 6.5f Verrou F : chaque expression de filtre temporel existe dans le dict `FILTERS` et dans le bloc « Filter Definitions » du HTML.
- 6.5g Verrou G : zéro cadratin ( — ) dans tout livrable destiné au site (corps HTML, package social, metas, alt, title ; les plages gardent le demi-cadratin `1959–2007`, les négatifs le signe moins `−0,013`) ; zéro tic IA (`worth noting`, `delve`, `dive into`, `ever-evolving`, `paradigm shift`, `as we navigate`, `in conclusion,`, `truly`, `literally`, `undeniably`, `fundamentally`) ; zéro verbe prescriptif appliqué à un profil (`should`, `must`, `need to`, `ought to`, `we recommend`) ; zéro langage d'action ou de timing (`buy`, `sell`, `entry point`, `price target`, `now is the time`, `overweight`, `underweight`). Règles AMF 2, 3 et 6.
- 6.5h Verrou H : `assert_series_locks(study_dir)` lit les études livrées dans `out/` et échoue sur un H2 de Beat déjà utilisé dans la série, un gabarit de titre repris de l'étude précédente, le même label de robustesse ou la même figure de phrase-pivot que l'étude précédente. Première étude d'une série : PASS par construction. Non rétroactif : R1→R9 restent en l'état.
- « Tout échec en 6 ou 6.5a-h → HALT. Pas de livraison. »


Step 7 — PACKAGE SOCIAL (lire `references/10-social-preflight-upload.md` avant d'écrire le package)

Bloquant :
- Pre-flight r/economics (§15), neuf cases : titre sans terme chargé, énonçant un FINDING chiffré, avec fenêtre de dates ou nombre d'observations ; self-comment finding + taille d'échantillon + « CC BY 4.0, methodology in comments » ; H1 provocant OK, jugement normatif non ; 3 premiers paragraphes 100 % factuels ; context-box dans la première section analytique ; Beat 3 dans les 2 sections suivant Beat 2 ; aucun langage prescriptif. « Si une seule case échoue, le post sera modéré ou hued. »
- Formats : RankMath meta title ≤60 `[Insight central] — [Dataset] ([Années]) | Eco3min` ; meta description ≤155 = le hook ; OG ≤200 ; X ≤280 ; LinkedIn ~600 ; r/dataisbeautiful `[OC]` ; self-comment 3 à 4 lignes ; HN ≤80. La divulgation de robustesse est offerte proactivement dans le self-comment (§5.5). Les mêmes valeurs que le HTML, tirées de la table maître.


Steps 8 et 8b — CHARTS STATIQUES ET INTERACTIF (lire `references/04-charts-statique-interactif.md` avant de générer ; le reste de la data viz relève de `visuels-eco3min`)

Bloquant :
- La donnée dicte le visuel. SCALE JUSTIFICATION documentée par chart ; ratio max/min > 5× → log obligatoire + vue linéaire « Supplementary View » ; 2×–5× choix justifié ; < 2× linéaire. Chart B conçu standalone pour r/dataisbeautiful (aha en 3 secondes).
- Le script lit le CSV, imprime chaque valeur annotée, se termine par un bloc d'assertions contre le CSV ; chaque chart inspecté visuellement, lisible à 380 px. Exports : page ~1400×750 · OG 1200×630 · social 1920×1080 quand le chart DIB est poussé.
- Chart interactif obligatoire (livrable 13b) : SVG en JavaScript natif, aucune bibliothèque externe, conteneur `data-*` dans le corps, tout le JS dans le snippet, donnée = CSV publié servi same-origin depuis `uploads/[YYYY]/[MM]/` ; toute valeur affichée vient d'une colonne du CSV, transformation déclarée assertée dans compute_stats.py ; descriptif uniquement (pas de flèche, de zone acheter/vendre, de projection, de seuil-signal ; bandes grisées = épisodes datables et sourcés) ; le `<picture>` de repli reste affiché jusqu'à un rendu réussi, testé réseau coupé. Vérifications : CSV en ligne à l'URL exacte et au bon mois · chaque colonne déclarée existe dans l'en-tête au caractère près · trois valeurs échantillonnées au survol correspondent au CSV · repli réseau coupé · Tab et flèches · 380 px. Code de référence : `snippet_model.php`, section « INTERACTIVE CHART ». Placé après le Beat 3 (bloc 14b).


Step 9 — GUIDE D'UPLOAD DES IMAGES (lire `references/10-social-preflight-upload.md` §22.2)

Bloquant :
- Par fichier : Title WP ≤60 · Alt identique à l'alt du HTML · Caption = sous-titre du chart · Description 2 à 3 phrases. Uploader SVG et PNG, PDF en archive ; référencer les originaux non suffixés (`-scaled`) ; chemins `uploads/[YYYY]/[MM]` exacts ; justification d'échelle de chaque chart.


Step 10 — ASSEMBLER ET DÉPLOYER (lire `references/09-deploiement-wordpress.md` avant d'assembler ; puis charger `eco3min-import-contenu-bilingue` pour le bundle)

Bloquant :
- Namespace `eco3-[STUDY]-*` par étude, `eco3-realrates` retiré ; le CSS scopé (~12 000 caractères, 63 classes) s'extrait par curl de l'étude publiée la plus récente puis se re-namespace, jamais reconstruit de zéro.
- Spécificité : `.entry-content p` du Customizer (0,1,1) bat toute règle d'étude à une classe. Tout sélecteur dont le sujet est un `<p>` atteint (0,2,0) : `scripts/css_specificity.py` — `boost_paragraph_rules()` après le re-namespace, `lint_paragraph_rules()` doit rendre une liste vide (16/09/2026, R3/R4/R6 : bloc « Latest observation » illisible en live, invisible en preview).
- Un Code Snippet par étude, ordre : garde (slug + variante `-2`) → CSS (`wp_head` 4) → JSON-LD Article/Dataset/FAQPage (`wp_head` 5) → OG et Twitter (`wp_head` 99) → filtres RankMath title/description (99, jamais l'onglet Social) → JS (`wp_footer` 99, délégation FAQ anti-double-init, copie de partage, embed, sommaire mobile). Le corps HTML ne contient ni `<style>` ni `<script>`.
- Règles dures : UTF-8 littéral dans les `content:""` ; Code Snippets sans `<?php` ouvrant ; heredoc `<<<'CSS'` valide ; assets en `wp-content/uploads/[YYYY]/[MM]` du mois courant, identiques dans HTML, snippet et guides ; originaux non suffixés ; SVG uploadés ; FAQ = `<h3>` dans `.eco3-[STUDY]-faq-item` basculant `.eco3-[STUDY]-open` ; OG = le PNG hero ; liens internes `/en/` côté EN ; embeds `https://eco3min.fr/embed/[chart-slug]`.
- Livrer le jeu complet (14 à 18 fichiers, §17.1) avec le résumé d'audit, le README / index (livrable 18) et le doc de pre-review (16).
- Après livraison, toute erreur découverte → son motif au registre (lire `references/12-registre-erreurs.md`) et son verrou au workflow. Ne jamais alléger un verrou sans relire ce registre.


Step R — RAFRAÎCHIR UNE ÉTUDE PUBLIÉE (lire `references/13-rafraichissement-etude-publiee.md` avant de toucher au texte ; ajouté le 18/09/2026)

Bloquant :
- Audit d'entrée avant toute écriture, cinq contrôles : la jumelle FR reçoit le CSS (`curl FR | grep -c eco3-<ns>-css` = 1), chaque `contentUrl` du Dataset répond 200, l'URL de citation est le permalink, un seul `<h1>`, `lint_paragraph_rules()` vide. Le module interactif absent se construit dans le même lot.
- Gelé : flags, taux de base, tableau des cas, tout chiffre dont la règle exige une confirmation différée. Étendu : les observations, dans un fichier suffixé `-V2`, lignes publiées recomputées et comparées avant ajout. L'épisode neuf va dans une section « en temps réel », jamais dans le tableau.
- Byline : mise à jour en premier, première publication entre parenthèses. `dateModified`, descriptions, `temporalCoverage`, FAQ JSON-LD, OG, RankMath (titre non tronqué, `facebook_image`, image à la une) suivent. Une ligne `claims.jsonl` par chiffre neuf et par langue.
- Toute écriture par `update-content` / `snippet-update` avec `expect_count` et `expect_sha256`, dry-run puis réel ; mémo daté avec les `ref` de rollback.


## 16. Checklist éditoriale pré-publication

**Backlink Hook**
- [ ] Hook défini avant production (≤25 mots, statistique frappante)
- [ ] Hook visible above the fold
- [ ] Hook dans TL;DR + 1er bullet Executive Summary + social snippets
- [ ] Hook compréhensible sans lire la page entière

**Adversarial Pre-Review**
- [ ] 4 reviewers simulés avant fetch des données
- [ ] Chaque attaque a une défense localisée dans le contenu
- [ ] Les changements de design issus de la pre-review sont implémentés

**Structure narrative**
- [ ] Beat 1 énoncé fairly (pas de strawman)
- [ ] Beat 2 = contradiction empirique chiffrée
- [ ] Beat 3 présent et substantiel (pas une phrase token)
- [ ] Beat 3 dans les 2 sections suivant Beat 2
- [ ] Verrou H PASS : titres de Beat, figure de phrase-pivot et label de robustesse ne répètent pas l'étude précédente, figure déclarée dans le README

**Anti-editorializing**
- [ ] Loaded-terms scan effectué et fixé
- [ ] Yield Curve Lesson appliquée (data + tableau + FAQ + methodology forcent les citations sans commentaire)
- [ ] H1 sans jugement normatif
- [ ] 3 premiers paragraphes 100 % factuels

**Data accuracy production** (si CSV produit)
- [ ] Tous les chiffres du contenu viennent du CSV
- [ ] Statistiques calculées via Python, copiées depuis stdout
- [ ] Épisodes historiques vérifiés ligne par ligne
- [ ] Direction vs niveau vérifiés séparément
- [ ] Chiffres hors-CSV marqués `<!-- SOURCE -->` ou `<!-- VERIFY -->`

**Audit extractif CSV-led (section 12)**
- [ ] Verifier CSV-led extractif produit (énumère depuis CSV, pas depuis HTML)
- [ ] Toutes les catégories de statistiques de la section 12.3 listées dans le verifier
- [ ] Seuils de tolérance respectés (section 12.5) — pas d'arrondi optimiste
- [ ] 100% des claims présents dans HTML vérifiées au verifier
- [ ] **0 failure** dans le verifier (pas de seuil "tolérable")

**Cohérence multi-livrables (section 13)**
- [ ] Tous les claims numériques répétés grep-ifiés dans TOUS les fichiers (HTML, PHP, MD)
- [ ] Single-source-of-truth table maître documentée
- [ ] Après toute correction d'une valeur : grep ancien-et-nouveau effectué dans TOUS les fichiers
- [ ] Liste finale 13.5 des fichiers parcourue

**Patterns à haut risque (section 14)**
- [ ] Toutes les claims "within X of Y" vérifiées arithmétiquement (14.1)
- [ ] Toutes les claims superlatives "since DATE" vérifiées par lookup CSV (14.2)
- [ ] Tous les comptages appariés à leur filtre exact dans `compute_stats.py` ET la prose (14.3)
- [ ] Aucun arrondi optimiste — précision matche la donnée (14.4)
- [ ] Tout "approximately X" a une justification documentée dans `hedge_justifications.json` (14.5)

**Forward distributions / Surveillance** (si applicable)
- [ ] Disclaimer légal présent ("Past distributions are not predictive...")
- [ ] Surveillance block en 3 éléments (invalidation, confirmation, catalyst)
- [ ] Aucune formulation prescriptive
- [ ] Marqueur `<!-- UPDATEABLE -->` présent

**Chart**
- [ ] Type de chart choisi pour matcher la donnée (pas template forcé)
- [ ] Justification d'échelle documentée
- [ ] Chart B fonctionne standalone pour r/dataisbeautiful
- [ ] Subtitle = takeaway journalistique, pas description d'axe

**Critère final**
- [ ] La page passe le test : un journaliste FT pressé peut citer le hook **dans les 30 secondes** sans lire la suite
- [ ] La page passe le test r/economics pre-flight (zéro point de friction modérateur)
- [ ] Le verifier extractif rapporte 100% des claims du HTML vérifiées contre le CSV (section 12)

---

## 21. Checklist consolidée du pipeline

Complète la checklist éditoriale du §16.

**Structure** : H1 spécifique + période + amorce d'insight, ≤110 · TL;DR
hook + robustesse + périmètre · latest-obs 4 · exec 4-6 dont le premier = hook ·
stats 5-6 · figure hero + sous-titre journalistique · prose « comment lire » ·
vue supplémentaire si >5× · 3 à 5 H2 analytiques avec mécanismes · Beats 1→2→3,
le 3 au plus deux sections après le 2 · encart de contexte · ≥2 tableaux ou
grilles · ≥3 takeaways · forward distribution + disclaimer · Levels to Watch 3-4 ·
points de retournement + observation courante · méthodologie (algorithme +
sensibilité + Filter Definitions + Python) · FAQ 5-6 (défensive + périmètre) ·
citation · related 3-6 vérifiés · footer.

**Intégrité des données** : CSV en premier · chaque valeur issue de stdout ·
PASS 1/2/3 exécutés, couverture 100 %, **audit recalculé depuis le CSV brut
uniquement** · sous-titres de charts, interp-grids, takeaways, surveillance et
textes alt assertés · aucun hedge injustifié (`hedge_justifications.json`
complet) · aucun claim de comptage sans assertion · aucun filtre temporel
informel · appariements concept-nombre vérifiés · tripwire narratif propre ·
points de retournement vérifiés ligne à ligne · directions de régime vérifiées ·
cohérence des valeurs entre livrables.

**Chart interactif** : présent · aucune bibliothèque externe · alimenté par le
CSV publié à l'URL exacte · chaque colonne déclarée existe dans l'en-tête · trois
valeurs de survol échantillonnées contre le CSV · repli `<picture>` testé réseau
coupé · navigable au clavier · lisible à 380 px · bandes grisées limitées à des
épisodes datables et sourcés · zéro élément prescriptif.

**Backlink** : hook défini au Step 0 · présent en TL;DR, en Exec-1 et dans le
social · compréhensible à froid · sous-titres = takeaways · type de chart dicté
par la donnée.

**Éditorial** : trois premiers paragraphes factuels · Beat 3 sincère (au moins une
concession) · « le système a fonctionné » reconnu là où c'est vrai · robustesse
divulguée, pas cachée · ≥8 liens internes vérifiés contre le snapshot · zéro
conseil, zéro certitude · **zéro cadratin dans tout livrable destiné au site,
zéro tic IA, zéro verbe prescriptif, zéro langage d'action (Verrou G)** · pas
le gabarit de titre, la figure de pivot ni le label de robustesse de l'étude
précédente (Verrou H) · les deux pre-flights et tous les audits en PASS.

**Sourcing** : chaque série FRED destinée à une colonne publiée vérifiée sans le
marqueur « Copyrighted: Citation Required » · aucun niveau brut d'une série
pre-approval dans le fichier, même en colonne de contexte (Verrou L) · si une
colonne citation-required subsiste, zéro « CC BY 4.0 » sur la page et licence
réelle dans le JSON-LD · niveaux recoupés contre l'émetteur, pas contre le canal
de redistribution · `provenance.md` complet · **avant de signaler un problème de
licence sur une page du site, lire sa notice et son JSON-LD** : le mécanisme
`eco3_source_rights()` vit dans le snippet, pas dans le CSV.

**Technique et déploiement** : pre-flight du slug fait · le corps n'a ni style ni
script · namespace `eco3-[STUDY]-*` cohérent (un grep du placeholder ne renvoie
rien) · snippet complet (CSS, JSON-LD, OG, RankMath, JS, anti-double-init,
délégation) · JSON-LD validé · FAQ de la page et du schéma identiques au mot près ·
`uploads/[YYYY]/[MM]` correct et identique partout · `-2` propagé si applicable ·
alt et title sur chaque image · charts inspectés visuellement ·
`<!-- UPDATEABLE -->` sur latest-obs et surveillance · preview rendue et vérifiée.

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

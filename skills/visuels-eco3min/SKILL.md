---
name: visuels-eco3min
description: "Standards de fond de tout visuel Eco3min (eco3min.fr), FR et EN — charts macro-financiers, heros, infographies, images sociales, illustrations : sourcing intégré au visuel, conformité AMF en data viz, choix du type de chart selon la donnée, échelles et axes, annotations, cohérence chiffrée article/visuel, qualité technique, recettes de rendu PNG et leurs assertions, copyright, critère de publication. Activer pour toute création ou révision d'un visuel, et dès qu'une demande contient « chart », « graphique », « hero », « héro », « visuel », « PNG », « SVG », « matplotlib », « Playwright », « rendu », « police de repli », « DejaVu », « débordement », « chevauchement », « dollar échappé », « mathtext », « légende », « direct labeling », « double axe », « pie chart », « échelle log », « bandes grisées », « récessions NBER », « flèche », « cible de prix », « c'est AMF-compliant ? », « le chiffre du chart ne matche pas l'article », « copyright du graphique ». Structure : SKILL.md = colonne vertébrale (sourcing §1, les 7 interdictions AMF condensées §2, règles bloquantes de choix de chart et de direct labeling §3, axes §4, cohérence §6, qualité §7, séquence Playwright §7 bis et cinq assertions matplotlib §7 ter condensées, critère de publication §9, checklist §10 verbatim) ; références dans references/ (à lire quand la section le dit) : 01 les 7 interdictions AMF détaillées, 02 tableau de choix de chart, échelles, annotations, 03 recette Playwright complète, 04 code des cinq assertions matplotlib et garde ASCII ; scripts/mpl_chrome.py = chrome canonique posé une fois (header, footer avec signature réservée, stat_tiles, fit_text, char_budget), jamais recopié, 05 copyright et versioning ; gardes réutilisables dans scripts/mpl_guards.py (police rendue, débordement du canvas, chevauchement d'en-tête, dollars échappés, sources avant signature, glyphes hors ASCII) à importer dans tout script matplotlib au lieu de recopier les assertions. Doctrines : la source vit dans le visuel lui-même (institution + code de série + date), pas seulement dans la légende ; un graphique peut violer l'AMF même si le texte ne la viole pas (7 interdictions : flèches achat/vente, zones prescriptives, cibles de prix, scénario unique, allocations recommandées, ranking géographique normatif, timing) ; les bandes grisées portent une légende explicite ; le type de chart sert la donnée, pas le joli (pie, 3D, double axe sauf cas validé, gradient décoratif interdits) ; direct labeling en bout de ligne obligatoire ≤6 séries, légende détachée bannie, spaghetti focus au-delà ; axe Y à zéro pour les barres, libre pour les lignes, log signalé ; tout chiffre du visuel matche le texte, et c'est l'article qui se corrige ; les échecs de rendu sont silencieux (police de repli, titre rogné, textes superposés, mathtext, sources qui mordent la signature) et ne s'attrapent que par assertion dans le script, jamais à l'œil (cycle 20, R2, R4, R6) ; polices vérifiées à l'œil sur le premier visuel d'une série. Hors périmètre : tokens (hex, familles, fonds, formats, chrome canonique) → brand-kit-eco3min ; provenance et licence des données → sourcing-donnees-eco3min ; voix et AMF du texte → editeur-eco3min ; doctrine propre à chaque famille de hero → production-hero-pilier, production-hero-majeur, production-hero-article-eco3min ; charts Reddit → production-chart-of-the-week (dont scripts/chart_guards.py, implémentation éprouvée des mêmes assertions). Combiner avec brand-kit-eco3min (toujours), editeur-eco3min, sourcing-donnees-eco3min, et la skill de production de la famille concernée."
---

# Standards visuels Eco3min

> **Philosophie.** Le système de design Eco3min repose sur deux couches complémentaires :
>
> 1. **Le brand kit (`brand-kit-eco3min`)** définit le minimum commun figé — palette, 3 familles typographiques (Source Serif 4 + Inter + IBM Plex Mono), fond crème, accent terracotta unique, codes couleurs régime, format sourcing, watermark. Il garantit la cohérence perçue cross-canal : un lecteur de r/economics qui voit 4 visuels Eco3min très différents doit toujours percevoir « même publication ».
>
> 2. **Ce skill (`visuels-eco3min`)** couvre les règles de fond qui s'appliquent à TOUS les visuels indépendamment du brand kit : conformité AMF, sourcing intégré, choix de chart selon la nature de la donnée, anti-patterns data viz, cohérence article/visuel, qualité technique, copyright. Ces règles sont des invariants — elles existaient avant le brand kit et continueraient d'exister sans lui.
>
> **Ce qui reste libre** : type de chart (line, histogram, kernel density, scatter, heatmap, matrix…), densité chromatique (sobre 1 accent OU multi-couleurs catégorielles OU gradient continu selon ce que sert la donnée), format/ratio (hors heros piliers à 1536×864 strict), composition. La diversité visuelle est un atout — c'est l'angle d'analyse qui varie, pas la marque.
>
> Pour la voix éditoriale et l'AMF côté texte, voir `editeur-eco3min`. Pour les patterns rédactionnels HTML, voir `formats-eco3min`. Pour les heros piliers spécifiquement, voir `production-hero-pilier`. Pour les charts viraux Reddit DIB, voir `production-chart-of-the-week`.

---

## COMMENT LIRE CE SKILL (découpage du 17/09/2026)

Ce fichier est la colonne vertébrale : chaque règle BLOQUANTE, condensée sous son numéro d'origine, la checklist verbatim et le moment où lire chaque référence. Le texte complet (exemples ❌ / ✅, tableau de choix de chart, recettes de rendu avec leur code, copyright, versioning) a été déplacé VERBATIM dans `references/` et fait foi au même titre que ce fichier. `scripts/mpl_guards.py` porte les assertions du §7 ter : on l'importe, on ne les recopie plus.

| Fichier | Contenu | À lire |
|---|---|---|
| `references/01-amf-7-interdictions.md` | §2 : les 7 interdictions AMF visuelles, chaque ❌ et son ✅ | avant de poser une annotation, une zone, une projection ou un ranking sur un chart |
| `references/02-choix-chart-echelles-annotations.md` | §3, §4, §5 : tableau donnée → chart, direct labeling, anti-patterns absolus, axes, log, annotations recommandées | avant de choisir le type de chart, puis avant de fixer les axes |
| `references/03-rendu-playwright.md` | §7 bis : séquence de chargement des polices, réglages, auto-ajustement du titre, vérification, repli | avant tout rendu HTML/SVG → PNG |
| `references/04-rendu-matplotlib-assertions.md` | §7 ter : code et motif des cinq assertions + garde ASCII | avant tout `savefig` matplotlib, et quand une assertion de `mpl_guards` échoue |
| `references/05-copyright-versioning.md` | §8 copyright, historique v1.0 → v1.6 | avant d'intégrer un élément tiers (logo, capture, image générée) ; à chaque évolution du skill |
| `scripts/mpl_guards.py` | `load_brand_fonts`, `assert_fonts_rendered`, `assert_no_overflow`, `assert_no_header_overlap`, `assert_escaped_dollars`, `assert_sources_before_signature`, `assert_ascii_or_cmap`, `run_guards` | importé par tout script matplotlib d'un visuel Eco3min |

Utilisation depuis un script de chart :

    sys.path.insert(0, os.path.expanduser('~/.claude/skills/visuels-eco3min/scripts'))
    from mpl_guards import load_brand_fonts, assert_escaped_dollars, run_guards
    CMAP = load_brand_fonts(FONT_DIR)      # enregistre les TTF, asserte les 3 familles, retourne le cmap
    ...
    run_guards(fig, ax, CMAP)              # les cinq assertions + ASCII, avant fig.savefig

Les cycles Chart of the Week importent `production-chart-of-the-week/scripts/chart_guards.py`, implémentation éprouvée des mêmes gardes avec le bandeau de killer phrase ; les deux modules portent la même doctrine (§7 ter).

---

## 1. Sourcing intégré dans le visuel

Même règle qu'en rédactionnel : la source apparaît **dans le visuel lui-même**, pas seulement dans la légende d'article. Un graphique extrait du contexte (capture, repost, AI Overview) doit rester attribuable.

**Position standard** : coin inférieur **gauche** (chrome canonique brand-kit v2.0 §0 ; la signature Eco3min occupe le coin droit), petite taille, mais lisible.

**Format type**
- Données brutes d'une institution : `Source: BCE · T4 2025`
- Calculs Eco3min : `Calculs Eco3min sur données FRED` ou `Calculs Eco3min · sources : BCE, BRI, INSEE`
- Estimation : `≈ estimation Eco3min · méthode dans l'article`

**Mention Eco3min** : présence systématique, discrète, en bas du visuel. Pas de logo géant. Le but est l'attribution, pas le branding.

**Date du visuel** : si la donnée évolue (taux, indices), inclure la date d'extraction (`données au 28 avril 2026`). Évite les visuels périmés repartagés sans contexte.

Pour le format canonique 2 lignes en IBM Plex Mono, voir `brand-kit-eco3min` section 6.

---

## 2. Conformité AMF visuelle — 7 interdictions (lire `references/01-amf-7-interdictions.md` avant toute annotation)

Toutes les règles AMF du skill `editeur-eco3min` ont une équivalence visuelle. Un graphique peut violer la conformité AMF même si le texte de l'article ne la viole pas.

Bloquant :
1. **Pas de flèches achat/vente** — annotation neutre datée à la place.
2. **Pas de zones colorées prescriptives** — les zones grisées marquent des régimes économiques (récessions, cycles), descriptif, avec **légende explicite** : `Zones grisées : récessions NBER`. Zones en codes régime du brand kit : descriptif par nature.
3. **Pas de cibles ou objectifs de prix** — seules les projections d'institutions tierces, attribuées et nommées.
4. **Pas de scénarios sans dispositif de nuance** — au moins 2, idéalement 3 scénarios, même fermeté visuelle, légende `Scénarios hypothétiques — non prédictifs`.
5. **Pas d'allocations recommandées en visuel** — allocations historiques observées, sourcées, seulement.
6. **Pas de comparaisons géographiques avec ranking visuel** — bar chart trié admis, légende neutre, aucun mot normatif dans le titre.
7. **Pas de timing matérialisé visuellement** — annotation factuelle datée, le lecteur conclut.

---

## 3. Choix du type de chart selon la donnée (lire `references/02-choix-chart-echelles-annotations.md` avant de choisir)

Règles standard de data viz finance — Claude doit choisir le type qui sert la donnée, pas le type qui fait joli. Le tableau donnée → chart approprié → à éviter est dans la référence 02.

Bloquant :
- **Multi-entités (pays, actifs, secteurs, indicateurs — 2 à 6 séries)** : line chart multi-séries en palette catégorielle (`brand-kit-eco3min` §2.5), labels directs en bout de ligne. Au-delà de 6 séries : spaghetti focus (N séries grises en arrière-plan + 1-2 séries accentuées aux rangs 1-2). Le format multi-entités est historiquement sous-utilisé chez Eco3min — le mobiliser dès que la donnée est comparative par nature.
- **Direct labeling** : pour tout chart à ≤6 séries, **chaque série est labellisée directement en bout de ligne** (ou au point le plus dégagé), dans la couleur de sa série, en Inter 11-12 px. **Légende détachée bannie**. Au-delà de 6 séries, seules les séries accentuées sont labellisées ; le nuage gris reçoit un label collectif unique.
- **Anti-patterns absolus** : pie charts à éviter en macro-finance (illisible au-delà de 3 segments) ; **3D : jamais** ; **double axe Y** à éviter sauf nécessité réelle (deux variables fortement corrélées dont les unités diffèrent), avec mention explicite du risque dans la légende — cas validé BBB-share + BBB OAS ; **gradient décoratif** interdit : une couleur = une catégorie, ou un gradient = une dimension continue.

---

## 4. Échelles et axes (lire `references/02-choix-chart-echelles-annotations.md` avant de fixer les axes)

Bloquant :
- **Axe Y commence à zéro** : obligatoire pour les bar charts. Optionnel — souvent indésirable — pour les line charts de prix, ratios, indices.
- **Échelle logarithmique** pour les séries de prix ou indices sur plus de 10 ans, les ratios à très grande dynamique, les comparaisons de croissances en % ; toujours indiquer `(échelle log)` dans le titre ou la légende.
- **Unités explicites** sur toutes les étiquettes d'axes (`%`, `points de base`, `milliards EUR`, `% du PIB`, `index 100 = janv. 2020`).
- **Période dans le titre** du chart. Pas de chart sans cadrage temporel.

---

## 5. Annotations recommandées (lire `references/02-choix-chart-echelles-annotations.md`)

Récessions en zones grisées légendées (NBER, OFCE/INSEE, CEPR) ; événements clés en annotations textuelles datées ; moyennes historiques en pointillé avec label ; régimes nommés en couleur du code régime (`brand-kit-eco3min` §3) ; **marqueur principal** : 1 accent terracotta `#B85C3C` sur le moment-clé (règle d'unicité `brand-kit-eco3min` §2.3).

---

## 6. Cohérence article ↔ visuel — vérification obligatoire

**Tout chiffre affiché dans le visuel doit matcher exactement le chiffre cité dans le texte.** Une discordance sape la crédibilité de l'ensemble et expose à des critiques AMF.

**Vérifications systématiques**
- Périodes citées identiques (un chart "1970-2024" ne va pas avec un texte qui parle de "1970-2023")
- Chiffres clés identiques (si le texte dit "+3,2 %", le visuel ne montre pas "+3,1 %")
- Sources identiques (un chart "Source : BCE" ne va pas avec un texte qui dit "selon les données de la BRI")
- Méthode de calcul identique (si le texte parle de "moyenne mobile 12 mois", le chart doit afficher une MM12, pas une MM6)

**Si écart détecté en révision** : c'est l'article qui est généralement à corriger sur le chiffre du visuel (les visuels sont produits depuis les données brutes), mais vérifier au cas par cas.

---

## 7. Qualité technique — non négociable

Une seule de ces erreurs disqualifie le visuel pour publication.

- **Pas de chevauchement** texte sur texte, texte sur courbe, label sur logo
- **Pas de troncature** : aucun mot coupé, aucun chiffre coupé
- **Pas de fautes d'orthographe** (français correct, accentuation correcte sur les majuscules — "É", pas "E")
- **Pas de pixellisation** : exporter en SVG quand possible, sinon PNG haute résolution (≥2x la taille d'affichage)
- **Lisibilité en miniature** : pour les exports sociaux, vérifier que le titre et au moins une donnée clé sont lisibles à 25 % de la taille (test feed mobile)
- **Contraste suffisant** : texte sombre sur fond clair ou inverse, jamais texte gris clair sur fond gris foncé
- **Cohérence des unités** : pas de mélange `M€` et `Md€` dans le même chart sans raison

---

## 7 bis. Rendu PNG — recette Playwright (lire `references/03-rendu-playwright.md` avant tout rendu HTML/SVG)

Chromium rend la page **avant** que les Google Fonts soient chargées si on ne l'attend pas explicitement : PNG en police de repli, **sans erreur, sans avertissement**.

**Séquence obligatoire — aucune étape n'est facultative** :
1. `set_content(html, wait_until="load")`
2. `await page.evaluate("document.fonts.ready")`
3. `wait_for_timeout(650)` — 650 à 700 ms ; en dessous, le rendu part trop tôt
4. exécuter l'auto-ajustement de titre (`window.__fit()`, attendre `window.__fit_done` par `wait_for_function`)
5. `wait_for_timeout(150)`
6. `screenshot(..., clip={"x":0,"y":0,"width":W,"height":H})`

Sauter l'étape 2 **ou** l'étape 3 suffit à produire le repli silencieux. `viewport` aux dimensions cibles, `device_scale_factor=2`, redescente par PIL/LANCZOS ; SVG pré-calculé en Python et embarqué inline (jamais en ressource externe). L'auto-ajustement du titre tourne **après** confirmation du chargement des polices. Vérifier la police rendue à l'œil sur le **premier visuel d'une série**.

---

## 7 ter. Rendu matplotlib — cinq assertions avant `savefig` (lire `references/04-rendu-matplotlib-assertions.md` avant tout `savefig`, importer `scripts/mpl_guards.py`)

Aucun de ces échecs ne lève d'exception : le PNG sort, il a l'air correct sur une vignette. **Les assertions se posent dans le script, pas dans la relecture.**

1. **La police demandée est bien la police rendue** — `FontProperties(family=X).get_name() == X` pour les trois familles (repli DejaVu Sans silencieux).
2. **Aucun texte ne déborde du canvas** — boîte englobante de chaque texte dans `[0, W] × [0, H]` (un titre trop long est rogné, pas mis à la ligne).
3. **Les textes d'en-tête ne se recouvrent pas** — intersection des boîtes de `fig.texts` < 12 % de la plus petite.
4. **Les `$` sont échappés** — deux `$` non échappés basculent la chaîne en mathtext italique ; écrire `\\$` et asserter.
5. **Le pied de source ne mord pas la signature** (16/09/2026, R6) — `x1` de la ligne `Sources` < `x0` de `Eco3min Research` − 8 px : test d'ordre horizontal, le seuil de 12 % laissant passer une morsure de fin de ligne.

Bonus, même famille : IBM Plex Mono n'a ni U+2009 ni U+202F — rester en ASCII dans tout texte de visuel et l'asserter, sinon vérifier le cmap de chaque glyphe non ASCII. Même famille que le garde étendu aux graduations et libellés d'axe (R2, R4) : chaque niveau de texte oublié par le balayage se rejoue.

**Le chrome se pose avec `scripts/mpl_chrome.py`, il ne se recopie pas** (ajouté le 18/09/2026 après quatre itérations de pied sur les charts de l'étude #6) : `header()` (titre serif, sous-titre Inter, ajustés), `footer(sources, method, url)` (deux lignes mono à gauche, signature et URL à droite ; la ligne gauche est réduite jusqu'au plancher de 5,2 pt et, si elle dépasse encore, le script lève avec le budget de caractères au lieu de laisser mordre la signature), `stat_tiles()` (bandeau de 2 à 4 tuiles KPI du brand kit §0, un seul chiffre en terracotta, filets), `fit_text()`, `char_budget()` (~150 caractères mono à 5,6 pt sur 8 in). Les gardes de `mpl_guards.py` restent obligatoires derrière.

---

## 8. Copyright et droits visuels (lire `references/05-copyright-versioning.md` avant d'intégrer un élément tiers)

Interdits : logos de médias concurrents, captures d'écran d'articles ou de pages tiers, images générées contenant marques ou personnages IP, **reproduction de graphiques publiés ailleurs** (toujours reproduire à partir des données brutes), photos de personnalités sans droits. Autorisés : données brutes des sources publiques, graphiques produits par Eco3min à partir de ces données, visuels génératifs originaux. Données fournisseurs payants (Bloomberg, Refinitiv, S&P) : vérifier les droits d'usage avant publication.

---

## 9. Critère de publication d'un visuel

Avant chaque publication, poser ces questions :

- Le visuel apporte-t-il **quelque chose que le texte seul ne fournit pas** (forme, échelle, dynamique, comparaison) ? Si la même information passe mieux dans une phrase, supprimer le visuel.
- Le visuel est-il **compréhensible en standalone** (sans lire l'article) ? Titre, source, axes lisibles, légende suffisante.
- Le visuel **survit-il à un repartage hors contexte** (capture sur X, AI Overview) avec sourcing et attribution intacts ?
- Le visuel est-il **distinctif** ? Si un lecteur aurait pu trouver exactement le même graphique dans la presse généraliste, il n'apporte rien à Eco3min.

---

## 10. Checklist pré-publication

**Conformité AMF visuelle**
- [ ] Aucune flèche achat/vente
- [ ] Aucune zone colorée prescriptive
- [ ] Aucune cible de prix matérialisée
- [ ] Scénarios prospectifs au pluriel + cadrés comme hypothétiques
- [ ] Allocations descriptives sourcées, jamais recommandées
- [ ] Comparaisons géographiques en chiffres neutres, sans ranking normatif
- [ ] Aucune annotation de timing actionnable

**Sourcing**
- [ ] Source intégrée dans le visuel (institution + date)
- [ ] Mention Eco3min discrète mais présente
- [ ] Date d'extraction si donnée vivante
- [ ] Format conforme à `brand-kit-eco3min` section 6

**Conformité brand kit**
- [ ] Typographie : Source Serif 4 + Inter + IBM Plex Mono (cf. `brand-kit-eco3min` section 1)
- [ ] Fond = un des 3 registres (`brand-kit-eco3min` §2.2), choix justifié
- [ ] Mode chromatique identifié (sobre / catégoriel / gradient — `brand-kit-eco3min` §5.2)
- [ ] Mode sobre : accent terracotta `#B85C3C` à 1 occurrence maximum
- [ ] Mode catégoriel : rangs §2.5 dans l'ordre, ≤6-7 séries, labels directs en bout de ligne (pas de légende détachée)
- [ ] Si régime nommé : code régime utilisé (cf. `brand-kit-eco3min` section 3)
- [ ] Aucune teinte ad hoc inventée

**Data viz**
- [ ] Type de chart adapté à la donnée (pas de pie chart, pas de 3D)
- [ ] Échelle d'axe Y justifiée (zéro pour bar, libre pour line, log si nécessaire)
- [ ] Unités explicites sur tous les axes
- [ ] Période cadrée dans le titre
- [ ] Annotations contextuelles si pertinentes (récessions, événements)

**Cohérence**
- [ ] Tous les chiffres du visuel matchent les chiffres du texte
- [ ] Périodes identiques entre texte et visuel
- [ ] Sources identiques

**Qualité technique**
- [ ] Aucun chevauchement, aucune troncature
- [ ] Aucune faute d'orthographe (accents sur majuscules inclus)
- [ ] Lisibilité en miniature testée (pour exports sociaux)
- [ ] Contraste suffisant
- [ ] Résolution suffisante (SVG ou PNG ≥2x)
- [ ] Si rendu Playwright : polices réellement chargées, vérifiées à l'œil sur le premier visuel de la série (cf. §7 bis)

**Copyright**
- [ ] Aucun logo média tiers
- [ ] Aucune capture de graphique tiers reproduite
- [ ] Aucun élément IP non libre
- [ ] Si données fournisseur payant, droits vérifiés

**Critère final**
- [ ] Le visuel apporte quelque chose que le texte ne fournit pas
- [ ] Le visuel est compréhensible en standalone

**Chrome canonique (brand-kit-eco3min v2.0 §0)**
- [ ] Sources bas-gauche, signature `Eco3min Research` bas-droite, zéro cadratin dans le visuel
- [ ] `mpl_guards.run_guards` (ou `chart_guards` sur un cycle Chart of the Week) passé avant `savefig`
- [ ] `brand_tokens.check_source` passé sur le script ou le SVG

---

## Versioning (historique complet dans `references/05-copyright-versioning.md`)

- **v1.6** (17/09/2026) — découpage en références + `scripts/mpl_guards.py` (les cinq assertions du §7 ter et le garde ASCII, importables) ; alignement sur le chrome canonique de `brand-kit-eco3min` v2.0 (sources à gauche, signature `Eco3min Research` à droite, zéro cadratin dans les exemples de format du §1) ; §7 bis ne prétend plus exclure matplotlib, régi par §7 ter. Aucune règle AMF, sourcing ou qualité modifiée.

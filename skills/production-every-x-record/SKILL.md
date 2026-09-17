---
name: production-every-x-record
description: "Production et révision des pages « Every X since Y » d'Eco3min (eco3min.fr) : le registre de référence d'un indicateur ultra-cité (Sahm Rule, yield curve, cycles Fed, taux réels, faillites bancaires FDIC, vagues d'inflation) avec son anomalie live, son tableau du record, son hero PNG autoportant, son chart interactif et son CSV, conçu pour les backlinks de qualité (FT, Ritholtz, Abnormal Returns) et la viralité r/economics. Activer pour « page Every X », « registre », « record historique », « every … since », « toutes les … depuis », « page backlink », « les 4 piliers », « data-check », « hook citable », « phrase citable », « cosplay », « CSS scopé », « snippet guardé par slug », « JSON-LD base64 », « chart canvas », « bande de chiffres-clés », « axe plafonné », « labels off-scale », « Research Summary », et pour R7 / R11 de la série GENERIQUE. Structure : SKILL.md = colonne vertébrale (règle cardinale verbatim, règles bloquantes §0 à §6 sous leurs numéros d'origine, anti-patterns, méthode anti-erreur, checklist et rappel zéro commentaire HTML verbatim) ; références dans references/ (à lire quand la section le dit) : 01 gate, formule de sélection, angle killer et honnêteté-blindage avec les cas Sahm et yield curve, 02 design découplé du brand kit, palette hex, axe Y, typographie, interdits de cosplay et règle de tri, 03 hero PNG autoportant et architecture de page (bloc HTML, snippet PHP, tableau du record, chart interactif, CSV, maillage) ; gardes dans scripts/record_checks.py (CSS 100 % scopé, bloc HTML sans script ni commentaire, zéro cosplay, round-trip base64, FAQ JSON-LD = FAQ visible, garde-fou par slug simulé en PHP avec stubs WP, node --check, chiffres-clés par livrable ; testées sur le registre des faillites bancaires du 01/09/2026). Doctrines : le backlink vient du contenu citable et de la distribution, jamais du design ; le claim killer est une hypothèse jusqu'à preuve sur le CSV (le hook un-inversion → récession est mort sur FRED, « never wrong » sur Sahm était faux) ; l'honnêteté étroite bat le superlatif cherry-pické et le dek ne contredit jamais la table du record ; design DÉCOUPLÉ du brand kit (fond blanc, gris contexte, un seul accent vermillon réservé à l'anomalie, crème et terracotta interdits ici) ; autorité EARNED jamais ASSERTED (« Cite this », DOI, « Abstract », share, click-to-copy, badges, affiliation, capture email bannis, v2 juillet 2026) ; CSS 100 % scopé sous un wrapper unique (bug réel body/* sur Blocksy) ; JSON-LD en base64 par slug au wp_head et chart canvas au wp_footer, jamais de shortcode ; trous de source affichés, jamais interpolés ; slug d'étude ≠ slug dataset, equity backlink jamais orpheline (update-in-place ou 301) ; r/economics flair Research Summary, titre factuel sans adjectif, un seul canal. Hors périmètre : la page dataset brute (production-dataset), le chart DIB autonome (production-chart-of-the-week), la couche éditoriale complète (production-research-study), le détail de la distribution HN (production-killer-hn). Combiner avec production-research-study, production-killer-hn, visuels-eco3min, eco3min-import-contenu-bilingue, production-dataset, pipeline-eco3min, editeur-eco3min, brand-kit-eco3min (référence de ce dont on s'écarte)."
---

# Every X — pages record historique pour backlink

## COMMENT LIRE CE SKILL (découpage du 17/09/2026)

Ce fichier est la colonne vertébrale : les deux règles cardinales, chaque règle BLOQUANTE de §0 à §6 sous ses numéros d'origine, les anti-patterns, la méthode anti-erreur, la checklist et le rappel zéro commentaire HTML. Le texte complet de §0 à §4 (rationale, cas réels Sahm / yield curve / inflation waves, palette hex, spécifications du chart interactif) a été déplacé VERBATIM dans `references/` et fait foi au même titre que ce fichier. Chaque section ci-dessous nomme le fichier à lire ; le lire est obligatoire au moment indiqué, pas facultatif. `scripts/record_checks.py` porte les gardes que chaque production recopiait dans son `validate.py` : on les importe, on ne les recopie plus.

| Fichier | Contenu | À lire |
|---|---|---|
| `references/01-gate-angle-honnetete.md` | §0 GATE (formule des 4 piliers, data-check, surface virale) et §1 angle killer (hook ≤ 25 mots, honnêteté-blindage avec les cas Sahm et « come back bigger », cadrage technique, phrase de désamorçage) | avant de proposer un sujet, puis avant d'écrire le hook |
| `references/02-design-decouple-cosplay.md` | §2 design découplé du brand kit : palette hex par défaut, figure/fond et dispositif de l'aha, piège de l'axe Y, typographie, interdits de cosplay, autorisés, règle de tri | avant de dessiner le hero ou le chart, puis avant la relecture de la page |
| `references/03-hero-png-architecture-page.md` | §3 hero PNG autoportant (bande de chiffres, anti-doublon, rendu inspecté) et §4 architecture de page (bloc HTML, CSS scopé, snippet PHP, tableau du record, chart interactif, CSV, maillage, URLs d'assets) | avant de rendre le hero, puis avant d'assembler le bloc HTML et le snippet |
| `scripts/record_checks.py` | gardes bloquantes : bloc HTML propre, CSS 100 % scopé, zéro cosplay, round-trip base64, FAQ JSON-LD = FAQ visible, garde-fou par slug (statique + simulation PHP avec stubs WP), node --check, chiffres-clés par livrable | importé par le `validate.py` de la production, avant livraison |

Utilisation depuis un dossier de production :

    sys.path.insert(0, os.path.expanduser('~/.claude/skills/production-every-x-record/scripts'))
    from record_checks import run_all
    fails = run_all(html={'en': html_en, 'fr': html_fr}, php=snippet_php, wrapper='.e3m-xxx',
                    slugs={'en': slug_en, 'fr': slug_fr}, js_path='src/chart.js',
                    figures={'en': ['4,117'], 'fr': ['4\u202f117']})
    assert not fails, fails

Le dossier `out/r1-bank-failures/` du projet « B. PLUS page bilingue » (registre des faillites bancaires, 01/09/2026) est l'implémentation de référence : `src/build_pages.py`, `src/build_snippet.py`, `src/hero.py`, `src/validate.py`. Le dupliquer, pas le réécrire ; son `validate.py` recopie les gardes que `record_checks.py` fournit désormais.

## RÈGLE CARDINALE (les deux non-négociables)

1. **Le backlink ne vient ni du design ni du polish — il vient du contenu CITABLE + la distribution.** Le design sert l'autorité perçue et la viralité, pas le backlink. Ne jamais brûler des itérations sur l'esthétique en croyant gagner des liens : passé un seuil de propreté, le levier est ailleurs (la phrase citable, le dataset, le timing du post). Erreur historique récurrente — la corriger.

2. **Le claim killer est une HYPOTHÈSE jusqu'à preuve sur le CSV.** Aucune production ne commence avant que le finding ait survécu au calcul sur la vraie série. (Cas d'école : le hook "un-inversion → récession" semblait le meilleur ; testé sur FRED, il MEURT — les deux épisodes Volcker donnent un délai négatif. Abandonné avant production. À l'inverse "never wrong" sur Sahm était FAUX et a dû être reformulé.) Le data-check précède tout.

---

## 0. GATE — avant toute production (lire `references/01-gate-angle-honnetete.md`)

Bloquant :
- §0.1 Les quatre piliers du seul carton backlink confirmé (yield curve → FT + Ritholtz) : indicateur ULTRA-CITÉ (le lecteur le connaît déjà) ; track record quasi-parfait sur longue période ; une ANOMALIE LIVE au moment de publier ; un dataset unique téléchargeable (CSV + JSON-LD Dataset). Manque un pilier → la pièce sera plus faible. Pas d'anomalie live → c'est de l'evergreen SEO, pas un carton backlink ; route différente.
- §0.2 Data-check bloquant (RÈGLE CARDINALE #2) : tirer la série (FRED/source primaire), **calculer le finding sur la vraie donnée**, confirmer qu'il tient. Un superlatif (« jamais », « chaque », « le seul ») qui ne survit pas exactement → reformuler vers la version étroite qui tient (§1.2). Ne jamais publier un superlatif que le CSV ne soutient pas.
- §0.3 GATE surface virale (→ `production-killer-hn`) AVANT de choisir le canal : le format « Every X » est r/economics-natif (finding débattable, payoff sans expertise lourde) et DIB-natif si chart-centré ; il n'est PAS HN-natif si le sujet est macro-spécialisé sans hook universel (échec term premium). Ne pas forcer HN.

---

## 1. L'angle killer (lire `references/01-gate-angle-honnetete.md`)

Bloquant :
- §1.1 Le hook = la phrase citable, ≤ 25 mots, factuelle, datée, contre-intuitive : celle qu'un journaliste FT reprend telle quelle. Le punch va dans le hook + le PNG + le 1er commentaire — **jamais dans le titre Reddit** (§6).
- §1.2 L'honnêteté est le BLINDAGE : la version honnête et étroite bat toujours le superlatif cherry-pické (« jamais trompé » était faux ; *« premier faux signal depuis 1970 ; deux exceptions antérieures, chacune suivie d'une récession »* est blindé ET toujours explosif). Disclose toi-même les cas gênants. **Le dek/hook ne doit JAMAIS contredire la table du record** : relire le dek APRÈS la table, ligne par ligne, chaque superlatif doit survivre à chaque ligne. Si le créateur/une autorité a commenté l'indicateur, le sourcer ET vérifier que ton décompte ne contredit pas le sien. Citation = source exacte obligatoire (permalink + date + support) ; jamais de mémoire ; `<!-- VERIFY -->` tant que non sourcée.
- §1.3 Cadrage technique non négociable : décrire l'indicateur pour ce qu'il EST (coïncident vs prédicteur, real-time vs revised). Mal cadrer = un quant te corrige en commentaire #2 ; le cadrage juste rend souvent l'anomalie PLUS frappante.
- §1.4 Phrase de désamorçage sémantique pour tout finding reposant sur une classification (« faux signal », « récession », « épisode ») : assumer le choix de définition + la falsifiabilité (*« My criterion is explicit: […]. If [new data] later shows otherwise, I'll revise. »*).

---

## 2. Design graphique — DÉCOUPLÉ DU BRAND KIT ECO3MIN (lire `references/02-design-decouple-cosplay.md`)

Bloquant :
- Principe figé : une page backlink n'optimise PAS la cohérence avec le site mais les CODES VISUELS DU GENRE (autorité FT / Fed / Bloomberg) + la lisibilité en vignette + la survie en dark-mode. Le brand kit (fond crème #F8F5EE, terracotta #B85C3C) est fait pour le site, pas pour ces pages. La sobriété EST l'optimisation ; plus de couleurs = moins de partage.
- §2.1 Palette par défaut : fond blanc pur `#FFFFFF` (ou `#FCFCFC`), **jamais de crème** ici ; texte `#14141A` ; séries/contexte gris `#9CA3AF` ; bandes de contexte `#D9DCE1` ; grille `#E3E5E9` ; **UN SEUL accent saturé, rouge vermillon `#E03127`, RÉSERVÉ à l'élément focal/l'anomalie** (la ligne de seuil critique peut le prendre, en pointillé).
- §2.2 Figure/fond : contexte en gris muet, anomalie en accent, lisible en 3 secondes. Ne JAMAIS colorier les éléments de contexte dans l'accent. Un seul dispositif géométrique de l'aha par visuel, léger (alpha ~0,5, trait fin), sémantiquement lié au finding ; s'il faut l'expliquer par une légende dédiée, il est trop malin.
- §2.3 Axe Y : si des outliers écrasent le seuil et l'anomalie dans les 10 % bas du graphe, **plafonner l'axe** et laisser les gros pics sortir par le haut (clip) ; **labeller chaque pic hors-échelle avec sa valeur** en gris foncé `#54545f`, PAS en accent.
- §2.4 Typo : serif éditorial pour le titre (Source Serif 4), sans pour les labels/UI (Inter), mono pour les chiffres (IBM Plex Mono), parce qu'elles servent l'autorité, pas par obligation de brand. Piège : IBM Plex Mono n'a pas l'espace fine (U+2009) → insécable U+00A0 pour les nombres FR.
- §2.5 Autorité EARNED, jamais ASSERTED (FIGÉ). **INTERDITS sur la page** : bloc « Cite this » / « How to cite », BibTeX/APA, DOI ou identifiant fabriqué ; rangée de boutons « Share » / « Share this research » ; click-to-copy (banni depuis la v2 : une version antérieure le prescrivait, en contradiction avec cette section) ; badges / pills « Public dataset », « Open research », « Peer-reviewed », « Verified », trust-seals, compteurs de vues/citations ; badge / logo de licence décoratif ; bloc auteur / affiliation / ORCID ; cadre « Abstract », « Working paper », « Download the paper / PDF version » ; capture email / newsletter (§4). **AUTORISÉ** : bouton CSV simple, ligne de meta discrète « License: CC BY 4.0 », source FRED · NBER, section Méthodologie, TL;DR en langage simple (PAS « Abstract »), petit kicker de section. Règle de tri : CONTENU (informe / prouve / explique) reste, DÉCORATION (réclame le prestige ou le partage) dégage. `cosplay_scan` de `scripts/record_checks.py` le vérifie avant livraison.

---

## 3. Le hero PNG autoportant (lire `references/03-hero-png-architecture-page.md`)

Bloquant :
- PNG self-contained : titre + sous-titre + **bande de 3-4 chiffres-clés** + sourcing 2 lignes mono + watermark, tout BAKÉ dans l'image. Format 1536×864, livré en ≥2x (3072×1728). **Zéro stat redondante dans la bande** (remplacer le doublon par une ancre distincte).
- PAS de tableau dans l'image si la donnée est mono-métrique (courbe) ; tableau seulement si la donnée est génuinement tabulaire. Matcher le visuel à la nature de la donnée.
- Anti-doublon : HTML minimal autour du PNG (dek éditorial + meta) ; pas de `<figcaption>` ni de titre HTML qui répète le PNG — **une seule couche dit le titre** (le H1 SEO est fourni par Blocksy).
- Rendu : l'outil est libre, le critère ne l'est pas — tout élément chiffré tracé depuis le vrai CSV chargé dans la session ; layout vérifié (footer dans le cadre, rien de tronqué ni chevauché) ; **screenshot rendu et INSPECTÉ avant livraison** ; l'aha se lit en vignette ~400px ; hero FR rendu et inspecté séparément, taille/wording dédiés plutôt qu'une traduction qui tronque.

---

## 4. Architecture de page (lire `references/03-hero-png-architecture-page.md`)

Bloquant :
- Bloc HTML = markup + CSS uniquement, **AUCUN `<script>`, AUCUN H1**, dans un bloc Custom HTML (pas l'éditeur classique → wpautop). Blocksy fournit le titre/H1.
- **CSS 100 % SCOPÉ (BLOQUANT)** : tout le markup sous UN wrapper à classe unique (ex. `.e3m-wave`), chaque sélecteur du `<style>` commence par ce wrapper. INTERDITS : `body{…}`, `*{…}`, `html{…}`, tout sélecteur d'élément nu (bug réel : fuite sur le header/footer Blocksy de toute la page). Reset en `.wrapper *{box-sizing:border-box}`. Vérification programmatique obligatoire : `css_scoped` de `scripts/record_checks.py`.
- **Snippet PHP séparé** (Code Snippets, PHP, « Run everywhere », **sans `<?php` de tête**), **guardé par slug** selon le motif canonique de `eco3min-import-contenu-bilingue` (`is_singular('page')` + `get_queried_object() instanceof WP_Post` + map par `post_name`, nom UNIQUE). Au `wp_head` : JSON-LD `@graph` (Article + Dataset + FAQPage) des DEUX langues, **encodé en base64 par slug** (jamais en clair/heredoc : l'échappement casse silencieusement dans le bundle). Au `wp_footer`, mêmes slugs : le **chart interactif canvas, AUCUNE lib**, qui injecte `window.<data>` + le JS et se monte sur un `<div id="…">` placeholder du bloc HTML ; pas de shortcode ; si le JS échoue le div vide est invisible. Rien d'autre, pas de click-to-copy. `snippet_static` + `php_simulate` de `scripts/record_checks.py` vérifient le motif et l'émission slug par slug.
- **Hook + TABLEAU du record above-the-fold, en HTML** indexable (JAMAIS le record uniquement dans une image). Barres de magnitude CSS pures autorisées dans le tableau (anomalie en accent, contexte en gris) ; masquer la colonne sous ~480px si elle serre.
- Chart interactif : readout mono au survol ET au touch ; crosshair ; boutons de fenêtres (Full + 4-5 épisodes du registre) qui **remplacent un 2e chart comparatif** ; labels des pics avec halo blanc (`strokeText` sous le `fillText`) ; **trous de source = `null` affiché « no data », JAMAIS interpolé ni ponté** ; DPR-aware, responsive, i18n par slug (FR : virgule + insécable) ; **testé en harnais Playwright/Chromium desktop + mobile + zoom, captures INSPECTÉES**. Plafond ~2 visuels (hero + interactif), au-delà = bascule « outil ».
- Structure éditoriale : finding-first / mécanisme / steelman / « what it doesn't prove » (→ `production-research-study`).
- **CSV téléchargeable** = la conversion qui SERT le backlink. **Pas de capture email** sur une page backlink (elle vit sur la page dataset). Bouton CSV SEUL dans la zone download ; deux CSV du même dataset = toujours « CSV seul ».
- **Maillage interne** vers le cluster dans le corps + le bloc Related, PAS un bouton concurrent dans la zone download.
- **URLs des assets** (hero, CSV) en `uploads/AAAA/MM/` du mois EN COURS, base identique partout (BLOQUANT dans `eco3min-import-contenu-bilingue`, s'applique ici aussi).

---

## 5. URL / SEO / cannibalisation

- **Ne JAMAIS orphaner l'equity backlink.** Une page qui ranke et a des backlinks (FT/Ritholtz) : on **met à jour en place** (même slug) ou on **301** vers le nouveau. Jamais une slug neuve qui abandonne les liens existants.
- **Pour un NOUVEL évènement Reddit, créer une page GÉNUINEMENT NOUVELLE** (nouvel angle), ne PAS re-soumettre la même URL (risque repost r/economics, surtout avec un historique Rule IV).
- **Page étude ≠ page dataset.** L'étude vise les requêtes humaines composées (history, false signals, why 2024) ; le dataset vise le ticker/terme brut (trafic bot/IA). **La slug de l'étude ne doit PAS reprendre le terme de la page dataset** (sinon cannibalisation). Ex : étude `sahm-rule-false-signals-history` vs dataset `sahm-rule-recession-indicator-dataset`.
- Slug plat sous `/en/`, jamais inventer un slug qui existe déjà.

---

## 6. Distribution r/economics (→ `production-killer-hn` pour le détail)

- **Flair : `Research Summary`** (pas `Blog` = signal auto-promo → Rule IV ; pas `Editorial` = opinion contestable ; jamais `Misleading`).
- **Titre : factuel, daté, sourcé DANS le titre, ZÉRO adjectif.** Pas de "never wrong"/"shocking". **Pas la structure "X did Y. Z did not." (deux phrases juxtaposées = sensationnaliste, bannie).** `[OC]` à la fin. Le punch n'est PAS dans le titre.
- **Premier commentaire posté dans la minute** : finding-first, méthode transparente, **pré-empte les 3 objections** (real-time vs revised / coïncident-pas-prédicteur / les cas-limites du décompte), source l'autorité, inclut la **phrase de désamorçage + falsifiabilité** (§1.4), **lien UNE seule fois en bas**.
- **Un seul canal à la fois.** Pas de cross-post HN simultané (self-comment sur sa propre soumission = risque `[dead]` sur compte chargé).
- **Pas de self-comment de relance** ; répondre seulement aux vraies questions.
- **Timing** : viser ~9h00–9h30 ET (15h00–15h30 Paris) pour un sujet US. **Éviter la fenêtre d'une sortie macro qui porte SUR ton sujet** — risque double : noyé par le flux, ou péremption en direct (cas : ne pas poster un indicateur EMPLOI en semaine NFP/JOLTS/ADP ; le tirage peut contredire ton angle 2 jours après publication). Vérifier le calendrier macro avant de figer la date.

---

## Anti-patterns (ce qu'on REJETTE explicitement)

- Croire que le design fait le backlink → c'est le contenu citable + la distribution.
- Publier un superlatif que le CSV ne soutient pas (cherry-pick) → version honnête étroite.
- **Un dek/hook qui contredit la propre table du record de la page** → relire le dek contre chaque ligne de la table (cas réel : "almost never come back bigger" vs 7/12 "higher").
- Hook hedgé/mou ("may be", "arguably") → factuel et assumé + falsifiabilité.
- Titre Reddit accrocheur / structure "X. Y." → factuel, daté, sans adjectif.
- Fond crème / palette brand kit sur une page backlink → blanc + codes du genre.
- Accent (rouge) sur les éléments de contexte → réservé à l'anomalie.
- Tableau dans l'image pour une donnée mono-métrique → courbe ; tableau seulement si données tabulaires.
- Doublon titre/source PNG ↔ HTML → une seule couche dit le titre.
- **CSS non scopé dans le bloc HTML (`body{}`, `*{}`, éléments nus)** → fuite sur le thème ; tout sous le wrapper.
- **JSON-LD en clair/heredoc dans le snippet** → base64 par slug (casse silencieuse à l'embarquement bundle sinon).
- **Interpoler / ponter un mois manquant de la source** dans le hero ou le chart interactif → trou honnête (`null`, "no data") + caveat en méthodo.
- **Cosplay académique** ("Cite this", DOI, "Abstract", bloc auteur/affiliation, "Download the paper") → autorité gagnée par le contenu, jamais assertée par des widgets.
- **Boutons "Share this research" / click-to-copy / badges "public dataset" / "open research" / trust-seals / compteurs** → sobriété FT/Fed ; ces insignes BAISSENT la crédibilité et signalent l'auto-promo (Rule IV).
- **Badge / logo de licence décoratif** → la licence est une ligne de meta discrète, pas un insigne.
- Nouvelle slug qui orpheline les backlinks → update-in-place ou 301.
- Slug d'étude qui reprend le terme du dataset → cannibalisation.
- Capture email sur la page backlink → CSV seul ; email sur la page dataset.
- Cross-post HN + Reddit simultané, self-comment de relance → un canal, zéro relance.
- Forcer HN sur un sujet sans surface virale → SEO/DIB/X.

---

## Méthode anti-erreur

- **CSV = source de vérité.** Tout chiffre calculé, jamais de mémoire. Audit extractif : le CSV énumère les claims (→ `production-research-study`).
- **Définir explicitement la règle de franchissement/épisode** (sustained vs touch d'un mois). Piège réel : un `>=seuil` sans condition de persistance sur-compte (Nov 1976 compté à tort). Définir, puis coder.
- **JS du snippet : `node --check`** avant livraison. **JSON-LD : parser (JSON valide) + round-trip du base64** (décoder ce qui sera livré et re-parser). La FAQ du JSON-LD doit être IDENTIQUE à la FAQ visible (sinon pénalité mismatch) — **vérifier programmatiquement** (extraire les paires h3/p du HTML, normaliser, comparer aux `mainEntity`).
- **Simuler le snippet avant livraison quand PHP est disponible** : `php -l` + stubs WP minimaux (`add_action`, `is_singular`, `get_queried_object`) → vérifier l'émission sur chaque slug du bundle ET le silence sur un slug tiers (garde-fou anti-fuite).
- **Rendre un preview de CHAQUE visuel (hero EN, hero FR, widget desktop/mobile/zoom) et l'inspecter** avant de committer — l'aha doit se lire en vignette.
- **Cohérence des chiffres** entre hero PNG, tableau HTML, chart interactif, JSON-LD, 1er commentaire, social — tous sur le même CSV. Automatiser ce qui s'automatise (mêmes valeurs clés grep-ées dans chaque livrable).
- **`<!-- VERIFY -->`** sur tout fait hors-CSV non encore sourcé (citations, permalinks) ; ne pas publier tant qu'ils restent.

Les contrôles mécaniques de cette section (CSS scopé, node --check, round-trip base64 du JSON-LD, FAQ JSON-LD = FAQ visible, `php -l` + stubs WP sur chaque slug et silence sur un slug tiers, chiffres-clés grep-és par livrable) sont implémentés dans `scripts/record_checks.py` (`run_all`) : l'importer dans le `validate.py` de la production, ne pas les réécrire.

---

## Checklist pré-publication

- [ ] Les 4 piliers de sélection réunis (indicateur cité, track record, anomalie live, dataset)
- [ ] Finding calculé sur le CSV et confirmé (ou reformulé en version étroite honnête)
- [ ] Dek/hook relus contre la table du record — zéro contradiction interne
- [ ] Cas-limites disclosés ; décompte aligné sur l'autorité si elle a parlé
- [ ] Citations sourcées (permalink + date) ; plus aucun `<!-- VERIFY -->`
- [ ] Hook ≤ 25 mots, citable, factuel
- [ ] Design : fond blanc, gris contexte, UN accent réservé à l'anomalie, axe plafonné + labels off-scale gris
- [ ] Hero PNG autoportant (chiffres-clés sans doublon + source bakés), pas de tableau si mono-métrique ; hero FR rendu et inspecté séparément
- [ ] Pas de doublon titre/caption PNG ↔ HTML
- [ ] **Zéro cosplay** : aucun "Cite this"/DOI/"Abstract"/share-buttons/click-to-copy/badges/affiliation/"PDF du papier" ; autorité portée par le contenu (license = ligne meta discrète, CSV = bouton simple, Méthodologie = substance)
- [ ] Bloc HTML sans script ni H1 ; **CSS 100 % scopé sous le wrapper (0 sélecteur global, vérifié programmatiquement)**
- [ ] Snippet PHP guardé par slug (motif canonique) : JSON-LD base64 EN+FR au wp_head + chart au wp_footer ; pas de `<?php` de tête ; nom unique ; garde-fou testé (émet sur les slugs du bundle, silence ailleurs)
- [ ] Tableau du record en HTML above-the-fold (barres CSS optionnelles) ; chart interactif testé en harnais (desktop + mobile + zoom, captures inspectées) ; trous de source affichés honnêtement ; CSV seul ; pas d'email
- [ ] Slug ≠ slug dataset ; equity préservée (update-in-place / 301) si page existante
- [ ] node --check JS OK ; JSON-LD valide + round-trip base64 ; FAQ JSON-LD = FAQ visible (vérif programmatique)
- [ ] URLs d'assets en `uploads/AAAA/MM` du mois EN COURS, base identique partout (→ skill import)
- [ ] Titre Reddit factuel + `[OC]` ; flair Research Summary ; 1er commentaire prêt (3 objections + désamorçage + lien en bas)
- [ ] Date hors fenêtre macro qui porte sur le sujet ; ~15h Paris ; un seul canal
- [ ] Metas RankMath (title/desc) cohérentes avec le cadrage honnête ; alt image descriptif

---

## Combiner avec
- `production-research-study` — couche éditoriale (Beat 1/2/3, Backlink Hook, anti-editorializing, audit CSV-led).
- `production-killer-hn` — couche distribution (GATE surface virale, titre, 1er commentaire, anti-self-comment, timing).
- `visuels-eco3min` — AMF appliqué à la data viz, sourcing intégré, qualité technique.
- `eco3min-import-contenu-bilingue` — format canonique du snippet (base64, garde-fou par slug), règle AAAA/MM des assets, bundle d'import.
- `production-dataset` — la page dataset associée (CSV servi, JSON-LD Dataset).
- `pipeline-eco3min` — création/màj de la série CSV en amont.
- `brand-kit-eco3min` — RÉFÉRENCE DE CE DONT ON S'ÉCARTE (le brand est pour le site, pas pour ces pages).

---

## Versioning
- **v1** — création (Sahm, yield curve).
- **v2 (juil. 2026, page inflation waves)** — click-to-copy retiré du snippet et BANNI (contradiction avec §2.5) ; rendu hero rendu outil-agnostique (le critère = CSV réel + screenshot inspecté) ; format snippet aligné sur le skill import (JSON-LD base64 par slug, motif de garde canonique, montage du chart au wp_footer sur placeholder — pas de shortcode) ; ajout scoping CSS BLOQUANT (bug réel body/*) ; cohérence dek↔table ; specs chart interactif (halo, trous honnêtes, test harnais mobile) ; bande de stats sans doublon ; dispositif géométrique de l'aha encadré ; piège U+2009 Plex Mono.
- **v3 (17/09/2026)** — découpage : SKILL.md = colonne vertébrale, §0 à §4 déplacés VERBATIM dans `references/01`→`03`, gardes extraites dans `scripts/record_checks.py` (testées à l'identique sur le registre des faillites bancaires du 01/09/2026 + tests négatifs) ; second frontmatter (corps mort) supprimé ; description réécrite ; aucune règle modifiée.
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

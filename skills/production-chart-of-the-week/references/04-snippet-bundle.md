# production-chart-of-the-week — référence : Snippet interactif et bundle JSON d'import (ÉTAPE 4, ÉTAPE 10)

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

ÉTAPE 4 — Le snippet interactif (pour la page eco3min)

Architecture obligatoire
- Page WordPress : contient UNIQUEMENT le shortcode [eco3min_chart_xxx] dans un bloc Shortcode ou HTML
- Snippet PHP (Code Snippets, type "Frontend only") : enregistre le shortcode, encapsule HTML + SVG + CSS + JS inline
- Aucun script ou style dans la page WordPress elle-même
Cette séparation est non-négociable : Paul gère tout son JS/CSS via Code Snippets, jamais inline dans les pages WP.

Conventions techniques du snippet
- Préfixe CSS : toutes les classes en eco3-[chartname]- pour éviter les collisions Blocksy
- !important sur toutes les CSS pour overrider les styles thème
- SVG vanilla : pas de Chart.js / D3 / autre dependency, pour vitesse de chargement
- Vanilla JS : pas de jQuery, pas de framework
- IntersectionObserver : animation reveal seulement quand le chart entre dans le viewport
- Mobile responsive : breakpoint à 640px, font-sizes réduits
- Accessibilité : tabindex, role="graphics-symbol", aria-label sur chaque rect

Les 3 vues obligatoires
Tout chart interactif doit proposer minimum 3 vues toggle :
- Default : la vue principale (équivalent du chart Reddit)
- Breakdown #1 : décomposition par catégorie principale (par entreprise, par pays, par secteur, etc.)
- Breakdown #2 : décomposition par dimension secondaire (par année, par sous-période, par classe d'actifs, etc.)
Cette interactivité est la seule raison rationnelle pour qu'un viewer Reddit clique vers eco3min. Le chart statique sur Reddit ne peut pas faire les toggles. C'est le hook conversion central.

Référence : le snippet canonique
snippet_capex_interactive.php du cycle AI capex (mai 2026) sert de template de base. Pour chaque nouveau chart, dupliquer et adapter :
- Le nom du shortcode et du data-attribute
- Le tableau de données (PROGRAMS, COMPANIES, etc.)
- Les fonctions buildRows() pour les 3 vues
- Le X_MAX et X_TICKS
- Les couleurs des segments breakdown


ÉTAPE 10 — BUNDLE JSON D'EXPORT (PLUGIN WORDPRESS « CHART OF THE WEEK »)

Le plugin « Chart of the Week » ingère un bundle JSON unique par cycle et fait, dans l'ordre : (1) crée/maj le Code Snippet (idempotent par nom, balise <?php de tête retirée, activé), (2) crée/maj les 2 pages EN/FR avec metas RankMath + JSON-LD + image mise en avant, liées en traductions Polylang, (3) insère la carte d'étude en 1re position dans chaque hub et recompte le compteur (les 2 emplacements : valeur accent + ligne « N studies/études »).

**Forme de livraison, selon la taille.** Sous ~15 Ko, la réponse ne contient rien d'autre que le JSON dans un bloc de code. Au-delà — cas normal dès que l'article est complet ; le bundle du cycle 19 faisait 65 Ko — l'écrire dans `chart_of_the_week.json` du dossier du cycle et livrer le fichier, en annonçant sa taille et la raison. **Ne jamais tronquer le JSON pour le faire tenir dans un bloc.**

Schéma (schema_version courant) :
- cycle : { id, date (YYYY-MM-DD), topic }
- snippet : { name (= « Eco3min — <sujet> »), description, scope: "global", shortcode: "[eco3min_chart_xxx]", code }
  → code = le contenu du snippet PHP SANS la balise <?php de tête (Code Snippets l'ajoute lui-même pour le type « php »). Par défaut le snippet est en SVG/JS vanilla sans dépendance (cf. ÉTAPE 4). Si, par dérogation à l'ÉTAPE 4, une bibliothèque externe est utilisée (Chart.js, etc.), elle DOIT être chargée depuis un CDN autorisé par la Content-Security-Policy du site : cdn.jsdelivr.net ou unpkg.com — JAMAIS cdnjs.cloudflare.com (bloqué par la CSP : le graphe ne se rend pas, "Chart is not defined" — bug observé cycle 11).
- pages : { en: {...}, fr: {...} } — chacune :
  - lang ("en"/"fr"), post_type ("page"), status ("publish" — publication directe depuis le 19/09/2026 ; le plugin met "draft" si le champ manque)
  - slug : EN = slug nu servi sous /en/ via Polylang (mode répertoire) ; FR = slug plat à la racine
  - title (= H1 / post_title), content : HTML **classique** complet de l'article, PNG statique inséré AU MILIEU. **ZÉRO commentaire HTML, zéro `<script>`, zéro `ld+json` inline.**
    ⚠️ « Zéro commentaire HTML » inclut les **délimiteurs Gutenberg** `<!-- wp:html -->`. Le `content` part en HTML classique ; les shortcodes s'exécutent exactement pareil. Règle figée août 2026 après l'incident Autoptimize du 27/08 : 8 pages servies en HTTP 500, invisibles pour Google, corps affiché normalement dans le navigateur. Panne silencieuse. Vaut aussi pour les commentaires en tête des cartes hub. Détail dans `eco3min-import-contenu-bilingue`.
  - featured_image : URL complète du PNG = https://eco3min.fr/wp-content/uploads/AAAA/MM/cycle{N}_chart_desktop_16x9.png (STRICTEMENT identique au src de la <figure>, à seo.og_image et à json_ld.image)
  - seo : { title (≤60 car.), description (150-160 car.), focus_keyword, canonical, og_title, og_description, og_image (= featured_image), og_image_alt, robots: ["index","follow"] }
  - json_ld : [ Article, Dataset ] — le champ image de l'Article = la même URL PNG ; le Dataset pointe le CSV téléchargeable
- polylang : { link_translations: true }
- hubs : { en: { post_id: 12664, insert_after: "<div class=\"eco3-grid\">", dedupe_marker, card_html }, fr: { post_id: 12662, insert_after: "<div class=\"eco3-grid\">", dedupe_marker, card_html } }
  → post_id figés : 12664 = Macro Watch (EN), 12662 = Observatoire macro (FR). Carte EN = AVEC lang-note 🇫🇷 vers la page FR ; carte FR = SANS lang-note. dedupe_marker = le href canonique de la carte (anti-doublon au ré-import).

SKILLS À CHARGER AVANT DE CONSTRUIRE LE BUNDLE (les oublier coûte une passe de correction)

- `hub-card-etude` — templates verbatim de `card_html` EN et FR, et leurs pièges : préfixe `en/` sur la featured image côté EN, slug FR plat, lang-note 🇫🇷 sur la carte EN et JAMAIS sur la carte FR, `.eco3-card__media` sur UNE seule ligne (sinon wpautop injecte des `<br>`), ordre strict media → badge → title → desc → sources → lang-note → cta. Ne jamais inventer ce balisage.
- `eco3min-import-contenu-bilingue` — la règle « zéro commentaire HTML » et le contrôle mécanique à exécuter avant de rendre le bundle.

VALIDATION AVANT LIVRAISON

Le bundle est écrit par un **script qui refuse d'écrire si une assertion casse**, jamais assemblé à la main. Le script est versionné dans le dossier du cycle.

Assertions minimales :
- cohérence du nom de PNG et de CSV entre `<figure> src`, `og_image`, `json_ld.image`, `featured_image` et `distribution.contentUrl` ;
- `post_type` = `page` ; post_id des hubs = 12664 (EN) / 12662 (FR) ;
- longueurs SEO (title ≤60, description 150-160) ;
- le code du snippet ne commence pas par `<?php` ;
- zéro commentaire HTML, zéro `<script>`, zéro `ld+json` dans le `content` ;
- PNG statique non adjacent au chart interactif ;
- asymétrie de lang-note respectée ;
- zéro em-dash ;
- `<div>` ouverts et fermés en nombre égal dans chaque `content` (la réserve du cycle 21 en avait un non fermé) ;
- aucune mention de statut réglementaire (« AMF », « registered », « enregistré auprès ») dans le `content` : Eco3min n'en a aucun (editeur-eco3min règle 7) et le disclaimer de pied est posé par hook global, jamais dans la page ;
- JETONS PÉRIMÉS : quand un chiffre a changé en cours de cycle (recalage de millésime, correction), lister les anciennes valeurs (`77.1`, `7.4 min`, `tenfold`, `2024`…) et asserter leur absence sur la sérialisation JSON complète, cartes hub comprises. Et la méthode de propagation : chaque phrase chiffrée se réécrit par paire explicite avec `assert old in s`, jamais par remplacement global d'un nombre.

DIVERGENCE DE DOCTRINE NON TRANCHÉE (cycle 19)

`eco3min-import-contenu-bilingue` interdit le champ `json_ld` dans les pages et impose que le snippet porte le JSON-LD en base64 guardé par slug, au motif d'un doublon dans le `<head>`. Mais cette skill se déclare explicitement « sans hubs », donc hors périmètre Chart of the Week. Tant que l'arbitrage n'est pas fait : on suit le schéma ci-dessus (`json_ld` dans les pages) et on vérifie au Preview du plugin qu'il n'y a bien qu'**un seul** bloc JSON-LD dans le `<head>`.

Règles bloquantes du bundle :
- Le nom du PNG dans featured_image, le src de la <figure>, og_image et json_ld.image sont STRICTEMENT identiques et suivent cycle{N}_chart_desktop_16x9.png.
- Le snippet code ne commence JAMAIS par <?php.
- Les post_id des hubs sont 12664 (EN) et 12662 (FR).
- Cohérence des chiffres : les chiffres clés des cartes hub et des pages sont identiques à ceux de l'article et de l'audit (mêmes valeurs au chiffre près).
- Le bundle n'est généré que sur « donne moi le json », jamais spontanément.
- Le `content` des deux pages ne contient AUCUN commentaire HTML, délimiteurs Gutenberg compris.
- `card_html` suit les templates **verbatim** de `hub-card-etude` — ce balisage ne s'invente pas.
- Aucun em-dash nulle part dans le bundle.

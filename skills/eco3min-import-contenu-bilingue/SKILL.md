---
name: eco3min-import-contenu-bilingue
description: "Assemblage + IMPORT d'une paire de PAGES WordPress bilingues (EN+FR) via le plugin Eco3min Import (Page bilingue), puis le bundle JSON, poussé et exécuté à distance par tools/wp_push.py + ability eco3min/import-bundle (19/09/2026 : publication directe, dry_run obligatoire, le bundle ne transite jamais par le MCP). Fond délégué aux skills de contenu (research-study, dataset, q-and-a, every-x-record). Active pour produire les 2 pages, audit bloquant si chiffres, metas, snippet et composant interactif. RÈGLES FIGÉES : la seconde langue n'est JAMAIS une traduction par défaut — miroir, adaptation légère ou forte, tranché et annoncé AVANT de rédiger, faits communs identiques au chiffre près ; composant interactif OBLIGATOIRE sur chaque paire (sauf page outil/simulateur), barre de qualité en 4 tests, décidé AVANT rédaction ; snippet OBLIGATOIRE portant JSON-LD des 2 pages en base64 + composant, guardé par slug, jamais dans le HTML ni un champ json_ld ; metas RankMath en EN ET FR ; import en PAGE (jamais post), aucun hub ; zéro commentaire HTML ; assets en uploads/AAAA/MM du mois EN COURS. Combiner avec archi-, editeur-, visuels- et formats-eco3min."
---

# Eco3min — Import contenu bilingue (paire de PAGES EN + FR)

## Mission et périmètre
Ce skill est la couche **ASSEMBLAGE + IMPORT** : à partir d'un contenu déjà conçu, produire une **paire de pages WordPress bilingues** (EN + FR) prêtes à être ingérées par le plugin **« Eco3min Import → Page bilingue »**, puis — sur commande — le **bundle JSON d'import**.

Ce skill ne rédige PAS le fond. La prose, l'angle, la structure éditoriale, le TL;DR, la conformité AMF et le maillage interne viennent des skills de contenu selon le type de page :
- étude de recherche → `production-research-study`
- page dataset → `production-dataset`
- Q&A → `production-q-and-a`
- page record « Every X » → `production-every-x-record`
- page outil / simulateur → `simulateurs-eco3min`
- toute rédaction / révision / style / AMF → `editeur-eco3min`
- structure du site, silos, levels, slugs, parentage → `archi-eco3min`
- visuels (charts, infographies, images sociales) → `visuels-eco3min` + `brand-kit-eco3min`
- blocs HTML (encarts, TL;DR, FAQ) → `formats-eco3min`

Ce skill orchestre la mise en forme bilingue, les assets, l'audit, les metas, le snippet de données structurées, le composant interactif et le packaging JSON. Il est le pendant de `production-chart-of-the-week`, mais générique et sans Reddit ni hubs.

**Portée de la section « Composant interactif ».** Elle vaut au-delà du bundle `bilingual_page` : un projet qui produit des pages Eco3min dans un autre format d'import (Format C v1.1 des clusters, par exemple) charge ce skill **pour cette seule section** — la barre de qualité et les contraintes de forme y sont identiques ; seule la plomberie de livraison du snippet change, et elle relève alors du projet.

## Trois différences fondamentales vs production-chart-of-the-week
1. **Import en PAGE WordPress** (`post_type: "page"`), jamais en article/post.
2. **Aucune mise à jour des hubs** Macro Watch (12664) / Observatoire macro (12662). Le bundle ne contient PAS de bloc `hubs`. Si un bloc `hubs` traîne, le plugin l'ignore (avec avertissement) — mais on n'en produit pas.
3. **Aucune machinerie Reddit/DIB** : pas de titre [OC], pas de top comment, pas de zones 1/2/3, pas de test beautiful, pas d'ancrage cognitif, pas de pack de lancement.

## Livrables (7 max, certains optionnels)
1. `page_en.html` — HTML Gutenberg complet de la page EN. **Toujours produit.**
2. `page_fr.html` — HTML Gutenberg complet de la page FR, à l'un des trois degrés d'adaptation arbitrés (cf. « Décision bilingue »). **Toujours produit.**
3. `snippet.php` — snippet Code Snippets. **OBLIGATOIRE.** Il porte toutes les données structurées JSON-LD des deux pages (EN + FR), guardé par slug (cf. section dédiée), **et le composant interactif de la paire**, lui aussi obligatoire (cf. « Composant interactif »).
4. PNG(s) — visuel(s) de la page. **OPTIONNEL**. Nommage canonique bloquant (cf. infra).
5. `dataset.csv` — données téléchargeables. **OPTIONNEL** (pages dataset / études chiffrées).
6. `fact_check_audit.md` — audit ligne-par-ligne. **BLOQUANT dès que la page contient des chiffres / citations** (cf. infra).
7. `import.json` — bundle d'import pour le plugin. 

## Ordre de production
1. **Contenu prêt** (via le skill de contenu approprié). Langue forte d'abord — souvent l'EN, mais pas toujours (cf. « Décision bilingue »).
2. **Deux décisions, dans le même souffle, AVANT toute rédaction** :
   a. **Décision bilingue** : arbitrer le degré d'adaptation de la seconde langue, l'annoncer, attendre l'accord si le choix est disputable.
   b. **Décision du composant interactif** : la question qu'il tranche et son mécanisme, annoncés. Elle conditionne les séries à récupérer et le placement du visuel statique.
3. **Assets** : visuel(s), CSV — selon le type de page.
4. **Page de la langue forte** assemblée en HTML Gutenberg (image statique placée selon la section « Placement de l'image statique »). Aucun JSON-LD dans le HTML, aucun `<script>`.
5. **Audit factuel ligne-par-ligne** sur cette première page (BLOQUANT si chiffres) → `fact_check_audit.md`, zéro 🔴 résiduel avant de continuer. Les séries qui alimentent le composant y passent au même titre que celles du texte.
6. **Page de la seconde langue**, au degré d'adaptation arbitré à l'étape 2. Les faits communs aux deux versions sont identiques au chiffre près ; les faits propres à la version adaptée passent leur propre audit.
7. **Metas SEO RankMath EN + FR** (obligatoires dans les deux langues : title ≤60, description 150-160, focus keyword, canonical, OG) + construction du snippet portant le JSON-LD des deux pages **et le composant**.
8. **bundle JSON** (réponse = uniquement le JSON dans un bloc de code).
9. Terminer par une **checklist pré-import** adaptée à la page.

## Décision bilingue — la seconde langue n'est pas une traduction par défaut

**Règle figée.** Une paire bilingue Eco3min n'est pas un miroir Polylang. Le degré d'adaptation est un **choix éclairé, tranché par Claude avant de rédiger la seconde langue, et annoncé** — jamais un réflexe de traduction, jamais un réflexe de réécriture intégrale.

### Les trois degrés

| Degré | Ce que c'est | Quand |
|---|---|---|
| **1. Miroir** | Même sujet, mêmes données, même architecture. Écriture idiomatique dans la langue cible : on ne calque pas la syntaxe, mais on ne change ni les faits ni les exemples. | Le sujet porte identiquement dans les deux marchés, et les données pertinentes sont les mêmes des deux côtés. |
| **2. Adaptation légère** | Même thèse, même architecture, mêmes données centrales. On substitue les **points de référence** : institutions, comparables, ordres de grandeur familiers, exemples d'ancrage. | Le sujet porte des deux côtés, mais le lecteur d'un marché n'a pas les mêmes repères (Fed/Treasury/S&P 500 vs BCE/OAT/CAC 40). C'est le cas le plus fréquent. |
| **3. Adaptation forte** | Même thèse, **données propres** au marché de la langue cible. L'architecture peut diverger. Les deux pages ne partagent que l'idée directrice et la méthode. | Le sujet n'a pas de public en l'état dans la seconde langue, ou l'objet national diffère (PER vs 401(k), FDIC vs cadre de résolution européen). |

### Comment trancher

Trois critères, dans cet ordre :

1. **La demande observée par langue.** Si la session dispose de chiffres GSC, Ahrefs ou Bing par langue, ils tranchent. Un cluster à zéro impression dans une langue est le signal du degré 3, pas du degré 1.
2. **La disponibilité de la donnée dans le marché cible.** Une série qui n'existe que pour un pays impose soit le degré 1 (on publie la donnée étrangère telle quelle, en l'assumant), soit le degré 3 (on change de donnée). Jamais le bricolage intermédiaire.
3. **Le coût du faux.** Le degré 1 sur un sujet sans public produit une page morte. Le degré 3 sur un sujet universel produit deux pages qui se concurrencent inutilement et double le coût d'audit. En cas d'hésitation entre deux degrés adjacents, choisir le moins invasif et le dire.

**Claude propose et justifie.** Si le brief impose un degré, il prévaut. Si le choix est disputable, Claude l'annonce et attend l'accord avant de rédiger — pas après.

### Invariants, quel que soit le degré

- **Écriture native dans chaque langue.** Aucune version n'est un décalque syntaxique de l'autre, même au degré 1. Ton FT/Les Échos/Bloomberg côté FR, FT/Bloomberg côté EN.
- **Les faits communs aux deux versions sont identiques au chiffre près.** Un écart chiffré entre EN et FR sur un même fait est un défaut bloquant, jamais un arrondi.
- **Jamais de chiffre « équivalent » fabriqué** pour singer l'autre version. Une asymétrie d'ancrage assumée et signalée vaut mieux qu'un chiffre non sourçable.
- **Les faits propres à une version adaptée passent leur propre audit** (mêmes règles, cf. section audit). Le degré 3 double la charge d'audit : c'est le prix, il se budgète à l'étape 2.
- **Slugs différents** par langue : le slug de la seconde langue suit son mot-clé natif, pas la traduction du premier.
- **Metas RankMath rédigées nativement** par langue, jamais traduites littéralement.
- **Le degré retenu est documenté** dans le recap de livraison, avec sa justification en une phrase.

### Anti-patterns de la décision bilingue

- Traduire par défaut sans avoir posé la question du public.
- Réécrire intégralement par défaut « pour faire natif » quand un degré 2 suffisait.
- Publier une seconde page uniquement pour la symétrie, sur un sujet sans lecteur dans cette langue, sans réancrage.
- Trancher le degré **après** avoir rédigé la seconde page.
- Laisser diverger un chiffre commun entre les deux versions.

## Audit factuel ligne-par-ligne (BLOQUANT si la page contient des chiffres)
Même discipline que `production-chart-of-the-week` / `production-research-study` / `review-article-eco3min`. Forme condensée ici.

- **Extraction exhaustive** : parcourir l'article du début à la fin, lister CHAQUE nombre, date précise, citation attribuée, comparaison superlative, calcul dérivé. 50 chiffres → 50 lignes.
- **Classification** 🟢 / 🟡 / 🔴 :
  - 🟢 : valeur recalculée dans la session depuis le CSV/source, ou fait historique iconique stable.
  - 🟡 : plausible, in-context, mais non recalculée ni web-vérifiée.
  - 🔴 : citation attribuée non confirmée ; chiffre précis (≥3 sig.) sur fait récent non confirmé ; « approximately X » sans calcul ; superlatif non recalculé.
- **Résolution de chaque 🔴** : (a) recalcul Python visible, (b) web_search source primaire, (c) reformulation prudente, ou (d) suppression.
- **Cohérence inter-livrables** : un même chiffre clé est identique partout — page EN, page FR, snippet (JSON-LD), **composant interactif**, visuel, CSV.
- **Audit livré comme fichier séparé, AVANT le bundle.** Pas de bundle tant qu'un 🔴 subsiste.
- **La série du composant passe l'audit comme le reste.** Une donnée qui n'apparaît que dans le composant, jamais dans le texte, n'échappe pas à l'extraction : elle est publiée, donc elle est auditée.
- **Adaptation forte (degré 3)** : les données propres à la seconde version ne sont PAS couvertes par l'audit de la première. Elles passent le même audit, dans le même fichier, en section distincte.
- Garde-fou label/série : une série dont le label annonce une statistique (median/average, real/nominal) DOIT être cette statistique.

## Le snippet (OBLIGATOIRE) — données structurées + composant + garde-fou slug
Le snippet est le seul endroit où vivent les données structurées, et le seul endroit où vit le JS du composant. Règles figées :

- **JSON-LD dans le snippet, JAMAIS dans le HTML.** Aucun `<script type="application/ld+json">` dans `content`. Aucun champ `json_ld` dans le bundle (il serait émis en double par le plugin au wp_head → doublon `<head>`, nuisible SEO).
- Le snippet porte les **DEUX langues** : le JSON-LD EN et le JSON-LD FR (typiquement Dataset + FAQPage, ou les types adaptés à la page), sélectionnés à l'exécution selon le slug.
- **GARDE-FOU par slug (obligatoire)** : le snippet n'émet QUE sur les slugs des pages du bundle, jamais ailleurs (sinon fuite sur tout le site). Le garde-fou s'applique à **CHAQUE hook** du snippet — `wp_head` pour le JSON-LD, `wp_footer` pour le composant. Motif canonique :

```php
add_action( 'wp_head', function () {
    if ( ! is_singular( 'page' ) ) { return; }
    $obj = get_queried_object();
    if ( ! ( $obj instanceof WP_Post ) ) { return; }
    $ld = array(
        'slug-en' => '<BASE64_JSONLD_EN>',
        'slug-fr' => '<BASE64_JSONLD_FR>',
    );
    $slug = $obj->post_name;
    if ( isset( $ld[ $slug ] ) ) {
        echo "\n" . '<script type="application/ld+json">' . "\n"
           . base64_decode( $ld[ $slug ] ) . "\n"
           . '</script>' . "\n";
    }
}, 20 );
```

- **JSON-LD encodé en base64.** Recommandé fortement : le payload est du JSON, embarqué dans du PHP, lui-même embarqué dans le JSON du bundle. Le base64 (`base64_decode`) supprime tout risque d'échappement (guillemets, apostrophes FR, `<`, `>`). Sans base64, l'échappement triple casse silencieusement les données structurées. (Si le base64 est chunké sur plusieurs lignes pour la lisibilité, retirer les retours ligne avant `base64_decode` via `str_replace`.)
- **FAQ JSON-LD = FAQ visible** de la page correspondante, dans CHAQUE langue (mismatch = pénalité rich results). En adaptation forte, les deux FAQPage peuvent différer en contenu : chacune doit refléter la FAQ réellement visible sur SA page. Si la page FR existante n'a pas été fournie dans la session, sa FAQPage est marquée « à aligner sur la FAQ visible FR » et vérifiée avant import.
- Code sans balise `<?php` de tête (Code Snippets l'ajoute pour le type « php »).
- Nom de snippet UNIQUE par étude (le plugin est idempotent par nom → deux études au même nom se surchargent). Convention : `Eco3min — {slug ou id d'item} JSON-LD`.
- **Vérification avant livraison (recommandé fort)** : round-trip du base64 (décoder, re-parser le JSON) ; si PHP est disponible dans l'environnement, `php -l` + simulation avec stubs WP (`add_action`, `is_singular`, `get_queried_object`) pour vérifier l'émission sur chaque slug du bundle ET le silence sur un slug tiers.
- Libs externes du snippet : `cdn.jsdelivr.net` ou `unpkg.com` — jamais `cdnjs.cloudflare.com` (bloqué par la CSP du site).

## Composant interactif — OBLIGATOIRE sur chaque paire

**Règle figée (sept. 2026).** Le composant interactif n'est pas une option d'enrichissement. Chaque paire de pages livrée en porte **un**, propre à la page, monté par le snippet, servi dans les deux langues.

La raison n'est pas décorative : c'est le seul élément de la page qu'un lecteur ne consomme pas en une lecture. C'est ce qui lui donne une raison de revenir, et ce qu'un résumé de LLM ne réplique pas. Une page dont tout le contenu tient dans un paragraphe de synthèse est une page que l'agrégateur remplace.

### La barre de qualité — quatre tests

Un composant qui échoue à l'un de ces tests **ne compte pas comme livré**. Le corriger ou changer de mécanisme, jamais le livrer faible : un graphe de remplissage coûte la confiance qu'il devait construire.

1. **Il tranche une question que le texte ne peut pas trancher.** Le lecteur arrive avec SA valeur — son pays, sa date, son seuil, sa fenêtre — et la page ne peut pas les énumérer toutes. Un composant qui rejoue une figure déjà commentée dans le texte est un PNG animé : il tombe.
2. **Il repose sur de la donnée vérifiée.** Mêmes chiffres que la page, l'audit, le visuel et le CSV. Aucune série qui n'a pas passé l'audit factuel n'entre dans un composant : pas d'interpolation pour boucher un trou, pas de série d'appoint récupérée après coup pour « nourrir » le graphe.
3. **Il tient debout seul et augmente le texte.** Compréhensible sans avoir lu la page — un lecteur peut en envoyer le lien à un collègue — tout en répondant à la thèse de la page, jamais à côté d'elle.
4. **Il n'est pas le clone du précédent.** Le mécanisme suit la question, pas l'habitude. Deux pages de suite sur le même mécanisme (même curseur temporel, même toggle de séries) → en changer. Le mécanisme retenu se consigne dans la mémoire du projet, en le nommant par son mécanisme et non par son sujet — « curseur d'année + recalcul en dollars constants », pas « faillites bancaires ».

### La seule exception

La page **outil / simulateur** *est* déjà le composant. Ne pas en empiler un second.

### Motif d'omission non recevable

« La page n'a pas de série à explorer » ne justifie pas l'omission au moment du bundle. Une page sans rien à explorer n'avait pas de quoi franchir le cadrage en amont — cela se dit au brief, pas à la livraison. Si le sujet est réel mais la donnée trop maigre pour un composant honnête, c'est un arbitrage à remonter à l'utilisateur **avant** de rédiger, jamais une omission silencieuse.

### Décider tôt

Le mécanisme s'arbitre **avant** de rédiger, à l'étape 2 de l'ordre de production, en même temps que le degré bilingue. Décidé après, il illustre au lieu de trancher, et il arrive trop tard pour orienter les séries à récupérer et le placement du visuel statique.

### Deux modes de montage (le MÊME snippet les porte)

Un seul bloc snippet dans le bundle : il porte le hook `wp_head` (JSON-LD) **et** le composant.

1. **Injection `wp_footer` sur placeholder (DÉFAUT pour les pages assemblées en bloc Custom HTML** — every-x, études au bloc autoportant) : le bloc HTML de la page contient un simple `<div id="…"></div>` ; le snippet ajoute un hook `wp_footer` **guardé par les MÊMES slugs** qui injecte les données (`window.<data>` + variable de langue selon le slug) puis le JS qui se monte sur le placeholder. Avantages : le bloc HTML reste 100 % sans script ; pas de shortcode à enregistrer ; si le JS échoue, le div vide est invisible (dégradation propre). Le champ `shortcode` du bundle est alors **OMIS**.
2. **Shortcode** : quand le composant doit être positionné via un bloc shortcode Gutenberg (pattern simulateurs, ou insertion au milieu d'un contenu non monolithique). Le même snippet enregistre le shortcode ; le champ `shortcode` du bundle est renseigné.

### Contraintes de forme

- **JS vanilla de préférence** (canvas dessiné main, aucune lib) ; si lib nécessaire → jsdelivr/unpkg uniquement, jamais cdnjs (CSP) ; `node --check` sur le JS avant livraison.
- **Libellés ET données localisés par langue.** La variable de langue du hook sélectionne les deux : en adaptation forte, le composant peut servir deux jeux de données distincts, comme il sert déjà deux jeux de libellés. **Zéro chaîne EN résiduelle côté FR** — contrôle sur la table de libellés, pas à l'œil.
- **Couleurs, typo, densité** : `brand-kit-eco3min`, comme n'importe quel visuel Eco3min.
- **AMF** : le composant est soumis aux mêmes règles que le texte (cf. `editeur-eco3min`). Aucune zone prescriptive, aucune flèche directionnelle, aucune trajectoire prospective unique. Un curseur qui laisse le lecteur explorer des scénarios est acceptable ; un curseur qui affiche « objectif », « cible » ou « niveau à atteindre » ne l'est pas.
- **Accessibilité minimale** : le composant reste lisible sans interaction (état par défaut porteur de sens) et ne dépend pas du survol seul sur mobile.
- **Le rendu du composant se vérifie, il ne se déduit pas du DOM (19/09/2026, S022).** Un contrôle par `read_page` /
  `javascript_tool` qui lit les valeurs, les tailles et l'absence de débordement prouve que le composant *fonctionne*, pas
  qu'il *s'affiche* : les barres de l'effet de base sont parties en ligne avec un `background` transparent parce que les
  variables CSS (`--e3u-*`) étaient déclarées sur la racine du panneau (`.eco3-usrel`) et pas sur celle du composant
  (`.eco3-usrel-app`), et rien ne l'a vu. Deux règles : (1) **les tokens CSS d'un snippet se déclarent sur chaque racine
  montée** (panneau, composant, shortcode), ou sur un sélecteur commun listant toutes ces racines, jamais sur une seule ;
  (2) avant livraison, sur l'aperçu local, **asserter les styles calculés des éléments qui portent l'encodage visuel**
  (`getComputedStyle(...).backgroundColor` des barres, `color` des libellés, `stroke` / `fill` d'un SVG) : aucun ne vaut
  `rgba(0, 0, 0, 0)` ni la couleur héritée du thème, et chaque `var(--…)` utilisé par le CSS du composant est résolu
  sur sa racine (`getComputedStyle(root).getPropertyValue('--token')` non vide). Une capture d'écran du composant à
  largeur desktop et à 375 px est prise quand l'outil le permet ; quand il échoue (fenêtre masquée, timeout), c'est
  l'assertion sur les styles calculés qui fait foi, pas une lecture textuelle.

## Le slug de page ne doit JAMAIS être le nom de base d'un asset (BLOQUANT)

**C'est le piège le plus coûteux de cette couche, et il ne ressemble pas à un
problème de slug : il ressemble à un import raté.**

`wp_unique_post_slug()` vérifie, pour un type de contenu hiérarchique,
`post_type IN ('page', 'attachment')`. **Une pièce jointe occupe donc l'espace de
noms des slugs de page.** Conséquence directe :

- `mon-sujet.csv` uploadé → slug d'attachment `mon-sujet`
- `mon-sujet.xlsx` uploadé → slug d'attachment `mon-sujet-2`
- la page importée ensuite ne peut plus obtenir que **`mon-sujet-3`**

**Et là le vrai dégât commence.** La garde du snippet compare le `post_name`
**exact**. Un slug suffixé, et la page perd d'un coup le CSS scopé, le JSON-LD,
l'Open Graph et le composant interactif : elle s'affiche en styles de thème nus.
Le canonical du bundle, le `@id` du JSON-LD, l'`og:url` et l'encart de citation
pointent tous vers une URL qui n'existe pas. Rien dans l'import ne signale
l'erreur — le plugin rapporte un succès.

**Ce n'est pas théorique** : trois études de la Factory sont parties comme ça,
suffixées côté EN uniquement, parce que le slug FR diffère du nom des fichiers,
qui portent le nom anglais. Le symptôme rapporté était « l'import capote à chaque
fois » alors que l'import réussissait.

### Les deux règles, l'une ou l'autre suffit

1. **Nom de base des assets ≠ slug de page.** La règle par défaut : le slug de
   page porte le mot-clé natif, les assets portent un préfixe distinct. Écrire
   les deux comme deux constantes séparées dans le script de build, jamais dériver
   l'une de l'autre.
2. **Importer le bundle AVANT d'uploader le CSV et le XLSX.** La page prend son
   slug propre, les pièces jointes se rangent derrière.

### Assertion à poser dans le build du bundle

```python
assert page_slug != asset_base, (
    'le slug de page est le nom de base des assets : le CSV le volera')
```

### Diagnostic en une ligne sur une page déjà publiée

```bash
curl -sS "https://eco3min.fr/en/<slug>/" | grep -c 'eco3-<study>-css'
```

`0` alors que la page existe = la garde ne matche pas = le slug porte un suffixe.
Comparer avec la page de l'autre langue : si elle rend `1`, le snippet est bon et
seul le slug est en cause.

### Réparation

Renommer les slugs des deux médias, puis le slug de la page, puis purger le
cache. **Renommer le slug d'un média ne touche pas l'URL du fichier**, donc aucun
contenu n'est à modifier, aucun ré-upload n'est nécessaire. Si le renommage n'est
pas possible, réimporter avec un **nouveau slug de page** et propager partout :
garde du snippet, canonical, `@id` et `url` du JSON-LD, `og:url`, encart de
citation, package social.

⚠️ Les abilities MCP `ewpa/update-post` acceptent l'appel et renvoient un succès
mais **n'écrivent ni `slug` ni `post_name`** : le renommage passe par wp-admin.

### Corollaire sur le watermark des visuels

Un watermark qui contient l'URL complète de la page est **cuit dans le PNG**. Un
changement de slug le rend faux et impose de re-rendre et de ré-uploader toute la
série. Le watermark porte le domaine, pas le chemin.

---

## Nommage canonique des fichiers (BLOQUANT)
Le bug du 404 vient toujours d'un nom de fichier différent — ou d'un dossier de date faux — entre ce qu'on uploade et ce que l'article référence.

- **Image** : choisir un nom de fichier et l'utiliser à l'identique partout DANS UNE MÊME PAGE — `src` de la `<figure>`, `seo.og_image`, `pages.{en,fr}.featured_image`, et le champ `image` du JSON-LD correspondant. (Un hero localisé EN vs FR est admis, et il est même attendu dès que le visuel porte du texte : chaque page reste cohérente en interne.)
- **CSV** : nom identique entre le fichier uploadé, le lien de téléchargement dans les DEUX pages, et le JSON-LD Dataset (`distribution.contentUrl`) le cas échéant. En adaptation forte avec données distinctes, deux CSV distincts, chacun cohérent avec sa page.
- **URL d'upload = année/mois EN COURS (BLOQUANT).** Les URLs des assets suivent le format `https://eco3min.fr/wp-content/uploads/AAAA/MM/<fichier>`, où **AAAA = année en cours** et **MM = mois en cours au moment où le bundle est produit** — WordPress range les médias dans un dossier daté par mois d'upload. **Ne JAMAIS coder en dur un mois/année passés ou devinés** : au moment d'écrire le bundle, prendre la date du jour. Exemple : en **juillet 2026 → `.../uploads/2026/07/<fichier>`**. Cette même URL (base identique) doit apparaître à l'identique dans le `src` de la `<figure>`, `seo.og_image`, `pages.{en,fr}.featured_image`, le champ `image` du JSON-LD et `distribution.contentUrl`. Une seule chaîne de base → un seul find-replace si l'upload réel diffère. Un mois faux → featured image absente et image/CSV en 404 sur la page publiée. **Cas révision d'une page déjà publiée** : si des assets INCHANGÉS restent en médiathèque dans leur dossier d'origine (sans ré-upload), leurs URLs existantes peuvent être conservées ; tout asset ré-uploadé ou nouveau prend le mois en cours. Décision explicite, jamais implicite — et signalée à l'utilisateur.
- Le PNG doit être **uploadé dans la Médiathèque WordPress avant l'import** : le plugin récupère le `featured_image` par URL. URL vers un fichier absent → pas de featured image.

## Placement de l'image statique
- **Si le composant interactif EST le hero de la page** (il ouvre la page, mode shortcode typiquement) : le PNG statique va **AU MILIEU de l'article** (après la première grande section), jamais juste sous le chart interactif. La featured image WP reste le PNG.
- **Si le composant interactif est secondaire** (hero PNG autoportant en tête, chart interactif plus bas — pattern every-x) : le hero PNG reste en tête, le composant se place où l'éditorial le dicte (typiquement après le tableau/record qu'il permet d'explorer).
- **Page outil / simulateur** (seul cas sans composant supplémentaire, le simulateur en tenant lieu) : placement normal du/des visuel(s) selon l'éditorial.
- **Contrainte conservée dans tous les cas** : **jamais le PNG statique immédiatement adjacent au composant interactif** (doublon visuel).

## Marqueur de fraîcheur `e3m-review` — OBLIGATOIRE sur toute page périssable (18/09/2026)

Une page est **périssable** dès qu'un événement daté ou prévisible rendra faux un fait qu'elle
affirme : montant ou taux « en vigueur », date d'une prochaine échéance, compte à rebours,
calendrier millésimé, dernière observation d'une série citée dans la prose ou le hero, registre
« Every X since Y » qu'un nouvel événement allongera, projection recalculée chaque mois. La
quasi-totalité des pages `tool`, des calendriers, des pages vivantes et des registres le sont ;
une étude ou un article dont les chiffres sont historiques et datés dans le texte ne l'est pas.

**La décision se prend au cadrage, avec le composant et le degré bilingue, et se livre dans le
bundle** : le `content` de chaque page périssable **commence** par le marqueur, avant le chapeau,
dans chaque langue de la paire (une page EN et sa jumelle FR peuvent avoir des échéances
différentes : deux marqueurs, un par page).

```
<!--e3m-review due="2026-10-15" lead="7" do="Chaque mi-mois : ajouter le dernier IPC (Insee, serie 011818264) dans ipc.obs de eco3min_smic_data() du snippet 271 ; si le cumul atteint 2 %, attendre le decret puis mettre a jour smic.* et ipc.ref_* ; reposer due sur la publication Insee suivante."-->
```

Règles :

- `due` = **la date du prochain événement qui périme la page** (publication de la source,
  décision, échéance légale), jamais une durée de confort. Aucune ancre identifiable → +6 mois,
  et le dire au recap.
- `lead` = le temps qu'exige le travail, pas une marge de politesse : 7 si c'est un patch de
  snippet ; 21 par défaut ; 30 si l'action dépend d'un tiers ou impose de régénérer un hero.
- `do` = la **spécification du travail**, lisible dans six mois par quelqu'un qui n'a pas produit
  la page : quelle source, quelle fonction et quelles clés du snippet, quels chiffres de la
  prose et du hero à vérifier, comment reposer `due`. Jamais « mettre à jour ».
- Guillemets **droits** `"` uniquement ; dans `do`, aucun `"`, aucun `<`, `>`, `-->`, aucun
  `&entity;`. Le snippet 226 ne lit que le **premier** marqueur d'une page (`preg_match`) et
  une date invalide fait disparaître la page de l'écran admin **en silence**.
- Un seul marqueur par page. Sur une page déjà publiée, il se pose par `eco3min/update-content`
  en patch byte-exact devant le premier bloc, jamais par une meta : les metas `_e3m_review_*`
  sont projetées à `save_post`, elles se lisent, elles ne s'écrivent pas.
- Vérification après import : `_e3m_review_due` de la page porte la date du marqueur (preuve que
  le moniteur l'a vu passer), et la page répond `200 200` avec et sans `ao_noptimize=1`.

Mécanisme complet (snippet 226, metas, états `overdue`/`soon`/`ok`, écran
`tools.php?page=e3m-review`) : `plugins-eco3min`, `references/07-code-snippets-pieges.md`.
Traitement des échéances : projet « Eco3min Keep Content Fresh ». Ce skill ne dit qu'une chose
qu'eux ne disent pas : **le marqueur se pose à la naissance de la page, pas quand elle est déjà
périmée.**

## Slugs et parentage (via archi-eco3min — JAMAIS inventer un slug)
- **EN** : slug nu, servi sous `/en/` via Polylang en mode répertoire (ex. `slug` → `/en/slug/`).
- **FR** : slug plat à la racine (ex. `/slug-fr/`).
- **Parentage optionnel** : `parent_slug` d'une page existante (pour l'EN, la parente doit être sous `/en/`). Ne jamais inventer un slug de parent.
- Le garde-fou du snippet doit lister exactement les slugs des pages du bundle — sur `wp_head` **et** sur `wp_footer`.

## Conformité AMF (via editeur-eco3min)
Média analytique non prescriptif. Pas de `should/must/buy/sell/allocate/target`, pas d'allocation chiffrée par classe d'actifs, pas de trajectoire prospective unique présentée comme certaine, pas de conseil personnalisé. Les six règles AMF s'appliquent aux deux langues, **au texte des FAQPage et au composant interactif** (libellés, légendes, états par défaut), quel que soit le degré d'adaptation.

## Le plugin « Eco3min Import → Page bilingue » (cible de l'import)
- crée/maj le Code Snippet (OBLIGATOIRE ici) — idempotent par nom, balise `<?php` de tête retirée, scope global, activé. C'est ce snippet qui émet le JSON-LD au wp_head et monte le composant au wp_footer.
- crée/maj les 2 pages EN/FR en `post_type=page` : `wp_insert/update_post`, langue Polylang + lien de traduction, metas RankMath (EN+FR), featured image sideloadée, parent optionnel. Le plugin n'injecte plus de JSON-LD depuis les pages (plus de champ `json_ld`).
- hubs → rien.
- **Page dans une seule langue (FR seule ou EN seule) : même bundle, un seul bloc dans `pages{}`.** Vérifié dans `eco3min-import.php` le 18/09/2026 (`isset($b['pages']['en']) ? … : 0`) : l'autre langue est optionnelle, `link_translations` est ignoré avec un avertissement. Le schéma ci-dessous montre les deux blocs parce que la paire est le cas courant, pas parce qu'elle est exigée. **Jamais de création par abilities MCP** (`ewpa/create-page`, `eco3min/snippet-create`, `set-metas`, `set-seo`) pour contourner : le bundle pose slug, langue, metas eco3min, SEO, image à la une et snippet en une passe, rejouable (leçon S020, 18/09/2026 : page 43487 créée par abilities, sans slug ni image, faute d'avoir ouvert le code du plugin).
- **Metas eco3min : depuis Eco3min Import 2.3.0 (17/09/2026), le bundle DOIT porter un bloc `eco3min`** par page (`pages.en.eco3min` / `pages.fr.eco3min`) ou au niveau du bundle (`eco3min.en` / `eco3min.fr`) : `{"level": "...", "cluster": "<slug PILIER de la langue>", "sub_pilier": "<slug PAGE sous-pilier de la langue>", "parent_major": <post_id>}` (valeurs tirées d'`archi-eco3min` ; `overwrite: true` seulement pour corriger une page existante, sinon fill-only ; backups `_e3i_bak_eco3min_*`, ID sous-pilier dérivé). Sans ce bloc — et sous 2.2.1 en live, qui l'ignore — la page reste sans level, donc **invisible au conseil de maillage du mega**, qui ne traite que `pillar` / `sub_pillar` / `major_article` / `satellite` ; le rattrapage relève alors de `metas-eco3min` (sous-page « MAJ metas » ou `eco3min/set-metas`), dans l'ordre : level → cluster et sous-pilier → `parent_major`. Tenter `parent_major` avant la classification produit une erreur « satellite introuvable ».

Garde-fous du plugin : Preview (dry run) / Apply, source JSON `upload → textarea → fichier serveur` (`wp-content/uploads/eco3min-import/bilingual-page.json`), idempotence (meta UID + fallback slug+langue), avertissement si un bloc `hubs` est présent.

## Import à distance — `wp_push.py` + `eco3min/import-bundle` (19/09/2026, voie par défaut)
Depuis `eco3min-mcp` 1.3.0 l'import ne passe plus par wp-admin. Quatre appels, dans cet ordre, **tous exécutés par Claude** ; Paul ne fait que vérifier la page en ligne à la fin :

0. **OK de Paul sur chaque visuel** (hero, chart) montré par SendUserFile — bloquant, règle de `visuels-eco3min` §9 ; sans cet OK, aucun des appels suivants.
1. `py -3.14 eco3min-projets/tools/wp_push.py <dossier>/import.json <PNG> <CSV…> --check` — gardes locales (JSON valide ; chaque asset référencé dans le bundle sous `uploads/AAAA/MM/` du mois courant ; aucun nom de base d'asset égal à un slug de page) puis contrôle serveur des collisions de nom en médiathèque, **rien n'est écrit**. Une collision = renommer l'asset ET son URL dans le bundle, jamais laisser WordPress suffixer.
2. Même commande sans `--check` — bundle déposé dans `uploads/eco3min-import/<name>.json` (`name` déduit de l'`import_type` : `bilingual-page`), assets enregistrés en médiathèque dans `uploads/AAAA/MM/` du mois courant. Le rapport donne l'URL réelle de chaque asset : elle doit être identique à celle du bundle.
3. Ability `eco3min/import-bundle` `{"mode": "bilingual", "dry_run": true}` — lire le log du plugin (`errors` doit valoir 0 ; le `[dry] CRÉATION` doit porter le slug prévu, un `MAJ` inattendu signale une collision d'UID ou de slug).
4. `{"mode": "bilingual", "dry_run": false}` — `pages[]` renvoie post_id, slug réel, statut, URL, id de l'image à la une. Le bundle est archivé côté serveur. Donner les URL à Paul pour vérification visuelle, puis enchaîner le post-import (backlog, assets_sync, metas).

Règles :
- **Le bundle ne transite jamais par le MCP** (40-60 Ko = 12-20k tokens de sortie déjà dépensés pour l'écrire) : `import-bundle` ne prend qu'un nom de fichier. Jamais de `content` inline dans une ability, jamais `ewpa/create-page` / `eco3min/create-pair` pour une page produite par un skill de contenu.
- **`status: "publish"` dans le bundle** (décision du 19/09/2026 : publication directe, Paul vérifie la page en ligne ; le plugin met `draft` si le champ manque). Le `dry_run` de l'étape 3 reste obligatoire — c'est la seule garde avant que la page soit servie et dans le sitemap.
- Identifiants dans `~/.config/eco3min/wp_push.env` (hors git). Route absente (404) ou 401 = plugin `eco3min-mcp` < 1.3.0 ou mot de passe d'application invalide : le dire à Paul, ne pas contourner.
- Repli si la route est indisponible : la sous-page wp-admin « Page bilingue » (Preview puis Apply) — c'est le même code, `e3i_run_bilingual()`.

## Schéma du bundle JSON
Réponse = rien d'autre que le JSON dans un bloc de code.

```jsonc
{
  "schema_version": "1.0",
  "import_type": "bilingual_page",
  "item": {
    "id": "slug-stable-de-l-item",       // id stable (logs/idempotence), libre
    "label": "Libellé humain"
  },
  "snippet": {                            // OBLIGATOIRE — JSON-LD des 2 pages + composant interactif
    "name": "Eco3min — {slug} JSON-LD",   // UNIQUE par étude (idempotence par nom)
    "description": "...",
    "scope": "global",
    "shortcode": "[eco3min_xxx]",         // OPTIONNEL : seulement si le composant est monté par SHORTCODE (omis en mode wp_footer/placeholder)
    "code": "...(PHP SANS balise <?php ; hook wp_head guardé par slug ; JSON-LD EN+FR en base64 ; + composant interactif OBLIGATOIRE : wp_footer guardé ou shortcode)..."
  },
  "pages": {
    "en": {
      "lang": "en",
      "post_type": "page",
      "status": "publish",                // publication directe (19/09/2026) ; "draft" seulement sur demande explicite
      "slug": "slug-en",                  // servi sous /en/ via Polylang
      "parent_slug": null,                // OPTIONNEL : slug d'une page parente existante
      "title": "H1 / post_title EN",
      "content": "...(HTML Gutenberg complet ; AUCUN JSON-LD ici ; AUCUN <script> ; AUCUN commentaire HTML ; <div> placeholder du composant si mode wp_footer ; placement du PNG selon la section dédiée)...",
      "featured_image": "https://eco3min.fr/wp-content/uploads/AAAA/MM/<fichier>.png",  // AAAA/MM = année/mois EN COURS
      "seo": {                            // OBLIGATOIRE
        "title": "≤60 car.",
        "description": "150-160 car.",
        "focus_keyword": "...",
        "canonical": "https://eco3min.fr/en/slug-en/",
        "og_title": "...",
        "og_description": "...",
        "og_image": "= featured_image de CETTE page (strictement identique)",
        "og_image_alt": "...",
        "robots": ["index", "follow"]
      }
      // PAS de champ "json_ld" — les données structurées sont dans le snippet
    },
    "fr": {
      "lang": "fr",
      "post_type": "page",
      "status": "publish",
      "slug": "slug-fr",                  // plat à la racine ; mot-clé natif, pas la traduction du slug EN
      "parent_slug": null,
      "title": "H1 / post_title FR",
      "content": "...(HTML Gutenberg FR ; AUCUN JSON-LD ici ; AUCUN <script> ; AUCUN commentaire HTML ; <div> placeholder du composant si mode wp_footer)...",
      "featured_image": "...",            // hero localisé attendu si le visuel porte du texte ; même AAAA/MM en cours
      "seo": { /* OBLIGATOIRE ; rédigé nativement ; canonical = https://eco3min.fr/slug-fr/ */ }
      // PAS de champ "json_ld"
    }
  },
  "polylang": { "link_translations": true }
  // PAS de bloc "hubs"
}
```

### Règles bloquantes du bundle
- `post_type` = `"page"` pour les deux langues (jamais `post`).
- Aucun bloc `hubs`.
- `snippet` OBLIGATOIRE, portant le JSON-LD des deux pages, guardé par slug (`is_singular('page')` + `post_name` ∈ slugs du bundle) ; code ne commence jamais par `<?php` ; nom de snippet unique par étude.
- Données structurées UNIQUEMENT dans le snippet : aucun `<script type="application/ld+json">` dans `content`, aucun champ `json_ld` dans les pages (sinon double émission).
- **Composant interactif OBLIGATOIRE** (seule exception : page outil/simulateur, qui en tient lieu), conforme aux quatre tests de la barre de qualité. Porté par le MÊME snippet — mode `wp_footer`/placeholder (défaut, champ `shortcode` OMIS) ou mode shortcode (champ `shortcode` renseigné). Le hook `wp_footer` est guardé sur les mêmes slugs que le `wp_head`. Placeholder `<div>` présent dans le `content` des **deux** langues en mode wp_footer.
- Libellés et données du composant localisés par langue ; aucune chaîne résiduelle de l'autre langue.
- `seo` OBLIGATOIRE dans les DEUX langues (title, description, focus_keyword, canonical, OG), rédigé nativement par langue.
- Slug FR ≠ slug EN, chacun sur le mot-clé natif de sa langue.
- **Slug de page ≠ nom de base des assets** (CSV, XLSX, PNG) : une pièce jointe occupe l'espace de noms des slugs de page et volerait celui de la page, ce qui casserait silencieusement la garde du snippet. Cf. section dédiée.
- **Degré d'adaptation de la seconde langue arbitré et documenté** ; faits communs identiques au chiffre près entre les deux versions.
- JSON-LD en base64 dans le code (recommandé fort) pour éviter tout problème d'échappement.
- Le nom d'image dans `featured_image`, le `src` de la `<figure>`, `seo.og_image` et le champ `image` du JSON-LD d'une même page sont strictement identiques.
- **URLs des assets (image, CSV) au format `uploads/AAAA/MM/` avec AAAA/MM = année et mois EN COURS à la production** (jamais un mois passé ou deviné ; exception explicite et signalée : assets inchangés déjà en médiathèque lors d'une révision) ; base identique entre HTML, `featured_image`, `og_image`, champ `image` du JSON-LD et `distribution.contentUrl`.
- CSV : nom identique entre fichier, liens de téléchargement EN+FR, et JSON-LD Dataset.
- Libs externes (snippet) depuis jsdelivr/unpkg, jamais cdnjs.
- **Aucun commentaire HTML dans `content`** (cf. règle figée en fin de fichier).
- Cohérence des chiffres : valeurs identiques entre page EN, page FR, audit, composant, visuel, CSV, JSON-LD.


## Checklist pré-import (à adapter)
- [ ] **Degré d'adaptation bilingue arbitré AVANT rédaction de la 2e langue, annoncé et justifié en une phrase**
- [ ] **Composant interactif : question tranchée et mécanisme annoncés AVANT rédaction ; quatre tests de la barre de qualité passés ; mécanisme ≠ celui de la page précédente, consigné dans la mémoire du projet**
- [ ] Page de la langue forte produite (HTML Gutenberg), placement de l'image statique conforme, PNG non adjacent au composant ; aucun JSON-LD dans le HTML ; aucun `<script>` dans le HTML ; **aucun commentaire HTML**
- [ ] Audit `fact_check_audit.md` livré, zéro 🔴 résiduel (si la page a des chiffres) ; **les séries du composant y figurent** ; en adaptation forte, les données propres à la 2e version ont leur section d'audit
- [ ] Seconde page produite au degré retenu ; faits communs identiques au chiffre près ; aucun chiffre « équivalent » fabriqué
- [ ] Slugs distincts, chacun sur le mot-clé natif de sa langue
- [ ] **Aucun slug de page n'est le nom de base d'un asset** (garde locale de `wp_push.py`, bloquante) ; en voie wp-admin, bundle importé AVANT l'upload du CSV et du XLSX ; après import, vérifier qu'aucun slug ne porte de suffixe numérique — et si un suffixe est apparu malgré tout, relire le `canonical_url` RankMath : il porte le slug PRÉVU, donc pointe vers une URL qui redirige (vers la page elle-même, ou vers l'accueil), et RankMath sort la page du sitemap ; 3 pages trouvées ainsi le 19/09/2026 (39572, 42654, 42646), corrigées par `eco3min/set-seo canonical_url` = URL réelle, puis un « Mettre à jour » wp-admin pour régénérer le sitemap
- [ ] Snippet OBLIGATOIRE : JSON-LD EN+FR (base64), hook wp_head guardé par slug, code sans `<?php`, nom unique ; composant interactif porté par le même snippet (wp_footer guardé = défaut / shortcode si placement Gutenberg) ; round-trip base64 vérifié ; `node --check` sur le JS
- [ ] Composant : `<div>` placeholder présent dans les DEUX pages (mode wp_footer) ; libellés et données localisés, zéro chaîne EN résiduelle côté FR ; libs jsdelivr/unpkg ; couleurs et typo `brand-kit-eco3min` ; état par défaut porteur de sens ; au moins un chiffre pivot vérifié identique à la page, l'audit et le CSV
- [ ] **Rendu du composant vérifié sur l'aperçu, pas déduit du DOM** : styles calculés des éléments porteurs de l'encodage visuel non transparents, variables CSS résolues sur chaque racine montée (panneau ET composant), capture desktop + 375 px si l'outil le permet
- [ ] FAQ JSON-LD = FAQ visible dans chaque langue (FR vérifiée contre la page FR réelle si elle préexiste)
- [ ] Metas SEO RankMath en EN ET FR (title ≤60, desc 150-160, focus, canonical, OG), rédigées nativement
- [ ] Aucun champ `json_ld` dans les pages du bundle
- [ ] Image : nom de fichier identique dans figure src / og_image / json_ld image / featured_image (par page) ; PNG uploadé dans la Médiathèque ; hero localisé si le visuel porte du texte
- [ ] **URLs image/CSV au format `uploads/AAAA/MM/` avec l'année et le mois EN COURS (pas un mois passé/deviné ; exception révision signalée) ; base identique partout (figure, og_image, featured_image, JSON-LD image, contentUrl)**
- [ ] CSV (si présent) : nom identique entre fichier, liens EN+FR, et JSON-LD Dataset
- [ ] Slugs vérifiés (EN nu sous /en/, FR plat) ; `parent_slug` existant si renseigné — jamais inventé ; garde-fou du snippet = ces slugs exacts (wp_head ET wp_footer)
- [ ] AMF : pas de prescription, pas d'allocation chiffrée, pas de trajectoire unique certaine (EN + FR + texte FAQPage + libellés du composant)
- [ ] `import_type: "bilingual_page"`, `post_type: "page"`, pas de bloc `hubs`
- [ ] Bundle généré 
- [ ] Visuels (hero, chart) montrés à Paul, OK explicite reçu AVANT le premier `wp_push.py`
- [ ] Import : `wp_push.py … --check` → `wp_push.py …` → `eco3min/import-bundle` dry_run → apply (section « Import à distance ») ; `status: "publish"` dans le bundle ; URL des pages données à Paul pour vérification
- [ ] **Post-import prévu** : classer le level, poser cluster et sous-pilier, puis `parent_major` — sinon la page reste invisible au conseil de maillage (cf. `metas-eco3min`)
- [ ] **Post-import, liens vers uploads/ vérifiés par l'index (19/09/2026)** : `py -3.14 eco3min-projets/tools/assets_sync.py` puis `grep http_404 context/assets-inventaire.csv | grep -E '(,|;)<post_id>(;|,)'` doit être vide pour les deux post_id de la paire. Attrape le fichier que WordPress a renommé avec un suffixe (`-1`, `-4`…) parce que le nom était déjà pris, et le `-v2` jamais uploadé — dans les deux cas l'URL écrite dans la page et le JSON-LD est morte (incident crack spread, 404 du 12/07 au 19/09/2026). Si le fichier est un dataset pipeline, le lien doit viser `/dataset/…`, jamais une copie dans uploads/.
- [ ] **Page périssable → marqueur `<!--e3m-review due lead do-->` en tête du `content` de chaque page**, `due` = prochain événement qui la périme, `do` = spécification du travail (source, snippet, fonction, clés, chiffres à vérifier) ; guillemets droits, aucun `<` `>` `"` dans `do` ; après import, `_e3m_review_due` porte la date

## Anti-patterns — ne JAMAIS faire
- **Traduire la seconde langue par défaut, sans avoir arbitré le degré d'adaptation** — ou le trancher après l'avoir rédigée.
- **Réécrire intégralement par défaut** « pour faire natif » quand une adaptation légère suffisait : deux pages qui divergent sans raison doublent le coût d'audit et se concurrencent.
- Publier une seconde page pour la seule symétrie, sur un sujet sans lecteur dans cette langue, sans réancrage.
- Laisser diverger un chiffre commun aux deux versions, ou fabriquer un chiffre « équivalent » non sourçable.
- **Livrer une paire sans composant interactif**, ou l'omettre au motif que « la page n'a pas de série » — cela se dit au cadrage, pas au moment du bundle.
- **Livrer un composant qui rejoue une figure déjà commentée dans le texte** (PNG animé) : il échoue au test 1.
- Tirer une série hors audit pour « nourrir » le composant, ou interpoler pour boucher un trou.
- Décider du mécanisme du composant après avoir rédigé les deux pages.
- Reprendre le mécanisme d'interaction de la page précédente par habitude.
- Empiler un second composant sur une page outil / simulateur, qui en tient déjà lieu.
- Laisser des libellés ou des données non localisés côté FR dans le composant.
- Mettre le JSON-LD dans le HTML de la page (`<script ld+json>` dans `content`) ou dans un champ `json_ld` du bundle → doit être dans le snippet, sinon doublon `<head>`.
- Livrer un bundle sans snippet, ou un snippet sans garde-fou par slug (fuite du JSON-LD — ou du JS du composant — sur tout le site) ; le garde-fou s'applique à CHAQUE hook du snippet (wp_head ET wp_footer).
- Réutiliser le même nom de snippet entre deux études (surcharge par idempotence).
- Omettre les metas SEO dans une des deux langues, ou les traduire littéralement.
- Faire commencer le code du snippet par `<?php`.
- Embarquer le JSON-LD en clair dans le PHP au lieu du base64 (casse silencieuse par échappement).
- Mettre un `<script>` dans le `content` d'une page pour monter le composant interactif → il vit dans le snippet (wp_footer/placeholder ou shortcode).
- Exiger un shortcode quand le montage wp_footer/placeholder suffit (page en bloc Custom HTML) — ou l'inverse : injecter au wp_footer un composant qui doit être positionné via bloc Gutenberg.
- Zone prescriptive, flèche directionnelle, « cible » ou « objectif » dans le composant (AMF).
- Importer en post/article au lieu de page ; produire un bloc `hubs`.
- Référencer un nom d'image/CSV différent entre le fichier uploadé et la page → 404.
- **Coder en dur un mois/année d'upload passés ou devinés dans les URLs d'assets au lieu du mois EN COURS → featured image absente, image/CSV en 404.**
- **Donner à un asset le nom de base du slug de la page** : la pièce jointe vole le slug, la page part en `-2` ou `-3`, et le snippet cesse d'émettre sans un mot d'erreur. Trois études de la Factory sont parties comme ça.
- Mettre l'URL complète de la page dans le watermark d'un visuel : elle est cuite dans le PNG et un changement de slug oblige à re-rendre toute la série.
- Placer le PNG statique juste sous le composant interactif (dans tous les modes de montage).
- Charger une lib du snippet depuis `cdnjs.cloudflare.com` (CSP) — utiliser jsdelivr/unpkg.
- Inventer un slug ou un `parent_slug`.
- Rédiger le contenu de fond dans ce skill au lieu de le déléguer au skill de contenu approprié.
- Livrer le bundle avec un 🔴 résiduel non résolu.
- Considérer le chantier terminé à l'import : sans le rattrapage des metas eco3min, la page reste `uncategorized` et hors du conseil de maillage.

## Versioning
- **v1.0** — création (snippet base64 par slug, règle AAAA/MM, bundle bilingual_page).
- **v1.1 (juil. 2026, page inflation waves)** — composant interactif généralisé en deux modes de montage portés par le même snippet : injection `wp_footer` guardée par slug sur div placeholder (DÉFAUT pour pages en bloc Custom HTML, champ `shortcode` omis) vs shortcode (placement Gutenberg) ; « Placement de l'image statique » conditionné (interactif-hero vs interactif-secondaire, contrainte anti-adjacence conservée) ; exception explicite AAAA/MM pour assets inchangés en révision de page publiée ; vérifs recommandées (round-trip base64, `php -l` + stubs, node --check, FAQ FR alignée sur la page FR réelle). Aucune règle v1.0 supprimée.
- **v1.2 (sept. 2026)** — **la seconde langue n'est plus une traduction par défaut.** La règle « Page FR = traduction idiomatique de l'EN audité » est REMPLACÉE par la section « Décision bilingue » : trois degrés (miroir / adaptation légère / adaptation forte), arbitrés par Claude avant rédaction sur trois critères (demande observée par langue, disponibilité de la donnée dans le marché cible, coût du faux), annoncés et documentés. Motif : le miroir par défaut produisait des pages mortes sur les sujets sans public dans une des deux langues, et contredisait la doctrine bilingue portée par les fichiers de rédaction du projet Writer. Invariants ajoutés : écriture native quel que soit le degré, faits communs identiques au chiffre près, audit propre aux données de la version adaptée, slugs et metas natifs par langue. Ajouts secondaires : mention explicite que le plugin ne pose aucune meta eco3min et que le rattrapage post-import relève de `metas-eco3min` (avec son ordre d'opérations) ; hero localisé attendu dès que le visuel porte du texte ; « zéro commentaire HTML » remonté dans les règles bloquantes du bundle et la checklist. Aucune règle v1.0/v1.1 supprimée.
- **v1.4 (sept. 2026)** — **le slug de page ne doit jamais être le nom de base d'un asset.** Section bloquante ajoutée après trois études de la Factory parties avec une URL suffixée côté EN (`-2`, `-3`) : `wp_unique_post_slug()` inclut `attachment` dans sa vérification, donc un `<slug>.csv` uploadé avant l'import vole le slug de la page, et la garde du snippet, qui compare le `post_name` exact, cesse d'émettre CSS, JSON-LD, Open Graph et composant. Le symptôme se lit comme un import raté alors que l'import a réussi. Ajouts : les deux règles d'évitement (nom d'asset distinct, ou import avant upload des données), l'assertion à poser dans le build, le diagnostic `curl | grep -c` en une ligne, la procédure de réparation, la note que `ewpa/update-post` n'écrit pas le slug, et le corollaire watermark sans chemin. Aucune règle antérieure supprimée.
- **v1.3 (sept. 2026)** — **le composant interactif n'est plus conditionnel, il est OBLIGATOIRE sur chaque paire.** La formulation « s'il y a un composant interactif » est REMPLACÉE par une obligation, assortie d'une **barre de qualité en quatre tests** (trancher ce que le texte ne peut pas trancher, reposer sur de la donnée auditée, tenir debout seul, ne pas cloner le mécanisme précédent) — sans cette barre, l'obligation produirait exactement le graphe de remplissage qu'elle vise à éviter. Une seule exception : la page outil/simulateur, qui en tient lieu. « La page n'a pas de série » est explicitement non recevable comme motif d'omission au moment du bundle. La décision du mécanisme est **avancée à l'étape 2**, avec le degré bilingue, parce qu'elle conditionne les séries à récupérer et le placement du visuel. Contraintes de forme regroupées (JS vanilla, libs jsdelivr/unpkg, localisation des libellés ET des données, brand-kit, AMF appliquée au composant, état par défaut porteur de sens). Les séries du composant entrent dans le périmètre de l'audit factuel. La section « Portée » précise que cette section vaut aussi pour les projets qui produisent des pages Eco3min dans un autre format d'import. Motif : rendre au site une valeur qu'un résumé de LLM ne réplique pas, et donner au lecteur une raison de revenir. Aucune règle v1.0/v1.1/v1.2 supprimée.
---

## RÈGLE FIGÉE (août 2026) — Zéro commentaire HTML dans le contenu publié

**Statut : bloquant. Aucune exception.**

### La règle

Le HTML livré dans le `post_content` d'une page Eco3min — bloc Custom HTML, bloc Gutenberg,
contenu poussé par un bundle d'import — ne contient **aucun commentaire HTML** : ni en-tête de
documentation, ni marqueur de section (`<!-- 1. INTRO -->`), ni note de maintenance.

Les commentaires structurels restent utiles **pendant l'assemblage**. Ils sont retirés avant
d'émettre le bundle ou de coller le HTML dans l'éditeur.

### Pourquoi — incident du 27 août 2026, 8 pages en HTTP 500

Huit pages bilingues portaient un commentaire d'en-tête de ce type :

```
<!-- ============================================================
     ECO3MIN — PAGE FR (bloc Custom HTML)
     Slug: /histoire-chocs-petroliers-inflation-depuis-1973/
     Pas de <h1> (Blocksy). Pas de <script> (snippet PHP porte le chart).
     ============================================================ -->
```

Autoptimize scanne les balises `<script>` / `<style>` **en regex, sans ignorer les commentaires
HTML**. Il a lu le `<script>` littéral, considéré toute la prose française qui suivait comme du
JavaScript, et l'a passée à son minifieur → fatale dans le callback de buffer de sortie →
**HTTP 500 servi avec le corps complet de la page**.

Conséquence : la page s'affiche normalement dans un navigateur, y compris en navigation privée
(Chrome rend le corps quel que soit le statut), et elle est **invisible pour Google**, qui ne lit
que le code de statut. Diagnostic tardif, via la Search Console, après désindexation.

Deux effets secondaires du même motif :

- `wpautop` traite les noms de balises blocs (`h1`, `style`, `p`…) **même à l'intérieur d'un
  commentaire** : il enveloppe le commentaire dans un `<p>` et insère des sauts de ligne en plein
  milieu. Le commentaire livré n'est déjà plus celui qui a été écrit.
- Le commentaire est téléchargé à chaque affichage sans rien apporter au lecteur.

### Interdits absolus

Dans un commentaire HTML, jamais : `<script`, `<style`, `<h1`, `<div`, `<!--`, `-->`.
La règle « zéro commentaire » rend ce point acquis par construction — il est rappelé ici parce
que la tentation revient à chaque page dont le JS vit dans un snippet.

### La seule exception : le marqueur `<!--e3m-review … -->`

Un seul commentaire est admis, et il est **obligatoire** sur une page périssable (section
« Marqueur de fraîcheur ») : `<!--e3m-review due="…" lead="…" do="…"-->`, en tête du `content`.
Il est sûr par construction tant que `do` ne contient aucun `<`, `>`, `"` ni `-->` : rien
qu'Autoptimize puisse prendre pour une balise, rien que `wpautop` puisse casser. Le contrôle
mécanique ci-dessous l'exclut explicitement ; tout autre commentaire reste bloquant.

### Où mettre la documentation à la place

- Contexte de production, slug, mode de montage du composant, mécanisme retenu, degré d'adaptation
  bilingue → **commentaire PHP `/* … */` dans le snippet Code Snippets de la paire**.
  Serveur uniquement, jamais dans la sortie HTML.
- Métadonnées de traçabilité → champs du bundle JSON.

### Vérification mécanique — avant de rendre le bundle

```python
import re
REVIEW = re.compile(r'^<!--e3m-review due="\d{4}-\d{2}-\d{2}" lead="\d+" do="[^"<>]*"-->')
for lang, html in (("EN", html_en), ("FR", html_fr)):
    found = [c for c in re.findall(r'<!--.*?-->', html, re.S) if not REVIEW.match(c)]
    assert not found, f"{lang} : {len(found)} commentaire(s) HTML — {[c[:80] for c in found[:3]]}"
    if perissable:  # décidé au cadrage
        assert REVIEW.match(html.lstrip()), f"{lang} : page périssable sans marqueur e3m-review en tête"
        assert html.count('<!--e3m-review') == 1, f"{lang} : un seul marqueur par page"
```

### Vérification après publication — le navigateur ne valide rien

```bash
for u in <slug-fr> en/<slug-en>; do
  a=$(curl -sS -o /dev/null -w '%{http_code}' "https://eco3min.fr/$u/")
  b=$(curl -sS -o /dev/null -w '%{http_code}' "https://eco3min.fr/$u/?ao_noptimize=1")
  echo "$a $b  $u"
done
```

Attendu : `200 200`. Un `500 200` signifie qu'Autoptimize s'étrangle sur le contenu — chercher
une balise littérale dans le HTML avant toute autre hypothèse.

### Note outillage

`ewpa/search-replace` (connecteur WP MCP) **sanitise la chaîne de recherche et en retire les
balises HTML** avant de matcher : `search: "ni <script>"` devient `search: "ni "` et remplace les
97 occurrences de la sous-chaîne « ni » de la page. Ne jamais s'en servir pour un search-replace
impliquant du HTML. Corriger dans l'éditeur WordPress.

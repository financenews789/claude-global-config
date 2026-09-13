---
name: production-timemachine-eco3min
description: >
  Production des pages « Time Machine » d'Eco3min — page interactive autonome, bilingue
  FR/EN, bâtie sur UNE série temporelle, qu'on fait défiler (scrub + play) et où le visuel
  principal se DÉFORME en direct pendant que l'historique S'ACCUMULE en traces fantômes
  (« la donnée dessine une forme reconnaissable qui évolue dans le temps » — modèle jivx).
  Esthétique sombre/typée délibérément hors du brand kit (anti-défaut-IA), readout vivant,
  record en énorme cliquable, note méthode honnête, CSV reproductible, JSON-LD Dataset.
  Déploiement : design standalone → Code Snippet shortcode scopé → pages WP bilingues
  (template blank + Polylang) via le bundle d'import. Activer pour créer, réviser ou
  débugger une Time Machine. À NE PAS confondre avec : page dataset (production-dataset),
  chart DIB statique (production-chart-of-the-week), simulateur prospectif
  (simulateurs-eco3min), étude texte (production-research-study). Implémentation de
  référence : « yield-curve-timemachine » (courbe des taux US 1981-2026).
---

# Time Machine — production

Une **Time Machine** est une page interactive autonome (un seul shortcode rend TOUT le design),
construite sur **une série temporelle**, où l'utilisateur fait défiler le temps avec une barre
de scroll + un bouton play, et regarde **le visuel principal se déformer** pendant que **les états
passés s'accumulent** sous la forme présente. C'est le format viral « jouet de données » : son
plaisir est l'interaction et la forme qui évolue, pas un titre-à-claim.

Combiner avec : `brand-kit-eco3min` (qu'on **enfreint** sciemment : sombre, pas cream),
`visuels-eco3min`, `editeur-eco3min` (AMF, style), `sourcing-donnees-eco3min` (provenance),
`eco3min-import-contenu-bilingue` (packaging), `production-killer-hn` + `production-chart-of-the-week`
(distribution), `archi-eco3min` + `plugins-eco3min` (slugs, snippet, WP).

---

## §0 — RÈGLE CARDINALE & gates

**RÈGLE CARDINALE.** Une Time Machine ne se justifie que si **la donnée dessine une forme qui se
DÉFORME de façon signifiante quand on avance dans le temps**, et que **l'accumulation des fantômes
veut dire quelque chose** (on voit l'enveloppe de l'histoire). Si le sujet est un scalaire qui monte
ou descend, ce n'est PAS une Time Machine — c'est une courbe : route vers `production-dataset` ou
`production-chart-of-the-week`. Ne force jamais le format.

### Gate 1 — le test « forme-dans-le-temps » (bloquant)
Le format marche quand la donnée a une **forme transversale** qui se réorganise image par image :
- **coupe transversale qui se déforme** : courbe des taux par échéance (réf), pyramide des âges,
  distribution/histogramme, term structure, courbe de Phillips qui boucle ;
- **éclosion spatiale** : événements sur une carte par année (crises, ouvertures, défauts) ;
- **structure qui se réorganise** : composition d'un agrégat, classement qui permute, réseau.

Échoue (→ autre format) : une seule valeur dans le temps (taux directeur, CPI, un spread isolé).
Il n'y a pas de « forme » à morpher ; les fantômes ne racontent rien.

**Test rapide** : « si je superpose 500 images de la donnée, est-ce que j'obtiens une *enveloppe*
parlante (un nuage de courbes, une carte qui se remplit, un éventail) ? » Oui → Time Machine.
Non → dataset/chart.

### Gate 2 — surface de distribution (cross-ref `production-killer-hn`)
Appliquer le gate viral du skill killer-hn. La plupart des Time Machines sont belles mais **de niche** :
- **DIB (r/dataisbeautiful)** = canal le plus probable de gros succès (le chart porte le choc).
- **HN** = meilleur pari pour les **backlinks de qualité**, via le vecteur *plaisir interactif*
  (jivx) + l'audience HN lettrée en finance/quant — PAS via un mot-marteau. Variance assumée.
- Ne jamais survendre le gate : si le sujet échoue aux tests de viralité universelle, c'est un sujet
  pour DIB, pas un sujet raté.

---

## §1 — La donnée (discipline)

1. **Source primaire réelle uniquement** (FRED, ECB SDMX, BIS, World Bank, BLS, NY Fed, IMF…).
   Réf `sourcing-donnees-eco3min`. Le footer = source RÉELLE des chiffres, jamais relabellisée.
2. **Le CSV est la source de vérité ET il est autoportant** : colonnes brutes + colonnes dérivées
   pour qu'un tiers puisse **rejouer la thèse depuis le seul fichier**. Réf yield-curve : `month`,
   les 7 rendements, les 2 spreads, les drapeaux d'inversion, drapeau récession NBER,
   `months_to_next_recession`. C'est le « show your work » qui crédibilise sur HN.
3. **Chiffres calculés EN DIRECT** depuis la donnée embarquée (jamais saisis à la main). Un record,
   un extrême, une moyenne → le moteur les calcule ou ils sont vérifiés au centième contre le CSV.
4. **Honnêteté de FRÉQUENCE — piège majeur.** La fréquence de la page conditionne CHAQUE claim.
   Un record cité doit être vrai *à la fréquence de la page*. Leçon de référence : le 2s10s a touché
   **−1.08 en daily** (mars 2023) mais la page est **mensuelle** → en mensuel le 2s10s le plus profond
   est **1981 (−1.14)** et 2023 n'atteint pas −1.00 ; le vrai record récent exact est le **10Y−3M à
   −1.74 (mai 2023)**. Toujours étiqueter la fréquence et vérifier l'extrême contre le CSV de la page.
5. **Couverture longue** (décennies) : l'accumulation des fantômes n'est frappante qu'avec assez
   d'histoire. Alignement temporel propre, granularité constante.

---

## §2 — Le design (doctrine sombre/typée)

**RÈGLE.** On **n'utilise PAS** le brand kit cream / Source Serif / terracotta. C'est exactement la
« tête de défaut IA » qui se fait **moquer sur HN** (constat du fil jivx). On va **sombre, typé,
factuel** :
- fond encre (`#0E1320`), panneau (`#141A28`), texte (`#E7E4DD`) ; familles `Inter` (sans),
  `ui-monospace`/IBM Plex Mono (mono, pour labels/chiffres), un titre sobre ;
- **un seul accent** fonctionnel (teal `#45B6AF` neutre / red `#D75A7A` = état inversé/critique).
  Le rouge encode un **état réel** (inversion), jamais décoratif.

Composants obligatoires :
1. **Le morph** : le visuel principal se reforme à mesure qu'on scrolle ; les états passés
   **s'accumulent** en traits translucides, **colorés par l'état** (ex. rouge = inversé, pâle =
   normal), opacités tunables. C'est la magie « forme qui évolue ».
2. **Readout vivant** : grosse année + 2-3 stats clés + une **légende dynamique** liée au moment
   (annotations curées sur des dates clés, sinon caption générique par état).
3. **Contrôles** : **barre de scroll draggable** (timeline) + **play/pause** + un toggle de
   série/spread si pertinent. La timeline porte les **bandes de récession/contexte**.
4. **Chips « Jump to »** : épisodes curés + extrêmes (plus haut / plus bas / plus profond / plus pentu).
5. **Record en ÉNORME** (HN adore les records) : un bandeau « Deepest/Highest X on record » avec la
   valeur en gros, **cliquable** → bascule la série + scrolle sur le mois du record, de sorte que le
   readout affiche **exactement** la même valeur (cohérence au centième). Valeur calculée/vérifiée,
   **à la fréquence de la page**.
6. **Note méthode honnête** : ce qu'est la donnée, la source, et les **caveats** (régularité observée
   ≠ mécanisme ; confounds ; « montre ce que X a fait, pas ce que X fera »). Les caveats sont une
   FORCE — c'est le désamorçage qui rend crédible sur HN.
7. **Téléchargement CSV** identique au fichier hébergé (même colonnes, même nom).

**Interdits** (cross-ref `production-every-x-record`) : zéro **cosplay d'autorité** — pas de « Cite
this », DOI, « Abstract », badges « public dataset », bloc auteur-affiliation. L'autorité se gagne par
le contenu.

---

## §3 — Architecture technique (le pattern de build)

**Phase 1 — STANDALONE.** Construire d'abord la page complète autonome : self-contained, **sans libs
externes si possible** (SVG fait main), donnée réelle inline. Vérifier rendu + mobile + console clean
en headless avant d'aller plus loin.

**Phase 2 — SHORTCODE scopé** `[eco3min_<x> lang="en|fr"]` (Code Snippet) :
- **CSS namespacé** sous un conteneur `.eco3<x>` ; **les variables CSS sur le conteneur**, pas sur
  `:root`. Conséquence critique : la fonction qui lit les couleurs doit lire
  `getComputedStyle(root)` (le conteneur), **pas** `document.documentElement` — sinon couleurs vides.
- **JS scopé** : `INIT` sur `DOMContentLoaded`, trouve le conteneur (`querySelector('.eco3<x>[data-…]')`),
  lit `data-lang`, **IDs préfixés fixes** (`#eco3<x>-yr`, etc.) → **une seule instance par page**.
  Le script est émis AVANT le markup (assets d'abord) → l'init DOIT attendre `DOMContentLoaded`.
- **SEO server-side** : le **PHP rend la prose SEO** (eyebrow, H1, lede, méthode, footer, label
  download) — pour que les crawlers la voient dans le HTML initial. Le **JS** ne peuple que les
  **labels d'UI dynamiques** depuis un objet `STR`.
- **Bilingue** : `STR` (en/fr) en JS pour le dynamique ; `$T` (en/fr) en PHP pour la prose statique.
- **Sécurité apostrophes** : tout le texte FR/EN utilise l'apostrophe typographique `’` (U+2019) ou
  des entités HTML (`&rsquo;`, `&amp;`) → **aucune apostrophe ASCII** ne se balade, donc on peut
  embarquer le JSON dans une chaîne PHP simple-quote sans casse. **Assert** `"'" not in json` au build.
- Données + `STR` émis **une seule fois** (garde statique `$done`) ; markup à chaque appel du shortcode.
- **Pas de `<?php`** en tête. Libs externes (s'il y en a) depuis **jsdelivr/unpkg**, jamais cdnjs.

**Phase 3 — PAGES WP bilingues** via le bundle (réf `eco3min-import-contenu-bilingue`) :
`import_type: bilingual_page` ; le champ **`snippet`** installe le Code Snippet ; **`content` des pages
= juste le shortcode** (`<!-- wp:shortcode -->[eco3min_<x> lang="en"]<!-- /wp:shortcode -->`) ; SEO +
**JSON-LD Dataset** (les 3 réfs image `featured/og/json-ld` strictement identiques) ; Polylang lié ;
`status: draft`. Un seul import installe snippet + 2 pages.

**Phase 4 — RÉGLAGES WP** (tout injecté par le shortcode → « cette page uniquement », car le CSS ne se
charge que là où le shortcode existe) :
- **Template blank/canvas** (Blocksy content-canvas) + **masquer le titre WP** ;
- **Masquer le titre de template + le breadcrumb** : `.hero-section{display:none}` (+
  `.entry-header .page-title, .ct-breadcrumbs`) — scopé via le CSS du snippet ;
- **Override fond sombre pleine page** : `html,body{background:#0E1320}` + neutraliser les conteneurs
  du thème (`#main, .ct-container, .entry-content, article, .entry-card{background:transparent}`).

---

## §4 — Doctrine MOBILE (la co-visibilité — non négociable)

**RÈGLE.** Tout l'intérêt est de **regarder le visuel se déformer EN faisant glisser la barre**. Donc
sur mobile, **la barre de scroll doit être co-visible avec le graphique**. Le readout passe **en dessous**.

- **Ordre mobile** : (record) → graphique → barre de scroll → readout → contrôles → reste.
- **Technique** : le graphique et la barre vivent dans des conteneurs différents → on **aplatit la
  hiérarchie** avec `display:contents` sur les conteneurs concernés, puis on `order:` librement
  (desktop intact, tout dans `@media (max-width:760px)`).
- **PIÈGE à connaître** : un enfant flex avec `flex:1 1 Npx` (dimensionné pour la **largeur** desktop)
  voit son `flex-basis:Npx` s'appliquer à la **HAUTEUR** dans une colonne flex mobile → barre géante
  (320 px observés). **Reset `flex:0 0 auto`** sur mobile.
- Garder `width:100%` sur la barre, et vérifier que **record + graphique + barre tiennent sur un écran**
  (~690 px utiles sur un téléphone courant). Record au-dessus = hook above-the-fold.

---

## §5 — i18n (discipline)

- `STR` par langue : mois pleins, mois courts, **labels d'échéance** (ex. `Y` vs `A`), tags, gabarits
  de lead, annotations, captions, hint, chips, **label du record**, play/pause, noms de spread.
- `$T` (PHP) par langue pour la prose SEO (eyebrow, H1, lede, méthode, footer, download).
- **Tout** ce que voit l'utilisateur est localisé, **y compris les dates** du record/readout
  (`STR.months[i] + " " + année`) et les unités de spread.
- Apostrophes `’` (U+2019) / entités partout, **assert** au build.

---

## §6 — AMF & honnêteté

- **Descriptif/historique uniquement.** « Montre ce que X a fait, pas ce que X fera. » Pas de
  prescription, pas de prévision présentée comme un fait, pas de « should/devrait ».
- Les **caveats honnêtes sont un atout** : ils constituent le **désamorçage** qui désamorce les
  guerres de commentaires sur HN (régularité ≠ mécanisme, confounds, cas ouverts). Les écrire.
- Pas de zones colorées prescriptives, pas de flèches achat/vente, pas de cible de prix
  (réf `visuels-eco3min`).

---

## §7 — Distribution (cross-ref)

Ce format vise **DIB** (le chart porte le choc — pari le plus probable de gros succès) **et HN**
(backlinks de qualité, via le plaisir interactif). Appliquer le **gate + le séquencement** de
`production-killer-hn` (typiquement : HN lundi 15h Paris → +24h DIB image statique + lien vers la
PAGE, pas vers le thread HN → ensuite r/economics). Pour DIB, produire un **export statique** via
`production-chart-of-the-week`. Le **record** et le **morph** sont les hooks.

---

## §8 — Méthode anti-erreur

1. **Build par transformations assertées** (lire la donnée/le moteur, appliquer des remplacements avec
   `assert old in source`), jamais d'édition à l'aveugle.
2. **Vérifier le rendu à CHAQUE changement**, en headless, **desktop + mobile + FR**. Le contrôle
   **visuel est obligatoire** (le namespacing/scoping CSS casse silencieusement).
3. **Le harnais de test DOIT inclure le CSS** (leçon : CSS oublié dans la page de test → faux « cassé »).
   Pour le fond sombre, tester aussi contre un **conteneur blanc « boxed »** simulé pour prouver
   l'override.
4. `node --check` le JS ; **sanity PHP** structurelle (équilibre heredoc/nowdoc, pas de `<?php` en tête,
   `add_shortcode` présent).
5. **Vérifier les chiffres contre le CSV** (record/extrême **à la fréquence de la page**) ; cliquer le
   record en headless et confirmer que le readout affiche la même valeur.

---

## §9 — PIÈGES (checklist des erreurs déjà commises)

- ❌ Record cité à la **mauvaise fréquence** (daily vs mensuel) → vérifier contre le CSV de la page.
- ❌ `flex:1 1 Npx` → **N px de hauteur** sur mobile en colonne → `flex:0 0 auto`.
- ❌ **Double H1** (template WP + shortcode) → masquer le H1 du template (CSS, accepté) ou toggle
  Blocksy par page (DOM-propre, 1 seul H1).
- ❌ **Cadre cream/blanc** autour de la carte → override fond sombre scopé au shortcode.
- ❌ `cv()` lit les vars sur `documentElement` après qu'elles ont migré sur le conteneur → lire `root`.
- ❌ **Harnais de test sans CSS** → rendu faussement cassé.
- ❌ **Ré-importer pour appliquer un changement de snippet** → repasse les pages publiées en **draft**.
  Pour tout changement *interne au snippet*, **mettre à jour le code du Code Snippet**, jamais ré-importer.
- ❌ **Look brand par défaut** (cream/serif/terracotta) → moqué sur HN → sombre/typé.
- ❌ **Cosplay d'autorité** (Cite this, DOI, badges) → banni.
- ❌ Forcer le format sur un **scalaire** (pas de forme à morpher) → dataset/chart à la place.

---

## §10 — Checklist de livraison

- [ ] Gate 1 (forme-dans-le-temps) **et** Gate 2 (surface de distribution) passés honnêtement.
- [ ] Donnée source primaire réelle ; CSV autoportant (brut + dérivé) ; chiffres calculés/vérifiés.
- [ ] Record exact **à la fréquence de la page**, cliquable, cohérent au centième avec le readout.
- [ ] Design sombre/typé, accent unique encodant un état réel ; morph + fantômes ; readout vivant.
- [ ] Note méthode honnête (caveats) ; téléchargement CSV identique au fichier hébergé ; AMF respecté.
- [ ] Pas de cosplay d'autorité.
- [ ] Shortcode scopé (`.eco3<x>`, vars sur conteneur, `cv()`→root, IDs préfixés, init sur DOMContentLoaded).
- [ ] SEO server-side (PHP rend H1/lede/méthode) ; `STR` JS pour le dynamique ; bilingue complet,
      dates/unités localisées.
- [ ] Apostrophes `’`/entités, assert no-ASCII-`'` ; pas de `<?php` ; libs jsdelivr/unpkg.
- [ ] Mobile : record → graphique → **barre** → readout ; `flex:0 0 auto` ; tout tient sur un écran.
- [ ] WP : template blank, titre WP masqué, titre template + breadcrumb masqués, override fond sombre —
      tout via le snippet (« cette page uniquement »).
- [ ] Bundle d'import : `bilingual_page`, snippet inclus, content = shortcode, SEO + Dataset JSON-LD
      (images identiques), Polylang lié, status draft.
- [ ] Rendu vérifié en headless desktop + mobile + FR ; `node --check` ; sanity PHP.
- [ ] Distribution planifiée (killer-hn gate + séquencement ; export DIB via chart-of-the-week).

---

**Implémentation de référence** : `yield-curve-timemachine` — la courbe des taux du Trésor US 1981-2026,
shortcode `[eco3min_yield_curve lang]`, record « Deepest inversion on record · 10Y−3M · −1.74 pts ·
May 2023 ». S'en servir comme gabarit.

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

---
name: production-hero-pilier
description: "Production des heros de pages PILIERS d'eco3min.fr (série template-driven d'environ 10 piliers, 1536×864, fond crème), FR et EN — le visuel qui montre le territoire d'un silo en 5 secondes. Activer pour toute création ou itération d'un hero de pilier : « hero du pilier », « hero pilier X », « refais le hero de politique-monetaire-taux », « prochain pilier », « option A ou SM ? », « rotation série », « quel format pour ce pilier », « small multiples 2×2 », « dual-anchor », « tag pilier », « layout 6 zones », « hero-A-1990-2026.png ». Structure : SKILL.md = colonne vertébrale (mission, règle UNE idée visuelle dominante et les 4 formats A / B / C / SM, rotation série bloquante v1.2, process condensé, contraintes éditoriales verbatim, charte, layout 6 zones, anti-patterns et 3 tests verbatim, livraison, input) ; références dans references/ (à lire quand l'étape le dit) : 01 process en 4 étapes avec l'audit de faisabilité data, la table des proxies académiques et les cartes d'options, 02 layout canonique avec la variante barre régimes, la variante Option SM (labels catégoriels uppercase, annotations dual-anchor) et la hiérarchie des 5 signaux, 03 note d'usage, arbitrages de mai 2026, workflow et piliers candidats ; pas de scripts/ propres (gardes : brand-kit-eco3min/scripts/brand_tokens.py et visuels-eco3min/scripts/mpl_guards.py). Doctrines : UN format par hero, jamais empilés ; rotation série bloquante (jamais 2 piliers consécutifs sur le même format, max 2 heros consécutifs en mode sobre, input = format + mode des 2 derniers heros, dérogation signalée jamais tranchée en silence) ; audit de faisabilité data avant de coder (couverture de période, symétrie des N catégories) ; rigueur métrique : le proxy est LE standard académique du concept sur toute la période (HY OAS contredisait la thèse sur marches-financiers, mai 2026, l'ACM term premium était le bon) ; proxy ou transition de série signalé DANS le chart et en footer, jamais en footer seul ; symétrie de traitement des N catégories ; terracotta unique en mode sobre, verticale répétée acceptée en Option SM ; dual-anchor moyenne-par-régime obligatoire en SM ; timestamp en ligne 2 du sourcing seulement ; chrome canonique v2.0 : sources bas-gauche, signature Eco3min Research + URL bas-droite, tag pilier sans numérotation ; production en code depuis le CSV réel, Claude Design pour explorer les options. Hors périmètre : heros de majeur (production-hero-majeur, thèse sur fond blanc) et d'article (production-hero-article-eco3min, 1200×630) ; tokens (brand-kit-eco3min) ; AMF visuelle, choix de chart et rendu (visuels-eco3min) ; corps de la page (formats-eco3min, pilier-kit). Combiner avec brand-kit-eco3min, visuels-eco3min, sourcing-donnees-eco3min, editeur-eco3min, archi-eco3min."
---

# Production — Hero visuel pour page pilier Eco3min

## Mission opérationnelle

Générer le visuel hero placé en tête d'une page pilier de eco3min.fr (site bilingue macro-financier, benchmark éditorial FT / Bloomberg / Les Échos). Ce hero appartient à une série template-driven d'~10 piliers — penser **template transférable**, pas one-off.

## Fonction du hero

- Transmettre LA thèse structurante de la page en **5 secondes**, comprise pleinement en 15-30 secondes.
- Établir la crédibilité data-driven dès le premier regard.
- Rester lisible si partagé seul sur X / LinkedIn / Reddit.
- NE PAS dupliquer le contenu texte de la page — l'**amplifier visuellement**.

---

## COMMENT LIRE CE SKILL (découpage du 17/09/2026)

Ce fichier est la colonne vertébrale : les deux règles bloquantes (UNE idée, rotation série), le process condensé, les contraintes éditoriales, le layout, les anti-patterns, les tests et le format de livraison. Le détail (audit data et table des proxies, cartes d'options, layout 6 zones et variantes, arbitrages de mai 2026) a été déplacé VERBATIM dans `references/` et fait foi au même titre que ce fichier. Chaque étape ci-dessous nomme le fichier à lire ; le lire est obligatoire au moment indiqué. Les tokens et le chrome sont dans `brand-kit-eco3min` (v2.0 §0), les gardes de rendu dans `visuels-eco3min` §7 bis / §7 ter.

| Fichier | Contenu | À lire |
|---|---|---|
| `references/01-process-these-data-options.md` | Étapes 1 à 4 : thèse, audit de faisabilité data, rigueur métrique et table des proxies, cartes d'options, SVG modulaire, variante linguistique | avant l'Étape 1 (audit data), puis avant de présenter les options |
| `references/02-layout-canonique-variantes.md` | architecture 6 zones, variante barre régimes, variante Option SM (labels catégoriels, dual-anchor, titre et sous-titre SM), format sourcing footer, hiérarchie des 5 signaux | avant de coder le layout, obligatoire si Option SM ou barre régimes |
| `references/03-note-usage-arbitrages-workflow.md` | genèse du skill, confirmé canonique, arbitrages tranchés, workflow code vs Claude Design, à actualiser, piliers candidats | avant de proposer un pilier suivant, et quand un arbitrage passé est remis en cause |

---

## Règle bloquante : UNE idée visuelle dominante

Un hero ≠ infographie de manuel. Choisir **UN** format parmi :

**(A) Série temporelle anchor** — un graphique unique (taux, ratio, indice) avec ≤4 annotations descriptives. Données réelles, source citée, axes chiffrés.

**(B) Comparaison binaire/ternaire** — deux ou trois régimes/états mis en regard sur des dimensions quantifiées. Max 4 lignes de comparaison.

**(C) Diagramme conceptuel non-trivial** — ≤7 éléments, relations non-linéaires (boucles, rétroactions, asymétries). Refusé si la structure est une simple chaîne A→B→C.

**(SM) Small multiples 2×2** — grille de 4 mini-charts indépendants partageant le même axe temporel et le même moment-pivot. Chaque cellule = UNE propriété distincte d'un concept structurel multi-dimensionnel. Verticale terracotta cohérente à la même date sur les 4 cellules (redondance contrôlée acceptée : elle sert la thèse « N propriétés convergent »). À choisir UNIQUEMENT quand la thèse mentionne explicitement N propriétés/dimensions distinctes ET qu'aucune métrique unique ne peut capturer le basculement. Layout enrichi spécifique — voir section Layout canonique.

**INTERDIT** : empiler (A) + (B) + (C) + (SM) dans le même visuel. Si hésitation entre formats, demander à Paul de trancher avant de coder.

---

## Règle bloquante : rotation série (anti-monotonie, v1.2)

Les heros piliers forment une **série** — c'est comme série qu'ils sont perçus (page d'accueil, navigation inter-piliers, partages groupés). La monotonie observée sur les premiers piliers livrés (convergence vers l'Option A + mode sobre crème + 1 ligne terracotta) était flaguée comme risque en v1.1 ; elle devient une règle en v1.2.

**Deux rotations obligatoires, vérifiées AVANT l'étape Options** :

1. **Rotation de format** : le format retenu (A / B / C / SM) doit différer de celui du **pilier précédent**. Sur 4 piliers consécutifs, aucun format ne peut apparaître plus de 2 fois. Si la donnée du pilier n'appelle *vraiment* qu'un format déjà utilisé au pilier précédent, le signaler à Paul comme dérogation explicite — jamais trancher en silence.

2. **Rotation de mode chromatique** : pas plus de **2 heros consécutifs en mode sobre** (charcoal + 1 terracotta). Le troisième bascule en **mode catégoriel** (palette `brand-kit-eco3min` §2.5 — pertinent dès que le pilier compare des régimes, des époques, des pays ou des classes d'actifs) ou en gradient si la donnée est continue. Le mode catégoriel n'est pas une baisse de sobriété : c'est le registre FT/OWID des comparaisons multi-entités, saturation sourde inchangée.

**Ce qui ne tourne JAMAIS (squelette identitaire de la série)** : layout 6 zones, fond crème (le blanc et le charcoal inversé sont réservés aux majeurs et formats spéciaux — cf. brand kit §2.2), triade typo, sourcing footer 2 lignes, watermark, tag pilier, direct labeling. La variété se joue dans le format et la couleur À L'INTÉRIEUR de ce squelette — identité par la structure, variété par la couleur.

**Input requis** : format + mode chromatique des 2 derniers heros livrés (cf. section Input attendu). Sans cet input, demander avant de proposer les options.

---

## Process en 4 étapes (lire `references/01-process-these-data-options.md` avant l'Étape 1)

Bloquant :
- **Étape 1 — Thèse + audit de faisabilité data.** Thèse en UNE phrase ; page sans thèse univoque → signaler le problème éditorial AVANT toute production. Pour chaque série mobilisable, couverture de la période visée vérifiée (TIPS commencent en 2003 pour une thèse 1990-2026 → flaguer) ; série incomplète → proxy pré-période avec disclosure, recadrage de la thèse ou chart court + annotation, **proposé à Paul, jamais tranché en silence**. N catégories nommées → chacune représentable de façon symétrique, sinon flaguer.
- **Étape 1.3 — Rigueur métrique.** La métrique est **LE proxy académique standard** du concept énoncé (table dans la référence 01 : coût du capital → TIPS `DFII10`, prime de duration → ACM term premium, prime crédit → HY OAS `BAMLH0A0HYM2`, vol → `VIXCLS`…). **Test bloquant : la métrique fait ce qu'elle prétend SUR LA PÉRIODE COMPLÈTE de la thèse.** Plusieurs proxies défendables : celui cité dans la page, sinon le plus Bloomberg-ready, sinon le plus reproductible (FRED). Doute → demander à Paul AVANT de coder.
- **Étape 2 — 2 ou 3 options** de formats différents, chacune en carte structurée (titre, mockup ou description, ce que l'œil capte en 3 s, données avec codes, compromis). Paul arbitre.
- **Étape 3 — Production finale** en 1536×864 depuis le CSV réel, code modulaire par zone (1/2/3/5/6 texte paramétrable FR/EN, zone 4 chart-block invariant). Rendu en code : HTML/SVG → Playwright (`visuels-eco3min` §7 bis) ou matplotlib + `mpl_guards` (§7 ter) ; `brand_tokens.check_source` sur le script avant livraison.
- **Étape 4 — Variante linguistique systématique** : même structure, mêmes données, seul le texte change ; titre traduit qui garde le rythme, pas une traduction littérale plate.

---

## Contraintes éditoriales (non négociables)

### Sourcing intégré au visuel

- Sources institutionnelles citées en **bas-gauche** (Fed, BCE, BIS, FMI…) — chrome canonique `brand-kit-eco3min` v2.0 §0
- **Codes de série explicites** (DFII10, DGS10, etc.) — pas seulement « Federal Reserve » générique
- Méthodologie résumée en une ligne, ex : « TIPS 10Y from 2003 · pre-2003 proxy = DGS10 − sticky core CPI YoY · Values rounded for readability »
- « Updated [mois année] »
- Signature `Eco3min Research` ligne 1 + URL pilier ligne 2 en **bas-droite** (IBM Plex Mono, zéro cadratin)

### AMF compliance (visuel)

- Aucune flèche achat/vente, aucune zone colorée prescriptive
- Aucune cible de prix, aucune ligne « buy zone / sell zone »
- Annotations descriptives uniquement (« real rates turned positive Oct 2022 »), **jamais prescriptives**
- Aucun terme dramaturgique : pas de « collapse », « explosion », « destruction », « failed »

### Honnêteté data

- Axes chiffrés. Pas d'axe tronqué qui amplifie artificiellement.
- Pas de label « indicative » sur série chiffrable.
- Si série composite ou proxy : méthodologie en footer **ET** signalisation visuelle DANS le chart (pointillé vs plein, label de transition, etc.). **Footer seul ne suffit pas.**

### Symétrie de traitement des catégories

- Si la thèse mentionne N régimes/scénarios/catégories, les N doivent avoir un cue visuel équivalent (zone ombrée, ligne verticale, label délimité).
- Asymétrie volontaire acceptable SI éditorialement justifiée (ex: rupture sharp + transition graduelle), mais à **signaler comme choix délibéré** dans la livraison.

---

## Charte visuelle

**Palette, typographie, codes régime → voir `brand-kit-eco3min` (v1.1+).** Le brand kit fournit la source de vérité commune à toutes les productions visuelles Eco3min :
- 3 familles typo fixes (Source Serif 4 + Inter + IBM Plex Mono)
- Palette principale (charcoal `#1A1A1A` + gris medium `#757575` + accent terracotta `#B85C3C`)
- Fond crème `#F8F5EE` (registre fixe de la série heros piliers — blanc et charcoal inversé réservés à d'autres familles, brand kit §2.2)
- **Palette catégorielle 7 rangs (brand kit §2.5)** — pour les heros en mode catégoriel (comparaisons multi-régimes, multi-époques, multi-actifs), avec direct labeling en bout de ligne
- 6 codes couleurs régime sur 2 axes (3 macro + 3 monétaire) — priorité sémantique : à utiliser quand le hero nomme explicitement un régime
- Règle terracotta clarifiée : **unicité en mode sobre** (1 occurrence, label inclus) ; en mode catégoriel, terracotta = couleur de la série rang 1, l'unicité ne s'applique pas — mais le hero garde UN focus visuel

### Règles spécifiques aux heros piliers (en complément du brand kit)

**Densité** — information dense mais épurée. Aucun élément qui n'enseigne pas. Si un élément peut être retiré sans perte d'information, le retirer.

**Format**
- Ratio 16/9, dimensions **1536×864** strict pour la série hero pilier (contrairement au reste du brand kit qui laisse les ratios libres selon contexte).
- Test mobile : tout lisible à **380px** de large. Police mini ≈ équivalent 14px à 1536px de largeur.

**Anti-pattern terracotta cluster — version durcie pour les heros** : la règle d'unicité du brand kit s'applique avec une vigilance particulière sur les heros piliers, qui sont les visuels les plus exposés du site. Empiriquement validé sur 3 piliers livrés (mai 2026) : le pilier `politique-monetaire-taux` avec 1 ligne terracotta isolée a plus d'impact que `macroeconomie-geopolitique` avec 5 occurrences cluster. **Test** : si tu peux retirer 2 occurrences de terracotta sans dégrader la lecture de la thèse, retire-les.

**Cas Option SM** : la verticale terracotta se répète sur les 4 cellules à la même date — redondance contrôlée acceptée parce qu'elle sert la thèse « N propriétés convergent », pas un cluster.

Chrome canonique v2.0 (`brand-kit-eco3min` §0) : titre Source Serif 4 charcoal, sous-titre Inter gris medium, sources bas-gauche 2 lignes mono, signature `Eco3min Research` + URL pilier bas-droite, zéro cadratin, tag pilier sans numérotation.

---

## Layout canonique (lire `references/02-layout-canonique-variantes.md` avant de coder le layout)

Architecture 6 zones, confirmée sur `politique-monetaire-taux` et `macroeconomie-geopolitique` (mai 2026), défaut sur les piliers suivants sauf raison éditoriale signalée à Paul :

1. **Tag pilier** (haut-gauche) — uppercase mono, ex. `POLITIQUE MONÉTAIRE & TAUX — PILIER`, sans numéro
2. **Titre** (serif large, ≤8 mots) — porte la thèse, rythme conservé en traduction
3. **Sous-titre** (Inter, 2 phrases max) — phrase 1 décrit ce que montre le chart, phrase 2 porte la thèse
4. **Chart pleine largeur** — le visuel dominant, contient toute la donnée
5. **Signature** (bas-droite) — `Eco3min Research` ligne 1 + URL pilier ligne 2
6. **Sourcing** (bas-gauche) — 2 lignes : `Sources: [Institution] ([codes]); …` / `Updated [mois année] · [méthodo 1 ligne] · Values rounded for readability` ; le timestamp n'apparaît QUE là

Bloquant :
- **Hiérarchie des 5 signaux intra-chart**, ordre décroissant strict : accent terracotta (1 marqueur) → zone ombrée medium grey → pointillé vertical fin → zone ombrée light beige → annotations courtes (≤4, bord supérieur). Redondance contrôlée acceptable (2 signaux pour une même frontière) si elle sert la robustesse de lecture, interdite si remplissage.
- **Variante barre régimes en pied** seulement quand la géométrie de la courbe raconte déjà les phases (chart « geom-led »).
- **Option SM** : structure interne par cellule en 4 niveaux (label catégoriel uppercase terracotta `PROPRIÉTÉ 01 · CONCEPT`, titre de métrique, chart avec verticale terracotta à la même date sur les 4 cellules, **annotations dual-anchor moyenne-par-régime avant/après obligatoires**, jamais point-précises) ; titre qui porte les deux axes (N régimes, M propriétés, rupture en YYYY).

---

## Anti-patterns explicitement proscrits

- Diagramme de flux linéaire trivial (chaque flèche évidente)
- Empilement timeline + colonnes texte + chart + diagramme dans le même hero
- Bullets points multiples qui dupliquent la TOC de l'article
- Chart « indicatif » non chiffré sur axes
- Titre + sous-titre + 3 colonnes + mini-chart + watermark (surcharge classique)
- Symboles ↗ ↘ sans contexte numérique
- Légende détachée du graphique forçant des allers-retours
- Transition de séries (proxy ↔ donnée réelle) cachée uniquement en footer — doit AUSSI être visible dans le chart
- **Redondance forcée du signalement** — chercher artificiellement un 2e pointillé / une 2e zone ombrée parce que « ça marchait bien sur un pilier précédent », alors qu'il n'y a qu'une seule transition réelle à marquer. La redondance est un outil de robustesse, pas un pattern à reproduire mécaniquement
- **Doublon timestamp** — `Updated [mois année]` apparaissant à 2 endroits (ex: haut-droite du visuel ET ligne 2 du sourcing footer). Choisir UN seul emplacement, par défaut la ligne 2 du sourcing footer
- **Accent terracotta cluster** — 4 ou 5 occurrences de terracotta sur des éléments connexes (ligne verticale + shading + label-régime + bullet décoratif + label-chiffre) en argumentant qu'elles servent la même narration. Même cohérentes, ces occurrences multiples diluent l'impact visuel. Voir règle Palette pour le test de validation
- **Proxy métrique adjacent** — choisir une métrique connexe « qui marche aussi » (ex : HY OAS pour illustrer un duration risk premium, alors que l'ACM term premium existe) au lieu du proxy académique standard du concept énoncé. Risque : la métrique adjacente peut raconter une histoire DIFFÉRENTE de la thèse et la contredire silencieusement. Cas observé sur le test direct `marches-financiers` (mai 2026) : HY OAS choisi pour « primes de risque » → courbe redescendue à son plancher historique en 2024-2026, contredisant la thèse « primes reconstituées ». Voir Étape 1.3 Rigueur métrique
- **Bottom annotations point-précises au lieu de dual-anchor en Option SM** — `−1,19 % août 2021 → +2,40 % oct. 2023` est précis mais demande au lecteur de reconstruire la temporalité. Pour les small multiples, utiliser systématiquement le format moyenne-par-régime avant/après (voir Variante Layout Option SM)

---

## Tests de validation embarqués

**Test 1 — Comptage non-initié.** Si le titre mentionne N éléments (« trois régimes », « deux scénarios »…), Paul doit pouvoir montrer le hero à quelqu'un sans contexte et lui demander de compter N éléments. Si la personne compte ≠ N, itérer sur la signalétique.

**Test 2 — Mobile 380px.** Avant livraison, simuler le rendu à 380px de large : aucun chevauchement d'annotations, labels méthodo restent lisibles, sourcing footer toléré moins lisible.

**Test 3 — Lecture 5 secondes.** Masquer mentalement le titre/sous-titre et regarder uniquement le chart pendant 5 secondes. La thèse se capte ? Si non, elle est portée par le texte plutôt que par la donnée — revoir.

---

## Livraison attendue

1. **Audit thèse + faisabilité data** (réponses à Étape 1)
2. **2-3 options visuelles** (Étape 2) avec briefs structurés
3. **SVG final FR** (après arbitrage de Paul)
4. **SVG final EN** (variante stricte)
5. **Checklist « ce qui tient et ne doit pas être cassé »** — 3 à 5 points du squelette à reproduire sur les piliers suivants

---

## Input attendu de Paul

- Contenu intégral de la page pilier (FR ou EN)
- Slug et URL de la page
- **Format (A/B/C/SM) et mode chromatique (sobre/catégoriel/gradient) des 2 derniers heros piliers livrés** — requis pour la rotation série (règle bloquante v1.2). À lire d'abord dans l'index `eco3min-projets/context/assets-inventaire.csv` (19/09/2026) : — d'abord `py -3.14 eco3min-projets/tools/assets_sync.py` (incrémental, ~10 s) pour que l'index reflète le site, puis `grep ',hero,' assets-inventaire.csv | grep -E '(,|;)pillar(;|,)' | sort -t, -k7 -r | head -3`, puis ouvrir la colonne `generateur` des deux derniers — format et mode se lisent dans le code. Demander à Paul seulement si `generateur` est vide (hero legacy).
- Éventuelles contraintes spécifiques (chiffres prioritaires, cohérence avec un autre hero déjà produit)

---

## Articulation avec autres skills

- **`brand-kit-eco3min`** — source de vérité pour palette, typographie, codes régime, fond crème, accent terracotta, format sourcing, watermark. Ce skill spécialise pour le cas hero pilier (format 1536×864 strict, layout 6 zones, hiérarchie 5 signaux intra-chart, variantes A/B/C/SM).
- **`visuels-eco3min`** — règles générales de data viz Eco3min (AMF, sourcing, types de chart, anti-patterns finance, qualité technique). Ce skill spécialise pour le cas hero pilier.
- **`formats-eco3min`** — catalogue des formats HTML pour les pages. Ce skill ne traite que du hero, pas du corps de la page.
- **`editeur-eco3min`** — règles éditoriales (ton, AMF, sourcing, anti-patterns IA) qui s'appliquent aussi au texte du hero (titre + sous-titre).
- **`archi-eco3min`** — structure des piliers et URLs (pour les slugs FR/EN et le watermark URL).
- **`production-chart-of-the-week`** — différent objectif (chart viral DIB) mais palette et typo cohérentes via le brand kit. Ne pas confondre les deux missions.

Note d'usage, arbitrages tranchés, workflow et piliers candidats : `references/03-note-usage-arbitrages-workflow.md` (lire avant de proposer un pilier suivant). Version : v1.3 (17/09/2026) — découpage en références, alignement sur le chrome canonique v2.0 (sources gauche / signature droite, zéro cadratin, numérotation de pilier bannie), production en code depuis le CSV réel. Les trois heros piliers livrés en mai 2026 avec le pied inversé restent tels quels jusqu'à leur prochaine itération.

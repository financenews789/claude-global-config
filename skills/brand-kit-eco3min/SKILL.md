---
name: brand-kit-eco3min
description: "Système de design Eco3min v2.0 (17/09/2026), source de vérité des tokens visuels pour toute production visuelle du site et de sa distribution : heros de pilier, de majeur et d'article, charts d'étude et de dataset, images sociales, illustrations ; Chart of the Week est un design à part optimisé pour Reddit, régi par production-chart-of-the-week et exempté du chrome canonique. Activer pour toute création, itération ou révision d'un visuel Eco3min, FR ou EN, et dès qu'une demande contient « hero », « héro », « chart », « graphique », « visuel », « PNG », « palette », « couleur », « typo », « police », « fond crème / blanc / charcoal », « terracotta », « watermark », « signature », « sourcing », « bandeau de chiffres », « stat tiles », « killer phrase », « codes régime », « quelle couleur pour », « c'est dans la charte ? ». Structure : SKILL.md = colonne vertébrale (§0 chrome canonique unique, tokens hex en tableaux, 3 familles typo, 3 registres de fond, règle du terracotta, 3 modes chromatiques, formats stricts, checklist verbatim) ; références dans references/ (à lire quand la section le dit) : 01 typographie détaillée, 02 palette et codes régime en 3 teintes, 03 formats, règles d'usage, sourcing et watermark, 04 articulation et versioning ; scripts/brand_tokens.py = les mêmes tokens en Python (import, jamais de hex recopié) et le contrôle de palette d'un script ou d'un SVG. Doctrines : identité par la structure, variété par la couleur (v1.1) ; chrome canonique invariant v2.0 = titre Source Serif 4 charcoal, sous-titre Inter gris medium, sources mono bas-gauche 2 lignes, signature `Eco3min Research` mono bas-droite (URL en ligne 2 sur les heros), zéro cadratin dans un visuel, jamais de navy ni de numérotation de pilier ; 3 familles typo Source Serif 4 + Inter + IBM Plex Mono et aucune autre ; 3 registres de fond crème #F8F5EE défaut / blanc #FFFFFF majeurs et charts denses / charcoal #1A1A1A inversé ; terracotta #B85C3C = unicité en mode sobre, rang 1 en mode catégoriel ; palette catégorielle 7 rangs dérivée des familles régime pour toute série nommée, direct labeling en bout de ligne ; le seul rouge est #C73E2E et les seuls gris sont les 5 neutres (audit 17/09/2026 : deux heros d'étude livrés en rouge #E03127 et gris Tailwind) ; priorité sémantique des 6 codes régime sur les rangs ; bandeau de chiffres ≤4 tuiles, un seul chiffre terracotta ; rotation anti-monotonie codée dans les skills de production. Hors périmètre : AMF visuelle, choix du type de chart, qualité technique et recettes de rendu (visuels-eco3min) ; provenance et licence des données (sourcing-donnees-eco3min) ; voix éditoriale (editeur-eco3min). Combiner avec visuels-eco3min (toujours), puis selon la famille : production-hero-pilier, production-hero-majeur, production-hero-article-eco3min, production-research-study, production-dataset, sourcing-donnees-eco3min."
---

# Brand kit Eco3min v2.0

> Système de design pour la production visuelle d'Eco3min. Document de référence amont — toutes les productions visuelles (heros piliers, charts, illustrations, datasets, social) s'y conforment.
>
> **Philosophie** : un minimum commun figé (typo + sourcing + watermark + chrome de chart) qui garantit la cohérence perçue, des libertés encadrées sur le reste (type de chart, densité, intensité chromatique, fond, format) qui préservent la diversité éditoriale. Un lecteur de r/economics doit voir « 4 angles d'analyse, même publication » — pas « 4 charts identiques ».
>
> **Doctrine v1.1 — identité par la structure, variété par la couleur.** L'autorité visuelle des références du genre (OWID, FT, Urban Institute) ne vient pas d'une monochromie : elle vient d'un **chrome de chart uniforme** (typographie, hiérarchie titre/sous-titre, footer source, attribution, direct labeling) appliqué à des palettes catégorielles variées mais sourdes. Chez Eco3min, le squelette invariant est : les 3 familles typo, le sourcing footer 2 lignes mono, le watermark, les règles AMF. La couleur, le fond et le format sont des axes de variété **encadrés** — la monotonie chromatique est un défaut au même titre que l'incohérence de marque. Corollaire : le mode « charcoal + 1 terracotta » est UN registre parmi trois (voir §5.2), pas le défaut universel.

---

## COMMENT LIRE CE SKILL (découpage du 17/09/2026)

Ce fichier est la colonne vertébrale : le chrome canonique (§0), tous les tokens (hex, familles, formats) et les règles bloquantes. Le texte complet de chaque section (rationales, configurations fines, 6 codes régime en 3 teintes, articulation, versioning) a été déplacé VERBATIM dans `references/` et fait foi au même titre que ce fichier. Chaque section ci-dessous nomme le fichier à lire ; le lire est obligatoire au moment indiqué. `scripts/brand_tokens.py` porte les mêmes tokens en Python : on l'importe, on ne recopie plus un hex dans un script de chart.

| Fichier | Contenu | À lire |
|---|---|---|
| `references/01-typographie.md` | §1 : les 3 familles, leurs configurations canoniques (tailles, graisses, letter-spacing), fallbacks CSS, dualité web/export | avant de coder le texte d'un visuel (tailles et graisses), et quand une police manque |
| `references/02-palette-codes-regime.md` | §2, §3 : neutres, 3 registres de fond, terracotta, palette catégorielle 7 rangs, couleurs web interdites, 6 codes régime × 3 teintes (zone / ligne / label) | avant de choisir les couleurs d'un chart ; obligatoire dès qu'un régime est nommé ou qu'une zone pâle est tracée |
| `references/03-formats-usage-sourcing-watermark.md` | §4 à §7 : formats canoniques, type de chart, 3 modes chromatiques, annotations, test du terracotta, format des sources, watermark | avant de fixer le format et le mode chromatique, puis avant d'écrire le pied du visuel |
| `references/04-articulation-versioning.md` | §8, §9, versioning, note d'usage : ce que chaque skill compagne reprend du brand kit, historique v1.0 → v2.0 | quand deux skills semblent se contredire sur la charte, et à chaque évolution du brand kit |
| `scripts/brand_tokens.py` | tokens en Python (FONTS, NEUTRALS, BACKGROUNDS, TERRACOTTA, RANKS, REGIMES, SAND, FRAME, SIGNATURE, FORMATS), `PALETTE`, `off_palette()`, `check_source()` | importé par tout script de chart ; lancé en CLI sur le script ou le SVG avant livraison |

Utilisation depuis un script de production :

    sys.path.insert(0, os.path.expanduser('~/.claude/skills/brand-kit-eco3min/scripts'))
    from brand_tokens import FONTS, NEUTRALS, BACKGROUNDS, TERRACOTTA, RANKS, REGIMES, SAND, FRAME, SIGNATURE, FORMATS, check_source
    ...
    assert not check_source(__file__), check_source(__file__)   # aucun hex hors charte dans ce script

Contrôle en ligne de commande, bloquant avant livraison :

    python ~/.claude/skills/brand-kit-eco3min/scripts/brand_tokens.py generate_chart.py hero.svg

---

## 0. Chrome canonique — l'invariant qui fait « même publication » (v2.0)

Audit du 17/09/2026 sur six visuels du site livrés depuis juillet (trois heros d'étude R1, R3, R4, trois charts d'étude R2, R3, R12) : les **formes** sont variées (doubles barres, ligne + barres, nuage, bande d'écart, lollipop, multi-lignes), les fonds alternent crème et blanc, les modes chromatiques alternent. Ce qui fuit, c'est le **chrome** : quatre graphies de signature (`eco3min` serif gris, `eco3min.fr` mono gras, `Eco3min - Research / eco3min.fr`, `Eco3min Research | eco3min.fr`), sous-titres tantôt serif tantôt Inter, deux heros en rouge `#E03127` et gris Tailwind hors charte, un gris `#4A4A4A` ad hoc. Le diagnostic n'est donc pas la monotonie : c'est l'identité diluée. Le chrome ci-dessous ne varie jamais ; la variété se joue dans la forme, la palette et le fond.

**Hors périmètre du chrome §0 : Chart of the Week.** C'est un design à part, optimisé pour performer sur r/dataisbeautiful et non pour le site : `production-chart-of-the-week` (ÉTAPE 3, template V4) fait autorité sur son titre, sa signature `Eco3min` seule, son bandeau et sa palette par registre. Il ne reprend du brand kit que les trois familles typo, les 3 registres de fond et la palette catégorielle comme port d'attache (référence 04, §9).

**Bloquant, sur tout visuel Eco3min :**

- **Titre** : Source Serif 4, weight 600, charcoal `#1A1A1A` (crème `#F8F5EE` sur fond charcoal inversé). Jamais navy `#1A237E` ni aucun bleu : le navy est l'identité du site web (§2.4), pas des visuels.
- **Sous-titre / deck** : Inter, weight 400, gris medium `#757575`. Le Source Serif italique est réservé aux citations et pull-quotes, jamais au sous-titre descriptif.
- **Pied, bas-gauche** : les sources, IBM Plex Mono 9–10 px gris medium, 2 lignes (ligne 1 `Sources: …` avec codes de série ; ligne 2 date, méthode en une ligne, `values rounded for readability` si arrondi).
- **Pied, bas-droite** : la signature, IBM Plex Mono, `Eco3min Research` ligne 1 ; ligne 2 = URL de la page sur les heros (pilier, majeur, article) et les études ; ligne 1 seule sur un chart social distribué hors site. Aucune autre graphie (`eco3min`, `Eco3min — Research`, `Chart: Eco3min`), aucun logo.
- **Zéro cadratin (`—`) dans les textes courants d'un visuel** (sous-titre, annotations, bandeau, sources, signature) : séparateur `·`, plages en demi-cadratin ou tiret. Même règle que le texte du site (`editeur-eco3min`). Seule exception : le séparateur du tag de registre mono (`… — PILIER`, `MAJEUR — …`), convention en place sur les heros livrés.
- **Tag de registre**, haut-gauche, IBM Plex Mono uppercase : `[PILIER] — PILIER` sur un hero pilier, `MAJEUR — [PILIER PARENT]` sur un majeur, `[NOM DU PILIER]` sur un hero d'article ; **jamais de numérotation « PILIER 03 / 10 »** (numéros faux issus de tables locales divergentes de `archi-eco3min`).
- **Bandeau de chiffres (stat tiles)**, quand un visuel en porte : 4 tuiles maximum sur une ligne ; chiffre en Inter weight 600 `tabular-nums` 36–44 px charcoal, **un seul chiffre en terracotta** (le focus), jamais un chiffre en mono ; libellé Inter 12–13 px charcoal ; sous-libellé IBM Plex Mono 10 px gris medium ; séparateurs filet `#DED7C7` sur crème, `#E0E0E0` sur blanc.
- **Killer phrase / bandeau éditorial** : Inter weight 500 charcoal, habillage léger = filet terracotta de 4 px à gauche + fond sand `#F2EAD8` ; jamais de pavé plein bordé.
- **Couleurs** : uniquement les tokens de §2 et §3. Le seul rouge est `#C73E2E` ; les seuls gris sont les 5 neutres de §2.1. Un hex qui n'est pas dans `brand_tokens.PALETTE` est un défaut bloquant, pas une nuance.
- **Contrôle** : `check_source()` sur le script ou le SVG avant livraison ; sur matplotlib, les assertions de `visuels-eco3min` §7 ter (police rendue, débordement, chevauchement, `$`, sources avant signature).

---

## 1. Typographie — 3 familles fixes, aucune autre (lire `references/01-typographie.md` avant de coder le texte)

| Rôle | Famille | Usage bloquant |
|---|---|---|
| Serif éditorial | **Source Serif 4** | titres, titres descriptifs de métrique, citations |
| Sans-serif | **Inter** | sous-titres, annotations chiffrées, labels d'axes, légendes, chiffres des tuiles ; `font-variant-numeric: tabular-nums` obligatoire sur les axes |
| Monospace | **IBM Plex Mono** | codes de série, sources, signature, labels catégoriels uppercase, tags de registre |

- Configurations canoniques (tailles, graisses, letter-spacing) et fallback chains : référence 01.
- Les polices ne sont pas installées sur le poste : matplotlib retombe sur DejaVu Sans et Chromium sur la police de repli **sans erreur**. La famille rendue s'asserte (`visuels-eco3min` §7 bis et §7 ter).
- IBM Plex Mono n'a ni U+2009 ni U+202F : rester en ASCII dans les textes de visuel, ou vérifier le cmap de chaque glyphe non ASCII.
- Le site web utilise une autre triade (Libre Baskerville + DM Sans + JetBrains Mono) : dualité assumée, aucune règle ne demande d'unifier (§1.4 en référence).

---

## 2. Palette — tokens (lire `references/02-palette-codes-regime.md` avant de choisir les couleurs)

### 2.1 Neutres

| Rôle | Hex |
|---|---|
| Charcoal (texte primaire, séries principales) | `#1A1A1A` |
| Gris medium (texte secondaire, séries d'arrière-plan, axes) | `#757575` |
| Gris light (grille, séparateurs) | `#C4C4C4` |
| Gris très light (zones secondaires, axes) | `#E0E0E0` |
| Filet crème (cadre des heros d'article, séparateurs sur crème) | `#DED7C7` |
| Sand (fond du bandeau killer phrase) | `#F2EAD8` |
| Sand border (bordure du bandeau sur crème) | `#E5DFD3` |

### 2.2 Fond — 3 registres officiels

| Registre | Hex | Usage |
|---|---|---|
| Crème éditorial | `#F8F5EE` | **défaut** : heros piliers, heros d'article (V3), charts d'articles, datasets, illustrations |
| Blanc pur | `#FFFFFF` | **heros MAJEUR** (convention gravée) ; charts à richesse chromatique élevée (≥4 séries, heatmaps, matrices) |
| Charcoal inversé | `#1A1A1A` | formats spéciaux assumés (Time Machine, certains cycles Chart of the Week) ; jamais pour la série des heros piliers |

### 2.3 Accent terracotta `#B85C3C`

**Mode sobre** : UN marqueur principal par chart (ligne verticale, point annoté, OU zone — pas plusieurs simultanément) + son label nominal éventuel. **Mode catégoriel** : couleur du rang 1 de la palette catégorielle (§2.5) — la série focus/principale. **Test** : si tu peux retirer 2 occurrences de terracotta sans dégrader la lecture de la thèse, retire-les. Même en mode catégoriel, un chart à thèse désigne UN focus visuel, pas cinq.

### 2.4 Couleurs web, interdites dans un visuel

Navy `#1A237E` et or `#C9A84C` sont réservés aux composants UI du site. Un chart Eco3min ne doit pas en contenir.

### 2.5 Palette catégorielle — 7 rangs, pour toute série nommée

| Rang | Nom | Hex |
|---|---|---|
| 1 | Terracotta (série focus, toujours en premier) | `#B85C3C` |
| 2 | Bleu acier (paire par défaut avec le rang 1) | `#4A6B8A` |
| 3 | Vert sourd | `#6B8E5F` |
| 4 | Violet pourpre | `#6B4A6B` |
| 5 | Ocre sourd | `#B8854A` |
| 6 | Charcoal doux | `#4A3F3D` |
| 7 | Rouge sourd (dernier rang délibéré, le seul rouge de la charte) | `#C73E2E` |

Bloquant : priorité sémantique des codes régime (§3) sur les rangs ; ordre des rangs respecté (un chart 3 séries = rangs 1-2-3) ; plafond 6-7 séries, au-delà spaghetti focus (N séries en `#C4C4C4` / `#757575` + 1-2 séries aux rangs 1-2) ; direct labeling en bout de ligne obligatoire ≤6 séries, légende détachée bannie ; rouge et vert jamais seule distinction entre deux séries adjacentes ; zones pâles = teinte « zone » de la famille régime correspondante ; aucune teinte hors de ces 7 rangs + neutres + codes régime.

---

## 3. Codes régime — 6 familles × 3 teintes (lire `references/02-palette-codes-regime.md` dès qu'un régime est nommé)

| Axe | Régime | Zone | Ligne | Label |
|---|---|---|---|---|
| macro | Inflationniste | `#F4DDD8` | `#C73E2E` | `#8B2A1F` |
| macro | Désinflationniste | `#D8E2EC` | `#4A6B8A` | `#2D4256` |
| macro | Stagflation | `#ECE2D2` | `#B8854A` | `#6E4E2B` |
| monétaire | Liquidité abondante | `#DCE5D6` | `#6B8E5F` | `#3E5536` |
| monétaire | Restriction | `#DDD4DD` | `#6B4A6B` | `#3E2A3E` |
| monétaire | Crise systémique | `#D8D5D3` | `#4A3F3D` | `#1F1A18` |

**Si le visuel nomme explicitement un régime dans son texte** (titre, sous-titre, annotation, légende), il **doit** utiliser la couleur de ce régime. Ne pas inventer une teinte ad hoc. Plusieurs régimes simultanés : le code de chacun pour sa portion.

---

## 4. Formats stricts (lire `references/03-formats-usage-sourcing-watermark.md` avant de fixer le format)

| Visuel | Dimensions | Skill |
|---|---|---|
| Hero pilier | **1536×864** strict | `production-hero-pilier` |
| Hero majeur | **1536×864** strict | `production-hero-majeur` |
| Hero d'article (V3) | **1200×630** strict | `production-hero-article-eco3min` |
| Chart of the Week | **1920×1080**, un seul rendu | `production-chart-of-the-week` |
| Charts d'étude, de dataset, social | libres ; ce qui compte est le ratio et la lisibilité au repartage (social 1200×675 ou 1080×1080) | |

Les trois formats de hero alimentent des gabarits WordPress et des cartes de partage : y déroger casse le cadrage en aval. Tout visuel se teste à **380 px** de large.

---

## 5. Modes chromatiques et rotation (lire `references/03-formats-usage-sourcing-watermark.md` avant de choisir le mode)

- **Mode sobre** (charcoal + 1 terracotta) : charts à 1 série, thèse qui tient dans UN marqueur. Ce n'est **plus le défaut universel**.
- **Mode catégoriel** (palette §2.5) : dès que le chart distingue N séries nommées — régimes, pays, actifs, secteurs, époques. Le format signature OWID/FT.
- **Gradient continu** : quand le chart code une dimension continue. Jamais pour distinguer des catégories.
- **Anti-monotonie (règle de série)** : au sein d'une même famille de visuels, ne pas enchaîner plus de 2-3 productions consécutives dans le même mode chromatique. La rotation opérationnelle est codée dans `production-hero-pilier` (rotation bloquante) et, pour son propre design, dans `production-chart-of-the-week` (ÉTAPE 3-BIS).
- **Annotations interdites** (détail AMF dans `visuels-eco3min` §2) : flèches achat/vente, zones « buy/sell », cibles de prix, timing actionnable, symboles ↗ ↘ sans contexte numérique. Aucune échelle « bien / mal » (dégradé vert→rouge) sur des pays ou des groupes.
- **Type de chart** : libre selon ce qui sert la donnée ; règles fines dans `visuels-eco3min` §3.

---

## 6. et 7. Sourcing et signature (lire `references/03-formats-usage-sourcing-watermark.md` avant d'écrire le pied)

Le chrome §0 fixe la position et la graphie. Le format des deux lignes de sources est bloquant :

```
Ligne 1 — Sources: [Institution] ([codes série]); [Institution] ([série]); …
Ligne 2 — Updated [mois année] · [méthodologie résumée en 1 ligne] · Values rounded for readability
```

Codes de série explicites (pas seulement « Federal Reserve ») ; date d'extraction si donnée vivante ; le timestamp n'apparaît qu'en ligne 2, jamais dupliqué en haut du visuel. La mention Eco3min est portée par la signature bas-droite, une seule fois.

---

## 8. Anti-patterns visuels et articulation (lire `references/04-articulation-versioning.md` en cas de conflit entre skills)

Les 7 interdictions AMF, les anti-patterns data viz (3D, pie chart > 3 segments, gradient décoratif) et la qualité technique sont gravés dans `visuels-eco3min` §2, §3, §7 : indépendants du brand kit, ils s'appliquent à tout visuel. Les skills de production du site (`production-hero-pilier`, `production-hero-majeur`, `production-hero-article-eco3min`, `production-research-study`, `production-dataset`) spécialisent ce brand kit ; en cas de désaccord sur la charte, **ce fichier gagne** et la divergence se remonte ici. `production-chart-of-the-week` est l'exception : design Reddit à part, il gagne sur son propre visuel.

---

## 10. Checklist pré-livraison d'un visuel

**Typographie**
- [ ] Source Serif 4 utilisé pour titre / sous-titre
- [ ] Inter utilisé pour annotations et chiffres
- [ ] IBM Plex Mono utilisé pour sources et codes série
- [ ] Pas d'autre famille de polices

**Palette**
- [ ] Fond = un des 3 registres §2.2 (crème défaut / blanc / charcoal inversé), choix justifié par la famille de visuel
- [ ] Texte primaire en charcoal `#1A1A1A` (ou crème sur fond charcoal inversé)
- [ ] Mode chromatique identifié : sobre / catégoriel / gradient (§5.2)
- [ ] Mode sobre : accent terracotta `#B85C3C` à 1 occurrence MAX
- [ ] Mode catégoriel : rangs de la palette §2.5 respectés dans l'ordre, ≤6-7 séries, direct labeling en bout de ligne
- [ ] Si régime nommé : couleur du code régime utilisée (priorité sémantique sur les rangs)
- [ ] Rouge `#C73E2E` / vert `#6B8E5F` jamais seule distinction entre 2 séries adjacentes
- [ ] Aucune teinte ad hoc inventée hors rangs, neutres et codes régime

**Sourcing**
- [ ] Source intégrée dans le visuel (pied)
- [ ] Codes série explicites (pas seulement « Federal Reserve »)
- [ ] Mention « Eco3min Research » ou équivalent
- [ ] Date d'extraction si donnée vivante

**Anti-patterns AMF**
- [ ] Aucune flèche achat/vente
- [ ] Aucune cible de prix
- [ ] Aucune zone prescriptive
- [ ] Annotations descriptives uniquement

**Qualité technique**
- [ ] Aucun chevauchement texte / texte / courbe
- [ ] Aucune troncature
- [ ] Lisibilité testée à 380 px de largeur (mobile feed)
- [ ] Accents corrects sur majuscules (« É », « À »)

**Chrome canonique v2.0**
- [ ] Titre charcoal (jamais navy), sous-titre Inter gris medium
- [ ] Sources bas-gauche 2 lignes mono ; signature `Eco3min Research` bas-droite (+ URL sur un hero)
- [ ] Zéro cadratin dans les textes courants du visuel (seul le tag de registre en porte un)
- [ ] Tag de registre sans numérotation de pilier
- [ ] Bandeau de chiffres : ≤4 tuiles, un seul chiffre terracotta, chiffres en Inter tabular
- [ ] `check_source()` passé sur le script ou le SVG : aucun hex hors `PALETTE`

---

## Versioning (historique complet dans `references/04-articulation-versioning.md`)

- **v2.0** (17/09/2026) — découpage en références + `scripts/brand_tokens.py`, et **chrome canonique §0** après audit de six visuels du site livrés depuis juillet : les formes et les modes varient correctement, le chrome fuit (quatre graphies de signature, sources à gauche ou à droite selon la famille, sous-titres serif ou Inter, deux heros en rouge `#E03127` et gris Tailwind). Chart of the Week explicitement exempté du chrome §0 : design à part pour Reddit, `production-chart-of-the-week` fait autorité. Décisions : sous-titre = Inter ; sources bas-gauche et signature `Eco3min Research` bas-droite sur toutes les familles (les trois heros piliers livrés en mai 2026 avec le pied inversé restent tels quels jusqu'à leur prochaine itération) ; zéro cadratin ; navy interdit ; numérotation de pilier bannie partout ; tokens sand et filet crème gravés ; spec des bandeaux de chiffres ; le seul rouge est `#C73E2E` ; contrôle de palette par script. Aucune règle de palette, de typo ou de régime modifiée.

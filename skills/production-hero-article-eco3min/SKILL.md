---
name: production-hero-article-eco3min
description: "Production du héro V3 d'un ARTICLE Eco3min (satellite ou article courant), bilingue FR/EN, 1200×630 sur fond crème avec cadre #DED7C7 — troisième registre de la famille héro, à côté de production-hero-pilier (territoire, 1536×864, dense) et production-hero-majeur (thèse, fond blanc, aéré). Activer pour toute conception ou réparation de héro d'article : « héro de l'article », « hero V3 », « repair image », « V3 Worklist », « regénère l'image de l'article », « eco3min-v3-{post_id}.png », « kicker », « le visuel est une V2 déguisée », « paire FR/EN du héro », « cadre crème », « 1200×630 ». Skill courte, non découpée : tout sert à chaque invocation. Pas de scripts/ propres (gardes : brand-kit-eco3min/scripts/brand_tokens.py et visuels-eco3min/scripts/mpl_guards.py ; recette Playwright dans visuels-eco3min references/03). Doctrines : rendu en code (HTML/SVG → PNG), jamais une illustration raster ni une photo ; hiérarchie stricte des idées visuelles — l'objet même de l'article dessiné en vraie donnée > comparaison chiffrée vérifiée > diagramme conceptuel sur-mesure > archétype générique interdit ; test d'échec « V2 déguisée » : si le visuel pourrait illustrer trois autres articles du domaine, recommencer ; « pas de chiffre de timing » n'est pas « pas de donnée » ; le minimalisme se gagne par une forme forte, pas par absence d'idée ; cohérence de paire figée : un concept, mêmes données, même composition, rendu une fois par langue, avec l'exception des paires juridictionnelles où les chiffres sont exacts par juridiction ; socle 1200×630, crème, filet #DED7C7 inset ~26 px, terracotta unique, kicker = nom du pilier déduit via archi-eco3min sans numérotation, titre = h1 verbatim ; chrome canonique brand-kit v2.0 §0 (sources bas-gauche, signature Eco3min Research + eco3min.fr bas-droite, zéro cadratin) ; gate 2.0 : aucun chiffre non vérifié, source légalement publiable, pas de points décoratifs, AMF ; quand la source contredit l'article, le visuel suit la source et l'article est signalé ; méthode en 7 étapes avec annonce en une ligne avant de rendre et QA (accent unique, collisions, débordement, accents sur capitales, palette). Hors périmètre : plomberie du pipeline V3 (JSON d'export/import, boucle Worklist / Apply → Eco3min repair image/CLAUDE.md) ; tokens (brand-kit-eco3min) ; AMF visuelle et rendu (visuels-eco3min) ; piliers (archi-eco3min) ; sources (sourcing-donnees-eco3min). Combiner avec brand-kit-eco3min, visuels-eco3min, archi-eco3min, sourcing-donnees-eco3min, editeur-eco3min."
---

# Production — Héro V3 d'un article Eco3min

## Statut

Formalisé septembre 2026 par extraction du projet « repair image », qui portait
cette doctrine dans son `CLAUDE.md` depuis la V3. Pipeline mature : des dizaines
de paires livrées sur neuf piliers.

Charte de fond (palette, typo, fonds, sourcing) : **`brand-kit-eco3min` fait
autorité**. AMF visuelle, choix de chart, qualité technique, recette de rendu
Playwright : **`visuels-eco3min` fait autorité**. Liste et numérotation des
piliers : **`archi-eco3min` fait autorité**. Légalité et provenance des données
tracées : **`sourcing-donnees-eco3min` fait autorité**.

## Mission

Le héro placé en tête d'un article courant. C'est un **asset de citation** : il
voyage seul en repartage, capture, AI Overview, sans le corps de l'article.

Rendu en **code** (HTML/SVG → PNG). Jamais une illustration raster générée.
Jamais une photo.

## Place dans la famille héro

| | PILIER | MAJEUR | **ARTICLE (V3)** |
|---|---|---|---|
| Montre | un territoire de silo | une thèse défendable | **l'objet propre de cet article** |
| Fond | crème `#F8F5EE` | blanc `#FFFFFF` | **crème `#F8F5EE`** |
| Format | 1536×864 strict | 1536×864 | **1200×630** |
| Composition | dense, cartographique | aérée, un geste | **compacte, un dispositif** |
| Tag | `PILIER — …` | `MAJEUR — [pilier parent]` | **`NOM DU PILIER`** |

## Le saut V3 — le cœur du skill

La V2 était un héro typographique plus un diagramme abstrait piocké dans une
bibliothèque d'archétypes (lag, divergence, cycle…) puis annoté.

**Test d'échec** : si le visuel pourrait illustrer trois autres articles du même
domaine, c'est une V2 déguisée. Recommencer.

### Hiérarchie des idées visuelles (ordre de préférence strict)

1. **L'objet même de l'article, dessiné depuis de vraies données.** Article sur
   la courbe des taux inversée → dessiner **la courbe inversée**, pente réelle,
   points court et long réels. Article sur une hiérarchie de performances → le
   classement réel, les écarts réels. Article sur le cycle du crédit → la forme
   réelle du cycle. C'est ça, la V3 : on dessine **la chose**, pas une métaphore
   interchangeable.
2. **Une comparaison ou un repère chiffré vérifié**, toujours sourcé.
3. **Un diagramme conceptuel sur-mesure** — seulement si l'article n'a aucun
   objet dessinable ni donnée vérifiable. Et même là, composé pour cet
   article-là, pas instancié depuis un template.
4. **L'archétype abstrait générique** = dernier recours absolu, à éviter.

**« Pas de chiffre de timing » ≠ « pas de donnée ».** On peut presque toujours
dessiner une **forme réelle** — une courbe, une structure, une répartition —
sans énoncer la moindre prévision. Chercher cette forme avant d'abandonner
l'option 1.

Corollaire, aligné sur la règle « preuve d'abord » de `production-hero-majeur` :
si l'article a une preuve empirique disponible, la forme doit la **montrer**, pas
l'illustrer.

### Densité

Le vide peut être un parti pris, mais une image quasi vide avec trois labels lit
« pauvre », pas « épuré ». Si le minimalisme est choisi, il doit être **gagné**
par une forme forte, pas subi par absence d'idée.

## Cohérence de paire FR/EN — règle figée

**Un seul concept, mêmes données, même composition.** Le visuel est conçu une
fois, puis rendu une fois par langue.

Ne changent que : le titre (le `h1` de chaque langue, **verbatim**), la langue du
kicker et des labels, le texte des annotations.

On ne redessine **jamais** un concept différent par langue.

⚠️ **Exception données.** Beaucoup de paires sont des adaptations
juridictionnelles (le FR couvre les instruments et le droit français, l'EN les
équivalents US) plutôt que des traductions. Grammaire visuelle commune, mais
**chiffres exacts par juridiction** : reprendre le chiffre FR côté EN serait
faux. Le repérer à la lecture des deux `full_text`.

## Socle de design verrouillé

Ce qui suit spécialise `brand-kit-eco3min` pour ce registre. Tout ce qui n'est
pas listé ici suit le brand kit sans exception.

- **Format 1200×630.**
- Fond crème `#F8F5EE`, texte charcoal `#1A1A1A`, gris `#757575`.
- **Cadre : filet fin `#DED7C7` en inset ~26 px.** Signature du registre article.
- Terracotta `#B85C3C` = **accent unique** : une seule occurrence, sur l'élément
  porteur de la thèse. Jamais deux zones terracotta.
- Trois familles typo, rien d'autre : Source Serif 4 (titre), Inter (thèse et
  labels), IBM Plex Mono (kicker, pied, sourcing).
- **Kicker** en haut-gauche : le nom du pilier, mono, capitales, letter-spacing.
  Le pilier se déduit de `pillar` / `sub_pilier` via **`archi-eco3min`**, seule
  source. Introuvable → kicker neutre « Analyse macro-financière » /
  « Macro-Financial Analysis ».
  ⚠️ **Pas de numérotation « / NN »** — même convention que
  `production-hero-majeur`. Les tables de piliers recopiées dans les projets ont
  divergé de `archi-eco3min` et produit des numéros faux ; le dénominateur est
  supprimé pour fermer définitivement la faille.
- **Pied** (chrome canonique `brand-kit-eco3min` v2.0 §0) : sources bas-gauche en IBM Plex Mono quand le héro porte une donnée ; signature bas-droite `Eco3min Research` ligne 1, `eco3min.fr` ligne 2, IBM Plex Mono. Zéro cadratin dans les textes courants du visuel.
- Titre = le `h1` de l'article, **verbatim**. Langue du kicker et des labels =
  le champ `lang`.

## Gate 2.0 — intégrité des données et AMF (non négociable)

Même gate que `production-hero-majeur`, appliqué au registre article.

- **Aucun chiffre non vérifié** sur l'image. Impossible de sourcer une valeur en
  direct → **pas de chiffre**, et on bascule sur un héro conceptuel.
- Toute donnée affichée porte **sa source et sa date**, en mono, discret.
- La source doit être **légalement publiable**, pas seulement réelle : voir
  `sourcing-donnees-eco3min`. Pas de Yahoo ni d'agrégateur scrapé.
- S'étend à toute forme qui *ressemble* à de la donnée : nuage, distribution,
  dispersion. Pas de points décoratifs qui miment une série.
- Interdits AMF : flèches achat/vente, cibles de prix, zones prescriptives,
  « buy » / « sell », recommandations. Descriptif uniquement.
- Pas de logo géant : attribution discrète, pas branding.

**Quand la source primaire contredit le corps de l'article** : le visuel est
construit sur la donnée correcte, et c'est **l'article** qui est signalé pour
correction. Jamais l'inverse.

## Méthode

1. Lire les `full_text` des deux langues, plus `h1` et `meta_description`.
   Formuler en une phrase la **thèse** et le **mécanisme** central, communs aux
   deux langues.
2. Choisir l'idée visuelle unique selon la hiérarchie ci-dessus.
3. Si option données : vérifier chaque valeur sur source primaire. Noter source
   et date. Échec → conceptuel, sans chiffre.
4. **Annoncer en une ligne avant de rendre** : thèse + visuel choisi + source de
   donnée (ou « conceptuel, sans donnée » et pourquoi).
5. Composer le visuel une fois, le rendre une fois par article. Recette de rendu
   Playwright et séquence de chargement des polices : `visuels-eco3min` §7 bis (`references/03-rendu-playwright.md`) ; en matplotlib, `mpl_guards.run_guards` avant `savefig` (§7 ter).
6. QA : accent terracotta unique, collisions de labels, débordement du cadre, palette (`brand_tokens.check_source` sur le script ou le SVG, aucun hex hors charte),
   accents sur capitales.
7. Remonter jusqu'à trois signalements éditoriaux hiérarchisés.

## Anti-patterns

- **Archétype générique annoté** — la V2 déguisée. Le défaut n°1.
- **Second accent terracotta** — numéro de kicker, point séparateur, label
  d'annotation ou trait de connecteur passés en terracotta. La violation la plus
  fréquente en QA.
- **Courbe dessinée de mémoire** — polyligne « à l'œil » au lieu du CSV réel.
- **Chiffre FR recopié côté EN** sur une paire juridictionnelle.
- **Numéro de pilier inventé** — recopier une table de piliers locale au lieu de
  lire `archi-eco3min`.
- Emoji, photo, raster IA, plus de trois polices.

## Articulation

- `brand-kit-eco3min` — charte. Ce skill spécialise pour le registre article.
- `visuels-eco3min` — AMF, choix de chart, qualité technique, **recette de rendu
  PNG (Playwright, §7 bis)**.
- `production-hero-pilier` / `production-hero-majeur` — les deux autres registres.
- `archi-eco3min` — piliers, slugs, symétrie FR/EN.
- `sourcing-donnees-eco3min` — provenance et légalité des données tracées.
- `editeur-eco3min` — AMF côté texte du titre.

La plomberie du pipeline V3 — schéma du JSON d'export, JSON d'import, boucle
V3 Worklist / Apply — vit dans `Eco3min repair image/CLAUDE.md`, pas ici.

## Versions

- **V3** (septembre 2026) — extraction du projet « repair image ».
- **V3.1** (17/09/2026) — description réécrite ; pied aligné sur le chrome canonique `brand-kit-eco3min` v2.0 §0 (sources bas-gauche, signature `Eco3min Research` + `eco3min.fr` bas-droite, zéro cadratin) ; contrôle de palette ajouté à la QA ; pointeurs vers les références de `visuels-eco3min`. Aucune règle de fond modifiée. Skill volontairement non découpée (173 lignes, tout sert à chaque invocation).

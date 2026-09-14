---
name: production-hero-majeur
description: Production des visuels hero des pages MAJEUR d'eco3min.fr (article de fond d'un cluster), FR/EN. Activer pour créer/itérer un hero de majeur. Logique opposée au pilier : argument visuel d'UNE thèse (renversement consensus→thèse), pas cartographie d'un territoire. Identité : fond blanc (vs crème pilier), compo éditoriale aérée, tag MAJEUR — [pilier parent]. Liberté de forme (menu ouvert, courbe NON défaut, anti-répétition) sur socle d'honnêteté minimal. Couvre : thèse/renversement/preuve, gate 2.0 données réelles (rien de chiffré sans CSV ; toute forme qui IMPLIQUE de la donnée y tombe, pas de points décoratifs), vérif méthode/label 2.3 (formule = label, jamais 'Damodaran' sur ce qui n'en est pas), règle 'preuve d'abord' (concept réservé aux thèses sans preuve chiffrable), socle verrouillé (typo 3 familles, terracotta unique, sourcing, AMF, 1536×864), 3 tests. Combiner avec brand-kit-eco3min, visuels-eco3min, editeur-eco3min, archi-eco3min ; pendant de production-hero-pilier.
---

# Production — Hero visuel pour article MAJEUR Eco3min

## Statut

**Skill temporaire v0.3** (juillet 2026 ; v0.2 mai 2026), créé après itération sur le majeur « markets reorganize around rates », resynchronisé après l'épisode sourcing/légalité du même cas, aligné en v0.3 sur `brand-kit-eco3min` v1.1 (convention fond blanc gravée, palette catégorielle §2.5 disponible). Dérive du prompt `prompt-hero-majeur-eco3min` v2.1 (version Claude Design). À durcir après 2-3 majeurs livrés — voir « À actualiser ». Charte de fond (palette, typo, codes régime) : **`brand-kit-eco3min` est la source de vérité** ; provenance/licence des données tracées : **`sourcing-donnees-eco3min` est la source de vérité.**

## Mission

Hero placé en tête d'un article **MAJEUR** (article de fond qui ancre un cluster MAJEUR + satellites), bilingue FR/EN. Benchmark FT / Bloomberg / Les Échos. C'est un **asset de citation** : il voyage seul sur Reddit / X / AI Overview, sans le corps de l'article.

## Principe directeur — majeur ≠ pilier

| | Hero de PILIER | Hero de MAJEUR |
|---|---|---|
| Montre | un **territoire** de silo | **une thèse** défendable, souvent à contre-courant |
| Répond à | « de quoi parle ce silo ? » | « quelle affirmation cet article démontre-t-il ? » |
| Réussite | situer le champ couvert | capter le **renversement** consensus → thèse |
| Échec | trop étroit | **décrire le sujet** au lieu de prouver l'affirmation |

**Test d'échec** : si le visuel pourrait illustrer trois autres articles du domaine, il porte le sujet, pas la thèse.

## Identité visuelle majeur (distincte du pilier)

- **Fond blanc `#FFFFFF` par défaut** (vs crème `#F8F5EE` pilier). Crème ou charcoal `#1A1A1A` inversé acceptés en variante assumée.
- **Composition éditoriale aérée** : UN geste dominant, marge haute généreuse, titre plus grand, peu d'éléments, beaucoup de respiration. Pas cartographique.
- **Tag** `MAJEUR — [PILIER PARENT]` (pas de numérotation « / 10 »).
- ✅ « Fond blanc = majeur » est **gravé dans `brand-kit-eco3min` v1.1 §2.2** (3 registres de fond : crème défaut / blanc majeurs et charts denses / charcoal inversé formats spéciaux). Plus de risque de dérive inter-skills.
- **Palette catégorielle disponible** : pour les formes multi-séries du menu (comparaison/divergence, small multiples, dumbbell multi-entités), utiliser la palette 7 rangs du brand kit §2.5 avec direct labeling — le terracotta reste le rang 1 / la série focus. L'unicité terracotta ne vaut qu'en mode sobre.

## Liberté de forme (le cœur du skill)

Menu ouvert. **La courbe n'est PAS le réflexe** — réservée aux thèses qui *sont* une trajectoire dans le temps. **Pas deux majeurs consécutifs sur la même forme** (diversité = objectif). Donner en input la forme du majeur précédent pour ne pas la rejouer.

Formes (non limitatif, selon la forme de la thèse) : comparaison/divergence · diagramme conceptuel · small multiples 2×2 · matrice/heatmap · distribution/ridge/**dumbbell** · « un grand chiffre » éditorial · hero typographique/pull-quote data-ancré · composition hybride · série temporelle anchor (en dernier recours).

**Règle d'or** : la liberté n'est pas l'empilement. UN dispositif dominant par hero.

## Process

### 1 — Thèse / renversement / preuve (bloquant)
Écrire : (a) la thèse en une phrase (l'affirmation, pas le sujet) ; (b) contre quel consensus ; (c) quelle **donnée ou rapport** rend le renversement visible — la preuve montre le renversement, pas le sujet. Si la thèse n'est pas univoque, le signaler.

### 2 — Données réelles + méthode (bloquant ; s'applique dès que le visuel chiffre OU *implique* de la donnée)

**Gate 2.0 — absolu.** Aucune série chiffrable tracée sans le **CSV/XLSX réel ET légalement publiable** (voir `sourcing-donnees-eco3min` : pas de Yahoo/agrégateur scrapé pour un visuel publié ; sources propres = primaires publiques type FRED/ECB, émetteur, API licenciée, ou séries académiques type Fama-French ; footer = source réelle). Pas de polyligne « à l'œil ». Si la donnée manque → **s'arrêter** et la réclamer (nom, code, source, période, fréquence par série) ; avancer en mode schéma non chiffré en attendant. **Extension** : toute forme qui *ressemble* à de la donnée (nuage, distribution, dumbbell, matrice, « champ » de dispersion) est construite sur le CSV réel — **pas de points décoratifs**. Un dispersion field inventé = la courbe eyeballed en version diagramme, interdit. Seules les formes **manifestement schématiques** (relations, flux, pull-quote) échappent au gate.

**2.1 Faisabilité.** Couverture de période vérifiée ; série incomplète → proposer proxy/disclosure/recadrage, ne pas trancher en silence.

**2.2 Rigueur métrique.** Proxy = LE standard académique du concept (coût du capital → TIPS `DFII10` ; prime duration → ACM term premium NY Fed ; prime crédit → HY OAS `BAMLH0A0HYM2` ; vol → `VIXCLS`). Test : la métrique fait-elle ce qu'elle prétend sur **toute** la période ?

**2.3 Méthode ET label (le contrôle qui attrape les erreurs).** Pour toute série construite : (1) formule exacte écrite ; (2) **jamais un nom de méthode** (Damodaran, Shiller, ACM) sur une construction qui n'en est pas une — `E/P forward − TIPS 10Y` n'est PAS « Damodaran », c'est « ERP simple » ; (3) footer = formule réellement tracée ; (4) **sanity-check magnitude** vs ordre de grandeur connu, signalé *avant* de tracer.

**Règle « preuve d'abord » (prioritaire sur le choix de forme).** Une forme **conceptuelle/typographique** n'est légitime **que si la thèse n'a pas de preuve chiffrable disponible**. Si l'article a la preuve empirique, la forme doit la **montrer**, pas l'**illustrer** — montrer ≠ courbe (dumbbell, nuage réel, matrice gardent la variété en prouvant).

### 3 — Choisir la forme (menu ci-dessus)
### 4 — 2-3 options de **formes différentes** → arbitrage de Paul avant production
### 5 — Production finale FR puis EN
Valeurs/polylignes depuis le CSV. Footer = formule validée (2.3). Variante EN : même composition, mêmes données, texte seul change ; titre dense, rythme conservé.

## Socle verrouillé (non négociable, court)

- **Honnêteté data** — gate 2.0 + 2.3 ; axes jamais tronqués ; proxy/composite signalé dans le visuel ET en footer.
- **Typo — 3 familles, aucune autre** (signature Eco3min) : Source Serif 4 (titres) · Inter (chiffres/axes, `tabular-nums`) · IBM Plex Mono (codes, tags, sourcing).
- **Accent terracotta `#B85C3C`** — un seul rôle accentué par visuel, jamais un cluster ; un accent isolé sans signification est à retirer.
- **Sourcing footer 2 lignes + watermark `Eco3min — Research` + URL** ; codes série explicites ; mention Eco3min toujours présente.
- **AMF** — aucune flèche/zone achat-vente, aucune cible de prix, annotations descriptives, aucun terme dramaturgique. « Marquer » = clarté du renversement, pas sensationnalisme.
- **Export 1536×864**, lisible à 380 px.

## 3 tests avant livraison
1. **Comptage non-initié** — si le titre annonce N éléments, ils sont comptables sur le visuel.
2. **Mobile 380 px** — aucun chevauchement.
3. **Lecture 5 s, thèse-led** — masquer titre/sous-titre : le renversement se capte par le visuel seul ? Sinon il est porté par le texte → revoir. Le plus important pour un majeur.

## Anti-patterns observés (session mai 2026)
- **Courbe eyeballed** — polyligne dessinée de mémoire au lieu du CSV (1er majeur taux).
- **Label méthode faux** — « méthode Damodaran » sur un `E/P − TIPS` (≠ Damodaran). Magnitude 1,7 % incohérente avec la méthode affichée.
- **Dispersion field décoratif** — nuage de points inventés qui *mime* la donnée sur une thèse pourtant data-riche (MSCI Growth/Value dispo). Concept là où la preuve existait.
- **Terracotta isolé sans sens** — un 2e accent décoratif (point unique dans un champ) qui dilue l'accent principal.
- **Source non publiable** — données ETF récupérées via Yahoo (yfinance) pour un visuel publié sur site commercial : CGU restrictives. Résolu en passant à une source légalement propre (voir ci-dessous).

## Pattern de résolution réussi (cas « markets reorganize around rates »)
La bonne sortie du même cas, après corrections : **dumbbell value/growth × 5 années (2022→mars 2026)**, barre terracotta = l'écart, pic de cycle (−49 pts mars 2026) mis en valeur. Pourquoi ça marche : (1) **forme ≠ courbe** qui *montre* la preuve (l'écart qui s'écarte) au lieu de l'illustrer — application directe de « preuve d'abord » ; (2) données **réelles et légalement propres** (portefeuilles Fama-French Developed, gratuit/citable, + FRED `DFII10`) ; (3) **label footer = construction exacte** (tri book-to-market, total return, rebase déc. 2021) ; (4) chiffres recoupés sur le CSV avant livraison (les 5 taux réels EOM vérifiés). Modèle de référence pour les majeurs à thèse « divergence/écart qui se creuse ».

## Input attendu
Article majeur intégral · slug + **pilier parent** (tag/watermark) · **CSV/XLSX** des séries (sinon réclamer) · forme du majeur précédent (anti-répétition).

## Articulation
- `brand-kit-eco3min` — source de vérité charte (palette, typo, codes régime). Ce skill spécialise pour le hero majeur.
- `sourcing-donnees-eco3min` — source de vérité provenance/licence/légalité des données tracées (gate 2.0 : propre, pas seulement réelle).
- `production-hero-pilier` — pendant pilier (logique inverse : territoire vs thèse, crème vs blanc, dense vs aéré).
- `visuels-eco3min` — AMF, sourcing, qualité, choix de chart. `editeur-eco3min` — ton, AMF du titre/sous-titre. `archi-eco3min` — slugs FR/EN, pilier parent.
- `prompt-hero-majeur-eco3min` v2.1 — dérivé Claude Design de ce skill (workflow recommandé par défaut).

## À actualiser après 2-3 majeurs si
- Une forme du menu domine au point de relancer la monotonie (risque symétrique : tout en dumbbell/divergence).
- La qualité oscille trop entre majeurs (prix de la liberté) → resserrer le menu aux 4-5 formes fiables.
- La convention « fond blanc = majeur » est adoptée → la graver dans `brand-kit-eco3min`.
- Un layout canonique majeur stable émerge (zones, hiérarchie de signaux) → le figer comme l'a fait le skill pilier.

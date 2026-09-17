# brand-kit-eco3min — référence : Anti-patterns (renvoi), articulation avec les autres skills, versioning, note d'usage (§8, §9, Versioning, Note)

Extrait VERBATIM de SKILL.md (découpage du 17/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée, le chrome canonique §0 et le moment où lire ce fichier.

## 8. Anti-patterns visuels (non négociables)

Renvoi au skill `visuels-eco3min` section 2 (7 interdictions AMF), section 3 (anti-patterns data viz : pas de 3D, pas de pie chart au-delà de 3 segments, pas de gradient décoratif), section 7 (qualité technique).

Ces règles sont gravées et indépendantes du brand kit — elles s'appliquent à tout visuel Eco3min.

---

## 9. Articulation avec les autres skills

| Skill | Relation au brand kit |
|---|---|
| `production-hero-pilier` | Implémentation stricte du brand kit pour la série des ~10 piliers. La règle « accent terracotta unique » du skill devient une règle générale du brand kit. |
| `production-hero-article-eco3min` | Spécialise le brand kit pour le troisième registre de hero (article, 1200×630, crème, cadre `#DED7C7`). Le brand kit reste la source de vérité charte. |
| `visuels-eco3min` | Conserve les règles AMF, sourcing, qualité technique, choix de chart. Le brand kit fournit le minimum commun (typo + palette + codes régime) qu'il imposait précédemment de façon variable. |
| `formats-eco3min` | Indépendant. Aucun chevauchement (HTML/structurel). |
| `production-chart-of-the-week` | La **typo** reste obligatoire (signature cross-canal). Le **fond** se choisit parmi les 3 registres §2.2 (crème / blanc / charcoal inversé) selon le registre éditorial du cycle. La **palette du chart** est libre par registre (règle de diversité propre au skill), avec la palette catégorielle §2.5 comme port d'attache par défaut ; seuls les éléments récurrents (watermark, sourcing) restent fixés. Résout la contradiction v1.0 (« fond crème obligatoire » vs sa propre règle de diversité de palette). |
| `production-research-study`, `production-dataset`, `production-q-and-a` | Indépendants pour le contenu textuel (suivent `editeur-eco3min`). Pour les visuels qu'ils contiennent, ils suivent le brand kit. |

---

## Versioning

- **v1.0** (mai 2026) — première formalisation après audit transversal des 3 skills design existants (`production-hero-pilier`, `visuels-eco3min`, `formats-eco3min`) et observation de la diversité visuelle déjà en place (US Inflation 113 Years, BBB-ification, Affordability Matrix, Spread WTI-Brent).
- **v1.1** (juillet 2026) — « diversité chromatique contrôlée », après audit anti-monotonie (constat : ~90 % des visuels en mode charcoal + 1 terracotta, heros piliers convergents ; cause racine : palette catégorielle verrouillée sur les régimes nommés). Changements : (1) palette catégorielle générale à 7 rangs (§2.5) dérivée des familles régime — aucune teinte nouvelle ; (2) 3 registres de fond officiels (§2.2), convention « blanc = hero majeur » gravée ; (3) doctrine « identité par la structure, variété par la couleur » (mécaniques OWID/FT : chrome uniforme + palettes catégorielles + direct labeling) ; (4) règle terracotta clarifiée (unicité = mode sobre uniquement) ; (5) mode sobre déclassé de défaut universel à mode adapté mono-série ; (6) contradiction fond/palette avec `production-chart-of-the-week` résolue. Le squelette identitaire (typo, sourcing, watermark, AMF, saturation sourde) est inchangé — c'est lui qui a gagné les citations FT Alphaville / Ritholtz, il ne bouge pas.
- **v1.2** (septembre 2026) — intégration du registre « hero d'article » (V3), qui tournait en production hors brand kit : format 1200×630 gravé au §4, token de filet crème `#DED7C7` ajouté au §2.1, fond crème étendu explicitement à ce registre au §2.2. Aucune règle existante modifiée.

À actualiser quand :
- Une nouvelle famille de visuel demande une convention non prévue
- Une mauvaise lisibilité émerge sur un code régime particulier
- Un brand kit étendu (illustration, motion, print) devient nécessaire

---

## Note d'usage interne

Ce skill définit le brand kit Eco3min (v2.0 depuis le 17/09/2026). Pour la voix éditoriale, voir `editeur-eco3min`. Pour les règles AMF data viz et qualité technique, voir `visuels-eco3min`. Pour les patterns spécifiques aux heros piliers, voir `production-hero-pilier`. Pour les charts viraux Reddit, voir `production-chart-of-the-week` — ce dernier est un design à part, optimisé pour Reddit et exempté du chrome canonique §0 (titre, signature `Eco3min` seule, bandeau et palette du chart libres par registre éditorial, selon sa propre ÉTAPE 3) ; il conserve la typographie et choisit son fond parmi les 3 registres §2.2.

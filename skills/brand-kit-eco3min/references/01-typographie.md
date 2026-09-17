# brand-kit-eco3min — référence : Typographie, 3 familles fixes, configurations canoniques, fallbacks, dualité web/export (§1)

Extrait VERBATIM de SKILL.md (découpage du 17/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée, le chrome canonique §0 et le moment où lire ce fichier.

## 1. Typographie — 3 familles fixes

### 1.1 Serif éditorial : Source Serif 4

**Usage** : titres, sous-titres italiques, titres descriptifs de métrique, citations.

**Pourquoi** : dessin moderne, large amplitude de poids (200 à 900), excellent rendu à toute taille, italic distinctif qui sert les sous-titres analytiques. Téléchargeable gratuitement sur Google Fonts.

**Configurations canoniques** :
- Titre principal hero : 38–48 px, weight 600
- Citation / pull-quote italique éditorial : 17–22 px, weight 400, italic (v2.0 : le sous-titre descriptif d'un chart ou d'un hero est en Inter, cf. SKILL.md §0)
- Titre descriptif métrique (en small multiples) : 14–16 px, weight 500
- Citations en blockquote : 18–22 px, weight 400, italic

**Fallback chain CSS** : `"Source Serif 4", "Source Serif Pro", Georgia, "Times New Roman", serif`

### 1.2 Sans-serif : Inter

**Usage** : annotations chiffrées dans le chart, labels d'axes, légendes, callouts de données, texte de UI sur les visuels riches (Affordability matrix, etc.).

**Pourquoi** : optimisé pour les écrans ET le print, lisibilité parfaite à petite taille (12 px), chiffres tabulaires disponibles (`font-variant-numeric: tabular-nums`).

**Configurations canoniques** :
- Annotations chiffrées (« $3.05 remaining », « 2019 peak: 51% ») : 11–13 px, weight 500
- Labels d'axes : 10–11 px, weight 400
- Légendes : 11–12 px, weight 400
- Callouts d'événement (« mars 2020 — COVID ») : 11 px, weight 500

**Chiffres tabulaires obligatoires** sur les axes (sinon les alignements verticaux dansent).

**Fallback chain CSS** : `Inter, "Helvetica Neue", Arial, -apple-system, BlinkMacSystemFont, sans-serif`

### 1.3 Monospace : IBM Plex Mono

**Usage** : codes de série (FRED `DFII10`, ICE `BAMLH0A0HYM2`), sources en pied de visuel, captions, labels catégoriels uppercase (`PROPRIÉTÉ 01 · COÛT DU CAPITAL`), tags piliers (`POLITIQUE MONÉTAIRE & TAUX — PILIER`, sans numérotation « / NN »).

**Pourquoi** : signature visuelle d'Eco3min — la ligne sources en mono uppercase est ton trait distinctif le plus reconnaissable. Plex Mono est plus chaud qu'un courrier monospace générique.

**Configurations canoniques** :
- Sources footer ligne 1 : 9–10 px, weight 400, letter-spacing 0.5
- Sources footer ligne 2 (méthodo) : 9 px, weight 400, letter-spacing 0.5
- Labels catégoriels uppercase : 10–11 px, weight 500, letter-spacing 1.2–2.5
- Tag pilier (sans numéro) : 10 px, weight 500, letter-spacing 1.5
- Codes série dans le chart : 9–10 px, weight 400

**Casse** : uppercase systématique pour labels catégoriels et tags. Sentence case ou mixte pour le contenu des sources.

**Fallback chain CSS** : `"IBM Plex Mono", "SF Mono", Menlo, Consolas, monospace`

### 1.4 Dualité web vs export — assumée

Le site web (CSS v3.4) utilise une autre triade : **Libre Baskerville + DM Sans + JetBrains Mono**. Cette dualité est volontaire et documentée :

- Le web a ses contraintes (chargement, hinting écran, accessibilité) — Libre Baskerville et DM Sans y sont plus performants.
- Les visuels exportés ont les leurs (compression PNG/WEBP, lisibilité au repartage) — Source Serif 4, Inter, Plex Mono y sont supérieurs.

Aucune règle ne demande d'unifier. Si une refonte typographique globale est décidée plus tard (par exemple lors d'une collaboration designer), on basculera des deux côtés en même temps. D'ici là, la dualité est un trait d'usage, pas une dette.

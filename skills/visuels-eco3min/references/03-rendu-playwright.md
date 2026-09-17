# visuels-eco3min — référence : Rendu PNG des visuels HTML/SVG, recette Playwright (§7 bis)

Extrait VERBATIM de SKILL.md (découpage du 17/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 7 bis. Rendu PNG — recette Playwright

Le rendu de référence des visuels codés (heros, charts HTML/SVG) passe
par **Chromium via Playwright** (ou par matplotlib avec polices enregistrées et assertées, §7 ter), jamais par une capture manuelle :
c'est le seul chemin qui garantit les trois familles typographiques réelles.

### Le piège des polices

Chromium rend la page **avant** que les Google Fonts soient chargées si on ne
l'attend pas explicitement. Le résultat est un PNG en police de repli —
**sans erreur, sans avertissement**, exactement comme la retombée silencieuse
de matplotlib sur DejaVu Sans. Un visuel entier peut partir en production dans la
mauvaise typo sans que rien ne le signale.

### Séquence obligatoire — aucune étape n'est facultative

1. `set_content(html, wait_until="load")`
2. `await page.evaluate("document.fonts.ready")`
3. `wait_for_timeout(650)` — 650 à 700 ms ; en dessous, le rendu part trop tôt
4. exécuter l'auto-ajustement de titre (voir plus bas)
5. `wait_for_timeout(150)`
6. `screenshot(..., clip={...})`

Sauter l'étape 2 **ou** l'étape 3 suffit à produire le repli silencieux.

### Réglages

- `viewport` aux dimensions cibles, `device_scale_factor=2` — on rend en
  rétine, puis on redescend aux dimensions exactes par PIL/LANCZOS.
- `screenshot` avec un `clip` **explicite**
  `{"x":0,"y":0,"width":W,"height":H}` : sans lui, une marge parasite ou un
  débordement d'un pixel change les dimensions du fichier.
- SVG : géométrie **pré-calculée en Python** puis embarquée en
  SVG inline dans le HTML. Un SVG chargé en ressource externe déclenche des
  blocages cross-origin. Full-canvas en `viewBox="0 0 W H"`,
  `position:absolute; inset:0`, le texte HTML par-dessus en `z-index`.

### Auto-ajustement du titre

Boucle JS qui décrémente la taille de police depuis ~44 px jusqu'à un
plancher de 24-26 px tant que le titre déborde de son budget de deux lignes.

**Doit tourner après confirmation du chargement des polices** — mesurer
avant, c'est mesurer la police de repli, donc calculer un mauvais palier.

L'exposer en `window.__fit()`, l'appeler par `page.evaluate()`, et attendre
`window.__fit_done` via `wait_for_function()` plutôt que par un timeout fixe.

### Vérification

Vérifier explicitement la police rendue sur le **premier visuel d'une
série** — même consigne que pour matplotlib. Un zoom sur un mot en
Source Serif 4 suffit : si le rendu est en sans-serif, toute la série est
à refaire.

### Repli

Si Chromium est indisponible, l'installer (`playwright install chromium`). En
dernier recours seulement, rendre un SVG pur via `cairosvg` — mais la
fidélité typographique y est moins bonne.

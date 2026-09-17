# visuels-eco3min — référence : Rendu matplotlib, les cinq assertions avant savefig et le garde ASCII (§7 ter)

Extrait VERBATIM de SKILL.md (découpage du 17/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 7 ter. Rendu matplotlib — quatre assertions avant `savefig`

Le §7 bis couvre le chemin Playwright, qui est celui des heros et des charts
HTML. Les charts codés en matplotlib — Chart of the Week, visuels de dataset,
séries longues — passent par un autre chemin, avec ses propres échecs
silencieux. Aucun d'eux ne lève d'exception : le PNG sort, il a l'air correct
sur une vignette, et le défaut ne se voit qu'agrandi ou pas du tout.

**Les quatre assertions se posent dans le script, pas dans la relecture.** Une
inspection visuelle rapide a laissé passer les trois premières au moins une fois
chacune, sur des scripts écrits par quelqu'un qui connaissait le piège.

### 1. La police demandée est bien la police rendue

Matplotlib retombe sur DejaVu Sans **sans erreur ni avertissement** quand la
famille n'est pas enregistrée. Voir la recette d'instanciation en mémoire de
projet ; le contrôle, lui, tient en trois lignes.

```python
from matplotlib.font_manager import FontProperties
for family in ('Source Serif 4', 'Inter', 'IBM Plex Mono'):
    got = FontProperties(family=family).get_name()
    assert got == family, 'repli de police : demandé %r, obtenu %r' % (family, got)
```

### 2. Aucun texte ne déborde du canvas

Un titre trop long est **rogné au bord du PNG**, pas mis à la ligne, pas réduit.
Sur un rendu 1920×1080 examiné en vignette, un titre amputé de ses trois
derniers mots passe inaperçu.

```python
fig.canvas.draw()
r = fig.canvas.get_renderer()
W, H = fig.get_size_inches() * fig.dpi
for t in list(fig.texts) + list(ax.texts):
    bb = t.get_window_extent(renderer=r)
    assert -1 <= bb.x0 and bb.x1 <= W + 1, 'débordement horizontal : %r' % t.get_text()[:48]
    assert -1 <= bb.y0 and bb.y1 <= H + 1, 'débordement vertical : %r' % t.get_text()[:48]
```

### 3. Les textes d'en-tête ne se recouvrent pas

Titre, sous-titre, badge d'unité et bandeau de killer phrase sont posés en
coordonnées figure. Il suffit qu'un titre s'allonge d'un mot pour que le badge
en haut à droite lui passe dessus. Le recouvrement est parfaitement lisible en
plein écran et invisible sur une vignette.

La tolérance n'est pas cosmétique : les boîtes englobantes de texte incluent
toute la hauteur de ligne, donc deux lignes empilées serré se touchent sans se
gêner. Seule une vraie morsure compte.

```python
from matplotlib.transforms import Bbox
boxes = [(t.get_text()[:40], t.get_window_extent(renderer=r)) for t in fig.texts]
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        (na, a), (nb, b) = boxes[i], boxes[j]
        inter = Bbox.intersection(a, b)
        if inter is None:
            continue
        share = (inter.width * inter.height) / min(a.width * a.height, b.width * b.height)
        assert share < 0.12, 'chevauchement %.0f%% : %r / %r' % (share * 100, na, nb)
```

### 4. Les `$` sont échappés

**Deux `$` non échappés dans une même chaîne basculent tout le texte intermédiaire
en mathtext**, rendu en italique mathématique, espacement cassé, sans le moindre
avertissement. C'est le piège le plus vicieux de la liste parce qu'il ne frappe
que les visuels en dollars, et qu'une killer phrase du type
`"Refunds averaged $0.4bn a month. In June the Treasury paid back $49.2bn."`
part entièrement en italique : le lecteur voit une phrase bizarre, pas une erreur.

Dans une chaîne Python, écrire `\\$`. Et asserter :

```python
assert '$' not in TEXTE.replace('\\$', ''), 'dollar non échappé : %r' % TEXTE
```

Le même piège existe sur les libellés d'axe construits à la volée : un
`'$%d bn' % v` isolé passe, deux `$` dans le même libellé basculent.

### 5. Le pied de source ne mord pas le watermark (ajouté le 16/09/2026)

La troisième assertion tolère 12 % de recouvrement de la plus petite boîte,
et c'est le bon seuil pour deux lignes empilées. Mais sur une ligne de sources
longue, une morsure de fin de ligne sur le watermark reste sous 12 % de la boîte
du watermark et passe. Vu sur R6, chart ladder FR : « …rendement total du
marché US)Eco3min Research ». Asserter l'ordre horizontal, pas seulement le
recouvrement.

```python
foot = [t for t in fig.texts if t.get_text().startswith('Sources')]
wm = [t for t in fig.texts if t.get_text().startswith('Eco3min Research')]
if foot and wm:
    assert foot[0].get_window_extent(renderer=r).x1 < wm[0].get_window_extent(renderer=r).x0 - 8,         'the source line runs into the watermark'
```

Même famille que le garde étendu aux graduations et libellés d'axe (R2, R4) :
chaque niveau de texte oublié par le balayage se rejoue.

### Bonus, même famille : les glyphes hors ASCII

IBM Plex Mono n'a **ni U+2009 ni U+202F**. Une espace fine insécable dans un
« 2 499 » à la française est rendue par une police de substitution, en silence.
Le contrôle le moins coûteux est de rester en ASCII dans tout texte de visuel et
de l'asserter ; sinon, vérifier le cmap de la police demandée pour chaque
caractère non ASCII.

```python
for t in list(fig.texts) + list(ax.texts):
    assert t.get_text().isascii(), 'glyphe hors ASCII, vérifier le cmap : %r' % t.get_text()
```

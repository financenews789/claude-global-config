# production-research-study — référence : Sélection du type de chart, discipline de génération, chart interactif (§10)

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 10. Sélection du type de chart

**Règle directrice** : la donnée dicte le visuel, pas un template figé.

Choix possibles :
- Line chart + zones grisées de régimes (séries temporelles avec décomposition)
- Scatter plot (corrélations bivariées)
- Heatmap (matrices de relations)
- Small multiples (comparaisons inter-épisodes)
- Ridge plot (distributions par régime)
- Waterfall (décomposition d'une variation)
- Stacked area (composition évolutive)
- Density / quantile bands (distributions historiques)
- Gantt / timeline (séquencement d'événements)

### 10.1 Justification obligatoire

Pour chaque chart de l'étude, documenter :

```
SCALE JUSTIFICATION:
Data range: [min] to [max], ratio = [X]×
→ Primary: [log/linear] because [reason]
→ Supplementary: [yes/no]
```

### 10.2 Politique d'échelle

| Ratio max/min | Échelle primaire | Vue supplémentaire |
|---|---|---|
| > 5× | Log (default obligatoire) | Linear comme "Supplementary View" |
| 2×–5× | Choix justifié | Autre échelle si utile |
| < 2× | Linear | Pas nécessaire |

### 10.3 Le chart "r/dataisbeautiful"

Une étude doit avoir un chart conçu pour fonctionner **standalone** sur les réseaux sociaux :
- Compréhensible sans l'article
- Visuellement mémorable (layout non conventionnel encouragé)
- "Aha moment" en 3 secondes
- Version standalone qui raconte l'histoire complète sans texte d'accompagnement

C'est typiquement le **Chart B** (le scatter ou le ridge plot, pas le hero line chart).

### 10.4 Les autres règles data viz

Les standards Eco3min (sourcing intégré dans le chart, AMF visuel, anti-patterns 3D / pie / double Y, accentuation des majuscules, etc.) restent ceux du skill `visuels-eco3min`. Ce skill ajoute uniquement la dimension narrative ci-dessus.

---

### 10.5 Discipline de génération

Le script de chart **lit le CSV** (`parse_dates` là où c'est pertinent), imprime **chaque valeur annotée**, et se termine par un **bloc d'assertions** vérifiant chaque annotation contre le CSV.

Puis : **inspecter visuellement chaque chart** avec l'outil de vue, et corriger chevauchements et troncatures avant livraison, avec contrôle de lisibilité à 380 px.

Exports : page ~1400×750 · OG 1200×630 · social autonome 1920×1080 pour le chart destiné à r/dataisbeautiful quand il est poussé.

---

### 10.6 Le chart interactif — livrable obligatoire

Les charts statiques restent la preuve citable et l'image OG. Le chart interactif
est ce qu'un lecteur de Hacker News manipule avant de décider s'il upvote, et ce
qu'une IA ne peut pas résumer à la place du lecteur. Il **s'ajoute**, il ne
remplace rien.

**Contrat technique.** SVG construit en JavaScript natif, **aucune bibliothèque
externe** — pas de CDN, pas de dépendance qui pourrira, aucun tiers qui voit le
lecteur. Le markup est un conteneur à attributs `data-*` dans le corps HTML ; tout
le JS vit dans le snippet, parce que le corps ne contient ni `<style>` ni
`<script>` (§20.2). La donnée vient du **CSV publié de l'étude**, servi en
same-origin depuis `uploads/[YYYY]/[MM]/`.

**Contrat d'audit.** Toute valeur affichée par le module vient d'une colonne du
CSV. Le module ne calcule rien qui ne soit pas déclaré ; une transformation
déclarée est assertée dans `compute_stats.py` comme n'importe quelle autre
statistique (§18.2). Les valeurs affichées par défaut — typiquement la dernière
observation — entrent dans le périmètre imprimé du Step 4.

**Contrat AMF.** Descriptif uniquement. Pas de flèche directionnelle, pas de zone
« acheter / vendre », pas de projection, pas de seuil présenté comme un signal
d'action. Les bandes grisées ne portent que des **épisodes datables et sourcés**,
jamais des zones interprétatives. Les règles de `visuels-eco3min` s'appliquent au
survol et aux étiquettes comme aux charts statiques.

**Dégradation, non négociable.** Si le fetch échoue, si le CSV est malformé, ou si
JS est absent, le `<picture>` de repli contenu dans le conteneur reste affiché et
la page reste complète et citable. Le module ne retire le repli qu'**après** un
rendu réussi. Tester le repli réseau coupé — le supposer ne suffit pas.

**Vérifications avant livraison** : le CSV est en ligne à l'URL exacte et au bon
mois · chaque colonne déclarée existe dans l'en-tête au caractère près · trois
valeurs échantillonnées au survol correspondent au CSV · le repli s'affiche réseau
coupé · Tab atteint le graphe et les flèches déplacent le curseur · lisible à
380 px.

Le code de référence, les attributs et le CSS vivent dans le `snippet_model.php`
du projet de série, section « INTERACTIVE CHART ».

---

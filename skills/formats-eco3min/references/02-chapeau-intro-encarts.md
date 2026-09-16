# formats-eco3min — référence : Chapeau, intro éditoriale, encarts et leurs templates (§2, §3, §4)

Extrait VERBATIM de SKILL.md (découpage du 16/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 2. Chapeau éditorial

Standard presse économique (FT, Les Échos). Court paragraphe de cadrage immédiatement après le H1.

**Quand l'utiliser**
- Articles de fond (majeur, satellite long)
- Études de cas
- Articles dont l'angle ne ressort pas évidemment du H1

**Quand s'en passer**
- Notes courtes, brèves
- FAQ et Q&A pages (inutile, redondant avec la question)
- Articles où l'introduction joue déjà ce rôle

**Spécifications**
- 1 à 2 phrases, 30 à 45 mots
- Phrase 1 = mécanisme économique ; phrase 2 = conséquence
- Ton analytique et factuel, pas d'emphase
- Ne reprend pas mot pour mot l'introduction
- Pas de `<strong>`, pas de `<em>`

**Template HTML**

```html
<p class="eco3min-chapeau">
[1 à 2 phrases — mécanisme + conséquence — 30-45 mots max]
</p>
```

**Exemple**

```html
<p class="eco3min-chapeau">
Comparer achat et location uniquement via mensualité et loyer masque
des variables décisives comme le coût d'opportunité du capital ou la
mobilité résidentielle.
</p>
```

---

## 3. Intro éditoriale

Paragraphe de transition entre le chapeau et l'introduction proprement dite. Donne le contexte de l'angle.

**Quand l'utiliser** : couplé à un chapeau, sur articles de fond.
**Quand s'en passer** : sans chapeau, ou si l'introduction enchaîne déjà naturellement.

**Spécifications**
- 1 paragraphe, 20 à 40 mots
- Ne répète pas le chapeau
- Pose l'angle, ne conclut pas

**Template HTML**

```html
<p class="eco3min-intro">
[1 paragraphe — contexte ou angle — 20-40 mots max]
</p>
```

**Ordre dans la page** : H1 → chapeau → intro éditoriale → image éventuelle → introduction.

---

## 4. Encarts (callouts)

Quatre encarts existent dans le système visuel Eco3min. **Aucun de ces quatre n'est obligatoire en soi** — ils sont mobilisés selon ce que l'article a besoin de mettre en valeur.

**Doctrine de sobriété (style FT).** La prose porte l'analyse ; les blocs étiquetés la servent.
- Sur un **MAJEUR / une étude** : signature citable = **TL;DR de tête (§5.1) + 🧭 Lecture eco3min (§4.1)**. Le reste (Erreur fréquente, À retenir, Cadre, FAQ, extraits) est optionnel.
- Sur un **satellite** : signature = **TL;DR de tête + exactement 1 encart** (À retenir OU Erreur fréquente). 🧭 Lecture eco3min et 🧠 Cadre d'analyse sont **réservés aux MAJEURs / études**.

**Plafond ~3 blocs étiquetés par article** (les 2 signatures + au plus un autre). **Jamais empiler trois récaps en puces** (TL;DR + À retenir + extraits partageables) : au plus un récap en puces en plus du TL;DR. Si retirer un bloc ne fait rien perdre au lecteur, ne pas le mettre.

**Phrase-pivot** (voir `editeur-eco3min` §5, obligatoire par article) : elle vit d'abord dans la prose ; elle peut être reprise UNE fois dans la 🧭 Lecture eco3min ou la conclusion — jamais dans les deux, jamais trois occurrences au total.

### 4.1 Encart "Lecture eco3min"

**Rôle** : phrase analytique citable, en rupture avec une lecture dominante. Conçue pour être extractible par les moteurs génératifs (SearchGPT, AI Overviews) avec attribution claire au site.

**Quand l'utiliser**
- Articles de fond où une thèse analytique distincte est posée
- Études et research pages

**Quand s'en passer**
- Articles purement explicatifs sans thèse propre
- **Satellites** (encart réservé aux MAJEURs / études)
- Brèves
- FAQ/Q&A

**Spécifications**
- 1 seule phrase, ≤25 mots
- Ton affirmatif (pas de "peut", "tend à", "souvent")
- Vocabulaire macro stable, non normatif
- Doit exprimer un désaccord ou une rupture analytique avec une lecture courante
- Position : fin du raisonnement analytique, avant toute clôture éditoriale

## Encarts — la double classe est obligatoire

⚠️ **Règle bloquante.** Tout encart porte **deux** classes sur le même `div` :
`eco3min-callout` **plus** sa variante. Et le titre est dans un
`div.eco3min-callout-title` **à l'intérieur**.

```html
<div class="eco3min-callout eco3min-lecture">
  <div class="eco3min-callout-title">…</div>
  …
</div>
```

**Une variante seule est INVALIDE** — `<div class="eco3min-lecture">` sans
`eco3min-callout` ne reçoit aucun style : l'encart se rend en paragraphe nu, sans
erreur ni signal. C'était l'erreur d'une ancienne version des guidelines
éditoriales, propagée sur les articles produits pendant qu'elle faisait foi.

Les quatre variantes :

| Variante | Encart |
|---|---|
| `eco3min-lecture` | 🧭 Lecture eco3min |
| `eco3min-warning` | Erreur fréquente |
| `eco3min-keypoints` | À retenir |
| `eco3min-method` | Cadre d'analyse |

Le TL;DR de tête n'est **pas** un encart : il a son propre balisage
`eco3-tldr` et ne prend jamais `eco3min-callout`.

Contrôle avant livraison :

```python
import re
mauvais = re.findall(r'<div class="eco3min-(?:lecture|warning|keypoints|method)"', html)
assert not mauvais, "encart sans la classe eco3min-callout : %s" % mauvais
```

---

**Template HTML**

```html
<div class="eco3min-callout eco3min-lecture">
  <div class="eco3min-callout-title">🧭 Lecture eco3min</div>
  <p>
    [Phrase unique — ≤25 mots — analytique — en rupture avec lecture dominante]
  </p>
</div>
```

### 4.2 Encart "Erreur fréquente"

**Rôle** : signaler une erreur de lecture courante et la corriger.

**Quand l'utiliser** : sujets où une lecture biaisée existe (indicateurs trompeurs, raccourcis statistiques, confusions conceptuelles).
**Quand s'en passer** : sujets sans erreur de lecture identifiable, ou si le corps de l'article traite déjà la correction de manière fluide.

**Structure type (3 phrases)**
1. Description de l'erreur
2. Pourquoi elle est trompeuse
3. La lecture correcte

**Template HTML**

```html
<div class="eco3min-callout eco3min-warning">
  <div class="eco3min-callout-title">Erreur fréquente</div>
  <p>
    [Description — pourquoi trompeuse — correction de lecture]
  </p>
</div>
```

### 4.3 Encart "À retenir"

**Rôle** : synthèse en fin d'article.

**Quand l'utiliser** : articles longs (>800 mots) qui méritent une cristallisation finale, **à condition d'apporter des points que le TL;DR de tête ne contient pas déjà**.
**Quand s'en passer** : articles courts ; articles dont la conclusion analytique remplit déjà ce rôle ; **si le TL;DR de tête couvre déjà ces points** ; cas où une synthèse en prose fonctionne mieux qu'une liste à puces.

**Spécifications**
- 2 à 4 points
- Formulés analytiquement, jamais prescriptifs
- Pas de conseil, pas de prédiction

**Template HTML**

```html
<div class="eco3min-callout eco3min-keypoints">
  <div class="eco3min-callout-title">À retenir</div>
  <ul>
    <li>[Point 1 — analytique, factuel]</li>
    <li>[Point 2 — analytique, factuel]</li>
    <li>[Point 3 — analytique, factuel]</li>
  </ul>
</div>
```

### 4.4 Encart "Cadre d'analyse" (rare)

**Rôle** : poser un cadre méthodologique explicite quand l'article s'appuie sur une grille de lecture peu commune.

**Quand l'utiliser** : research pages, études chiffrées avec méthodologie distinctive.
**Quand s'en passer** : par défaut. C'est l'encart le moins fréquent — un seul si présent.

**Template HTML**

```html
<div class="eco3min-callout eco3min-method">
  <div class="eco3min-callout-title">Cadre d'analyse</div>
  <p>[Explication du cadre méthodologique]</p>
</div>
```

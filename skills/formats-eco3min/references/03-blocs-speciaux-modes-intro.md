# formats-eco3min — référence : TL;DR de tête, FAQ SEO, extraits, angle, intention, modes d'introduction (§5, §6)

Extrait VERBATIM de SKILL.md (découpage du 16/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 5. Blocs spéciaux (textuels)

Le **TL;DR de tête (§5.1) est obligatoire sur les articles** ; les autres patterns ci-dessous sont disponibles, à mobiliser si l'article s'y prête, jamais en routine (cf. doctrine de sobriété §4).

### 5.1 TL;DR de tête — OBLIGATOIRE (articles, pas pages ni Q&A)

Bloc `.eco3-tldr` placé juste après le chapeau + l'intro éditoriale, AVANT l'introduction : version structurée et extractible (AI Overviews, moteurs génératifs) de l'essentiel. **Obligatoire sur tout article** (MAJEUR, satellite, étude, "Every X", chart). **Exclus** : pages piliers/sous-piliers (voir `pilier-kit`) et Q&A (déjà un TL;DR propre). Les articles longs du site sont toujours concernés ; seule dérogation : de rares notes < ~450 mots.

C'est un **bloc de tête, pas un encart** — il ne compte pas dans le "1 encart" des satellites, et forme avec la 🧭 Lecture eco3min (MAJEUR) la paire signature citable.

**Forme**
- `lead` : 1 phrase auto-portante (citable telle quelle, sans "cet article…"), teaser qui donne l'angle. **≤ 35 mots FR / ≤ 30 mots EN.**
- 2 à 4 puces (3 par défaut) : un fait + un concret (chiffre + source/date, seuil, ou mécanisme nommé), tiré du corps de l'article.
- **Anti-uniformité** : varier l'ouverture (proscrire en boucle "le consensus regarde X / le vrai signal est Y", "ce qui change sans bruit", "pas X mais Y", "X n'est plus seulement Y") ; varier la longueur (2/3/4 puces) ; toujours spécifique.
- AMF comme le reste (voir `editeur-eco3min` §4).

**Template HTML** (le CSS `.eco3-tldr` est global — pas de style inline)

```html
<div class="eco3-tldr">
  <div class="eco3-tldr__label">TL;DR</div>
  <p class="eco3-tldr__lead">[lead — teaser auto-portant, ≤ 35/30 mots]</p>
  <ul class="eco3-tldr__list">
    <li>[puce 1 — fait + concret]</li>
    <li>[puce 2 — fait + concret]</li>
    <li>[puce 3 — fait + concret]</li>
  </ul>
</div>
```

(Pose / rétro-équipement sur l'existant : plugin `eco3min-tldr`.)

### 5.2 FAQ SEO

3 à 5 questions reproduisant de **vraies requêtes longue traîne** (Google PAA), pas une FAQ marketing.

- Questions très spécifiques au sujet
- Réponses courtes (2–4 phrases), factuelles, nuancées
- À éviter si le corps de l'article répond déjà à ces questions de manière fluide
- **Anti-cannibalisation du hub Q&R** : n'ajouter une FAQ inline que si ses questions ne sont **pas** déjà traitées par une page du hub Q&R, et sans second JSON-LD QAPage en conflit (le balisage reste géré côté hub)

### 5.3 Extraits partageables

3 punchlines extractibles, ≤240 caractères chacune. Intitulés possibles : "Points clés", "En 3 phrases", "3 idées à retenir". À utiliser sur articles à forte densité analytique. Inutile si l'article est déjà très court. **Jamais cumulés avec le TL;DR de tête ET l'encart "À retenir"** (ce serait un 3ᵉ récap en puces — cf. §4). En pratique, le TL;DR porte déjà cette fonction.

### 5.4 Paragraphe d'angle éditorial

Court mini-bloc en milieu d'article qui resitue pourquoi le sujet compte maintenant. Sert à éviter la lecture purement intemporelle. Reformulation libre — éviter les structures recyclées.

### 5.5 Intention humaine sous-jacente

Un paragraphe qui reformule en langage non technique ce que cherche réellement le lecteur. Utile sur sujets à forte charge émotionnelle (récession, immobilier, retraite). Inutile sur sujets purement techniques.

> **Un seul dispositif d'angle par article.** §5.4 (angle éditorial), §5.5 (intention humaine) et le « signal faible » de mise en contexte (cf. `editeur-eco3min` §3) jouent le même rôle : ouvrir un angle / recontextualiser. **N'en mobiliser qu'un seul** — empilés, ils rendent l'article méta-bavard et formulaïque.

---

## 6. Modes structurels d'introduction (articles satellites)

Trois modes possibles. **Choisir un seul**, ne pas les combiner.

| Mode | Ouverture | À éviter en première phrase |
|---|---|---|
| **A — Fait précis** | Chiffre daté observable | Théorie, objection |
| **B — Objection** | Croyance répandue à déconstruire | Chiffre brut |
| **C — Mécanisme discret** | Mécanisme micro/institutionnel concret | Chiffre, objection |

Le choix du mode dépend de l'angle : un article sur un seuil franchi appelle le mode A, un article qui corrige une lecture dominante appelle le mode B, un article sur une transmission peu visible appelle le mode C.

Pour les articles majeurs, l'introduction est plus posée et le point d'accroche conjoncturel peut être intégré au raisonnement plutôt que mis en avant.

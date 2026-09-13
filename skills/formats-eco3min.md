---
name: formats-eco3min
description: Catalogue des formats HTML d'Eco3min — chapeau et intro éditoriale, encarts (Lecture eco3min, Erreur fréquente, À retenir, Cadre d'analyse), blocs spéciaux (TL;DR, FAQ SEO, extraits partageables), modes structurels d'introduction, règles de méta-titre, variation des ancres internes, sources autorisées, outils Eco3min. À activer pour toute rédaction structurée d'article, FAQ ou Q&A destinée au site. Ce skill fournit des templates et des critères de sélection sans imposer leur usage — c'est l'angle de l'article qui décide quels patterns mobiliser.
---

# Catalogue des formats Eco3min

> **Philosophie de ce skill.** C'est une **boîte à outils**, pas une checklist. Aucun pattern n'est obligatoire en soi — c'est l'angle, la longueur et la nature de l'article qui décident. Un article court analytique peut très bien n'avoir aucun encart. Un article majeur en a généralement 2 ou 3. Si un pattern n'apporte rien à un article donné, il ne doit pas être inséré pour cocher une case.
>
> Pour l'identité éditoriale et la conformité AMF, voir le skill `editeur-eco3min` (les deux skills se complètent).

---

## 1. Hiérarchie article majeur / satellite

Sert à décider de la profondeur et de l'angle, pas à ajouter une contrainte.

| | Article majeur | Article satellite |
|---|---|---|
| **Rôle** | Pose le cadre conceptuel d'un cluster | Creuse un point précis |
| **Ton** | Posé, analytique, pédagogique | Plus angulaire, ciblé |
| **Cible** | "OK, j'ai compris le mécanisme global" | "Oui, mais concrètement dans ce cas ?" |
| **Longueur indicative** | Fourchette du blueprint (défaut 2 500–4 000 ; ancien plafond 3 000 supprimé, juill. 2026) | Fourchette du blueprint (défaut 1 500–2 500) |
| **Blocs étiquetés** | TL;DR + 🧭 Lecture (signatures) + ≤1 autre | TL;DR + 1 encart + synthèse finale |

**Règle anti-cannibalisation** : le majeur ne descend pas dans les détails (réservés aux satellites) ; les satellites ne redéfinissent pas le cadre général (réservé au majeur).

### 1.1 La même hiérarchie s'applique aux pages autoportantes

Le vocabulaire dit « article majeur » et « article satellite » parce qu'il vient
des clusters. Les **pages autoportantes** — celles que produit le pipeline page
bilingue — relèvent des mêmes deux registres :

| Registre | Types de page |
|---|---|
| **MAJEUR** | registre « Every X since Y », étude de recherche, page record, page dataset, time-machine |
| **SATELLITE** | Q&A, page outil / simulateur / calculateur |

Le registre se choisit sur la **nature de la page, pas sur sa longueur**. Une Q&A
dense reste un registre satellite ; un registre « Every X » bref reste un
registre MAJEUR. Les quotas d'encarts du §4 suivent le registre.

### 1.2 Ce qui tombe faute d'objet sur une page autoportante

Ces règles ne sont pas contredites : elles n'ont simplement plus de support.

- **La rotation des modes A/B/C** entre satellites consécutifs (§6) — il n'y a
  pas de série. Les trois modes restent une grille utile pour choisir la
  charpente d'une page isolée ; seule la **contrainte de rotation** disparaît.
- **La variation du type d'encart** par rapport au satellite précédent. Même
  raison.
- **L'unicité des ancres à l'échelle du cluster** (§8) — remplacée par l'unicité
  **dans la page**, plus une vérification dans `maillage.csv` qu'une ancre proche
  ne pointe pas déjà vers la même cible depuis ailleurs sur le site.
- **L'anti-cannibalisation intra-cluster** — remplacée par une
  anti-cannibalisation **site-wide** : l'intention de la page ne doit pas être
  déjà servie par une page vivante du snapshot.
- **Les fourchettes de longueur** (2 500-4 000 et 1 500-2 500 du tableau
  ci-dessus). Elles équilibrent un MAJEUR et ses satellites **à l'intérieur d'un
  cluster** ; une page autoportante n'a pas cet équilibre à tenir. Reprendre ces
  chiffres importerait une contrainte sans objet et ferait écrire pour atteindre
  un nombre.

  **À la place, la longueur s'arbitre page par page et se justifie**, sur quatre
  déterminants dans cet ordre : ce que l'intention exige (une requête qui demande
  un chiffre et sa définition se sert en 400 mots) · la densité de la donnée
  disponible (un registre de 300 lignes porte un corps qu'un registre de 12
  lignes ne porte pas) · le format (une page outil dont le simulateur fait le
  travail n'a pas besoin d'un long texte) · le voisinage (la longueur des pages
  qui servent des intentions comparables, dans le snapshot).

  La longueur est une **conséquence** du contenu, jamais une cible. Ni
  remplissage, ni troncature. Si une skill `production-*` fixe une fourchette
  pour ce type de page, elle prévaut.

  ⚠️ **L'asymétrie EN/FR n'est pas un défaut à corriger** : l'anglais sort
  naturellement 7 à 10 % plus court à contenu équivalent. Ne pas rembourrer l'EN
  pour l'aligner sur le FR.

  ⚠️ Le comptage par `re.sub(r"<[^>]+>", " ", html).split()` **surcompte de 5 à
  8 %** — les nombres français éclatent, les guillemets isolent des tokens.
  L'annoncer comme un comptage regex, jamais comme un nombre de mots réel.


---

## 1 bis. Structure éditoriale d'un article de cluster

Un article de cluster — majeur comme satellite — contient ces cinq éléments,
**sans ordre imposé** :

1. un **fait déclencheur** récent ;
2. une **analyse des mécanismes** ;
3. une **mise en perspective** macro ou historique ;
4. au moins un **scénario alternatif ou risque** ;
5. des **implications concrètes**.

⚠️ « Implications concrètes » = impacts économiques **observables** (ménages,
entreprises, marchés). Jamais des actions à entreprendre : c'est une frontière
AMF, pas une nuance de style.

### La flexibilité est la règle, pas l'exception

Le nombre de sections, leur intitulé et leur ordre sont **libres**. Une section
peut être absente si elle n'apporte rien. Réorganiser l'ordre environ une fois
sur quatre.

Si la borne haute de longueur est atteinte, prioriser dans cet ordre : analyse
centrale, implications concrètes, scénarios. Le reste devient facultatif.

### Variation structurelle — obligatoire

Le risque n'est pas qu'un article soit mal structuré, c'est que **tous les
articles aient la même structure**. Sur un cluster entier, cela se voit.

- Certains articles concluent **sans liste**, par une synthèse rédigée en un ou
  deux paragraphes.
- Certains ne contiennent **aucune liste**.
- D'autres placent leur unique liste dans le **dernier tiers**.
- Alterner les paragraphes courts et un paragraphe long.

Test : si un autre article du site pouvait être reconnu comme « issu du même
modèle » par sa seule structure, réécrire.

---

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
<!-- wp:html -->
<div class="eco3min-callout eco3min-lecture">
  <div class="eco3min-callout-title">🧭 Lecture eco3min</div>
  <p>
    [Phrase unique — ≤25 mots — analytique — en rupture avec lecture dominante]
  </p>
</div>
<!-- /wp:html -->
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
<!-- wp:html -->
<div class="eco3min-callout eco3min-warning">
  <div class="eco3min-callout-title">Erreur fréquente</div>
  <p>
    [Description — pourquoi trompeuse — correction de lecture]
  </p>
</div>
<!-- /wp:html -->
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
<!-- wp:html -->
<div class="eco3min-callout eco3min-keypoints">
  <div class="eco3min-callout-title">À retenir</div>
  <ul>
    <li>[Point 1 — analytique, factuel]</li>
    <li>[Point 2 — analytique, factuel]</li>
    <li>[Point 3 — analytique, factuel]</li>
  </ul>
</div>
<!-- /wp:html -->
```

### 4.4 Encart "Cadre d'analyse" (rare)

**Rôle** : poser un cadre méthodologique explicite quand l'article s'appuie sur une grille de lecture peu commune.

**Quand l'utiliser** : research pages, études chiffrées avec méthodologie distinctive.
**Quand s'en passer** : par défaut. C'est l'encart le moins fréquent — un seul si présent.

**Template HTML**

```html
<!-- wp:html -->
<div class="eco3min-callout eco3min-method">
  <div class="eco3min-callout-title">Cadre d'analyse</div>
  <p>[Explication du cadre méthodologique]</p>
</div>
<!-- /wp:html -->
```

---

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

---

## 7. Méta-titre — règles

**Interdit** : année explicite (2025, 2026), date calendaire, "actuellement", "aujourd'hui", "cette année". Le titre doit rester pertinent dans 6–12 mois.

**Actualité implicite** : un mécanisme qui évolue, un seuil franchi, une inflexion, un déséquilibre — sans dater.

**Test** : si le titre est amélioré en supprimant la date, la version sans date est obligatoire.

**Évite** : titres vagues ("tendances", "panorama", "le marché de…").

---

## 8. Variation des ancres internes

Trois règles cumulatives.

**Inter-articles** : pour un même lien cible, des articles différents utilisent des ancres différentes.

**Intra-article** : aucune ancre n'est répétée dans un même article. 5 liens = 5 ancres distinctes.

**Qualité** :
- 3 à 8 mots
- Descriptive du contenu de la cible
- Intégrée naturellement dans une phrase
- Jamais "cliquez ici", "voir ici", "lire aussi", "en savoir plus"

**Exemple** — pour des liens vers `/cycle-economique/`

| Article | Ancre |
|---|---|
| Majeur | les dynamiques du cycle économique |
| Satellite 1 | comprendre les phases conjoncturelles |
| Satellite 2 | l'alternance expansion-récession |
| Satellite 3 | le fonctionnement des cycles |

---

## 9. Sources autorisées (référence rapide)

Citer **institution + date** dans le flux du texte. Pas de section "Sources" en fin d'article, pas d'URL externes, pas de notes de bas de page.

**Banques centrales** : Fed (Réserve fédérale), BCE, BoE, BoJ, BNS.

**Institutions internationales** : FMI, OCDE, BRI (Banque des règlements internationaux), Banque mondiale.

**Statistiques nationales** : INSEE (France), BLS / Bureau of Labor Statistics (USA), Eurostat, ONS (UK), Destatis (Allemagne).

**Enquêtes bancaires clés** : *Bank Lending Survey* (BCE), *Senior Loan Officer Opinion Survey* / SLOOS (Fed).

**Autres** : Trésors et ministères des Finances, autorités de régulation (AMF, SEC, FCA), agences de notation (Moody's, S&P, Fitch — pour ratings uniquement).

**Données estimées** : préfixer avec `≈` et expliciter brièvement la méthode.

**Exemples conformes**
- "Selon le *Bank Lending Survey* de la BCE (T4 2025), 42 % des banques de la zone euro…"
- "D'après les séries longues de la BRI, le ratio crédit/PIB est passé de ≈165 % au T1 2010 à ≈180 % fin 2021."
- "Le *Senior Loan Officer Opinion Survey* de la Fed (janvier 2026) indique…"

---

## 10. Outils Eco3min — linking interne (optionnel)

Trois outils analytiques **du pôle macro** sont listés ci-dessous. **Maximum 1 lien outil par article. Aucun lien outil = choix valide.** Insérer un lien uniquement si l'outil éclaire un point précis du raisonnement. Les outils éligibles dépendent du pilier : d'autres piliers ont (ou auront) leurs propres outils — la pipeline B reçoit la liste éligible en paramètre.

| Outil | URL | Quand l'utiliser |
|---|---|---|
| **Lecture du cycle de taux** | `/outils-analyse-macroeconomique/lecture-cycle-taux/` | Articles sur politique monétaire, taux, crédit, immobilier via financement, marchés dépendants du régime de taux — surtout si le texte évoque variation, plateau, durée de maintien, délais |
| **Diagnostic du cycle macro** | `/outils-analyse-macroeconomique/diagnostic-du-cycle-macro-cadre-danalyse-eco3min/` | Articles macro ou pont, lectures de régime, études de cas transversales — surtout si le texte évoque ambiguïté de régime, signaux contradictoires, transition lente, stabilité fragile |
| **Indicateur économique trompeur** | `/outils-analyse-macroeconomique/indicateur-economique-trompeur/` | Articles évoquant indicateurs rassurants, résilience apparente, marchés calmes, chômage bas, inflation stable, bénéfices solides — quand un risque de lecture biaisée existe |

**Règles**
- Ancre neutre et descriptive ; jamais "voir notre outil", "outil eco3min"
- Lien intégré dans un paragraphe analytique, jamais en intro ou conclusion
- Si retirer le lien ne change rien à la compréhension de l'article → ne pas l'insérer

---

## 11. Bulletin macro hebdomadaire — linking interne (optionnel)

URL : `/barometre-macroeconomique-feuille-de-route/`

À mentionner ponctuellement, jamais systématiquement. Ancre naturelle ("le point macro hebdomadaire", "le baromètre macro", etc.), pas d'ancre SEO.

---

## 12. Format HTML général

Compatible WordPress Gutenberg.

**Balises autorisées** : `<h2>`, `<h3>`, `<p>`, `<strong>`, `<em>`, `<ul>`, `<li>`, `<a href="">`.

**Encarts** : envelopper dans `<!-- wp:html -->` et `<!-- /wp:html -->` pour Gutenberg.

**Interdit** : Markdown, `<html>`, classes CSS custom (sauf préfixe `eco3min-` et le bloc `.eco3-tldr`), styles inline.

**Méta-description** : portée par le champ `rank_math_description` du JSON de sortie (≤155 caractères), **jamais dans le corps**. Ne pas l'écrire en `<p><em>…</em></p>` en tête d'article (elle s'afficherait en italique et doublerait le chapeau).

---

## Annexe — menus anti-répétition

Ces listes ne sont **pas des templates**. Elles existent pour une seule raison :
sur un cluster de 7 à 30 paires, le même angle rédigé par le même modèle
converge vers la même ouverture. Le menu casse cette convergence.

**Mode d'emploi.** Piocher réellement au hasard — ne jamais privilégier la
première entrée — puis **reformuler**. Si la structure retenue ressemble à une
précédente, changer l'ordre des mots, le verbe principal ou le point d'entrée
logique. Recopier une entrée à l'identique reproduit le problème qu'elle est
censée résoudre.

**Interdit** : reprendre mot pour mot une formulation déjà produite ; utiliser
deux fois de suite une structure identique (par exemple deux « ce que le marché
+ verbe » consécutifs).

### Ouvertures de paragraphe d'angle éditorial (§5.4)

- Pourquoi ce sujet prend une importance nouvelle
- Ce qui compte davantage qu'il n'y paraît
- L'élément qui rebat la lecture habituelle
- Ce qui pourrait déplacer le consensus
- L'aspect que peu d'analyses mettent en avant
- Ce qui change sans faire de bruit
- La dimension souvent laissée de côté
- Pourquoi ce thème revient par la bande
- Le point d'attention qui s'installe progressivement
- Ce que révèle une lecture moins immédiate
- Pourquoi l'équilibre actuel n'est pas aussi stable
- Le facteur qui modifie la trajectoire
- Ce que cette situation implique concrètement
- Ce que le marché commence à intégrer par touches
- Pourquoi cette dynamique mérite d'être isolée
- L'angle de lecture qui échappe au flux d'actualité
- Ce qui rend ce sujet plus stratégique qu'il n'y paraît

### Entrées d'intention humaine sous-jacente (§5.5)

- La vraie interrogation derrière ce sujet porte sur…
- Ce type de question revient souvent lorsque…
- Ce débat masque en réalité une inquiétude plus simple :
- Le point de friction pour beaucoup n'est pas tant X que Y
- Ce qui rend ce sujet sensible tient surtout à…
- Derrière cette lecture se joue une crainte implicite :
- Ce raisonnement devient central dès lors que…
- L'erreur n'est pas de se poser la question, mais de la formuler ainsi…

À proscrire : « ce que le lecteur cherche », et toute structure reprise à
l'identique sur deux articles consécutifs.

### Points d'accroche conjoncturels

- Ce que le marché ne mesure pas encore pleinement
- Ce que les prix intègrent imparfaitement

### Ouvertures d'introduction à alterner

Ne jamais enchaîner deux introductions bâties sur un paradoxe explicite, une
opposition « on observe X alors que Y », ou une promesse de compréhension en
dernière phrase. Alterner entre : un fait discret mais précis · un glissement
progressif du cadre · un rappel historique court · un changement de variable
clé · une tension non résolue.

### Tournures analytiques à varier impérativement

Ces quatre-là reviennent d'elles-mêmes et signent le gabarit :

- « la lecture dominante se focalise sur X, alors que le facteur décisif reste Y »
- « le déséquilibre se situe moins sur X que sur la dynamique de Y »
- « l'attention se porte souvent sur X, au détriment de Y »
- « X capte le débat, mais Y conditionne la trajectoire »

Les reformuler systématiquement, ou passer en phrase nominale, ou inverser la
logique causale.

### Respiration stylistique

Tous les deux à trois paragraphes, s'autoriser une phrase très courte, une
phrase nominale, ou une rupture de rythme volontaire. La prose parfaitement
régulière est le signe le plus lisible d'un texte produit en série.

**Règle d'or.** Si deux sorties consécutives présentent une similarité lexicale
ou rythmique perceptible, la seconde est réécrite. Si un autre article du site
pouvait être reconnu comme « issu du même modèle » par sa seule structure, son
rythme ou sa logique interne, la production est invalide.

---

## RAPPEL BLOQUANT — Zéro commentaire HTML dans le contenu publié

Les marqueurs de section en commentaire HTML utilisés dans les templates de ce skill
(`<!-- 1. INTRO -->`, `<!-- 5. MACRO TAKEAWAY -->`, etc.) sont des **repères d'assemblage**.
Ils ne survivent pas dans le HTML livré : on les retire avant de coller le contenu ou d'émettre
le bundle.

Motif : Autoptimize scanne `<script>` / `<style>` en regex **sans ignorer les commentaires HTML**.
Une balise littérale citée en prose dans un commentaire fait avaler du texte au minifieur JS,
provoque une fatale dans le callback de buffer et renvoie un **HTTP 500 avec le corps complet** —
page normale dans le navigateur, invisible pour Google. Incident du 27 août 2026, 8 pages
désindexées. `wpautop` mutile en plus ces commentaires (enveloppe en `<p>`, saut de ligne inséré
au milieu dès qu'un nom de balise bloc y figure).

Règle canonique, vérifications mécaniques et alternative (commentaire PHP dans le snippet) :
voir `eco3min-import-contenu-bilingue`, section « RÈGLE FIGÉE (août 2026) ».

Contrôle avant livraison :

```python
import re
assert not re.findall(r'<!--.*?-->', html, re.S), "commentaire HTML dans le contenu"
```

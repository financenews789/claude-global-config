---
name: formats-eco3min
description: "Catalogue des formats HTML rédactionnels d'Eco3min (eco3min.fr), FR et EN : chapeau et intro éditoriale, TL;DR de tête, les quatre encarts (🧭 Lecture eco3min, Erreur fréquente, À retenir, Cadre d'analyse), FAQ SEO inline, extraits partageables, paragraphe d'angle et intention humaine, modes d'introduction A/B/C, méta-titre, ancres internes, sources autorisées, liens outils, format HTML Gutenberg, menus anti-répétition. Activer pour toute rédaction ou révision structurée d'un article, d'une étude, d'une page autoportante, d'une FAQ ou d'une Q&A destinée au site, et pour les articles du projet B Writer et les pages du pipeline page bilingue : « écris l'article », « mets un encart », « ajoute un TL;DR », « À retenir ou Erreur fréquente ? », « Lecture eco3min », « chapeau », « FAQ inline », « quel mode d'intro », « quelles ancres », « quelle longueur », « majeur ou satellite », « registre de la page », « eco3min-callout », « eco3-tldr », « rank_math_description ». SKILL.md = colonne vertébrale (règles bloquantes et quotas de chaque section avec leurs numéros d'origine §1 à §12, contrôles Python, rappel zéro commentaire HTML) ; références dans references/ (à lire quand la section le dit) : 01 hiérarchie et structure d'article, 02 chapeau, intro et templates des encarts, 03 TL;DR, blocs spéciaux et modes d'intro, 04 méta-titre, ancres, sources, outils et HTML, 05 menus anti-répétition ; pas de scripts/. Doctrines : boîte à outils, pas checklist — l'angle décide quels patterns mobiliser ; signature MAJEUR / étude = TL;DR + 🧭 Lecture eco3min, satellite = TL;DR + exactement 1 encart, plafond ~3 blocs étiquetés, jamais trois récaps en puces ; double classe eco3min-callout + variante obligatoire, une variante seule se rend en paragraphe nu (erreur d'anciennes guidelines propagée sur les articles produits) ; TL;DR obligatoire sur tout article, exclu des piliers, sous-piliers et Q&A, lead ≤35 mots FR / ≤30 EN ; implications concrètes = impacts observables, jamais des actions (frontière AMF) ; sur page autoportante la longueur s'arbitre page par page et n'est jamais une cible, asymétrie EN/FR normale, comptage regex surcompte de 5 à 8 % ; méta-titre sans date ni année ; un seul dispositif d'angle par article ; maximum 1 lien outil ; méta-description dans rank_math_description, jamais dans le corps ; zéro commentaire HTML dans le contenu publié (incident Autoptimize du 27 août 2026, 8 pages désindexées). Hors périmètre : identité éditoriale, style et règles AMF → editeur-eco3min ; blocs .eco3-* des pages piliers et sous-piliers → pilier-kit ; assemblage et import des pages → eco3min-import-contenu-bilingue ; hub Q&A → production-q-and-a ; silos, levels et metas → archi-eco3min. Combiner avec editeur-eco3min, archi-eco3min, pilier-kit, production-research-study, production-q-and-a, production-dataset, eco3min-import-contenu-bilingue."
---

# Catalogue des formats Eco3min

> **Philosophie de ce skill.** C'est une **boîte à outils**, pas une checklist. Aucun pattern n'est obligatoire en soi — c'est l'angle, la longueur et la nature de l'article qui décident. Un article court analytique peut très bien n'avoir aucun encart. Un article majeur en a généralement 2 ou 3. Si un pattern n'apporte rien à un article donné, il ne doit pas être inséré pour cocher une case.
>
> Pour l'identité éditoriale et la conformité AMF, voir le skill `editeur-eco3min` (les deux skills se complètent).

---

## COMMENT LIRE CE SKILL (découpage du 16/09/2026)

Ce fichier est la colonne vertébrale : la philosophie, puis pour chaque section les règles BLOQUANTES et les quotas, sous leurs numéros d'origine (§1 bis, §4, §5.1, §6, §8… : d'autres skills et des CLAUDE.md de projets y renvoient). Les critères « quand l'utiliser / quand s'en passer », les templates HTML, les tableaux, les exemples et les menus ont été déplacés VERBATIM dans `references/` et font foi au même titre que ce fichier. Chaque section ci-dessous nomme le fichier à lire ; le lire est obligatoire au moment indiqué, pas facultatif. Pas de `scripts/` : les deux contrôles Python tiennent en deux lignes et restent ici.

| Fichier | Contenu | À lire |
|---|---|---|
| `references/01-hierarchie-structure-article.md` | §1, §1.1, §1.2, §1 bis : tableau majeur / satellite, registres des pages autoportantes, ce qui tombe faute de cluster, arbitrage de longueur, cinq éléments, variation structurelle | avant de fixer le registre, la longueur et la charpente d'un article ou d'une page |
| `references/02-chapeau-intro-encarts.md` | §2, §3, §4 : chapeau, intro éditoriale, doctrine de sobriété, double classe, templates des quatre encarts | avant d'écrire la tête d'article, puis avant de poser tout encart |
| `references/03-blocs-speciaux-modes-intro.md` | §5, §6 : TL;DR de tête et son template, FAQ SEO, extraits partageables, angle éditorial, intention humaine, modes A/B/C | avant d'écrire le TL;DR, puis avant de choisir le mode d'introduction |
| `references/04-titre-ancres-sources-outils-html.md` | §7 à §12 : méta-titre, ancres internes, sources autorisées, tableau des outils, bulletin, format HTML | avant le méta-titre et les liens internes, puis avant l'assemblage HTML final |
| `references/05-annexe-menus-anti-repetition.md` | Annexe : ouvertures d'angle éditorial, entrées d'intention humaine, accroches conjoncturelles, ouvertures d'introduction, tournures à varier, respiration stylistique | avant chaque paragraphe d'angle ou d'intention, et sur toute série d'articles (cluster, lot de pages) |

---

## §1 — Hiérarchie majeur / satellite, pages autoportantes (lire `references/01-hierarchie-structure-article.md`)

Bloquant :
- MAJEUR : pose le cadre conceptuel d'un cluster ; satellite : creuse un point précis. **Règle anti-cannibalisation** : le majeur ne descend pas dans les détails (réservés aux satellites) ; les satellites ne redéfinissent pas le cadre général (réservé au majeur).
- Blocs étiquetés : majeur = TL;DR + 🧭 Lecture (signatures) + ≤1 autre ; satellite = TL;DR + 1 encart + synthèse finale. Longueur indicative en cluster : fourchette du blueprint (défaut 2 500–4 000 pour le majeur, ancien plafond 3 000 supprimé en juill. 2026 ; défaut 1 500–2 500 pour le satellite).
- §1.1 Pages autoportantes (pipeline page bilingue) : registre MAJEUR = « Every X since Y », étude de recherche, page record, page dataset, time-machine ; SATELLITE = Q&A, page outil / simulateur / calculateur. Le registre se choisit sur la **nature de la page, pas sur sa longueur**. Les quotas d'encarts du §4 suivent le registre.
- §1.2 Sur une page autoportante tombent, faute d'objet : la rotation des modes A/B/C (§6, la grille reste utile) ; la variation du type d'encart ; l'unicité des ancres à l'échelle du cluster (§8), remplacée par l'unicité dans la page plus une vérification dans `maillage.csv` ; l'anti-cannibalisation intra-cluster, remplacée par une anti-cannibalisation site-wide contre le snapshot ; les fourchettes de longueur. **À la place, la longueur s'arbitre page par page et se justifie** sur quatre déterminants dans cet ordre : ce que l'intention exige · la densité de la donnée disponible · le format · le voisinage dans le snapshot. La longueur est une **conséquence** du contenu, jamais une cible. Ni remplissage, ni troncature. Si une skill `production-*` fixe une fourchette pour ce type de page, elle prévaut.
- **L'asymétrie EN/FR n'est pas un défaut à corriger** (l'anglais sort 7 à 10 % plus court) : ne pas rembourrer l'EN. Le comptage par `re.sub(r"<[^>]+>", " ", html).split()` **surcompte de 5 à 8 %** : l'annoncer comme un comptage regex, jamais comme un nombre de mots réel.

## §1 bis — Structure éditoriale d'un article de cluster (lire `references/01-hierarchie-structure-article.md`)

Bloquant :
- Cinq éléments, **sans ordre imposé** : un fait déclencheur récent ; une analyse des mécanismes ; une mise en perspective macro ou historique ; au moins un scénario alternatif ou risque ; des implications concrètes.
- « Implications concrètes » = impacts économiques **observables** (ménages, entreprises, marchés). Jamais des actions à entreprendre : c'est une frontière AMF, pas une nuance de style.
- Nombre, intitulé et ordre des sections **libres** ; une section absente si elle n'apporte rien ; réorganiser l'ordre environ une fois sur quatre. Borne haute de longueur atteinte → prioriser dans cet ordre : analyse centrale, implications concrètes, scénarios.
- Variation structurelle **obligatoire** : certains articles concluent sans liste, certains ne contiennent aucune liste, d'autres placent leur unique liste dans le dernier tiers ; alterner paragraphes courts et un paragraphe long. Test : si un autre article du site pouvait être reconnu comme « issu du même modèle » par sa seule structure, réécrire.

## §2–§3 — Chapeau et intro éditoriale (lire `references/02-chapeau-intro-encarts.md`)

Bloquant :
- Chapeau `<p class="eco3min-chapeau">` : 1 à 2 phrases, 30 à 45 mots ; phrase 1 = mécanisme économique, phrase 2 = conséquence ; ton analytique sans emphase ; ne reprend pas l'introduction ; pas de `<strong>`, pas de `<em>`. Sur les articles de fond et études de cas ; jamais sur FAQ et Q&A (redondant avec la question) ni sur les notes courtes.
- Intro éditoriale `<p class="eco3min-intro">` : 1 paragraphe, 20 à 40 mots, couplée à un chapeau, ne le répète pas, pose l'angle sans conclure.
- **Ordre dans la page** : H1 → chapeau → intro éditoriale → image éventuelle → introduction. Le TL;DR de tête (§5.1) s'insère juste après chapeau + intro éditoriale, AVANT l'introduction.

## §4 — Encarts : sobriété, quotas, double classe (lire `references/02-chapeau-intro-encarts.md`)

Bloquant :
- **Doctrine de sobriété (style FT).** La prose porte l'analyse ; les blocs étiquetés la servent. Sur un MAJEUR / une étude : signature citable = **TL;DR de tête (§5.1) + 🧭 Lecture eco3min (§4.1)** ; le reste (Erreur fréquente, À retenir, Cadre, FAQ, extraits) est optionnel. Sur un satellite : signature = **TL;DR de tête + exactement 1 encart** (À retenir OU Erreur fréquente). 🧭 Lecture eco3min et 🧠 Cadre d'analyse sont **réservés aux MAJEURs / études**.
- **Plafond ~3 blocs étiquetés par article** (les 2 signatures + au plus un autre). **Jamais empiler trois récaps en puces** (TL;DR + À retenir + extraits partageables). Si retirer un bloc ne fait rien perdre au lecteur, ne pas le mettre.
- Phrase-pivot (`editeur-eco3min` §5, obligatoire par article) : elle vit d'abord dans la prose ; reprise UNE fois au plus dans la 🧭 Lecture eco3min ou la conclusion — jamais dans les deux, jamais trois occurrences au total.
- 🧭 Lecture eco3min (§4.1) : 1 seule phrase, ≤25 mots, ton affirmatif (pas de "peut", "tend à", "souvent"), en rupture avec une lecture courante, placée en fin du raisonnement analytique. Erreur fréquente (§4.2) : 3 phrases — l'erreur, pourquoi elle trompe, la lecture correcte. À retenir (§4.3) : 2 à 4 points analytiques, jamais prescriptifs, seulement s'ils apportent ce que le TL;DR de tête ne contient pas déjà. Cadre d'analyse (§4.4) : rare, un seul si présent.
- **Double classe obligatoire.** Tout encart porte **deux** classes sur le même `div` : `eco3min-callout` **plus** sa variante (`eco3min-lecture`, `eco3min-warning`, `eco3min-keypoints`, `eco3min-method`), le titre dans un `div.eco3min-callout-title` à l'intérieur. **Une variante seule est INVALIDE** : l'encart se rend en paragraphe nu, sans erreur ni signal (erreur d'une ancienne version des guidelines, propagée sur les articles produits pendant qu'elle faisait foi). Le TL;DR de tête n'est **pas** un encart : balisage `eco3-tldr`, jamais `eco3min-callout`. Aucun repère `<!-- wp:html -->` autour des encarts : zéro commentaire HTML, sans exception (§12, RAPPEL BLOQUANT en fin de fichier ; décision du 16/09/2026).

Contrôle avant livraison :

```python
import re
mauvais = re.findall(r'<div class="eco3min-(?:lecture|warning|keypoints|method)"', html)
assert not mauvais, "encart sans la classe eco3min-callout : %s" % mauvais
```

## §5 — Blocs spéciaux : TL;DR obligatoire, FAQ, extraits, angle (lire `references/03-blocs-speciaux-modes-intro.md`)

Bloquant :
- §5.1 TL;DR de tête `.eco3-tldr` : **obligatoire sur tout article** (MAJEUR, satellite, étude, "Every X", chart), placé juste après chapeau + intro éditoriale, AVANT l'introduction. **Exclus** : pages piliers/sous-piliers (voir `pilier-kit`) et Q&A (déjà un TL;DR propre). Seule dérogation : de rares notes < ~450 mots. Bloc de tête, pas un encart : il ne compte pas dans le "1 encart" des satellites.
- Forme : `lead` = 1 phrase auto-portante (citable telle quelle, sans "cet article…"), **≤ 35 mots FR / ≤ 30 mots EN** ; 2 à 4 puces (3 par défaut), chacune un fait + un concret (chiffre + source/date, seuil, ou mécanisme nommé) tiré du corps ; **anti-uniformité** : varier l'ouverture (proscrire en boucle "le consensus regarde X / le vrai signal est Y", "ce qui change sans bruit", "pas X mais Y", "X n'est plus seulement Y") et le nombre de puces ; CSS `.eco3-tldr` global, pas de style inline ; AMF comme le reste. Rétro-équipement de l'existant : plugin `eco3min-tldr`.
- FAQ SEO (§5.2) : 3 à 5 vraies requêtes longue traîne, réponses 2–4 phrases ; **anti-cannibalisation du hub Q&R** : seulement si les questions ne sont pas déjà traitées par une page du hub, et sans second JSON-LD QAPage (balisage géré côté hub).
- Extraits partageables (§5.3) : 3 punchlines ≤240 caractères ; **jamais cumulés avec le TL;DR de tête ET l'encart "À retenir"** (3ᵉ récap en puces, cf. §4).
- **Un seul dispositif d'angle par article** : §5.4 (angle éditorial), §5.5 (intention humaine) et le « signal faible » (`editeur-eco3min` §3) jouent le même rôle ; n'en mobiliser qu'un seul.

## §6 — Modes structurels d'introduction (lire `references/03-blocs-speciaux-modes-intro.md`)

Bloquant :
- Satellites : trois modes, **choisir un seul**, ne pas les combiner — A fait précis (chiffre daté observable), B objection (croyance répandue à déconstruire), C mécanisme discret (mécanisme micro/institutionnel concret). Le choix dépend de l'angle : seuil franchi → A, lecture dominante à corriger → B, transmission peu visible → C.
- Majeurs : introduction plus posée, point d'accroche conjoncturel intégré au raisonnement plutôt que mis en avant.

## §7–§8 — Méta-titre, ancres internes (lire `references/04-titre-ancres-sources-outils-html.md`)

Bloquant :
- Méta-titre : **interdit** année explicite (2025, 2026), date calendaire, "actuellement", "aujourd'hui", "cette année" ; le titre reste pertinent dans 6–12 mois ; actualité implicite (mécanisme qui évolue, seuil franchi, inflexion, déséquilibre) sans dater. **Test** : si le titre est amélioré en supprimant la date, la version sans date est obligatoire. Pas de titre vague ("tendances", "panorama", "le marché de…").
- Ancres, trois règles cumulatives : inter-articles (même cible → ancres différentes d'un article à l'autre) ; intra-article (aucune ancre répétée : 5 liens = 5 ancres distinctes) ; qualité (3 à 8 mots, descriptive de la cible, intégrée naturellement dans une phrase, jamais "cliquez ici", "voir ici", "lire aussi", "en savoir plus").

## §9–§12 — Sources, outils, bulletin, format HTML (lire `references/04-titre-ancres-sources-outils-html.md`)

Bloquant :
- Sources (§9) : citer **institution + date** dans le flux du texte ; pas de section "Sources" en fin d'article, pas d'URL externes, pas de notes de bas de page ; données estimées préfixées `≈` avec la méthode explicitée. Liste des sources autorisées et exemples conformes dans la référence.
- Outils Eco3min (§10) : **Maximum 1 lien outil par article. Aucun lien outil = choix valide.** Ancre neutre et descriptive, jamais "voir notre outil", "outil eco3min" ; lien dans un paragraphe analytique, jamais en intro ou conclusion ; si retirer le lien ne change rien à la compréhension → ne pas l'insérer. Les trois outils du pôle macro et leurs URL sont dans la référence ; les outils éligibles dépendent du pilier, la pipeline B reçoit la liste en paramètre.
- Bulletin macro (§11) `/barometre-macroeconomique-feuille-de-route/` : ponctuel, jamais systématique, ancre naturelle, pas d'ancre SEO.
- Format HTML (§12), compatible Gutenberg : **balises autorisées** `<h2>`, `<h3>`, `<p>`, `<strong>`, `<em>`, `<ul>`, `<li>`, `<a href="">` ; **interdit** Markdown, `<html>`, classes CSS custom (sauf préfixe `eco3min-` et le bloc `.eco3-tldr`), styles inline. **Méta-description** : champ `rank_math_description` du JSON de sortie (≤155 caractères), **jamais dans le corps**, jamais en `<p><em>…</em></p>` en tête d'article.

## Annexe — menus anti-répétition (lire `references/05-annexe-menus-anti-repetition.md`)

Bloquant :
- Les menus ne sont **pas des templates** : sur un cluster de 7 à 30 paires, le même modèle converge vers la même ouverture. Piocher réellement au hasard — jamais la première entrée — puis **reformuler**. **Interdit** : reprendre mot pour mot une formulation déjà produite ; deux structures identiques de suite ; « ce que le lecteur cherche ».
- Ne jamais enchaîner deux introductions bâties sur un paradoxe explicite, une opposition « on observe X alors que Y », ou une promesse de compréhension en dernière phrase.
- Les quatre tournures qui signent le gabarit (« la lecture dominante se focalise sur X, alors que le facteur décisif reste Y » et ses trois sœurs, listées dans la référence) se reformulent systématiquement, ou passent en phrase nominale, ou inversent la logique causale.
- Respiration : tous les deux à trois paragraphes, une phrase très courte, nominale ou une rupture de rythme.

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

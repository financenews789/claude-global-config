---
name: production-q-and-a
description: Production et révision rigoureuse des pages Q&A d'Eco3min (hub /en/qa/ et /qr/) — couche SEO d'autorité bilingue FR/EN qui redistribue le trafic vers piliers, études et datasets. Couvre la reformulation descriptive AMF-compliant, la structure HTML complète (TL;DR snippet-ready, TOC, Short answer, What the data shows, Why it happens avec synthèse par régime obligatoire, What it means for actors, Practical observation, Go deeper, Related questions, FAQ finale), les règles de densité par paragraphe, la classification A/B/C des chiffres avec web_search obligatoire pour les chiffres point précis non iconiques, l'angle distinctif obligatoire par FAQ, le balisage JSON-LD QAPage, et les règles de maillage interne. À activer pour toute création ou révision de page Q&A.
---

# Production de pages Q&A — Eco3min

> Ce skill couvre la rédaction et la révision des pages du hub Q&A bilingue d'Eco3min (`/en/qa/` en anglais, `/qr/` en français). Pour le pipeline de production batch (mapping 350 FAQ, JSON d'import WordPress, fragments PHP, workflow Polylang), voir les Custom Instructions du Projet Claude dédié — ce skill ne duplique pas ces éléments. Voir aussi `editeur-eco3min` pour l'identité éditoriale et l'AMF, `formats-eco3min` pour les patterns rédactionnels, `visuels-eco3min` pour la data viz.

---

## 1. Règle d'or éditoriale

> **Une FAQ Eco3min optimale doit pouvoir être lue par un journaliste FT, un universitaire, et un PM de hedge fund sans qu'aucun des trois trouve qu'elle est inférieure à ce qu'il aurait pu produire lui-même.**

C'est le test de qualité ultime. Si tu doutes qu'une FAQ passe ce test, tu la réécris avant rendu. Pas de demi-mesure.

---

## 2. Reformulation descriptive de la question (AMF règle 4)

C'est la **première vérification** avant toute rédaction. Une question prescriptive ne peut pas être traitée — elle doit être reformulée descriptive avant que la page existe.

### 2.1 Conversion systématique

| ❌ Prescriptive (interdite) | ✅ Descriptive (publiable) |
|---|---|
| Should I sell stocks before a recession? | What has historically happened to stocks in the 12 months before US recessions? |
| Faut-il acheter de l'or en période d'inflation ? | Comment l'or s'est-il comporté lors des épisodes inflationnistes ? |
| Is bitcoin a good investment? | What has been bitcoin's risk-return profile compared to traditional assets? |
| Dois-je acheter des obligations longues maintenant ? | Comment les obligations longues se sont-elles comportées à travers les cycles de taux depuis 1980 ? |

### 2.2 Patterns de reformulation

**Anglais**
- "Should I…?" → "What has historically happened when…?"
- "Is X a good…?" → "How has X performed compared to…?"
- "When to buy/sell…?" → "What has triggered past episodes of…?"

**Français**
- "Faut-il…?" → "Comment X s'est-il comporté lorsque…?"
- "Dois-je…?" → "Quelle dynamique observe-t-on lorsque…?"
- "Est-ce le moment de…?" → "Quels signaux ont historiquement précédé…?"

### 2.3 Test final

La question reformulée doit pouvoir recevoir une **réponse factuelle datée**. Si la seule réponse possible reste "ça dépend de votre profil", la question est encore prescriptive — la reformuler à nouveau.

---

## 3. Structure HTML complète

Chaque page (FR comme EN) suit rigoureusement ce template. Pas de variation structurelle.

```html
<!-- 1. TL;DR -->
<div class="eco3-qa-tldr">
<p><strong>[3 phrases sèches, snippet-ready. Phrase 1 = définition. Phrase 2 = mécanisme. Phrase 3 = implication/nuance.]</strong></p>
</div>

<!-- 2. TABLE OF CONTENTS -->
<div class="eco3-qa-toc">
<p><strong>In this article</strong></p>  <!-- ou "Dans cet article" pour FR -->
<ul>
<li><a href="#short-answer">The short answer</a></li>
<li><a href="#data">What the data shows</a></li>
<li><a href="#mechanism">Why it happens — the macro mechanism</a></li>
<li><a href="#investors">What it means for different economic actors</a></li>
<li><a href="#action">Practical observation</a></li>
<li><a href="#deeper">Go deeper</a></li>
<li><a href="#related">Related questions</a></li>
<li><a href="#faq">Frequently asked questions</a></li>
</ul>
</div>

<!-- 3. SHORT ANSWER ~200 mots — DENSITÉ : 3 paragraphes de 2-3 phrases, jamais plus de 4 -->
<h2 id="short-answer">The short answer</h2>
<p>[Réponse intuitive, exemple concret ou analogie]</p>
<p>[Nuance ou contexte qui complique]</p>
<p>[Conclusion pédagogique]</p>
<p>→ <em>New to [domain]?</em> <a href="[URL hub éducation]">[Nom hub]</a></p>

<!-- 4. WHAT THE DATA SHOWS ~300 mots — LISTE À PUCES OBLIGATOIRE quand 3+ stats -->
<h2 id="data">What the data shows</h2>
<p>[Source FRED/BIS/etc + période + observation principale]</p>
<p>Le contexte chiffré (Source, période) :</p>
<ul>
<li>[Stat 1 avec date]</li>
<li>[Stat 2 avec date]</li>
<li>[Stat 3 avec date]</li>
<li>[Stat 4 avec date]</li>
</ul>
<p>[L'EXCEPTION qui nuance]</p>
<p>→ <em>Dataset:</em> <a href="[URL dataset]">[Nom dataset]</a></p>

<!-- 5. WHY IT HAPPENS ~350 mots — DENSITÉ STRICTE : max 4 phrases par canal -->
<h2 id="mechanism">Why it happens — the macro mechanism</h2>
<p>[Introduction au mécanisme]</p>
<p><strong>[Canal 1]</strong> [explication ≤4 phrases + lien pilier]</p>
<p><strong>[Canal 2]</strong> [explication ≤4 phrases — y placer l'angle distinctif si possible + lien]</p>
<p>[Phrase courte de transition optionnelle pour éviter le mur de texte]</p>
<p><strong>[Canal 3 si pertinent]</strong> [explication ≤4 phrases]</p>
<p>[Synthèse par régime — PARAGRAPHE COMPLET 3-5 phrases contrastant 2-3 régimes]</p>

<!-- 5bis. PHRASE SIGNATURE — DOIT REFLÉTER L'ANGLE DISTINCTIF -->
<p class="eco3-qa-signature"><em>[Aphorisme mémorable, 1-2 lignes, citable isolément]</em></p>

<p>→ <em>Framework:</em> <a href="[URL pilier]">[Nom pilier]</a></p>

<!-- 6. WHAT IT MEANS FOR ACTORS ~250 mots — DENSITÉ : 2-3 phrases par catégorie, jamais plus -->
<h2 id="investors">What it means for different economic actors</h2>
<p><strong>Savers</strong> [description AMF-compliant, 2-3 phrases]</p>
<p><strong>Investors</strong> [description AMF-compliant, 2-3 phrases]</p>
<p><strong>[Troisième catégorie]</strong> [description, 2-3 phrases]</p>
<p>[Paragraphe final type "a common error is..."]</p>

<!-- 7. PRACTICAL OBSERVATION — VARIATION OBLIGATOIRE PAR BATCH (voir section 9) -->
<h2 id="action">Practical observation</h2>
<div class="eco3-qa-action">
<p><strong>What the data suggests for understanding your situation:</strong></p>
<ul>
<li><strong>Question to ask yourself:</strong> [variante : auto-réflexive / diagnostique / scénaristique / comparative]</li>
<li><strong>Data to monitor:</strong> [variante : niveau / spread / diffusion / vélocité]</li>
<li><strong>Historical parallel:</strong> [date précise + chiffre vérifiable obligatoires]</li>
<li><strong>What the literature documents:</strong> [auteur — varier dans le batch]</li>
</ul>
<p><em>This is descriptive information to help you frame your own analysis. Eco3min does not provide investment advice.</em></p>
</div>

<!-- 8. GO DEEPER -->
<h2 id="deeper">Go deeper</h2>
<div class="eco3-qa-deeper">
<p>📊 <strong>Full study:</strong> <a href="[URL étude]">[Titre]</a></p>
<p>📁 <strong>Datasets:</strong> <a href="[URL]">[Nom]</a> · <a href="[URL]">[Nom]</a></p>
<p>📖 <strong>Related analysis:</strong> <a href="[URL]">[Titre]</a></p>
</div>

<!-- 9. RELATED QUESTIONS — 4 liens, PROXIMITÉ THÉMATIQUE STRICTE -->
<h2 id="related">Related questions</h2>
<ul class="eco3-qa-related">
<li><a href="[URL FAQ 1]">[Question]</a></li>
<li><a href="[URL FAQ 2]">[Question]</a></li>
<li><a href="[URL FAQ 3]">[Question]</a></li>
<li><a href="[URL FAQ 4]">[Question]</a></li>
</ul>

<!-- 10. FAQ — 3 sous-questions neutres — UNE D'ELLES DÉTAILLE L'ANGLE DISTINCTIF -->
<h2 id="faq">Frequently asked questions</h2>
<h3>[Sous-question 1 — "Is X relevant?" / "How does X differ from Y?" — JAMAIS "Should I…?"]</h3>
<p>[Réponse descriptive 80-120 mots]</p>
<h3>[Sous-question 2 — détaille l'angle distinctif]</h3>
<p>[Réponse descriptive]</p>
<h3>[Sous-question 3]</h3>
<p>[Réponse descriptive]</p>

<!-- 11. FOOTER -->
<div class="eco3-qa-footer">
<p><em>Published by Eco3min Research · Updated [MOIS AAAA]</em><br>
<em>Eco3min explains macro dynamics through data, not opinions.</em><br>
→ <a href="https://eco3min.fr/en/about/">Methodology</a></p>
</div>
```

**Longueur cible** : 1 200–1 400 mots par page, hors TL;DR et footer. Même longueur en FR et EN pour chaque paire.

---

## 4. TL;DR — règles strictes

- **Exactement 3 phrases**, pas 2, pas 4
- **Format snippet-ready** : autosuffisantes, sans référence à "voir plus haut"
- **Architecture** : phrase 1 = définition, phrase 2 = mécanisme, phrase 3 = implication ou nuance
- **Aucun "vous"**, aucun adressage direct
- **Aucune prescription** (cf. AMF)
- **Au moins un chiffre** dans la phrase 1 ou 2
- **Au moins une source nommée** sur l'ensemble

Le contenu textuel pur de la TL;DR (sans HTML, sans `<strong>`) sert également pour le champ `answer` du JSON-LD QAPage et pour les fragments PHP de schema.

---

## 5. Phrase signature — distinction Eco3min

Une seule phrase, mémorable, aphoristique, citable isolément. Conçue pour être citée par AI Overviews, médias et lecteurs.

**Règle clé** : la phrase signature **doit refléter l'angle distinctif** (cf. section 7). Si l'angle distinctif est "le QE a comprimé la prime de terme à zéro pendant 5 ans", la phrase signature reformule cet angle de manière percutante.

**Critères**
- Affirmative (pas de "may", "could", "tend to")
- Distinctive (formule un mécanisme, pas une généralité)
- Auto-suffisante (compréhensible hors contexte)
- 15 à 25 mots
- Test : si une autre Q&A du hub pourrait reproduire cette signature à l'identique, elle n'est pas distinctive

---

## 6. Vérification factuelle des chiffres — classification A/B/C

C'est l'une des règles les plus critiques. Aucun chiffre point précis ne peut être produit sans vérification ou marquage explicite.

### 6.1 Catégorie A — Chiffres iconiques stables

Utilisables sans web_search, mais **avec source nommée**. Exemples :
- Pic CPI US à 9,1 % en juin 2022
- Fed Funds +525 bp mars 2022 → juillet 2023
- Pic du bilan Fed à ≈ 8,97 Tn$ en avril 2022
- Récessions NBER datées (1990-91, 2001, 2008-09, 2020)
- Krachs majeurs (1929, 1987, 2000, 2008, 2020)
- Constantes académiques (CAPE moyen historique ≈ 17, ERP US historique 4-6 %)

Source identifiable : FRED série, NBER, Shiller dataset.

### 6.2 Catégorie B — Chiffres précis non iconiques

**web_search OBLIGATOIRE** avant utilisation. Exemples :
- Toute estimation point précise ("ERP implicite à 4,60 % en janvier 2024")
- Tout chiffre annualisé d'un indice ou facteur sur fenêtre spécifique
- Tout volume agrégé annuel (buybacks, M&A, IPO)
- Toute statistique attribuée à un auteur ou rapport spécifique
- Tout chiffre qui « semble bon » mais que tu ne peux pas confirmer dans ton contexte

**Si web_search ne confirme pas** → REMPLACER par fourchette qualitative ("around 4-6%", "approximately one-third", "the literature documents premia of meaningful magnitude").

### 6.3 Catégorie C — Approximations et ordres de grandeur

Autorisés avec marqueur ("approximately", "around", "roughly") si l'ordre de grandeur est défendable. Préciser systématiquement la période ("over 1990-2020").

### 6.4 Refus formel

**Ne JAMAIS produire un chiffre point précis (catégorie B) inventé ou approximé.** Mieux vaut une fourchette honnête qu'un chiffre faux.

### 6.5 Whitelist des sources nommables

Sources autorisées comme références chiffrées, citables sans vérification au-delà de l'ordre de grandeur :
FRED, NBER, BIS, BEA, BLS, Shiller (online data), Damodaran (NYU Stern), Kenneth French data library, S&P Dow Jones Indices, MSCI, FactSet, IBES, Russell, CBOE, IMF WEO, Fed (FRED-Atlanta-NY-StLouis publications), ECB SDW, Eurostat, Banque de France, INSEE.

Toute autre source nommée doit être web_search-vérifiée.

---

## 7. Angle distinctif obligatoire

Chaque FAQ doit contenir AU MOINS UN angle non-trivial qu'un lecteur ne trouverait pas dans les 10 premiers résultats Google. **C'est ce qui distingue Eco3min d'Investopedia.**

### 7.1 Définition d'un angle distinctif

- Divergence entre sagesse conventionnelle et données récentes (ex : "la prime small-cap a quasi disparu post-2000")
- Nuance de régime que les explications standards ignorent (ex : "le facteur qualité crashe en début de reprise comme 2009")
- Mécanisme structurel sous-théorisé en grand public (ex : "les 0DTE ont changé la lecture du put/call ratio")
- Faille théorique d'un cadre populaire (ex : "le modèle Fed mélange réel et nominal")
- Changement de régime récent qui invalide les manuels (ex : "le QE a comprimé la prime de terme à zéro pendant 5 ans")

### 7.2 Placement dans la structure

L'angle distinctif apparaît **en trois endroits** :
- Cité d'abord dans la **section "Why it happens"** (canal 2 ou 3, formulation dense)
- Réaffirmé dans la **phrase signature**
- Détaillé dans **une des trois sous-questions du FAQ final**

### 7.3 Ce qui n'est PAS un angle distinctif

- Définir un concept (banal)
- Citer un auteur académique seul (insuffisant)
- Décrire un mécanisme classique (banal)
- Donner une stat historique seule (banal)

### 7.4 Test

Si l'angle peut tenir en une phrase de la forme « **Contrairement à ce que [la sagesse conventionnelle / les manuels / le grand public] suggère, [observation empirique récente]** », c'est un angle distinctif. Si tu ne peux pas formuler la phrase, l'angle est insuffisant — la FAQ doit être retravaillée.

---

## 8. Synthèse par régime — paragraphe complet obligatoire

La phrase « Synthesis by regime » qui clôt la section mécanisme doit être un **paragraphe complet de 3-5 phrases** contrastant explicitement 2 régimes — idéalement 3.

### 8.1 Format imposé

Mention obligatoire de :
- Contexte macro (inflation, taux réels, liquidité)
- Observation historique correspondante
- Paramètre qui définit la transition entre régimes

### 8.2 Exemple BON

> Synthèse par régime : en disinflation avec taux réels en baisse (2019-2021), les actions de croissance et l'or surperforment ; en stagflation avec taux réels en hausse (2022), value, matières premières et duration courte tendent à dominer ; le pivot s'est joué sur le passage des taux réels 10 ans de −1,2 % à +2,5 % en 18 mois.

### 8.3 Exemple INSUFFISANT

> Synthesis by regime: in stable regimes, the factor works; in volatile regimes, it does not.

(Pas de chiffres, pas de période, pas de paramètre de transition.)

---

## 9. Diversification du bloc "Practical observation"

Sur 10 FAQ d'un batch, **varier au moins 3 fois sur les 4 puces**. Sinon, le lecteur reconnaît la formule et la valeur perçue chute.

**Bloc "Question to ask yourself"** (varier la nature)
- Auto-réflexive : "Am I anchored on X or on Y?"
- Diagnostique : "Where in the cycle does my portfolio currently sit?"
- Scénaristique : "What would I observe if regime A were ending?"
- Comparative : "Does my exposure differ from a passive benchmark in this dimension?"

**Bloc "Data to monitor"** (varier la nature)
- Niveau d'indicateur (VIX, taux 10 ans)
- Spread ou écart (HY vs IG, Russell 2000 vs S&P 500)
- Diffusion ou breadth (% d'actions en hausse, dispersion sectorielle)
- Vélocité ou rate of change (révisions à 4 semaines, accélération)

**Bloc "Historical parallel"** : ancrer obligatoirement sur une **date précise et un chiffre vérifiable** (catégorie A ou B web-searched).

**Bloc "What the literature documents"** : varier les auteurs au sein du batch — éviter Damodaran, Shiller ou Fama-French dans plus de 3 FAQ par batch de 10.

---

## 10. Densité par paragraphe — règles strictes

- **Section mechanism** : maximum 4 phrases par sous-paragraphe (canal 1, 2, 3). Si un canal dépasse, scinder ou raccourcir.
- **Section short-answer** : 3 paragraphes de 2-3 phrases, jamais plus de 4 phrases.
- **Section investors** : chaque catégorie en 2-3 phrases, jamais plus.
- **Phrase de respiration** : entre canal 2 et canal 3, autoriser une phrase courte de transition.
- **Règle générale** : maximum 4 phrases par paragraphe (5 pour ouverture de section). Une idée principale par paragraphe.

---

## 11. Maillage interne — règles strictes

### 11.1 Cohérence linguistique
- Liens dans une page **EN** → URLs EN exclusivement
- Liens dans une page **FR** → URLs FR exclusivement
- Pas de croisement (Polylang gère le switch langue natif)

### 11.2 Densité
- **Minimum 6 liens internes** par page
- **Maximum 12 liens internes** par page (éviter la dilution SEO)
- Pas plus de **2 liens par paragraphe**

### 11.3 Test de justification (silencieux, avant placement)

Chaque lien doit pouvoir être justifié par une phrase de la forme « **Le lecteur de cette FAQ veut probablement aussi [URL liée] parce que [raison logique précise]** ».

Vérifier :
1. Le lecteur de la FAQ courante a-t-il une question naturelle qui mène à la FAQ liée ?
2. Le lien est-il dans la même langue (EN→EN, FR→FR) ?
3. Le slug existe-t-il dans une source autorisée ?

Si une réponse est non → lien retiré.

### 11.4 Cross-références au sein d'un batch

Quand on produit un batch, **minimum 2 liens vers des FAQ du même batch** dans chaque FAQ (peut compter dans le minimum 6). Cela crée un mini-cluster d'autorité.

### 11.5 Related Questions — proximité thématique stricte

Les 4 liens de la section Related Questions doivent être thématiquement étroitement liés. Pas de lien vers une FAQ d'un autre domaine si non strictement nécessaire.

### 11.6 Metas éditoriales d'une Q&A — doctrine figée le 17/09/2026

Chaque page Q&A porte, **dès l'import**, `level = faq`, `cluster` = le **pilier thématique** de sa langue (jamais le hub `qa`/`qr`, sauf repli quand aucun pilier ne domine ses liens sortants) et `sub_pilier` = le sous-pilier de ce pilier vers lequel elle renvoie le plus. Le choix se lit dans les liens de la page elle-même : le pilier et le sous-pilier qui reçoivent le plus de liens du bloc « Go deeper » et du corps sont le rattachement. Slugs de piliers et sous-piliers par langue dans `archi-eco3min` (références 03). Le bundle les porte : bloc `eco3min` de « Page bilingue » (Eco3min Import ≥ 2.3.0) ou champs du Q&A Importer ; sinon, seconde passe « MAJ metas » ou `eco3min/set-metas`. Une Q&A laissée sur le hub reste invisible des projets A/B/C (snapshot par silo) et du rattrapage d'orphelins, et ressort dans l'export pending du Cleanup à chaque cycle. Doctrine et historique : `metas-eco3min` §9.4.

---

## 12. Cohérence cross-FAQ dans un batch

### 12.1 Anti-répétition

Dans un même batch de 10 FAQ :
- Pas plus de **3 mentions** du même auteur académique
- Pas plus de **3 mentions** du même parallèle historique (éviter "2008-2009" dans 7 FAQ)
- Pas plus de **4 utilisations** du même dataset interne en lien

### 12.2 Hiérarchie de complexité

- Identifier la FAQ "la plus fondamentale" du batch et y placer un ton plus pédagogique
- Identifier la FAQ "la plus avancée" du batch et y développer un angle technique plus poussé
- Éviter le ton uniforme sur les 10 FAQ

---

## 13. Style et formulations

### 13.1 Voix

Impersonnelle, analytique. Privilégier : "la recherche documente", "les données montrent", "historiquement", "selon FRED".

### 13.2 Formulations nuancées (éviter les absolus)

- ❌ "X means Y" → ✅ "X typically translates to Y"
- ❌ "this proves that..." → ✅ "the evidence suggests that..."
- ❌ "the relationship has weakened considerably" → ✅ "the relationship has become less stable"
- ❌ "always", "never", "every" → ✅ "in most cases", "historically", "generally"

**Exception** : les faits chiffrés vérifiables ne sont pas des absolus. "Inflation peaked at 9.1% in June 2022" reste tel quel.

### 13.3 Aérer la section "What the data shows"

Quand 3+ statistiques chiffrées, **liste à puces obligatoire**. Cette règle s'applique uniquement à cette section pour préserver le ton analytique des autres.

### 13.4 Équivalence FR/EN

Pour chaque paire : même structure, même longueur, mêmes chiffres, phrase signature traduite intelligemment (pas calque littéral).

---

## 14. Conformité AMF — rappels spécifiques aux Q&A

(6 règles complètes dans `editeur-eco3min`. Spécificités Q&A.)

- **Règle 4 systématique** : la question elle-même est descriptive, jamais "Should I…?" ni "Faut-il…?"
- **Règle 1 stricte** : aucun pourcentage d'allocation recommandé, même en exemple
- **Règle 3 stricte** : pas de "Buy X when Y" même reformulé — temporalité descriptive uniquement
- **Règle 6 stricte** : timing toujours empirique daté ("In the 12 months following an inversion…"), jamais opérationnel ("After an inversion, consider…")

Toute phrase contenant "should", "recommend", "advise", "buy", "sell", "allocate", "target", "devrait", "recommander", "conseiller", "acheter", "vendre", "allouer", "cibler" doit être reformulée — sauf si citée entre guillemets depuis une source externe nommée.

Formules acceptables :
- "Historically, [X] has been observed when [Y]"
- "In the 1970s, [Z] experienced [outcome]"
- "Research by [author, year] shows [finding]"

---

## 15. Copyright

- Aucune citation directe de plus de **14 mots** d'une source externe
- **Une seule citation directe par source** dans toute la page
- Sources paraphrasées intégralement

---

## 16. Aucun JavaScript

Le HTML produit ne contient AUCUN script, AUCUN onclick, AUCUN event handler JS. Uniquement HTML statique, classes CSS, liens `<a>`.

---

## 17. JSON-LD QAPage

Type **QAPage**, pas Article. C'est ce qui rend la page éligible aux Q&A boxes Google et aux AI Overviews structurés.

```json
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "[Question reformulée descriptivement, identique au H1]",
    "text": "[Question identique au H1]",
    "answerCount": 1,
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "[TL;DR complète — 3 phrases, identique au texte affiché]",
      "inLanguage": "en",
      "datePublished": "[YYYY-MM-DD]",
      "url": "https://eco3min.fr/en/qa/[slug]/",
      "author": {
        "@type": "Organization",
        "name": "Eco3min",
        "url": "https://eco3min.fr/"
      }
    }
  }
}
```

**Règles strictes**
- `name` et `text` Question : identiques au H1
- `text` Answer : identique à la TL;DR affichée (texte brut, sans `<strong>`)
- `inLanguage` : `"en"` pour `/en/qa/`, `"fr"` pour `/qr/`
- `answerCount` : toujours 1
- Jamais `@type: Article` sur une page Q&A

---

## 18. Slugs et URLs

**Convention**
- Anglais : `https://eco3min.fr/en/qa/[slug-en]/`
- Français : `https://eco3min.fr/qr/[slug-fr]/`

**Règles de slug** : evergreen, keyword-rich, pas de date, 5-6 mots max, pas de stop words ("the", "a", "le", "la"). Les slugs sont **figés dans le master mapping** quand on travaille en batch — jamais inventer un slug par soi-même dans ce contexte.

---

## 19. Méta-description

- Maximum 155 caractères
- Reprend l'essence de la phrase 1 de la TL;DR + un chiffre clé
- Pas de question dans la méta (la question est dans le H1)
- Pas d'incitation prescriptive ("Découvrez si…")

---

## 20. Tableau de vérification béton (AVANT rendu)

Avant de produire les livrables finaux d'un batch, exécuter cette checklist FAQ par FAQ et présenter le résultat sous forme de tableau Markdown.

| # | Slug EN | Chiffres B vérifiés | Angle distinctif | Régime contrasté | Block "Pract." varié | Liens justifiés | Densité OK |
|---|---|---|---|---|---|---|---|
| 1 | slug-en-1 | ✓ ou liste | ✓ + 1 phrase | ✓ + nb régimes | ✓ ou non | ✓ ou nb retirés | ✓ |

**Critères par colonne**

- **Chiffres B vérifiés** : ✓ uniquement si tous les chiffres point précis ont été soit web_search-confirmés, soit dégradés en fourchette qualitative
- **Angle distinctif** : ✓ + phrase au format « Contrairement à X, Y ». Si pas formulable → FAQ à retravailler
- **Régime contrasté** : ✓ + nombre de régimes (minimum 2). Si 1 seul → FAQ à retravailler
- **Block "Pract." varié** : ✓ si variante non utilisée dans les 2 FAQ précédentes du batch
- **Liens justifiés** : ✓ si tous passent le test silencieux de la section 11.3
- **Densité OK** : ✓ si aucun paragraphe ne dépasse 4 phrases (5 pour ouverture)

**Action en cas de ✗** : identifier les FAQ concernées, réécrire les sections fautives AVANT rendu, re-exécuter la checklist, ne livrer que toutes cases ✓.

---

## 21. Mention de vérifications appliquées (post-livraison)

Après les livrables, ajouter une note courte (3-4 lignes max) :

> **Vérifications appliquées** : [résumé en 2 phrases. Ex : « Tous les chiffres point précis ont été web_search-vérifiés sauf X (fourchette qualitative). Chaque FAQ contient un angle distinctif et au moins 2 régimes contrastés. »]

Cette note remplace tout autre commentaire postambule.

---

## 22. Checklist finale pré-publication (page unique)

**Question et reformulation**
- [ ] H1 entièrement descriptif, jamais "Should I" / "Faut-il"
- [ ] Question réceptive à une réponse factuelle datée

**TL;DR**
- [ ] Exactement 3 phrases (définition + mécanisme + implication)
- [ ] Au moins un chiffre, au moins une source nommée
- [ ] Aucun "vous" / "you"

**Vérification factuelle**
- [ ] Tous les chiffres catégorie B web_search-confirmés ou dégradés
- [ ] Sources de la whitelist ou explicitement vérifiées

**Angle distinctif**
- [ ] Formulable au format « Contrairement à X, Y »
- [ ] Présent en section 5 (canal 2 ou 3), phrase signature, sous-question FAQ

**Régime-aware**
- [ ] Synthèse par régime = paragraphe 3-5 phrases
- [ ] Au moins 2 régimes contrastés avec contexte macro et paramètre de transition

**Structure**
- [ ] Toutes les sections HTML présentes dans l'ordre
- [ ] 1 200–1 400 mots hors TL;DR et footer
- [ ] Liste à puces dans "What the data shows" si 3+ stats
- [ ] Densité respectée (max 4 phrases par paragraphe)

**Conformité AMF**
- [ ] Aucun "should/buy/allocate/target" non reformulé
- [ ] FAQ finale en sous-questions descriptives
- [ ] Bloc "Practical observation" avec disclaimer AMF final

**Maillage**
- [ ] 6 à 12 liens internes
- [ ] Tous EN→EN ou FR→FR (jamais croisé)
- [ ] Tous justifiables par le test de la section 11.3
- [ ] Related questions thématiquement étroits

**JSON-LD**
- [ ] Type QAPage (jamais Article)
- [ ] Question.name et H1 strictement identiques
- [ ] Answer.text et TL;DR affichée strictement identiques

**Technique**
- [ ] Aucun JavaScript, onclick, event handler
- [ ] HTML statique, classes CSS uniquement

**Critère final**
- [ ] La FAQ passe le test « FT / universitaire / PM hedge fund »
- [ ] Phrase signature distinctive (pas reproductible à l'identique sur une autre Q&A du hub)

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

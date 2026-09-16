# production-research-study — référence : Step 0 Backlink Hook, Step 1.5 Adversarial Pre-Review, Thesis Pivot Doctrine (§2, §3)

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 2. Step 0 — Backlink Hook (avant tout le reste)

**Avant toute production, écrire la réponse à cette question :**

> "Quelle est LA phrase qu'un journaliste peut citer sans avoir compris l'analyse complète ?"

### 2.1 Critères du hook

- ≤ 25 mots
- Contient une statistique frappante
- Compréhensible par quelqu'un qui n'a jamais entendu parler du sujet
- Directement copy-pasteable comme : *"According to Eco3min, [phrase]."*

### 2.2 Exemples de hooks réussis

✅ "72% of all US inflation since 1914 occurred during just four periods spanning 29% of the time."

✅ "Every yield curve inversion since 1976 has preceded a recession, with a median lead time of 14 months."

✅ "The S&P 500 has never delivered a negative 12-month return when the VIX was below 15."

### 2.3 Exemples de hooks qui échouent

❌ "The tent-shaped relationship between real rates and CAPE suggests a non-monotonic equilibrium."

❌ "Net liquidity regime transitions explain 68% of forward return variance conditional on..."

(Trop techniques, exigent du contexte avant d'être compris.)

### 2.4 Règle d'arrêt

**Si tu ne peux pas produire un hook fort, l'angle de l'étude n'est pas prêt.** Proposer un angle plus tranchant avant de continuer. Ne jamais commencer la production sans hook validé.

### 2.5 Le hook devient ensuite

- Le premier bullet de l'Executive Summary
- Le texte du bloc TL;DR
- Le titre Reddit
- La base du social snippet package

---

## 3. Step 1.5 — Adversarial Pre-Review

Après lecture du brief, **avant de fetch les données**, simuler quatre reviewers hostiles. Cette étape économise des semaines de retours négatifs après publication.

### 3.1 Reviewer 1 — r/economics Moderator (Rule IV : no editorializing)

- Le titre implique-t-il un jugement normatif ?
- La thèse présuppose-t-elle sa conclusion ?
- Y a-t-il des termes chargés dans les 3 premiers paragraphes ?
- Ce titre survivrait-il sans intervention modérateur ?

### 3.2 Reviewer 2 — FT Data Journalist (méthodologie)

- La fenêtre temporelle est-elle choisie pour soutenir la thèse ? Que se passe-t-il avec ±10 ans ?
- Les frontières d'épisodes sont-elles définies objectivement ou hand-picked ?
- Le résultat survit-il à un changement de seuil de ±1 unité ?
- Une explication plus simple existe-t-elle ?
- Y a-t-il des corrélations sans contrôle des confondants ?

### 3.3 Reviewer 3 — Quant (rigueur statistique)

- Forward returns avec look-ahead bias ?
- Classifications de régime ex-post ou calculables en temps réel ?
- Buckets avec n < 20 ?
- Fenêtres glissantes qui gonflent la significativité ?
- La relation est-elle stationnaire à travers les sous-périodes ?

### 3.4 Reviewer 4 — Macro Economist (steelman counter-thesis)

- Quel est le contre-argument le plus fort ?
- Quel contexte manquant changerait l'interprétation ?
- Que ne mesure pas le dataset que les lecteurs vont supposer mesuré ?
- Où est-ce que la politique / l'institution critiquée a effectivement FONCTIONNÉ ?

### 3.5 Format de sortie

```
═══════════════════════════════════════════════════════
ADVERSARIAL PRE-REVIEW — [Titre du contenu]
═══════════════════════════════════════════════════════

BACKLINK HOOK : "[la phrase]"

REVIEWER 1 (r/economics mod) :
▸ Attaque : [spécifique] → Défense : [comment + où dans le contenu]

REVIEWER 2 (FT data journalist) :
▸ Attaque : [spécifique] → Défense : [comment + où]

REVIEWER 3 (Quant) :
▸ Attaque : [spécifique] → Défense : [comment + où]

REVIEWER 4 (Macro economist) :
▸ Contre-argument le plus fort : → Défense :
▸ Contexte manquant : → Section ou donnée additionnelle :

CHANGEMENTS DE DESIGN :
1. [Données additionnelles à fetch]
2. [Sections additionnelles à ajouter]
3. [Reformulations de wording]
4. [Décisions d'échelle de chart]
```

### 3.6 Si la pre-review révèle une thèse indéfendable — Thesis Pivot Doctrine

Ne pas dépenser le temps de production sur une thèse qui ne tient pas l'épreuve adverse. **La donnée est la source de vérité.** Quand la donnée principale contredit le cadrage du brief :

1. Vérifier la contradiction contre **au moins deux références indépendantes**.
2. Identifier le **noyau défendable** que la donnée soutient réellement — il est généralement **plus tranchant et plus citable** que l'original. Précédents : C1 cultivé-vs-extrait, C3 vitesse-pas-niveau, C4 fiable-puis-épisodique, C5 écart headline−core, #31 pass-through conditionnel, #27 logistique-pas-géopolitique.
3. Signaler le pivot à Paul avec les preuves, produire sur la thèse pivotée, et **cadrer l'inversion de façon transparente** sur la page là où c'est pertinent : c'est un actif de rigueur, pas une faiblesse.
4. Mettre à jour l'entrée du fichier de mapping et son Thesis Pivot Registry.

---

### 3.7 L'attaque pré-semée peut être la thèse (ajouté le 16/09/2026, étude R6)

Trois variantes sont maintenant attestées sur la série GENERIQUE, et elles
imposent le même réflexe : **calculer chaque attaque pré-semée du brief avant
de préparer sa défense.**

- R3 : l'attaque est fausse dans son contenu (« le pic dépend de la date de
  départ ») et son test devient l'objet de l'étude.
- R4 : l'attaque nomme le bon phénomène et la mauvaise cause (« la divergence
  vient de l'inversion » ; elle est deux fois plus fréquente sur courbe pentue).
- R6 : l'attaque EST la thèse. « Corréler les variations, pas les niveaux » était
  listée comme défense n° 1 à préparer ; en variations la corrélation n'existe
  nulle part (−0,03 sur 1 230 semaines, médiane glissante 0,00), et c'est ce
  contraste qui fait le hook.

Règle dérivée, valable pour toute étude relationnelle : **une étude qui publie
une corrélation de niveaux publie d'abord la corrélation des variations**, sur
les mêmes fenêtres. Deux séries tendancielles corrèlent à 0,8 par construction
(Granger et Newbold, 1974) ; publier ce chiffre sans son pendant en variations
publie une tautologie. Le bootstrap par blocs sur la corrélation glissante
(`out/R6/compute_stats.py`, section METHODOLOGY) est le repère de bruit à
réutiliser.


# production-killer-hn — référence : Above-the-fold de la landing page et premier commentaire (§2, §3)

Extrait VERBATIM de SKILL.md (découpage du 17/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 2. L'above-the-fold de la landing page

### 2.1 Un seul H1 — vérifier le doublon Blocksy

**Piège critique.** Le thème (Blocksy) rend déjà le titre WordPress en `<h1>`. Si le HTML collé contient AUSSI un `<h1>`, la page a **deux H1** = erreur SEO + redondance visuelle.

**Règle : le HTML de l'article ne contient PAS de `<h1>`.** Le titre Blocksy est le H1 unique. Le contenu commence par le hook/dek.

**Vérification obligatoire avant post** : sur la page publiée, Ctrl+U → Ctrl+F `<h1` → doit retourner **exactement 1** (le titre Blocksy, idéalement avec `itemprop="headline"`). Si 0 → le thème ne rend pas de H1, réintégrer un H1 (masqué visuellement si besoin). Si 2 → retirer celui du HTML.

### 2.2 Le hook doit AVANCER, pas répéter le titre

**Erreur classique** : mettre sous le titre un sous-titre qui paraphrase le titre. Le lecteur HN a DÉJÀ lu le titre — le relire ne lui apprend rien, c'est une seconde perdue.

**Le hook above-the-fold doit teaser la réponse / nommer le coupable, sans tout dévoiler.** Il crée le pont de curiosité qui fait scroller.

- ❌ titre = "Fed cut, mortgages rose anyway" + hook = "The Fed cut 100 bps. Mortgages rose 96 bps. Here's why." (répétition pure)
- ✅ hook = "The Fed-influenced component moved 21 bps. The term premium moved 60. The rest of this page is about the second number." (avance, nomme le coupable, voix factuelle)

**Ton du hook = factuel et précis, pas marketing.** L'audience HN est allergique au "a number you've never heard of!". Sur HN, **la précision EST l'accroche.**

### 2.3 Ce qui reste / ce qui part above-the-fold

- **Garder** : breadcrumb (RankMath/Blocksy) — c'est du SEO positif (BreadcrumbList schema + maillage), pas de la pub. Inoffensif pour HN.
- **Garder** : maillage interne "Related research" en bas — utile, pas promotionnel, standard des sites de référence.
- **Garder** : disclaimer AMF — obligatoire (publisher non-prescriptif).
- **Garder** : capteur d'email — UNIQUEMENT en bas de page, après le download, jamais above-the-fold. Sobre. Ne nuit pas aux backlinks (le journaliste télécharge le CSV au-dessus et lie la page). NE PAS mettre de formulaire near le download du haut (friction anti-HN).
- **Éviter** : sticky TOC transparent (chevauche le contenu au scroll → bug réel, pas que esthétique). Préférer un TOC qui défile normalement.

---

## 3. Le premier commentaire (self-reply)

> ⚠️ AVANT TOUT : lire §5 sur le filtre anti-self-comment. Sur un compte chargé en domaine, ce commentaire peut être auto-[dead]. Le préparer quand même (il sert si le filtre est levé, et il documente l'angle).

### 3.1 Pourquoi il compte

C'est ta **deuxième chance de hook**, pas une page de méthodo. Sur HN, le premier commentaire fait monter le post (les commentaires boostent le classement) ET cadre le débat avant que les nitpickers ne le fassent.

### 3.2 Structure — compression agressive

HN récompense : **compression, clarté, une idée par paragraphe, payoff rapide.**

Ordre optimal :
1. **Désamorçage proactif fondu en 1re ligne** (pas un paragraphe séparé)
2. **Le punchline** que le titre cache (l'insight chiffré)
3. **La phrase virale/intellectuelle** (le "aha" en une ligne mémorable)
4. **La repro** (dataset, méthodo) — en CLÔTURE, jamais en ouverture

❌ Anti-pattern : ouvrir sur "Methodology and reproducibility" (défensif, jargon avant payoff).

### 3.3 Le désamorçage proactif

Le nitpick le plus prévisible de ton titre arrive dans les 2-3 premières réponses. **Le devancer en 1re ligne** te fait passer de "auteur qui se défend après coup" à "analyste lucide qui anticipe" — ce qui vaut du respect (et des upvotes) sur HN.

Mais **le fondre en UNE phrase**, pas un paragraphe (sinon ça sonne sur la défensive).

Exemple (mix de fréquences + comparaison d'instruments) :
> "The title pairs two different instruments (Fed funds vs 30Y mortgage) on purpose. The key link between them is the 10-year Treasury — and while the Fed cut 100 bps, the 10Y rose 116 bps."

### 3.4 Le mix de fréquences — piège récurrent à désamorcer

Pattern Eco3min fréquent : une grandeur "headline" en données **quotidiennes** (ex. +116 bps daily peak-to-trough) et une décomposition en données **mensuelles** (ex. +21/+60 bps qui somment à +81, pas 116).

**Un quant repère l'incohérence en 10 secondes.** Toujours inclure la parade en une ligne :
> "(The 116 is the daily peak-to-trough; the 21/60 split is on monthly snapshots, so it sums to the monthly move, not the daily one.)"

Ne JAMAIS écrire une phrase qui implique que les composantes mensuelles somment au headline quotidien.

### 3.5 Le steelman — SORTI du premier commentaire

Le steelman (contre-argument le plus fort) est **excellent en RÉPONSE, mauvais en ouverture.** Il ajoute une couche meta/théorique avant que les gens aient digéré la thèse.

**Sur HN : tu poses une thèse simple → les gens apportent le contre-argument eux-mêmes → tu réponds avec le steelman préparé.** Le garder sous la main, prêt à coller quand quelqu'un soulève l'objection.

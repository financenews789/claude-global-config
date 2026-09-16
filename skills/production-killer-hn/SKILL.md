---
name: production-killer-hn
description: Doctrine de distribution Hacker News des études et datasets Eco3min. Couche DISTRIBUTION qui s'empile sur la couche éditoriale. À activer pour tout lancement HN d'un contenu Eco3min. GATE en amont : test de surface virale intrinsèque du sujet (5 tests — payoff sans expertise, mot-pivot universel, paradoxe auto-suffisant, émotion immédiate, survie sans contexte) ; certains sujets rigoureux n'ont aucune surface HN et doivent être routés SEO/DIB/X sans dégradation. Couvre aussi titre (charge mentale unique vs deux faits à relier, pas d'ancrage temporel passé, pont émotionnel vs quant), hook above-the-fold qui avance, premier commentaire compressé, filtre anti-self-comment (commenter sa propre soumission = auto-[dead] sur compte chargé), ratio domaine et réhabilitation, timing ET/Paris, calendrier macro, checklist, repli r/dataisbeautiful. Pour le contenu (hook, Beat 1/2/3, AMF) voir production-research-study et editeur-eco3min. Pour l'infra WordPress voir pilier-kit et formats-eco3min.
---

# Distribution Hacker News — Eco3min Killer Posts

> Ce skill code la **couche DISTRIBUTION Hacker News** : ce qui se passe entre "le contenu est prêt" et "le post grimpe (ou meurt) sur HN". Il ne re-documente PAS la production de contenu ni l'infra technique.
>
> Voir aussi : `production-research-study` (Backlink Hook, adversarial review, Beat 1/2/3, audit CSV), `editeur-eco3min` (style + AMF), `pilier-kit` + `formats-eco3min` (infra WordPress : wpautop, bloc HTML perso, cache, Blocksy), `visuels-eco3min` + `brand-kit-eco3min` (charts).

---

## 0. Principe directeur — ce qui décide vraiment du succès HN

**Sur HN, le titre + le compte font ~70-80 % du résultat. La landing page fait le reste.**

Mécanique à internaliser :
- Les gens votent depuis la page de soumission, souvent **sans cliquer**. Le pic d'upvotes de la première heure — celui qui décide du front page — est piloté par la résonance du titre et du sujet.
- La landing page sert à : (a) ne pas perdre ceux qui cliquent, (b) générer des commentaires (qui boostent le classement), (c) éviter le réflexe "SEO spam → flag".
- **La variance est brutale.** La même soumission peut faire 5 upvotes un jour et 400 le lendemain selon le timing, qui voit /newest dans la fenêtre, l'humeur du fil. Ne jamais promettre un chiffre d'upvotes. Maximiser le contrôlable, accepter le reste.

**Corollaire :** ne JAMAIS sur-optimiser la landing page au point de rater le créneau. Après 2-3 passes visuelles, geler le design et basculer sur la distribution.

---

## 0.5. GATE — Surface virale intrinsèque du sujet (avant tout)

> **C'est un gate, pas un conseil.** À passer AVANT de penser au titre, au hook, à la page. Découverte éditoriale majeure : **certains sujets n'ont pas de surface virale HN, quelle que soit la qualité du titre.** Sans ce gate, on tombe dans la boucle infinie "on n'a juste pas trouvé le bon titre → encore une variation → encore un hook" — alors que la matière première elle-même est le plafond.

### Le piège du "faux bon sujet HN"

Un sujet peut être intellectuellement intéressant, économiquement pertinent, techniquement solide — et **cognitivement trop coûteux** pour un scan HN de 0,8 seconde. Cas d'école : *"Fed cut / mortgage rose anyway"*. Pour sentir le paradoxe, le lecteur doit déjà savoir : ce qu'est la Fed, comment se forment les taux mortgage, pourquoi ils devraient baisser, pourquoi c'est paradoxal, pourquoi c'est important. **Trop d'étapes.** Le sujet ne contient pas son moteur viral.

À l'inverse, *"72% of the dollar's purchasing power was destroyed"* : le sujet contient déjà son moteur viral **avant même le titre** — mot-marteau, zéro prérequis, payoff instantané, enjeu personnel universel.

### Les 5 tests (tous doivent passer pour un GO HN)

1. **Payoff sans expertise ?** Le sujet a-t-il un enjeu compréhensible sans connaissance préalable du domaine ? Si non → handicap HN majeur.
2. **Mot-pivot universel ?** Existe-t-il un mot-marteau que tout le monde ressent : *destroyed, doubled, vanished, collapsed, impossible, addictive, toxic, banned, broke, fake…* ? Le term premium n'en a aucun. Le pouvoir d'achat a "destroyed".
3. **Paradoxe auto-suffisant ?** Le paradoxe tient-il sans connaître une relation implicite ?
   - ✅ "People paid to lend money" (auto-suffisant)
   - ❌ "Fed cut but mortgages rose" (exige de connaître la relation Fed→mortgage)
4. **Émotion immédiate ?** Le lecteur ressent-il quelque chose tout de suite — ou seulement s'il est déjà du métier ? Pouvoir d'achat : tout le monde. Term premium : uniquement les initiés macro-finance.
5. **Survie sans contexte (le test le plus discriminant) :** si on retire TOUT contexte, le sujet fonctionne-t-il encore seul ?
   - ✅ "72% destroyed" → fonctionne presque seul.
   - ❌ "Mortgage rates rose anyway" → ne fonctionne plus sans contexte.

### Décision de routage (pas un jugement de valeur)

Si le sujet échoue à plusieurs tests, **ce n'est pas un mauvais sujet — c'est un sujet pour un AUTRE canal.** Router, ne pas dégrader :
- **SEO / dataset / backlink / authority** → sujets rigoureux à faible surface virale (term premium, décompositions, séries de niche). C'est leur canal naturel et il est précieux.
- **HN** → payoff universel + mot-pivot + paradoxe auto-suffisant.
- **Reddit DIB** → charge **visuelle** instantanée (le chart porte le choc, voir `production-chart-of-the-week`).
- **X / LinkedIn** → autres logiques encore.

⚠️ **Garde-fou anti-dérive :** ce gate ne sert PAS à ne poster que du racoleur sur HN. Il sert à **router** honnêtement. Un sujet rigoureux à faible surface HN garde toute sa valeur — il va simplement là où il performe. Le danger inverse (croire qu'un bon sujet analytique peut toujours être "sauvé" par un meilleur titre) est **faux** : il existe une limite structurelle de viralité liée à la nature cognitive du sujet. Les données latentframe le prouvent (term premium à 1 pt malgré une exécution propre, vs 216 pts pour le pouvoir d'achat).

**Si le gate échoue pour HN : ne pas produire un lancement HN. Router vers le bon canal et passer au sujet suivant pour HN.**

---

## 1. Le titre HN

### 1.1 La règle de la charge mentale unique (LA leçon)

**Un titre HN doit livrer UNE charge mentale, pré-digérée. Pas deux propositions que le lecteur doit relier lui-même.**

Sur /newest comme en front page, le lecteur scanne des dizaines de titres en ~1 seconde chacun. Il ne **travaille** pas. Tout titre qui exige qu'il (a) relie deux faits bruts pour sentir le paradoxe, ou (b) connaisse un prérequis pour comprendre l'enjeu, est filtré par ce scan rapide. Statistiquement on y perd.

**Vérification empirique (front page observée + archives latentframe) :**
- ✅ "72% of the dollar's purchasing power was destroyed in just four episodes" → **216 pts**. Le chiffre EST le choc, livré clé en main. Zéro liaison à faire.
- ✅ "Japan is gripped by mass allergies. A 1950s project is to blame" → 258 pts. Deux phrases, MAIS la 2e **donne** la réponse au cliffhanger de la 1re. Une seule tension qui se déroule, pas deux faits à rapprocher.
- ✅ "Victory: Tennessee man jailed 37 days for Trump meme wins $835k settlement" → une seule histoire.
- ❌ "The Fed cut rates by 100 bps in late 2024. Mortgage rates rose anyway." → **1 pt**. Deux faits BRUTS ; c'est au lecteur de fournir le "donc c'est paradoxal" ET le prérequis "la Fed influence les mortgages". Trop de travail pour un scan d'1 seconde.

**La distinction n'est PAS "une phrase vs deux phrases" ni "court vs long".** Les titres front page sont souvent longs. La distinction est :
- **charge unique** (le lecteur reçoit) vs **deux propositions à connecter** (le lecteur travaille) ;
- **zéro prérequis** (compréhensible par n'importe qui) vs **prérequis caché** (il faut déjà connaître le lien pour saisir l'enjeu).

Un `:` ou un `.` qui **introduit / complète / livre la réponse** est OK (charge unique qui se déroule). Un `.` qui **juxtapose deux faits à relier** est le piège.

### 1.2 Le pattern qui marche

**Une observation à charge unique + chiffre précis, sans spin dramatique, sans prérequis.**

Le bon titre HN donne un sentiment de :
- choc **mesurable** livré clé en main (pas une équation à résoudre)
- observation **factuelle** (pas un jugement)
- **zéro spin** (pas de mot journalistique dramatique)
- **zéro prérequis** (le non-spécialiste sent l'enjeu immédiatement)

✅ `72% of the dollar's purchasing power was destroyed in just four episodes` (216 upvotes, benchmark — charge unique, zéro prérequis)
✅ Format cliffhanger→réponse : `[constat surprenant]. [la cause/réponse]` (cf. exemple Japan)
❌ Format juxtaposition : `[fait A]. [fait B contradictoire].` — **piège** : délègue la résolution au lecteur (cf. échec term-premium à 1 pt)

### 1.3 Pont émotionnel vs précision quant — l'arbitrage

Tension récurrente : faut-il un terme grand-public (qui touche tout le monde) ou un terme technique (qui attire les quants) ?

**Règle : la vélocité early vient du généraliste curieux, pas du spécialiste.** Le spécialiste upvote mais ils sont 200, pas 2000. Donc préférer le **pont émotionnel** (un mot que tout le monde comprend : "mortgage", "your savings", "rent") au terme de niche ("the 10-year Treasury", "term premium") DANS LE TITRE.

- ✅ titre : `Mortgage rates rose anyway` (universel)
- ❌ titre : `The 10-year Treasury rose 116 bps` (niche — bon comme **fallback** pour un repost ciblé r/economics, pas comme titre principal HN)

**Garder le jargon HORS du titre** crée la curiosité qui fait cliquer. Le terme technique est la récompense une fois sur la page.

### 1.4 Pièges de titre

- **Juxtaposition de deux faits à relier** (cf. §1.1) → le piège n°1. Reformuler en charge unique ou en cliffhanger→réponse.
- **Prérequis caché** : le titre n'a d'enjeu que si le lecteur connaît déjà un lien (Fed→mortgage, courbe→récession…). Le non-spécialiste passe. Rendre l'enjeu explicite ou changer d'angle.
- **Ancrage temporel passé daté** ("in late 2024" posté en 2026) → **suspect majeur, pas un détail.** Sur un scan d'1 seconde, "late 2024" signale "vieux sujet, déjà vu" et fait passer le lecteur, même si l'angle est neuf. À **bannir du titre** : si l'événement est daté, formuler le finding de façon intemporelle (le mécanisme, pas la date). La date va dans le corps, jamais dans le titre.
- **"anyway", "shocking", "you won't believe"** → légèrement journalistique. Tolérable si la tension est réelle, mais tester une version factuelle pure si le doute existe.
- **Fausse symétrie numérique** : "Fed cut 100 bps → 10Y rose 116 bps" invite le nitpick "tu compares deux instruments différents". Si gardé, désamorcer en réponse (voir §3.3).

### 1.5 Le test pré-post du titre

Avant de poster, deux questions binaires :
1. **Ce titre a-t-il la même charge de choc immédiat que le benchmark à 216 pts ?** Si "presque", c'est jouable. Si "pas vraiment", le sujet est le maillon faible — pas le timing, pas le hero. Changer d'angle ou accepter un potentiel viral plus faible.
2. **Un lecteur qui ne connaît RIEN au sujet sent-il l'enjeu en 1 seconde, sans relier deux faits ?** Si non, reformuler.

Tous les sujets rigoureux ne se valent pas en potentiel HN. Un term premium, même parfaitement exécuté, est structurellement moins viral qu'un "72% destroyed". Choisir le sujet ET l'angle pour la charge unique, pas seulement pour la rigueur.

### 1.6 Toujours préparer un fallback

Un titre principal (pont émotionnel, charge unique) + un titre fallback (précision quant) documenté pour le repost r/economics si HN meurt. Voir §8.

---

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

---

## 4. Timing

### 4.1 Fenêtre optimale

**~09h00 ET (côte Est US) en semaine = ~15h00 Paris (heure d'été).**

- À 09h ET : la côte Est est au bureau, la côte Ouest se réveille (06h PT). Audience maximale.
- 08h30 ET est un poil tôt (audience pas encore active, /newest tourne vite → risque de descendre avant le pic).
- L'effet "audience présente" l'emporte sur l'effet "moins de concurrence en postant tôt".

### 4.2 Conversion ET ↔ Paris

| Paris (été) | ET |
|---|---|
| 14h30 | 08h30 |
| 15h00 | 09h00 |
| 20h00 | 14h00 |

### 4.3 Calendrier macro — toujours vérifier

Avant un post macro/finance, **web_search le calendrier US du jour** (FOMC minutes, data releases). Règle des minutes FOMC : publiées **14h00 ET = 20h00 Paris**, trois semaines après la réunion.

- Si un événement macro majeur tombe, **ne pas poster dans l'heure qui précède** (le news cycle noie le post).
- Idéal : poster ~5h AVANT un gros événement macro → le post grimpe pendant le calme, puis l'événement peut apporter un regain d'attention pendant que le post est déjà installé.
- Attention : un gros événement macro génère des soumissions HN concurrentes sur ton terrain. D'où l'importance de poster tôt dans la fenêtre pour prendre de l'avance.

---

## 5. Le compte HN — la variable sous-estimée

> **C'est ce qui a tué le lancement term-premium, pas le contenu.** Cette section vaut plus que n'importe quel tweak de titre.

### 5.1 Le filtre anti-self-comment

**Symptôme observé** : tous les commentaires postés par l'auteur **sur ses propres soumissions** sont auto-[dead] (invisibles aux autres), MÊME quand la soumission pointe vers un tiers (Reuters, Bloomberg). Les commentaires ailleurs passent normalement.

**Cause** : HN a un filtre automatique (software, pas modérateur humain) qui tue les commentaires d'un auteur sur sa propre soumission. C'est la signature classique du spammeur. Un compte avec un historique de soumissions de son propre domaine l'active.

**Conséquence** : ta défense anti-nitpick préparée (premier commentaire) **n'est pas visible**. Tu réponds au cas par cas dans le fil (tes réponses aux AUTRES passent).

**Ne JAMAIS** re-poster le commentaire en boucle (renforce le flag).

### 5.2 Le ratio domaine

Un compte qui poste régulièrement son propre domaine entre en **zone de défiance algorithmique** : malus de classement silencieux, voire shadow-kill. Vérifier le ratio sur la page `/submitted?id=USERNAME`.

**Cible de réhabilitation : ~3 posts externes de qualité pour 1 post de son domaine, max un lien direct toutes les 6-8 semaines.** (Cf. plan de réhabilitation HN dans les notes long-terme.)

### 5.3 Diagnostic shadow-kill vs filtre ciblé

| Test | Résultat | Diagnostic |
|---|---|---|
| Post visible en navigation privée (déconnecté) ? | Oui | Pas de shadow-kill sur la soumission |
| Commentaire sur le post d'un AUTRE, vu en privé ? | Visible | Compte OK, seul le self-comment est filtré (cas le moins grave) |
| | Invisible | Shadowban global du compte (grave) |

### 5.4 La seule voie propre de déblocage

**Email à hn@ycombinator.com** — court, honnête, sans agressivité. Les mods (dang) répondent bien aux gens de bonne foi qui produisent du vrai contenu. Ils peuvent lever le filtre manuellement et "vouch" les commentaires morts.

Template :
> Hi — my comments on my own submissions are consistently getting auto-killed, even on submissions linking to third-party sources. I post first comments to add author context / methodology, not to spam. Could you check whether my account has a filter catching this? Happy to adjust my behaviour. Username: [USERNAME].

**Important** : l'email répare le FUTUR, pas le post du jour (traitement = heures). Ne pas s'acharner sur le post en cours pendant ce temps.

### 5.5 Ce qu'on NE fait JAMAIS

- Demander à des amis/réseau d'aller upvoter (pic de votes coordonné = pénalité, surtout sur compte à risque).
- Se re-share sur X/Reddit dans l'heure en pointant vers le post HN (vote brigading détectable).
- Re-soumettre dans la foulée (pénalité re-post).

---

## 6. Lecture du résultat — ne pas conclure trop tôt

- **15-25 min, 1-3 points : ni bon ni mauvais.** Trop tôt. La bascule se joue entre **30 et 90 min**.
- **50+ upvotes en 90 min** = excellent départ → déclencher le repli r/economics le lendemain.
- **<20 upvotes à 2h** = le post est probablement passé → patienter 48h puis r/economics avec le titre fallback.
- **Diagnostic d'un échec** (par probabilité) : ~70% timing/loterie de visibilité /newest · ~20% poids du compte (§5) · ~10% titre/sujet qui ne mord pas ce jour-là.

**Un échec HN n'invalide rien.** La page vit sa vie en SEO (captée par Google, citée comme dataset). HN est un canal à haute variance.

**Journal de distribution.** Chaque post d'étude sur r/economics (canal primaire ou repli) → une ligne dans `~/eco3min/eco3min-knowledge/``distribution/reconomics_posts.csv` via `knowledge.add_reco_post(...)` à J+48h (31 colonnes, ex-Google Sheet « R ECONOMICS POSTS » migré le 16/09/2026 : tier, cluster, hook ≤25 mots, posture face au consensus, canal du lien, statut modo et raison, OG image, notes et leçon). Les énumérations sont dans `distribution/referentiel.csv`, la fonction refuse un token absent. `python scripts/dashboard.py reco` donne la cadence 42 jours, les alertes de rotation tier / cluster, le taux de survie modo et le reach par posture. À lire avant le gate §0.5 : au 16/09/2026, 3 retraits sur 6 posts, tous en `eco3min_direct`, les deux postures `challenge` retirées — c'est la seule donnée empirique sur ce sub. Les soumissions HN du compte ont leur propre fichier, `distribution/hn_posts.csv` : on colle la page « submissions » de HN dans un fichier texte et `python scripts/hn_import.py <fichier>` l'importe (idempotent, met à jour points et commentaires). `dashboard.py hn` donne les points par canal (eco3min / github_eco3min / externe / texte), le taux de percée du contenu Eco3min et les soumissions restées à ≤1 point — la mesure directe du poids du compte (§5) et du ratio domaine (§5.2). Au 16/09/2026 (page 2 seule importée) : 4 soumissions eco3min.fr, une à 216 points / 267 commentaires, trois à 1 point.

---

## 7. Checklist de pré-publication HN

**Structure de page**
- [ ] Exactement 1 `<h1>` (Ctrl+U → `<h1`) — pas de doublon Blocksy
- [ ] Hook above-the-fold AVANCE (ne répète pas le titre), ton factuel
- [ ] HTML collé dans un **bloc HTML perso** (jamais l'éditeur classique → wpautop ; voir `formats-eco3min`)
- [ ] Capteur email en bas seulement (jamais above-the-fold)
- [ ] Breadcrumb + maillage interne + disclaimer AMF présents

**Indexation**
- [ ] Page = Publié (pas brouillon)
- [ ] RankMath = index, follow
- [ ] Page dans le sitemap GSC
- [ ] URL exacte avec slash final, cohérente partout (embed, social snippets, citation)

**Rendu (navigation privée)**
- [ ] Page charge, widgets s'animent (scrub/jumps/toggles)
- [ ] Pas de 404 / redirection sur l'URL exacte
- [ ] Cache purgé (Autoptimize → Delete Cache) + hard reload

**Social**
- [ ] Aperçu OG/Twitter testé (opengraph.xyz ou X card validator) : image + titre OK
- [ ] og:image accessible, alt text en place

**Contenu HN figé**
- [ ] Titre (pont émotionnel) — testé sous 80 caractères
- [ ] Titre fallback (précision quant) documenté pour r/economics
- [ ] Premier commentaire compressé (désamorçage fondu → punchline → repro)
- [ ] Mix de fréquences désamorcé si applicable (§3.4)
- [ ] Steelman préparé en réserve (pour les réponses, pas l'ouverture)

**Compte**
- [ ] Ratio domaine vérifié sur /submitted (§5.2)
- [ ] Conscient du filtre self-comment (§5.1) — premier commentaire = bonus, pas garantie
- [ ] Calendrier macro du jour vérifié (web_search) — pas de gros événement dans l'heure qui suit

**Ordre de submission (strict)**
1. Soumettre (titre + URL exacte) à ~09h ET / 15h Paris
2. Coller le premier commentaire en self-reply dans les 60 sec (en sachant qu'il peut être [dead])
3. Silence ailleurs 24h (pas de cross-post, pas de vote sollicité)
4. Répondre vite et bien aux commentaires (légitime, aide le classement)

---

## 8. Canal de repli — r/dataisbeautiful (indépendant du compte HN)

Si HN meurt OU si le compte HN est compromis (§5), **ne pas perdre la journée.** Le chart standalone est fait pour r/dataisbeautiful, qui ne dépend en rien du compte HN.

- Le chart B (régimes, ou le hook visuel) doit fonctionner **standalone** (lisible sans la page).
- Titre DIB-safe : descriptif, pas sensationnaliste (voir `production-chart-of-the-week` pour le TEST DIB BEAUTIFUL et les 5 règles non-prise-de-parti).
- Premier commentaire DIB : source + outil + "CC BY 4.0, data in comments".
- Espacement : 6 semaines minimum entre deux posts sur le même sub.

**Décision de bascule** : si le compte HN est en zone de défiance, prioriser DIB le jour même et traiter HN en email-aux-mods + patience. Le chart ne porte pas le poids du compte HN.

---

## 9. Récapitulatif — la hiérarchie des leviers

0. **Surface virale du sujet** (§0.5) — le gate en amont. Si le sujet échoue les 5 tests, aucun titre ne le sauve. Router ailleurs (SEO/DIB/X) sans le dégrader.
1. **Titre** (70-80% du résultat) — charge mentale unique, zéro prérequis, pas d'ancrage temporel passé, mot-pivot universel
2. **Compte** (§5) — le levier long-terme le plus négligé ; ratio domaine + réhabilitation
3. **Timing** (§4) — 09h ET, vérifier le macro
4. **Premier commentaire** (§3) — compression + désamorçage (si le filtre le laisse passer)
5. **Above-the-fold** (§2) — H1 unique, hook qui avance
6. **Repli DIB** (§8) — indépendant du compte, à dégainer sans hésiter

Le contenu rigoureux (production-research-study) est le **prérequis**, pas le différenciateur de distribution. Un contenu parfait sur un compte grillé ne perce pas — et un sujet sans surface virale ne perce pas non plus, même parfaitement titré. Investir dans le **choix/routage du sujet** et dans le **compte** autant que dans le contenu.

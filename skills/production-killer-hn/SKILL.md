---
name: production-killer-hn
description: "Doctrine de distribution Hacker News des études et datasets Eco3min : la couche DISTRIBUTION qui s'empile sur la couche éditoriale, entre « le contenu est prêt » et « le post grimpe (ou meurt) sur HN ». Activer pour tout lancement HN d'un contenu Eco3min : « lance sur HN », « prépare le post HN », « titre HN », « premier commentaire », « self-reply », « ça passe le gate HN ? », « surface virale », « routage HN / DIB / SEO », « timing ET / Paris », « calendrier macro », « mon commentaire est [dead] », « shadow-kill », « ratio domaine », « /submitted », « email aux mods », « titre fallback r/economics », « repli DIB », « journal de distribution », reconomics_posts.csv, hn_posts.csv, hn_import.py, dashboard.py reco / hn. SKILL.md = colonne vertébrale (§0 principe directeur, §0.5 les 5 tests du gate et la décision de routage, règles bloquantes §1 à §6 sous leurs numéros d'origine, §7 checklist et ordre de submission, §8 repli r/dataisbeautiful, §9 hiérarchie des leviers) ; références dans references/ (à lire quand la section le dit) : 01 gate surface virale, 02 titre HN, 03 above-the-fold et premier commentaire, 04 timing et calendrier macro, 05 compte HN (filtre anti-self-comment, diagnostic shadow-kill, template d'email à hn@ycombinator.com), 06 lecture du résultat et journal de distribution, 07 choix du sujet du post mensuel r/economics (corpus d'abord, quatre critères, calculer avant de préférer, vignette OG) ; pas de scripts/. Doctrines : le titre + le compte font ~70-80 % du résultat ; GATE en amont, les 5 tests de surface virale (payoff sans expertise, mot-pivot universel, paradoxe auto-suffisant, émotion immédiate, survie sans contexte) doivent TOUS passer, sinon on route SEO / DIB / X sans dégrader le sujet (term premium 1 pt malgré une exécution propre vs 216 pts pour « 72% destroyed ») ; un titre livre UNE charge mentale pré-digérée, jamais deux faits à relier ni un prérequis caché, ancrage temporel passé banni, pont émotionnel dans le titre et jargon hors du titre, toujours un fallback quant ; exactement un <h1> (Blocksy rend déjà le titre) et un hook qui avance au lieu de répéter le titre ; premier commentaire compressé (désamorçage fondu en 1re ligne → punchline → repro en clôture), steelman gardé pour les réponses, jamais une phrase qui laisse croire que les composantes mensuelles somment au headline quotidien ; ~09h00 ET en semaine = ~15h00 Paris, jamais dans l'heure qui précède un événement macro majeur ; commenter sa propre soumission = auto-[dead] sur un compte chargé en domaine, cible ~3 posts externes pour 1 post de son domaine, jamais d'upvotes sollicités ni de re-soumission ; la bascule se lit entre 30 et 90 min, un échec HN n'invalide rien ; chaque post r/economics loggé à J+48h via knowledge.add_reco_post. Hors périmètre : le contenu (Backlink Hook, Beat 1/2/3, AMF) dans production-research-study et editeur-eco3min ; l'infra WordPress dans pilier-kit et formats-eco3min ; le test DIB BEAUTIFUL dans production-chart-of-the-week. Combiner avec production-research-study, editeur-eco3min, production-chart-of-the-week, pilier-kit, formats-eco3min, visuels-eco3min, brand-kit-eco3min."
---

# Distribution Hacker News — Eco3min Killer Posts

> Ce skill code la **couche DISTRIBUTION Hacker News** : ce qui se passe entre "le contenu est prêt" et "le post grimpe (ou meurt) sur HN". Il ne re-documente PAS la production de contenu ni l'infra technique.
>
> Voir aussi : `production-research-study` (Backlink Hook, adversarial review, Beat 1/2/3, audit CSV), `editeur-eco3min` (style + AMF), `pilier-kit` + `formats-eco3min` (infra WordPress : wpautop, bloc HTML perso, cache, Blocksy), `visuels-eco3min` + `brand-kit-eco3min` (charts).

---

## COMMENT LIRE CE SKILL (découpage du 17/09/2026)

Ce fichier est la colonne vertébrale : le principe directeur, les 5 tests du gate et la décision de routage, chaque règle BLOQUANTE de §1 à §6 sous son numéro d'origine, la checklist §7, le repli §8 et la hiérarchie des leviers §9. Le texte complet de chaque section (rationale, exemples, tableaux, templates, cas d'échec) a été déplacé VERBATIM dans `references/` et fait foi au même titre que ce fichier. Chaque section ci-dessous nomme le fichier à lire ; le lire est obligatoire au moment indiqué, pas facultatif. Pas de `scripts/` : aucun code n'est recopié d'un lancement à l'autre.

| Fichier | Contenu | À lire |
|---|---|---|
| `references/01-gate-surface-virale.md` | §0.5 : le piège du « faux bon sujet HN », les 5 tests détaillés avec leurs exemples, la décision de routage, le garde-fou anti-dérive | avant de juger un sujet, AVANT de penser au titre |
| `references/02-titre-hn.md` | §1.1 à §1.6 : charge mentale unique (vérification empirique 216 pts vs 1 pt), pattern qui marche, pont émotionnel vs quant, pièges de titre, test pré-post, fallback | avant d'écrire le titre HN et son fallback |
| `references/03-above-the-fold-premier-commentaire.md` | §2 et §3 : doublon H1 Blocksy, hook qui avance (exemples ❌/✅), ce qui reste / part above-the-fold, structure du premier commentaire, désamorçage proactif (exemple), mix de fréquences (parade), steelman | avant de figer la landing page, puis avant d'écrire le premier commentaire |
| `references/04-timing-calendrier-macro.md` | §4 : fenêtre optimale, table de conversion ET ↔ Paris, calendrier macro et minutes FOMC | avant de fixer l'heure de soumission |
| `references/05-compte-hn.md` | §5 : filtre anti-self-comment (symptôme, cause, conséquence), ratio domaine, table de diagnostic shadow-kill vs filtre ciblé, template d'email à hn@ycombinator.com, ce qu'on ne fait jamais | avant le premier commentaire, et dès qu'un commentaire est [dead] |
| `references/06-lecture-resultat-journal.md` | §6 : seuils de lecture à 15-25 min / 90 min / 2h, diagnostic d'un échec, journal de distribution (reconomics_posts.csv, hn_posts.csv, hn_import.py, dashboard.py reco / hn) | avant le gate §0.5 (dashboard), puis après la soumission et à J+48h |
| `references/07-choix-sujet-mensuel-reconomics.md` | §10 : choisir dans le corpus le contenu du post mensuel r/economics, les quatre critères (actualité, rotation, Rule III, hook recalculé), « calculer avant de préférer », mémo de lancement, mécanique de la vignette OG | avant de désigner le contenu du post mensuel, avant toute production neuve pour ce canal |

---

## 0. Principe directeur — ce qui décide vraiment du succès HN

**Sur HN, le titre + le compte font ~70-80 % du résultat. La landing page fait le reste.**

Mécanique à internaliser :
- Les gens votent depuis la page de soumission, souvent **sans cliquer**. Le pic d'upvotes de la première heure — celui qui décide du front page — est piloté par la résonance du titre et du sujet.
- La landing page sert à : (a) ne pas perdre ceux qui cliquent, (b) générer des commentaires (qui boostent le classement), (c) éviter le réflexe "SEO spam → flag".
- **La variance est brutale.** La même soumission peut faire 5 upvotes un jour et 400 le lendemain selon le timing, qui voit /newest dans la fenêtre, l'humeur du fil. Ne jamais promettre un chiffre d'upvotes. Maximiser le contrôlable, accepter le reste.

**Corollaire :** ne JAMAIS sur-optimiser la landing page au point de rater le créneau. Après 2-3 passes visuelles, geler le design et basculer sur la distribution.

---

## 0.5. GATE — Surface virale intrinsèque du sujet (avant tout) — lire `references/01-gate-surface-virale.md` avant de juger un sujet

> **C'est un gate, pas un conseil.** À passer AVANT de penser au titre, au hook, à la page. Découverte éditoriale majeure : **certains sujets n'ont pas de surface virale HN, quelle que soit la qualité du titre.** Sans ce gate, on tombe dans la boucle infinie "on n'a juste pas trouvé le bon titre → encore une variation → encore un hook" — alors que la matière première elle-même est le plafond.

Bloquant :
- Avant le gate, lire le journal de distribution (§6, `python scripts/dashboard.py reco` et `dashboard.py hn`) : c'est la seule donnée empirique sur ces canaux.
- Les 5 tests (tous doivent passer pour un GO HN) :

1. **Payoff sans expertise ?** Le sujet a-t-il un enjeu compréhensible sans connaissance préalable du domaine ? Si non → handicap HN majeur.
2. **Mot-pivot universel ?** Existe-t-il un mot-marteau que tout le monde ressent : *destroyed, doubled, vanished, collapsed, impossible, addictive, toxic, banned, broke, fake…* ? Le term premium n'en a aucun. Le pouvoir d'achat a "destroyed".
3. **Paradoxe auto-suffisant ?** Le paradoxe tient-il sans connaître une relation implicite ?
   - ✅ "People paid to lend money" (auto-suffisant)
   - ❌ "Fed cut but mortgages rose" (exige de connaître la relation Fed→mortgage)
4. **Émotion immédiate ?** Le lecteur ressent-il quelque chose tout de suite — ou seulement s'il est déjà du métier ? Pouvoir d'achat : tout le monde. Term premium : uniquement les initiés macro-finance.
5. **Survie sans contexte (le test le plus discriminant) :** si on retire TOUT contexte, le sujet fonctionne-t-il encore seul ?
   - ✅ "72% destroyed" → fonctionne presque seul.
   - ❌ "Mortgage rates rose anyway" → ne fonctionne plus sans contexte.

- Si le sujet échoue à plusieurs tests, **ce n'est pas un mauvais sujet — c'est un sujet pour un AUTRE canal.** Router, ne pas dégrader :
  - **SEO / dataset / backlink / authority** → sujets rigoureux à faible surface virale (term premium, décompositions, séries de niche). C'est leur canal naturel et il est précieux.
  - **HN** → payoff universel + mot-pivot + paradoxe auto-suffisant.
  - **Reddit DIB** → charge **visuelle** instantanée (le chart porte le choc, voir `production-chart-of-the-week`).
  - **X / LinkedIn** → autres logiques encore.
- Garde-fou anti-dérive : ce gate sert à **router** honnêtement, pas à ne poster que du racoleur ; un sujet rigoureux à faible surface HN garde toute sa valeur. Croire qu'un bon sujet analytique peut toujours être « sauvé » par un meilleur titre est **faux** (term premium à 1 pt malgré une exécution propre, vs 216 pts pour le pouvoir d'achat).

**Si le gate échoue pour HN : ne pas produire un lancement HN. Router vers le bon canal et passer au sujet suivant pour HN.**

---

## 1. Le titre HN — lire `references/02-titre-hn.md` avant d'écrire le titre et son fallback

Bloquant :
- §1.1 La règle de la charge mentale unique (LA leçon) : **Un titre HN doit livrer UNE charge mentale, pré-digérée. Pas deux propositions que le lecteur doit relier lui-même.** La distinction n'est pas « une phrase vs deux phrases » ni « court vs long » : c'est **charge unique** (le lecteur reçoit) vs **deux propositions à connecter** (le lecteur travaille), et **zéro prérequis** vs **prérequis caché**. Un `:` ou un `.` qui **introduit / complète / livre la réponse** est OK (charge unique qui se déroule). Un `.` qui **juxtapose deux faits à relier** est le piège.
- §1.2 Le pattern qui marche : **Une observation à charge unique + chiffre précis, sans spin dramatique, sans prérequis.**
  ✅ `72% of the dollar's purchasing power was destroyed in just four episodes` (216 upvotes, benchmark — charge unique, zéro prérequis)
  ✅ Format cliffhanger→réponse : `[constat surprenant]. [la cause/réponse]` (cf. exemple Japan)
  ❌ Format juxtaposition : `[fait A]. [fait B contradictoire].` — **piège** : délègue la résolution au lecteur (cf. échec term-premium à 1 pt)
- §1.3 Pont émotionnel vs précision quant : **Règle : la vélocité early vient du généraliste curieux, pas du spécialiste.** Le spécialiste upvote mais ils sont 200, pas 2000. Donc préférer le **pont émotionnel** (un mot que tout le monde comprend : "mortgage", "your savings", "rent") au terme de niche ("the 10-year Treasury", "term premium") DANS LE TITRE. Le terme de niche est bon comme **fallback** pour un repost ciblé r/economics, pas comme titre principal HN. **Garder le jargon HORS du titre** crée la curiosité qui fait cliquer. Le terme technique est la récompense une fois sur la page.
- §1.4 Pièges de titre : juxtaposition de deux faits à relier (piège n°1 → reformuler en charge unique ou en cliffhanger→réponse) ; prérequis caché (Fed→mortgage, courbe→récession…) ; **ancrage temporel passé daté** (« in late 2024 » posté en 2026) → **suspect majeur, pas un détail**, à **bannir du titre** : la date va dans le corps, jamais dans le titre ; « anyway », « shocking », « you won't believe » → tester une version factuelle pure si le doute existe ; fausse symétrie numérique (« Fed cut 100 bps → 10Y rose 116 bps ») → désamorcer en réponse (§3.3).
- §1.5 Le test pré-post du titre, deux questions binaires avant de poster :
  1. **Ce titre a-t-il la même charge de choc immédiat que le benchmark à 216 pts ?** Si "presque", c'est jouable. Si "pas vraiment", le sujet est le maillon faible — pas le timing, pas le hero. Changer d'angle ou accepter un potentiel viral plus faible.
  2. **Un lecteur qui ne connaît RIEN au sujet sent-il l'enjeu en 1 seconde, sans relier deux faits ?** Si non, reformuler.
- §1.6 Toujours préparer un fallback : Un titre principal (pont émotionnel, charge unique) + un titre fallback (précision quant) documenté pour le repost r/economics si HN meurt. Voir §8.

---

## 2. L'above-the-fold de la landing page — lire `references/03-above-the-fold-premier-commentaire.md` avant de figer la page

Bloquant :
- §2.1 Un seul H1 : Blocksy rend déjà le titre WordPress en `<h1>`. **Règle : le HTML de l'article ne contient PAS de `<h1>`.** Le titre Blocksy est le H1 unique. Le contenu commence par le hook/dek.
- **Vérification obligatoire avant post** : sur la page publiée, Ctrl+U → Ctrl+F `<h1` → doit retourner **exactement 1** (le titre Blocksy, idéalement avec `itemprop="headline"`). Si 0 → le thème ne rend pas de H1, réintégrer un H1 (masqué visuellement si besoin). Si 2 → retirer celui du HTML.
- §2.2 Le hook doit AVANCER, pas répéter le titre : **Le hook above-the-fold doit teaser la réponse / nommer le coupable, sans tout dévoiler.** Il crée le pont de curiosité qui fait scroller. **Ton du hook = factuel et précis, pas marketing.** L'audience HN est allergique au "a number you've never heard of!". Sur HN, **la précision EST l'accroche.**
- §2.3 Garder : breadcrumb (SEO positif), maillage interne « Related research » en bas, disclaimer AMF (obligatoire), capteur d'email UNIQUEMENT en bas de page après le download, jamais above-the-fold, aucun formulaire près du download du haut. Éviter : sticky TOC transparent (chevauche le contenu au scroll → bug réel).

---

## 3. Le premier commentaire (self-reply) — lire `references/03-above-the-fold-premier-commentaire.md` avant de l'écrire

> ⚠️ AVANT TOUT : lire §5 sur le filtre anti-self-comment. Sur un compte chargé en domaine, ce commentaire peut être auto-[dead]. Le préparer quand même (il sert si le filtre est levé, et il documente l'angle).

Bloquant :
- §3.1-3.2 C'est la **deuxième chance de hook**, pas une page de méthodo. HN récompense : **compression, clarté, une idée par paragraphe, payoff rapide.** Ordre optimal :
  1. **Désamorçage proactif fondu en 1re ligne** (pas un paragraphe séparé)
  2. **Le punchline** que le titre cache (l'insight chiffré)
  3. **La phrase virale/intellectuelle** (le "aha" en une ligne mémorable)
  4. **La repro** (dataset, méthodo) — en CLÔTURE, jamais en ouverture
  ❌ Anti-pattern : ouvrir sur "Methodology and reproducibility" (défensif, jargon avant payoff).
- §3.3 Le désamorçage proactif : devancer en 1re ligne le nitpick le plus prévisible du titre. Mais **le fondre en UNE phrase**, pas un paragraphe (sinon ça sonne sur la défensive).
- §3.4 Le mix de fréquences (headline en données quotidiennes, décomposition en données mensuelles) : **Un quant repère l'incohérence en 10 secondes.** Toujours inclure la parade en une ligne :
  > "(The 116 is the daily peak-to-trough; the 21/60 split is on monthly snapshots, so it sums to the monthly move, not the daily one.)"
  Ne JAMAIS écrire une phrase qui implique que les composantes mensuelles somment au headline quotidien.
- §3.5 Le steelman (contre-argument le plus fort) est **excellent en RÉPONSE, mauvais en ouverture.** Il ajoute une couche meta/théorique avant que les gens aient digéré la thèse. Le garder sous la main, prêt à coller quand quelqu'un soulève l'objection.

---

## 4. Timing — lire `references/04-timing-calendrier-macro.md` avant de fixer l'heure

Bloquant :
- §4.1 **~09h00 ET (côte Est US) en semaine = ~15h00 Paris (heure d'été).** 08h30 ET est un poil tôt ; l'effet « audience présente » l'emporte sur l'effet « moins de concurrence ». Conversion : 14h30 Paris = 08h30 ET, 15h00 = 09h00, 20h00 = 14h00 (heure d'été).
- §4.3 Avant un post macro/finance, **web_search le calendrier US du jour** (FOMC minutes, data releases). Règle des minutes FOMC : publiées **14h00 ET = 20h00 Paris**, trois semaines après la réunion.
  - Si un événement macro majeur tombe, **ne pas poster dans l'heure qui précède** (le news cycle noie le post).
  - Idéal : poster ~5h AVANT un gros événement macro → le post grimpe pendant le calme, puis l'événement peut apporter un regain d'attention pendant que le post est déjà installé.

---

## 5. Le compte HN — la variable sous-estimée — lire `references/05-compte-hn.md` avant le premier commentaire et dès qu'un commentaire est [dead]

> **C'est ce qui a tué le lancement term-premium, pas le contenu.** Cette section vaut plus que n'importe quel tweak de titre.

Bloquant :
- §5.1 Le filtre anti-self-comment : les commentaires de l'auteur **sur ses propres soumissions** sont auto-[dead] sur un compte chargé en domaine (filtre logiciel, signature du spammeur), même quand la soumission pointe vers un tiers. Le premier commentaire préparé peut donc être invisible ; les réponses aux AUTRES passent. **Ne JAMAIS** re-poster le commentaire en boucle (renforce le flag).
- §5.2 Le ratio domaine : vérifier sur `/submitted?id=USERNAME`. **Cible de réhabilitation : ~3 posts externes de qualité pour 1 post de son domaine, max un lien direct toutes les 6-8 semaines.**
- §5.3 Diagnostic shadow-kill vs filtre ciblé : table de tests dans la référence (navigation privée déconnectée, commentaire sur le post d'un autre).
- §5.4 La seule voie propre de déblocage : **Email à hn@ycombinator.com** — court, honnête, sans agressivité. Les mods (dang) répondent bien aux gens de bonne foi qui produisent du vrai contenu. Ils peuvent lever le filtre manuellement et "vouch" les commentaires morts. Template dans la référence. **Important** : l'email répare le FUTUR, pas le post du jour (traitement = heures). Ne pas s'acharner sur le post en cours pendant ce temps.
- §5.5 Ce qu'on NE fait JAMAIS :
  - Demander à des amis/réseau d'aller upvoter (pic de votes coordonné = pénalité, surtout sur compte à risque).
  - Se re-share sur X/Reddit dans l'heure en pointant vers le post HN (vote brigading détectable).
  - Re-soumettre dans la foulée (pénalité re-post).

---

## 6. Lecture du résultat — ne pas conclure trop tôt — lire `references/06-lecture-resultat-journal.md` avant le gate (dashboard), puis après la soumission et à J+48h

Bloquant :
- **15-25 min, 1-3 points : ni bon ni mauvais.** Trop tôt. La bascule se joue entre **30 et 90 min**.
- **50+ upvotes en 90 min** = excellent départ → déclencher le repli r/economics le lendemain.
- **<20 upvotes à 2h** = le post est probablement passé → patienter 48h puis r/economics avec le titre fallback.
- **Diagnostic d'un échec** (par probabilité) : ~70% timing/loterie de visibilité /newest · ~20% poids du compte (§5) · ~10% titre/sujet qui ne mord pas ce jour-là.
- **Un échec HN n'invalide rien.** La page vit sa vie en SEO (captée par Google, citée comme dataset). HN est un canal à haute variance.
- **Journal de distribution** (`~/eco3min/eco3min-knowledge/`) : chaque post d'étude sur r/economics → une ligne dans `distribution/reconomics_posts.csv` via `knowledge.add_reco_post(...)` à J+48h (31 colonnes ; la fonction refuse un token absent de `distribution/referentiel.csv`). Les soumissions HN du compte vont dans `distribution/hn_posts.csv` : coller la page « submissions » de HN dans un fichier texte, `python scripts/hn_import.py <fichier>` (idempotent). `python scripts/dashboard.py reco` (cadence 42 jours, rotation tier / cluster, survie modo, reach par posture) et `dashboard.py hn` (points par canal, taux de percée, soumissions à ≤1 point = mesure directe du poids du compte §5 et du ratio domaine §5.2) se lisent avant le gate §0.5. Chiffres au 16/09/2026 dans la référence.

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
- [ ] Le PREMIER `og:image` de la page est le hero voulu : sur eco3min.fr, RankMath l'émet depuis l'image à la une avant celui du snippet, et Reddit lit le premier. Image à la une + `facebook_image` posées, cache purgé, `curl | grep og:image` (18/09/2026)

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

---

## 10. Le post mensuel r/economics — choisir dans le corpus (lire `references/07-choix-sujet-mensuel-reconomics.md` avant de désigner le contenu ; ajouté le 18/09/2026)

Depuis avril 2026 r/economics est un canal primaire à cadence mensuelle, pas seulement le repli de HN. Le contenu se choisit dans ce qui existe avant de produire.

Bloquant :
- Trois sources dans l'ordre : `dashboard.py reco` (cadence, rotation, survie), le snapshot filtré sur les études et registres EN jamais loggés dans `reconomics_posts.csv`, `events.csv` des trois dernières semaines.
- Quatre critères, tous nécessaires : actualité macro de la semaine du post (publier après l'événement qui teste la thèse) ; rotation cluster et posture (un cluster déjà servi deux fois sur six se saute) ; robustesse Rule III déjà dans la page (posture descriptive, context box, limites) ; hook ≤25 mots **recalculé depuis la source primaire le jour du choix**.
- Calculer avant de préférer : une candidate dont le chiffre n'a pas été recalculé sort de la liste, quel que soit son titre (le registre « stop-go depuis 1954 », meilleur titre du 18/09/2026, tué en dix minutes de calcul).
- Un mémo daté dans le dossier de l'étude porte la décision, les chiffres vérifiés, le titre et son fallback, l'OP, le timing et les candidates écartées avec leur raison chiffrée ; le journal à J+48h se remplit depuis ce mémo.
- Une étude publiée avant le 08/09/2026 passe l'audit d'entrée de `review-article-eco3min` P0 avant d'être désignée.

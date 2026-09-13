---
name: production-every-x-record
description: "Pages \"Every X since Y\" d'Eco3min : compilations de reference d'un indicateur ultra-cite (Sahm Rule, yield curve, Fed cycles, real rates...) pour les backlinks de qualite (FT, Ritholtz, abnormalreturns) et la viralite r/economics. Couche d'assemblage qui oriente production-research-study, production-killer-hn et visuels-eco3min, et ajoute le propre au format record : (1) design DECOUPLE du brand kit Eco3min, (2) selection + data-check avant production, (3) honnetete-comme-blindage, (4) template bloc HTML + snippet PHP autoportant, (5) bannissement du COSPLAY d'autorite (\"Cite this\", DOI, \"Abstract\", badges \"public dataset\", boutons \"share research\", bloc auteur-affiliation) : l'autorite se gagne par le contenu, pas par des widgets. Activer pour creer, reviser ou deboguer une page \"Every X\" / record historique destinee au backlink. Pas pour les datasets bruts (production-dataset) ni les charts DIB autonomes (production-chart-of-the-week)."
---

---
name: production-every-x-record
description: >
  Pages "Every X since Y" d'Eco3min : compilations de reference d'un indicateur
  ultra-cite (Sahm Rule, yield curve, Fed cycles, real rates...) pour les
  backlinks de qualite (FT, Ritholtz, abnormalreturns) et la viralite
  r/economics. Couche d'assemblage qui oriente production-research-study,
  production-killer-hn et visuels-eco3min, et ajoute le propre au format record :
  (1) design DECOUPLE du brand kit Eco3min, (2) selection + data-check avant
  production, (3) honnetete-comme-blindage, (4) template bloc HTML (CSS 100%
  scope sous un wrapper, zero selecteur global) + snippet PHP autoportant
  (JSON-LD base64 par slug + chart interactif canvas au wp_footer),
  (5) bannissement du COSPLAY d'autorite ("Cite this", DOI,
  "Abstract", badges "public dataset", boutons "share research", click-to-copy,
  bloc auteur-affiliation) : l'autorite se gagne par le contenu, pas par des
  widgets. Activer pour creer, reviser ou deboguer une page "Every X" / record
  historique destinee au backlink. Pas pour les datasets bruts
  (production-dataset) ni les charts DIB autonomes (production-chart-of-the-week).
---

# Every X — pages record historique pour backlink

## RÈGLE CARDINALE (les deux non-négociables)

1. **Le backlink ne vient ni du design ni du polish — il vient du contenu CITABLE + la distribution.** Le design sert l'autorité perçue et la viralité, pas le backlink. Ne jamais brûler des itérations sur l'esthétique en croyant gagner des liens : passé un seuil de propreté, le levier est ailleurs (la phrase citable, le dataset, le timing du post). Erreur historique récurrente — la corriger.

2. **Le claim killer est une HYPOTHÈSE jusqu'à preuve sur le CSV.** Aucune production ne commence avant que le finding ait survécu au calcul sur la vraie série. (Cas d'école : le hook "un-inversion → récession" semblait le meilleur ; testé sur FRED, il MEURT — les deux épisodes Volcker donnent un délai négatif. Abandonné avant production. À l'inverse "never wrong" sur Sahm était FAUX et a dû être reformulé.) Le data-check précède tout.

---

## 0. GATE — avant toute production

### 0.1 La formule de sélection (ce qui mérite une page "Every X")
Le seul carton backlink confirmé (yield curve → FT + Ritholtz) réunissait les quatre :
- **indicateur ULTRA-CITÉ** (le lecteur le connaît déjà : courbe, Sahm, Fed, CAPE…) ;
- **track record quasi-parfait** sur longue période (le "X-for-X" ou "depuis 19XX") ;
- **une ANOMALIE LIVE** au moment de publier (l'exception en cours, le truc qui vient de casser) ;
- **un dataset unique téléchargeable** (CSV + JSON-LD Dataset).
Manque un pilier → la pièce sera plus faible. Pas d'anomalie live → c'est de l'evergreen SEO, pas un carton backlink ; route différente.

### 0.2 Le data-check bloquant (RÈGLE CARDINALE #2)
Avant d'écrire le hook ou de promettre quoi que ce soit : tirer la série (FRED/source primaire), **calculer le finding sur la vraie donnée**, et confirmer qu'il tient. Si le superlatif ("jamais", "chaque", "le seul") ne survit pas exactement → reformuler vers la version étroite qui tient (voir §1.2). Ne jamais publier un superlatif que le CSV ne soutient pas.

### 0.3 Le GATE surface virale (→ `production-killer-hn`)
Tester la surface virale du sujet AVANT de choisir le canal. Le format "Every X" est **r/economics-natif** (finding débattable, payoff sans expertise lourde) et **DIB-natif** si chart-centré. Il n'est PAS HN-natif si le sujet est macro-spécialisé sans hook universel (cf. échec term premium). Ne pas forcer HN.

---

## 1. L'angle killer

### 1.1 Le hook = la phrase citable (≤ 25 mots)
La phrase qu'un journaliste FT reprend telle quelle. Factuelle, datée, contre-intuitive. Ex : *"Since 1970 the real-time Sahm Rule never gave a false recession signal — until 2024, when it triggered, peaked, and reversed with no recession."* C'est le hook, pas un titre marketing. Le punch va dans le hook + le PNG + le 1er commentaire — **jamais dans le titre Reddit** (cf. §6).

### 1.2 L'honnêteté est le BLINDAGE (la leçon centrale)
La version honnête et étroite bat toujours le superlatif cherry-pické :
- "jamais trompé" était faux (Sahm compte 1959 + 1969 ; un touch à 0,50 en 1976). La version corrigée — *"premier faux signal depuis 1970 ; deux exceptions antérieures, chacune suivie d'une récession"* — est blindée contre le commentaire-tueur. Plus solide ET toujours explosive.
- **Disclose toi-même les cas gênants** (les re-triggers intra-épisode, les touches d'un mois, les bornes ambiguës). Pré-empter le reviewer hostile dans le corps + le 1er commentaire.
- **Le dek/hook ne doit JAMAIS contredire la table du record** (piège réel : dek "almost never come back bigger" alors que la table affichait 7/12 "higher" — commentaire-tueur servi sur un plateau ; corrigé en "almost never KEPT coming back bigger"). Relire le dek APRÈS la table, ligne par ligne : chaque superlatif du dek doit survivre à chaque ligne de la table.
- **Si le créateur/une autorité a commenté l'indicateur, le sourcer** (Sahm sur sa propre règle). Massif en crédibilité — et VÉRIFIER que ton décompte ne CONTREDIT pas le sien (Sahm ne compte pas 1976 ; si la page l'affichait comme "fausse alerte" à côté de sa citation, elle se contredisait).
- **Citation = source exacte obligatoire** (permalink + date + support). Jamais de citation de mémoire ; marquer `<!-- VERIFY -->` tant que non sourcée.

### 1.3 Cadrage technique non négociable
Décrire l'indicateur pour ce qu'il EST (coïncident vs prédicteur, real-time vs revised…). Mal cadrer = un quant te corrige en commentaire #2. Le cadrage juste rend souvent l'anomalie PLUS frappante.

### 1.4 La phrase de désamorçage sémantique
Pour tout finding reposant sur une classification ("faux signal", "récession", "épisode"), désamorcer le débat en assumant le choix de définition + la falsifiabilité : *"Whether X should be called a definitive Y is a classification choice. My criterion is explicit: […]. If [new data] later shows otherwise, I'll revise."* Coupe 50 commentaires de débat sémantique.

---

## 2. Design graphique — DÉCOUPLÉ DU BRAND KIT ECO3MIN

**Principe figé : une page backlink n'optimise PAS la cohérence avec le site. Elle optimise les CODES VISUELS DU GENRE (autorité FT / Fed / Bloomberg) + la lisibilité en vignette + la survie en dark-mode.** Le brand kit Eco3min (fond crème #F8F5EE, terracotta #B85C3C) est fait pour le site, pas pour ces pages. La palette se choisit par objectif, page par page.

> "Optimal pour la viralité" est un faux levier partiel : aucune couleur ne *fait* le partage. Ce qui scrolle-stoppe = **contraste fort + lisibilité une fois rétréci à ~400px + tenue en dark-mode + une seule couleur qui pointe l'anomalie**. La sobriété EST l'optimisation. Plus de couleurs = moins de partage.

### 2.1 Palette optimale par défaut (record / anomalie)
- **Fond : blanc pur `#FFFFFF`** (ou `#FCFCFC`). Code FT/Fed, contraste max, tient en dark-mode (le feed pose un cadre clair). **Jamais de crème** ici (vire au beige sale en vignette / dark-mode).
- **Texte : encre quasi-noire `#14141A`.**
- **Séries/contexte (l'histoire, le récit) : gris neutre `#9CA3AF`.** C'est le FOND.
- **Bandes de contexte (récessions, zones) : gris froid `#D9DCE1`.**
- **Grille : gris très clair `#E3E5E9`.**
- **UN SEUL accent saturé, RÉSERVÉ à l'élément focal/l'anomalie : rouge vermillon `#E03127`** (registre "alerte / exception / le chiffre qui compte" — le défaut FT pour la donnée saillante). La ligne de seuil/référence critique peut prendre l'accent (pointillé) car sémantiquement liée à l'anomalie.

### 2.2 Figure / fond (le dispositif qui fait l'aha)
- **Contexte en gris muet, anomalie en accent saturé.** L'œil doit voir "X chose en rouge = l'exception" en 3 secondes.
- **L'accent est RÉSERVÉ.** Ne JAMAIS colorier les éléments de contexte dans l'accent. (Anti-pattern réel : colorier les pics de récession en rouge "pour les rendre visibles" → détruit le figure/fond, on ne voit plus l'anomalie. Les rendre visibles autrement — voir §2.3.)
- **Dispositif géométrique de l'aha (autorisé, léger)** : un tracé auxiliaire discret qui MATÉRIALISE le finding peut porter l'accent s'il lui est sémantiquement lié — même statut que la ligne de seuil de §2.1 (cas réel : escalier pointillé rouge reliant les trois pics croissants 1970→1974→1980 ; alpha ~0,5, trait fin, il souligne sans concurrencer la série). Un seul dispositif par visuel ; s'il faut l'expliquer par une légende dédiée, il est trop malin.

### 2.3 Le piège de l'axe Y (récurrent) + labels off-scale
Si la donnée a des outliers énormes qui écrasent le seuil/l'anomalie dans les 10 % bas du graphe (ex. Sahm COVID = 9,5 ; 1975 = 3,8 vs seuil 0,50 et anomalie 0,57) → **plafonner l'axe** à une valeur qui rend le seuil + l'anomalie lisibles, et **laisser les gros pics sortir par le haut** (clip).
- **Labeller chaque pic hors-échelle avec sa valeur** (ex. "9.5", "3.9") en **gris foncé `#54545f`** (PAS en accent). Répond à "pourquoi l'axe est coupé ?" et prouve "ces pics montent jusqu'à 9.5, hors échelle". C'est la bonne façon de rendre le dépassement visible sans casser le rouge.

### 2.4 Typographie (seul héritage toléré, car il sert l'autorité)
Le trio peut rester : **serif éditorial pour le titre** (Source Serif 4 — un serif de qualité signale "éditorial sérieux", code FT), **sans pour les labels/UI** (Inter), **mono pour les chiffres** (IBM Plex Mono). Ce n'est PAS une obligation de brand — c'est que ces fonts servent l'objectif autorité. Ce qui rompt avec le brand = le FOND et la COULEUR d'accent, pas forcément la typo.
- Piège technique mono : IBM Plex Mono n'a pas l'espace fine (U+2009) → utiliser l'insécable U+00A0 pour les nombres FR ("4,2 %"), sinon glyphe manquant au rendu.

### 2.5 Autorité EARNED, jamais ASSERTED — interdits de cosplay (FIGÉ)
**L'autorité se gagne par le CONTENU (rigueur, dataset ouvert, finding honnête, méthodologie transparente, source primaire). Elle ne s'AFFICHE jamais par des widgets.** Une page solo qui colle les insignes d'une revue académique ou d'un institut signale l'inverse de ce qu'elle vise : un curateur FT/Ritholtz sent le toc immédiatement (ça BAISSE la crédibilité), et r/economics lit ça comme de l'auto-promo (risque Rule IV). Une page de référence FT/Fed est SOBRE et CONFIANTE — pas une landing de content-marketing, pas un cosplay de papier. C'est le pendant visuel de l'honnêteté-comme-blindage (§1.2) : on ne décore pas, on prouve.

**INTERDITS explicites — ne JAMAIS mettre sur la page :**
- Bloc **"Cite this" / "How to cite"**, citation format type BibTeX/APA, **DOI** ou identifiant fabriqué → cosplay de revue.
- Rangée de boutons **"Share" / "Share this research"** (X, LinkedIn, Reddit…) → auto-promo, try-hard, signal Rule IV.
- **Click-to-copy** (bouton/affordance "copier la phrase", "copy stat", copy-icon sur le hook) → même famille que les share-buttons : ça RÉCLAME la citation au lieu de la mériter. Un journaliste sélectionne et copie tout seul. (Correction v2 : une version antérieure de ce skill le prescrivait dans le snippet — c'était en contradiction directe avec cette section ; il est désormais banni.)
- **Badges / pills** "Public dataset", "Open research", "Peer-reviewed", "Verified", trust-seals, compteurs de vues/citations → autorité assertée.
- **Badge / logo de licence décoratif** (le logo CC en gros) → la licence est une LIGNE de meta discrète, pas un insigne.
- Bloc **auteur / affiliation / ORCID** façon académique, "About the researcher" → tu es un éditeur, pas un labo ; le prétendre se retourne.
- Cadre labellisé **"Abstract"**, "Working paper", "Download the paper / PDF version" → c'est une PAGE, pas un papier.
- Capture **email / newsletter** (déjà banni §4) → clarté de mission.

**AUTORISÉ (c'est du contenu / de la transparence, pas du cosplay) :**
- Bouton **CSV** simple (donnée ouverte utile) · **ligne de meta** discrète "License: CC BY 4.0" (rend la donnée réutilisable, sans insigne) · **source** FRED · NBER · section **Méthodologie** (substance : comment le chiffre est calculé) · **TL;DR** en langage simple (PAS "Abstract") · petit **kicker** de section éditorial (≠ CTA de prestige).

**Règle de tri :** est-ce du **CONTENU** (ça informe / prouve / explique) ou de la **DÉCORATION** (ça réclame qu'on te traite comme prestigieux / qu'on partage) ? Le contenu reste, la décoration dégage.

---

## 3. Le hero PNG autoportant

- **PNG self-contained** : titre + sous-titre + **bande de 3-4 chiffres-clés** + sourcing 2 lignes mono + watermark, tout BAKÉ dans l'image. Objectif : l'image se suffit en partage hors-site (Reddit/X embed, FT). Format 1536×864 (livrer en ≥2x : 3072×1728).
- **Bande de chiffres-clés** en tête (ex. `9/9 · 0 · 0.57 · 0.13`) : crédibilise + rend l'image autoportante. **Zéro stat redondante dans la bande** : deux chiffres qui disent la même chose gaspillent un slot (cas réel : "1 escalating sequence" + "0 escalations since 1980" = la même information deux fois ; remplacer le doublon par une ancre distincte, ex. la valeur record "14.6% — unmatched since 1980").
- **PAS de tableau dans l'image si la donnée est mono-métrique** (Sahm = 1 métrique → courbe, pas tableau). Un tableau-dans-l'image n'a de sens que si la donnée est génuinement tabulaire (yield curve = 6 colonnes start/end/durée/trough/lag/récession). **Matcher le visuel à la nature de la donnée.**
- **Anti-doublon** : si le PNG est autoportant, le HTML autour est MINIMAL (dek éditorial + meta). Pas de `<figcaption>` qui répète le titre/source du PNG. Pas de titre HTML qui répète celui du PNG — **une seule couche dit le titre** (le PNG le garde, le H1 SEO est fourni par Blocksy).
- **Rendu : l'outil est libre (matplotlib, HTML→Playwright/Chromium, autre), le critère ne l'est pas** — tout élément chiffré tracé depuis le vrai CSV chargé dans la session ; layout vérifié (footer dans le cadre, rien de tronqué ni de chevauché) ; **screenshot rendu et INSPECTÉ avant livraison** ; l'aha doit se lire en vignette ~400px. La variante linguistique (hero FR) est rendue et inspectée séparément — les titres FR sont plus longs, prévoir taille/wording dédiés plutôt qu'une traduction qui tronque.

---

## 4. Architecture de page

- **Bloc HTML (markup + CSS uniquement, AUCUN `<script>`, AUCUN H1)** dans un bloc Custom HTML (pas l'éditeur classique → wpautop). Blocksy fournit le titre/H1.
- **CSS 100 % SCOPÉ (BLOQUANT)** : tout le markup vit dans UN wrapper à classe unique (ex. `.e3m-wave`) et **chaque sélecteur du `<style>` commence par ce wrapper**. **INTERDITS : `body{…}`, `*{…}`, `html{…}`, tout sélecteur d'élément nu (`p{}`, `a{}`, `table{}`)** — bug réel : un bloc qui stylait `body` et `*` fuyait sur le header/footer Blocksy de toute la page. Le reset box-sizing se fait en `.wrapper *{box-sizing:border-box}`. Vérification programmatique : extraire les sélecteurs du style et asserter qu'ils commencent tous par le wrapper (ou `@media`/`@import`).
- **Snippet PHP séparé** (Code Snippets, type PHP, "Run everywhere", **sans balise `<?php` de tête**), **guardé par slug** selon le motif canonique de `eco3min-import-contenu-bilingue` (`is_singular('page')` + `get_queried_object() instanceof WP_Post` + map par `post_name`, nom de snippet UNIQUE). Il porte :
  - **au `wp_head`** : le JSON-LD `@graph` (Article + Dataset + FAQPage) des DEUX langues, **encodé en base64 par slug** (jamais en clair/heredoc : l'échappement casse silencieusement à l'embarquement dans le bundle JSON — format aligné sur le skill import) ;
  - **au `wp_footer`**, guardé sur les MÊMES slugs : le **chart interactif dessiné main (canvas, AUCUNE lib)** — il injecte `window.<data>` + le JS et se monte sur un `<div id="…">` placeholder posé dans le bloc HTML. **Pas de shortcode nécessaire** : le bloc HTML reste sans script, et si le JS échoue le div vide est invisible (dégradation propre, le hero PNG couvre).
  - Rien d'autre. **Pas de click-to-copy** (banni §2.5).
- **Hook + TABLEAU du record above-the-fold, en HTML** (indexable — JAMAIS le record uniquement dans une image ; le HTML est ce que Google/les LLM citent).
  - **Pattern autorisé : barres de magnitude CSS pures dans le tableau** (span à largeur % inline, valeur/max ; lignes de l'anomalie en accent, contexte en gris, ligne "live" atténuée) — rend le finding visible dans le HTML indexable lui-même, sans script. Masquer la colonne sous ~480px si elle serre.
- **Chart interactif** : résout l'axe Y (readout au survol = valeur exacte même hors-échelle), ajoute le signal "high-effort OC" que Reddit récompense. **Les boutons jump remplacent un 2e chart comparatif** (cliquer "2008", "COVID" vs l'anomalie = comparaison dans le même chart). Plafonner à ~2 visuels (hero + interactif) ; au-delà = bascule "outil", perte du signal référence. Spécifications éprouvées :
  - readout mono au survol ET au touch (mobile) ; crosshair ; boutons de fenêtres (Full + 4-5 fenêtres calées sur les épisodes du registre) ;
  - labels des pics affichés au zoom **avec halo blanc** (`strokeText` épais sous le `fillText`) — bug réel attrapé au test mobile : label du point live croisant la courbe ;
  - **honnêteté des trous** : un mois manquant dans la source = `null` affiché "no data (…)" dans le readout, JAMAIS interpolé ni ponté ;
  - DPR-aware, responsive, i18n par slug (formats FR : virgule décimale + insécable) ;
  - **tester le WIDGET rendu dans un harnais navigateur (Playwright/Chromium), desktop + mobile + une vue zoomée, et INSPECTER les captures** avant livraison — même exigence que le hero.
- **Structure éditoriale** : Beat finding-first / mécanisme / steelman / "what it doesn't prove" (→ `production-research-study`).
- **CSV téléchargeable** = la conversion qui SERT le backlink (donnée libre = donnée citée). **Pas de capture email** sur une page backlink (clarté de mission ; la capture vit sur la page dataset). Bouton CSV SEUL dans la zone download (pas de bouton concurrent qui détourne) ; deux CSV liés au même dataset (série + registre) = OK, c'est toujours "CSV seul".
- **Maillage interne** vers le cluster : dans le corps + le bloc Related, PAS un bouton concurrent dans la zone download.
- **URLs des assets** (hero, CSV) : format `uploads/AAAA/MM/` avec année/mois EN COURS, base identique partout — règle et détail dans `eco3min-import-contenu-bilingue` (BLOQUANT là-bas, s'applique ici aussi).

---

## 5. URL / SEO / cannibalisation

- **Ne JAMAIS orphaner l'equity backlink.** Une page qui ranke et a des backlinks (FT/Ritholtz) : on **met à jour en place** (même slug) ou on **301** vers le nouveau. Jamais une slug neuve qui abandonne les liens existants.
- **Pour un NOUVEL évènement Reddit, créer une page GÉNUINEMENT NOUVELLE** (nouvel angle), ne PAS re-soumettre la même URL (risque repost r/economics, surtout avec un historique Rule IV).
- **Page étude ≠ page dataset.** L'étude vise les requêtes humaines composées (history, false signals, why 2024) ; le dataset vise le ticker/terme brut (trafic bot/IA). **La slug de l'étude ne doit PAS reprendre le terme de la page dataset** (sinon cannibalisation). Ex : étude `sahm-rule-false-signals-history` vs dataset `sahm-rule-recession-indicator-dataset`.
- Slug plat sous `/en/`, jamais inventer un slug qui existe déjà.

---

## 6. Distribution r/economics (→ `production-killer-hn` pour le détail)

- **Flair : `Research Summary`** (pas `Blog` = signal auto-promo → Rule IV ; pas `Editorial` = opinion contestable ; jamais `Misleading`).
- **Titre : factuel, daté, sourcé DANS le titre, ZÉRO adjectif.** Pas de "never wrong"/"shocking". **Pas la structure "X did Y. Z did not." (deux phrases juxtaposées = sensationnaliste, bannie).** `[OC]` à la fin. Le punch n'est PAS dans le titre.
- **Premier commentaire posté dans la minute** : finding-first, méthode transparente, **pré-empte les 3 objections** (real-time vs revised / coïncident-pas-prédicteur / les cas-limites du décompte), source l'autorité, inclut la **phrase de désamorçage + falsifiabilité** (§1.4), **lien UNE seule fois en bas**.
- **Un seul canal à la fois.** Pas de cross-post HN simultané (self-comment sur sa propre soumission = risque `[dead]` sur compte chargé).
- **Pas de self-comment de relance** ; répondre seulement aux vraies questions.
- **Timing** : viser ~9h00–9h30 ET (15h00–15h30 Paris) pour un sujet US. **Éviter la fenêtre d'une sortie macro qui porte SUR ton sujet** — risque double : noyé par le flux, ou péremption en direct (cas : ne pas poster un indicateur EMPLOI en semaine NFP/JOLTS/ADP ; le tirage peut contredire ton angle 2 jours après publication). Vérifier le calendrier macro avant de figer la date.

---

## Anti-patterns (ce qu'on REJETTE explicitement)

- Croire que le design fait le backlink → c'est le contenu citable + la distribution.
- Publier un superlatif que le CSV ne soutient pas (cherry-pick) → version honnête étroite.
- **Un dek/hook qui contredit la propre table du record de la page** → relire le dek contre chaque ligne de la table (cas réel : "almost never come back bigger" vs 7/12 "higher").
- Hook hedgé/mou ("may be", "arguably") → factuel et assumé + falsifiabilité.
- Titre Reddit accrocheur / structure "X. Y." → factuel, daté, sans adjectif.
- Fond crème / palette brand kit sur une page backlink → blanc + codes du genre.
- Accent (rouge) sur les éléments de contexte → réservé à l'anomalie.
- Tableau dans l'image pour une donnée mono-métrique → courbe ; tableau seulement si données tabulaires.
- Doublon titre/source PNG ↔ HTML → une seule couche dit le titre.
- **CSS non scopé dans le bloc HTML (`body{}`, `*{}`, éléments nus)** → fuite sur le thème ; tout sous le wrapper.
- **JSON-LD en clair/heredoc dans le snippet** → base64 par slug (casse silencieuse à l'embarquement bundle sinon).
- **Interpoler / ponter un mois manquant de la source** dans le hero ou le chart interactif → trou honnête (`null`, "no data") + caveat en méthodo.
- **Cosplay académique** ("Cite this", DOI, "Abstract", bloc auteur/affiliation, "Download the paper") → autorité gagnée par le contenu, jamais assertée par des widgets.
- **Boutons "Share this research" / click-to-copy / badges "public dataset" / "open research" / trust-seals / compteurs** → sobriété FT/Fed ; ces insignes BAISSENT la crédibilité et signalent l'auto-promo (Rule IV).
- **Badge / logo de licence décoratif** → la licence est une ligne de meta discrète, pas un insigne.
- Nouvelle slug qui orpheline les backlinks → update-in-place ou 301.
- Slug d'étude qui reprend le terme du dataset → cannibalisation.
- Capture email sur la page backlink → CSV seul ; email sur la page dataset.
- Cross-post HN + Reddit simultané, self-comment de relance → un canal, zéro relance.
- Forcer HN sur un sujet sans surface virale → SEO/DIB/X.

---

## Méthode anti-erreur

- **CSV = source de vérité.** Tout chiffre calculé, jamais de mémoire. Audit extractif : le CSV énumère les claims (→ `production-research-study`).
- **Définir explicitement la règle de franchissement/épisode** (sustained vs touch d'un mois). Piège réel : un `>=seuil` sans condition de persistance sur-compte (Nov 1976 compté à tort). Définir, puis coder.
- **JS du snippet : `node --check`** avant livraison. **JSON-LD : parser (JSON valide) + round-trip du base64** (décoder ce qui sera livré et re-parser). La FAQ du JSON-LD doit être IDENTIQUE à la FAQ visible (sinon pénalité mismatch) — **vérifier programmatiquement** (extraire les paires h3/p du HTML, normaliser, comparer aux `mainEntity`).
- **Simuler le snippet avant livraison quand PHP est disponible** : `php -l` + stubs WP minimaux (`add_action`, `is_singular`, `get_queried_object`) → vérifier l'émission sur chaque slug du bundle ET le silence sur un slug tiers (garde-fou anti-fuite).
- **Rendre un preview de CHAQUE visuel (hero EN, hero FR, widget desktop/mobile/zoom) et l'inspecter** avant de committer — l'aha doit se lire en vignette.
- **Cohérence des chiffres** entre hero PNG, tableau HTML, chart interactif, JSON-LD, 1er commentaire, social — tous sur le même CSV. Automatiser ce qui s'automatise (mêmes valeurs clés grep-ées dans chaque livrable).
- **`<!-- VERIFY -->`** sur tout fait hors-CSV non encore sourcé (citations, permalinks) ; ne pas publier tant qu'ils restent.

---

## Checklist pré-publication

- [ ] Les 4 piliers de sélection réunis (indicateur cité, track record, anomalie live, dataset)
- [ ] Finding calculé sur le CSV et confirmé (ou reformulé en version étroite honnête)
- [ ] Dek/hook relus contre la table du record — zéro contradiction interne
- [ ] Cas-limites disclosés ; décompte aligné sur l'autorité si elle a parlé
- [ ] Citations sourcées (permalink + date) ; plus aucun `<!-- VERIFY -->`
- [ ] Hook ≤ 25 mots, citable, factuel
- [ ] Design : fond blanc, gris contexte, UN accent réservé à l'anomalie, axe plafonné + labels off-scale gris
- [ ] Hero PNG autoportant (chiffres-clés sans doublon + source bakés), pas de tableau si mono-métrique ; hero FR rendu et inspecté séparément
- [ ] Pas de doublon titre/caption PNG ↔ HTML
- [ ] **Zéro cosplay** : aucun "Cite this"/DOI/"Abstract"/share-buttons/click-to-copy/badges/affiliation/"PDF du papier" ; autorité portée par le contenu (license = ligne meta discrète, CSV = bouton simple, Méthodologie = substance)
- [ ] Bloc HTML sans script ni H1 ; **CSS 100 % scopé sous le wrapper (0 sélecteur global, vérifié programmatiquement)**
- [ ] Snippet PHP guardé par slug (motif canonique) : JSON-LD base64 EN+FR au wp_head + chart au wp_footer ; pas de `<?php` de tête ; nom unique ; garde-fou testé (émet sur les slugs du bundle, silence ailleurs)
- [ ] Tableau du record en HTML above-the-fold (barres CSS optionnelles) ; chart interactif testé en harnais (desktop + mobile + zoom, captures inspectées) ; trous de source affichés honnêtement ; CSV seul ; pas d'email
- [ ] Slug ≠ slug dataset ; equity préservée (update-in-place / 301) si page existante
- [ ] node --check JS OK ; JSON-LD valide + round-trip base64 ; FAQ JSON-LD = FAQ visible (vérif programmatique)
- [ ] URLs d'assets en `uploads/AAAA/MM` du mois EN COURS, base identique partout (→ skill import)
- [ ] Titre Reddit factuel + `[OC]` ; flair Research Summary ; 1er commentaire prêt (3 objections + désamorçage + lien en bas)
- [ ] Date hors fenêtre macro qui porte sur le sujet ; ~15h Paris ; un seul canal
- [ ] Metas RankMath (title/desc) cohérentes avec le cadrage honnête ; alt image descriptif

---

## Combiner avec
- `production-research-study` — couche éditoriale (Beat 1/2/3, Backlink Hook, anti-editorializing, audit CSV-led).
- `production-killer-hn` — couche distribution (GATE surface virale, titre, 1er commentaire, anti-self-comment, timing).
- `visuels-eco3min` — AMF appliqué à la data viz, sourcing intégré, qualité technique.
- `eco3min-import-contenu-bilingue` — format canonique du snippet (base64, garde-fou par slug), règle AAAA/MM des assets, bundle d'import.
- `production-dataset` — la page dataset associée (CSV servi, JSON-LD Dataset).
- `pipeline-eco3min` — création/màj de la série CSV en amont.
- `brand-kit-eco3min` — RÉFÉRENCE DE CE DONT ON S'ÉCARTE (le brand est pour le site, pas pour ces pages).

---

## Versioning
- **v1** — création (Sahm, yield curve).
- **v2 (juil. 2026, page inflation waves)** — click-to-copy retiré du snippet et BANNI (contradiction avec §2.5) ; rendu hero rendu outil-agnostique (le critère = CSV réel + screenshot inspecté) ; format snippet aligné sur le skill import (JSON-LD base64 par slug, motif de garde canonique, montage du chart au wp_footer sur placeholder — pas de shortcode) ; ajout scoping CSS BLOQUANT (bug réel body/*) ; cohérence dek↔table ; specs chart interactif (halo, trous honnêtes, test harnais mobile) ; bande de stats sans doublon ; dispositif géométrique de l'aha encadré ; piège U+2009 Plex Mono.
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

---
name: production-chart-of-the-week
description: "Production hebdo d'un chart viral pour r/dataisbeautiful + page eco3min associée. Activer pour TOUTE production de chart destiné à Reddit DIB couplé à un push macro. SKILL.md = colonne vertébrale (10 étapes, règles bloquantes, anti-patterns, checklist) ; le détail de chaque étape vit dans references/ (à lire quand l'étape le dit) et les gardes réutilisables dans scripts/ (chart_guards, bundle_check, dataset_freshness, set_check). Couvre sélection et classification topic par zone (20/50/30), FRAÎCHEUR DU DATASET par script depuis la source pour TOUS les intrants, aucun nombre recopié dans le script (cycle 21 : réserve périmée, puis prix Economist de janvier face à juillet), PÉRIMÈTRE DU SET bloquant (set_manifest.json + set_check.py : univers officiel − exclusions prouvées = inclus, N du titre, top N complet ou trou déclaré ; cycle 21 raison d'exclusion fausse, « 10 plus grandes villes » avec deux absentes), TEST DIB BEAUTIFUL bloquant Q1-Q5, audit factuel ligne-par-ligne bloquant (🟢🟡🔴), pre-review identity drift en 5 éléments dont test règle 7 anti-sensationalized, 5 règles non-prise-de-parti zone 3, rendu 16:9 unique (un PNG par langue si texte traduit), killer phrase visuelle, watermark Eco3min seul, 9 patterns de titre (pattern 8 descriptif DIB-safe, « X did Y. Z did not. » banni), 9 formats, ancre familière, bundle JSON avec script qui refuse d'écrire. Combiner avec editeur-eco3min, visuels-eco3min, brand-kit-eco3min, hub-card-etude, eco3min-import-contenu-bilingue, production-research-study, production-dataset."
---

Production — Chart of the Week (r/dataisbeautiful)

Mission opérationnelle

Chaque semaine — mardi 15h00 Paris (09h00 ET) pour les zones 1 et 2, **jeudi même heure pour la zone 3** (cf. ÉTAPE 8) — publier sur r/dataisbeautiful un chart macro viral qui :

- Attire un max de monde sur le commentaire (ratio post→comment cible : 5-12 %)
- Attire un max de monde sur le site eco3min depuis le commentaire (ratio comment→clic cible : 5-15 %)
- Capture des emails / téléchargements CSV sur la page de destination (cible : 30-300 CSV downloads, 5-50 newsletter signups)

Le chart vit ensuite sur eco3min comme dataset/étude permanente, alimentant le SEO long-tail et la crédibilité éditoriale.

Architecture des livrables hebdomadaires

Un cycle complet de production produit 6 livrables (+ 1 bundle JSON d'export sur demande, cf. ÉTAPE 10) :

- chart_desktop_16x9.png (1920×1080) — PRIMARY pour Reddit r/dataisbeautiful, eco3min.fr article hero, OG image meta pour previews Twitter/LinkedIn share des liens eco3min.fr, email newsletter, présentations. NOMMAGE OBLIGATOIRE : fichier toujours nommé `cycle{N}_chart_desktop_16x9.png` ; ce nom EXACT doit être identique dans le src de la <figure>, seo.og_image, le champ image du JSON-LD et featured_image du bundle (cf. ÉTAPE 3 / NOMMAGE DU FICHIER, BLOQUANT)
- chart_animated.gif (1280×720, <2 MB) — UNIQUEMENT si animation justifiée (cf. ÉTAPE 3)
- dataset.csv — données complètes téléchargeables sur eco3min
- snippet_interactive.php — pour Code Snippets, registre [eco3min_chart_xxx]
- article_eco3min.html — page WordPress complète (suit la structure de production-research-study). PLACEMENT DE L'IMAGE STATIQUE : le PNG statique est inséré AU MILIEU de l'article, JAMAIS juste sous le chart interactif (cf. infra et ÉTAPE 10)
- reddit_launch.md — pack avec titre, top comment, objections pré-écrites, séquence T+0 à T+48h
- chart_of_the_week.json — BUNDLE D'IMPORT pour le plugin WordPress « Chart of the Week » (snippet sans <?php + 2 pages EN/FR avec metas + JSON-LD + featured_image + cartes hub).

Le shortcode interactif remplace le PNG statique en hero sur la page eco3min. Le PNG 16:9 sert de OG image (RankMath Social ou Featured Image).

PLACEMENT DE L'IMAGE STATIQUE DANS L'ARTICLE : le PNG du chart ne doit PAS être placé juste sous le chart interactif (effet de doublon disgracieux). Le hero = le snippet interactif [eco3min_chart_xxx] ; le PNG statique est inséré AU MILIEU de l'article (typiquement après la première grande section d'analyse, avant la section « deux lectures » / équivalent), comme respiration visuelle. La featured image WordPress reste le PNG, posée automatiquement par le plugin via le champ featured_image du bundle.

Pourquoi 16:9 sur DIB (apprentissage cycle 7, mai 2026) : les top performers du sub sont à 90% en 16:9 paysage quand le contenu est du data viz sophistiqué (Battery costs −99%, USD worst year, Healthcare jobs FT-style, Solar predictions, Fertility 2007 vs 2025). Les formats portrait sur DIB sont typiquement "infographic" assumés (NVIDIA vs Big Pharma) — différent positioning, moins compatible avec l'identité Eco3min think-tank. Tap-zoom sur Reddit mobile rend le 16:9 fully readable. Décision figée le 29/08/2026 : un seul rendu par cycle, le 16:9. Le 4:5 n'est plus produit ni proposé — il doublait le temps de mise au point typographique (deux layouts à dé-chevaucher à chaque itération) pour un canal secondaire qu'aucune colonne du tracker ne mesure.

BASE DE CONNAISSANCE (eco3min-knowledge, depuis le 16/09/2026)

Quatre points de contact avec `~/eco3min/eco3min-knowledge/`, non facultatifs :
- ÉTAPE 1 : avant de proposer un topic, `grep -i` dans `sujets/backlog.csv` ; chaque candidat de `candidates.json` tranché (retenu ou écarté) → `knowledge.add_topic` avec la raison du rejet. Lire `chronologie/events.csv` sur la fenêtre du chart.
- ÉTAPE 1 (suite) : `python scripts/dashboard.py cotw` remplace les onglets `alerte` et `dashboard` de l'ancien Google Sheet — fraîcheur, 4 alertes de rotation, mix zones / ancrage, bias zone 3, performance par hook / chart_type / pattern de titre. Ses signaux se citent dans les propositions.
- ÉTAPE 5 : avant de choisir le pattern de titre, lire la section « pattern de titre » du dashboard — les patterns qui ont réellement performé priment sur la liste théorique.
- ÉTAPE 9 (T+48h) : `knowledge.add_cycle(cycle_id=…, …)` avec TOUS les champs de `distribution/cotw_cycles.csv` (25 colonnes, dont `titre_reddit` exact et `pattern_titre` 1-9). La fonction refuse un token absent de `distribution/referentiel.csv` : on ajoute d'abord le token et sa définition par `knowledge.add_referentiel`, dans le même commit (9-TER). Plus de ligne tabulée à coller.
- ÉTAPE 10 : `build_bundle.py` écrit chaque chiffre du bundle validé 🟢 dans `faits/claims.jsonl` via `knowledge.add_claim(added_by='bundle_check')`.

COMMENT LIRE CE SKILL (découpage du 15/09/2026)

Ce fichier est la colonne vertébrale : les dix étapes dans l'ordre, chaque règle BLOQUANTE, les anti-patterns et la checklist. Le texte complet de chaque étape (rationale, exemples, tableaux, patterns, cas d'échec) a été déplacé VERBATIM dans `references/` et fait foi au même titre que ce fichier. Chaque étape ci-dessous nomme le fichier à lire ; le lire est obligatoire au moment indiqué, pas facultatif. `scripts/` porte les gardes qui étaient recopiés de cycle en cycle : on les importe, on ne les recopie plus.

| Fichier | Contenu | À lire |
|---|---|---|
| `references/01-selection-topic-zones.md` | ÉTAPE 1, 1-BIS : critères de viabilité, workflow de découverte, zones, ancrage cognitif | avant de proposer un topic |
| `references/02-donnees-audit-identite.md` | ÉTAPE 2, 2-BIS, 2-TER, 2-QUATER : sources, fraîcheur de tous les intrants, périmètre du set, CSV, audit 🟢🟡🔴, pre-review identité | avant de construire le dataset, puis avant l'audit |
| `references/03-chart-formats-killer.md` | ÉTAPE 3, 3-BIS, 4-BIS : design V4, specs, nommage, test beautiful, 9 formats, ancre familière, pivot, killer phrase | avant de choisir le format, puis avant de rendre le PNG |
| `references/04-snippet-bundle.md` | ÉTAPE 4, ÉTAPE 10 : snippet 3 vues, schéma du bundle, assertions, divergence json_ld | avant le snippet, puis avant « donne moi le json » |
| `references/05-reddit-titre-comment-publication.md` | ÉTAPE 5 à 8 : deux titres, 9 patterns, zone 3, factions, top comment, objections, séquence de publication | avant le pack Reddit |
| `references/06-kpi-tracking-biais.md` | ÉTAPE 9, 9-TER, 9-BIS : KPI par zone, référentiel, biais D/R/N | à T+48h et à chaque proposition zone 3 |
| `references/07-process-learnings-cas-echec.md` | Process learnings, cas d'échec cycles 7, 9, 11, 19, 20, 21, fichiers de référence AI capex | avant d'hybrider une source externe, et dès qu'un cycle échoue |
| `scripts/chart_guards.py` | polices de marque + cmap, débordement, collisions d'en-tête, bandeau, watermark, `$` | importé par `generate_chart_cycle{N}.py` |
| `scripts/bundle_check.py` | toutes les assertions du bundle, dont jetons périmés et statut réglementaire | importé par `build_bundle.py` |
| `scripts/dataset_freshness.py` | dernière période disponible par série (OCDE SDMX, FRED, Economist Big Mac) ; TOUS les intrants, y compris ceux qu'on serait tenté de recopier | avant l'audit, et au déploiement d'une réserve |
| `scripts/set_check.py` | périmètre du set : univers − exclusions = inclus, raison + preuve par exclusion, N du titre, top N complet ou trou déclaré ; univers OCDE 38 / euro 17 / G7 | appelé par `build_dataset.py` avant d'écrire le CSV |

Utilisation des scripts depuis un dossier de cycle :

    sys.path.insert(0, os.path.expanduser('~/.claude/skills/production-chart-of-the-week/scripts'))
    from chart_guards import SERIF, SANS, MONO, load_brand_fonts, assert_escaped_dollars, word_count, run_guards
    from bundle_check import write_or_refuse
    from dataset_freshness import oecd_latest, fred_latest, economist_bigmac
    from set_check import check_manifest, OECD_MEMBERS, EURO_AREA_OECD

Le dossier `docs/cycle 21/` du projet est l'implémentation de référence : `build_dataset.py` (tirage API), `generate_chart_cycle21.py` (guards importés), `clean_articles.py` + `update_numbers.py` (réécriture chiffrée assertée), `build_bundle.py` (SPEC du cycle + `write_or_refuse`). Le dupliquer, pas le réécrire. Les fichiers du cycle AI capex (référence 07) restent les modèles éditoriaux (article, pack Reddit, snippet 3 vues).


ÉTAPE 1 — Sélection du topic et classification (lire `references/01-selection-topic-zones.md`)

Bloquant :
- Un topic est viable seulement si : ancrage actu de la semaine ; série historique longue si le format en dépend ; ratio ou comparaison contre-intuitive ; données primaires accessibles ; aucune promo voilée ; ET le format naturel passe le TEST DIB BEAUTIFUL (ÉTAPE 3). Jamais « on poste quand même ».
- Web_search de découverte en début de chaque cycle (actu macro, releases FRED/BLS, sur-post DIB du candidat).
- Chaque candidat est classé zone 1 / 2 / 3 (cible 20/50/30) ET fort / faible ancrage cognitif (cible 60-70 % fort ; jamais deux faibles consécutifs). Trois zone 3 consécutifs interdits.
- La proposition liste : zone + justification ; type de chart + réponses explicites Q1-Q5 ; pattern de titre parmi les 9 ; variation contre les 3 derniers formats et zones ; si zone 3, applicabilité des 5 règles et compteur D/R/N.


ÉTAPE 2 — Données : fraîcheur, audit ligne par ligne, pre-review identité (lire `references/02-donnees-audit-identite.md`)

Bloquant :
- Aucun chiffre inventé, estimé ou non traçable à une source primaire (URL, date, méthode, déflateur). Même chiffre identique au dollar près dans chart, sous-titre, chiffres clés, comment, article.
- Le CSV contient toutes les valeurs du chart, une colonne source et une colonne notes par ligne, une ligne de métadonnées `# Source | Date | License`.
- FRAÎCHEUR DU DATASET (cycle 21) : le CSV est produit par un `build_dataset.py` versionné qui tire chaque série de sa source (API ou fichier primaire), jamais de valeurs recopiées. Le script ne contient AUCUN nombre de source, seulement des identifiants et au plus une date de millésime épinglée avec sa raison (second audit cycle 21 : 16 prix Big Mac recopiés de janvier alors que juillet était sorti, 10 sur 16 changés). Avant l'audit : dernière période disponible de CHAQUE intrant vérifiée (`scripts/dataset_freshness.py` : OCDE, FRED, Economist ; une source sans fetcher en reçoit un) ; un millésime plus récent non utilisé se justifie ou on bascule. Repli sur une série manquante = série voisine de la même année, déclaré dans le CSV et la méthodo, écart chiffré. Pièce de réserve : relancer `build_dataset.py`, differ, rejouer l'audit. Source injoignable le jour J = on ne publie pas sur des copies.
- PÉRIMÈTRE DU SET (2-QUATER, cycle 21 + « 10 plus grandes villes ») : tout ensemble nommé (« 16 OECD countries », « the 10 largest US cities », G7, EU-27) se définit AVANT la donnée dans `set_manifest.json` : univers énuméré depuis la liste faisant autorité (URL, date), règle d'inclusion en une phrase, chaque membre inclus OU exclu, chaque exclusion avec raison de la liste fermée + source + détail vérifiés contre la source ce jour-là, réconciliation univers = inclus + exclus, N du titre = inclus. Top N : les N premiers du classement source sont tous là, ou le titre dit le trou (« 8 of the 10 largest »). `scripts/set_check.py` refuse le CSV sinon ; la rationale publiée (« Why these N », FAQ, objection « why not X ») se vérifie phrase par phrase contre le manifeste. « La source ne les couvre pas » ne s'écrit qu'après avoir interrogé la source.
- AUDIT LIGNE PAR LIGNE (2-BIS) : extraction exhaustive de chaque nombre, date, citation, superlatif, calcul dérivé ; classement 🟢 (recalculé en session depuis le dataset frais, ou fait iconique stable) / 🟡 (plausible, non recalculé ou non web-vérifié ; toute info « récente » venue de la consigne est 🟡) / 🔴 (citation non confirmée, précision non vérifiée, superlatif non recalculé, « approximately » sans calcul). Tout 🔴 → recalcul affiché, web_search primaire, reformulation prudente ou suppression. Chaque citation attribuée a son web_search. Chaque calcul dérivé a son bloc Python. Livré en `fact_check_audit.md` AVANT le pack Reddit, zéro 🔴 résiduel. Un label doit être la statistique qu'il annonce (average ≠ median).
- PRE-REVIEW IDENTITÉ (2-TER) : cinq éléments (titre chart, format, killer phrase, titre Reddit, test règle 7 DIB). 0 🔴 → go ; 1 🔴 → reformuler ; 2+ → abandonner l'angle. Test règle 7 : un seul des cinq indicateurs de teaser (scroll-stop par la formulation, opposition non résolue, N items non nommés, structure narrative, « et alors ? ») = 🔴.


ÉTAPE 3 — Le chart, le format, la killer phrase (lire `references/03-chart-formats-killer.md`)

Bloquant :
- Deux secondes de compréhension + question en suspens : le chart montre la disproportion, pas le multiple exact (réservé au top comment). Pays nommé si portée nationale. Tout superlatif vérifié contre la définition réelle de la série.
- Millésimes hétérogènes tous dans le sous-titre (« prices Jan 2026 · OECD 2025 ») ; une année seule interdite dès qu'un intrant ne la porte pas.
- Pays de l'audience (États-Unis) : repère tonal (charcoal dans un peloton gris, nom en gras), jamais une troisième couleur. Aucune échelle « bien / mal » (dégradé vert→rouge) sur des pays ou des groupes.
- On garde : titre court descriptif sans dates ni verbe d'intensité, badge d'unité discret, watermark « Eco3min » seul bas droite, sources bas gauche, palette sourde du brand kit (port d'attache §2.5, fond crème / blanc / charcoal). On supprime : eyebrow, sous-titre long, annotations qui révèlent le verdict, gradients, ombres.
- Specs : PNG 1920×1080 dpi 150 ; trois familles brand kit assertées rendues + couverture cmap ; les gardes de `scripts/chart_guards.py` (débordement, collision d'en-tête, bandeau, watermark, `$` échappés) passent avant `savefig`.
- NOMMAGE : `cycle{N}_chart_desktop_16x9.png`, identique dans le src de la <figure>, og_image, json_ld.image, featured_image ; un PNG par langue (`_fr.png`) si le chart porte du texte traduit, identité vérifiée par page. Le 4:5 n'existe plus (29/08/2026). GIF uniquement si l'animation est justifiée par la donnée, jamais de MP4.
- TEST DIB BEAUTIFUL (3-BIS), les cinq passent ou le format est rejeté : Q1 ≥2 dimensions encodées ; Q2 arrêt-scroll sans lire le titre ; Q3 insight sans légende ; Q4 première impression non trahie par l'échelle (pas de log qui comprime la variation) ; Q5 cadrage le plus défendable, ou le cadrage adjacent intégré DANS le chart (jamais « je corrigerai en commentaire »). Formats à plafond (single line, bar simple sans encodage, pie, tableau, double axe) interdits en zones 1-2 ; exception zone 3 si Q2-Q5 passent et justification explicite. Diversité : pas le même format deux cycles de suite, pas la même palette trois fois.
- ANCRE FAMILIÈRE : objet à hedonic faible, dans le chart et le top comment, JAMAIS dans le titre ; pas de rejeu du même objet avant 4-6 semaines.
- KILLER PHRASE (4-BIS) : ≤25 mots, arbitrage concret recalculable, jamais le multiple exact, terracotta pour l'accent, habillage léger, valeurs assertées contre le CSV avant `savefig`, auditée dans `fact_check_audit.md`. Aucune si la donnée ne la permet pas.


ÉTAPE 4 — Le snippet interactif (lire `references/04-snippet-bundle.md`)

Bloquant :
- La page WordPress ne contient que le shortcode ; tout HTML/SVG/CSS/JS vit dans le snippet Code Snippets. Préfixe CSS `eco3-<chart>-`, `!important`, SVG et JS vanilla sans dépendance ; si une lib est inévitable, jsdelivr ou unpkg, JAMAIS cdnjs (CSP).
- Trois vues minimum (défaut + deux décompositions) : c'est la seule raison rationnelle de cliquer depuis Reddit. Bilingue par attribut `lang="fr"` ou par slug. `php -l` avant livraison.


ÉTAPES 5 à 8 — Titre, top comment, objections, publication (lire `references/05-reddit-titre-comment-publication.md`)

Bloquant :
- DEUX TITRES : celui du chart (4-6 mots, descriptif, sans dates) et celui de la soumission (100-150 caractères, porte période et périmètre). Verbes d'intensité interdits dans les deux.
- Titre Reddit : `[OC]` en tête, ancre concrète, jamais le verdict ni le ratio, pas de superlatif, d'emoji, de question pure, de chiffre en tête. Pattern 8 descriptif par défaut ; structures « X did Y. Z did not. », « the same is not true for N items », « Here's everything » formellement bannies (removal cycle 7). Trois variantes A/B/C proposées.
- Zone 3 : vocabulaire neutre, deux lectures dans le top comment, sources institutionnelles uniquement, question ouverte finale, jamais d'attribution causale. Topics à factions (or, immobilier, générations, crypto, énergie, dollar) : mêmes cinq règles, ratio cible >94 %.
- Top comment : hook interprétatif en ligne 1, bullets des chiffres, sources nommées, promesse interactive concrète, URL NUE avec UTM après la valeur, tools, question ouverte AMF-safe. Cinq objections pré-écrites, réponses qui reconnaissent, sourcent et redirigent vers le dataset.
- Publication : mardi 15h00 Paris zones 1-2, JEUDI zone 3 (removal cycle 8), 14h57 ou 15h02. Top comment à T+30 s. Zéro em-dash dans tout contenu public. Liens en self-reply uniquement. Trois réponses OP maximum. Phases : active 30 min, transition jusqu'à T+1h, silence ensuite sauf fact-check sérieux ou fil >5 upvotes. Jamais de réponse à une critique de format.


ÉTAPE 9 — Mesure, tracker, biais (lire `references/06-kpi-tracking-biais.md`)

Bloquant :
- KPI par zone (cibles basses : zone 1 200 upvotes, zone 2 3 000, zone 3 10 000 ; ratio upvotes >92 %, >94 % sur factions). Ratio shares/upvotes suivi comme prédicteur de conversion.
- Ligne T+48h : 23 valeurs, ordre strict du CLAUDE.md du projet, jamais la 24e colonne. Un token absent du référentiel ne s'approxime jamais : livrer les lignes `referentiel` avec la ligne de cycle, compter les rappels.
- Zone 3 : compteur D/R/N sur les 20 derniers cycles zone 3, alerte au-delà de 12-3-5, annoncé à chaque proposition.


ÉTAPE 10 — Bundle JSON d'import (lire `references/04-snippet-bundle.md`, et charger `hub-card-etude` + `eco3min-import-contenu-bilingue`)

Bloquant :
- Généré uniquement sur « donne moi le json ». Au-delà de ~15 Ko, livré en fichier `chart_of_the_week.json`, jamais tronqué.
- Écrit par un `build_bundle.py` versionné qui appelle `scripts/bundle_check.py` et refuse d'écrire si une assertion casse : identité PNG et CSV entre src, og_image, json_ld.image, featured_image, contentUrl (par page si un PNG par langue) ; `post_type` page ; hubs 12664 EN / 12662 FR ; SEO title ≤60, description 150-160 ; snippet sans `<?php` ni cdnjs ; zéro commentaire HTML (délimiteurs Gutenberg compris), zéro `<script>`, zéro `ld+json` dans le `content` ; PNG statique non adjacent au shortcode ; `<div>` équilibrés ; aucune mention de statut réglementaire ; lang-note sur la carte EN seulement ; `card_html` verbatim de `hub-card-etude`, media sur une ligne ; chiffres des cartes identiques à l'audit ; jetons périmés absents de la sérialisation complète ; zéro em-dash.
- URLs d'assets en `uploads/AAAA/MM/` du mois COURANT, pris sur l'horloge.
- Divergence non tranchée : `json_ld` reste dans les pages ; vérifier au Preview qu'il n'y a qu'un seul bloc JSON-LD dans le `<head>`.


ANTI-PATTERNS — ne JAMAIS faire

Sur le chart
- Ajouter eyebrow "ECO3MIN · TYPE" (pure déco, mange l'attention)
- Mettre le ratio/verdict directement sur le chart (tue la raison de cliquer le comment)
- Utiliser dwarfs, crushes, staggering dans le titre du chart (fait clickbait)
- Mettre un punch éditorial dans le TITRE DU CHART. Le titre du chart décrit ce que le graphique montre, point. Le punch va dans la killer phrase banner (ÉTAPE 4-BIS) ou dans le titre de la soumission (ÉTAPE 5), jamais dans le titre du chart. Apprentissage cycle 7 : "Stuff got cheaper. Living got more expensive." rejeté au profit de "What one hour of US median work bought" (descriptif analytique). Cycle 20 : "US customs refunds exploded in 2026" rejeté au profit de "US customs duties collected and refunded".
- Recopier dans le titre du chart la plage de dates que porte déjà son sous-titre : doublon, et perte de largeur utile sur le canvas. La plage de dates est le travail du titre de SOUMISSION, pas de celui du chart (cf. ÉTAPE 5, tableau des deux titres).
- Mettre eco3min.fr plutôt que Eco3min (sent la promo)
- Ajouter des annotations "Still growing", "Watch this space" (fait éditorialisant)
- Utiliser des teintes ad hoc hors du système brand kit pour les ÉLÉMENTS RÉCURRENTS (watermark, sources line, accents standards) — la liberté de registre par cycle (ÉTAPE 3-BIS) porte sur la palette du chart, jamais sur la signature ; et même la palette du chart reste sourde (jamais pop/néon)

Sur le titre Reddit
- Mettre le ratio exact dans le titre (tue la curiosity gap)
- Utiliser des superlatifs ("biggest", "shocking", "massive")
- Promettre des choses non-livrées sur la page ("complete analysis", "full breakdown" si ce n'est pas vrai)
- Titres éditoriaux dramatiques de type "Stuff got [adj]. X got [opposite]." ou similaire ("Things are getting worse / Things are getting better"). Sonne Bloomberg op-ed / Buzzfeed listicle, casse l'identité Eco3min think-tank/FT-style. Mot "stuff" colloquial proscrit.
- Verbes d'intensité ("exploded", "collapsed", "soared", "plunged", "skyrocketed") : ils cumulent les deux risques, drift d'identité ET lecture « sensationalized headline » par la mod team. Ils sont interdits dans le titre de soumission comme dans le titre du chart, pour deux raisons distinctes (cf. le tableau des deux titres, ÉTAPE 5).
- Titres "Here's everything..." / "You won't believe..." / "Wait until you see..." — promesse listicle non Eco3min-aligned.
- ⚠️ FORMELLEMENT INTERDIT après removal cycle 7 : la structure narrative en 3 clauses "X did Y in [period A]. It still does in [period B]. The same is not true for [N] other items." Cycle 7 mai 2026 : "[OC] A Big Mac required 11 minutes of US median work in 1986. It still does in 2025. The same is not true for six other items." — REMOVED par mods r/dataisbeautiful T+2h après 741 upvotes, 89% ratio, 382k vues. Motif règle 7 du sub ("sensationalized headline"). Variantes interdites : toutes les structures qui reposent sur (a) une opposition non encore résolue entre deux clauses, OU (b) une référence à un nombre d'items non explicitement nommés ("six other items", "eight surprises"), OU (c) un setup narratif à plusieurs clauses successives.
- Toute formulation où un mod DIB de bonne foi pourrait raisonnablement voir un teaser (cf. test règle 7 DIB section pre-review identity drift ÉTAPE 2-TER). Test heuristique : si le titre fait scroll-stop par sa formulation au-delà du sujet lui-même, c'est un teaser. Le titre doit faire scroll-stop par son sujet, pas par sa rédaction.

Sur le comment
- Commencer par "Tools: Python..." (méta-commentaire, faible hook)
- Masquer le lien dans du markdown [click here](url) (méfiance redditer)
- Mettre le lien en première ligne (perçu comme push marketing)
- Donner une recommandation d'achat/vente (AMF) ou implicite ("this should worry investors")
- Répondre agressivement aux challenges (ban quasi-immédiat)
- Coller une réponse 100% AI-générée non-retravaillée (les redditers détectent)

Sur la donnée
- Inventer un chiffre "à la louche" sous prétexte que la source est introuvable
- Utiliser une source secondaire (Twitter, blog perso) pour un chiffre principal
- Avoir une incohérence numérique entre chart, comment, article (toujours faire le check d'incohérence avant publication)
- Citer une source sans la lire (ex: "per Goldman Sachs" sans avoir vu le rapport)
- Mélanger deux deflators dans le même chart (CPI ET New Start Index → choisir UN seul, mentionner l'autre dans la méthodo)
- Livrer un article sans avoir produit fact_check_audit.md ligne-par-ligne au préalable (cf. ÉTAPE 2-BIS — bloquant)
- Livrer un article avec un 🔴 résiduel non résolu dans l'audit (chaque 🔴 doit être recalculé, confirmé par web_search, reformulé prudemment ou supprimé)
- Garder une citation attribuée (titre + auteur + année) sans web_search dédié confirmant l'existence du document
- Garder une comparaison superlative ("largest since 1967", "first time since 2021") sans la recalculer sur le dataset complet
- Hériter un chiffre d'une session antérieure sans le re-vérifier (chaque cycle audite ses chiffres depuis zéro, même si déjà vérifiés dans un cycle précédent)
- Recopier des valeurs de source dans `build_dataset.py` « parce que le fichier n'est pas garanti disponible » (cycle 21 bis : prix Big Mac de janvier publiés face à une livraison de juillet) ; on épingle une date, jamais des nombres
- Laisser l'ensemble être « les membres que la donnée a » au lieu de l'énumérer depuis la liste officielle avant de construire (« 10 plus grandes villes » avec deux absentes)
- Écrire une raison d'exclusion sans l'avoir vérifiée contre la source le jour même (« l'OCDE ne les couvre pas » alors qu'il leur manque seulement l'année 2025) ; une raison fausse recopiée dans l'article, la FAQ et l'objection pré-écrite est réfutable en un clic, trois fois
- Annoncer « the N largest » quand un membre du top N manque, ou combler le trou avec le N+1 sans le dire
- En cas de doute persistant après recalcul + web_search, garder le chiffre "au cas où" — règle : en cas de doute, supprimer la phrase

Sur les sujets et la classification zone (NOUVEAU)
- Topic proposé sans assignation zone 1/2/3 explicite — chaque candidat doit être classé
- Trois cycles consécutifs en zone 3 sans rotation forcée vers zone 1 ou 2 — risque de profil partisan cumulatif
- Topic zone 3 proposé sans confirmation que les 5 règles non-prise de parti sont applicables
- Cycle zone 3 dont la sélection accentue un déséquilibre D/R déjà existant (>12-3-5 dans un sens) — il faut proposer une alternative qui rééquilibre
- Topic en zone 1 ou 2 dont le format naturel est single-line chart ou bar simple — il faut soit enrichir le format soit abandonner pour DIB

Sur le format visuel
- Single-line chart d'une seule série uploadé sur DIB EN ZONE 1 OU 2 (n'encode qu'une dimension visuelle, plafond viral mécanique <200 upvotes) — autorisé sur eco3min en illustration, jamais en post Reddit zone 1 ou 2 ; autorisé en zone 3 si sujet politique fort compense
- Bar chart simple à 4-5 barres horizontales sans encodage couleur additionnel uploadé sur DIB en zones 1 ou 2 ; autorisé en zone 3 si sujet politique fort compense
- Pie chart, time-series à deux axes Y, tableau-en-image uploadés sur DIB (formats rejetés par la communauté toutes zones confondues)
- "Hockey stick" simple (une seule courbe qui décolle, sans contexte multi-série) sur DIB en zones 1 ou 2
- "Le sujet est intéressant donc le chart suffira" — sur DIB le visuel doit fonctionner pour lui-même en zones 1 et 2. En zone 3, le sujet peut compenser, mais Q2, Q3, Q4 et Q5 du test beautiful doivent toujours passer.
- Choisir un sujet en zone 1 ou 2 qui n'appelle naturellement qu'un format à plafond viral connu, sans l'enrichir ni l'abandonner
- Skip du test DIB beautiful en phase sélection topic
- Topic proposé sans réponse explicite aux 5 questions du test beautiful
- Choisir un cadrage plus dramatique mais attaquable quand un cadrage adjacent plus défendable existe, et compter sur le top comment pour corriger (échec Q5 — l'objection vit dans le chart, le commentaire ne récupère pas le ratio : cycles 9 et 11)
- Dégrader le standard "beautiful" si aucun topic candidat ne passe le test — préférer ne pas poster cette semaine et garder le sujet pour eco3min uniquement
- Répéter le même type de chart deux cycles de suite (cf. ÉTAPE 3-BIS — règle de diversité secondaire)
- Réutiliser la même palette trois cycles de suite sans variation

Sur les titres (NOUVEAU, basé sur analyse de 15 top performers)
- Émoji dans le titre (présent dans 0 des 15 top performers analysés)
- "shocking" / "crazy" / "insane" / "you won't believe" (présent dans 0 des 15)
- Titre sous forme de question pure ("Did you know that...?") (présent dans 0 des 15)
- Titre qui commence par un chiffre précis ("$1.1 trillion in 24 months...") (présent dans 0 des 15)
- Superlatif marketing ("biggest ever", "massive", "huge")
- Verdict / ratio exact dans le titre ("X is 3.1× combined") — tue la curiosity gap

Sur les règles de non-prise de parti en ZONE 3 (NOUVEAU, BLOQUANT)
- Utiliser des adjectifs interdits dans un chart ou titre zone 3 (devastating, alarming, shocking, terrible, great)
- Citer une source partisane en zone 3 (Politico, Axios, Fox News, MSNBC, ThinkProgress, Heritage Foundation, Center for American Progress)
- Faire une attribution causale dans un chart zone 3 ("Trump caused X" / "Biden's policy created Y") — le chart montre une corrélation temporelle, pas une causalité
- Prendre parti dans le top comment OP ou dans les réponses en zone 3 — l'OP reste strictement descriptif et neutre
- Répondre à un commentateur qui essaie de faire prendre parti à l'OP par autre chose que le redirect vers les données ("the data comes from [source], readers interpret as they see fit")
- Skipper le format "deux lectures + question ouverte" dans le top comment OP zone 3

Sur la distribution
- Poster un MP4 en mode Image sur DIB (rejet automatique)
- Poster sur eco3min.fr direct sur HN dans les 6 semaines suivant le précédent (filter compte)
- Cross-poster instantanément sur 4 subs en parallèle (anti-spam filter)
- Tagger publiquement FT Alphaville (déclenche perte de goodwill)

Sur les réponses Reddit (anti-AI-detection)
- Répondre à TOUS les commentaires, même les non-upvotés (pattern "OP trop investi")
- Format identique pour toutes les réponses : bullets + reconnaissance + données + question retournée (pattern reconnaissable AI en 3-4 réponses consécutives)
- Vocabulaire trop policé : "Important distinction", "Genuine question back", "Let me be precise", "What's interesting is that..."
- Cohérence excessive : zéro faute de frappe, zéro contraction, zéro langage parlé sur 4+ réponses
- Répondre aux trolls de préférence (xBris18 type "this shouldn't be eligible") — différent d'un challenge méthodologique
- Répondre en thread à un commentaire qui critique le format ("not beautiful", "single ticker", "this is just a chart of a ticker") — c'est un signal pour le cycle suivant, pas un débat à avoir. Le critique a généralement factuellement raison sur la forme et débattre ne fait qu'amplifier le commentaire.
- Coller verbatim une réponse générée par AI sans réécrire en mots à soi
- Continuer à répondre activement après T+1h (la fenêtre algo est passée, les nouvelles réponses ressemblent à du content scheduling)

Sur le bundle JSON et le nommage des fichiers (NOUVEAU)
- Livrer un PNG dont le nom diffère de la référence dans l'article / le bundle (src de la <figure>, seo.og_image, json_ld.image, featured_image) — provoque une image 404 (bug observé cycle 11). Le nom canonique est cycle{N}_chart_desktop_16x9.png partout.
- Placer le PNG statique juste sous le chart interactif dans l'article au lieu de l'insérer AU MILIEU de l'article
- Faire commencer le code du snippet du bundle par <?php (Code Snippets l'ajoute lui-même pour le type « php »)
- Charger une lib externe du snippet depuis cdnjs.cloudflare.com (bloqué par la CSP) — utiliser cdn.jsdelivr.net ou unpkg.com
- Produire le bundle JSON spontanément — il n'est généré que sur la commande explicite « donne moi le json »


À cocher mentalement (ou littéralement dans un fichier) avant T-1h :

Sélection topic & format (BLOQUANT — avant de produire le moindre PNG)
- [ ] Topic propose un ratio / comparaison contre-intuitive ancré dans l'actu de la semaine
- [ ] Zone assignée explicitement : 1 (macro pure neutre) / 2 (narrative dramatique consensuel) / 3 (macro politique descriptif)
- [ ] Répartition cumulée vérifiée : on ne dépasse pas 3 cycles consécutifs en zone 3, on ne sous-représente pas la zone 2 (qui doit être ~50% des cycles)
- [ ] Si zone 3 : les 5 règles non-prise de parti (cf. ÉTAPE 5-BIS) sont applicables sur ce topic
- [ ] Si zone 3 : le compteur D/R/N sur les 20 derniers cycles zone 3 n'est pas en alerte (>12-3-5 dans un sens) ; si oui, ce cycle doit rééquilibrer
- [ ] Format de chart envisagé identifié explicitement (pas "on verra")
- [ ] TEST DIB BEAUTIFUL passé : réponse explicite aux 5 questions Q1/Q2/Q3/Q4/Q5
  - [ ] Q1 Encodage visuel : ≥2 dimensions encodées visuellement, dimensions nommées
  - [ ] Q2 Arrêt-scroll : pattern visuel attractif décrit en une phrase
  - [ ] Q3 Insight sans légende : ce que le chart raconte visuellement hors texte
  - [ ] Q4 Lecture non-trahie : la 1re impression (avant lecture de l'échelle) va dans le sens du message — pas de log/axe absolu qui inverse la lecture
  - [ ] Q5 Cadrage défendable : le cadrage retenu est le plus défendable de la donnée ; si un cadrage adjacent est plus rigoureux (age-band vs génération, per-capita vs absolu, médiane vs moyenne, définition réelle de la série vs "largest"…) il est soit adopté soit intégré DANS le chart — pas renvoyé au top comment
- [ ] Si zone 1 ou 2 : le format n'est PAS un single-line chart à une série, ni un bar chart simple à 4-5 barres uniformes, ni un pie chart, ni un double axe Y
- [ ] Si zone 3 et format bar chart simple ou single-element : justification explicite que le sujet politique compense (référence chart précédent comparable performant)
- [ ] Le format est différent du chart du cycle précédent (rotation diversité)
- [ ] Si ce cycle repose sur une ANCRE FAMILIÈRE (objet du quotidien, cf. ÉTAPE 3-BIS) : l'objet n'a pas déjà servi d'ancre dans les 4-6 dernières semaines (sinon repost < 1 mois = removal mécanique règle 6 DIB)
- [ ] Pattern de titre identifié parmi les 9 référencés (cf. ÉTAPE 5)
- [ ] Si tout topic candidat échoue le test → autres topics proposés plutôt que dégrader

Données (BLOQUANT — aucune ligne ne peut rester non cochée)
- [ ] fact_check_audit.md produit comme fichier séparé (cf. ÉTAPE 2-BIS)
- [ ] Tableau d'audit ligne-par-ligne couvre tous les chiffres, dates, citations, et calculs dérivés de l'article HTML
- [ ] Aucun 🔴 résiduel : chaque entrée 🔴 a été soit (a) recalculée sur dataset avec calcul Python visible, soit (b) confirmée par web_search avec URL primaire, soit (c) reformulée prudemment, soit (d) supprimée
- [ ] Toutes les citations attribuées (titre + auteur + année + média) ont fait l'objet d'un web_search dédié pour confirmer l'existence du document
- [ ] Toutes les comparaisons superlatives ("largest since X", "first since Y", "approximately Z%") ont été recalculées explicitement
- [ ] Tous les calculs dérivés (delta T+N, ratio, médiane, "above trough by") ont leur calcul Python affiché dans l'audit
- [ ] Tous les chiffres du chart sont dans dataset.csv
- [ ] Dataset produit par `build_dataset.py` depuis la source ; dernière période disponible de chaque série vérifiée ; repli éventuel (série voisine, même année) déclaré dans le CSV et la méthodo
- [ ] `build_dataset.py` ne contient aucun nombre de source (identifiants + date de millésime au plus) ; chaque intrant a son fetcher dans `dataset_freshness.py` et sa dernière livraison est celle utilisée, ou l'écart est justifié par écrit
- [ ] `set_manifest.json` écrit AVANT le dataset : univers depuis la liste officielle (URL, date), règle d'inclusion, chaque exclusion avec raison fermée + source + détail vérifiés ce jour-là, réconciliation univers = inclus + exclus, N du titre = inclus ; `set_check.py` passe dans `build_dataset.py`
- [ ] Si ensemble classé (« N plus grands ») : les N premiers du classement source sont tous présents, ou le titre et le comment disent le trou
- [ ] Rationale publiée du périmètre (« Why these N », FAQ, objection « why not X ») vérifiée phrase par phrase contre le manifeste ; test final : « quel nom manque au lecteur qui coche la liste officielle, et ma phrase sur ce nom est-elle vraie aujourd'hui ? »
- [ ] Si pièce de réserve : `build_dataset.py` relancé, diff avec le CSV de réserve, audit rejoué sur le résultat
- [ ] Millésimes hétérogènes tous portés par le sous-titre du chart
- [ ] Chaque chiffre a une source primaire identifiée et URL traçable
- [ ] Cohérence vérifiée : même chiffre clé apparaît identique dans chart / Key Findings / comment / article

Chart
- [ ] Test DIB beautiful passé : Q1 encodage visuel (≥2 dimensions encodées explicitement nommées), Q2 arrêt-scroll (pattern visuel décrit), Q3 insight sans légende (le chart raconte quelque chose même sans annotations), Q4 lecture non-trahie (1re impression dans le sens du message — pas de log/axe absolu qui inverse la lecture), Q5 cadrage défendable (le cadrage retenu est le plus défendable, ou le cadrage adjacent plus rigoureux est intégré DANS le chart — jamais renvoyé au commentaire)
- [ ] Le format n'est PAS dans la liste noire : pas de single-line chart, pas de bar chart simple à 4-5 barres uniformes, pas de pie chart, pas de tableau-en-image, pas de double axe Y
- [ ] PNG desktop 16:9 (1920×1080) généré — pour Reddit DIB primary + article eco3min + OG image
- [ ] PNG nommé cycle{N}_chart_desktop_16x9.png — nom identique dans le src de la <figure>, seo.og_image, json_ld.image et featured_image du bundle (cf. ÉTAPE 3 / ÉTAPE 10)
- [ ] GIF <2MB généré si justifié (sinon : pas de GIF)
- [ ] Pas d'eyebrow, pas de sous-titre long, pas d'annotation révélant le verdict
- [ ] Killer phrase visuelle présente dans le chart (banner sand) si la donnée le permet ; sinon explicitement non-applicable
- [ ] Watermark "Eco3min" seul navy gras 12pt en bas droite (pas de tagline, pas d'URL, pas de "u/Eco3min", pas de "OC made with...")
- [ ] Sources line en bas gauche avec sources primaires nommées
- [ ] Type de chart différent des 3 cycles précédents (cf. ÉTAPE 3-BIS — règle de diversité secondaire)
- [ ] Les quatre assertions matplotlib passent (police, débordement, chevauchement d'en-tête, `$` échappés) + garde ASCII — cf. `visuels-eco3min` §7 ter
- [ ] Titre du chart et titre de soumission traités comme deux objets distincts : plage de dates dans la soumission, pas dans le titre du chart ; aucun verbe d'intensité dans l'un ni dans l'autre (cf. tableau ÉTAPE 5)

Pre-review Eco3min identity drift (BLOQUANT — cf. ÉTAPE 2-TER)
- [ ] Title chart : descriptif factuel (0 🔴)
- [ ] Format chart : data viz ≥2 dimensions, pas infographic (0 🔴)
- [ ] Killer phrase : factuelle, ratio recalculable (0 🔴, ou non-applicable si pas de killer phrase)
- [ ] Title Reddit : counter-intuitif factuel, pas de promesse listicle "Here's everything..." ni structure narrative bannie "X did Y. Z did not." (0 🔴)
- [ ] Test règle 7 DIB anti-sensationalized (NOUVEAU cycle 7+1) : titre purement descriptif du contenu visuel, pas de setup narratif, pas de contraste teasé, pas de référence à N items non explicitement nommés (0 🔴)
- [ ] Total : 0 🔴 sur 5 — sinon reformuler avant livraison ; 2+ 🔴 = abandonner le cycle

Snippet
- [ ] PHP syntaxe validée (php -l)
- [ ] 3 vues toggle fonctionnelles (test rendu Playwright ou similaire)
- [ ] Tooltip hover OK
- [ ] Mobile responsive vérifié

Page eco3min
- [ ] Shortcode [eco3min_chart_xxx] en hero (remplace le PNG)
- [ ] PNG static inséré AU MILIEU de l'article (pas juste sous le chart interactif)
- [ ] PNG static configuré comme OG image dans RankMath
- [ ] Bouton CSV download visible above-the-fold
- [ ] Opt-in newsletter visible
- [ ] UTM dans le lien Reddit
- [ ] Clarity active (F12 Network → "clarity.ms")
- [ ] Page charge en <3s sur 4G mobile

Reddit assets
- [ ] Titre option A choisi, copié en clipboard
- [ ] Top comment finalisé en presse-papiers
- [ ] 5 réponses objections pré-écrites accessibles
- [ ] Compte Reddit logué, prêt à poster

Timing
- [ ] Jour de publication conforme à la zone : mardi 15h00 Paris (09h00 ET) en zone 1/2, **jeudi** en zone 3 (cf. ÉTAPE 8) — fenêtre US East Coast morning + EU afternoon
- [ ] 1h de bloc dans l'agenda pour répondre aux comments en temps réel

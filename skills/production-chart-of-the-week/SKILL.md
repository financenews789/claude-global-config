---
name: production-chart-of-the-week
description: "Production hebdo d'un chart viral pour r/dataisbeautiful + page eco3min associée. Activer pour TOUTE production de chart destiné à Reddit DIB couplé à un push macro. Couvre sélection et classification topic par zone (20/50/30), TEST DIB BEAUTIFUL bloquant, audit factuel ligne-par-ligne bloquant (🟢🟡🔴), pre-review identity drift Eco3min en 5 éléments dont test règle 7 anti-sensationalized titre (apprentissage cycle 7 removal), 5 règles non-prise-de-parti zone 3, double livraison 16:9 desktop, killer phrase visuelle, watermark Eco3min seul, 9 patterns titre (pattern 8 descriptif DIB-safe, structures 'X did Y. Z did not.' bannies), 9 formats (dont dumbbell log scale), pivot structurel dichotomie, pattern ANCRE FAMILIÈRE (objet du quotidien comme pivot intuitif, hedonic faible, ancre dans chart+comment jamais dans le titre, pas de rejeu avant 4-6 semaines). Combiner avec editeur-eco3min, visuels-eco3min, production-research-study, production-dataset."
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


ÉTAPE 1 — Sélection du topic (lundi matin / dimanche soir)

Critères obligatoires
Un topic est viable si tous ces critères sont remplis :

- Ancrage actu : un événement éco/macro de la semaine en cours rend le sujet pertinent maintenant (Fed meeting, earnings hyperscalers, BLS release, IMF report, géopolitique de change, etc.)
- Série historique longue : minimum 30 ans d'historique disponible publiquement (FRED, BLS, BIS, World Bank, SEC EDGAR, ECB, etc.). Les charts à série longue performent 3-5× mieux sur DIB que les snapshots court-terme.
- Ratio ou comparaison contre-intuitive : le chart doit révéler un fait que l'audience générale ne connaît pas (ratio inattendu, ranking historique, comparaison entre secteurs/pays/époques).
- Données primaires accessibles : aucune donnée tierce non-vérifiable. Si le chiffre central vient d'un blog ou d'un PDF non-officiel, on change de topic.
- Pas de promo voilée : si le sujet sert un produit, une crypto, une boîte cotée → refus immédiat (DIB filter anti-marketing).
- Le format de chart qui matche naturellement la donnée passe le TEST DIB BEAUTIFUL (cf. ÉTAPE 3-BIS — les 5 questions doivent toutes passer). Si le sujet n'appelle qu'un single-line chart à une série ou un bar chart simple à N barres uniformes, deux options : (a) enrichir le format avec encodage visuel additionnel (small multiples par sous-période, overlay de référence, décomposition par catégorie), ou (b) garder le sujet pour la page eco3min sans poste Reddit. JAMAIS d'option "on poste quand même" — un post à <200 upvotes grève la réputation du compte sur DIB et coûte une semaine.

Workflow obligatoire de découverte topic
Lancer systématiquement un web_search au début de chaque cycle hebdomadaire :

- Search : "macro economic news this week site:reuters.com OR site:ft.com OR site:bloomberg.com"
- Search : "FRED data release this week" + "BLS release this week"
- Search : "[hyperscaler] earnings guidance" si on est en saison earnings
- Search : "[topic candidat] historical chart" pour vérifier qu'il n'a pas été surposté récemment sur DIB

Cross-référence avec datasets existants eco3min (79 datasets disponibles) : si un dataset eco3min existant peut être recyclé/mis à jour pour le sujet de la semaine, c'est l'option préférée (gain de temps + cohérence SEO).

Topics qui marchent (patterns validés sur DIB)
- Rankings historiques ("4th worst since 1973")
- Multiples spectaculaires ("3.1× combined")
- Régimes de longue durée qui basculent (real interest rates, currency regimes, volatility regimes)
- Comparaisons cross-époques (today vs 1929 / 1973 / 2008 / 2020)
- Données SEC EDGAR sur Big Tech (capex, R&D, buybacks)
- Données monétaires Fed/BCE (balance sheet, RRP, TGA, M2, net liquidity)

Topics à éviter
- Charts purement actu hebdo sans profondeur historique (Bloomberg-like)
- Sujets crypto sauf angle macro (BTC stock-to-flow, ETF flows)
- Sujets micro-marché (specific stock picks, options flow)
- Tout sujet où eco3min n'a pas de dataset existant ET où la donnée historique est dispersée/incomplète


ÉTAPE 1-BIS — Classification du topic par zone (20/50/30)

Au moment de la sélection topic, chaque candidat doit être classé explicitement dans une des trois zones. La répartition cible sur 50 cycles/an est 20% zone 1 / 50% zone 2 / 30% zone 3.

Zone 1 — Macro pure neutre (10 cycles/an attendus)
Description : sujets économiques/financiers/historiques sans charge politique active et sans narrative dramatique ascendant. Capex corporate, structures monétaires, courbes historiques techniques, ratios de valorisation, cycles longs.
Exemples : Fed Phillips Curve historique, ratios capex hyperscalers, M2 cycles, term premium history, gold real returns over 50 years.
Plafond viral DIB attendu : 200-2000 upvotes.
Mesure de succès principale : conversion eco3min (CSV downloads, newsletter signups), SEO long-tail, autorité éditoriale cumulative. Pas la viralité Reddit.
Risque AMF / politique : zéro.

Zone 2 — Macro pure + narrative dramatique consensuel (25 cycles/an attendus, MOTEUR PRINCIPAL)
Description : sujets économiques/techno/finance avec un claim numérique frappant ET un narrative ascendant ou descendant consensuel qui ne polarise pas politiquement. Le claim "wow" est dans le chiffre, pas dans l'attribution causale.
Exemples : Battery costs -99% in 30 years, Solar beating IEA predictions, Cost per gigabyte of storage 1980-2025, AI training compute doubling every N months, productivity vs energy intensity historiques, semiconductor density Moore's Law style.
Plafond viral DIB attendu : 3000-10000 upvotes.
Mesure de succès : upvotes + conversion eco3min.
Risque AMF / politique : zéro. C'est le sweet spot risk-adjusted.

Zone 3 — Macro politique descriptif (15 cycles/an attendus)
Description : phénomènes économiques quantifiés qui touchent un débat politique actif. Le chart décrit factuellement un effet, une asymétrie, un fact-check chiffré. Sources primaires officielles uniquement. Vocabulaire neutre. Le débat se lance entre les commentateurs, pas via la voix d'Eco3min.
Exemples : Healthcare jobs only since 2024 (BLS), Effects of [bill] on income quintiles (Penn Wharton), US Budget Sankey, Deficit historical context, Tax burden by income decile, Tariff revenues projected, Federal employment by administration.
Plafond viral DIB attendu : 10000-50000 upvotes.
Mesure de succès : upvotes massifs + conversion + débat lancé en commentaires (pas dans l'OP).
Risque AMF / politique : faible si les 5 RÈGLES DE NON-PRISE DE PARTI sont respectées (cf. ÉTAPE 5-BIS).

Règle de rotation entre zones
Si trois cycles consécutifs ont tous été zone 3 → forcer une rotation vers zone 1 ou 2 le cycle suivant pour ne pas créer un profil partisan cumulatif sur le compte Reddit. Tracer dans le tracker (Google Sheet « ECO3MIN — CYCLES TRACKER », cf. INSTRUCTIONS — section TRACKING) la zone de chaque cycle, le format de chart utilisé, et (pour zone 3) le sens du claim politique.

DIMENSION D'ANCRAGE COGNITIF (TRANSVERSE AUX ZONES)

Au-delà de la zone politique, classer chaque topic candidat par son degré d'ancrage dans l'intuition financière personnelle du viewer DIB médian :

Topics à FORT ancrage (à prioriser quand possible, à zone politique égale) :
- Prix de l'or, métaux précieux (intuition patrimoniale)
- Immobilier (prix, taux hypothécaires, primary home)
- Salaires médians, revenu disponible par décile
- Prix essence, énergie résidentielle
- Retraite, épargne par âge, longévité
- Démographie, fertilité, espérance de vie
- Dette publique par habitant
- Inflation alimentaire, panier de la ménagère

Topics à FAIBLE ancrage (viables mais à ne pas surreprésenter) :
- Capex hyperscalers ou sectoriels
- IPO valorisations, fusions-acquisitions
- Breakeven inflation, swap spreads, term premium
- Multiples de valorisation corporate
- Cycles M2, monetary aggregates

Observation empirique (cycles Capex avril 2026 et Gold mai 2026) : à zone politique égale et qualité de chart égale, les topics à fort ancrage out-performent les topics à faible ancrage sur deux dimensions : (a) upvotes (+50-80% typique), (b) ratio shares/upvotes (×3-5 typique). L'effet vient de la portée hors-DIB du sujet — les viewers partagent ce qui résonne avec leur expérience personnelle, pas ce qui les éduque sectoriellement.

Cible 50 cycles/an : 60-70% des cycles sur topics à fort ancrage, 30-40% sur topics à faible ancrage. Ne pas faire deux cycles consécutifs à faible ancrage (risque de plateau sur les KPI cumulatifs eco3min).

Phase sélection topic — checklist obligatoire complète
À chaque proposition de topic, lister explicitement :
- Zone (1, 2 ou 3) + justification (pourquoi cette zone)
- Type de chart envisagé + résultat du test DIB beautiful (cf. ÉTAPE 3-BIS — les 5 questions doivent toutes passer)
- Pattern de titre envisagé parmi les 9 référencés (cf. ÉTAPE 5)
- Variation vs les 3 derniers cycles : lister les 3 derniers formats utilisés ET les 3 dernières zones
- Si zone 3 : confirmation que les 5 règles non-prise de parti sont applicables ET vérification que le bias cumulatif sur les 20 derniers cycles zone 3 ne penche pas vers un camp (cf. ÉTAPE 9-BIS sur le tracking)


ÉTAPE 2 — Vérification stricte des données (NON-NÉGOCIABLE)

Règle absolue : aucun chiffre dans le chart, le titre, le commentaire ou l'article ne doit être inventé, estimé "à la louche", ou non-traçable à une source primaire.

Procédure de vérification
Pour chaque chiffre qui apparaîtra publiquement :
- Source primaire identifiée : URL exacte du document source (10-K, communiqué Fed, série FRED, BLS table, etc.)
- Date de la source : quand le chiffre a été publié/révisé pour la dernière fois
- Méthode de calcul si dérivé : si le chiffre est un ratio, une moyenne, un cumul → la formule doit être documentée dans le CSV produit
- Inflation/conversion explicite : si conversion 2025 USD, indiquer la série CPI utilisée (BLS CPIAUCSL est le défaut) et l'année de base
- Cohérence cross-document : le chiffre dans le chart, le sous-titre, le tableau Key Findings, le commentaire Reddit, et l'article doit être identique au dollar près. Toute différence = bug à corriger avant publication.

Web_search obligatoire
Pour tout chiffre récent (< 6 mois), point précis non-iconique :
- web_search avec le chiffre exact pour vérifier qu'il est cité par au moins 2 sources crédibles
- Si seule source = un tweet, blog perso, ou forum → refus, on cherche le primary

Le check anti-incohérence interne
Avant publication, rechercher dans tous les livrables produits (article HTML + comment Reddit + chart annotations) chaque chiffre clé du Key Findings. Si même chiffre apparaît avec deux valeurs différentes (ex: "11×" dans Key Findings et "18×" dans le body), bug bloquant.
Exemple concret du cycle AI capex (mai 2026) : l'article body disait "approximately 18" pour le run-rate Apollo, alors que Key Findings + Conclusion disaient "≈11×". Calcul correct : $355B/an (2026E) / $31B (Apollo peak 1966 en 2025 USD) = 11.45×. Le 18× venait d'une moyenne 24-mois ($562B/an) du brouillon initial. L'incohérence aurait été détectée et exploitée par les commentateurs DIB en moins d'une heure.

Le CSV produit DOIT contenir toutes les données du chart
Le fichier dataset.csv téléchargeable depuis eco3min doit permettre à n'importe qui de reproduire exactement le chart. Cela signifie :
- Toutes les valeurs affichées dans le chart présentes dans le CSV
- Une colonne source pour chaque ligne (URL ou citation primaire)
- Une colonne notes pour les méthodologies particulières (deflator utilisé, période d'agrégation, ajustements)
- Une première ligne de métadonnées : # Source: eco3min.fr/[slug] | Date: [YYYY-MM-DD] | License: CC-BY 4.0


ÉTAPE 2-BIS — AUDIT LIGNE PAR LIGNE PRÉ-LIVRAISON (BLOQUANT)

Cette étape est NON-SKIPPABLE. Aucun livrable (article HTML, Reddit pack, SEO meta) ne peut être présenté à Paul tant que cet audit n'a pas été exécuté entièrement sur l'article et que zéro 🔴 résiduel ne subsiste.

Pourquoi cette étape existe
Cycle CPI heatmap (19 mai 2026, audit post-livraison Paul) — quatre erreurs factuelles avaient passé un premier audit "global" et étaient dans l'article livré :
- "+5.95pp in 1973" dans Three Observations — calcul jamais re-vérifié sur dataset, vraie valeur T+12 = +4.45pp
- "larger than any single-month move at the equivalent point in the four prior cases" — claim comparatif jamais calculé sur dataset, faux (1948-51 avait +1.73pp à T+11 vs 2024-26 à +0.85pp)
- "IMF's Historical Inflation Cycles in Advanced Economies, 2023" — citation fabriquée, le vrai papier IMF est "One Hundred Inflation Shocks: Seven Stylized Facts" (WP 23/190)
- "approximately 2.5% by mid-2006" — affirmation jamais recalculée, vraie valeur Juin 2006 = 4.18%

Cause racine : un audit "global" qui regarde la cohérence et les principaux chiffres ne suffit pas. Les erreurs passent dans les phrases secondaires, les digressions, les citations attribuées, les comparaisons en passant. Il faut un audit ligne par ligne, chaque chiffre, chaque attribution, chaque calcul dérivé.

Procédure obligatoire (ordre strict)

Étape 2-bis.1 — Extraction exhaustive
Parcourir l'article HTML du début à la fin et lister dans un tableau :
- Chaque nombre numérique (pourcentage, ratio, dollar, mois, années, durée)
- Chaque date précise (mois + année minimum)
- Chaque citation attribuée (titre + auteur + année + média)
- Chaque comparaison superlative ("the largest", "the lowest", "the first since", "more than", "approximately")
- Chaque calcul dérivé (delta, ratio, moyenne, médiane)
Aucune omission tolérée. Si l'article contient 60 chiffres, le tableau a 60 lignes.

Étape 2-bis.2 — Classification par ligne
Classer chaque entrée 🟢 / 🟡 / 🔴 :
- 🟢 LOW : valeur directement issue du dataset chargé dans la session ET recalculée dans cette session par un bloc Python explicite
- 🟡 MEDIUM : valeur plausible, in-context, MAIS pas recalculée explicitement OU pas web-vérifiée
- 🔴 HIGH : citation attribuée (titre + auteur + année) non confirmée par web_search dans la session ; pourcentage à 3+ chiffres significatifs sur fait récent non confirmé ; "approximately X" sans calcul affiché ; comparaison superlative ("largest", "first since", "lowest in N years") non recalculée

Précisions de classification :
- 🟢 admet aussi le **fait historique stable et iconique** (frères Hunt 1980, crise des otages en Iran…), même sans recalcul en session.
- Un chiffre iconique mais **ancien de plus de deux ans** redescend en 🟡 : le web_search est fait au moins une fois, à la première publication.
- Toute information « récente » **issue du contexte de la consigne de Paul** est 🟡 par défaut, jamais 🟢. Si le claim est central, web_search obligatoire.

Étape 2-bis.3 — Résolution obligatoire
Tout 🔴 → action obligatoire au choix :
- (a) recalculer sur le dataset si possible, en affichant le calcul dans un bloc Python visible
- (b) web_search pour confirmer la citation/le chiffre depuis une source primaire (.gov, .org institutionnel, papier académique référencé)
- (c) reformulation prudente : "approximately X" devient "around X" ou "more than Y" ; superlatif devient descriptif sans superlatif
- (d) suppression pure et simple : si aucun de (a)(b)(c) ne marche, la phrase entière contenant le chiffre disparaît de l'article

Tout 🟡 → recalculer (option a) ou web-confirmer (option b). Si aucune des deux n'est faisable rapidement → traiter comme 🔴 et appliquer (c) ou (d).
Tout 🟢 → no action.

Règle "en cas de doute, supprimer" : si après tentative de résolution un doute subsiste, supprimer la phrase entière. Mieux vaut un article 3% plus court qu'un article avec une erreur factuelle qui se fera attaquer dans les commentaires Reddit.

Étape 2-bis.4 — Audit des citations attribuées (cas particulier)
Chaque citation type "(per the IMF's [titre], YYYY)" ou "the Federal Reserve's [document], YYYY" doit faire l'objet d'un web_search dédié pour confirmer :
- Que le document existe (titre exact + auteur exact + année exacte)
- Que la citation faite correspond au contenu du document
Si l'un des deux échoue → suppression de la citation. Le fait sous-jacent peut souvent être conservé sans attribution ("As is standard in academic work on inflation cycles...") plutôt qu'avec une attribution fausse.

Étape 2-bis.5 — Recalcul obligatoire des calculs dérivés
Toute phrase contenant un calcul dérivé (delta, moyenne, médiane, ratio, "at T+N months", "X percentage points above", "from $A to $B = X%") doit avoir son calcul affiché en bloc Python visible dans l'audit. Pas de calcul mental, pas de "ça doit faire à peu près".
Pour les charts à séries temporelles (T+N alignment) : recalculer toutes les valeurs cited à T+N depuis la donnée brute, pour chaque épisode mentionné dans l'article. La cohérence T+11 ≠ T+12 doit être respectée.

Étape 2-bis.6 — Audit final livré comme fichier séparé
Le tableau d'audit complet (avec sa colonne 🟢🟡🔴, ses calculs Python, ses URL de web_search, et la liste des suppressions/reformulations appliquées) est livré comme fichier fact_check_audit.md distinct.
Ce fichier est livré AVANT le Reddit pack et avant la confirmation finale à Paul que l'article est prêt. Pas de livraison de Reddit launch tant que fact_check_audit.md ne montre pas zéro 🔴 résiduel.

Patterns d'erreur typiques à chercher activement
Liste non-exhaustive des erreurs qui ont passé des audits superficiels dans les cycles précédents :
- Citation académique au titre approximatif ("IMF's [titre plausible]") — chercher web_search systématique
- Comparaison superlative non recalculée ("largest since 1967", "first since February 2021") — recalculer sur dataset complet
- Delta T+N hérité d'un brouillon antérieur ("+5.95pp" qui est en fait une vieille valeur) — recalculer depuis trough_value en session
- "approximately X%" jamais recalculé — afficher le calcul explicite
- Date approximative ("mid-2006") qui implique une valeur — recalculer la valeur exacte au mois mentionné
- Pourcentage qui dérive d'un autre pourcentage ("3.1× combined" = AI / (Manhattan+Marshall+Apollo)) — refaire le calcul depuis les valeurs individuelles
- Attribution agrégée plausible mais sans source spécifique ("per executive commentary on the Q1 2026 earnings call") — vérifier que la commentary existe vraiment
- Chiffre repris d'une session antérieure sans re-vérification — chaque nouveau cycle, l'audit est refait à partir de zéro même pour des chiffres précédemment vérifiés
- Série dont le label annonce une statistique différente de ce qu'elle mesure (median vs average, real vs nominal, seasonally adjusted vs raw) — vérifier que la série EST la statistique annoncée : AHE / AHETPI = MOYENNE (jamais "median") ; OEWS = médiane. À fort ancrage cognitif (salaires, prix), ce mismatch de label se fait démonter publiquement sur source officielle (cycle 7 repost : AHETPI ~31 $ labellée "median work" vs OEWS ~24,5 $)


ÉTAPE 2-TER — Pre-review Eco3min identity drift (BLOQUANT)

Cette étape complète l'audit ligne-par-ligne (ÉTAPE 2-BIS). Elle est non-skippable et bloquante.

Pourquoi cette étape existe
Sur 50 cycles/an, même si chaque livrable individuel passe l'audit factuel, le cumul peut faire drifter l'identité Eco3min vers Bloomberg op-ed, Buzzfeed listicle, ou infographic populiste. C'est le risque "mort par mille petites pentes". L'audit factuel attrape les erreurs ; ce pre-review attrape les drifts de marque.
Apprentissage cycle 7 (mai 2026 — Purchasing Power) : le titre Reddit original "[OC] A Big Mac took 11 minutes... Here's everything that didn't keep up" a été rejeté à ce pre-review (1 🔴 sur "promesse listicle") et reformulé en "[OC] A Big Mac required 11 minutes... The same is not true for six other items" (0 🔴, Eco3min-aligned). Différence faible en CTR estimé (~25%), différence forte en cohérence d'identité cumulative.

Procédure obligatoire
Auditer explicitement 5 éléments du cycle (la 5ème ajoutée après removal cycle 7) :

| Élément | Question identité | 🟢 Si | 🔴 Si |
| :-- | :-- | :-- | :-- |
| Title chart | Zone analytique ou éditoriale ? | Descriptif factuel ("What one hour of US median work bought") | Jugement opinable ("Stuff got cheaper. Living got more expensive.") |
| Format chart | Data viz ou infographic ? | Encodage ≥2 dim, log scale, dumbbell, scatter, heatmap | Tiles colorées, gros chiffres dominants, pictos, gros emoji |
| Killer phrase | Factuelle ou suggestive émotionnellement ? | Ratio recalculable ("now costs the wage-time of nearly 40 mid-range TVs") | Adjectif qualifiant ("an absolutely insane shift in cost of living") |
| Titre Reddit | Counter-intuitif factuel ou promesse listicle ? | "Hours of [métrique] for [N items], [période]" | "Here's everything..." / "You won't believe..." / "X did Y. Z did not." |
| Test règle 7 DIB ⚠️ NOUVEAU cycle 7 | Le titre peut-il être lu par mod team comme sensationalized headline ? | Strictement descriptif du contenu visuel | Setup narratif, contraste teasé, référence à N items non explicité, promesse de découverte |

Test règle 7 DIB — méthode opérationnelle
Lire le titre Reddit envisagé et poser la question : "Un mod de r/dataisbeautiful qui voit ce titre dans la queue de modération va-t-il y voir une description plate du chart, ou un teaser narratif ?"
Indicateurs concrets d'un titre teaser (= 🔴 sur ce test) :
- Le titre fait scroll-stop par sa formulation (au-delà du sujet lui-même)
- Le titre contient une opposition non encore résolue ("X did Y, but Z..." / "Most people think X, but actually...")
- Le titre fait référence à un nombre d'items sans les nommer ("6 other items", "8 things", "5 surprises")
- Le titre utilise une structure narrative (clauses successives qui construisent un contraste)
- Le titre suscite la question "et alors ?" plutôt que d'y répondre
Si un seul de ces indicateurs s'applique → 🔴 sur le test règle 7 → reformuler en pattern purement descriptif (cf. Pattern 8 révisé).
Référence cycle 7 : le titre "A Big Mac required 11 minutes of US median work in 1986. It still does in 2025. The same is not true for six other items." cochait 4 des 5 indicateurs (scroll-stop, opposition non résolue, référence à N items non nommés, structure narrative à 3 clauses). Removed par mods T+2h. L'audit B.5 actuel aurait dû l'attraper. Le test règle 7 explicite ci-dessus est la conséquence.

Règle de décision
- 0 🔴 sur 5 → cycle libéré pour publication
- 1 🔴 sur 5 → reformuler l'élément concerné avant livraison
- 2+ 🔴 sur 5 → le cycle est mal calibré, abandonner et choisir un autre angle
Ne JAMAIS publier avec un 🔴 résiduel sur la base de "le viral l'emporte cette fois". C'est exactement comme ça que l'identité dérive cumulativement OU que les mods removed le post.
Apprentissage cycle 7 : le 5ème test (règle 7 DIB) est non-négociable. Le coût d'un removal mod après 2h de traction = perte de 5,000-15,000 upvotes finaux. Pas comparable avec le coût d'attendre 30 min de plus pour reformuler le titre.

Lien avec le pre-review adversarial existant
Ce pre-review s'ajoute aux 4 reviewers hostiles du skill production-research-study (Adversarial Pre-Review). Les 4 reviewers cherchent les attaques factuelles probables ; ce pre-review identité cherche le drift de marque. Les deux sont complémentaires et obligatoires.


ÉTAPE 3 — Le chart (template V4 minimaliste)

Le principe central : 2 secondes de compréhension + question en suspens
Le chart doit être :
- Comprensible en 2 secondes : un utilisateur Reddit qui scroll voit le chart, comprend l'idée principale, upvote ou pas. Si l'idée demande plus de 2 sec à émerger, le chart est mort.
- Avec une question implicite : le chart révèle visuellement un fait frappant (disproportion énorme, ratio inattendu) MAIS ne révèle PAS le verdict chiffré exact. Ce verdict reste réservé au commentaire.
- **Portée nationale = pays nommé.** Dès qu'un cycle porte sur un seul pays, le nom du pays apparaît dans le titre du chart ou dans l'image. Sans lui, la moitié du sub suppose « US » et l'autre moitié conteste — et le débat porte sur le périmètre au lieu de la donnée.
- **Superlatif = vérification de la série.** Tout « largest / highest / only / first / record » se vérifie contre la **définition réelle** de la série sous-jacente, pas contre son nom. Apprentissage cycle 9 : « 20 largest US metros » ≠ indice Case-Shiller 20-City ; les trois commentaires les plus upvotés du thread étaient cette critique, ratio 86,3 %.
Exemple V4 AI capex : la barre orange écrase les 3 grises → le viewer comprend "AI capex >> programmes historiques" (idée en 2 sec). Mais le chart ne dit PAS "3.1× combined" → pour avoir le ratio exact, il faut aller dans le commentaire.

Règles de design (template V4 minimaliste)
Ce qu'on garde :
- Titre court (4-6 mots utiles, pas de superlatif marketing) — ex: "Big Tech AI capex vs US megaprojects"
- Mini-badge top-right : unité/conversion (ex: "2025 USD (inflation-adjusted)") en 10pt italique discret
- Watermark bottom-right : Eco3min (gras 12pt navy) uniquement. Pas de tagline secondaire type "Weekly macro chart" — il alourdit le footprint promo et n'apporte rien au reader. Pas de URL "eco3min.fr". Pas de "OC made with Eco3min toolkit". Pas de "u/Eco3min · r/dataisbeautiful". Le [OC] est déjà dans le titre Reddit, pas besoin de doublon. Convention FT/Economist : signature simple en bas droite, point final.
- Source line bottom-left : sources primaires nommées en 9pt
- Couleurs : la palette varie selon le type de chart (voir ÉTAPE 3-BIS sur la diversité des formats). Aucune palette n'est imposée par cycle — mais le **port d'attache par défaut** est la palette catégorielle du brand kit (brand-kit-eco3min §2.5, 7 rangs sourds terracotta→bleu acier→vert→violet→ocre→charcoal→rouge) et les 3 registres de fond §2.2 (crème / blanc / charcoal inversé). Les sorties du port d'attache sont légitimes quand le registre éditorial du sujet les appelle, et pilotées par la règle de diversité de l'ÉTAPE 3-BIS. Direct labeling en bout de ligne pour tout multi-séries ≤6 (cf. visuels-eco3min §3).

Ce qu'on supprime systématiquement :
- Eyebrow type "ECO3MIN · CAPITAL EXPENDITURES" → pure déco
- Sous-titre long → redondant avec les labels des barres
- Annotations type "Still growing", "Combined: $XXXB", brackets de comparaison → révèlent la réponse
- Légendes décoratives, gradients, ombres, fontes fantaisie

Spécifications techniques
PNG statique (pour X, LinkedIn, OG image, fallback Reddit) :
- Format : PNG, 1920×1080 (16:9), DPI 150
- Police : DejaVu Sans (cohérence cross-OS)
- Title fontsize : 30pt, à réduire si l'assertion de débordement le demande. Un titre long ne se met pas à la ligne dans matplotlib, il est rogné au bord du PNG.
- Plot bbox : [0.22, 0.14, 0.74, 0.64] pour aérer haut et bas (éviter chevauchement watermark/x-axis)

QUATRE ASSERTIONS AVANT `savefig` (bloquant) : repli de police, débordement de
canvas, chevauchement des textes d'en-tête, échappement des `$` — plus le garde
ASCII sur le cmap. Code et motif de chacune dans `visuels-eco3min` §7 ter. Les
quatre échecs sont silencieux : le PNG sort, il paraît correct en vignette, et
seule l'assertion les attrape. Ne pas s'en remettre à la relecture visuelle.

NOMMAGE DU FICHIER (BLOQUANT) : le PNG desktop est TOUJOURS nommé cycle{N}_chart_desktop_16x9.png (ex. cycle11_chart_desktop_16x9.png). Ce nom EXACT doit apparaître à l'identique partout : le src de la <figure> dans l'article, seo.og_image, le champ image du JSON-LD, et pages.{en,fr}.featured_image du bundle (cf. ÉTAPE 10). Un nom différent entre le fichier que j'uploade et la référence dans l'article = image 404 (bug observé cycle 11). Le CSV suit la même logique avec son propre nom de fichier, identique entre le fichier uploadé, le lien de téléchargement de l'article et le bundle.

GIF Reddit — UNIQUEMENT SI L'ANIMATION EST JUSTIFIÉE PAR LA DONNÉE :
Avant de produire un GIF, appliquer cette règle de validation :
L'animation est JUSTIFIÉE quand la donnée a une dimension temporelle ou narrative réelle :
- Time-series longue qui se déroule (ex: 50 ans de données mensuelles)
- Évolution avant/après visible avec un changement de régime
- Construction progressive d'un total qui révèle un punch
- Cartographie/scatter qui change de configuration sur des dimensions multiples
- Animation morphing qui montre un état A se transformer en état B
L'animation N'EST PAS JUSTIFIÉE quand :
- 4-5 barres qui se remplissent dans un ordre arbitraire (cas du cycle AI capex mai 2026)
- Aucune dimension temporelle réelle dans la donnée
- Le punch est entièrement contenu dans la frame finale du GIF
- L'animation est purement décorative
Si l'animation n'est pas justifiée, poster le PNG seul. Sur DIB, une animation gratuite est probablement net négative en upvotes (-10-20% estimé) car :
- Elle ralentit la compréhension dans le scroll feed
- Certains users la perçoivent comme gimmicky
- Des trolls peuvent attaquer ("not everything needs to be animated")
- Compense partiellement par dwell time + brand recall, mais reste défavorable sur l'individuel post
Le contre-argument long-terme (animation = post mémorable = brand recall sur 50 cycles) ne tient que si l'animation a une réelle valeur de signal qualité, pas si elle est décorative.

Spécifications GIF si justifié :
- Format : GIF, 1280×720 (réduction de taille pour mobile)
- DPI : 120, FPS : 18, durée : 6 secondes
- Title fontsize : 24pt (réduit vs PNG car canvas plus petit)
- Cible taille : < 2 MB, idéalement < 1 MB
- Watermark : "Eco3min" seul (cohérent avec le PNG)

Pourquoi GIF et pas MP4 : depuis avril 2026, r/dataisbeautiful en mode "Image" rejette les vidéos avec message "Cette communauté n'autorise pas les vidéos". Le GIF passe car techniquement c'est une image animée. Ne jamais essayer de poster un MP4 en mode Image.

Référence : le script Python canonique
Le script generate_chart_v4.py du cycle AI capex (mai 2026) sert de template de base. Pour chaque nouveau chart, dupliquer ce script et adapter :
- La liste PROJECTS ou équivalent (les données du chart)
- Le titre, le badge, les sources line
- Éventuellement le X_MAX et les X_TICKS pour caler l'échelle
Ne pas réintroduire bracket, eyebrow, ou subtitle long. Si tu te surprends à vouloir ajouter ces éléments "pour clarifier", c'est que tu es en train de tuer la viralité.

ÉTAPE 3-BIS — Sélection du format pour DIB : TEST BEAUTIFUL (PRIMAIRE) + diversité (secondaire)

Cette étape est BLOQUANTE. Aucun chart ne peut être produit (et a fortiori uploadé sur Reddit) sans avoir passé le test DIB beautiful complet.

Pourquoi cette règle existe
Le sub r/dataisbeautiful a un critère explicite dans son nom : "is this beautiful?". Ce n'est pas un critère cosmétique, c'est ce qui détermine le plafond viral du post. Un chart factuellement correct et bien sourcé peut plafonner à <200 upvotes simplement parce qu'il n'est pas visuellement intéressant en soi.
Échec documenté : cycle "It took gold 45 years to surpass its inflation-adjusted peak" (mai 2026) — single-line chart d'une seule série, claim historique fort, données solides. Résultat : 106 upvotes en 3h, commentaire critique "It's literally just a chart of a single ticker. What's beautiful about it?" non contesté. Pas de viralité possible parce que la forme échouait le test "beautiful" indépendamment de la qualité du claim.
La diversité entre cycles existe toujours, mais elle est secondaire au test beautiful. Le test beautiful est primaire et bloquant.

Le TEST DIB BEAUTIFUL — 5 questions, toutes doivent passer
À appliquer en phase de sélection topic ET juste avant de produire le PNG. Si une seule question échoue, le format est rejeté et on cherche une alternative (enrichissement ou changement de topic ou de cadrage).

Q1 — ENCODAGE VISUEL : ce chart encode-t-il au moins 2 dimensions de données visuellement (au-delà de l'axe X / axe Y de base) ?
Exemples de double encodage valide :
- couleur ET position (heatmap)
- taille ET temps (bubble chart évolutif)
- ranking ET durée (slope chart, bump chart)
- géographie ET intensité (choropleth)
- distribution ET temps (ridge plot, joyplot)
- hiérarchie ET valeur (treemap, sunburst)
- N catégories ET temps simultanés (small multiples, stacked area)
Un single-line chart à une série ou un bar chart simple à N barres uniformes n'encode qu'1 dimension visible (la valeur sur l'axe Y/X). ÉCHEC automatique de Q1.

Q2 — ARRÊT-SCROLL : un viewer qui voit le chart sans lire le titre s'arrête-t-il dessus parce que le pattern visuel attire l'œil ?
Pattern attractif = contraste fort, asymétrie marquée, structure répétitive (small multiples, heatmap), trajectoire surprenante (slope chart croisé), densité visuelle (ridge plot empilé), géométrie inattendue (Sankey, waterfall).
Une courbe monotone propre, même sur 50 ans avec annotations événementielles, n'attire pas le scroll. ÉCHEC de Q2.

Q3 — INSIGHT SANS LÉGENDE : si je supprime tout texte sauf le titre, le chart raconte-t-il encore quelque chose visuellement ?
Test pratique : masquer mentalement les annotations, les valeurs en bout de barre, les légendes — il reste quoi ? Si la réponse est "rien, sans les annotations le chart ne dit rien", le visuel ne porte pas le claim — c'est juste un support du texte. ÉCHEC de Q3.

Q4 — LECTURE NON-TRAHIE (apprentissage cycle 7 repost) : la première impression visuelle, AVANT de lire l'échelle et la légende, confirme-t-elle le message ou le contredit-elle ?
Un chart peut passer Q1/Q2/Q3 et quand même tromper si l'encodage (échelle log, axe absolu sur grandeurs incommensurables, double-codage couleur) inverse la lecture intuitive. Test pratique : montrer le chart 2 secondes à quelqu'un qui ne lit que le titre — sa première impression va-t-elle dans le sens du message ? Si le viewer médian conclut "rien n'a changé / tout pareil" là où la donnée dit "divergence massive", Q4 ÉCHOUE — peu importe que l'échelle soit mathématiquement correcte. Renvoi : format 9 (décision d'encodage absolu-vs-variation) ; PROCESS LEARNINGS (le filtre hybridation attrape le drift de TON, pas le défaut d'ENCODAGE — Q4 comble ce trou).
Échec documenté cycle 7 repost : dumbbell sur axe absolu log (6 items, 5 ordres de grandeur). Le log comprimait la variation — qui était le message — au point que la première lecture était "rien n'a changé". Critique #1 du thread (log scale, plus upvotée que le post lui-même), ratio tombé à 83,8%. Cf. CAS D'ÉCHEC.

Q5 — CADRAGE DÉFENDABLE (apprentissage cycles 9 et 11 — BLOQUANT, à trancher en phase SÉLECTION, AVANT le choix du format) : sur la donnée source retenue, existe-t-il un cadrage alternatif que le commentateur DIB médian jugerait plus rigoureux que celui choisi ? Si oui, pourquoi ne pas le prendre — et la seule raison est-elle qu'il est plus dramatique / plus viral ?
- PASS : le cadrage retenu est le plus défendable de la donnée, OU le cadrage adjacent plus défendable est intégré DANS le chart (2e panneau, série de référence, annotation), pas seulement promis au top comment.
- FAIL : il existe un cadrage adjacent plus défendable, on ne le prend pas parce qu'il est moins spectaculaire, et l'attaque qui en découle vit dans le chart. → Résolution : soit basculer sur le cadrage défendable (quitte à perdre du drama), soit l'intégrer au chart lui-même.
RÈGLE DURE : si l'attaque prévisible vit dans le CHART, un top comment correctif ne récupère pas le ratio. Cycle 11 (wealth by generation) : le cut par âge (age-band) — le cadrage défendable — a été donné en commentaire, le ratio est quand même tombé à 92% (topic à factions, cible ≥94%), les deux commentaires les plus upvotés du thread étant précisément cette critique (alsimoneau +1224, at1445 +655). Neutraliser une objection de cadrage = changer de cadrage OU mettre le cut défendable DANS l'image — jamais "je répondrai en commentaire".
AXES DE CADRAGE ADJACENT à tester mécaniquement (les objections DIB récurrentes) :
- cohorte / génération vs tranche d'âge (age-band)
- absolu vs per-capita (par tête / par ménage)
- nominal vs réel (inflation-adjusted)
- médiane vs moyenne (mean tirée par outliers : top 1 %, une poignée de milliardaires type Musk/Bezos/Zuckerberg)
- part (%) / niveau, et total vs distribution
- "largest / top N" nommé vs définition réelle de l'indice / de la série
- brut vs net
PRÉCÉDENTS :
- Cycle 9 : "20 largest US metros" ≠ indice Case-Shiller 20-City → les 3 commentaires les plus upvotés du thread étaient cette critique, ratio 86,3%.
- Cycle 11 : generation-share vs age-band → les 2 commentaires les plus upvotés du thread étaient cette critique, ratio 92%.
DISTINCT DE Q4 : Q4 = tromperie VISUELLE (échelle / log qui inverse la première impression). Q5 = choix de MÉTRIQUE / cadrage (quelle variable on montre). Un chart peut passer Q4 et rater Q5 : au cycle 11 l'encodage stacked-area était lisible (Q4 OK) mais le cadrage par génération était le cadrage attaquable (Q5 FAIL). Le tell : si l'objection prévisible porte sur "tu aurais dû montrer X plutôt que Y", c'est Q5 ; si elle porte sur "ton échelle trompe l'œil", c'est Q4.

Formats à plafond viral connu sur DIB (À ÉVITER POUR REDDIT — sauf exception zone 3)
Ces formats sont autorisés comme illustration sur la page eco3min mais ne sont PAS uploadés sur DIB en post principal, sauf exception zone 3 :
- Single-line chart d'une seule série temporelle (même sur 50 ans, même avec annotations événementielles) — échoue Q1 et Q2
- Bar chart simple à 4-5 barres horizontales sans encodage couleur additionnel ou catégorie secondaire — échoue Q1
- Pie chart (toujours, conventions DIB) — échoue Q2
- Tableau formaté en image — échoue Q1 et Q2
- Time-series à deux axes Y (rejetée par la communauté DIB par convention)
- "Hockey stick" simple (une seule courbe qui décolle, sans contexte multi-série) — échoue Q1

EXCEPTION ZONE 3 : un bar chart simple ou un single-element chart peut être accepté si le sujet politique est suffisamment fort par lui-même (style "Generational Gap Congress" 12k upvotes, "Longest government shutdown" — leurs charts sont des bar charts simples mais le sujet politique fait le travail viral). Dans ce cas, Q1 peut échouer mais Q2, Q3, Q4 et Q5 doivent toujours passer. La justification doit être explicite dans la phase sélection topic : "Q1 ne passe pas mais le sujet zone 3 [X] compense — référence performante : [chart précédent similaire qui a fait Yk upvotes]".

EN ZONE 1 ET 2 : aucune exception au test beautiful. Single-line chart d'une seule série ou bar chart simple = rejet automatique. Format réservé à la page eco3min en illustration uniquement.

Si le sujet (en zone 1 ou 2) n'appelle naturellement qu'un de ces formats, deux options :
(a) ENRICHIR : ajouter une dimension visuelle pour passer le test
- Superposer un small multiples par sous-période historique
- Ajouter une heatmap d'événements en arrière-plan (recessions, crises)
- Décomposer en N catégories (régions, secteurs, cohortes)
- Ajouter une seconde série de référence (ratio, normalisation, benchmark)
- Ajouter des bandes de drawdown coloriées
- Transformer en slope chart avec N actifs/cohortes
- Passer à small multiples ou ridge plot si la donnée le permet
(b) ABANDONNER le sujet pour DIB et garder pour eco3min uniquement (article + dataset publiés sans poste Reddit cette semaine)
JAMAIS d'option (c) "on poste quand même en croisant les doigts". Le post Reddit raté grève la fréquence d'apparition d'eco3min sur DIB (l'algorithme du sub mémorise les comptes à faible engagement) et coûte une semaine sans contrepartie.

Formats à fort potentiel visuel sur DIB (9 patterns identifiés sur top performers)
Ces formats passent généralement le test beautiful nativement. Liste hiérarchisée par compatibilité avec l'identité éditoriale Eco3min (sobre, cream, journalistique) :

1. SPAGHETTI FOCUS — LE SWEET SPOT POUR ECO3MIN ⭐
N lignes grises en background + 1-2 lignes accentuées en couleur. Le contraste focus/background fait l'insight visuel.
- Compatible identité cream/sober Eco3min : naturellement académique
- Encode ≥2 dimensions : cohorte (chaque ligne grise = un cas historique) + temps
- Narrative claim visible : la ligne accentuée raconte l'histoire seule
- Références performantes : "US dollar worst year" (Semafor), "Healthcare jobs since 2024" (FT-style), "Solar beating predictions"
- Quand l'utiliser : tout claim "X est inhabituel/extrême par rapport à ses précédents historiques", "X diverge de Y", "X bat les prévisions"

2. Comparison side-by-side / before-after (small multiples à 2-3 panneaux)
Force la comparaison visuelle. Référence : "Fertility 2007 vs 2025", "Gerrymandering Texas neutral vs 2025", "Big Beautiful Bill quintiles".

3. Heatmap matricielle dense
Deux dimensions encodées (catégorie + temps + intensité). Pattern recognition visuel sans lire. Référence : "Vaccines reduced measles cases" (Our World in Data).

4. Sankey / flux d'allocation
Décomposition de flux, structure visuelle unique. Référence : "US Budget FY2024 Sankey" (Chartr).

5. Stacked comparison décomposée
Une grande barre vs N empilés avec catégorisation visible. Référence : "NVIDIA valuation vs Big Pharma".

6. Multi-line avec annotation événementielle structurelle
Lignes multiples (≥4 séries différenciées) + 2-4 annotations verticales événementielles. Référence : "15 years of r/relationship_advice", "Vaccines measles".

7. Scatter / phase space (audience plus nerd)
Hulls ou clusters par catégorie sur 2 axes. Référence : "Fed Phillips Curve, Chair by Chair".

8. Threshold crossing / reference line (audience macro / précieux métaux / records historiques)
Une courbe historique longue + une ligne horizontale fixe à un seuil iconique. Le viewer voit visuellement la courbe approcher, échouer à dépasser, puis finalement traverser (ou rester en-dessous). Encode 2 dimensions (la série temporelle + le seuil) sans surcharge textuelle. Compatible avec sujets "X took N years to surpass Y" ou records historiques longs. Très DIB-friendly (les reference lines sont un classique accepté). Référence : Gold 1980 peak ($2,860 real, traversé Feb 2025 après 45 ans — cycle mai 2026, 390 upvotes / 96% ratio / 163% ratio shares-upvotes).

9. Dumbbell chart log scale ⭐ (apprentissage cycle 7 mai 2026)
N items horizontaux (3-8 max), chacun avec deux dots (point A = état initial, point B = état final) reliés par une ligne, sur une seule échelle log. Encode ≥2 dimensions (item × période), raconte la TRAJECTOIRE (mouvement entre 2 états) au lieu de juste les 2 états comme un small multiples. Compatible avec interactivité sorting (BY CHANGE / BY VALUE / A→Z) — vraie killer feature pour la conversion eco3min.
Critères d'éligibilité :
- Sujet "avant vs après" sur une métrique scalaire commune (work-hours, $, %, ratio, années)
- 3-8 items maximum (au-delà : trop dense)
DÉCISION D'ENCODAGE (apprentissage cycle 7 repost — BLOQUANT, à trancher AVANT le choix d'échelle) :
Si le message EST la valeur absolue (combien coûte X) ET les items tiennent dans ~2 ordres de grandeur → dumbbell sur axe absolu (linéaire si possible).
Si le message est la VARIATION (de combien X a changé) → NE PAS afficher l'absolu sur log. Le log comprime précisément la variation : le viewer voit "tout pareil" alors que la donnée diverge. Encoder directement la variation (axe Δ%, base commune, ex. −100 à +200%) ; valeurs absolues reléguées en labels sur les points.
Items sur >2-3 ordres de grandeur ET message = variation → axe Δ% ou split en 2 groupes d'amplitude. Un log "forcé par l'amplitude" n'est pas une solution à justifier, c'est le signal de changer la métrique affichée.
Tell de publication : si tu te retrouves à défendre ton échelle dans les commentaires, le chart a raté sa lecture en 2 secondes. Renvoi : test beautiful Q4 (ÉTAPE 3-BIS).
Référence cycle 7 : le FORMAT dumbbell était bon (item × période, trajectoire) ; c'est l'encodage absolu+log sur 5 ordres de grandeur (6 min essence → 13 255 h maison) qui a comprimé la variation, fait monter la critique log scale en tête de thread, et tiré le ratio à 83,8%. Le format reste ⭐ — l'erreur était l'échelle, pas le format.

Pattern transverse — ANCRE FAMILIÈRE (objet du quotidien comme pivot intuitif du CONTENU)
Un objet du quotidien universellement reconnu sert d'unité de mesure que le lecteur ressent dans son corps ("11 minutes de travail pour un Big Mac"), contre laquelle une variable abstraite (wage-time, inflation, PPP) devient lisible. Au cycle 7, le Big Mac a été le déclencheur de discussion #1 (Big Mac Index, threads mankiw/choco_pi/datums, réaction "3 TVs → 40 TVs" la plus citée).
Ce pattern précède et nourrit le PIVOT STRUCTUREL ci-dessous : l'ancre familière décide quel objet ; le pivot structurel le place visuellement.
CRITÈRES DE SÉLECTION DE L'ANCRE (par ordre d'importance) :
- Hedonic adjustment FAIBLE — l'objet-ancre doit être ~constant dans le temps. Le Big Mac (2×1.6oz patties en 1986 comme en 2026) est l'archétype.
  ⚠️ Le critère porte sur le rôle d'ANCRE, pas sur la présence dans le chart. Un objet à hedonic fort peut — et doit souvent — apparaître comme item de contraste : au cycle 7, la TV (3.3 → 40 wage-time-TVs) était un item du dumbbell, et c'est précisément son hedonic massif qui crée l'écart spectaculaire. La règle : ne jamais faire reposer le point de référence stable sur un objet dont la composition a changé, parce que c'est exactement là que les objections méthodo frappent. La TV a généré ~15 commentaires hostiles au cycle 7 en tant qu'item ; en tant qu'ancre elle aurait fait dérailler le thread entier.
  À ÉVITER comme ancre : voiture (sécurité/électronique/normes), TV, smartphone, logement.
- Ancrage émotionnel fort — tout le monde l'achète, le ressent, en a une intuition de prix immédiate.
- Légitimité académique préexistante — idéalement déjà un index reconnu, ce qui réduit (sans supprimer) la surface d'objection méthodo. Inférence, confiance moyenne : un index préexistant ne ferme pas le débat, il déplace la charge de preuve. À noter : le Big Mac a The Economist mais c'est du PPP cross-pays, pas du wage-time historique — l'analogie de légitimité est partielle. Le café a des séries BLS dédiées ; le Coca n'a pas d'index → moins défendable face aux objections.
Bons candidats futurs : café, essence (déjà utilisé cycle 7 comme item), abonnement mensuel, panier petit-déjeuner.
Placement de l'ancre et du hook qu'elle génère — l'ancre va dans le CHART + le TOP COMMENT, jamais dans le titre de la submission. C'est la leçon de placement du removal cycle 7 ; détail et formulation canonique dans ÉTAPE 5 (Pattern 8 révisé), ÉTAPE 2-TER (test règle 7) et CAS D'ÉCHEC — Cycle 7. Le post peut et doit être plus large que l'ancre (cycle 7 = 6 items + dichotomie services/goods) ; le titre reste descriptif et large. Le mismatch fatal du cycle 7 : titre rétréci à l'ancre + cliffhanger, alors que le post était large.
INTERDIT : rejouer le même objet.
- Règle 6 DIB (pas de repost de contenu populaire sous 1 mois) → un 2e post "Big Mac" sous 30 jours = removed mécaniquement.
- Redondance d'identité : deux cycles sur le même objet = signal "one-trick pony", l'inverse de l'autorité cumulative visée sur 50 cycles/an.
→ Décliner l'ARCHÉTYPE (ancre familière + wage-time) sur un objet différent, un thème différent, pas avant 4-6 semaines.

Pattern transverse — PIVOT STRUCTUREL POUR CHARTS À DICHOTOMIE
(Pour le choix de l'objet-pivot, voir le pattern ANCRE FAMILIÈRE ci-dessus — critères de sélection et règle de non-rejeu.)
Quand le sujet a une dichotomie naturelle (services-vs-goods, fixed-vs-floating, public-vs-private, taxed-vs-untaxed, regulated-vs-unregulated), identifier UN item qui peut servir de pivot conceptuel visuel au centre du chart.
Caractéristiques d'un bon pivot :
- Universellement reconnu (Big Mac, dollar, gallon de gas, action SP500)
- Position numérique au centre de la distribution ou à un point remarquable
- Idéalement : valeur stable / inchangée → sert d'ancre cognitive
Effet recherché : transforme une "liste désordonnée" en "narrative structurelle". Le viewer scan en 2 secondes : 3 items d'un côté du pivot, 3 de l'autre. Le pivot devient le point de référence implicite pour évaluer les autres.
Référence cycle 7 : Big Mac (STABLE, ±0%, "tracked wages exactly") au centre du dumbbell, 3 items "MORE WORK" au-dessus, 2 items "LESS WORK" en dessous. Visualisé avec double-bordure beige+slate sur le dot pour signifier "deux époques superposées au même point".

Règle de diversité entre cycles : si un cycle utilise spaghetti focus, les 2-3 suivants doivent utiliser autre chose. Tracker le format utilisé par cycle dans le Google Sheet (cf. INSTRUCTIONS — section TRACKING).

Règle de diversité entre cycles (SECONDAIRE au test beautiful, mais maintenue)
Ne pas répéter le même type de chart deux semaines de suite, et pas plus de deux fois sur quatre cycles consécutifs.
Au début de chaque cycle, lister les 3-4 derniers PNG livrés et leurs formats. Si le format envisagé pour la semaine est identique au plus récent → forcer une rotation vers un format différent.

Diversité de palette aussi
Même règle pour les couleurs. Si trois cycles consécutifs ont utilisé la même combinaison (ex : navy + gold sur fond crème), le quatrième cycle doit basculer ailleurs : fond blanc pur (registre academic working paper), fond charcoal inversé #1A1A1A (registre Bloomberg terminal — aligné brand-kit-eco3min §2.2), palette divergente bleu-rouge (registre research note), palette monochrome (registre print), mode catégoriel complet (rangs §2.5), etc.
Le choix de palette est dicté par le registre éditorial que le sujet appelle, pas par une charte rigide — le brand kit fournit le port d'attache (rangs §2.5, 3 registres de fond §2.2), pas une prison. Un chart sur les chocs pétroliers peut très bien être rouge brique sur fond crème ; un chart sur la dette souveraine peut être teal sombre sur fond blanc. Deux garde-fous seulement : saturation sourde (jamais pop/néon, cohérence FT) et signature fixe (watermark, sources line — ils ne varient jamais avec le registre).

Inventaire des formats à mobiliser (référence)

| Format | Passe Q1 nativement ? | Quand l'utiliser | Quand l'éviter |
| :-- | :-- | :-- | :-- |
| Bar chart horizontal | Non (enrichir avec couleur catégorielle) | Comparaison de N items sur une seule métrique, ranking, AVEC encodage couleur additionnel | Si N < 6 sans encodage couleur (échec Q1) |
| Bar chart vertical | Non (enrichir avec stacking ou couleur) | Comparaison sur axe temporel discret AVEC décomposition | Si série unique non-décomposée |
| Line chart 1 série | NON | Page eco3min illustration uniquement | Tout post Reddit |
| Line chart multi-séries (≥4) | Oui | Time-series comparée entre actifs/pays/épisodes | Si série unique ou 2 séries seulement |
| Heatmap matricielle | Oui | Pattern recognition sur deux dimensions | Quand les valeurs ont besoin d'être lues exactement |
| Small multiples | Oui | Comparaison de N épisodes structurellement similaires | Quand N > 12 ou < 3 |
| Slope graph | Oui | Évolution entre deux points discrets pour N items | Si N > 20 |
| Dot plot / scatter | Oui (avec taille+couleur) | Distribution, corrélation, ranking précis | Time-series simple |
| Sankey | Oui | Flux d'allocation entre catégories | Si moins de 3 niveaux |
| Stacked area | Oui | Décomposition d'un total qui évolue dans le temps | Si > 6 composantes (illisible) |
| Waterfall / bridge | Oui | Décomposition d'un changement entre deux états | Si plus de 8 steps |
| Ridge plot / violin | Oui | Distribution sur N catégories ordonnées | Si données trop bruitées |
| Choropleth / map | Oui | Variation géographique | Sans dimension géographique forte |

Sortie attendue à l'étape sélection topic
Quand le skill propose 2-3 topics candidats au début du cycle (cf. ÉTAPE 1), il doit explicitement mentionner pour chaque candidat :
- Quel type de chart sera utilisé
- Résultat du TEST DIB BEAUTIFUL — réponse explicite aux 5 questions :
  - Q1 Encodage visuel : combien de dimensions encodées ? Lesquelles ?
  - Q2 Arrêt-scroll : qu'est-ce qui rend ce visuel surprenant à regarder ?
  - Q3 Insight sans légende : qu'est-ce que le chart dit visuellement, hors texte ?
  - Q4 Lecture non-trahie : la 1re impression (avant lecture de l'échelle) va dans le sens du message — pas de log/axe absolu qui inverse la lecture
  - Q5 Cadrage défendable : le cadrage retenu est-il le plus défendable de la donnée ? Si un cadrage adjacent est plus rigoureux (age-band vs génération, per-capita vs absolu, médiane vs moyenne, définition réelle de la série vs "largest"…), soit on bascule dessus, soit on l'intègre DANS le chart — jamais "je corrigerai en commentaire"
- Pourquoi ce type matche la donnée (pas juste "c'est différent")
- En quoi il varie par rapport aux 3 derniers cycles (lister les 3 derniers formats utilisés)

Si l'une des 5 questions du test beautiful ne passe pas, le candidat est rejeté. Soit on enrichit le format (option a : small multiples, overlay référence, décomposition catégorielle, annotations événementielles structurelles), soit on change de cadrage (Q5), soit on abandonne le topic pour DIB et on le garde pour eco3min uniquement (option b).
Si tous les candidats appellent un format qui échoue le test beautiful, le skill doit proposer d'autres topics plutôt que livrer un quatrième chart à plafond viral connu. Une semaine sans post Reddit est meilleure qu'un post à 100 upvotes qui grève la réputation du compte sur DIB.

ÉTAPE 4 — Le snippet interactif (pour la page eco3min)

Architecture obligatoire
- Page WordPress : contient UNIQUEMENT le shortcode [eco3min_chart_xxx] dans un bloc Shortcode ou HTML
- Snippet PHP (Code Snippets, type "Frontend only") : enregistre le shortcode, encapsule HTML + SVG + CSS + JS inline
- Aucun script ou style dans la page WordPress elle-même
Cette séparation est non-négociable : Paul gère tout son JS/CSS via Code Snippets, jamais inline dans les pages WP.

Conventions techniques du snippet
- Préfixe CSS : toutes les classes en eco3-[chartname]- pour éviter les collisions Blocksy
- !important sur toutes les CSS pour overrider les styles thème
- SVG vanilla : pas de Chart.js / D3 / autre dependency, pour vitesse de chargement
- Vanilla JS : pas de jQuery, pas de framework
- IntersectionObserver : animation reveal seulement quand le chart entre dans le viewport
- Mobile responsive : breakpoint à 640px, font-sizes réduits
- Accessibilité : tabindex, role="graphics-symbol", aria-label sur chaque rect

Les 3 vues obligatoires
Tout chart interactif doit proposer minimum 3 vues toggle :
- Default : la vue principale (équivalent du chart Reddit)
- Breakdown #1 : décomposition par catégorie principale (par entreprise, par pays, par secteur, etc.)
- Breakdown #2 : décomposition par dimension secondaire (par année, par sous-période, par classe d'actifs, etc.)
Cette interactivité est la seule raison rationnelle pour qu'un viewer Reddit clique vers eco3min. Le chart statique sur Reddit ne peut pas faire les toggles. C'est le hook conversion central.

Référence : le snippet canonique
snippet_capex_interactive.php du cycle AI capex (mai 2026) sert de template de base. Pour chaque nouveau chart, dupliquer et adapter :
- Le nom du shortcode et du data-attribute
- Le tableau de données (PROGRAMS, COMPANIES, etc.)
- Les fonctions buildRows() pour les 3 vues
- Le X_MAX et X_TICKS
- Les couleurs des segments breakdown


ÉTAPE 4-BIS — Killer phrase visuelle intégrée dans le chart

Distincte du Backlink Hook (défini dans le skill production-research-study). Apprentissage cycle 7 mai 2026.

Pourquoi cette étape existe
Au-delà du Backlink Hook (phrase citable ≤25 mots dans l'article HTML, destinée aux re-shares journalistes), produire pour chaque cycle une KILLER PHRASE VISUELLE intégrée dans le chart comme banner cream/sand discret entre subtitle et chart body. Objectif : maximiser les cross-platform shares (Twitter, LinkedIn) où l'image partagée contient déjà sa phrase virale, sans nécessiter de clic vers l'article.

Distinction fonctionnelle entre les trois hooks

| Élément | Emplacement | Objectif | Audience |
| :-- | :-- | :-- | :-- |
| Backlink Hook | Article HTML, phrase citable ≤25 mots | Re-shares journalistes, citations médias | Médias, journalistes |
| Killer phrase visuelle | Banner cream/sand dans le chart PNG | Cross-platform shares (Twitter, LinkedIn) | Lecteurs hors-Reddit, partage natif |
| Title Reddit | Submission Reddit, ≤140 chars | Clic depuis le feed Reddit | Reddit DIB users |

Les trois hooks sont complémentaires et non redondants. Le chart partagé sur X sans légende doit raconter une histoire avec le killer phrase ; le lien Eco3min partagé doit promettre du value-add via le Backlink Hook ; le post Reddit doit faire cliquer via le title.

Caractéristiques d'une bonne killer phrase visuelle
- Énonce un arbitrage concret universel (cycle 7 : "1 année de college = wage-time de 40 TVs en 2025 vs 3.3 TVs en 1985")
- Ratio mathématique vérifiable et recalculable depuis le dataset
- ≤25 mots maximum
- Couleur dominante = navy, accent burgundy (#A23F2E) sur les chiffres clés
- Banner sand (#F2EAD8) avec bordure cream (#E5DFD3), padding modeste
- Position : entre subtitle et chart body, ou sous le titre du chart selon le layout

Quand NE PAS produire de killer phrase visuelle
Si le sujet ne permet pas une killer phrase factuelle vérifiable, ne pas en inventer une. Mieux vaut un chart sans banner qu'une phrase fausse, prétentieuse, ou qui drift vers Bloomberg op-ed. Exemple de phrase à éviter : "An absolutely insane shift in American cost of living" (suggestif, non vérifiable, drift identitaire).

Audit obligatoire de la killer phrase visuelle
À inclure dans fact_check_audit.md (cf. ÉTAPE 2-BIS) :
- Maths recalculée en Python visible (3 checks minimum) : ratio antérieur, ratio postérieur, multiplicateur
- Présence vérifiée dans HTML article + PNG chart desktop + PHP snippet (3 endroits, cohérence stricte)
- Cohérence numérique avec le dataset principal et les Key Findings de l'article
Si l'un de ces 3 checks échoue → 🔴 résiduel → blocage de la livraison Reddit pack.


ÉTAPE 5 — Le titre Reddit

DEUX TITRES DISTINCTS, DEUX FONCTIONS — À NE JAMAIS CONFONDRE (bloquant)

Un cycle produit **deux** titres. Ils ne s'écrivent pas selon les mêmes règles, et
une critique de l'un ne s'applique pas à l'autre. La confusion est facile parce
que les deux se disent « le titre » ; elle coûte soit un titre de chart
sensationnaliste, soit un titre de soumission redondant.

| | **Titre du chart** | **Titre de la soumission Reddit** |
| :-- | :-- | :-- |
| Où il vit | dans le PNG, en Source Serif 4 gras navy, en haut à gauche | dans le champ titre de r/dataisbeautiful |
| Qui le lit | celui qui regarde déjà l'image | celui qui scrolle le feed et n'a pas encore vu l'image |
| Longueur | 4-6 mots utiles | 100-150 caractères |
| Ce qu'il porte | ce que le graphique montre, rien de plus | le sujet **et le cadrage** : période, périmètre, unité |
| Période, plage de dates | **non** — elle est dans le sous-titre du chart | **oui**, elle fait partie du travail du titre (pattern 8) |
| Registre | descriptif analytique, aucun verbe d'intensité | descriptif, aucun verdict, aucun teaser |
| Ce qui le régit | ÉTAPE 3 (règles de design) + ANTI-PATTERNS « Sur le chart » | cette étape + ÉTAPE 2-TER (test règle 7) + ANTI-PATTERNS « Sur le titre Reddit » |

Conséquences pratiques :

- **Ne pas recopier la plage de dates du titre de soumission dans le titre du
  chart** : le sous-titre du chart la porte déjà, et le doublon mange la largeur
  utile du canvas. Inversement, l'omettre dans la soumission prive le lecteur du
  feed du seul cadrage dont il dispose.
- **Un retour du type « ton titre est trop institutionnel, mets plutôt
  [formulation accrocheuse] » doit d'abord être requalifié** : parle-t-il du chart
  ou de la soumission ? S'il parle du chart, la réponse est presque toujours non,
  le titre du chart reste plat. S'il parle de la soumission, la reformulation se
  teste contre le test règle 7 DIB de l'ÉTAPE 2-TER avant d'être retenue.
- **Les adjectifs d'intensité sont interdits dans les deux**, et pour deux raisons
  différentes : identité éditoriale côté chart, risque de suppression par les
  modérateurs côté soumission. Un mot comme « exploded » échoue aux deux titres.
- Le pre-review d'identité (ÉTAPE 2-TER) audite **les deux lignes séparément** :
  « Title chart » et « Titre Reddit » sont deux des cinq éléments, pas un seul.

Apprentissage cycle 20 : une relecture externe a proposé « US customs refunds
exploded in 2026 » pour remplacer le titre du chart, puis, en repli, d'y ajouter
la plage « 2015-2026 ». Les deux propositions visaient en réalité la soumission.
Le titre du chart est resté descriptif et sans dates ; la période est partie dans
le titre Reddit, où elle avait sa place.

Format obligatoire
- [OC] en début (Original Content tag, mandatory)
- 100-150 caractères idéal (max 300)
- Inclut un anchor concret (chiffre, période, nom propre) qui donne envie de regarder
- N'inclut PAS le verdict de la comparaison (pas de "X is more than Y", pas de ratio exact)
- Pas de mots faibles ("biggest", "huge", "shocking", "amazing", "you won't believe")
- Pas d'emoji

9 patterns de titre observés sur top performers DIB (>10k upvotes)
Issus de l'analyse des 15 charts économiques DIB qui ont dépassé 10k upvotes. À utiliser en rotation selon le sujet.

Pattern 1 — CONDITIONAL HOOK : "If you exclude X, [counterintuitive claim]"
Setup d'un fait counterintuitif. Excellente compatibilité zone 3 (macro politique descriptif).
Référence : "If you exclude healthcare employment, the U.S. has lost jobs since 2024"

Pattern 2 — SUPERLATIF TEMPOREL : "The X-est Y in [period]"
Anchor d'unicité historique. Compatible zone 1, 2 ou 3.
Références : "The longest government shutdown in US history" ; "The US dollar is on track for its worst year in modern history"

Pattern 3 — COMPARISON EXPLICITE : "X vs Y [period]"
Promesse de jugement visuel direct. Compatible zone 2 (NVIDIA vs Pharma) ou zone 3 (gerrymandering).
Références : "NVIDIA valuation vs Big Pharma" ; "Neutral Districts vs. 2025 Gerrymandered Districts in Texas" ; "U.S. Total Fertility Rate by State 2007 vs 2025"

Pattern 4 — METHODOLOGY HOOK : "I analyzed N years of X" / "X by Y"
Crédibilise l'OP, signale du travail. Compatible zone 1 ou 2.
Références : "I analyzed 15 years of comments on r/relationship_advice" ; "The Fed's Eternal Struggle: Jobs vs Prices, Chair by Chair"

Pattern 5 — REAL-TIME / EVENT-DRIVEN : "X reacting in real time to Y"
Urgence + actualité, parfait pour cycles event-driven. Compatible zone 3 (Fed meeting, BLS release, Trump address).
Référence : "Oil prices reacting in real time to Trump's National Address"

Pattern 6 — NARRATIVE VERB ASCENDANT/DESCENDANT : "X keeps Ying Z" / "X reduced Y across Z"
Histoire avec direction. Sweet spot zone 2.
Références : "Solar Electricity keeps beating Predictions" ; "Vaccines reduced measles cases across US states"

Pattern 7 — DESCRIPTIVE + SUSPENSE : titre neutre mais le viewer veut voir la réponse
Question implicite ("laquelle est la plus haute ?"). Compatible zone 3 si vocabulaire neutre.
Références : "Politically Motivated Murders in the US by Ideology of Perpetrator" ; "The Generational Gap in the U.S. Congress" ; "The US Government's Budget Last Year, In One Chart (FY2024)"

Pattern 8 — TITRE PUREMENT DESCRIPTIF DIB-SAFE (révisé après removal cycle 7 mai 2026)
⚠️ CHANGEMENT MAJEUR : la structure "X did Y. Z did not." que j'avais initialement classée Eco3min-aligned a été removed par la mod team r/dataisbeautiful au cycle 7 (Purchasing Power), à T+2h après 741 upvotes, 89% ratio, 382k vues. Motif : violation de la règle 7 du sub ("Post titles must describe the data plainly without using sensationalized headlines"). Le pattern paraissait sobre par contraste avec "Stuff got cheaper" mais reste un teaser implicite ("The same is not true for six other items" lu comme listicle promise).
Conséquence : la structure "X did Y. Z did not." est désormais formellement INTERDITE pour les cycles DIB.
Pattern 8 révisé : titre purement descriptif du contenu visuel, sans aucun setup narratif.
Pattern type : [OC] [Métrique] for [N items], [Period A] vs [Period B] (encoding optionnel)
Exemples conformes :
- ✅ [OC] Hours of US median wage-time required to buy six everyday items, 1985 vs 2025
- ✅ [OC] Wage-time cost of six US household items, 1985 vs 2025 (log scale, in hours)
- ✅ [OC] What one hour of US median work bought in 1985 vs 2025: six items on a log scale
Le test décisif : le titre ne doit promettre AUCUNE découverte, AUCUN contraste teasé, AUCUNE référence à un nombre d'items non explicité. Si le titre fait scroll-stop par sa formulation (au-delà du sujet lui-même), c'est un teaser et il sera removed.
Patterns formellement BANNIS pour DIB (cf. ANTI-PATTERNS section) :
- "X did Y. Z did not." ou variantes
- "The same is not true for [N] other items"
- "Here's how X compares to Y, Z, and W"
- Tout titre contenant une promesse non explicitée
Référence cycle 7 cas d'échec documenté : "[OC] A Big Mac required 11 minutes of US median work in 1986. It still does in 2025. The same is not true for six other items." — 137 chars, factuellement vrai, REMOVED par mods DIB T+2h pour règle 7. Trajectoire pré-removal : 741 upvotes, 89% ratio, 166 commentaires, 382k vues, "2e publication la plus populaire de tous les temps" du compte. Perte de viralité estimée : 5,000-15,000 upvotes finaux. Conversion eco3min préservée : ~1,500-4,000 sessions Reddit→eco3min capturées avant removal.

Pattern 9 — DURÉE D'ATTENTE / RÉCUPÉRATION : "It took X N years to do Y" / "Y for N consecutive years/months" / "X stood unbroken for N years"
Le hook temporel contient sa propre tension narrative (durée longue + verbe de résolution) sans nécessiter un chiffre de magnitude. À privilégier sur le hook de magnitude pure ("$X trillion") quand la donnée le permet — observation empirique : à zone et qualité de chart égales, hook temporel out-performe magnitude de 50-100% en upvotes et 5-10x en partages.
Référence : "It took gold 45 years to surpass its 1980 inflation-adjusted peak" (cycle mai 2026, 390 upvotes / 96% ratio / 163% ratio shares-upvotes).

Anti-patterns titre confirmés (présents dans 0 des 15 top performers analysés)
- Pas d'emoji dans le titre
- Pas de "shocking" / "crazy" / "insane" / "you won't believe"
- Pas de titre sous forme de question pure ("Did you know that...?")
- Pas de titre qui commence par un chiffre précis ($X trillion...)
- Pas de superlatif marketing ("biggest ever", "massive", "huge")

Trois variantes systématiques
Toujours proposer trois variantes au choix avant publication, idéalement chacune sur un pattern différent :
Option A — Anchor number + descriptive (généralement le meilleur compromis)
[OC] $1.1 trillion in 24 months: How Big Tech AI capex stacks up against Apollo, Marshall Plan, and Manhattan Project
Option B — Pure descriptif sans chiffre (plus safe, moins viral)
[OC] Big Tech AI capex (2025–2026) vs America's three biggest 20th-century mega-projects, in 2025 dollars
Option C — Question pure (highest CTR, plus risqué côté mods)
[OC] How does Big Tech's 2025–2026 AI capex compare to Apollo + Marshall Plan + Manhattan Project combined?
Recommander A par défaut sauf si le sujet appelle clairement B ou C.


ÉTAPE 5-BIS — Règles de non-prise de parti pour la ZONE 3 (BLOQUANTES)

S'applique UNIQUEMENT aux cycles zone 3 (macro politique descriptif). Pour zones 1 et 2, ces règles ne sont pas pertinentes (mais le bon sens éditorial s'applique de toute façon).
Cinq règles à appliquer systématiquement. Si un de ces critères ne peut pas être respecté pour un topic donné, le topic n'est pas faisable en zone 3 et doit être abandonné ou reframé en zone 1 ou 2.

Règle 1 — Vocabulaire neutre uniquement dans le chart
Adjectifs autorisés : large, significant, sharp, sustained, concentrated, abrupt, persistent, marginal, broad.
Adjectifs INTERDITS dans le chart et dans le titre Reddit : devastating, alarming, terrible, great, shocking, unprecedented (sauf si factuellement le premier jamais — alors on dit "first since YYYY", pas "unprecedented").
Exemple correct : "If you exclude healthcare employment, the U.S. has lost jobs since 2024" (descriptif, neutre).
Exemple incorrect : "DEVASTATING: U.S. employment has COLLAPSED outside healthcare since 2024" (éditorialisant).

Règle 2 — Deux lectures présentées explicitement dans le top comment OP
Format obligatoire à insérer dans le top comment Reddit (cf. ÉTAPE 6 sur la structure du comment) :
"Some read this as [interpretation favorable to one side]. Others read this as [interpretation favorable to the other side]. The data points to one of these more clearly than the other — curious how this sub interprets it."
Pas d'affirmation éditoriale dans le commentaire Eco3min. Le débat naît du choix du viewer. L'OP est neutre, le sub se polarise tout seul.

Règle 3 — Sources primaires bipartisanes ou gouvernementales uniquement
Sources autorisées en zone 3 : BLS, BEA, Fed, Treasury, CBO, Penn Wharton Budget Model, Tax Policy Center, Tax Foundation, OECD, IMF, BIS, World Bank, FRED, sec.gov, Cato Institute (centre-droit libéral non-partisan strict), Brookings (centre).
Sources INTERDITES pour cycles zone 3 : Politico, Axios (penchent éditorialement), Fox News, MSNBC, ThinkProgress, Heritage Foundation, Center for American Progress, ou tout think-tank explicitement partisan dans l'identité politique américaine.
Une source primaire institutionnelle est presque inattaquable comme "biased". C'est le bouclier principal.

Règle 4 — Question ouverte finale qui force la divergence
Format à utiliser en fin de top comment OP :
- "Is this more like [historical case A] or [historical case B]?"
- "Does the data here argue for [framework X] or [framework Y]?"
- "Curious how this sub interprets the gap between [observation 1] and [observation 2]."
Le viewer doit choisir un côté — c'est ça qui crée les commentaires. Mais c'est lui qui choisit, pas l'OP.

Règle 5 — Jamais d'attribution causale dans le chart
Le chart montre une corrélation temporelle ("après le bill Y, X a fait Z" / "depuis 2024, X a évolué de N%").
Le chart ne dit JAMAIS "le bill Y a causé Z" ou "Trump a fait Z" ou "Biden a fait Z".
Le viewer fait l'inférence causale lui-même en lisant le chart. C'est la différence fondamentale entre journalisme économique (autorisé, AMF-safe, FT-style) et commentaire éditorial (interdit pour Eco3min).

Conséquence pour les réponses Reddit en zone 3
En phase active T+0 à T+30min sur DIB, l'OP doit répondre uniquement aux questions méthodologiques (sources, calculs, périodes, définitions). Si un commentateur essaie de faire prendre parti à l'OP ("So you're saying Biden's economy is failing, right?"), redirect systématique vers les données :
"The data comes from [source]. Readers can interpret as they see fit — I don't take a position on the policy debate."
Pour le silence post-T+1h : strict, comme pour les autres zones (cf. ÉTAPE 8).


NON-PRISE DE PARTI ÉLARGIE AUX TOPICS À FACTIONS (TRANSVERSE AUX ZONES)

Les 5 règles de non-prise de parti définies pour la zone 3 (politique) s'appliquent aussi aux topics zone 1 et zone 2 quand le sujet implique des factions actives, indépendamment de la dimension politique stricte.

Topics à factions identifiés :
- Or, métaux précieux (goldbugs vs gold bears)
- Immobilier (propriétaires vs locataires)
- Retraite, démographie (générations)
- Bitcoin / crypto (maximalistes vs no-coiners)
- Énergie nucléaire / renouvelables (factions énergétiques)
- USD comme monnaie de réserve (dollarization vs de-dollarization narrative)

Sur ces topics, appliquer systématiquement :
1. Vocabulaire neutre dans le chart (règle 1 zone 3)
2. Reformulation chronologique des objections narratives (cf. cycle Gold mai 2026 : "fear trade" reframé via timing breach Feb 2025 vs US-Iran Feb 2026)
3. Sources primaires uniquement (WGC, BIS, IMF, FRED, BLS — pas de think-tanks à agenda)
4. Question ouverte finale qui invite au débat sans le résoudre
5. Pas d'attribution causale dans le chart

Indicateur de réussite : ratio upvote DIB > 94% (vs médiane DIB 88-92%). Le ratio Gold de 96% sur un topic à factions actives (cycle mai 2026) est le bench à viser sur les cycles similaires. Un ratio < 90% sur un topic à factions = signal que les règles n'ont pas été appliquées rigoureusement et que le post a basculé en débat partisan goldbug-vs-bear / propriétaire-vs-locataire / etc.

En réponses sur un topic à factions : ne jamais prendre parti ni défendre une lecture factionnelle ; répondre uniquement aux questions méthodologiques (sources, calculs, périodes) ; rediriger vers les données ("the data comes from [source], readers interpret as they see fit"). Ignorer complètement les termes drapeau idéologiques (de-dollarization, fiat collapse, fear trade, money printer, late-stage capitalism) — ni valider, ni contredire, reformuler chronologiquement le fait factuel sous le terme.


ÉTAPE 6 — Le top comment OP

Pourquoi le comment est l'élément central
Sur DIB, le ratio post→comment est typiquement de 1-3 % en chart auto-suffisant, 5-12 % en chart avec curiosity gap. Le comment est la SEULE porte d'entrée vers eco3min. Toute la conversion se joue ici.

Structure obligatoire (validée sur cycle AI capex mai 2026)
[Ligne 1 — HOOK INTERPRETATIF FORT, jamais méta-commentaire]
"There are only a handful of moments in modern US history where capital has been mobilized at this scale — and only one of them is entirely private-sector."

[Ligne blanche]

[Bullets des chiffres clés, scannable en 5 secondes]
All figures inflation-adjusted to 2025 USD using BLS CPI:
- Manhattan Project (1942–46): $36B
- Marshall Plan (1948–52): $137B
- Apollo Program (1960–73): $189B
- Combined total: $362B
- Big Tech AI capex (2025–26): $1,123B = 3.1× the combined total

[Ligne blanche]

[Détails sources nommées + breakdown par sous-catégorie]
The four hyperscalers driving this: Amazon ($332B), Microsoft ($308B)... Sources: Q4 2025 10-Ks for actuals, Q1 2026 earnings calls (Apr 29-30, 2026) for guidance.

[Ligne blanche]

[HOOK INTELLECTUEL #2 + PROMESSE INTERACTIVE + LIEN]
I built an interactive version on eco3min where you can toggle the [primary metric] bar to see [breakdown #1] or [breakdown #2] — useful if you want to see [specific value-add]. The closest historical analogue at comparable scale is [comparison X] (~$Y in 2025 USD): [structural similarity], very different [outcome dimension].

https://eco3min.fr/[slug]/?utm_source=reddit&utm_medium=social&utm_campaign=dib_[topic]

[Ligne blanche]

[Tools + sources]
Tools: Python (matplotlib). Sources: [list]. Happy to answer methodology questions.

[Ligne blanche]

[QUESTION OUVERTE FINALE qui force la réflexion + suggère qu'une réponse est dans les données]
Honest open question for the sub: is this [phenomenon X] more like [historical case A] or like [historical case B]? The data points to one of these reads more clearly than the other — curious how this sub interprets it.

Règles non-négociables
- URL nue : jamais [click here](url). Le redditer doit voir l'URL en clair pour faire confiance.
- UTM tracking obligatoire : ?utm_source=reddit&utm_medium=social&utm_campaign=dib_[topic]. Sans UTM, Clarity ne peut pas attribuer le trafic Reddit (Reddit casse souvent le referrer).
- Lien APRÈS la valeur : ligne 9-10 du comment, jamais ligne 1-3. Si le lien arrive trop tôt, perçu comme marketing → scroll past.
- Tools obligatoires : règle DIB, mods rejettent les posts [OC] sans mention des outils.
- Sources nommées et vérifiables : 10-K date, série FRED, document gov spécifique. Anti-troll de premier niveau.
- Question ouverte AMF-safe : "is this more like X or Y?" jamais "should investors do Z?"

Le hook intellectuel #2 = la promesse interactive
C'est la phrase qui justifie le clic. Format obligatoire :
"The interactive version on eco3min lets you [verbe d'action 1], [verbe d'action 2], or [verbe d'action 3]"
Verbes d'action concrets que la version interactive permet et que le chart Reddit ne permet pas :
- "toggle individual companies on/off"
- "switch between annual and cumulative view"
- "compare nominal vs inflation-adjusted"
- "see the per-company breakdown"
- "filter by region/sector/year"
Si la version interactive n'a pas au moins 2 fonctions concrètes que le static n'a pas, le hook est faible et il faut renforcer le snippet avant le post.


ÉTAPE 7 — Anticipation des objections (les 5 OBJECTIONS standards)

Pour chaque chart, pré-écrire 5 réponses aux objections probables. Avoir ces réponses prêtes en clipboard pour publication T+5 à T+30min après le post.
Templates récurrents par type de chart :
- Objection "apples to oranges" : structurel, public vs privé, nominal vs réel, etc.
- Objection "the number is wrong / outdated" : citer source primaire avec date exacte
- Objection "context is missing" : GDP-share, per-capita, run-rate, etc.
- Objection "your inflation method is BS" : justifier le choix CPI / autre deflator
- Objection "you're cherry-picking the period" : montrer que la conclusion tient sur des fenêtres alternatives
Les réponses doivent toujours :
- Reconnaître le point quand il est légitime ("Fair point — they're structurally different")
- Donner la source précise pour défendre le chiffre
- Ne JAMAIS s'énerver, JAMAIS rétorquer agressif
- Glisser un détail spécifique du dataset eco3min ("included in the dataset linked above") pour redriver vers le site


ÉTAPE 8 — Séquence de publication T+0 à T+48h

JOUR DE PUBLICATION — DÉPEND DE LA ZONE (BLOQUANT)

- **Zones 1 et 2** : mardi, 15h00 Paris / 09h00 ET. C'est le créneau par
  défaut ; toutes les heures ci-dessous s'y réfèrent.
- **Zone 3 (macro politique)** : **jeudi uniquement**, même heure. Un contenu
  zone 3 posté le mardi s'expose à une suppression par les
  modérateurs — constaté au cycle 8, post supprimé. Le mardi
  concentre le trafic politique du sub et la vigilance des mods ; le jeudi est
  nettement plus tolérant sur le même contenu.

Un topic zone 3 qui ne peut pas attendre le jeudi n'est pas publié en zone 3 :
soit il est reframe en zone 1 ou 2, soit il glisse à la semaine suivante.

RÈGLES DURES DE RÉPONSE (TOUTES ZONES)

- **Aucun em-dash** dans le moindre contenu public, réponses Reddit
  comprises. C'est la signature de détection IA la plus lue par les
  redditeurs.
- **Les liens ne vont que dans les self-replies**, jamais dans une réponse
  directe à un commentateur : un lien en réponse directe se lit comme du
  push marketing.
- **Trois réponses OP maximum par thread.** Au-delà, l'OP a l'air de
  défendre son post.

T-1h (mardi 14h00 Paris — jeudi 14h00 en zone 3)
Vérifications pré-vol :
- Page eco3min teste OK en navigation privée mobile (load < 3s)
- Shortcode [eco3min_chart_xxx] rend correctement les 3 vues
- Bouton CSV download fonctionne
- Mailpoet form / opt-in newsletter visible
- UTM dans le lien Reddit
- Clarity events configurés (csv_download_click, newsletter_subscribe)
- Top comment chargé en presse-papiers
- 5 réponses objections chargées dans un fichier texte ouvert

T+0 (mardi 15h00 Paris / 09h00 ET)
Upload sur r/dataisbeautiful en mode Image :
- GIF si animation justifiée (cf. ÉTAPE 3)
- Sinon PNG static seul
Heure exacte : préférer 14h57, 15h02 plutôt que 15h00 pile (évite la collision avec les push automatiques de bots). Titre option A. Submit.

T+30 secondes
Coller le top comment immédiatement. Reddit boost les posts où l'OP commente vite.

T+0 à T+30 minutes — PHASE ACTIVE (haute valeur, fenêtre algo critique)
C'est la fenêtre où l'OP doit être le plus actif. L'algo Reddit boost les posts où l'OP répond rapidement aux premiers commentaires.
- Répondre dans les 5 minutes à toute question méthodologique
- Réponses substantives (3-6 phrases), source précise citée
- Glisser naturellement la mention de la version interactive eco3min
- Upvoter discrètement les commentaires substantiels (même critiques) — montre du good-faith engagement aux mods

T+30 min à T+1h — PHASE TRANSITION (cadence ralentie)
Fenêtre algo critique se ferme. Le risque AI-detection augmente avec chaque réponse formelle.
- Espacer les réponses de 10-15 minutes minimum
- Dégrader visiblement le format : pas de bullets systématiques, pas de "Important distinction", pas de question retournée à chaque fois
- Réécrire en mots à soi avant de coller : ajouter contractions ("yeah", "imo", "fwiw"), langage parlé, tolérer fautes mineures
- Réponses plus courtes (2-3 phrases au lieu de 4-6)
- Calibration de longueur par phase : T+0-30min, réponses 60-120 mots max ; T+30min-1h, 40-80 mots ; T+1h+, single-liner ou skip. Densité décroissante = signal d'OP confiant qui n'a plus à défendre.

T+1h à T+24h — PHASE PASSIVE (silence sauf urgence)
L'OP qui revient répondre 1h+ plus tard à des commentaires non-upvotés ressemble à du content scheduling. Ne pas répondre, sauf :
- Commentaire avec >5 upvotes (signal que ce sub-thread vit)
- Fact-check sérieux qui pourrait te discréditer (ex: "this number is wrong, here's the correct figure from [source]") — tu as 15 min pour corriger sinon le mauvais chiffre devient le narratif
- Question d'un défenseur spontané (entretenir l'allié)
EN ZONE 3 spécifiquement : NE JAMAIS prendre parti dans les commentaires ni défendre une lecture politique, même après T+1h. Si un commentateur essaie de te faire prendre parti, redirect systématique vers les données : "the data comes from [source], readers interpret as they see fit". NE PAS répondre aux critiques de format ou aux trolls de préférence — c'est un signal pour le cycle suivant, pas une discussion à avoir en thread.
Pour tout le reste : silence. Les défenseurs spontanés (MasterKoolT, Individual_Ice_6825 type) prennent le relais. Si un troll ou une affirmation fausse passe, un autre redditer la contredira (le sub a 22M membres).

T+1h
Si le post prend (>50 upvotes) : poster le PNG static sur X (thread 3 tweets), LinkedIn (1 paragraphe).

T+2 heures
Check Microsoft Clarity. Filter utm_source=reddit. Si <50 sessions alors que le post a >5k vues → tracking probablement cassé, debug.

T+24h
Cross-share sur r/economics avec framing macro différent (pas le même titre). Délai obligatoire 6 semaines minimum entre deux posts Reddit sur eco3min direct, donc utiliser le lien GitHub si le délai r/economics n'est pas écoulé.

T+48h
Si le post a fait >5k upvotes et a été cité dans des comments / sub-threads sérieux : pitch FT Alphaville par email direct. Jamais tagging public. Jamais sans la traction Reddit en evidence.


ÉTAPE 9 — Mesure et itération

KPI cibles par zone (calibrés selon la répartition 20/50/30)
Les cibles varient selon la zone du cycle. Un post à 213 upvotes en zone 1 (macro pure neutre) n'est pas un échec si la conversion eco3min est dans la cible. Le même score en zone 3 (macro politique) signale un problème de format ou de sélection.

Zone 1 — Macro pure neutre (~10 cycles/an)
| Métrique | Cible basse | Cible haute |
| :-- | :-- | :-- |
| Vues Reddit | 5k | 30k |
| Upvotes | 200 | 2,000 |
| Upvote ratio | 92% | 98% |
| Sessions Clarity utm=reddit | 50 | 500 |
| Téléchargements CSV | 10 | 100 |
| Newsletter signups | 2 | 20 |
Mesure principale : conversion eco3min + SEO long-tail. Pas la viralité Reddit.

Zone 2 — Macro pure + narrative dramatique (~25 cycles/an, MOTEUR PRINCIPAL)
| Métrique | Cible basse | Cible haute |
| :-- | :-- | :-- |
| Vues Reddit | 30k | 150k |
| Upvotes | 3,000 | 10,000 |
| Upvote ratio | 92% | 98% |
| Sessions Clarity utm=reddit | 200 | 1,500 |
| Téléchargements CSV | 30 | 300 |
| Newsletter signups | 5 | 50 |
Mesure principale : upvotes + conversion eco3min.

Zone 3 — Macro politique descriptif (~15 cycles/an)
| Métrique | Cible basse | Cible haute |
| :-- | :-- | :-- |
| Vues Reddit | 100k | 500k |
| Upvotes | 10,000 | 50,000 |
| Upvote ratio | 88% | 96% (plus polarisant donc ratio plus bas attendu) |
| Sessions Clarity utm=reddit | 500 | 3,000 |
| Téléchargements CSV | 100 | 800 |
| Newsletter signups | 20 | 150 |
Mesure principale : upvotes massifs + conversion + débat lancé dans les commentaires.

Métriques agrégées sur 50 cycles/an
- Upvotes moyen pondéré par cycle : 5,000-15,000
- Newsletter signups cumulés fin 2026 : 1,500-4,000
- CSV downloads cumulés fin 2026 : 5,000-15,000
- Ratio shares/upvotes médian : > 50%
- Ratio upvotes médian : > 92%

KPI TRANSVERSE — RATIO SHARES / UPVOTES
Sur tous les cycles, surveiller le ratio "partages Reddit / upvotes". Cette métrique mesure la "shareability" hors-DIB et est un meilleur prédicteur du SEO long-tail et de la conversion eco3min que les upvotes seuls.
Indicatif :
- Ratio < 20% : sujet purement DIB-niche, faible portée hors-canal
- Ratio 20-50% : sujet correct, viralité standard
- Ratio 50-100% : bon sujet à portée out-of-DIB (groupes finance, threads X, Slack)
- Ratio > 100% : sujet exceptionnel à portée culturelle large
- Ratio > 150% : top decile (référence : Gold 45 years cycle mai 2026, 163%)
Observation empirique : les topics à fort ancrage cognitif (cf. section dédiée) ont historiquement des ratios shares/upvotes > 80%. Les topics à faible ancrage plafonnent typiquement à 20-40%. Le ratio shares/upvotes est donc une métrique d'auto-correction du planning annuel : si plusieurs cycles consécutifs affichent un ratio < 30%, c'est un signal pour pivoter le mix topic vers du plus ancré.

KPI TRANSVERSE — RATIO UPVOTES
Surveiller systématiquement le ratio upvotes Reddit (% d'upvotes vs total votes). Indicatif :
- Ratio < 88% : zone risque DIB, signale soit un topic clivant mal géré, soit une critique de format pas adressée
- Ratio 88-92% : médiane DIB, performance correcte
- Ratio 92-95% : signal de discipline éditoriale fonctionnelle
- Ratio > 95% : excellent, top quintile DIB (référence : Gold cycle mai 2026, 96%)
Sur les topics à factions (cf. section "Non-prise de parti élargie"), viser ratio > 94%. Un ratio < 90% sur un topic à factions = échec d'application des règles non-prise de parti.

Signaux temps-réel pendant le post (utiles pour décisions in-flight)
- Ratio vues→upvotes à T+30 min : >0.5% = excellent, 0.2-0.5% = correct, <0.2% = le chart ne convertit pas. Si <0.2% à 30 min : ne pas insister à pousser via cross-post agressif, le post va plafonner.
- Ratio comments/upvotes : >20% = engagement très fort, le sujet polarise (bon pour traction). 5-15% = engagement normal. <5% = post passif, peu de débat.
- Vitesse première heure : si <50 upvotes à T+1h, frontpage DIB improbable. Si >150 à T+1h, frontpage probable, intensifier monitoring.

Décisions automatiques selon résultats
- Si vues post < cible basse de la zone → revoir le titre + sujet pour cycle suivant
- Si ratio post→comment < 3% → la curiosity gap dans le titre/chart était insuffisante
- Si sessions Clarity < cible basse alors que vues > cible basse → debugger UTM
- Si CSV downloads < cible basse → revoir visibilité bouton above-the-fold
- Si newsletter signups < cible basse → repenser le placement de l'opt-in
- Un post <200 upvotes en zone 2 ou zone 3 signale un problème de format ou de sélection topic — investiguer dans le cycle suivant.
- Un post <100 upvotes en zone 1 reste acceptable si la conversion eco3min est dans la cible — le succès long-terme est cumulatif.


ÉTAPE 9-TER — Token absent du référentiel : le signaler, jamais l'approximer

Le référentiel du tracker (onglet `referentiel`) est la liste fermée des valeurs
autorisées par colonne. Il vit dans le Google Sheet, il est en écriture seule
pour Paul, et il vieillit moins vite que la production : un cycle finit
régulièrement par avoir besoin d'un token qui n'y figure pas encore.

**Règle : ne jamais loger un cycle dans un token approchant.** Un slopegraph
consigné en `line` faute de token `slope`, un hook « première historique »
consigné en `breach_idea_recue` faute de mieux : dans les deux cas la ligne est
acceptée par le sheet, personne ne voit d'erreur, et l'agrégation par
`chart_type` ou par `viral_hook` du dashboard devient fausse pour toujours. Le
coût n'est pas dans le cycle courant, il est dans les décisions que le dashboard
orientera ensuite.

Conduite à tenir, à la livraison de la ligne tabulée T+48h :

1. Utiliser le token le plus proche **et le dire explicitement** dans le message
   qui accompagne la ligne, en nommant la valeur réellement observée.
2. Livrer, à côté de la ligne de cycle, **la ou les lignes à coller dans l'onglet
   `referentiel`** : trois colonnes, `colonne | valeur | définition`. Paul n'a
   qu'à les coller, il n'a rien à rédiger.
3. Répéter la demande à chaque cycle concerné tant que le token manque, et
   **compter les rappels** dans les notes. Un token réclamé trois fois ou plus
   est un défaut de process, pas un oubli : le signaler comme tel.

Ce que la dette de référentiel coûte, mesuré au cycle 20 : sur les 11 valeurs de
`viral_hook` réellement employées dans l'onglet `cycles`, **4 ne figurent pas au
référentiel** — `premiere_historique`, `ancre_familiere`, `hook_generationnel`,
`asymetrie_revisions`. Le tableau « PERFORMANCE PAR VIRAL HOOK » du dashboard ne
les agrège donc pas : il est aveugle à 6 cycles sur 18, dont les trois qui
portent `premiere_historique`, la meilleure moyenne observée du jeu. Le dashboard
ne se trompe pas, il ne voit pas — et c'est pire, parce que rien ne le signale.
Côté `chart_type`, `dumbbell` et `slope` manquent également, et le cycle 18 a été
consigné en `bar_chart_vertical`, un token qui n'existe nulle part.

Le remède n'est pas de deviner un token proche : c'est de livrer les lignes de
référentiel avec la ligne de cycle, à chaque fois, jusqu'à ce qu'elles soient
collées.


ÉTAPE 9-BIS — Suivi cumulatif du bias politique (sur 50 cycles)

S'applique uniquement aux cycles zone 3 (macro politique descriptif).

Pourquoi cette étape existe
Sur 15 cycles zone 3 par an, même si chaque cycle individuel respecte les 5 règles de non-prise de parti (cf. ÉTAPE 5-BIS), le cumul des sujets choisis peut mécaniquement pencher vers un camp politique américain. Si sur 12 mois tous les sujets zone 3 montrent toujours le même côté en faveur d'un camp (par exemple toujours du contenu qui rend mal à Trump, ou toujours pro-immigration, ou toujours anti-Fed), le compte Reddit est marqué comme partisan par la sélection des sujets même si chaque chart individuel est strictement factuel.
Risque concret : ban du sub, perte de goodwill, perception "Eco3min = média de gauche" ou "Eco3min = média de droite".

Procédure de tracking
Le tracking vit dans le Google Sheet « ECO3MIN — CYCLES TRACKER » (23 colonnes, cf. INSTRUCTIONS — section TRACKING). Colonnes utiles au suivi du bias politique :
| Colonne | Contenu |
| :-- | :-- |
| date | YYYY-MM-DD |
| topic | Sujet du cycle |
| zone | 1, 2 ou 3 |
| chart_format | spaghetti / heatmap / small_multiples / sankey / etc. |
| political_lean | D / R / N (UNIQUEMENT pour zone 3) |
| upvotes_final | Score à T+72h |
| csv_downloads | Cumul T+72h |

Règle d'équilibrage
Sur une fenêtre glissante des 20 derniers cycles zone 3, viser un équilibre approximatif. Exemple acceptable : 7D / 7R / 6N.
Seuil d'alerte : si le ratio dépasse 12-3-5 ou 3-12-5 dans un sens ou dans l'autre, forcer activement des cycles zone 3 qui rendent mal au camp sous-représenté pour rééquilibrer.

Définition opérationnelle de "rend mal à un camp"
- D (Democratic-leaning critique) : le fait factuel du chart contredit ou nuance un narratif favorable aux Démocrates (ex: "Healthcare jobs only" sous admin D ; "regulations failed to achieve X" sous admin D).
- R (Republican-leaning critique) : le fait factuel contredit ou nuance un narratif favorable aux Républicains (ex: "Tax cut effects favored top quintile" sous admin R ; "Tariff revenue below projection" sous admin R).
- N (neutral / structural) : le fait est descriptif d'un phénomène économique sans bénéfice partisan clair (ex: "Federal employment composition by administration" couvre les deux camps également).

Garde-fou contre la dérive lente
À chaque proposition de topic zone 3, vérifier explicitement le compteur D/R/N des 20 derniers cycles zone 3 ET formuler dans la justification : "ce cycle ajoute un [D/R/N] au compteur. Compteur actuel : X-Y-Z. Direction : équilibrage / accentuation."
Si la proposition accentue un déséquilibre déjà existant, proposer une alternative ou différer le cycle d'une semaine pour faire un cycle zone 1 ou 2 entretemps.

ÉTAPE 10 — BUNDLE JSON D'EXPORT (PLUGIN WORDPRESS « CHART OF THE WEEK »)

Le plugin « Chart of the Week » ingère un bundle JSON unique par cycle et fait, dans l'ordre : (1) crée/maj le Code Snippet (idempotent par nom, balise <?php de tête retirée, activé), (2) crée/maj les 2 pages EN/FR avec metas RankMath + JSON-LD + image mise en avant, liées en traductions Polylang, (3) insère la carte d'étude en 1re position dans chaque hub et recompte le compteur (les 2 emplacements : valeur accent + ligne « N studies/études »).

**Forme de livraison, selon la taille.** Sous ~15 Ko, la réponse ne contient rien d'autre que le JSON dans un bloc de code. Au-delà — cas normal dès que l'article est complet ; le bundle du cycle 19 faisait 65 Ko — l'écrire dans `chart_of_the_week.json` du dossier du cycle et livrer le fichier, en annonçant sa taille et la raison. **Ne jamais tronquer le JSON pour le faire tenir dans un bloc.**

Schéma (schema_version courant) :
- cycle : { id, date (YYYY-MM-DD), topic }
- snippet : { name (= « Eco3min — <sujet> »), description, scope: "global", shortcode: "[eco3min_chart_xxx]", code }
  → code = le contenu du snippet PHP SANS la balise <?php de tête (Code Snippets l'ajoute lui-même pour le type « php »). Par défaut le snippet est en SVG/JS vanilla sans dépendance (cf. ÉTAPE 4). Si, par dérogation à l'ÉTAPE 4, une bibliothèque externe est utilisée (Chart.js, etc.), elle DOIT être chargée depuis un CDN autorisé par la Content-Security-Policy du site : cdn.jsdelivr.net ou unpkg.com — JAMAIS cdnjs.cloudflare.com (bloqué par la CSP : le graphe ne se rend pas, "Chart is not defined" — bug observé cycle 11).
- pages : { en: {...}, fr: {...} } — chacune :
  - lang ("en"/"fr"), post_type ("page"), status ("draft" par défaut)
  - slug : EN = slug nu servi sous /en/ via Polylang (mode répertoire) ; FR = slug plat à la racine
  - title (= H1 / post_title), content : HTML **classique** complet de l'article, PNG statique inséré AU MILIEU. **ZÉRO commentaire HTML, zéro `<script>`, zéro `ld+json` inline.**
    ⚠️ « Zéro commentaire HTML » inclut les **délimiteurs Gutenberg** `<!-- wp:html -->`. Le `content` part en HTML classique ; les shortcodes s'exécutent exactement pareil. Règle figée août 2026 après l'incident Autoptimize du 27/08 : 8 pages servies en HTTP 500, invisibles pour Google, corps affiché normalement dans le navigateur. Panne silencieuse. Vaut aussi pour les commentaires en tête des cartes hub. Détail dans `eco3min-import-contenu-bilingue`.
  - featured_image : URL complète du PNG = https://eco3min.fr/wp-content/uploads/AAAA/MM/cycle{N}_chart_desktop_16x9.png (STRICTEMENT identique au src de la <figure>, à seo.og_image et à json_ld.image)
  - seo : { title (≤60 car.), description (150-160 car.), focus_keyword, canonical, og_title, og_description, og_image (= featured_image), og_image_alt, robots: ["index","follow"] }
  - json_ld : [ Article, Dataset ] — le champ image de l'Article = la même URL PNG ; le Dataset pointe le CSV téléchargeable
- polylang : { link_translations: true }
- hubs : { en: { post_id: 12664, insert_after: "<div class=\"eco3-grid\">", dedupe_marker, card_html }, fr: { post_id: 12662, insert_after: "<div class=\"eco3-grid\">", dedupe_marker, card_html } }
  → post_id figés : 12664 = Macro Watch (EN), 12662 = Observatoire macro (FR). Carte EN = AVEC lang-note 🇫🇷 vers la page FR ; carte FR = SANS lang-note. dedupe_marker = le href canonique de la carte (anti-doublon au ré-import).

SKILLS À CHARGER AVANT DE CONSTRUIRE LE BUNDLE (les oublier coûte une passe de correction)

- `hub-card-etude` — templates verbatim de `card_html` EN et FR, et leurs pièges : préfixe `en/` sur la featured image côté EN, slug FR plat, lang-note 🇫🇷 sur la carte EN et JAMAIS sur la carte FR, `.eco3-card__media` sur UNE seule ligne (sinon wpautop injecte des `<br>`), ordre strict media → badge → title → desc → sources → lang-note → cta. Ne jamais inventer ce balisage.
- `eco3min-import-contenu-bilingue` — la règle « zéro commentaire HTML » et le contrôle mécanique à exécuter avant de rendre le bundle.

VALIDATION AVANT LIVRAISON

Le bundle est écrit par un **script qui refuse d'écrire si une assertion casse**, jamais assemblé à la main. Le script est versionné dans le dossier du cycle.

Assertions minimales :
- cohérence du nom de PNG et de CSV entre `<figure> src`, `og_image`, `json_ld.image`, `featured_image` et `distribution.contentUrl` ;
- `post_type` = `page` ; post_id des hubs = 12664 (EN) / 12662 (FR) ;
- longueurs SEO (title ≤60, description 150-160) ;
- le code du snippet ne commence pas par `<?php` ;
- zéro commentaire HTML, zéro `<script>`, zéro `ld+json` dans le `content` ;
- PNG statique non adjacent au chart interactif ;
- asymétrie de lang-note respectée ;
- zéro em-dash.

DIVERGENCE DE DOCTRINE NON TRANCHÉE (cycle 19)

`eco3min-import-contenu-bilingue` interdit le champ `json_ld` dans les pages et impose que le snippet porte le JSON-LD en base64 guardé par slug, au motif d'un doublon dans le `<head>`. Mais cette skill se déclare explicitement « sans hubs », donc hors périmètre Chart of the Week. Tant que l'arbitrage n'est pas fait : on suit le schéma ci-dessus (`json_ld` dans les pages) et on vérifie au Preview du plugin qu'il n'y a bien qu'**un seul** bloc JSON-LD dans le `<head>`.

Règles bloquantes du bundle :
- Le nom du PNG dans featured_image, le src de la <figure>, og_image et json_ld.image sont STRICTEMENT identiques et suivent cycle{N}_chart_desktop_16x9.png.
- Le snippet code ne commence JAMAIS par <?php.
- Les post_id des hubs sont 12664 (EN) et 12662 (FR).
- Cohérence des chiffres : les chiffres clés des cartes hub et des pages sont identiques à ceux de l'article et de l'audit (mêmes valeurs au chiffre près).
- Le bundle n'est généré que sur « donne moi le json », jamais spontanément.
- Le `content` des deux pages ne contient AUCUN commentaire HTML, délimiteurs Gutenberg compris.
- `card_html` suit les templates **verbatim** de `hub-card-etude` — ce balisage ne s'invente pas.
- Aucun em-dash nulle part dans le bundle.


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


PROCESS LEARNINGS (META — apprentissages cycle 7 mai 2026)

Multi-iteration design log (à tracker)
Un chart évolue typiquement à travers 4-8 itérations (v1 → vN) avant la version finale livrée. C'est normal et productif. Le tracker (Google Sheet, cf. INSTRUCTIONS — section TRACKING) peut capturer cette itération comme un design log.
Colonne optionnelle à ajouter : iterations_count (nombre de versions PNG produites avant livraison finale). Permet d'apprendre cumulativement :
- Convergence rapide (1-2 iter) = format bien calibré pour le sujet
- Convergence longue (5+ iter) = format qui résiste, parfois sujet mal cadré
- Convergence longue sur >3 cycles consécutifs = signal de drift, soit format Eco3min mal calibré, soit attente esthétique non-explicite
Référence cycle 7 : 7 itérations (small multiples → hybride dumbbell → tweaks textuels → aération → mobile 4:5 → retour 16:9 sur DIB). Productif mais signale qu'une référence externe (Claude Design) a déclenché un re-design partiel — à noter dans notes_succes du tracker.

Réversibilité des décisions stratégiques
Une décision stratégique de format / titre / canal peut être inversée APRÈS construction si un argument nouveau émerge. C'est légitime et même nécessaire.
Principe : ne JAMAIS inverser sur la base de "j'ai un doute". Uniquement sur la base d'un argument explicite que l'on n'avait pas pleinement pesé au moment de la décision initiale. Capturer le raisonnement dans le tracker (champ notes_revision) pour apprentissage cumulatif.
Référence cycle 7 : décision Reddit 4:5 mobile → revue à 16:9 desktop sur la base de 3 arguments nouveaux (culture DIB top performers en 16:9 paysage, les % énormes de la 4:5 dominent et déséquilibrent, conversion eco3min mieux servie par data viz enthusiasts qui examinent vs scrollers casuels).

Hybridation de sources externes (sans copie aveugle)
Sources d'inspiration externes acceptables : Claude Design v0, top performers DIB référencés dans le skill, FT/Economist style guides, Our World in Data, Semafor.
Méthode : extraire séparément (a) ce qui est objectivement supérieur (format, mécanique, encodage, interactivité) et (b) ce qui drift l'identité Eco3min (ton, vocabulaire, framing, palette). Adopter (a), rejeter (b). Ne JAMAIS copier en bloc.
Référence cycle 7 : Claude Design a proposé un dumbbell chart avec titre "Stuff got cheaper. Living got more expensive." → adoption du format dumbbell + interactivité sorting (objectivement supérieurs), rejet du titre éditorial dramatique (drift Eco3min vers op-ed).


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


CAS D'ÉCHEC DOCUMENTÉS (apprentissage cumulatif)

Cette section archive les cycles qui ont échoué par défaut spécifique, pour ne PAS répéter. À mettre à jour à chaque échec significatif. Le coût d'un échec n'est récupéré que si l'apprentissage est cristallisé.

Cycle 7 (mai 2026) — Purchasing Power 1985 vs 2025 — REMOVED par mods DIB règle 7
Trajectoire pré-removal :
- T+0 (mardi 19 mai 09:00 ET) : publication
- T+12 min : 19k vues, 39 upvotes, 84.2% ratio
- T+35 min : 106k vues, 195 upvotes, 85.7% ratio, "5e publication la plus populaire de tous les temps"
- T+2h : 741 upvotes, 89% ratio, 166 commentaires, 382k vues, "2e publication la plus populaire de tous les temps" — REMOVED par mod team r/dataisbeautiful
Motif removal : règle 7 du sub — "Post titles must describe the data plainly without using sensationalized headlines."
Titre incriminé : [OC] A Big Mac required 11 minutes of US median work in 1986. It still does in 2025. The same is not true for six other items. (137 chars, factuellement vrai)
Cause racine : structure narrative à 3 clauses (X did Y / It still does in Z / The same is not true for [N] other items) lue par mod team comme teaser listicle. Le pattern paraissait sobre par contraste avec "Stuff got cheaper" mais reste un teaser implicite.
Perte estimée : 5,000-15,000 upvotes finaux (post en trajectoire frontpage major).
Conversion eco3min préservée : ~1,500-4,000 sessions Reddit→eco3min capturées avant removal (les 382k vues ont vu le link UTM avant suppression du post). Métriques Clarity à confirmer post-événement.
Apprentissages cristallisés :
- Le pattern 8 "X did Y. Z did not." est désormais formellement INTERDIT (cf. ÉTAPE 5 — Pattern 8 révisé)
- Le pre-review identity drift B.5 passe de 4 à 5 éléments avec ajout du test règle 7 DIB (cf. ÉTAPE 2-TER)
- Les anti-patterns titre Reddit listent maintenant explicitement les structures bannies cycle 7
- Heuristique opérationnelle : "Un mod de bonne foi qui voit ce titre dans la queue va-t-il y voir une description plate ou un teaser narratif ?" — si la réponse est ambiguë, reformuler.
Action de récupération réalisée : modmail respectueux envoyé proposant 3 titres descriptifs alternatifs validables. Repost prévu T+24h avec titre validé par mods ou Option descriptive par défaut.
Délai de récupération mod team typique : 6-24h.

Cycle 7 (suite) — REPOST resté en ligne : ratio sous le seuil de risque
- Repost à titre descriptif validé (lendemain du removal), resté en ligne jusqu'au bout.
- 675k vues (record du compte) MAIS 728 upvotes et ratio 83,8% (< seuil risque 88% ; topic à factions affordability, cible >94%).
- Critique #1 du thread, plus upvotée que le post lui-même : log scale (754 + 601 up).
- Cause racine UNIQUE, 3 symptômes : mauvaise métrique affichée — valeur absolue (heures de travail) au lieu de la variation. Absolu → 5 ordres de grandeur → log forcé → log comprime la variation → couleur directionnelle ajoutée pour compenser → collision de légende (2025=rouge mais vert si baisse).
- Fix proposé par le sub lui-même (teddyone, Encorhynchus, dsafklj) : axe Δ%, montants en labels.
- Nuance temporelle : v1 à 89% de ratio à T+2h ; c'est l'exposition prolongée du repost qui a accumulé les critiques et fait tomber le ratio. Le défaut était là dès la v1, le temps l'a révélé.
- Seconde prise factuelle, distincte de l'encodage : un commentateur a relevé que la série était l'AHETPI (Average Hourly Earnings, production & nonsupervisory) — une MOYENNE — présentée comme "median work" dans le titre, là où le median hourly wage OEWS (BLS) ~24,5 $ diffère nettement de l'AHETPI ~31 $. Erreur de label vérifiable sur source officielle. Cette prise est invisible pour le viewer médian (qui ignore AHETPI vs OEWS) et n'explique vraisemblablement PAS le ratio bas — la réception factionnelle du sujet (affordability) le fait. Mais elle est démontable, donc à éliminer pour elle-même : à fort ancrage cognitif, le mot exact (median/average) compte autant que le chiffre.
Apprentissages cristallisés :
1. Q4 (lecture non-trahie) ajouté au test beautiful (ÉTAPE 3-BIS).
2. Format 9 amendé : décision d'encodage absolu-vs-variation AVANT le choix d'échelle.
3. Tell "défendre son échelle en commentaire = échec lecture 2s".
4. Le filtre hybridation Claude Design (PROCESS LEARNINGS) attrape le drift de TON mais a laissé passer le défaut d'ENCODAGE du format adopté → Q4 est le garde-fou manquant.
5. Ne jamais coller "median" sur une série Average (AHE/AHETPI) ni l'inverse : l'audit ligne-par-ligne vérifie désormais que chaque série EST la statistique que son label annonce (cf. ÉTAPE 2-BIS, patterns d'erreur).


Les fichiers de référence du cycle AI capex sont les templates à dupliquer pour chaque nouveau cycle :
- generate_chart_v4.py — script Python statique + GIF (V4 minimaliste)
- snippet_capex_interactive.php — pattern PHP shortcode 3 vues
- article_ai_capex.html — structure article eco3min (à combiner avec production-research-study)
- reddit_launch_v3.md — pack Reddit complet (titre/comment/objections/séquence)
- capex_data.csv — exemple de dataset structuré avec sources
Ces fichiers vivent dans le projet "Eco3min — Chart of the Week" et servent de référence permanente.
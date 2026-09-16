# production-chart-of-the-week — référence : Données, fraîcheur du dataset, audit ligne par ligne, pre-review identité (ÉTAPE 2, 2-BIS, 2-TER, 2-QUATER)

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

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

FRAÎCHEUR DU DATASET (BLOQUANT, apprentissage cycle 21 — précède l'audit ligne par ligne)
Le 🟢 de l'audit se définit comme « recalculé depuis le dataset chargé en session ». Ce n'est une garantie que si le dataset lui-même est frais et reproductible. Au cycle 21, 16 lignes 🟢 reposaient sur un CSV de réserve assemblé à la main deux mois plus tôt : l'OCDE avait publié un millésime de plus (2025) et révisé l'ancien (salaire Mexique −15 %, Corée −10 %, Hongrie −8 %). Le chiffre-titre (77 minutes) était faux contre la source le jour du déploiement.
Règles :
- Le CSV du cycle est produit par un `build_dataset.py` versionné dans le dossier du cycle, qui tire chaque série de sa source par API ou fichier primaire (SDMX OCDE, FRED, etc.). Aucune valeur recopiée d'une session, d'un agrégateur ou d'un ancien cycle.
- Avant l'audit ligne par ligne : interroger la source pour la DERNIÈRE PÉRIODE DISPONIBLE de chaque série et vérifier que le CSV la porte. Un millésime plus récent disponible et non utilisé doit être justifié explicitement dans le CSV et l'article, sinon on bascule dessus.
- Repli sur une série manquante : si une seule série manque pour un pays sur la dernière année (cycle 21 : heures des salariés 2025, Israël), prendre la série voisine de la MÊME année (emploi total), le dire dans la colonne notes du CSV et dans la méthodo de l'article, et chiffrer l'écart. Ne jamais mélanger les années en silence.
- Pièces de RÉSERVE : chaque pièce embarque son `build_dataset.py`. Au déploiement on le relance, on diffe avec le CSV de réserve, et on rejoue l'audit sur le résultat. On ne réaudite jamais des chiffres recopiés : entre l'assemblage et la publication, un millésime sort et l'ancien est révisé.
- TOUS les intrants, pas seulement ceux qui ont une API. Cycle 21, second audit du 15/09 : `build_dataset.py` tirait bien l'OCDE par SDMX, mais les 16 prix Big Mac étaient RECOPIÉS dans le script depuis la livraison de janvier 2026 « parce que le fichier GitHub n'est pas garanti disponible ». The Economist avait publié juillet 2026 : 10 prix sur 16 avaient bougé (Israël +15 %, Canada +6 %, Japon +4 %), deux paires de pays s'inversaient dans le classement, et chaque prix en dollars du top comment était périmé. Règle : un script de dataset ne contient AUCUN nombre de source ; il contient des identifiants (série, fichier, pays) et au plus une DATE de millésime épinglée avec sa raison écrite. `dataset_freshness.py` couvre OCDE, FRED et Economist (`economist_bigmac()`) ; une source sans fetcher se voit ajouter le sien avant le cycle, pas contournée par une copie. Si la source est injoignable le jour J, le script échoue et on le dit ; on ne publie pas sur des valeurs recopiées.


ÉTAPE 2-QUATER — PÉRIMÈTRE DU SET (BLOQUANT, apprentissages cycle 21 et « 10 plus grandes villes »)

Un chart dont la population est un ensemble nommé (« 16 OECD countries », « the 10 largest US cities », « G7 », « every US state », « EU-27 ») est attaqué sur l'ensemble AVANT d'être attaqué sur les chiffres, et l'attaque est imparable parce qu'elle se vérifie sur une liste publique en trente secondes. Deux échecs documentés :
- « 10 plus grandes villes des États-Unis » : deux des dix manquaient. Personne n'avait listé les dix depuis le Census avant de construire ; l'ensemble était « ce que la donnée avait ». Le post a été étrillé sur le choix des villes, pas sur la mesure.
- Cycle 21 : la raison écrite pour exclure le Chili, la Colombie, le Costa Rica et la Turquie (« absents de la série OCDE de salaires en monnaie nationale ») était fausse. Ils y sont ; il leur manque la valeur 2025. L'Islande manquait et n'était nommée nulle part. L'article, l'objection pré-écrite et l'audit portaient tous la même phrase fausse, réfutable sur OECD Data Explorer. Attrapé la veille de la mise en ligne par une question de relecture (« le choix de ces 16 est justifié ? »), pas par le process.

Doctrine : l'ensemble se définit AVANT la donnée, pas à partir d'elle.
1. UNIVERS énuméré depuis la liste faisant autorité (site OCDE, Census, traité, liste officielle), avec URL et date de consultation. Jamais « de mémoire », jamais « les pays que la source a ».
2. RÈGLE d'inclusion en une phrase, applicable membre par membre (« membre OCDE hors euro ayant un prix Big Mac national et une valeur 2025 pour les trois séries »).
3. Chaque membre de l'univers est INCLUS ou EXCLU. Aucun troisième état. Chaque exclusion porte une raison de la liste fermée (`rule` / `no_value_in_source` / `no_value_for_vintage` / `methodology_break` / `other_documented`), la SOURCE où la preuve se lit et le DÉTAIL exact (« dernière valeur TRY : 2024 »). Une raison se VÉRIFIE contre la source le jour où on l'écrit : « la source ne les couvre pas » s'écrit après avoir interrogé la source, pas après l'avoir supposé.
4. RÉCONCILIATION arithmétique : univers = inclus + exclus, et le N du titre = nombre d'inclus. 38 − 17 − 5 = 16, écrit noir sur blanc.
5. Ensemble CLASSÉ (« les N plus grands par X ») : le classement vient de la source du classement, les N premiers sont tous présents, ou bien le titre dit le trou (« 8 of the 10 largest », jamais « the 10 largest » avec deux absents). Un membre du top N qui manque de donnée ne se remplace pas en silence par le N+1.
6. Le manifeste `set_manifest.json` du cycle porte tout cela ; `scripts/set_check.py` le réconcilie et refuse d'écrire le CSV si un membre est dans le vide, si une exclusion est sans preuve, si le compte du titre ne tombe pas juste, ou si un top N est troué sans que la revendication le dise. `build_dataset.py` l'appelle avant `DictWriter`.
7. La rationale publiée (article § « Why these N », FAQ, objection pré-écrite « why not X ») est GÉNÉRÉE depuis le manifeste ou vérifiée contre lui phrase par phrase. La même raison fausse recopiée dans cinq fichiers reste fausse cinq fois.
8. Test final avant livraison, à faire à voix haute : « Un lecteur qui prend la liste officielle et coche mes N : quel nom lui manque, et ma phrase sur ce nom est-elle vraie contre la source aujourd'hui ? »

Piège de lecture : « la source ne couvre pas X » et « la source n'a pas encore X pour l'année de référence » sont deux faits différents, et seul le second justifie une exclusion pour cohérence de millésime. Le premier, faux, se réfute d'un clic ; le second, vrai, est un argument plus fort (Turquie 2024 contre un prix 2026 après 60 % d'inflation = chiffre absurde). La vraie raison est presque toujours meilleure que la raison approximative.


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

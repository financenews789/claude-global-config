# production-chart-of-the-week — référence : Process learnings et cas d'échec documentés (cycles 7, 9, 11, 19, 20, 21, 21 bis, villes US), fichiers de référence

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

PROCESS LEARNINGS (META — apprentissages cycle 7 mai 2026)

Multi-iteration design log (à tracker)
Un chart évolue typiquement à travers 4-8 itérations (v1 → vN) avant la version finale livrée. C'est normal et productif. Le tracker (`eco3min-knowledge/distribution/cotw_cycles.csv`) peut capturer cette itération comme un design log.
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
Une maquette externe (Claude Design, image générée) se ré-exprime dans le script, avec les assertions ; elle ne se copie jamais à l'œil. Ses défauts de rendu (titre cassé sur deux lignes qui écrase le sous-titre, annotation tronquée, footer qui déborde, police hors brand kit) sont précisément ce que les gardes existent pour bloquer. Cycle 21 : adopté liseré de tête, killer phrase en filet, en-têtes alignés sur leurs colonnes, valeurs en mono, bandes claires sous les lignes clés, filet de footer ; rejeté tout le reste.
Sources d'inspiration externes acceptables : Claude Design v0, top performers DIB référencés dans le skill, FT/Economist style guides, Our World in Data, Semafor.
Méthode : extraire séparément (a) ce qui est objectivement supérieur (format, mécanique, encodage, interactivité) et (b) ce qui drift l'identité Eco3min (ton, vocabulaire, framing, palette). Adopter (a), rejeter (b). Ne JAMAIS copier en bloc.
Référence cycle 7 : Claude Design a proposé un dumbbell chart avec titre "Stuff got cheaper. Living got more expensive." → adoption du format dumbbell + interactivité sorting (objectivement supérieurs), rejet du titre éditorial dramatique (drift Eco3min vers op-ed).


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

Cycle 21 (septembre 2026) — Big Mac working time — DATASET DE RÉSERVE PÉRIMÉ ET NON REPRODUCTIBLE, attrapé avant publication
- Pièce de réserve assemblée en juillet 2026 sur OCDE « 2024 », déployée le 15/09. Une question de relecture (« pourquoi 2024 et pas 2026 ? ») a déclenché une requête SDMX au lieu d'une réponse de principe.
- Constat : 2025 disponible pour les trois séries et les 16 pays ; et les salaires « 2024 » du CSV ne correspondaient plus à la série en ligne (Mexique 224 354 vs 264 033 MXN). Le chiffre-titre (77 min) tombait à 62,6 ; le ratio 10,4× à 8,6×. Le récit tenait, le chiffre non.
- Deuxième défaut de la même pièce : une mention « registered with the AMF » fabriquée dans les deux articles, et un `<div>` non fermé.
- Coût évité : un post DIB dont le titre-chiffre est réfutable en deux clics sur OECD Data Explorer, sur un topic à factions.
Apprentissages cristallisés : bloc FRAÎCHEUR DU DATASET (ÉTAPE 2), millésimes sur le chart (ÉTAPE 3), assertions `<div>` / statut réglementaire / jetons périmés (ÉTAPE 10), et la règle de réserve : le dataset se retire à la source par script le jour J.

Cycle 21 bis (15/09/2026) — Big Mac working time — PÉRIMÈTRE DU SET FAUX ET SECOND INTRANT PÉRIMÉ, attrapés la veille par relecture
- Question de relecture : « le choix de ces 16 économies et pas d'autres est justifié ? ». Réponse de principe disponible dans cinq fichiers (article EN/FR, FAQ, objection D, audit §6, script) : « Chili, Colombie, Costa Rica, Turquie absents de la série OCDE de salaires en monnaie nationale ». Requête SDMX : les quatre y sont (CLP, COP, CRC, TRY) ; il leur manque la valeur 2025 (2023 ou 2024). Raison fausse, réfutable en 30 s sur OECD Data Explorer, recopiée cinq fois. L'Islande (pas de McDonald's depuis 2009, absente du fichier Economist) manquait au décompte 38 − 17 − 5 = 16 et n'était nommée nulle part. Le prix « euro area €6.08 » cité dans la FAQ et l'objection D n'existe pas dans le fichier Economist (6.00 en janvier, 6.19 en juillet).
- Même relecture, second constat : `build_dataset.py` tirait l'OCDE par API mais les 16 prix Big Mac étaient recopiés depuis janvier 2026 ; The Economist avait livré juillet 2026 (10 prix sur 16 modifiés, Israël 20 → 23 ILS, classement Norvège/Japon et Pologne/Hongrie inversé, tous les prix en dollars du top comment périmés). La règle FRAÎCHEUR existait depuis le matin même et avait été appliquée à la seule source qui avait déjà un fetcher.
- Précédent non documenté jusqu'ici, même famille : un post « 10 plus grandes villes des États-Unis » auquel il manquait deux des dix ; l'ensemble était « ce que la donnée avait », personne n'avait coché la liste Census. Étrillé sur le périmètre, pas sur la mesure.
- Cause racine commune : l'ensemble et les intrants étaient définis PAR la donnée disponible en session, puis rationalisés après coup. Une rationalisation après coup est une hypothèse non vérifiée qui se lit comme un fait.
Apprentissages cristallisés : ÉTAPE 2-QUATER PÉRIMÈTRE DU SET (manifeste univers / règle / exclusions prouvées / réconciliation / top N, `scripts/set_check.py` appelé par `build_dataset.py`), extension de FRAÎCHEUR à tous les intrants (aucun nombre de source dans un script, `economist_bigmac()` dans `dataset_freshness.py`, source injoignable = pas de publication sur copie), rationale publiée vérifiée phrase par phrase contre le manifeste, test final « quel nom manque au lecteur qui coche la liste officielle ? ».

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

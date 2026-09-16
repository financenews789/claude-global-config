# production-chart-of-the-week — référence : Le chart, test DIB beautiful, 9 formats, ancre familière, killer phrase (ÉTAPE 3, 3-BIS, 4-BIS)

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

ÉTAPE 3 — Le chart (template V4 minimaliste)

Le principe central : 2 secondes de compréhension + question en suspens
Le chart doit être :
- Comprensible en 2 secondes : un utilisateur Reddit qui scroll voit le chart, comprend l'idée principale, upvote ou pas. Si l'idée demande plus de 2 sec à émerger, le chart est mort.
- Avec une question implicite : le chart révèle visuellement un fait frappant (disproportion énorme, ratio inattendu) MAIS ne révèle PAS le verdict chiffré exact. Ce verdict reste réservé au commentaire.
- **Portée nationale = pays nommé.** Dès qu'un cycle porte sur un seul pays, le nom du pays apparaît dans le titre du chart ou dans l'image. Sans lui, la moitié du sub suppose « US » et l'autre moitié conteste — et le débat porte sur le périmètre au lieu de la donnée.
- **Superlatif = vérification de la série.** Tout « largest / highest / only / first / record » se vérifie contre la **définition réelle** de la série sous-jacente, pas contre son nom. Apprentissage cycle 9 : « 20 largest US metros » ≠ indice Case-Shiller 20-City ; les trois commentaires les plus upvotés du thread étaient cette critique, ratio 86,3 %.
- **Millésimes hétérogènes = tous sur le chart.** Quand les intrants n'ont pas la même année (prix janvier 2026, salaires OCDE 2025), le sous-titre les porte tous : « Big Mac prices Jan 2026 · wages, hours and tax OECD 2025 ». Une année seule (« 2026 ») est interdite dès qu'un intrant ne la porte pas ; un adoucisseur type « 2026 snapshot » ne règle rien, il appelle la même question. Prolongement de Q5 : l'objection vit dans l'image, elle s'y neutralise. Apprentissage cycle 21.
- **Pays de l'audience.** Sur une comparaison internationale, le pays d'origine du lectorat (États-Unis, ~75 % du trafic) reçoit un repère TONAL : barre charcoal dans un peloton gris, nom en gras. Jamais une troisième couleur pleine : sur un sub international, une barre US colorée se lit comme du pandering et déclenche les « why is US special » ; les deux couleurs du chart restent aux deux pôles du récit.
- **Pas d'échelle de valeur sur des pays ou des groupes.** Un dégradé vert→rouge, ou toute échelle « bien / mal », appliqué à des pays, générations ou catégories sociales est une prise de parti visuelle, hors palette, et un troisième système de couleur. Trois relectures IA sur trois l'ont proposé au cycle 21 ; refus dans toutes les zones.
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
- Polices : les trois familles du brand kit (Source Serif 4 titre, Inter labels, IBM Plex Mono valeurs et sourcing), chargées depuis `docs/fonts/` du projet et ASSERTÉES rendues (matplotlib retombe sur DejaVu sans un mot). Vérifier aussi la couverture cmap de chaque glyphe par famille : les accents FR et le point médian ne sont pas dans toutes les faces.
- Title fontsize : 30pt, à réduire si l'assertion de débordement le demande. Un titre long ne se met pas à la ligne dans matplotlib, il est rogné au bord du PNG.
- Plot bbox : [0.22, 0.14, 0.74, 0.64] pour aérer haut et bas (éviter chevauchement watermark/x-axis)

QUATRE ASSERTIONS AVANT `savefig` (bloquant) : repli de police, débordement de
canvas, chevauchement des textes d'en-tête, échappement des `$` — plus le garde
ASCII sur le cmap. Code et motif de chacune dans `visuels-eco3min` §7 ter. Les
quatre échecs sont silencieux : le PNG sort, il paraît correct en vignette, et
seule l'assertion les attrape. Ne pas s'en remettre à la relecture visuelle.

NOMMAGE DU FICHIER (BLOQUANT) : le PNG desktop est TOUJOURS nommé cycle{N}_chart_desktop_16x9.png (ex. cycle11_chart_desktop_16x9.png). Ce nom EXACT doit apparaître à l'identique partout : le src de la <figure> dans l'article, seo.og_image, le champ image du JSON-LD, et pages.{en,fr}.featured_image du bundle (cf. ÉTAPE 10). Un nom différent entre le fichier que j'uploade et la référence dans l'article = image 404 (bug observé cycle 11). Le CSV suit la même logique avec son propre nom de fichier, identique entre le fichier uploadé, le lien de téléchargement de l'article et le bundle.
UN PNG PAR LANGUE quand le chart porte du texte traduit (noms de pays, labels, killer phrase) : `cycle{N}_chart_desktop_16x9.png` pour la page EN, `cycle{N}_chart_desktop_16x9_fr.png` pour la page FR, rendus par le même script. L'identité des quatre références (src de la <figure>, og_image, json_ld.image, featured_image) se vérifie PAR PAGE, chacune vers son propre fichier. Le PNG EN reste le seul rendu Reddit / X / LinkedIn.

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

Règle de diversité entre cycles : si un cycle utilise spaghetti focus, les 2-3 suivants doivent utiliser autre chose. Tracker le format utilisé par cycle (colonne `format_chart` de `cotw_cycles.csv`, alerte « format identique 3× » du dashboard) dans le Google Sheet (cf. INSTRUCTIONS — section TRACKING).

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
- Couleur dominante = navy ; s'il faut un accent, le terracotta du brand kit (#B85C3C), jamais une teinte hors palette
- Habillage léger : filet terracotta à gauche et fond sand (#F2EAD8) à faible opacité, ou banner sand bordé cream (#E5DFD3). Le pavé plein et bordé pèse trop en vignette (relecture cycle 21)
- Elle porte l'ARBITRAGE, pas le multiple : « le burger le plus cher du monde est le plus vite gagné : 7,3 min ; Mexique 62,6 min » oui ; « 8,6× » non. Le multiple exact reste au top comment (curiosity gap), c'est ce qui réconcilie cette étape avec l'anti-pattern « pas de ratio sur le chart »
- Position : entre subtitle et chart body, ou sous le titre du chart selon le layout

Quand NE PAS produire de killer phrase visuelle
Si le sujet ne permet pas une killer phrase factuelle vérifiable, ne pas en inventer une. Mieux vaut un chart sans banner qu'une phrase fausse, prétentieuse, ou qui drift vers Bloomberg op-ed. Exemple de phrase à éviter : "An absolutely insane shift in American cost of living" (suggestif, non vérifiable, drift identitaire).

Audit obligatoire de la killer phrase visuelle
À inclure dans fact_check_audit.md (cf. ÉTAPE 2-BIS) :
- Maths recalculée en Python visible (3 checks minimum) : ratio antérieur, ratio postérieur, multiplicateur
- Présence vérifiée dans HTML article + PNG chart desktop + PHP snippet (3 endroits, cohérence stricte)
- Cohérence numérique avec le dataset principal et les Key Findings de l'article
Si l'un de ces 3 checks échoue → 🔴 résiduel → blocage de la livraison Reddit pack.

# production-chart-of-the-week — référence : KPI par zone, référentiel du tracker, suivi du biais politique (ÉTAPE 9, 9-TER, 9-BIS)

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

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

Le référentiel est la liste fermée des valeurs autorisées par colonne. Depuis
le 16/09/2026 il vit dans `~/eco3min/eco3min-knowledge/distribution/referentiel.csv`
(`fichier, colonne, valeur, definition`), et `knowledge.add_cycle` **refuse** un
token qui n'y figure pas — la dette silencieuse du Google Sheet n'est plus
possible. Il vieillit moins vite que la production : un cycle finit
régulièrement par avoir besoin d'un token qui n'y figure pas encore.

**Règle : ne jamais loger un cycle dans un token approchant.** Un slopegraph
consigné en `line` faute de token `slope`, un hook « première historique »
consigné en `breach_idea_recue` faute de mieux : dans les deux cas la ligne est
acceptée par le sheet, personne ne voit d'erreur, et l'agrégation par
`chart_type` ou par `viral_hook` du dashboard devient fausse pour toujours. Le
coût n'est pas dans le cycle courant, il est dans les décisions que le dashboard
orientera ensuite.

Conduite à tenir, au log du cycle à T+48h :

1. `knowledge.add_referentiel('cotw_cycles', colonne, valeur, définition)` —
   la définition est rédigée par Claude, une phrase, dans le style des lignes
   existantes du fichier.
2. Puis `knowledge.add_cycle(...)` avec le token exact. Les deux lignes partent
   dans le même commit.
3. `scripts/check.py` liste les tokens historiques encore « à définir » : en
   compléter un à chaque cycle jusqu'à extinction de la dette.

Ce que la dette de référentiel coûte, mesuré au cycle 20 : sur les 11 valeurs de
`viral_hook` réellement employées dans l'onglet `cycles`, **4 ne figurent pas au
référentiel** — `premiere_historique`, `ancre_familiere`, `hook_generationnel`,
`asymetrie_revisions`. Le tableau « PERFORMANCE PAR VIRAL HOOK » du dashboard ne
les agrège donc pas : il est aveugle à 6 cycles sur 18, dont les trois qui
portent `premiere_historique`, la meilleure moyenne observée du jeu. Le dashboard
ne se trompe pas, il ne voit pas — et c'est pire, parce que rien ne le signale.
Côté `chart_type`, `dumbbell` et `slope` manquent également, et le cycle 18 a été
consigné en `bar_chart_vertical`, un token qui n'existe nulle part.

Le remède n'est pas de deviner un token proche : c'est d'écrire le token au
référentiel avant la ligne de cycle. À la migration du 16/09/2026, ces 7 tokens
(`premiere_historique`, `ancre_familiere`, `hook_generationnel`,
`asymetrie_revisions`, `dumbbell`, `bar_chart_vertical`, `ancrage=moyen`) ont
été ajoutés au référentiel avec la mention « définition à écrire » : le
dashboard les agrège désormais, leur définition reste à compléter.


ÉTAPE 9-BIS — Suivi cumulatif du bias politique (sur 50 cycles)

S'applique uniquement aux cycles zone 3 (macro politique descriptif).

Pourquoi cette étape existe
Sur 15 cycles zone 3 par an, même si chaque cycle individuel respecte les 5 règles de non-prise de parti (cf. ÉTAPE 5-BIS), le cumul des sujets choisis peut mécaniquement pencher vers un camp politique américain. Si sur 12 mois tous les sujets zone 3 montrent toujours le même côté en faveur d'un camp (par exemple toujours du contenu qui rend mal à Trump, ou toujours pro-immigration, ou toujours anti-Fed), le compte Reddit est marqué comme partisan par la sélection des sujets même si chaque chart individuel est strictement factuel.
Risque concret : ban du sub, perte de goodwill, perception "Eco3min = média de gauche" ou "Eco3min = média de droite".

Procédure de tracking
Le tracking vit dans `~/eco3min/eco3min-knowledge/distribution/cotw_cycles.csv` (25 colonnes, ex-Google Sheet « ECO3MIN — CYCLES TRACKER » migré le 16/09/2026) ; `scripts/dashboard.py cotw` imprime le bias zone 3 sur les 20 derniers cycles. Colonnes utiles au suivi du bias politique (noms réels du CSV : `date_publication`, `topic`, `zone`, `format_chart`, `bias_politique`, `upvotes_24h`, `csv_downloads`) :
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

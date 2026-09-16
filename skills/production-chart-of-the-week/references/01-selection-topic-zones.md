# production-chart-of-the-week — référence : Sélection du topic, zones 20/50/30, ancrage cognitif (ÉTAPE 1, 1-BIS)

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

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

---
name: "maillage-orphelins-eco3min"
description: "AMONT du maillage interne Eco3min : choisir QUELLES pages reçoivent des liens entrants, COMBIEN, et DEPUIS QUELLES sources, avant de passer la main au projet C (rédaction des patches). Couvre la définition opératoire d'« orphelin » sur eco3min (in-degree éditorial, hubs à forte sortance exclus), le gate GSC bloquant qui évite de dépenser des patches sur des pages que Google ne sert pas, l'allocation proportionnelle du nombre de liens, l'appariement source→cible sur `snapshot.csv` et `maillage.csv`, le surprovisionnement de l'export « targets manual », et l'extraction programmatique des ancres. Activer sur « maille les orphelines », « pages publiées pas assez maillées », « donne-moi les IDs à exporter », « prépare un lot de patches de maillage », ou après un import de cluster resté isolé. La rédaction des patches est l'AVAL : voir patches-maillage-eco3min. Combiner avec plugins-eco3min et archi-eco3min."
---

Maillage des orphelines Eco3min — phase amont
Quand cette skill s'applique
Quand la sélection des cibles n'est pas déjà tranchée par le conseil de maillage du mega-plugin. Trois cas typiques :

rattrapage d'orphelines et de quasi-orphelines sur l'ensemble du site ;
cluster fraîchement importé, bien maillé en interne, invisible depuis le reste du site ;
pages uncategorized — le conseil du mega ne maille que 4 niveaux (pillar, sub_pillar, major_article, satellite) et ne les voit pas.
Quand le mega a produit des optimizations[], cette skill ne sert pas : la sélection est faite, on passe directement au projet C.

0. Entrées
~/eco3min-projets/context/snapshot.csv — une ligne par page.
~/eco3min-projets/context/maillage.csv — une ligne par lien interne résolu.
MCP gsc — impressions, position, requêtes par URL.
Datez les deux CSV avant de conclure quoi que ce soit. maillage.csv porte sa date de scan en 1re ligne (commentaire #) ; snapshot.csv n'en a pas — sa 1re ligne est l'en-tête, se rabattre sur le mtime du fichier. Annoncez « snapshot du JJ/MM, maillage scanné le JJ/MM ». Un cluster importé après le scan n'existe dans aucun des deux.

Ces fichiers sont gros : grep, jamais de lecture intégrale.

1. Définir la population de cibles
La métrique : in-degree ÉDITORIAL
L'in-degree brut ne veut rien dire sur ce site. Les hubs pointent vers presque tout : qr (~640 liens sortants), qa (~640), research-data (~250), donnees-analyses-macro-financieres (~240), plus observatoire-macro et macro-watch. Une page liée uniquement depuis une grille de cartes de hub n'a aucun lien éditorial entrant, et l'orphelin strict est un ensemble quasi vide (~34 pages, dont les deux tiers de level exclu).

Comptez donc les liens entrants qui satisfont TOUS ces critères :

source_lang == target_lang (un lien cross-lang ne compte pas) ;
source_post_id != target_post_id ;
source dont la sortance totale est ≤ 50 liens (au-delà, c'est un hub ou une page d'index, pas un lien éditorial) ;
source de level différent de exclu.
Les trois populations utiles
Population	Définition	Priorité
Orphelines strictes	0 lien entrant, tous critères confondus	haute
Quasi-orphelines	entrants uniquement depuis hubs / nav / exclu	haute
Cluster isolé	entrants uniquement intra-cluster, 0 externe	haute si récent
Exclusions de cible, toujours
Pages de level exclu (légal, CGV, cookies, briefing, embeds de test) et pages de service (mentions / ils-nous-citent, how-to-cite-eco3min). Elles n'ont pas vocation à recevoir du jus.

2. Gate GSC — BLOQUANT
Le maillage interne redistribue de l'autorité entre pages déjà indexées et déjà positionnées. Il ne crée pas de demande. Trois liens entrants sur une page que Google n'affiche jamais ne produisent rien.

Croisez les cibles avec impressions + position moyenne sur 28 jours et découpez :

Signal GSC	Lecture	Action
Position 8-20, impressions réelles	le maillage est probablement le facteur limitant	prioriser, allouer généreusement
Indexée, position > 30, impressions faibles	le problème est le contenu ou l'intention	1 lien de rattachement au silo, pas plus
0 impression, page ancienne	non servie	ne pas dépenser de patches
0 impression, page publiée < 3 semaines	pas d'historique exploitable	pari assumé, à annoncer explicitement comme tel
Ne sautez pas ce gate au motif que la sélection « paraît » évidente. Optimiser un graphe sans regarder le trafic est l'erreur la plus coûteuse de cette phase : elle consomme des patches, du temps d'audit humain et des insertions dans des articles vivants, pour zéro effet mesurable.

3. Allocation du nombre de liens
Jamais uniforme. Un « 3 par cible » appliqué à tout un lot dilue l'effet sur les pages qui peuvent bouger et le gaspille sur celles qui ne bougeront pas.

Repères, à moduler :

cible prioritaire (position 8-20 avec volume) : 4 à 6 liens ;
cible standard (orpheline avec un peu de demande) : 2 à 3 liens ;
cible de rattachement (0 impression, cluster neuf) : 1 à 2 liens.
Contraintes dures :

une même source porte au plus 2 patches par lot — au-delà, l'article se met à ressembler à une page de liens ;
une même cible ne dépasse pas le cap over-target-cap du projet C ;
chaque paire (source, cible) est unique, et la source ne doit pas déjà lier la cible (vérifier sur le post_content, pas seulement sur maillage.csv qui reflète le dernier scan).
4. Appariement source → cible
Levels de source autorisés
satellite, major_article, sub_pillar, pillar, foundation_article, case_study. Jamais un hub, jamais une page exclu, jamais une page faq ou tool en première intention (structures trop courtes ou trop atypiques).

Méthode
Passe algorithmique : overlap de tokens pondéré IDF sur post_title + rank_math_description + slug + cluster + sub_pilier, même langue, bonus si même cluster, exclusion des sources liant déjà la cible.
Reprise manuelle obligatoire. L'algo sort propre sur les corpus denses et nommés (raffinage, NFP/emploi, électricité, PER/PEA, crypto). Il produit de la bouillie dès que le titre de la cible est court ou abstrait, ou que le sujet n'a pas de corpus voisin. Sur ces cibles-là, cherchez le corpus à la main par grep thématique et acceptez d'allouer moins de liens.
Honnêteté sémantique avant volume. S'il n'existe pas de source dont un paragraphe parle réellement du sujet de la cible, la cible reçoit moins de liens. On ne comble pas un trou avec un rapprochement de silo.
5. Export mega : sur-provisionner à 5 sources par cible
snapshot.csv ne dit rien de la prosodie du contenu. Des pages classées satellite ou dataset sont en réalité des dashboards, des grilles de séries ou des pages de téléchargement sans un seul bloc de prose patchable — invisible avant l'export.

Demandez donc 5 sources candidates par cible, pas 3. L'extracteur élimine les inaptes, on garde les meilleures ancres, et il n'y a pas de second aller-retour d'export à faire.

Livrez la liste des IDs sources en une ligne séparée par des virgules : c'est le format que Paul colle dans le mega. Accompagnez-la du tableau de correspondance source → cible, pour qu'il puisse auditer l'appariement avant de dépenser l'export.

6. Extraction des ancres
Utilisez outils/extract_anchors.py du projet C sur le JSON « targets manual ». Le script applique par code tous les gates structurels et retourne des slices byte-exactes du post_content. Une ancre retapée à la main est la cause racine n°1 des rejets du plugin.

python "outils/extract_anchors.py" export.json --sources 379,887,2131 --max 4
Une source qui ne rend aucun candidat est un skip franc (structure-atypique ou no_anchor), tracé au rapport. Ce n'est pas une invitation à chercher l'ancre à l'œil.

7. Passage de relais
À partir de là, le CLAUDE.md du projet C « Eco3min Maillage Optimizer » fait autorité : sélection de l'emplacement dans le bloc, rédaction contextuelle de l'insertion, interdiction des enrobages-pointeurs, diversité d'ouverture, relecture post-patch, validation programmatique, format de sortie (≤ 20 patches par fichier, séparés par langue).

Pièges connus
Filtrer les encarts, pas les wrappers. Les zones interdites visent les encarts (eco3min-callout, eco3min-warning, eco3-tldr, eco3-qa-*, cartes, nav, CTA). Certaines pages « every-x-record » sont enveloppées dans un wrapper de page (eco3-realrates) : filtrer tout div contenant eco3- neutralise 100 % de leurs paragraphes et fait croire à tort qu'elles sont inexploitables.
maillage.csv reflète le dernier scan, pas l'état live. Un lien posé depuis le scan n'y est pas. Le contrôle anti-doublon se fait sur le post_content de l'export.
Un cluster bilingue fraîchement importé est toujours un faux positif d'orphelin interne : il est bien maillé entre ses propres pages et à zéro lien externe. C'est une cible légitime, mais l'in-degree brut ne le montre pas.
Concepts étrangers sans corpus miroir. Une page FR qui traite un dispositif américain (wash sale, step-up basis, Roth) n'a pas de source FR équivalente : le corpus FR parle d'enveloppes françaises. L'enrobage énonce une analogie de mécanique, jamais une équivalence de dispositif — et ce lot est le premier à auditer si un défaut remonte.
Anti-patterns
Sélectionner sur l'in-degree brut et conclure « le site n'a pas d'orphelines ».
Allouer N liens par cible uniformément.
Construire les ancres depuis le slug, ou depuis le seul target_title quand la cible a un historique GSC exploitable.
Exporter exactement autant de sources que de liens prévus.
Combler un manque de sources pertinentes par un rapprochement de silo
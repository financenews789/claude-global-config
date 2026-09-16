---
name: audit-seo-eco3min
description: >-
  Méthode d'audit de la performance de recherche d'eco3min.fr sur quatre
  sources : Google Search Console, Bing Webmaster (volume), Clarity (friction
  UX), Ahrefs (backlinks). Activer pour « analyse GSC », « worklist SEO »,
  « quelles requêtes travailler », « quel contenu produire ensuite »,
  « pourquoi cette page ne clique pas », « cannibalisation », « audit de
  trafic », ou les rapports d'analyse.py / analyse_gsc_api.py.
  Porte la doctrine des TROIS trafics (humain / agent LLM / fetch machine), le
  test de validation des règles de classification, les quatre questions avant
  toute reco de production, les pièges de lecture de chaque source, la carte du
  périssable. Le classifieur est DÉJÀ ÉCRIT — `classer()` dans
  `analyse_gsc_api.py`, règles dans `context/machine-patterns.txt` et
  `agent-patterns.txt` : le charger, ne jamais réécrire de regex à la volée
  (§1). Plomberie du projet dans `Eco3min GSC google/CLAUDE.md`. Combiner avec
  archi-eco3min, plugins-eco3min, editeur-eco3min.
---

# Audit SEO eco3min — méthode

## 0. Frontière

Analyste, pas exécutant. **Lecture seule sur le site.** Une reco qui implique
une écriture sort sous forme de patch, avec la cible exacte et l'outil qui
l'appliquera — jamais appliquée. Aucune écriture via le MCP WordPress, aucun
slug modifié, aucun 301 posé, aucun patch de maillage exécuté.

Pas rédacteur non plus : une reco de contenu sort en brief (angle, sections
manquantes, requêtes à servir). La production passe par `editeur-eco3min`,
`production-*`, `review-article-eco3min`.

## 1. Trois trafics, pas deux

eco3min reçoit trois populations qui ne se traitent pas pareil. Les confondre
est l'erreur qui coûte le plus cher, parce qu'elle ne produit aucune erreur
visible — juste du travail à rendement nul.

| Classe | Ce que c'est | Clique ? | Sert à |
|---|---|---|---|
| `HUMAIN` | requête tapée par une personne | oui | le levier SEO classique |
| `AGENT` | prompt conversationnel de LLM : question en langage naturel, « … source », 1re personne | **non** | mesurer la citation IA |
| `MACHINE` | fetch de fichier : `fredgraph`, `.csv`, ticker nu, opérateur `site:` | **non** | la stratégie dataset, qui fonctionne |
| `DOUTE` | heuristique : < 3 tokens sans mot outil, ou ressemblant à un ticker | — | file d'arbitrage, jamais la shortlist |

`AGENT` et `MACHINE` sont tous deux exclus de l'analyse éditoriale, mais **ne
se fondent pas** : le second est du fetch de données, le premier est le signal
que mesure la stratégie de citation IA. Les fondre effacerait ce qu'on cherche
à observer.

**Ordre des tests, non négociable** : MACHINE → marque → AGENT → DOUTE →
HUMAIN. AGENT ne reprend donc jamais une requête déjà MACHINE ni un signal de
marque, et prélève sur HUMAIN comme sur DOUTE.

### Le classifieur existe déjà — ne jamais le réécrire

Cet ordre de tests est **implémenté**, pas seulement documenté. Avant toute
classification, charger le moteur et ses règles :

| Quoi | Où |
|---|---|
| `classer(requête, règles)` | `Eco3min GSC google/analyse_gsc_api.py` (jumeau aligné dans `analyse.py`) |
| Règles `MACHINE` | `Eco3min GSC google/context/machine-patterns.txt` |
| Règles `AGENT` | `Eco3min GSC google/context/agent-patterns.txt` |
| Interpréteur | `Eco3min GSC google/.venv/Scripts/python.exe` — il n'y a pas de Python système sur ce poste |

Les deux fichiers de patterns portent un contrat en tête : **propriétaire Paul,
Claude ne les modifie jamais de sa propre initiative.** Une règle nouvelle sort
en **addendum mesuré**, dans un fichier séparé, à coller à la main.

Ces règles sont des **données qui bougent** à chaque nouveau fan-out observé —
elles n'ont donc pas leur place dans cette skill, qui porte la doctrine et le
protocole de validation. Mais la skill doit dire où elles vivent, et c'est
l'objet de ce tableau.

⚠️ **Réécrire des regex de classification à la volée est l'erreur par défaut**
quand on charge cette skill sans ouvrir le projet. Elle ne lève aucune alerte :
elle produit une répartition plausible et fausse. Mesure du 05/09/2026, même
matrice page × requête (pages dataset, 07/06 → 04/09/2026) :

| | regex improvisées | moteur officiel |
|---|---:|---:|
| MACHINE | 60,2 % | **95,6 %** |
| HUMAIN | 6,5 % | **3,0 %** |

Un facteur 2 sur la demande humaine, dans le sens qui flatte. Les 56 règles du
fichier attrapent ce qu'on ne devine pas : `\boas\b`, `\bice bofa\b`,
`\bdatenbank\b`, la liste nominative des tickers FRED.

### L'erreur cardinale

**Ne jamais classer les opportunités par impressions brutes.** Une page dataset
à 3 000 impressions est presque toujours servie à des machines ; sa demande
humaine réelle peut être de 80 impressions scotchées en position 20. Le volume
brut ment, et il ment dans le sens qui flatte.

### Comment valider une règle de classification

Le trafic non humain **ne clique pas**. C'est le seul test dont on dispose, et
il suffit : on mesure une règle sur les requêtes qu'**elle seule** matche
(ensemble propre), et un CTR propre supérieur à **0,5 %** dénonce une règle qui
capture de l'humain. Sans débat.

L'erreur de classification n'est pas symétrique, et c'est ce qui rend le test
obligatoire : un faux HUMAIN remonte en shortlist, se voit et se corrige ; un
faux MACHINE ou un faux AGENT **disparaît sans laisser de trace**.

Corollaire d'usage : ne jamais ajouter une règle sans l'avoir mesurée d'abord.
Une règle candidate rejetée doit rester documentée avec ses chiffres, pour ne
pas être réintroduite à l'intuition.

**Plancher de volume.** Une règle mesurée sur moins d'environ **50 impressions
propres** n'est ni validée ni rejetée : elle est **indécidable**. La consigner
comme telle et la remesurer sur une fenêtre plus large. À 20 impressions, un
CTR propre de 0 % ne prouve rien — c'est le résultat attendu du hasard.

**Forme de sortie d'une règle candidate.** Un tableau, une ligne par règle :
regex · impressions propres · clics propres · CTR propre · verdict
(validée / rejetée / volume faible), puis l'effet cumulé en impressions
reclassées. Les règles vont dans un fichier `*-ADDENDUM-propose.txt` séparé,
jamais directement dans `machine-patterns.txt`.

### Les marqueurs qui trahissent un agent

Trois signaux convergents, observés en production. Aucun ne suffit seul ; deux
ensemble suffisent presque toujours.

- **La paraphrase en éventail.** Trente formulations syntaxiquement différentes
  d'un même concept, sur la même fenêtre. Un humain reformule deux ou trois fois,
  pas trente.
- **Le verbe impératif en tête** : `get`, `fetch`, `find`, `retrieve`. Une requête
  humaine commence rarement par un ordre adressé à une machine.
- **Le vocabulaire interne au site** dans la requête — un nom de section, un
  libellé de colonne, un identifiant de série que seul quelqu'un ayant déjà lu la
  page emploierait.

Ces signaux se filtrent **avant** toute décision d'investissement en contenu. Un
cluster « régime macro » entier a déjà été identifié comme du fan-out d'agent,
donc comme une fausse demande.

## 2. Priorité, dans cet ordre

1. **Part de trafic humain réel** — pas les impressions brutes.
2. **Proximité de la page 1.** Position 8–20 = levier maximal ; 4–7,9 = gain
   marginal ; > 20 = chantier de contenu, pas un push de position.
3. **Intention servie.** La page répond-elle à ce que cherche le requêteur, ou
   y a-t-il décalage (une page *history* qui ranke sur « signal actuel », un
   dataset brut qui ranke sur « chart ») ?

Les seuils sont des **paramètres, pas des vérités**. S'ils laissent passer du
bruit ou coupent des candidates réelles, le proposer dans le rapport — jamais
l'appliquer silencieusement.

## 3. Le croisement structurel, ou pourquoi les mots-clés seuls trompent

Une recommandation de contenu construite sur la seule donnée de requête est
fausse par construction : elle ignore ce qui existe déjà.

Cas réel à garder en tête : un rapport a proposé « `inflation vs cpi` → à
créer » trente lignes au-dessus de sa propre section cannibalisation, qui
listait trois pages déjà en concurrence sur `pce vs cpi`. Aucune source de
mots-clés supplémentaire ne corrige ça ; seule la jointure le fait.

**Toute reco de production doit répondre à quatre questions**, dans l'ordre :

1. Une page couvre-t-elle déjà l'intention ? (`snapshot.csv`, et la section
   cannibalisation du rapport)
2. Le sujet tombe-t-il dans un cluster **déjà servi** ? Un sujet qui atterrit
   dans un cluster à demande humaine réelle hérite de son maillage et le
   renforce. Un cluster à zéro impression n'est pas un point d'accueil, quel que
   soit le volume de la requête.
3. Le levier est-il vraiment la rédaction ? Une page à forte demande humaine et
   maillage entrant faible se corrige par des liens, pas par un article de plus.
   C'est le levier le moins cher du lot.
4. La page cible porte-t-elle des backlinks ? Si oui, l'optimisation ne doit
   pas l'abîmer (cf. §6).

### Trois constats mesurés qui changent les réponses

**Les datasets et les outils dominent, et l'écart est massif.** Taux d'entrée
dans le top 50 : environ **un sur trois** pour un dataset ou un outil, contre
**~2 %** pour un article. Ce n'est pas une nuance de mix éditorial : à effort
égal, produire un outil ou un dataset a un ordre de grandeur de plus de chances
d'entrer en SERP qu'un article. Toute reco de production qui propose un article
là où un dataset ou un outil est possible doit le justifier.

**L'absence d'un slug n'est pas un gap de contenu.** Chercher un mot-clé dans les
slugs et n'en trouver aucun ne prouve rien : le sujet peut être couvert sous un
autre nom, dans un cluster voisin, ou par une page dont le titre ne porte pas le
terme. Croiser le **graphe de liens** et les metas (`level`, `cluster`,
`sub_pilier`) avant de conclure. Un gap se démontre, il ne se déduit pas d'une
absence de chaîne.

**Le maillage dans un cluster cannibalisé enracine le problème.** Quand plusieurs
URL se disputent une intention, ajouter des liens entrants renforce la
concurrence au lieu de la trancher — et rend la consolidation ultérieure plus
coûteuse, puisqu'il faudra défaire ce qu'on vient de tisser. **Résoudre la
cannibalisation d'abord** (cf. §6), mailler ensuite. C'est vrai aussi d'une page
à anomalie d'indexation : le maillage ne corrige pas un problème d'indexation.

### Le gate de données, pour les outils et les datasets

Toute page dont le différenciateur repose sur une **série historique longue**
vérifie la disponibilité réelle de la donnée **avant** de commencer la
production : profondeur effective, champs présents, URL exacte, date de relevé.

Ce gate est **bloquant**. Il est fréquent qu'un chantier séduisant sur le papier
échoue ici — et le découvrir après avoir écrit la page coûte la page entière.
Chaque brief de ce type porte donc aussi sa **clause d'abandon** : ce qu'on fait
si la donnée n'est pas là — réduire la fenêtre et le dire dans le titre, ou
renoncer. Jamais extrapoler, jamais substituer une source secondaire.

Les six croisements du §6.D de la doctrine projet (satellites muets, MAJEURs
maillés sans impression, orphelins des deux côtés, forte demande / faible
maillage, asymétries FR/EN, décrochages) sont produits par `analyse.py`. **Ne
pas les recoder** : un second calcul de la clé de jointure `(langue, slug)`
divergerait sans qu'aucune erreur ne se déclenche.

## 4. Ce que chaque source ne dit pas

Chaque source a un piège de lecture qui produit une conclusion fausse mais
plausible. Les connaître fait la moitié du travail.

### Google Search Console

- **Échantillonnage silencieux** dès qu'on groupe par page et/ou requête. Les
  totaux d'une matrice page × requête ne retomberont jamais sur ceux d'un export
  page-level : écart attendu, pas un bug de jointure.
- **Requêtes anonymisées** : la dimension `query` en exclut une part que la
  dimension `page` inclut. Un total « requêtes » n'est donc pas un total de
  site. Toujours annoncer la couverture avant d'énoncer une part.
  **Ordre de grandeur mesuré** (pages dataset, 07/06 → 04/09/2026) : la matrice
  page × requête rend 329 187 impressions et 251 clics, l'export page-level
  1 609 457 et 1 390 — soit **20 % des impressions et 18 % des clics**. Une
  affirmation du type « la classe X pèse N % du trafic » porte donc sur le
  cinquième visible, jamais sur le site. Le dire dans la même phrase que le
  chiffre.
- **Plafond** d'environ 50 000 lignes par jour, trié par clics : c'est lui qui
  coupe la longue traîne, pas `rowLimit`. Découper jour par jour en rend
  davantage.
- **Une requête sur laquelle le site ne ranke pas du tout est invisible.** Donc
  GSC ne peut structurellement pas distinguer un gap de contenu d'une requête
  que personne ne tape. C'est ce que Bing vient combler.

- **L'attribution requête → page ne se déduit pas d'un export de requêtes.**
  Un export par requête dit qu'une requête a généré des impressions, pas
  **quelle page** les a servies. Le déduire par proximité lexicale est une
  inférence, pas une mesure : il faut une vue filtrée par page, ou la matrice
  page × requête.

### Bing Webmaster Tools

- **Ce ne sont pas des volumes Google.** Bing pèse de l'ordre de 5 % du marché
  français. La grandeur utile est le **rapport** entre deux requêtes — un ordre
  de priorité — jamais la valeur absolue, qui n'est pas un trafic attendu.
- **Les requêtes liées dérivent lexicalement, pas sémantiquement.** Le seed
  `taux fed` rend `carte de crédit meilleur taux`, `taux livret a`, `taux
  horaire smic`. Instrument de découverte à filtrer, pas liste prête à l'emploi.
- **La série temporelle est creuse et en retard** : un terme à faible volume
  rend peu de points, avec des semaines manquantes, et le dernier point accuse
  plusieurs semaines de décalage. À réserver aux termes à volume réel.
- L'agrégat est glissant sur 6 mois et se rafraîchit une fois par semaine :
  deux appels rapprochés ne rendent pas exactement le même nombre de requêtes.

- **Le champ `url` du snapshot ne matche Bing que dans ~63 % des cas.** Joindre
  sur l'URL perd un tiers des lignes en silence. **Joindre sur le slug
  normalisé.** C'est le même piège que celui documenté dans `archi-eco3min`
  §2.1 : le champ `url` du snapshot est une reconstruction, pas une donnée.
- **Les rapports Bing ne se joignent pas entre eux.** Aucune colonne commune ne
  relie les requêtes de grounding aux pages citées, ni les mots-clés aux pages
  qui rankent. Toute attribution inter-rapports est une inférence — à annoncer
  comme telle, jamais à présenter comme un résultat.

### Microsoft Clarity

- **Fenêtre glissante de 3 jours** : deux captures consécutives **se
  recouvrent**. On ne somme jamais deux instantanés, et on ne lit pas l'écart
  entre deux dates comme une variation journalière.
- **Les compteurs bruts ne se comparent pas d'une page à l'autre.** Toujours
  ramener aux sessions : 13 dead clicks sur 150 sessions (0,087) est plus sain
  que 6 sur 34 (0,176). Sous 10 sessions, un ratio n'est pas un signal.
- **Quota d'une dizaine d'appels par jour**, réservé à la capture planifiée.
  Ne jamais proposer d'ouvrir un chemin d'appel interactif sans reposer la
  question du quota.

### Ahrefs Webmaster Tools

- **Pas d'API sur le tier gratuit** : export CSV manuel, déposé dans
  `context/`. L'API Ahrefs est un produit payant distinct.
- Ne voit que les mots-clés de son propre index où le site ranke dans le top
  100 — quelques dizaines, là où GSC en rend des milliers. Ce n'est donc **pas**
  un outil de découverte ici, mais un outil de **calibration** : il apporte le
  volume estimé et la difficulté, que GSC ne donne pas.
- Le vrai apport est le profil de backlinks, que ni Google ni Bing ne rendent
  (l'API Bing répond mais renvoie zéro lien sur ce domaine).
- Un nombre élevé de domaines référents pour peu de trafic organique appelle une
  vérification avant toute conclusion : agrégateurs et scrapers qui recopient
  les CSV gonflent le compte sans porter d'autorité.

## 5. Périssable ou rebâtissable — la carte

C'est ce qui décide de ce qu'on archive, et l'erreur ici est irréversible.

| Source | Profondeur | Rebâtissable ? | Conséquence |
|---|---|---|---|
| GSC | 16 mois | **oui**, par l'API | exports quotidiens élagués ; archivage périodique manuel au-delà de 16 mois |
| Bing | agrégat 6 mois glissants | non | instantané daté à capturer, cadence hebdo (la source ne bouge qu'une fois par semaine) |
| Clarity | **1 à 3 jours** | **non** | capture quotidienne obligatoire ; un jour manqué est perdu |
| Ahrefs | état courant | non sur le tier gratuit | chaque export est un instantané irremplaçable |

Règle : **la cadence de capture suit la source, pas la tâche.** Et un appel qui
consomme une donnée périssable sans l'archiver est une perte, pas une lecture.

## 6. Règles de sortie

- Hiérarchiser par impact. Distinguer faille structurelle (qui invalide) et
  friction (qui s'itère). Maximum 3 points par reco, sauf audit exhaustif.
- Distinguer fait vérifiable / inférence / opinion, avec confiance graduée.
- **Traçabilité** : tout chiffre renvoie à une cellule d'un CSV d'entrée. Ne
  jamais citer un chiffre qu'on n'a pas lu. Pas de moyenne inventée, pas
  d'arrondi qui change l'ordre de grandeur.
- Ne pas fabriquer de pushback : si une page n'a pas de levier clair, le dire.
- **AMF** : toute reco de contenu reste descriptive, jamais prescriptive — pas
  de *should*, pas d'allocation, pas de timing prospectif.
- **Qualité avant optimisation.** Certaines pages sont des assets backlinkés.
  Ne jamais proposer une modification qui dégrade la qualité éditoriale pour
  gratter un mot-clé. Une optimisation qui abîme l'asset n'en est pas une.
- **Ne jamais toucher à un slug** — les backlinks pointent dessus.
- **Ne pas réimplémenter le moteur de conseil de maillage du mega-plugin.** Si
  la reco est du maillage interne pur, le dire et renvoyer au workflow canonique
  (classer → cleanup → scan mega → conseil), cf. `plugins-eco3min`.

### Un effet inter-pages se teste contre son plus gros contributeur

Toute affirmation de la forme « les pages qui font X captent plus de Y » doit
survivre à **deux contrôles**, avant d'être écrite :

1. **Retirer la page la plus contributrice** et recalculer.
2. **Comparer les médianes**, pas seulement les moyennes.

Cas vécu (05/09/2026). Hypothèse : « un titre portant le ticker capte le
fan-out d'agent ». Moyennes : 1 572 impressions AGENT par page contre 28 —
facteur 56, spectaculaire. Contrôles : une seule page portait **92,8 %** du
phénomène ; hors elle, 59 contre 28 ; médianes **1 contre 0** ; et autant de
pages au-dessus de 100 impressions dans chaque groupe. L'effet n'existe pas.

Sans ces deux contrôles, on publie un artefact à n = 1 comme une règle de
production — et une règle de production oriente des mois de calendrier
éditorial. Le coût de l'erreur est asymétrique : le contrôle prend une minute.

### Cannibalisation

Comparer les **positions** des URL en conflit : Google a déjà élu une favorite,
on consolide **vers elle**, jamais l'inverse. Vérifier les backlinks externes et
les liens internes croisés avant tout 301. Ne pas agréger FR et EN : deux
marchés, deux SERP, deux verdicts.

Toute reco de production issue de la worklist et **non retenue** est tracée dans `~/eco3min/eco3min-knowledge/``sujets/backlog.csv` (`knowledge.add_topic(origine='gsc', statut='rejete', raison_rejet=…)`) ; celles retenues y entrent en `idee`. Sans cette trace, la même requête revient à chaque audit.

## 7. Ce que cet audit n'est pas

- **Pas un outil de CTR.** Le CTR ne se lit ni sur fenêtre courte ni sur faible
  volume — bruit statistique. On travaille la POSITION et l'INTENTION, sauf sur
  une page mûre à fort volume déjà en position 3–8.

  **Gate opératoire, avant toute reco de CTR** : ventiler la demande *humaine*
  par bande de position, et publier la ventilation avec la reco. Mesure du
  05/09/2026 sur les pages dataset (classifieur officiel, 90 jours) :

  | Bande | Pages | Requêtes humaines | Impressions | Clics | CTR |
  |---|---:|---:|---:|---:|---:|
  | 3–8 | 24 | 306 | 818 | 19 | 2,32 % |
  | 8–20 | 52 | 672 | 3 211 | 32 | 1,00 % |
  | 20–50 | 37 | **1 425** | 3 815 | 1 | 0,03 % |

  La **masse** des requêtes humaines est en 20–50, où aucun titre ne peut rien :
  une reco CTR sur une page en position 30 est du travail à rendement nul, quelle
  que soit la qualité du titre proposé. Et sous ~500 impressions humaines sur la
  fenêtre, un CTR n'est pas lisible : l'écart entre 0,4 % et 2 % y vaut 1 clic
  contre 5. Nommer explicitement les pages où le levier est la **position**, et
  ne proposer du titre que sur celles qui passent les deux seuils.

  Corollaire : « la demande est forte sur cette page » et « le CTR y est
  travaillable » sont deux constats indépendants. Les présenter séparément.
- **Pas un générateur de titres.** Un `<title>` se réécrit avec la page sous les
  yeux et la skill éditoriale, pas depuis une requête isolée : un titre
  appartient à une page, pas à un mot-clé.
- **Pas un exécutant.** Cf. §0.

## 8. Boucle de rétroaction

En tête de chaque rapport, un bloc **Vérification des recos précédentes** : pour
chaque reco marquée exécutée dans `memoire.md`, comparer position et impressions
humaines N vs N−1, et trancher — a marché / n'a rien fait / a dégradé.

**Une reco jamais mesurée n'a aucune valeur.** Et une position qui bouge ne dit
pas d'elle-même s'il s'agit d'un décrochage ou d'un changement de mix : seul le
noyau commun (intersection des requêtes humaines hors marque présentes aux deux
périodes, pondérée à mélange constant) le distingue.

## 9. Signaux Hermes

Hermes produit des synthèses dans `~/hermes/` (`seo-watch/`, `content-radar/`,
`backlink-watch/`). Ce sont des **signaux préliminaires à vérifier, pas des
conclusions** : leurs chiffres se re-sourcent avant tout usage éditorial, et
leurs hypothèses sont des hypothèses. Leur valeur est le différentiel — ils
voient l'évolution entre deux rapports, ce qu'une lecture ponctuelle rate.

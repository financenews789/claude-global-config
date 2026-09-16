# production-research-study — référence : Acquisition des données, playbook et gate de licence (§23)

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 23. Acquisition des données — playbook

La **légalité et la hiérarchie des sources** restent l'affaire de
`sourcing-donnees-eco3min`, qui fait autorité, et dont l'annexe B porte les
endpoints et leurs pièges. Ce qui suit est ce qui est propre aux études.

- **World Bank Pink Sheet** (matières premières, 1960→, annuel et mensuel,
  gratuit) : curl direct du XLSX depuis `thedocs.worldbank.org`. Si le jeton
  tourne, re-localiser depuis worldbank.org/commodity-markets. Feuilles d'indices
  annuels : **les données commencent ligne 10** ; nominal et réel MUV ; colonnes
  Fertilizers et Precious Metals incluses, plus le déflateur MUV.
- **CPI US** : API World Bank `FP.CPI.TOTL` (1960→T-1, base 2010=100), chaînée
  avec BLS v1 `CUUR0000SA0` pour l'année courante. Bizarreries de BLS v1 :
  **ignore les filtres d'année** (parser par année soi-même), sauter `M13`,
  sauter les valeurs `'-'`. Une moyenne d'année partielle se divulgue comme telle.
- **FRED** : `curl fredgraph.csv?id={ID}` depuis Bash est la route de première
  intention, et elle marche. Testée 7 sources sur 7 en HTTP 200 le 04/09/2026
  (`sourcing-donnees-eco3min`, annexe B), 6 séries sur 6 le 08/09/2026 (étude R1).
  L'ancienne note « peu fiable, coupures d'egress, 403 » portée ici était vraie
  dans son environnement et à sa date ; elle est **retirée** parce que, non datée,
  elle détournait durablement de la route la plus rapide.
  **L'autorité sur les endpoints et leurs replis est `sourcing-donnees-eco3min`,
  annexe B** — ne pas redocumenter les points d'entrée ici, deux sources de vérité
  divergent toujours.
  ⚠️ **Le contrôle de licence est un GATE du Step 0, pas une vérification de fin
  de production.** Il se fait **avant** de mesurer la profondeur d'une série et
  avant d'écrire une ligne, sur **chaque série destinée à une colonne publiée**,
  et sur **chaque intrant** d'un composite — une série dérivée hérite du niveau
  le plus dur de ses intrants. FRED distingue **trois** statuts, pas deux, et ils
  n'ont pas les mêmes conséquences : *public domain: citation requested* → CSV
  CC BY 4.0 possible · *copyrighted: citation required* → publiable avec
  attribution mais **jamais** en CC BY 4.0 · *copyrighted: pre-approval required*
  → **rien** sans accord écrit du détenteur, sur un site commercial. Le détail
  des trois niveaux, la commande de contrôle et la sortie applicable à chacun
  sont dans `sourcing-donnees-eco3min`, section « Cas FRED » — **autorité unique,
  ne pas les redocumenter ici**.
  Deux cas vécus. R1 (08/09/2026) : `USREC` et `M2V` sont « citation required » ;
  la colonne de récession a été reconstruite depuis les pics et creux du NBER,
  avec assertion qu'elle reproduit `USREC` à l'identique. R5 (10/09/2026) : les
  séries ICE BofA sont « pre-approval required », ce qui a **tué l'étude au
  Step 0** — aucun historique, si long soit-il, ne rattrape une licence fermée.
  C'est pour ce second cas que le contrôle remonte du Step 10 au Step 0.
- **FAO FFPI** : classeur en téléchargement direct, CC BY 4.0.
- **Jacks 1850–2025 (XLSX)** : bloqué par captcha à l'automatisation. Le
  demander à la main si une extension centenaire est voulue.
- **yfinance et agrégateurs scrapés : interdits** comme source d'un CSV publié.
  Le footer nomme la **vraie** source des chiffres, jamais un relabel plus
  présentable.

**Règle d'arrêt.** Si une source nécessaire est bloquée : **s'arrêter et demander
les fichiers.** Ne jamais substituer la mémoire du modèle à une récupération
ratée.

---

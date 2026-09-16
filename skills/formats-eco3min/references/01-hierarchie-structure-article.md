# formats-eco3min — référence : Hiérarchie majeur / satellite, pages autoportantes, structure d'un article de cluster (§1, §1.1, §1.2, §1 bis)

Extrait VERBATIM de SKILL.md (découpage du 16/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 1. Hiérarchie article majeur / satellite

Sert à décider de la profondeur et de l'angle, pas à ajouter une contrainte.

| | Article majeur | Article satellite |
|---|---|---|
| **Rôle** | Pose le cadre conceptuel d'un cluster | Creuse un point précis |
| **Ton** | Posé, analytique, pédagogique | Plus angulaire, ciblé |
| **Cible** | "OK, j'ai compris le mécanisme global" | "Oui, mais concrètement dans ce cas ?" |
| **Longueur indicative** | Fourchette du blueprint (défaut 2 500–4 000 ; ancien plafond 3 000 supprimé, juill. 2026) | Fourchette du blueprint (défaut 1 500–2 500) |
| **Blocs étiquetés** | TL;DR + 🧭 Lecture (signatures) + ≤1 autre | TL;DR + 1 encart + synthèse finale |

**Règle anti-cannibalisation** : le majeur ne descend pas dans les détails (réservés aux satellites) ; les satellites ne redéfinissent pas le cadre général (réservé au majeur).

### 1.1 La même hiérarchie s'applique aux pages autoportantes

Le vocabulaire dit « article majeur » et « article satellite » parce qu'il vient
des clusters. Les **pages autoportantes** — celles que produit le pipeline page
bilingue — relèvent des mêmes deux registres :

| Registre | Types de page |
|---|---|
| **MAJEUR** | registre « Every X since Y », étude de recherche, page record, page dataset, time-machine |
| **SATELLITE** | Q&A, page outil / simulateur / calculateur |

Le registre se choisit sur la **nature de la page, pas sur sa longueur**. Une Q&A
dense reste un registre satellite ; un registre « Every X » bref reste un
registre MAJEUR. Les quotas d'encarts du §4 suivent le registre.

### 1.2 Ce qui tombe faute d'objet sur une page autoportante

Ces règles ne sont pas contredites : elles n'ont simplement plus de support.

- **La rotation des modes A/B/C** entre satellites consécutifs (§6) — il n'y a
  pas de série. Les trois modes restent une grille utile pour choisir la
  charpente d'une page isolée ; seule la **contrainte de rotation** disparaît.
- **La variation du type d'encart** par rapport au satellite précédent. Même
  raison.
- **L'unicité des ancres à l'échelle du cluster** (§8) — remplacée par l'unicité
  **dans la page**, plus une vérification dans `maillage.csv` qu'une ancre proche
  ne pointe pas déjà vers la même cible depuis ailleurs sur le site.
- **L'anti-cannibalisation intra-cluster** — remplacée par une
  anti-cannibalisation **site-wide** : l'intention de la page ne doit pas être
  déjà servie par une page vivante du snapshot.
- **Les fourchettes de longueur** (2 500-4 000 et 1 500-2 500 du tableau
  ci-dessus). Elles équilibrent un MAJEUR et ses satellites **à l'intérieur d'un
  cluster** ; une page autoportante n'a pas cet équilibre à tenir. Reprendre ces
  chiffres importerait une contrainte sans objet et ferait écrire pour atteindre
  un nombre.

  **À la place, la longueur s'arbitre page par page et se justifie**, sur quatre
  déterminants dans cet ordre : ce que l'intention exige (une requête qui demande
  un chiffre et sa définition se sert en 400 mots) · la densité de la donnée
  disponible (un registre de 300 lignes porte un corps qu'un registre de 12
  lignes ne porte pas) · le format (une page outil dont le simulateur fait le
  travail n'a pas besoin d'un long texte) · le voisinage (la longueur des pages
  qui servent des intentions comparables, dans le snapshot).

  La longueur est une **conséquence** du contenu, jamais une cible. Ni
  remplissage, ni troncature. Si une skill `production-*` fixe une fourchette
  pour ce type de page, elle prévaut.

  ⚠️ **L'asymétrie EN/FR n'est pas un défaut à corriger** : l'anglais sort
  naturellement 7 à 10 % plus court à contenu équivalent. Ne pas rembourrer l'EN
  pour l'aligner sur le FR.

  ⚠️ Le comptage par `re.sub(r"<[^>]+>", " ", html).split()` **surcompte de 5 à
  8 %** — les nombres français éclatent, les guillemets isolent des tokens.
  L'annoncer comme un comptage regex, jamais comme un nombre de mots réel.


---

## 1 bis. Structure éditoriale d'un article de cluster

Un article de cluster — majeur comme satellite — contient ces cinq éléments,
**sans ordre imposé** :

1. un **fait déclencheur** récent ;
2. une **analyse des mécanismes** ;
3. une **mise en perspective** macro ou historique ;
4. au moins un **scénario alternatif ou risque** ;
5. des **implications concrètes**.

⚠️ « Implications concrètes » = impacts économiques **observables** (ménages,
entreprises, marchés). Jamais des actions à entreprendre : c'est une frontière
AMF, pas une nuance de style.

### La flexibilité est la règle, pas l'exception

Le nombre de sections, leur intitulé et leur ordre sont **libres**. Une section
peut être absente si elle n'apporte rien. Réorganiser l'ordre environ une fois
sur quatre.

Si la borne haute de longueur est atteinte, prioriser dans cet ordre : analyse
centrale, implications concrètes, scénarios. Le reste devient facultatif.

### Variation structurelle — obligatoire

Le risque n'est pas qu'un article soit mal structuré, c'est que **tous les
articles aient la même structure**. Sur un cluster entier, cela se voit.

- Certains articles concluent **sans liste**, par une synthèse rédigée en un ou
  deux paragraphes.
- Certains ne contiennent **aucune liste**.
- D'autres placent leur unique liste dans le **dernier tiers**.
- Alterner les paragraphes courts et un paragraphe long.

Test : si un autre article du site pouvait être reconnu comme « issu du même
modèle » par sa seule structure, réécrire.

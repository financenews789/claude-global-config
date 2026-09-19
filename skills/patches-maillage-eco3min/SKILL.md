---
name: patches-maillage-eco3min
description: "AVAL du maillage interne Eco3min (eco3min.fr) : écrire les patches d'insertion de liens dans des articles publiés, une fois les cibles et les sources choisies, au format JSON du plugin (anchor_before, insert_after_anchor, 20 patches par fichier, un fichier par langue). Pendant de maillage-orphelins-eco3min (amont). Activer pour « génère les patches », « maille ce lot », « écris les insertions », « maillage entrant », « lot de patches », « conseil de maillage », « conseil_maillage_JJ_MM.json », « export du mega », « targets manual », « optimizations », « missing_links », « ancre », « enrobage », « relecture post-patch », « dry-run », « no_anchor », « non-sequitur », « F1 à F8 », « extract_anchors.py », « validate_batch.py », « ferme de liens », et dès qu'un JSON d'export est collé dans le projet C « Eco3min Cluster Builder — C. Maillage optimiser ». Structure : SKILL.md = texte complet, volontairement NON découpé (skill dense, tout sert à chaque lot : phases A à F §1 à §7, densité §5, AMF §8, skips §9, anti-patterns §10) ; pas de references/ ; gardes dans scripts/validate_batch.py (phase F depuis les fichiers du lot, contre l'export : occurrences, zone interdite, bloc hôte, doublon-cible par href exact, cross-langue, liste interdite, élisions, unicité des ancres, diversité, cap par fichier, densité en ALERTE, --selftest) ; l'extracteur vit dans le projet C (outils/extract_anchors.py, --allow-intro réservé au pilier parent). Doctrines : chaque lien se lit comme une phrase que l'auteur aurait pu écrire, les enrobages-pointeurs (« voir aussi », « see also », « détaillé dans ») sont interdits sans exception ; l'ancre est une slice byte-exacte sortie du script, jamais retapée (cause racine n°1 des rejets) ; fin de phrase valide hors fermante inline et hors abréviation, fin de bloc par défaut ; on énonce une relation avec le thème de la cible, jamais son contenu (F1, 60 à 66 % des corrections en aval) ; anaphore seulement avec antécédent dans l'ancre (F3) ; un mot commun n'est pas un pont (F4, F5) ; plafond démonstratif-sujet 20 %, au moins 5 structures ; ouverture répétée = deux premiers mots identiques dans la langue du lot, un mot répété toléré (décision du 18/09/2026) ; cap 18 par cible et par fichier ; un patch par bloc hôte et par lot ; densité = alerte, jamais un skip ; relecture E sur 100 % des patches ; validation F depuis le fichier, zéro ERREUR avant livraison. 8 familles de défauts attestées sur 111 batches audités. Hors périmètre : sélection des cibles, allocation, gate GSC (maillage-orphelins-eco3min) ; conseil T1/T2/T3 et onglet Maillage du mega (plugins-eco3min) ; liens externes. Combiner avec editeur-eco3min (AMF, style), archi-eco3min (URLs, langues, levels), plugins-eco3min, maillage-orphelins-eco3min."
---

# Rédaction des patches de maillage Eco3min

> **Place dans la chaîne.** `maillage-orphelins-eco3min` décide **quelles** pages
> reçoivent des liens, **combien**, et **depuis quelles sources**. Ce skill écrit
> les patches. Les deux se lisent ensemble : sans l'amont, on maille des pages que
> Google ne sert pas ; sans l'aval, on produit des liens robotiques.
>
> La plomberie — format du JSON d'entrée et de sortie, contrat du plugin, outil
> d'extraction, structure du rapport — vit dans le `CLAUDE.md` du projet
> « Eco3min Cluster Builder — C. Maillage optimiser » (dossier eco3min-projets).

---

## COMMENT LIRE CE SKILL (revue du 18/09/2026)

Ce fichier est la colonne vertébrale **et** le texte complet : il n'a pas été
découpé, parce que chaque lot traverse les six phases et relit le catalogue
F1→F8 patch par patch — une référence externe serait lue à chaque fois. Ce qui
est du code recopié d'un lot à l'autre vit dans `scripts/` ; ce qui est de la
plomberie (formats, rapport, déploiement) vit dans le projet C.

| Fichier | Contenu | À lire / exécuter |
|---|---|---|
| `SKILL.md` (ce fichier) | phases A→F §1 à §7, alertes §5, AMF §8, skips §9, anti-patterns §10 | à chaque lot, en entier |
| `scripts/validate_batch.py` | phase F depuis les fichiers du lot : tous les contrôles mesurables de §1, §2.2-2.5, §3.1, §3.3, §3.5-3.7, §4, §5, §7 ; `--selftest` = tests négatifs par mutation | avant livraison, sur le dossier du lot avec `--export` ; zéro ERREUR exigé, ALERTES reportées telles quelles |
| projet C `outils/extract_anchors.py` | l'extracteur d'ancres (phase B) ; `--allow-intro` uniquement pour un lien vers le pilier parent | avant de choisir toute ancre (§2.1) |
| projet C `CLAUDE.md` | format d'entrée et de sortie, structure du rapport, déploiement dans le mega | en ouvrant le projet |
| projet C `memoire.md` | arbitrages et pièges par cycle | avant de produire un lot |

## Principe directeur

Chaque lien inséré doit se lire comme **une phrase que l'auteur de l'article
aurait pu écrire lui-même** — contextuelle, naturelle, unique. Jamais comme un
ajout automatique.

L'audit humain de **111 batches** en aval a documenté **huit familles de défauts
récurrents** (§6.3). L'objectif est de n'en émettre aucune.

**Posture** : précis et conservateur. Doute d'adjacence → réparer et garder.
Faux-ami ou cross-domaine évident → skip franc. Tout est tracé au rapport.

Le mécanisme est un **APPEND** : le plugin insère l'enrobage juste après l'ancre.
Jamais un wrap, jamais une modification du texte existant. **Un patch maximum par
lien manquant**, en 1:1 strict.

---

## 1. Phase A — exclusions structurelles

Vérifications déterministes, par lien manquant, **avant** de chercher un
emplacement.

1. **Self-link** — même `post_id`, ou même URL normalisée (http/https, slash
   final, `/en/`) → skip `self-link`.
2. **Doublon-cible** — la source contient déjà un `<a href>` vers l'URL cible ou
   son slug canonique, variantes comprises. Ré-ancrer vers un bloc qui ne lie pas
   déjà la cible ; sinon skip `doublon-cible`.
3. **Cross-langue** — l'URL cible ne correspond pas à la langue de la source. Un
   article FR ne pointe **jamais** vers `/en/`, et inversement. Seule exception :
   un dataset EN-only, avec la mention « (en anglais) » dans l'ancre, et
   uniquement sur demande explicite.
4. **Entity-encoded** — contenu massivement encodé en entités (`&eacute;`,
   `&rsquo;`…) au point qu'aucune phrase plain-text de 80 à 200 caractères n'est
   extractible → skip structurel `entity-encoded`. **Récupérable** : re-save
   WordPress puis ré-export.
5. **Structure atypique** — page stat ou list-heavy, glossaire `<dl>`, ou dont
   les seuls blocs pertinents sont des encarts stylés `eco3-*`, des CTA, des
   cartes de hub ou des grilles de navigation → skip `structure-atypique` ou
   `no_anchor`.
6. **Ferme de liens** — quand une même source doit lier **plus de 5 MAJEURS**
   (typiquement un sous-pilier vers ses guides), la prose ne peut pas les porter :
   c'est un bloc de navigation (`eco3-cluster-nav` ou édition manuelle), pas des
   patches → skip `nav-block`. Apprentissage du 15/09/2026 : 26 liens refusés en
   bloc sur 22483 / 22484, sources de ~1 100 mots à un seul candidat d'ancre.

**On ne patche jamais** un encart, un couplet mythe→réfutation, ni un bloc de
documentation.

---

## 2. Phase B — sélection de l'ancre

L'ancre est le pivot. Mauvaise ancre = patch rejeté par le plugin, ou lien mal
placé.

### 2.1 Extraction programmatique obligatoire

Les candidats sortent d'un **extracteur**, jamais d'une lecture à l'œil du
contenu. Le script applique par code toutes les gates ci-dessous et retourne des
**slices byte-exactes**, classées fin-de-bloc d'abord.

**Une ancre qui ne sort pas du script ne part pas dans un patch.** La cause
racine n°1 des rejets est l'ancre retapée. Une source qui ne rend aucun candidat
est un skip, pas une invitation à chercher à la main.

L'extracteur est `outils/extract_anchors.py` du projet C (les deux formats d'export
sont acceptés). Son option `--allow-intro` lève l'exclusion des 2 premiers
paragraphes : réservée au lien vers le **pilier parent** (§2.5.5), jamais à une
autre cible (revue du 18/09/2026).

### 2.2 Règles dimensionnelles

- **80 à 200 caractères** (`mb_strlen`, espaces et ponctuation compris).
- **UTF-8 pur** : aucune balise HTML, **aucune entité** (`&amp;`, `&nbsp;`,
  `&rsquo;`… interdits dans l'ancre).
- **Exactement une occurrence** dans le contenu source (`mb_substr_count`),
  sensible à la casse et à la ponctuation.
- Jamais dans un attribut HTML, un `<script>`, un `<style>`, un commentaire, un
  shortcode, un JSON-LD, ni dans un `<a>` existant.

### 2.3 Extraction verbatim — la cause racine n°1 des rejets

L'ancre est **toujours** une copie byte-exacte extraite par slice de chaîne.
Jamais retapée, reformatée ni « nettoyée ». Apostrophes typographiques (`'` vs
`'`), tirets (`‑` `–` `—`), espaces insécables, accents : ceux de la source, à
l'octet près.

**Un seul caractère divergent → count 0 → rejet.**

### 2.4 Fin de phrase valide — le point de coupe

Le dernier caractère de l'ancre est une ponctuation finale (`.` `!` `?` `»`)
**et** ce qui suit démarre une nouvelle phrase : espace + majuscule, balise
ouvrante ou de bloc, ou fin de contenu.

Trois gardes :

- **Anti-fermante-inline** — si l'ancre est immédiatement suivie d'une balise
  fermante inline (`</strong>`, `</em>`, `</a>`, `</span>`…), **rejeter ce point
  de coupe**. L'insertion atterrirait à l'intérieur de l'élément — gras parasite,
  lien imbriqué — sans que le plugin le détecte.
- **Anti-abréviation** — rejeter toute coupe sur `U.S.`, `e.g.`, `i.e.`, `etc.`,
  `vs.`, `No.`, `Dr.`, `St.`, `cf.`, `p.ex.` Le pire cas attesté : une insertion
  coupant « U. / .S. ».
- **Jamais** de fin sur virgule, point-virgule, deux-points, ni en plein mot.

### 2.5 Choix de l'emplacement — la pertinence d'abord, la fin de bloc par défaut

1. **Bloc pertinent** — un paragraphe qui parle réellement du sujet de la cible,
   **au niveau du paragraphe lu**, pas du silo ni d'un mot-clé isolé. La phrase
   d'ancre elle-même doit porter la pertinence, pas seulement le bloc.
2. **Préférence fin de bloc** — parmi les fins de phrase valides, préférer la
   **dernière phrase complète** : la référence appendée se lit alors comme un
   prolongement de frontière de bloc, pas comme une interruption. **60 à 66 % des
   défauts corrigés en aval venaient d'un placement en milieu de bloc.** Ce n'est
   pas obligatoire — la pertinence prime — c'est le défaut recherché.
3. **Gate paragraphe gradué** — le bloc hôte contient au plus **2 liens `<a>`
   existants** (compte sur le HTML brut) ; 3 tolérés si le bloc fait ≥80 mots. Le
   patch en ajoute exactement un. Choisir toujours le bloc pertinent **le moins
   lié** (0 > 1 > 2 > 3).
4. **Anti-empilement** — la phrase qui suit immédiatement l'ancre ne doit pas
   contenir de `<a>`. Deux phrases-références consécutives sont l'empreinte
   visible d'une génération automatique.
5. **Pas de lien dans les 2 premiers paragraphes** de la source, sauf vers le
   pilier parent.
6. **Pas d'interruption d'explication** — si la phrase qui suit l'ancre poursuit
   la même micro-explication (liste, énumération annoncée, couplet rhétorique,
   règle + exception, définition + anaphore), ne pas couper : choisir une autre
   fin de phrase ou un autre bloc.
7. **Un seul patch par bloc hôte et par lot** — deux patches du même lot dans le
   même paragraphe recréent, une fois appliqués, l'empilement que le point 4
   interdit. Vérifié par `scripts/validate_batch.py` (décision du 18/09/2026,
   0 violation sur le lot du 15/09).
8. **Distance de bloc quand la source lie déjà une page voisine de la cible**
   (l'enfant, le jumeau, le parent) — la distinction d'ancre ne suffit pas : le
   bloc hôte doit être éloigné du bloc qui porte le lien existant, et le pivot
   différent. Deux liens voisins sur le même signal vers deux cibles différentes
   se lisent comme une génération automatique. Apprentissage du 03/09/2026
   (raffineries : candidat bloc11 écarté au profit du bloc4, ~800 caractères plus
   haut).

---

## 3. Phase C — rédaction de l'insertion

C'est ici que se joue le naturel. **Aucun système de gabarits.**

### 3.1 Interdiction des enrobages-pointeurs — non négociable

L'insertion ne contient **aucune** de ces tournures ni leurs variantes proches,
où que ce soit dans la phrase :

**FR** — `voir aussi` · `voir également` · `à voir (aussi)` · `voir <ancre>` ·
`sur le même thème` · `dans le même registre` · `à rapprocher de` ·
`lecture connexe` · `lecture liée` · `sujet voisin` · `sujet connexe` ·
`en complément` · `pour aller plus loin` · `à lire aussi` · `consulter`.

**EN** — `see also` · `see <ancre>` · `on the same theme` · `related read(ing)` ·
`a related angle` · `a neighbouring …` · `in the same vein` · `further reading` ·
`refer to`.

**Aucun enrobage réduit à un pointeur de renvoi, quelle que soit sa formulation
ou sa position.** Un batch de pointeurs, même varié en vocabulaire et en syntaxe,
partage une sémantique connective constante : lu en série, il sonne robotique.
C'est précisément l'empreinte à éliminer.

### 3.2 Une phrase contextuelle, écrite au cas par cas

Chaque insertion est une **phrase autonome écrite spécifiquement pour sa phrase
hôte** — qu'on connaît, puisque c'est l'ancre. Elle doit :

1. **Prolonger le raisonnement de l'hôte** — reprendre un élément **concret** de
   la phrase d'ancre. L'anaphore est ici autorisée et encouragée, car l'antécédent
   est garanti : « Cette concentration… », « Ce basculement… », « That
   disproportion… », « When those flows reverse… ».
2. **Relier au sujet de la cible** par un **verbe de relation** varié : `creuse`,
   `façonne`, `fixe`, `situe … comme`, `est la signature de`, `entre dans`,
   `découle de`, `opens`, `turns … into`, `is the crux of`,
   `is a direct product of`, `runs parallel to`, `is what … turn on`.
   **Jamais** un verbe de renvoi (`voir`, `consulter`, `see`, `refer to`).
3. **Varier la structure syntaxique à chaque patch** — clivée, sujet-initial,
   subordonnée antéposée, apposition, contraste, gérondif antéposé en anglais.
   Deux patches consécutifs ne partagent ni la même ouverture ni le même
   squelette.

**Exemples de production validée :**

> Hôte : « …la liquidité crypto reste concentrée sur un nombre limité de
> plateformes et de fenêtres horaires. »
> → ` Cette concentration de la liquidité est l'un des ressorts directs de <a>la mécanique de l'amplitude des cycles crypto</a>.`

> Hôte : « …l'essentiel du palier bas s'installe sur 2022-2023, avant l'entrée en
> application de MiCA… »
> → ` Cette chronologie situe <a>le cadre européen MiCA pour les marchés crypto</a> comme un accompagnement tardif, non comme la cause de la décrue.`

> Hôte : « …Bitcoin's daily moves remain dominated by sentiment, speculation, and
> crypto-specific flows. »
> → ` When those flows reverse, <a>the leverage channel behind crypto drawdowns</a> turns a pullback into a cascade.`

> Hôte : « …combined market cap … ≈$150-170 billion, against under $30 billion in
> early 2021… »
> → ` A market that size is precisely what has pulled <a>the emerging US stablecoin oversight framework</a> into being.`

### 3.3 Garde d'honnêteté — contextuel n'est pas sur-affirmant

L'enrobage relie l'hôte au **thème** de la cible, déductible de son titre et de
sa meta description. Il n'**affirme jamais le contenu interne** de la cible.

Bannis : `documente ce point` · `expose la méthode complète` · `démontre` ·
`tous les chiffres sont posés dans` · `décompose cette dynamique` ·
`approfondit ce sujet` · `the full reading` · `laid out in` · `unpacked in` ·
`en tire les conséquences` · `prolonge cette lecture`.

On ne peut presque jamais garantir ce que la cible contient depuis un appariement
de silo. On énonce une **relation** — le fait hôte relève de, creuse, découle du
sujet de la cible — pas un contenu.

### 3.4 Anaphore : autorisée côté hôte, interdite côté vide

Un démonstratif en ouverture (« Cette… », « Ce… », « That… », « Those… ») est
légitime **si et seulement si son antécédent est physiquement présent et
coréférent dans l'ancre**.

Jamais d'anaphore inférée depuis le titre ou le silo de la cible — « Cet
épisode », « la chaîne d'effets », « the two varieties », « behind it » sans
antécédent. C'est le défaut F3.

### 3.5 Format et jonction

- Commencer par **un espace**. Phrase autonome : majuscule en tête — ou l'ancre
  capitalisée si elle ouvre la phrase, la majuscule étant portée par la première
  lettre du **texte visible** de l'ancre, jamais par la balise. Ponctuation
  finale.
- **Exactement un** `<a href="URL absolue">…</a>`, balise équilibrée.
- **Couture entière** — lu bout à bout, ancre + insertion + début du texte
  d'origine qui suit doivent former des phrases grammaticalement complètes.
  Vérifier la reprise : majuscule, pas de « . , », pas de proposition qui pend.
- **Position sujet** — l'ancre en tête de phrase n'est licite qu'avec un verbe
  discursif léger dont l'objet est réel. Jamais un titre-concept nu devant un
  verbe d'action.

### 3.6 Texte de l'ancre — langue naturelle et honnêteté sémantique

- **Jamais dérivé du slug.** Construit depuis le titre de la cible ou une
  reformulation descriptive naturelle.
- **FR** : contractions obligatoires (`du`, `des`, `de l'`, `au`, `aux`) — « de
  le », « à les », « de assurance » sont interdits, **dans l'ancre et à la
  jonction enrobage→ancre**. Si la contraction change le sens, reformuler
  l'enrobage ou introduire un nom de cadrage. Articles et prépositions de liaison
  présents, accents corrects, casse des sigles (ETF, MiCA, US, VIX, S&P 500).
- **EN** : articles et prépositions natifs, pas de dump de mots-clés.
- **Honnêteté sémantique** — l'ancre décrit ce que la cible **est réellement**,
  pas un descripteur voisin qui sonne bien. Une ancre grammaticalement propre
  mais sémantiquement fausse passe tous les checks et empoisonne le lecteur :
  c'est **pire** qu'un enrobage raté. Aucune ancre honnête possible → skip.
- Si le seul lien pertinent est un titre-concept, un **nom de cadrage**
  l'introduit (« l'article sur… », « l'étude de… », « l'analyse de… »).
- **Aucun compte dans l'ancre quand le bloc hôte en énonce un autre.** Une ancre
  « Argentina's four redenominations » sous un paragraphe qui écrit « cinq
  redénominations successives » est visible pour le lecteur et fausse pour l'un
  des deux. Reformuler sans le nombre, ou aligner sur le bloc hôte après
  vérification. Apprentissage du 03/09/2026.

### 3.7 Diversité d'ouverture — le durcissement anti-démonstratif

Le défaut le plus visible en série n'est pas le premier mot répété, c'est le
**squelette d'ouverture identique**. Une insertion qui commence par un
démonstratif en position sujet est acceptable à l'unité, mais devient l'empreinte
robotique n°1 dès qu'elle se répète. « Premiers mots différents » **ne suffit
pas** : « Ce retard… » et « Cette contrainte… » sont le même squelette.

1. **Plafond démonstratif-sujet** — au plus **20 % des patches d'un batch**
   (arrondi bas ; zéro si le batch fait moins de 5 patches) peuvent ouvrir sur
   `^(Ce|Cet|Cette|Ces)\s+\w+`. Au-delà, réécrire les excédentaires.
2. **Jamais deux ouvertures démonstratives** dans le batch, même non
   consécutives, tant que le plafond n'est pas déjà la contrainte active. En
   pratique : varier par défaut, le démonstratif-sujet est l'exception.
3. **Rotation obligatoire des structures** — chaque patch pioche dans cet
   inventaire, sans réutiliser la même structure sur deux patches consécutifs, et
   le batch mobilise **au moins 5 structures distinctes** :

   | Structure | Exemple |
   |---|---|
   | Clivée | « C'est ce retard qui… » |
   | Subordonnée antéposée | « Tant que cette marge reste étroite, … » |
   | Participe antéposé | « Maintenue sans nouvelle décision, cette pression… » |
   | Gérondif antéposé | « En renchérissant ce coût, une … » |
   | Apposition détachée | « Premier maillon à céder, il… » |
   | Inversion locative | « Entre le geste et sa matérialisation s'ouvre le délai qui… » |
   | Sujet-initial ou quantifieur | « Toute [ancre]… » — l'ancre porte la majuscule |
   | Infinitif / nominalisation sujet | « Suivre ce rendement, c'est jauger… » |
   | Possessif sujet | « Leur dette à taux variable les place… » |
   | Adjectif antéposé | « Longs et variables, ces délais… » |
   | Contraste | « Loin d'être derrière nous, ce resserrement… » |

4. **L'anaphore reste régie par §3.4.** Cette règle ne supprime pas l'ancrage
   contextuel : elle interdit seulement de le porter **toujours** par un
   démonstratif en tête. L'antécédent peut être repris par un groupe nominal, un
   pronom, un participe, ou un démonstratif placé plus loin dans la phrase.

---

## 4. Phase D — diversité à l'échelle du batch

Trois contraintes simultanées, mesurables, vérifiées par code.

1. **Unicité des ancres** — chaque texte d'ancre est unique dans **tout le
   batch** pour sa langue, toutes cibles confondues. Pour une cible saturée
   (8 patches ou plus), établir la liste des N ancres syntaxiquement **et**
   lexicalement distinctes **avant** génération : pivots variés — mécanique,
   cadre, lecture, écart, rôle, effet, champ, exigences — et jamais le même pivot
   dans 4 ancres consécutives vers la même cible. Impossible de produire N ancres
   naturelles distinctes → skip les derniers patches de la cible.
2. **Diversité structurelle des enrobages** — zéro ouverture de phrase répétée
   dans la langue, zéro squelette syntaxique identique sur deux patches
   consécutifs, verbes de relation variés.
   **Mesure de l'« ouverture répétée » (décision du 18/09/2026)** : les **deux
   premiers mots** du texte visible de l'insertion, casse et ponctuation
   ignorées. Un premier mot répété est toléré (« The », « A », « Une ») ; deux
   premiers mots identiques sur deux insertions de la même langue du lot
   bloquent (« see also », « in the same », « whether a » ×3 sur le lot du
   15/09 auraient été réécrits). C'est ce que vérifie `scripts/validate_batch.py`.
3. **Pivot croisé** — le mot-pivot de l'enrobage diffère du mot-pivot du texte
   d'ancre dans la même insertion. Pas « la mécanique… dans [la mécanique de…] ».
4. **Symétrie FR/EN sur pages jumelles** — quand la source et la cible existent
   dans les deux langues, chaque patch FR a son miroir EN sur la page jumelle :
   même bloc hôte, même pont, ancres miroir **jamais traduites mot à mot** (chaque
   langue reçoit une ancre native, §3.6). Une asymétrie est assumée et annoncée au
   rapport, jamais silencieuse (MMT FR/EN le 03/09/2026). Pratique constante
   depuis le 03/09/2026, cluster Crisis Hub du 15/09 en référence.

**Limite volumétrique** : 18 patches maximum vers une même URL cible **par fichier**
(décision du 18/09/2026 : un lot peut en livrer davantage, répartis sur plusieurs fichiers — 30 vers 7547 le 15/09 à ≤ 9 par fichier), anti-explosion de fichier. Aucun plafond sur les liens entrants d'une cible par
ailleurs — un MAJEUR central peut légitimement recevoir 20 liens ou plus si les
ancres sont distinctes.

---

## 5. Alertes de densité — jamais un skip

**Pas de plafond fixe de liens sortants par source.** Le critère est la densité
relative :

```
densité = nombre de mots de la source / (liens sortants existants + patches du batch sur cette source)
```

Sous le plancher de sa famille → **alerte au rapport**, Paul tranche. Le nombre de
mots absent → le signaler, ne pas l'inventer.

| Famille | Plancher (alerte en dessous) |
|---|---|
| `pillar` | aucune alerte ; note pour information au-delà de 30 liens |
| `sub_pillar`, `major_article`, `deep_study` | 70 mots/lien |
| `foundation_article`, `case_study`, `faq`, `satellite`, `uncategorized`, `beginner` | 90 mots/lien |
| `tool` | alerte au-delà de 10 liens sortants après patch |
| `dataset` | alerte au-delà de 5 liens sortants après patch |

⚠️ **Ne jamais skipper pour cause de densité** — c'est une alerte, pas un rejet.

---

## 6. Phase E — relecture post-patch, gate bloquant

Les validations techniques prouvent que le patch **passe le plugin**. Elles ne
prouvent pas qu'il **sert le lecteur**.

**Aucune livraison sans exécution de cette phase sur 100 % des patches
candidats.** Pas d'échantillonnage.

### 6.1 Procédure

Pour chaque patch : localiser l'ancre → identifier le **bloc hôte entier** →
épisser virtuellement l'insertion → rendre le bloc en texte lisible, lien inséré
marqué → **lire le paragraphe reconstruit en entier**, jamais la seule phrase
d'ancre → verdict.

### 6.2 Verdicts

- **APPROPRIÉ** — hôte et cible relèvent du même sujet au niveau du paragraphe.
  Conserver.
- **ADJACENT** — sujets voisins du même domaine large. Acceptable uniquement si
  l'enrobage n'affirme rien d'invérifiable. Listé nominativement au rapport.
- **HORS-SUJET** — domaines différents sans pont honnête. **Un enrobage bien
  écrit ne sauve pas un placement hors-sujet.** Ré-ancrer vers un bloc pertinent
  de la même source, puis repasser intégralement par les phases B à E ; sinon
  skip `non-sequitur`.

### 6.3 Les 8 familles de défauts attestées — crible obligatoire, par patch

| # | Défaut | Correction |
|---|---|---|
| **F1** | **Sur-affirmation du contenu cible** — l'enrobage prétend ce que la cible contient. **60 à 66 % des corrections en aval.** | Reformuler en relation (§3.3) |
| **F2** | **Coupure structurelle** — insertion au milieu d'une liste, entre annonce et déroulé, dans un couplet rhétorique, entre règle et exception, entre définition et anaphore. Reprise du texte d'origine en minuscule ou par virgule. | Re-choisir le point de coupe, en fin de bloc |
| **F3** | **Anaphore sans antécédent** — démonstratif dont l'antécédent n'est pas dans l'ancre. | Réécrire ancré dans l'hôte (§3.4) |
| **F4** | **Faux-ami / homonyme** — signature des suppressions en aval. Le seul pont hôte↔cible est un mot polysémique employé dans deux sens. | Ré-ancrer où le sens correspond ; sinon skip `non-sequitur` **franc** |
| **F5** | **Classe de cible hors-domaine parachutée** | Pont explicite au niveau du paragraphe exigé ; sinon ré-ancrer ou skip |
| **F6** | **Ancre slug-collée ou sémantiquement fausse** — télégraphique, élisions cassées, ou décrivant autre chose que la cible réelle. | Réécrire depuis le titre de la cible (§3.6). Le lien est conservé, seule l'ancre change |
| **F7** | **Couture cassée** — « . , », minuscule après la phrase-lien, double espace, abréviation coupée. | Réparer |
| **F8** | **Doublon-cible / self-link** — normalement exclus en phase A. S'ils réapparaissent (deux phrases voisines liant la même cible). | Ré-ancrer ou skip |

**Test du faux-ami (F4)** : retirer le mot commun. S'il ne reste aucun rapport de
sujet, c'est un F4. **Un mot commun n'est pas un pont.**

Lexique à haut risque, liste ouverte : portage/carry (position contre logement) ·
convexité (prix-taux contre crédit) · concentration (rendements contre
géographique ou géologique) · duration (obligataire contre durée de cycle) ·
cash (allocation contre BFR) · mining (métaux contre proof-of-work) · capital
(immobilisé contre venture) · euro (devise contre ARR) · term (premium contre
dépendance) · taux/rate (intérêt contre démographie ou fiscalité) · reserves
(bancaires contre change) · swap (lines contre réplication ETF) · growth (macro
contre facteur) · stress (financement contre climatique).

**Classes F5 attestées** : agri (cacao, minerai de fer…) et régulation
crypto/DeFi dans du macro pur · working capital dans de l'allocation · fiscalité
retraite (PER, 401(k)) dans de la liquidité bancaire · démographie et dépendance
dans du taux · SaaS-ARR dans du FX · format ou documentation de dataset lié à une
page de phénomène. **Un match de silo n'est pas un pont.**

### 6.4 Priorité et compteurs

**Réparer > ré-ancrer > skip.** Un lien de valeur ne se jette pas pour une
formulation ; un ré-ancrage repasse par la validation depuis le fichier **et** par
cette relecture.

Compteurs vérifiés par code avant écriture :
`nb_relus == nb_candidats` et
`APPROPRIÉ + ADJACENT + ré-ancrés + skips_E == candidats`, le tout plus les skips
structurels amont couvrant **chaque** lien manquant d'entrée. **Aucun lien ne
s'évapore en silence.**

---

## 7. Phase F — validation programmatique finale, depuis le fichier

Avant livraison, chaque patch du **fichier JSON écrit** est re-vérifié par code
contre le contenu source :

occurrences == 1 · longueur 80-200 · aucune balise ni entité dans l'ancre · fin
de phrase valide, hors fermante-inline et hors abréviation · `<a>` unique et
équilibré · href absolu cohérent avec la langue de la source · zéro occurrence de
la liste interdite §3.1 · `\b(de|à)\s+l(e|es)\b` == 0 sur le texte visible · zéro
doublon-cible · unicité des ancres par batch et par langue · zéro ouverture
répétée · zéro squelette consécutif.

Un patch qui échoue est corrigé ou skippé — **jamais livré**. La vérification
mentale est un premier filtre, jamais la garantie.

**Ces contrôles sont implémentés dans `scripts/validate_batch.py`** (revue du
18/09/2026) : l'exécuter sur le dossier du lot avec `--export` pointant sur
l'export du mega, ne livrer qu'à **zéro ERREUR**, reporter les ALERTES telles
quelles. Sans `--export`, le script le dit : la validation est incomplète. Après
toute modification du script, relancer `--selftest`. Le mega, lui, ne vérifie que
longueur, absence de balise, présence d'un `<a href`, `expected_occurrences` et
`mb_substr_count` = 1 : tout le reste repose sur ce script. Le snippet ci-dessous
est l'ancêtre du script, conservé pour mémoire ; le script fait foi.

```python
import re
opens = [re.sub(r'<[^>]+>', '', p['insert_after_anchor']).strip() for p in patches]
demonstr = [o for o in opens if re.match(r'^(Ce|Cet|Cette|Ces)\s+\w+', o)]
cap = int(len(patches) * 0.20)
assert len(demonstr) <= cap, f"trop d'ouvertures démonstratives : {len(demonstr)}/{len(patches)} (cap {cap})"

sk = [' '.join(o.split()[:4]) for o in opens]
assert all(sk[i] != sk[i-1] for i in range(1, len(sk))), "squelette d'ouverture répété sur patches consécutifs"

assert len({o.split()[0] for o in opens}) >= min(5, len(patches)), "variété d'ouverture insuffisante"
```

---

## 8. AMF

Aucune insertion ni ancre prescriptive (« devrait », « should », « il faut »),
avec pourcentage d'allocation, timing d'achat ou de vente, recommandation de
sélection ou de couverture, ou comparaison géographique non statistique.

Formulation descriptive, historique, empirique uniquement. En cas de doute :
reformuler. Impossible : skip. Détail dans `editeur-eco3min`.

---

## 9. Taxonomie des skips

Chaque skip est tracé au rapport avec sa raison.

`no_concept` (la source ne mentionne jamais le sujet cible au niveau paragraphe) ·
`no_anchor` (aucune phrase 80-200 unique, propre et pertinente extractible) ·
`entity-encoded` (structurel, récupérable) · `structure-atypique` ·
`non-sequitur` (hors-sujet, faux-ami F4 ou classe F5 confirmés en relecture) ·
`self-link` · `doublon-cible` · `over-target-cap` (18 par cible atteint) · `nav-block` (plus de 5 MAJEURS depuis une même source, §1.6) ·
cross-langue · AMF non reformulable · impossibilité d'ancre distincte sur cible
saturée.

---

## 10. Anti-patterns — chaque ligne est un interdit ferme

- **Enrobage-pointeur**, quelle que soit sa forme. L'enrobage continue la pensée
  de l'hôte et relie par un verbe de relation.
- **Enrobage qui affirme le contenu interne de la cible** (F1), ou qui ouvre sur
  une anaphore sans antécédent dans l'hôte (F3).
- **Rotation de gabarits**, réutilisation d'une même ouverture, deux squelettes
  syntaxiques identiques consécutifs.
- **Ancre dérivée du slug**, sémantiquement fausse, dupliquée dans le batch, ou
  avec élision cassée.
- **Titre-concept nu** en sujet d'un verbe d'action.
- **Ancre retapée à la main**, hors bornes 80-200, avec balise ou entité, non
  unique, finissant en milieu de phrase, suivie d'une fermante inline, ou coupant
  une abréviation.
- **Insérer** dans un bloc qui lie déjà la cible, dans les 2 premiers
  paragraphes hors pilier parent, après une phrase suivie d'un `<a>`, ou en
  coupant une explication.
- **FR→`/en/` ou EN→FR.** Self-link. Plus d'un patch par lien manquant.
- **Skipper pour cause de densité** de la source, ou de nombre de liens entrants
  de la cible.
- **Livrer sans relecture E sur 100 % des patches**, sans le bilan au rapport, ou
  en statuant sur la seule phrase d'ancre au lieu du paragraphe reconstruit.
- **« Sauver » un hors-sujet par un bel enrobage.** Traiter un mot commun comme
  un pont.

---

## Livraison et application

Un lot livré = fichiers `patches-{cluster}-00N.json` à zéro ERREUR de phase F. L'application est faite par Claude, fichier par fichier : `py -3.14 eco3min-projets/tools/wp_push.py <fichier>` puis ability `eco3min/mega-patches` `{file, dry_run: true}` → lecture des `skipped_details` / `failed_details` (un skip `no_anchor` renvoie à §1 : ancre retapée) → `dry_run: false`. Procédure et repli wp-admin dans `plugins-eco3min` §5 étape 8 ; re-scan mega ensuite, obligatoire.

## Articulation

- `maillage-orphelins-eco3min` — **l'amont** : quelles cibles, combien de liens,
  depuis quelles sources, gate GSC.
- `editeur-eco3min` — AMF, style, sourcing.
- `archi-eco3min` — URLs, langues, levels.
- `plugins-eco3min` — le mega, le conseil T1/T2/T3 qui produit l'export.

Le format du JSON d'entrée et de sortie, le contrat du plugin, l'extracteur
d'ancres et la structure du rapport vivent dans le `CLAUDE.md` du projet
« Eco3min Cluster Builder — C. Maillage optimiser » (dossier eco3min-projets).

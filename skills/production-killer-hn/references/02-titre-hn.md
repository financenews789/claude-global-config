# production-killer-hn — référence : Le titre HN (§1.1 à §1.6)

Extrait VERBATIM de SKILL.md (découpage du 17/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 1. Le titre HN

### 1.1 La règle de la charge mentale unique (LA leçon)

**Un titre HN doit livrer UNE charge mentale, pré-digérée. Pas deux propositions que le lecteur doit relier lui-même.**

Sur /newest comme en front page, le lecteur scanne des dizaines de titres en ~1 seconde chacun. Il ne **travaille** pas. Tout titre qui exige qu'il (a) relie deux faits bruts pour sentir le paradoxe, ou (b) connaisse un prérequis pour comprendre l'enjeu, est filtré par ce scan rapide. Statistiquement on y perd.

**Vérification empirique (front page observée + archives latentframe) :**
- ✅ "72% of the dollar's purchasing power was destroyed in just four episodes" → **216 pts**. Le chiffre EST le choc, livré clé en main. Zéro liaison à faire.
- ✅ "Japan is gripped by mass allergies. A 1950s project is to blame" → 258 pts. Deux phrases, MAIS la 2e **donne** la réponse au cliffhanger de la 1re. Une seule tension qui se déroule, pas deux faits à rapprocher.
- ✅ "Victory: Tennessee man jailed 37 days for Trump meme wins $835k settlement" → une seule histoire.
- ❌ "The Fed cut rates by 100 bps in late 2024. Mortgage rates rose anyway." → **1 pt**. Deux faits BRUTS ; c'est au lecteur de fournir le "donc c'est paradoxal" ET le prérequis "la Fed influence les mortgages". Trop de travail pour un scan d'1 seconde.

**La distinction n'est PAS "une phrase vs deux phrases" ni "court vs long".** Les titres front page sont souvent longs. La distinction est :
- **charge unique** (le lecteur reçoit) vs **deux propositions à connecter** (le lecteur travaille) ;
- **zéro prérequis** (compréhensible par n'importe qui) vs **prérequis caché** (il faut déjà connaître le lien pour saisir l'enjeu).

Un `:` ou un `.` qui **introduit / complète / livre la réponse** est OK (charge unique qui se déroule). Un `.` qui **juxtapose deux faits à relier** est le piège.

### 1.2 Le pattern qui marche

**Une observation à charge unique + chiffre précis, sans spin dramatique, sans prérequis.**

Le bon titre HN donne un sentiment de :
- choc **mesurable** livré clé en main (pas une équation à résoudre)
- observation **factuelle** (pas un jugement)
- **zéro spin** (pas de mot journalistique dramatique)
- **zéro prérequis** (le non-spécialiste sent l'enjeu immédiatement)

✅ `72% of the dollar's purchasing power was destroyed in just four episodes` (216 upvotes, benchmark — charge unique, zéro prérequis)
✅ Format cliffhanger→réponse : `[constat surprenant]. [la cause/réponse]` (cf. exemple Japan)
❌ Format juxtaposition : `[fait A]. [fait B contradictoire].` — **piège** : délègue la résolution au lecteur (cf. échec term-premium à 1 pt)

### 1.3 Pont émotionnel vs précision quant — l'arbitrage

Tension récurrente : faut-il un terme grand-public (qui touche tout le monde) ou un terme technique (qui attire les quants) ?

**Règle : la vélocité early vient du généraliste curieux, pas du spécialiste.** Le spécialiste upvote mais ils sont 200, pas 2000. Donc préférer le **pont émotionnel** (un mot que tout le monde comprend : "mortgage", "your savings", "rent") au terme de niche ("the 10-year Treasury", "term premium") DANS LE TITRE.

- ✅ titre : `Mortgage rates rose anyway` (universel)
- ❌ titre : `The 10-year Treasury rose 116 bps` (niche — bon comme **fallback** pour un repost ciblé r/economics, pas comme titre principal HN)

**Garder le jargon HORS du titre** crée la curiosité qui fait cliquer. Le terme technique est la récompense une fois sur la page.

### 1.4 Pièges de titre

- **Juxtaposition de deux faits à relier** (cf. §1.1) → le piège n°1. Reformuler en charge unique ou en cliffhanger→réponse.
- **Prérequis caché** : le titre n'a d'enjeu que si le lecteur connaît déjà un lien (Fed→mortgage, courbe→récession…). Le non-spécialiste passe. Rendre l'enjeu explicite ou changer d'angle.
- **Ancrage temporel passé daté** ("in late 2024" posté en 2026) → **suspect majeur, pas un détail.** Sur un scan d'1 seconde, "late 2024" signale "vieux sujet, déjà vu" et fait passer le lecteur, même si l'angle est neuf. À **bannir du titre** : si l'événement est daté, formuler le finding de façon intemporelle (le mécanisme, pas la date). La date va dans le corps, jamais dans le titre.
- **"anyway", "shocking", "you won't believe"** → légèrement journalistique. Tolérable si la tension est réelle, mais tester une version factuelle pure si le doute existe.
- **Fausse symétrie numérique** : "Fed cut 100 bps → 10Y rose 116 bps" invite le nitpick "tu compares deux instruments différents". Si gardé, désamorcer en réponse (voir §3.3).

### 1.5 Le test pré-post du titre

Avant de poster, deux questions binaires :
1. **Ce titre a-t-il la même charge de choc immédiat que le benchmark à 216 pts ?** Si "presque", c'est jouable. Si "pas vraiment", le sujet est le maillon faible — pas le timing, pas le hero. Changer d'angle ou accepter un potentiel viral plus faible.
2. **Un lecteur qui ne connaît RIEN au sujet sent-il l'enjeu en 1 seconde, sans relier deux faits ?** Si non, reformuler.

Tous les sujets rigoureux ne se valent pas en potentiel HN. Un term premium, même parfaitement exécuté, est structurellement moins viral qu'un "72% destroyed". Choisir le sujet ET l'angle pour la charge unique, pas seulement pour la rigueur.

### 1.6 Toujours préparer un fallback

Un titre principal (pont émotionnel, charge unique) + un titre fallback (précision quant) documenté pour le repost r/economics si HN meurt. Voir §8.

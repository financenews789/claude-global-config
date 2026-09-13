# Les skills — un seul endroit où travailler

## Trois emplacements, trois rôles

| Où | Ce que c'est | Ce que tu en fais |
|---|---|---|
| **claude.ai** | La **source de vérité**. Le seul endroit dont le contenu se charge réellement. | Tu y **uploades**. Rien d'autre n'a d'effet. |
| **Ce dossier** | L'**historique versionné**, et le seul endroit où on édite en local. | Tu y **édites**. Git garde le diff, que ni le compte ni le cache ne donnent. |
| `AppData/…/skills-plugin/` | Un **cache automatique**, persistant, resynchronisé par le client quand le compte change. | **Rien.** Ni l'éditer, ni le supprimer. `rafraichir.py` s'en sert comme fenêtre sur le compte, c'est tout. |

Le cache n'est pas une quatrième copie à gérer : c'est de la plomberie du client
Claude. Il existe depuis mars 2026, il ne coûte rien, il se met à jour seul.

## La boucle de travail

```
1.  éditer un fichier de skills/
2.  l'uploader sur claude.ai  →  Settings › Skills › écraser le contenu
3.  python skills/rafraichir.py   →  il confirme la parité
```

⚠️ **L'étape 2 n'est pas optionnelle.** Éditer un fichier ici ne change **rien**
au comportement de Claude tant qu'il n'est pas uploadé. Sauter l'upload, c'est
créer précisément la divergence que ce dossier sert à éviter.

## La limite des 1024 caractères — le motif qui revient

claude.ai **refuse une description de frontmatter de plus de 1024 caractères**,
et il le refuse à l'upload, après coup. Le motif est toujours le même : une
description déjà pleine à laquelle une édition ajoute quelques mots.

Ce n'est pas un accident, c'est structurel. Au 08/09/2026, **8 skills sur 31 sont
à moins de 35 caractères de la limite**, la plus serrée étant `metas-eco3min` à
1011. Sur celles-là, toute rallonge dépasse.

**La règle** : sur un skill dont la description est au-dessus de 990, on
**raccourcit d'abord**, on ajoute ensuite. Une description n'a pas à être
exhaustive — elle sert à ce que Claude décide de charger le skill, pas à le
résumer. Les détails vivent dans le corps.

`rafraichir.py` le vérifie maintenant à chaque exécution : il **bloque** (sortie
non nulle) si une description locale dépasse 1024, et signale en une ligne
combien sont dans la zone serrée.

## `rafraichir.py` — il dit qui est en avance sur qui

```bash
python skills/rafraichir.py            # rapport seul, n'écrit rien
python skills/rafraichir.py --ecrire   # aligne le miroir sur le compte
```

Le manifeste `.sync.json` enregistre l'état à la dernière synchronisation. C'est
lui qui permet de distinguer trois situations qu'une simple comparaison confond :

| Verdict | Ce que ça veut dire | Ce qu'on fait |
|---|---|---|
| `MIROIR EN AVANCE` | tu as édité en local, pas encore uploadé | **uploader** |
| `COMPTE EN AVANCE` | le compte a changé ailleurs | `--ecrire` |
| `CONFLIT` | les deux ont bougé depuis la dernière sync | arbitrer à la main |

**`--ecrire` refuse de s'exécuter** si le miroir est en avance : il écraserait ton
travail non uploadé. `--force` passe outre, en connaissance de cause.

Une skill signalée absente du compte n'est pas forcément supprimée : vérifier sur
claude.ai avant de la retirer d'ici.

## À quoi sert cette copie, puisque le cache existe

Trois choses que le cache ne donne pas :

- **Le diff.** Le cache dit l'état courant, jamais ce qui a changé. Sans
  versionnement, une skill modifiée est une modification invisible.
- **La sauvegarde.** Le cache vit dans `AppData`, hors du repo. Il ne part pas
  avec une sauvegarde du dépôt.
- **Un chemin stable.** Celui du cache contient deux identifiants opaques.

Et une quatrième, la plus utile en pratique : **pouvoir grepper**. C'est ce qui a
permis de constater que le format 1200×630 et le token `#DED7C7` tournaient en
production sans figurer dans aucune skill, que la séquence
`document.fonts.ready` n'existait nulle part, et que trois projets portaient
trois constats contradictoires sur l'accès à FRED.

**Avant d'écrire une règle dans un `CLAUDE.md`, grep ce dossier.**

## Ce qui n'est pas mirroité

Les skills fournies par Anthropic — `pptx`, `xlsx`, `pdf`, `docx`, `morning`,
`schedule`, `import-memory`, `consolidate-memory`, `explain-usage`,
`setup-cowork`. Elles ne sont pas de Paul, évoluent hors de son contrôle, et
certaines portent des fichiers annexes binaires.

## La limite de description

La `description` du frontmatter pilote l'**activation** de la skill : c'est sur
elle que se décide le chargement. Au-delà de **1014 caractères** elle est exposée
à la troncature — et c'est la **queue** qui saute, or c'est là que vivent les
renvois « activer pour… » et « combiner avec… ».

`INVENTAIRE.md` marque d'un ⚠️ celles qui dépassent. Le comptage se fait en
**caractères**, pas en octets : les accents comptent double en UTF-8, et une
mesure en octets surestime d'une quarantaine de caractères sur un texte français.

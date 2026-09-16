---
name: production-bulletin-mensuel
description: Doctrine éditoriale du bulletin mensuel Eco3min — la carte ajoutée en tête des deux pages permanentes (FR + EN) et l'e-mail MailPoet correspondant. Pendant du baromètre (production-barometre-mensuel) dans le cycle mensuel. Activer pour toute production de bulletin ou de numéro. Porte les règles qui ne changent pas d'un cycle à l'autre : les DEUX contenus obligatoires par numéro (l'étude du mois plus le baromètre — un seul bloc fait un mail maigre et le lecteur juge l'abonnement là-dessus), le piège du cadre régime (il ne change presque jamais, le bloc doit porter ce qui a bougé et non l'état), la distinction entre la carte de page (notice d'archive) et le corps du mail (sollicitation lue en boîte de réception), le format de carte 90-140 mots, et la doctrine du sujet et de l'aperçu. Claude n'envoie jamais l'e-mail : il prépare le brouillon, Paul relit et envoie. Combiner avec editeur-eco3min (langue, AMF), regime-classifier-eco3min (lecture du régime).
---

# Production du bulletin mensuel Eco3min

> **Portée.** Ce skill porte la **doctrine éditoriale** du bulletin : ce qui ne
> change pas d'un cycle à l'autre. La plomberie — post_id des pages, séquence des
> abilities MailPoet, ancres d'insertion, templates, chemins de sortie — vit dans
> le `CLAUDE.md` du projet « Eco3min bulletin update ».
>
> `editeur-eco3min` fait autorité sur la langue, le registre et l'AMF.
> `regime-classifier-eco3min` fait autorité sur la lecture du régime.

## Ce qu'est un cycle

Deux livrables, dans cet ordre :

1. **la carte du mois**, ajoutée en tête des deux pages permanentes du bulletin,
   FR et EN ;
2. **l'e-mail MailPoet** correspondant, FR et EN, **prêt à envoyer**.

⚠️ **Claude n'envoie jamais l'e-mail.** Il produit le corps, le sujet et le texte
d'aperçu, et prépare le brouillon. Paul relit et envoie. Les abilities MailPoet
n'ont d'ailleurs aucun paramètre de statut — c'est structurel, pas une consigne.

**Deux formulaires, deux listes, deux e-mails distincts.** Jamais un seul message
bilingue.

## L'entrée que Claude ne peut pas choisir

Un cycle a besoin d'**une étude Macro Watch qui a bien performé sur Reddit**,
choisie par Paul et donnée en entrée sous forme de la paire d'URL FR + EN.

Si elle n'est pas dans le message d'ouverture : **la demander et s'arrêter là**.
Le critère de sélection est une performance Reddit que Claude ne peut pas
observer. La choisir soi-même, c'est choisir au hasard en le cachant.

## La règle des deux contenus

**Un numéro porte toujours au moins deux contenus.**

Un seul bloc fait un mail maigre — et le lecteur juge la valeur de son abonnement
sur cette impression **avant** de juger le contenu lui-même. C'est la règle qui
protège le taux de désabonnement.

| | Contenu | Rôle |
|---|---|---|
| **1** | **L'étude du mois** | Le bloc le plus long. C'est lui que le sujet du mail promet : il ne se laisse pas enterrer |
| **2** | **Le baromètre du mois** | Le seul contenu du site **mensuel par construction**, donc le seul qui garantisse un second bloc sans remplissage |

⚠️ **Vérifier que le baromètre du mois est sorti** avant de rédiger : son titre
doit porter le mois courant. S'il porte le mois précédent, le signaler et
demander soit d'attendre, soit un second contenu de remplacement. **Ne jamais
lier un baromètre périmé en le présentant comme celui du mois.**

Le bloc baromètre résume **ce que le mois a changé**, pas ce qu'est un baromètre.

## Le cadre régime — et son piège

Le mois se relit d'abord dans `~/eco3min/eco3min-knowledge/``chronologie/events.csv` (zone, période) : ce qui y est daté et qualifié en régime est ce que le bulletin peut nommer sans rediscuter le classifier.

Deux ou trois lignes en tête. Jamais un pavé : le libellé du régime daté du
1er du mois, ses descripteurs, et le lien vers le classificateur live.

### Le piège : le régime ne change presque jamais

Le lookup mensuel rend le même code depuis mars 2025. Répéter les quatre mêmes
descripteurs tous les mois transforme le bloc en **papier peint** — et le lecteur
finit par sauter ce qui l'entoure, c'est-à-dire le reste du mail.

**Le cadre doit donc porter ce qui a bougé**, pas seulement l'état : un ou deux
chiffres repris du baromètre du mois, déjà audités. L'état seul ne suffit pas à
justifier le bloc.

### Les descripteurs se recopient depuis la page live

Mot pour mot depuis la page vers laquelle le mail pointe — pas depuis le lookup
mensuel. **Le mail et la page doivent dire la même chose.**

Ce sont **deux séries distinctes** : voir `regime-classifier-eco3min` §8. Ne
jamais avancer une durée (« inchangé depuis X ») sans l'avoir vérifiée sur la
série effectivement citée.

### Le mois où le régime change

Il cesse d'être un cadre. Il passe en **premier bloc**, gagne sa **propre carte**
sur les deux pages, et devient **le sujet du mail**.

Le reste du temps, il n'a pas droit à sa carte : il ne vit que dans l'e-mail, en
une ligne.

## La carte de page

**90 à 140 mots** de corps. Les cartes existantes vont de 60 à 130 ; au-delà, la
page devient un mur.

Le corps donne, dans cet ordre : le **fait contre-intuitif**, le **chiffre** qui
l'établit, la **source primaire** entre parenthèses, et **ce que la page
contient** (dataset, CSV). Il **ne conclut pas à la place du lecteur**.

- **Lien FR → page FR quand elle existe**, EN sinon. Un lien FR vers `/en/` est un
  pis-aller acceptable quand la paire FR n'existe pas — pas un modèle, et surtout
  pas une URL FR à inventer.
- L'étiquette de mois est le mois d'**ajout au bulletin**, pas la date de
  publication de l'étude.
- **Les cartes sont anti-chronologiques.** La nouvelle va en première position.
  Insérer en bas est l'erreur naturelle, elle ne casse rien de visible — elle
  enterre juste la nouveauté.
- Le mois d'une carte est un **label texte**, pas une date : rien ne le vérifie.
- **AMF** : aucune projection unique, aucune recommandation, aucun impératif
  d'action. Quand un fait a deux lectures concurrentes, **les deux figurent**.

### D'où viennent les chiffres

De la **page de l'étude**, jamais de la mémoire du modèle, et jamais d'un
re-sourcing chez l'institution : l'étude a déjà passé son audit factuel à sa
publication.

Le travail ici est de **resserrer, pas de reconstituer**. Un chiffre de la carte
qui ne se retrouve pas dans la page source est un chiffre à supprimer.

## Le corps du mail n'est pas la carte recopiée

C'est la distinction la plus facile à rater.

| | La carte | Le mail |
|---|---|---|
| Lu par | quelqu'un **déjà sur le site** | quelqu'un dans sa **boîte de réception** |
| Nature | une **notice d'archive** | une **sollicitation** |
| Attaque | pose le fait | accroche |

Mêmes chiffres, même prudence, **attaque différente**.

### Ossature du corps

1. la salutation, avec un défaut de prénom **dans la langue du mail** ;
2. une phrase qui annonce ce qu'il y a dans ce numéro ;
3. **le cadre régime** ;
4. une respiration ;
5. **l'étude du mois** — titre reformulé en gras, 80 à 120 mots, lien nommé ;
6. une respiration ;
7. **le baromètre du mois** — 50 à 80 mots, lien nommé ;
8. **le rappel de délivrabilité** (spam, onglet Promotions) — il reste à chaque
   envoi, c'est lui qui protège la liste ;
9. la signature et le lien de désinscription.

## Le sujet et l'aperçu

Ce sont **les deux champs qui décident si le reste est lu**.

- **Le sujet et l'aperçu sont dans la langue du mail.** Pas d'aperçu anglais sur
  un mail français.
- **L'aperçu ajoute.** Il ne répète pas le sujet et ne le paraphrase pas.
- **L'aperçu ne promet que ce que le corps contient.**

Livrer **trois candidats de sujet par langue**, classés, avec l'aperçu qui va
avec chacun.

⚠️ Si aucun ne tient sans forcer le fait, **le dire explicitement** plutôt que de
livrer un sujet mou. C'est le signal que l'étude retenue n'a pas d'accroche — et
c'est une information utile, pas un échec à masquer.

### Un objet vide n'arrête rien

Le numéro FR d'août 2026 est parti à 17 abonnés avec « Aucun sujet » en ligne
d'objet — la chaîne de repli de MailPoet. **Aucun avertissement dans
l'interface.**

Le sujet et l'aperçu se remplissent **en dernier** et se **relisent après
enregistrement**, en rouvrant l'e-mail.

## Anti-patterns

- Choisir l'étude du mois soi-même.
- Livrer un numéro à un seul contenu.
- Un cadre régime qui répète l'état sans dire ce qui a bougé.
- Recopier la carte de page dans le corps du mail.
- Insérer la nouvelle carte en bas de la liste.
- Lier un baromètre périmé en le présentant comme celui du mois.
- Un chiffre de carte absent de la page source.
- Un aperçu qui paraphrase le sujet, ou qui promet ce que le corps ne contient
  pas.
- Un sujet mou livré sans dire qu'il est mou.
- Envoyer l'e-mail.

## Articulation

- `production-barometre-mensuel` — le pendant du cycle mensuel, et le
  fournisseur du contenu 2.
- `editeur-eco3min` — langue, registre, AMF.
- `regime-classifier-eco3min` — lecture du régime, et la distinction entre la
  série live et le lookup mensuel.
- `production-research-study` — les études qui alimentent le contenu 1.

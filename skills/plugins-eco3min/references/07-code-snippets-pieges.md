# plugins-eco3min — référence : Code Snippets — outillage et pièges, snippet 226 (§16)

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

---

## 16. Code Snippets — outillage et pieges

### `ewpa/create-code-snippet` ne met a jour aucun snippet

L'ability **cree un nouveau snippet, toujours inactif**. Elle **ne met pas a
jour** un snippet existant.

S'en servir pour patcher un snippet en place produit un **doublon inactif**,
sans erreur : on croit avoir deploye, rien n'a bouge, et le site porte desormais
deux versions du meme code dont une dormante.

**Le deploiement d'un patch de snippet est manuel**, par l'interface Code
Snippets. Un projet qui prepare un patch de snippet ne peut pas clore sa propre
boucle : il livre le patch, quelqu'un le colle.

### L'export local n'est pas la version live

`~/eco3min-wp/snippets/` est un **export**. Avant de proposer un patch, relire la
version en base dans wp-admin : l'export peut avoir pris du retard sur une
modification faite directement dans l'interface.

### Snippet 226 — moniteur de fraicheur editoriale

`0226-eco3min-date-alerte-moniteur-de-fra-cheur-ditoriale.php`.

Il lit un commentaire HTML place dans le `post_content` :

```
<!--e3m-review due="2027-01-10" lead="30" do="ce qu'il faut faire"-->
```

et le projette a l'enregistrement du post en trois metas : `_e3m_review_due`,
`_e3m_review_lead`, `_e3m_review_do`.

**Les metas sont la voie de LECTURE rapide ; le `post_content` est la voie
d'ECRITURE.** Jamais l'inverse : ecrire la meta sans toucher au marqueur serait
ecrase au prochain `save_post`.

Etats calcules, `days = due − aujourd'hui` : `overdue` si negatif (non
masquable), `soon` si dans le preavis, `ok` sinon. Ecran :
`wp-admin/tools.php?page=e3m-review`, derriere authentification — **`WebFetch`
n'y accede pas**, l'inventaire se reconstruit par le MCP.

⚠️ **Le snippet ne lit que le PREMIER marqueur d'une page** — `preg_match`, pas
`preg_match_all`. Une page qui en porte deux n'est surveillee que par le
premier ; le second est du bruit qui fait croire a une surveillance.

⚠️ **Les guillemets du marqueur sont des `"` droits.** Un editeur qui les
typographie casse le parsing **silencieusement** : la page disparait de l'ecran
admin sans erreur. Une date invalide produit le meme effet.

Le pilotage complet — triage, classification du travail, repose de l'echeance —
vit dans le `CLAUDE.md` du projet « Eco3min Keep Content Fresh ».

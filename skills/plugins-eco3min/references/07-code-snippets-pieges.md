# plugins-eco3min — référence : Code Snippets — outillage et pièges, snippet 226 (§16)

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026), mis à jour le 16/09/2026 pour Eco3min MCP 1.2.x. Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

---

## 16. Code Snippets — outillage et pieges

### Patcher un snippet : `eco3min/snippet-update` (Eco3min MCP 1.2.1, en live depuis le 16/09/2026)

Cinq abilities `eco3min/snippet-*` (plugin `eco3min-mcp`, module
`class-eco3min-mcp-snippets.php`) :

| Ability | Rôle |
|---|---|
| `snippet-find` | liste/filtre (q, in_code, tag, scope, active, ids[]) ; `include_code:true` ajoute code + `mirror` à chaque résultat (1.2.2) |
| `snippet-get` | code live + `code_sha256` + `mirror{filename, content}` prêt pour `~/eco3min-wp/snippets/` |
| `snippet-update` | modification EN PLACE : `replacements[]` byte-exact (`find`, `replace`, `expect_count`) ou `code` complet ; name / description / tags / priority / scope |
| `snippet-create` | création, `activate:true` optionnel |
| `snippet-toggle` | activer / désactiver |

**Cycle obligatoire** :

1. `snippet-get {id}` → lire le code LIVE (jamais le miroir) et noter `code_sha256`.
2. `snippet-update {id, expect_sha256, replacements:[…]}` en dry-run (défaut) → vérifier `plan`, `operations[].count`, `check.ok`.
3. Même appel avec `dry_run:false` → lire `probe.verdict` :
   - `ok` : écrit, snippet toujours actif, `ref` pour rollback ;
   - `fatal` : le site ne répondait plus → l'ancien code a déjà été restauré **dans la même requête** (`auto_restored:true`) ; lire `probe.*.excerpt` ;
   - `unreachable` : écrit, mais le loopback n'a pas joint le site → vérifier à la main que eco3min.fr répond.
4. Rafraîchir le fichier miroir avec `mirror.content` de `snippet-get` (garder le nom de fichier existant, par préfixe d'ID).
5. Rollback si besoin : `eco3min/rollback {ref}`.

**Pourquoi ce n'est pas un simple `save_snippet()`** : sur un snippet ACTIF, le
Validator natif de Code Snippets compare les fonctions déclarées à
`get_defined_functions()` ; le snippet modifié est déjà chargé dans la requête
MCP (exécution à `plugins_loaded`), donc il voit ses propres fonctions comme
des doublons et `save_snippet()` **désactive le snippet en silence**. L'éditeur
wp-admin y échappe parce que Code Snippets reconnaît sa propre route REST ; la
route du MCP Adapter, non. `snippet-update` fait donc : syntaxe par
`token_get_all(TOKEN_PARSE)` sans exécution, contrôle de redéclaration qui
tolère les noms de l'ancienne version du même snippet, écriture directe en
table + purge du cache Code Snippets, sonde loopback (admin-ajax + accueil avec
query string, jamais servi par WP Super Cache).

**Erreurs typiques** : `eco3min_mcp_count_mismatch` (le `find` n'est pas
byte-exact ou apparaît N fois : rien n'est écrit) ; `eco3min_mcp_stale` (le
live a changé depuis la lecture : refaire `snippet-get`) ;
`eco3min_mcp_invalid_code` (syntaxe ou redéclaration : le message donne la
ligne ou le nom) ; `eco3min_mcp_locked` (snippet verrouillé dans wp-admin).

### `ewpa/create-code-snippet` ne met a jour aucun snippet

L'ability **cree un nouveau snippet, toujours inactif**. Elle **ne met pas a
jour** un snippet existant.

S'en servir pour patcher un snippet en place produit un **doublon inactif**,
sans erreur : on croit avoir deploye, rien n'a bouge, et le site porte desormais
deux versions du meme code dont une dormante.

`ewpa/update-code-snippet` et `ewpa/set-code-snippet-active` (Enable Abilities
for MCP 2.11.1, opt-in) existent mais **désactivent tout snippet actif dont le
code change** et exigent une réactivation manuelle dans wp-admin : même boucle
manuelle, avec en prime une fenêtre où le snippet ne tourne pas. Les laisser
décochées dans Réglages › WP Abilities.

### L'export local n'est pas la version live

`~/eco3min-wp/snippets/` est un **miroir**. Avant de proposer un patch, relire la
version en base par `snippet-get` : le miroir peut avoir pris du retard sur une
modification faite directement dans l'interface. `expect_sha256` protège
contre l'écrasement d'une telle modification.

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

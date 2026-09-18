# production-research-study — référence : Rafraîchissement d'une étude publiée (§25)

Ajouté le 18/09/2026 après le rafraîchissement de l'étude #6 (`2y-treasury-leads-fed-pivots`,
mai 2026, remise à jour pour la hausse Fed du 16/09/2026 et le post r/economics du 22/09).
Le Step 0→10 décrit une production ; il ne dit rien de ce qu'on touche et de ce qu'on gèle
quand une étude déjà en ligne reçoit six mois de données et un épisode neuf. Ce fichier
fait foi au même titre que SKILL.md.

## 25.1 Quand rafraîchir plutôt que produire

Un rafraîchissement se justifie quand les trois conditions tiennent : l'objet de l'étude n'a
pas changé (mêmes séries, même règle, même thèse), un événement daté vient de tester la thèse
hors échantillon, et la page a déjà une URL indexée ou citée. Si l'objet change, c'est une
étude neuve avec sa propre URL ; on ne recycle pas un slug pour une autre thèse.

## 25.2 Audit d'entrée (avant de toucher au texte)

Une étude antérieure au 08/09/2026 (avant la série GENERIQUE) porte presque toujours des
défauts hérités, invisibles depuis wp-admin. Cinq contrôles, dix minutes, tous passés sur
l'étude #6 le 18/09/2026 et tous positifs :

| Contrôle | Commande | Défaut trouvé sur #6 |
|---|---|---|
| La jumelle FR reçoit le CSS et le JS | `curl -s <URL FR> \| grep -c 'eco3-<ns>-css'` (attendu 1) | 0 : la garde du snippet ne listait que les slugs `en/…` |
| Les fichiers du Dataset JSON-LD répondent | `curl -o /dev/null -w '%{http_code}' <contentUrl>` sur chaque `distribution` | deux 404 sur `/datasets/…` depuis mai |
| L'URL de citation est la vraie URL | `grep -o 'Available at: [^<]*'` == permalink | slug `2-year-treasury-fed-pivot` inexistant |
| Un seul `<h1>` sur la page publiée | `grep -c '<h1'` (attendu 1) | conforme |
| Les `<p>` du snippet gagnent sur `.entry-content p` | `scripts/css_specificity.py`, `lint_paragraph_rules()` vide | 19 sélecteurs perdants, bloc « Open dataset » illisible |

Ajouter : le module interactif existe-t-il (§10.6) ? S'il n'existe pas, il fait partie du
rafraîchissement, pas d'un lot ultérieur.

## 25.3 Ce qui se gèle, ce qui s'étend

- **Gelé** : les flags de pivot ou d'épisode, les taux de base par régime, le tableau
  des cas, tout chiffre qui dépend d'une règle à confirmation différée (un pivot qui
  exige 100 pb de suivi sous 24 mois ne peut pas être daté le mois de la première hausse).
  Le texte le dit : « les indicateurs sont ceux de l'édition de mai 2026 ».
- **Étendu** : les observations. Le CSV est prolongé aux mêmes colonnes ; les lignes déjà
  publiées sont recomputées et comparées à la version publiée (tolérance 0,01 sur un taux,
  1 pb sur un spread) avant d'ajouter les nouvelles. Les colonnes forward qui deviennent
  observables se remplissent. Nouveau fichier, nom suffixé (`-V2`), ancien laissé en place :
  WordPress refuse un ré-upload sous le même nom, et un CSV cité ne disparaît pas.
- **Présenté à part** : l'épisode neuf entre dans une section « [Mois AAAA] in real time »
  placée après la section des exceptions et avant l'état courant. Il y est une observation
  posée à côté des cas datés, jamais une ligne de plus dans le tableau. Deux précautions
  s'y écrivent toujours : la différence de fréquence (chiffre quotidien contre moyenne
  mensuelle, les deux vrais, non sommables) et la règle de confirmation qui reste ouverte.

## 25.4 Ce qui se réécrit, dans l'ordre

1. Byline : la mise à jour en premier, la première publication entre parenthèses
   (`Updated: 18 September 2026 (first published May 2026)`). Ni « Published: May »
   seul (la page paraît périmée), ni « Published: September » seul (le JSON-LD dit mai,
   le texte parle de l'édition de mai : un journaliste voit l'écart).
2. TL;DR : une phrase sur l'épisode hors échantillon, avant le lien de contexte.
3. Dernier bullet de l'exec summary, bloc « Current state » et ses niveaux à surveiller,
   FAQ dont la question était datée (« que signale le spread actuel de −17 pb ? » devient
   « qu'a signalé le 2 ans avant la hausse de septembre 2026 ? »), méthodologie (couverture,
   fenêtre, n), texte du bloc de téléchargement (n lignes), licence (« refreshed »).
4. Snippet : `dateModified`, descriptions Article et Dataset, `temporalCoverage`,
   `measurementTechnique` (« extended to … with flags unchanged »), FAQ JSON-LD alignée mot
   pour mot sur la page, `og:title`, `og:description`, `twitter:*`, puis les URL d'assets.
5. RankMath : titre (vérifier qu'il n'est pas tronqué), description avec le chiffre neuf,
   `facebook_image` et `twitter_image`, image à la une = nouveau hero. RankMath émet le
   premier `og:image` de la page depuis l'image à la une ; c'est celui que Reddit lit.
6. `faits/claims.jsonl` : une ligne par chiffre neuf, sur chaque page de la paire ; une
   ligne remplacée reçoit `superseded`.

Chaque remplacement passe par `eco3min/update-content` avec `expect_count: 1`, dry-run
puis réel ; un compte inexact refuse tout le lot, c'est la vérification. Même chose pour
le snippet (`snippet-update`, `expect_sha256`) et pour la page FR, réécrite nativement.

## 25.5 Charts

Le hero est régénéré à la charte en vigueur (le hero de mai 2026 était en DejaVu et navy),
avec le bandeau de tuiles KPI quand l'étude a un chiffre d'événement : c'est la vignette
qui a le mieux marché sur r/economics (post #5). Les charts dont l'objet n'a pas bougé
restent en place. Les gardes de `visuels-eco3min` s'appliquent ; `scripts/mpl_chrome.py`
porte le pied et les tuiles.

## 25.6 Journal

Le dossier `out/<slug>-refresh-AAAA-MM/` garde : `build_dataset.py` (prolongation et
comparaison), `make_charts.py`, `data/stats.json` (tout chiffre du texte vient de là),
`deliverables/`, les scripts de vérification et un mémo daté avec les `ref` de rollback
de chaque écriture. La reproduction de l'algorithme original s'y consigne aussi quand elle
diverge (sur #6 : un pivot 1998-07 que la règle publiée n'a pas, condition non documentée).

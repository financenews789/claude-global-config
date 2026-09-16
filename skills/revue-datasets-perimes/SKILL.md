---
name: revue-datasets-perimes
description: "Revue périodique de fraîcheur des datasets BRUTS Eco3min (les pages qui affichent le bloc « Latest Value » et servent un CSV/XLSX/JSON) : recense les 192 ids des 8 pipelines, lit les meta JSON servis, liste ceux dont la dernière valeur est périmée, distingue délai de publication normal / source amont gelée / pipeline muet / snippet, diagnostique à la source (API ECB, DBnomics, FRED, Webstat, BoE) et corrige. Activer pour « passe en revue mes datasets », « lesquels sont périmés », « la latest value n'a pas bougé », « le pipeline tourne mais la page est vieille », « audit de fraîcheur », ou tous les 1-2 mois en routine. Porte le script audit_fraicheur.py, la grille de délais tolérés par fréquence, l'arbre de diagnostic (5 causes attestées le 2026-09-15 : migration de clé ECB, série INSEE vidée, miroir DBnomics gelé, série FRED/OCDE/FMI figée, id jamais servi), et la doctrine « la page suit la donnée » (une page écrite autour d'une série source se réécrit quand on change la source). Combiner avec pipeline-eco3min (où vit chaque id), production-dataset (réécriture de page), plugins-eco3min (snippets 35/36/50/114)."
---

# Revue des datasets périmés — Eco3min

> Périmètre : les **datasets bruts** — pages dont le contenu est piloté par les shortcodes `[eco3min_key_stats]` / `[eco3min_download]` (snippet 35) et un fichier `{id}.csv/.xlsx/.json` produit par un pipeline. Pas les études, pas les pages à graphique FRED embarqué sans CSV, pas les CSV statiques uploadés (big-tech, Friggit).
> Une page n'est « périmée » que si sa `latest_date` est plus vieille que ce que la source publie. Le seuil n'est pas une date fixe : c'est **fréquence déclarée + délai de publication de la source**.

---

## 0. Ce qu'on vérifie, et où

| Couche | Fichier / URL | Ce qu'on y lit |
|---|---|---|
| Registre des ids | `eco3min-data/config/*.json` + `DATASET_REGISTRY` (v2) + ids codés (régime, score) | pipeline, sous-dossier, fréquence, slug |
| Donnée servie | `https://eco3min.fr/wp-content/dataset-meta/[ecb|eia|fr/]{id}.json` | `generated_at` (le pipeline a-t-il écrit ?), `key_stats.latest_date` (la source a-t-elle bougé ?) |
| Page | `https://eco3min.fr/en/{slug}/` — bloc `class="eco3min-key-stats"` | ce que le lecteur voit ; doit être identique au meta |
| Inventaire des pages | `eco3min-projets/context/datasets-inventaire.csv` (post_id, lang, slug, url) | croisement page ↔ id, pages sans pipeline |

Le snippet 35 lit le JSON à chaque affichage : **si le meta est à jour, la page l'est** (le cache d'edge peut retarder de quelques minutes — lire avec `?nc=<timestamp>` et `Cache-Control: no-cache` avant de conclure).

---

## 1. Lancer l'audit (5 minutes)

```bash
python ~/.claude/skills/revue-datasets-perimes/scripts/audit_fraicheur.py \
  --repo C:/Users/pauld/eco3min/eco3min-data \
  --out  eco3min-data/logs/audit-fraicheur-$(date +%F).csv
```

Sortie : un résumé Markdown sur stdout (par statut) + le CSV complet. Statuts :

| Statut | Signification | Action |
|---|---|---|
| `OK` | `latest_date` dans le délai toléré | rien |
| `DELAI-NORMAL?` | jusqu'à 1,5× le délai toléré | vérifier le calendrier de la source ; en général rien |
| `A-VERIFIER` | au-delà | **diagnostic §2** |
| `PIPELINE-MUET` | `generated_at` > 3 jours | le dataset est skippé ou en erreur dans le run : lire le log GitHub Actions du pipeline (`gh run view --log`) |
| `META-VIDE` | 200 mais pas de `latest_date` | builder qui rend un DataFrame vide (`{"rows":0}`) |
| `404` | meta absent | id déclaré jamais servi, ou upload SFTP cassé |

Délais tolérés (constante `TOLERANCE_DAYS`, à recalibrer si une source change de rythme) : daily 14 j, weekly 21 j, monthly 90 j, quarterly 200 j, annual 500 j ; exceptions nommées dans `SLOW_IDS` (EIA électricité, obligations 10 ans OCDE via FRED : 110 j). `ted-spread` est un 404 connu (id réservé, LIBOR arrêté).

Puis croiser avec les pages si le doute porte sur l'affichage : fetch de la page, extraire le bloc key-stats, comparer la date affichée au meta. Le 2026-09-15, 184 pages sur 225 portaient le bloc ; les 41 autres = 25 pages ECB (template sans bloc, bande statique) + 16 pages sans pipeline.

---

## 2. Arbre de diagnostic — une cause à la fois

Toujours **interroger la source directement** avant de toucher au pipeline. Cinq causes attestées, dans l'ordre de fréquence observé :

### 2a. La source a changé de clé / de dataflow (ECB)
Symptôme : `generated_at` du jour, `latest_date` gelée, `observations` inchangé depuis des mois.
Test : `GET https://data-api.ecb.europa.eu/service/data/{dataflow}/{clé}?format=csvdata&lastNObservations=3`. Si la dernière période est la même que celle du meta, la source elle-même est gelée → chercher la clé de remplacement avec des jokers : `{dataflow}/M..N.000000..` (liste toutes les zones/fournisseurs) puis `dataflow/ECB?format=sdmx-2.1` pour les dataflows voisins.
Cas du 2026-09-15 (entrée de la Bulgarie dans l'euro) : `ICP` → `HICP` avec fournisseur `4D0` (5 séries HICP, indice rebasé 2025=100), agrégat `I9` (EA20) → `I10` (EA21) pour le PIB, `STS` → `STBS` pour la production industrielle. Correctif = `config/ecb_datasets.json` + snippet 50 (JSON-LD) + exemple Python et « Series key » sur la page.

### 2b. La source a vidé ou renommé la série (INSEE via DBnomics)
Symptôme : `PIPELINE-MUET` (le fetcher reçoit un doc sans `period`/`value` → warning → dataset skippé, meta jamais réécrit).
Test : `GET https://api.db.nomics.world/v22/series/{provider}/{dataset}/{série}?observations=1` → `docs[0]` sans clé `period`. Chercher la remplaçante : `…/series/{provider}/{dataset}?observations=1&limit=300` et filtrer sur les dimensions.
Cas : `T.CTTXC.TAUX.FM.…` (France métropolitaine) vidée → `FR-D976` (France hors Mayotte). Le périmètre change (≈ +0,3 pt) : **tous les chiffres cités dans la page se recalculent** (§4).

### 2c. Le miroir est gelé alors que la source vit (DBnomics/BDF)
Symptôme : `generated_at` du jour, `latest_date` gelée sur **toute une famille** de séries d'un même provider.
Test : `GET https://api.db.nomics.world/v22/datasets/{provider}/{dataset}` → `updated_at` ancien. Vérifier la source primaire (Webstat) pour confirmer qu'elle publie.
Cas : BDF/MIR1 et BSI1 gelés à 2026-04 depuis juin 2026 (11 séries, 22 pages). Correctif = provider direct dans `fr_updater.py` (API Webstat, secret `WEBSTAT_CLIENT_ID`, en-tête `X-IBM-Client-Id`, repli DBnomics sur échec). Tant que la clé n'est pas acceptée par l'API (401 « Invalid client id or secret » = application non abonnée au produit *WEBSTAT Banque de France FR V1* ou secret ≠ Client ID), le repli DBnomics sert l'ancienne donnée.

### 2d. La série FRED est figée (miroirs OCDE / FMI / BIS)
Symptôme : `latest_date` gelée, FRED confirme : `https://fred.stlouisfed.org/graph/fredgraph.csv?id={CODE}` (sans clé) s'arrête à la même date. Attention : FRED coupe les connexions après une rafale de requêtes ; espacer, ou lire `https://eco3min.fr/dataset/{id}.csv` produit par la CI.
Deux sous-cas :
- **Délai structurel** (IRLTLT01…, OCDE via FRED : 2-3 mois ; GFDEBTN, Trésor : ~2 mois) → `DELAI-NORMAL?`, rien à faire.
- **Abandon** (HDTGPDUSQ163N gelée 17 mois, IR3TIB01GBM156N 8 mois) → changer de source : composite FRED (`CMDEBT / GDP`, `scale 0.1`) ou builder v2 sur la source primaire (BoE IADB `IUMABEDR`, OGL v3, sans clé, bloc de droits `boe-ogl`). Ces deux cas ont exigé une **réécriture de page** (§4).

### 2e. L'id n'est jamais servi
`404` sur le meta et sur le CSV. Soit réservé (`ted-spread`), soit builder mort. Pas d'urgence si documenté.

### Ce qui n'est PAS une cause (vérifié le 2026-09-15)
- Le snippet 35 : il affiche fidèlement le meta. Le contrôler seulement si meta à jour **et** page vieille — alors c'est le cache (`ewpa/clear-cache`) ou un `dataset_id`/`subdir` faux dans le shortcode.
- Les workflows GitHub Actions : ils tournent (`generated_at` du jour partout). Un dataset muet est un skip dans un run réussi, pas un run raté.

---

## 3. Corriger le pipeline

1. Patcher la config (`config/*.json`) ou le builder (v2) — règles et invariants dans `pipeline-eco3min`.
2. Tester en local sans clé quand c'est possible : `python scripts/{updater}.py --dataset {id} --no-touch` (ECB, FR, v2 sans FRED). Vérifier `output/meta*/{id}.json` : `latest_date` récente, `observations` ≥ l'ancien.
3. Commit + push, puis `gh workflow run {pipeline}.yml -f dataset={id}` et lire le log : `gh run view <id> --log | grep -E "obs \(|WARN|ERROR"`.
4. Relire le meta servi avec `?nc=` : il doit porter le `generated_at` du run.
5. Métadonnées qui mentent au contrôle : `frequency` faux dans le registry (gold/silver disaient `daily` pour du mensuel) → corriger, sinon l'audit crie à tort.

---

## 4. Mettre la page en phase — doctrine « la page suit la donnée »

Une page dataset décrit sa source : clé de série, exemple Python, période, nombre d'observations, chiffres des régimes. Changer la source sans toucher la page produit une page fausse, ce qui est pire que périmée. Trois niveaux :

| Changement | Page | Snippet JSON-LD |
|---|---|---|
| même série, nouvelle clé (ECB) | search-replace de la clé (`ewpa/search-replace` par post_id, un appel par chaîne ; l'ancienne clé apparaît 2-3 fois : exemple Python, « Series key », lien portail `datasets/ICP/ICP.M…`) + base d'indice si rebasage | 50 (ECB) : `ecb_dataflow`/`ecb_key`/`unit` |
| même concept, périmètre différent (INSEE FM → FR-D976) | recalculer **chaque chiffre cité** depuis la nouvelle série (moyenne, min, max, dates de régimes) avant d'éditer ; scope, période, nb d'obs, meta description | — |
| autre série (HDTGPDUSQ163N → CMDEBT/GDP ; interbancaire → Bank Rate) | **réécriture complète** selon `production-dataset` (Cas B si composite : Construction & Components, What This Captures, Data Quality) ; paragraphe « Source change » en Data Quality qui date le changement et interdit la jonction avec l'ancien fichier | 36 / 114 : `series`, `temporalCoverage`, `source_type`, `components`, retirer `rights` si la nouvelle source est domaine public |

Les snippets se modifient dans wp-admin › Snippets (éditeur CodeMirror : `document.querySelector('.CodeMirror').CodeMirror.setValue(...)` puis bouton « Enregistrer l'extrait »), et l'export `eco3min-wp/snippets/00NN-*.php` se met en miroir. Il n'existe pas d'ability de mise à jour de snippet.

Vérification finale par page : titre, bloc key-stats (valeur + date = meta), zéro occurrence de l'ancienne clé dans le corps (les occurrences restantes viennent du JSON-LD → snippet), pas de commentaire HTML, pas de « Fatal ».

Registre des faits : quand un chiffre cité change, ajouter la nouvelle ligne dans `~/eco3min/eco3min-knowledge/``faits/claims.jsonl` (`knowledge.add_claim`, added_by = `revue-datasets-perimes`) et marquer l'ancienne `superseded` — jamais l'effacer. Puis `grep` le même `claim` sur les autres `page_id` : ce sont les pages à repasser au projet Keep Content Fresh.

---

## 5. Rapport

Écrire `eco3min-data/logs/audit-fraicheur-{date}.md` en quatre blocs : **corrigés** (avec commit et valeur après), **gelés amont à arbitrer** (avec l'option et son coût : clé à créer, page à réécrire), **normaux** (délai source), **hors périmètre** (pages sans bloc, sans pipeline). Trois failles max par retour ; les 25 pages ECB sans bloc key-stats et les 16 pages sans pipeline sont connues, ne pas les redécouvrir.

## 6. Fréquence

Mensuel suffit ; systématique après tout événement de périmètre (élargissement de la zone euro, rebasage Eurostat, changement de portail d'une banque centrale, migration d'API). L'audit du 2026-09-15 est le point de référence : 192 ids, 8 corrigés, 13 en attente d'une clé Webstat, 2 réécrits.

# pipeline-eco3min — référence : workflows GitHub Actions (§8) et recette de test local (§9)

Extrait VERBATIM de SKILL.md (découpage du 17/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 8. Workflows GitHub Actions

Squelette commun (5 workflows : FRED, ECB, non-FRED, EIA, FR) : `schedule.cron` + `workflow_dispatch` (input optionnel `dataset`) → checkout → setup-python 3.11 → `pip install -r requirements*.txt` → run updater (`--dataset` si input, sinon `--all`) → list files → **SFTP via `sshpass` + `sftp`** (cd dossier serveur, lcd dossier output, `put *`) → job summary.

- FRED, non-FRED, articles et régime : `requirements.txt`. ECB : `requirements-ecb.txt`. EIA : `requirements-eia.txt`. FR : `requirements-fr.txt`.
- Secrets consommés : `FRED_API_KEY`, `EIA_API_KEY`, `WP_TOUCH_SECRET`, `FTP_HOST`, `FTP_USER`, `FTP_PASSWORD`.
- `timeout-minutes: 30` par job.
- **Deux workflows sortent du squelette.** `update-articles.yml` tourne sur une fenêtre mensuelle (`0 9 11-19 * *`), pas en cron quotidien. `regime-update.yml` n'utilise pas `sshpass` + `put *` mais `wlixcc/SFTP-Deploy-Action`, **un step par fichier** (13 steps) : ajouter une sortie au classifier impose d'ajouter ses 3 steps de déploiement à la main, sinon le fichier est produit en CI et jamais servi.
- Créneaux occupés : 08:00 (FRED, ECB), 09:30 (non-FRED), 10:30 (EIA, FR, régime), 09:00 les 11–19 (articles). **10:30 porte déjà trois jobs concurrents sur le même SFTP OVH** — un nouveau pipeline prend un créneau libre, et ce triplet mérite d'être étalé.

---

## 9. Test local (recette)

Toujours **depuis la racine du repo** : les configs portent des chemins relatifs (`./output/datasets`), un lancement depuis `scripts/` écrit à côté.

```bash
export FRED_API_KEY=xxxx          # non requis pour ECB ni FR
export EIA_API_KEY=xxxx           # EIA uniquement
python scripts/eco3min_updater.py          --dataset {id} --no-touch
python scripts/eco3min_updater_v2.py       --dataset {id} --no-touch   # ou --list
python scripts/ecb_updater.py              --dataset {id} --no-touch
python scripts/eia_updater.py              --dataset {id} --no-touch   # ou --list
python scripts/fr_updater.py               --dataset {id} --no-touch   # ou --list
python scripts/eco3min_articles_updater.py --dataset {id} --no-touch
python scripts/score_eco3min.py     # pas d'argparse : écrit toujours tout
python scripts/regime_classifier.py # pas d'argparse, ET touch WP non désactivable
```
Vérifier : `output/.../{id}.csv` (date 1re col, métrique dernière col), `.xlsx` présent, `output/meta/{id}.json` avec `key_stats` peuplé (pas `{"rows":0}` → sinon source vide / code faux). `--no-touch` évite de pinger WP en test.

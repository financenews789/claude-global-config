# production-killer-hn — référence : Lecture du résultat et journal de distribution (§6)

Extrait VERBATIM de SKILL.md (découpage du 17/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 6. Lecture du résultat — ne pas conclure trop tôt

- **15-25 min, 1-3 points : ni bon ni mauvais.** Trop tôt. La bascule se joue entre **30 et 90 min**.
- **50+ upvotes en 90 min** = excellent départ → déclencher le repli r/economics le lendemain.
- **<20 upvotes à 2h** = le post est probablement passé → patienter 48h puis r/economics avec le titre fallback.
- **Diagnostic d'un échec** (par probabilité) : ~70% timing/loterie de visibilité /newest · ~20% poids du compte (§5) · ~10% titre/sujet qui ne mord pas ce jour-là.

**Un échec HN n'invalide rien.** La page vit sa vie en SEO (captée par Google, citée comme dataset). HN est un canal à haute variance.

**Journal de distribution.** Chaque post d'étude sur r/economics (canal primaire ou repli) → une ligne dans `~/eco3min/eco3min-knowledge/``distribution/reconomics_posts.csv` via `knowledge.add_reco_post(...)` à J+48h (31 colonnes, ex-Google Sheet « R ECONOMICS POSTS » migré le 16/09/2026 : tier, cluster, hook ≤25 mots, posture face au consensus, canal du lien, statut modo et raison, OG image, notes et leçon). Les énumérations sont dans `distribution/referentiel.csv`, la fonction refuse un token absent. `python scripts/dashboard.py reco` donne la cadence 42 jours, les alertes de rotation tier / cluster, le taux de survie modo et le reach par posture. À lire avant le gate §0.5 : au 16/09/2026, 3 retraits sur 6 posts, tous en `eco3min_direct`, les deux postures `challenge` retirées — c'est la seule donnée empirique sur ce sub. Les soumissions HN du compte ont leur propre fichier, `distribution/hn_posts.csv` : on colle la page « submissions » de HN dans un fichier texte et `python scripts/hn_import.py <fichier>` l'importe (idempotent, met à jour points et commentaires). `dashboard.py hn` donne les points par canal (eco3min / github_eco3min / externe / texte), le taux de percée du contenu Eco3min et les soumissions restées à ≤1 point — la mesure directe du poids du compte (§5) et du ratio domaine (§5.2). Au 16/09/2026 (page 2 seule importée) : 4 soumissions eco3min.fr, une à 216 points / 267 commentaires, trois à 1 point.

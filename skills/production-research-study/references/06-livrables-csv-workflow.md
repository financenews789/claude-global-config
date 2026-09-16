# production-research-study — référence : Jeu de livrables, le CSV pierre angulaire, mode opératoire (§17)

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 17. Livrables et workflow de production

### 17.1 Le jeu de livrables (14 à 18 fichiers par étude)

| # | Fichier | Notes |
|---|---|---|
| 1 | **CSV** (produit EN PREMIER) | Source unique de vérité. CC BY 4.0 |
| 2 | **XLSX** | Mêmes données + feuille README/métadonnées |
| 3 | **Corps HTML** | Prêt à coller dans l'éditeur WP. AUCUN `<style>`, AUCUN `<script>` |
| 4 | **Snippet PHP** | Autonome : CSS scopé + JSON-LD + OG + RankMath + JS |
| 5-13 | **2 ou 3 charts × PNG/SVG/PDF** | Conformes brand kit, vérifiés visuellement |
| 13b | **Chart interactif** | SVG en JS natif, **sans bibliothèque externe**, alimenté par le CSV publié. Markup `data-*` dans le corps, JS dans le snippet. Repli `<picture>` si le fetch échoue. Voir §10.6 |
| 14 | **Package social** | RankMath, OG, X, LinkedIn, Reddit ×3, HN + pre-flights |
| 15 | **Guide d'upload des images** | Title/Alt/Caption/Description WP par fichier |
| 16 | **Doc de pre-review adverse** | Sortie du Step 1.5 — un livrable, pas une note interne |
| 17 | **Sorties d'audit** | compute_stats.py, scripts d'audit, hedge_justifications.json |
| 17b | **`provenance.md`** | Registre exigé par `sourcing-donnees-eco3min` : par série, la source réelle, le code, l'URL de fetch, la licence et ses marqueurs, la méthode, la date. Plus le résultat du **cross-check contre l'émetteur** (pas contre le canal de redistribution) et la liste des séries utilisées en contrôle mais **jamais republiées** |
| 18 | **README / index des livrables** | Métadonnées canoniques (H1, slug, meta) + résumé d'audit |

### 17.2 Le CSV — la pierre angulaire

1. Récupérer la donnée source brute (§23, playbook d'acquisition).
2. Si on réutilise la donnée d'une autre page Eco3min : **récupérer la série
   sous-jacente et recalculer**. Jamais recopier une approximation.
3. Fusionner, nettoyer, calculer toutes les variables dérivées (YoY, spreads,
   classifications de régime, décalages, percentiles, composites).
4. Exporter propre : en-têtes explicites, dates cohérentes (YYYY-MM-DD, YYYY-MM,
   ou `year` en annuel), aucune valeur manquante dans les colonnes calculées.
5. Documenter chaque colonne : nom, type, unité, source, calcul.

**Exigence de valeur unique** : au moins **une variable qui n'existe dans aucune
source publique** — composite, classification de régime, série décalée, métrique
inter-datasets. C'est ce qui rend le dataset téléchargeable et citable.

**Colonnes de forward return (obligatoires, benchmark substitué).** Le S&P 500
par défaut ne vaut que pour les études macro US à pertinence actions.
**Substituer le benchmark naturel** selon le mapping : forward return propre
(études de prix ou de régime), CPI/PCE (transmission d'inflation), matière
première contre S&P (diversification), obligations (études de rendement).
Colonnes `fwd_6m_pct` et `fwd_12m_pct`, plus `fwd_12m_mdd` là où le drawdown a un
sens, et des horizons 5 ans / 10 ans en données annuelles. Jours de bourse pour
les séries quotidiennes, périodes calendaires sinon — **préciser lequel**. NaN
quand la fenêtre n'est pas écoulée.

17.3 workflow Step 0→10 : dans SKILL.md

### 17.4 Mode opératoire

Les études se demandent **une à la fois** (« Produce Study C6 — Gold Real ATH »).
Dérouler Step 0 → Step 10 dans une seule conversation, de façon autonome, étape
par étape, **sans s'arrêter pour approbation**, puis livrer le jeu complet.

Si l'angle du mapping est faible ou contredit par la donnée : pivoter selon la
doctrine (§3.6), le signaler, et produire quand même.

**Sortie canonique unique** : un slug, un H1, un jeu de metas. Pas de variantes.

---

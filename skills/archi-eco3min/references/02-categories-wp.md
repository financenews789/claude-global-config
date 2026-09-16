# archi-eco3min — référence : Catégories WordPress (§3.1, seconde section portant ce numéro)

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée (§3.3) et le moment où lire ce fichier. Note du 15/09/2026 : le « Piège de collision » ci-dessous cite `eco3min-site-audit`, plugin désinstallé depuis ; le fait demeure — `commodities-global-economy` est le slug de la **catégorie EN** des matières premières et ressemble à un ancien slug de pilier, ne jamais déduire l'un de l'autre. Le référentiel des slugs de pilier est `e3m_referentiel` (Mega → Référentiel), pas un installer.

---

### 3.1 Catégories WordPress — table vérifiée en base

⚠️ **Le slug de catégorie WP n'est PAS le slug du pilier.** Il est plus court et
structuré différemment, et il **diffère entre FR et EN** — ce n'est pas une
simple recopie. Un import qui réutilise le slug de pilier comme catégorie échoue
avec `Catégorie WP introuvable`.

Vérifiée en base le **04/09/2026** (`ewpa/get-categories`) :

| Pilier | Catégorie FR | `term_id` | Catégorie EN | `term_id` |
|---|---|---|---|---|
| Actions & ETF | `actions-et-etf` | 440 | `equities-etfs` | 550 |
| Crypto-actifs | `crypto-actifs` | 452 | `crypto-assets` | 552 |
| Éducation financière | `education-financiere` | 416 | `financial-education` | 554 |
| Immobilier | `immobilier` | 420 | `real-estate` | 556 |
| Macro & géopolitique | `macro-geopolitique` | 430 | `macroeconomics-geopolitics` | 558 |
| Marchés financiers | `marches` | 413 | `financial-markets-indices` | 8 |
| Matières premières | `matieres-premieres` | 458 | `commodities-global-economy` | 560 |
| Politique monétaire & taux | `politique-monetaire-taux` | 446 | `monetary-policy-rates-liquidity` | 562 |
| Stratégies d'investissement | `investissement-strategies` | 456 | `investment-strategies` | 564 |
| **Hub débutant** (`apprendre-investir`) | **aucune** | — | **aucune** | — |
| **Hub datasets** (`donnees-analyses-...`) | **aucune** | — | **aucune** | — |

**Neuf** catégories par langue, pas onze : les deux hubs n'en ont aucune. C'est
pourquoi la procédure de rattachement autonome les exclut — un sous-pilier dont
la catégorie WP n'est pas résolvable ne peut pas recevoir d'import.

**Piège de collision.** `commodities-global-economy` est le slug de la
**catégorie EN** des matières premières. C'est aussi l'un des slugs de **pilier**
EN obsolètes hardcodés dans `eco3min-site-audit` (cf. §7). Deux objets
différents, même chaîne : ne pas déduire l'un de l'autre.

Résolution toujours **par slug**, jamais par `term_id` codé en dur —
`Eco3min_Mega_Category_Resolver::resolve($slug)`. Les `term_id` ci-dessus sont
donnés pour le diagnostic, pas pour être écrits dans du code.

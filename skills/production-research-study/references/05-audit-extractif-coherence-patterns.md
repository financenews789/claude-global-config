# production-research-study — référence : Audit extractif CSV-led, cohérence multi-livrables, patterns de claims à haut risque (§12, §13, §14)

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 12. Audit extractif CSV-led — la méthode qui marche

Les sections 7 et 11 traitent du workflow de production et du scan sémantique. Cette section décrit la méthode d'audit numérique qui doit **clôturer la production**. Elle est non négociable parce qu'elle est la seule à attraper les erreurs qu'un audit déclaratif laisse passer systématiquement.

### 12.1 Le problème de l'audit déclaratif

Le pattern d'audit "par défaut" est déclaratif :

```python
# Pattern qui LAISSE PASSER des erreurs
for claim in [list_que_claude_choisit]:
    verify(claim)
```

Biais de sélection : Claude liste ce qu'il pense devoir vérifier, donc il vérifie ce qu'il sait déjà être correct. Les erreurs survivent dans les claims qu'il n'a pas pensé à inclure dans la check-list. Aucune règle déclarative ajoutée par-dessus n'a jamais corrigé ce pattern, parce que la règle devient elle-même un élément que Claude liste ou ne liste pas.

### 12.2 Le pattern qui marche : le CSV mène la check-list

```python
# Pattern extractif — le CSV dicte quoi vérifier
csv_derivable_claims = enumerate_all_statistics_from_csv()
for claim in csv_derivable_claims:
    if pattern_present_in_html(claim):
        assert html_value == csv_value_within_tolerance
```

Différence opérationnelle : la check-list est un **effet de bord** de l'énumération du CSV, pas une décision humaine. Tout ce qui est dérivable du CSV ET cité dans le contenu doit matcher au seuil approprié.

### 12.3 Statistiques que le verifier doit énumérer (minimum)

Pour chaque étude avec un CSV, le verifier extrait depuis le CSV au minimum :

- **Latest observation** — chaque colonne pertinente de la dernière ligne
- **Médianes pleine échantillon** de chaque colonne numérique
- **Moyennes pleine échantillon**
- **Min / max** et leurs dates exactes
- **Comptages par phase / par régime / par filtre temporel défini**
- **Pourcentages dérivés** (comptage / total × 100)
- **Spreads et différences** entre colonnes
- **Stats forward-window** conditionnelles aux régimes (médian, IQR, % positifs)
- **Volatilités par phase** et ratios cross-phase
- **Distances** entre valeur latest et seuils référencés (target Fed 2%, niveaux psychologiques, etc.)
- **Sensibilités** à des choix de seuil (typiquement ±0.05, ±0.10, ±0.15 unités)
- **Comptages "X of top N"** quand cités

### 12.4 Format d'une assertion de verifier

Chaque assertion suit ce format strict :

```python
add_claim(
    description="Latest T5YIE 60bp above 2% target",
    expected_text_in_html="60 basis points",
    verifier=abs((latest.t5yie - 2.00) * 100 - 60) < 1
)
```

Trois éléments obligatoires :
1. **description** humainement lisible (pour le report)
2. **expected_text_in_html** = la chaîne exacte qui doit apparaître dans le contenu
3. **verifier** = la condition booléenne calculée depuis le CSV

### 12.5 Seuils de tolérance — pas de générosité

| Type de valeur | Tolérance maximale |
|---|---|
| Pourcentage absolu (ex : 2.60%) | ±0.005% (= 0.5bp) |
| Pourcentage relatif (%) | ±0.05% absolu |
| Percentage points (pp) | ±0.005pp |
| Basis points | ±1bp |
| Comptages (n=X) | exact (zéro tolérance) |
| Ratios (X×) | ±0.015 |
| Moyennes / médianes | ±0.01 |

Tolérance plus large que ces seuils = arrondi optimiste. Si une valeur exige plus de tolérance, soit la précision de la claim est fausse, soit le claim doit être hedgé explicitement avec justification documentée (voir 14.5).

### 12.6 Reporting du verifier

```
EXHAUSTIVE VALUE-BY-VALUE VERIFICATION
======================================
Total claims:    [N]
Pass:            [M]
Fail:            [N-M]

[Si fail > 0]
FAILURE DETAILS:
  ✗ [description]: expected X, found Y, csv_value=Z
  ...
```

Si fail > 0 → **BLOQUER la livraison**. Aucun seuil "tolérable" de fails — même un seul fail signifie qu'au moins une claim est fausse.

### 12.7 Quand cet audit est-il obligatoire

- Toute étude qui produit un CSV
- Tout article pilier majeur qui cite plus de 5 valeurs chiffrées
- Tout dataset page avec plus de 3 stats panel
- Tout contenu où une erreur factuelle aurait un coût de réputation

### 12.8 Ce que cet audit ne couvre PAS (limites assumées)

Cet audit attrape une famille spécifique d'erreurs. Il en laisse passer d'autres :

- **Wording / sémantique du concept** — Le verifier teste la valeur, pas le concept attribué. Une phrase comme "the mean T5YIE was 2.00%" passerait le verifier si 2.00% est bien une médiane du CSV — même si la prose dit "mean" alors que c'est la médiane. Voir section 14 pour la couverture des claim patterns à haut risque.
- **Claims qualitatives non chiffrées** — "the longest sustained reversal", "the largest forecasting failure" — pas de valeur numérique à matcher. À vérifier manuellement.
- **Cohérence inter-livrables** — Le verifier audit un seul fichier à la fois. Voir section 13 pour le multi-fichiers.
- **CSV lui-même** — Source de vérité par définition. Si la donnée source (FRED, BLS) est révisée ou incorrecte, le verifier ne le saurait pas.

---

## 13. Cohérence multi-livrables

Les mêmes claims numériques apparaissent typiquement dans **5+ fichiers** : HTML body, FAQ, JSON-LD (PHP), Reddit post, LinkedIn post, Twitter thread, OG meta description, alt text d'images. Une erreur introduite dans un fichier se propage par copy-paste vers les autres si elle n'est pas attrapée en amont.

### 13.1 Le pattern de cargo-copy

Une erreur factuelle isolée détectée tard dans une étude peut se retrouver dupliquée 4+ fois :
- HTML body (Beat 3 paragraphe)
- HTML FAQ (réponse à une question)
- PHP JSON-LD FAQPage (réponse répétée pour SEO)
- Companion doc (Reddit body, LinkedIn post)

Ce pattern est dangereux parce que chaque fichier "valide" son propre contenu de manière isolée — la première fois Claude écrit la mauvaise valeur, puis il copy-paste, et l'audit de chaque fichier passe parce que les valeurs internes sont cohérentes. L'audit extractif de la section 12 sur un seul fichier n'attrape pas ce problème car la fausse valeur peut être interne-cohérente avec d'autres fausses valeurs.

### 13.2 Règle de single-source-of-truth

Avant tout copy-paste de claim entre fichiers :

1. **Documenter la valeur dans le verifier** (section 12)
2. **Inscrire la valeur dans une table maître** unique en début de session de production
3. **Référencer la table maître** quand le claim apparaît dans un nouveau fichier — pas de copy-paste verbal depuis un autre fichier

### 13.3 Audit de cohérence multi-fichiers

Après production de tous les deliverables :

```bash
# Pour chaque claim numérique répété dans 2+ fichiers
grep -rn "[claim_pattern]" *.html *.php *.md
# Vérifier que TOUTES les occurrences disent la même chose
```

Le verifier extractif (section 12) doit idéalement parcourir TOUS les deliverables produits, pas juste le HTML principal.

### 13.4 Procédure après une correction

Si on corrige une valeur dans UN fichier, **IMMÉDIATEMENT** :

1. Grep la **nouvelle** valeur dans TOUS les autres fichiers → confirmation de cohérence
2. Grep l'**ancienne** valeur (incorrecte) dans TOUS les fichiers → détection de copies oubliées
3. Re-run le verifier extractif après les fixes croisés

Cette procédure n'est pas optionnelle. Une erreur corrigée à un seul endroit mais oubliée ailleurs est **plus toxique** qu'une erreur initiale propagée — elle crée une incohérence visible sur la même page web où un lecteur peut voir simultanément deux valeurs contradictoires.

### 13.5 Liste minimale des fichiers à grep en final-check

Pour une study Eco3min standard :

```
breakeven-term-structure-page.html       (HTML principal)
breakeven-term-structure-snippet.php     (JSON-LD + OG meta)
social-chartspecs-uploadguide.md         (companion doc social)
audit_*.py                                (les verifiers eux-mêmes)
```

Plus toute autre file de companion produite (image upload guide, charts script, etc.).

---

## 14. Patterns de claims à haut risque

Cinq familles de claims survivent systématiquement aux audits standards et nécessitent une attention spécifique. Le verifier de la section 12 doit explicitement les couvrir.

### 14.1 Claims de distance / écart ("within X of Y")

**Pattern** : "[value] is within [N basis points / N%] of [reference]".

**Exemples d'erreurs observées** :
- ❌ "5-year breakeven within roughly 50bp of 2% target" — actuel : 60bp
- ❌ "Median 10Y within roughly 10bp of 2% target" — actuel : 33bp

**Règle** : ces claims sont **automatiquement vérifiables** par calcul arithmétique : `|value - reference|`.

**Implémentation dans le verifier** :
```python
# Extraire toute occurrence du pattern "within X of Y"
# Pour chaque match, vérifier la distance arithmétique
add_claim("Distance latest to target",
          "60 basis points",
          abs((latest_value - reference_value) * 100 - claimed_bps) < 1)
```

### 14.2 Claims de superlatif ("highest since X", "largest in N years")

**Pattern** : "[value] is the [highest/largest/lowest/longest] [in/since] [reference]".

**Exemples d'erreurs observées** :
- ❌ "3.41% — highest level since June 2008" — actuel : all-time series high (depuis 2003), pas un local max
- ❌ "largest miss in 18 years" — claim vague, à confirmer

**Règle** : tout superlatif daté exige une vérification explicite "find the LAST occurrence of equal or greater value" dans le CSV. Si aucune occurrence antérieure n'existe → c'est un all-time max/min, pas "highest since X".

**Procédure** :
```python
# Pour "highest since DATE" claim sur valeur V observée à claim_date
candidates = df[df.date < claim_date]
prior_at_or_above = candidates[candidates.value >= V]
if len(prior_at_or_above) == 0:
    correct_claim = "highest in entire series"
else:
    last_match_date = prior_at_or_above.date.max()
    correct_claim = f"highest since {last_match_date.strftime('%B %Y')}"
```

Le verifier doit également couvrir les **superlatifs absolus** : "lowest in series", "longest sustained period". Ces claims demandent un scan exhaustif du CSV avec la condition appropriée.

### 14.3 Filter conflation dans les comptages

**Pattern** : énoncer un comptage "N events in [phase/régime/window]" sans nommer le filtre exact qui produit N.

**Exemple d'erreur observée** :
- ❌ "Post-COVID cluster (15 months) is the longest sustained reversal"
  - 15 = Post-**2022** reversed count (filtre `date >= 2022-01-01`)
  - "Post-COVID phase" = filtre `date >= 2021-04-01` → count = 24
  - La claim conflate deux filtres dont les valeurs sont différentes

**Règle** : tout comptage doit être strictement apparié à son filtre exact dans la prose ET dans le verifier. Quand deux filtres adjacents existent (Post-COVID phase vs Post-2022 sub-window, ex-dysfunction vs full sample, ±0.05pp vs ±0.10pp threshold), ne jamais réutiliser un comptage de l'un pour l'autre sans recompute.

**Procédure de discipline dans `compute_stats.py`** :
```python
# Bonne pratique : imprimer le filtre EXACT à côté du comptage
n_post2022_reversed = df[(df.date >= '2022-01-01') & 
                         (df.regime == 'reversed')].shape[0]
print(f"Post-2022 reversed [filter: date>=2022-01-01, regime=reversed]: {n_post2022_reversed}")

n_postcovid_phase_reversed = df[(df.phase == 'Post-COVID') & 
                                (df.regime == 'reversed')].shape[0]
print(f"Post-COVID phase reversed [filter: phase=Post-COVID, regime=reversed]: {n_postcovid_phase_reversed}")
```

Imprimer le filtre **EXACT** à côté du comptage rend la conflation visible au stade compute.

### 14.4 Rounding direction discipline

**Pattern** : arrondir dans la direction qui rend l'argument plus rond / plus fort.

**Exemples d'erreurs observées** :
- ❌ "median spread 2010s = −0.31pp" — actuel : −0.27pp (arrondi à −0.30 dans le mauvais sens)
- ❌ "within roughly 50bp of target" — actuel : 60bp (arrondi à 50 dans le mauvais sens)

**Règle** : arrondir au seuil que la précision du CSV justifie, **sans biais directionnel**. Une valeur exacte qui passe le verifier n'est pas matière à arrondi optimiste.

**Test diagnostic** : si l'arrondi va dans la direction qui rend ton argument plus fort, c'est probablement un biais inconscient. Recompute et utiliser la valeur exacte.

### 14.5 Hedging discipline ("approximately X")

**Pattern** : utiliser "approximately X" / "roughly X" / "about X" pour masquer le fait qu'on n'a pas computed la valeur exacte.

**Règle** : tout "approximately X" doit avoir une **justification documentée** parmi :

1. **Valeur externe non-fetchable** — ex : "approximately $1.4T in bank reserves" — source citée
2. **Agrégation multi-points calculée** — ex : "approximately 0.73%" = moyenne de 3 valeurs mensuelles (0.67/0.76/0.77), valeurs exactes documentées ailleurs
3. **Arrondi narratif documenté** — ex : "approximately ten-fold expansion" = 10.36×, arrondi narratif explicite

**Anti-pattern** : tout "approximately X" non justifié = erreur d'audit potentielle. Le hedge ne cache pas l'absence de vérification — il cache l'absence de **précision**. Différence cruciale.

**Implémentation dans le verifier** :
```python
hedge_patterns = [r"\bapproximately\s+\$?[\d.]+",
                  r"\broughly\s+\$?[\d.]+",
                  r"\bnearly\s+\$?[\d.]+",
                  r"\babout\s+\$?[\d.]+",
                  r"\baround\s+\$?[\d.]+",
                  r"~[\d.]+"]

# Chaque hit doit être présent dans la table hedge_justifications.json
# Sinon → FAIL
```

### 14.6 Tableau récapitulatif

| Pattern | Détection | Vérification |
|---|---|---|
| "within X of Y" | regex `within (roughly )?\d+\s*(basis points\|bps?\|%)` | `abs(value - reference)` |
| "highest since DATE" | regex `(highest\|lowest\|largest)\s+(since\|in)\s+` | Scan CSV ascendant pour dernier match |
| Filter conflation | Manual review au stade compute_stats | Imprimer filtre exact à côté de chaque comptage |
| Optimistic rounding | Comparer prose vs CSV exact | Tolérance section 12.5 |
| Unjustified hedging | regex `approximately\|roughly\|nearly\|about\|~` + chiffre | Table `hedge_justifications.json` |

---

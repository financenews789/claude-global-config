# production-research-study — référence : Data accuracy, forward distributions, Key Levels to Watch (§7, §8, §9)

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 7. Data accuracy — quand un CSV est produit

### 7.1 CSV = source unique de vérité

Si l'étude produit son propre CSV, **chaque chiffre du contenu vient de ce CSV**. Sans exception.

Workflow :
1. CSV produit en premier
2. Statistiques calculées via blocs Python dédiés (pas de mémoire)
3. Statistiques imprimées sur stdout avec valeur exacte
4. Valeurs copiées depuis stdout vers le contenu

**Ne jamais écrire une statistique calculée de mémoire.** Recompute si dans le doute.

### 7.2 Vérification ligne par ligne pour les épisodes historiques

Pour chaque épisode datable :
1. Identifier la date exacte dans le CSV
2. Extraire la ligne via `df[df['date'] >= 'YYYY-MM-DD'].iloc[0]`
3. Imprimer toutes les valeurs de cette ligne
4. Copier ces valeurs imprimées dans le contenu

### 7.3 Le piège des deux dates

Quand un épisode implique deux dates (ex : pic et creux d'un drawdown), faire le lookup **séparément** pour chaque date. Ne JAMAIS mélanger des valeurs entre dates différentes — c'est une erreur fréquente sous pression de production.

### 7.4 Direction vs niveau

"NL rose during period X" ≠ "NL expanded YoY". Vérifier les deux séparément :
- Niveau : `df[end] > df[start]`
- YoY : `df[date]['yoy'] > 0`

Une variable peut très bien augmenter YoY tout en déclinant en niveau (ou inversement). Confondre les deux est une erreur classique.

### 7.5 Marquage des chiffres hors-CSV

Tout chiffre venant d'ailleurs que du CSV doit être marqué dans le HTML :
- `<!-- SOURCE: [référence] -->` pour un chiffre vérifié hors CSV
- `<!-- VERIFY: [description] -->` pour un chiffre approximatif à confirmer

### 7.6 Forward returns — colonnes minimales

Si l'étude produit un dataset avec dimension temporelle d'événements :

| Colonne | Type | Calcul |
|---|---|---|
| `sp500_fwd_6m_pct` | float | `((SP500[t+126] / SP500[t]) - 1) × 100` |
| `sp500_fwd_12m_pct` | float | `((SP500[t+252] / SP500[t]) - 1) × 100` |
| `sp500_fwd_12m_mdd` | float | Max drawdown sur `[t, t+252]` |

Trading days pour daily, calendar months pour monthly. Spécifier lequel. NaN pour les observations récentes où la fenêtre forward n'est pas écoulée. Substituer un benchmark approprié si les actions ne sont pas la cible naturelle (ex : returns obligataires pour une étude de courbe).

---

## 8. Forward distribution patterns (regime-conditional)

Format imposé pour les sections de distributions forward conditionnelles aux régimes.

**Tableau requis** : régime, n, médiane 6m, médiane 12m, IQR (P25–P75), % positifs 12m, MDD médian.

**Avertissements obligatoires** :
- Note méthodologique sur fenêtres glissantes vs non-glissantes
- Gestion des transitions de régime
- Caveat de taille d'échantillon si un bucket a n < 15

**Disclaimer légal obligatoire** :

> "Past distributions are not predictive of future outcomes. Regime-conditional statistics describe historical patterns, not expected returns."

---

## 9. Surveillance Block — "Key Levels to Watch"

Format pour les blocs de surveillance prospective. Trois éléments **exactement** :

1. **Invalidation threshold** — Niveau qui changerait le régime / la lecture
2. **Confirmation signal** — Observation qui renforcerait la lecture actuelle
3. **Calendar catalyst** — Prochaine release/décision programmée

### 9.1 Pattern de formulation conforme

> "Si [condition observable], alors [le régime change vers Z], ce qui historiquement a été associé avec [résultat factuel]."

### 9.2 Interdictions

❌ "Buy if X breaks Y"
❌ "Sell if VIX exceeds 30"
❌ "Investors should reduce exposure when..."
❌ Toute formulation prescriptive

✅ "If 10-year yields exceed 4.5% for 3 consecutive months, the regime would shift to one historically associated with growth equity drawdowns averaging −22%."

### 9.3 Marqueur HTML

Insérer `<!-- UPDATEABLE: refresh current values and next event dates monthly -->` au-dessus du bloc pour rappel de mise à jour.

---

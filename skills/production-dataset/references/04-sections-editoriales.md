# production-dataset — référence : Macro Takeaway, Construction & Components, What This Index Captures, Data Quality, Historical Regimes, intro (§6 à §11)

Extrait VERBATIM de SKILL.md (découpage du 16/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 6. Macro Takeaway — section critique

Valeur ajoutée vs un miroir de la source. Positionne la série dans le système macro et illustre un mécanisme par un épisode daté.

**Paragraphe 1 — mécanisme structurel.** Rôle de la série dans la lecture macro ; variables avec lesquelles elle interagit (taux, inflation, dollar, crédit) ; **au moins un lien interne contextuel** ; 3-4 phrases denses. Cas B : nommer le concept canonique, et si une étude porte un nom proche, mailler l'étude sans reprendre son angle.

**Paragraphe 2 — illustration récente.** Épisode daté précis, chiffres datés, mécanisme expliqué (le pourquoi, pas que le combien) ; 3-4 phrases.

**Conformité AMF — descriptif, jamais prescriptif :**
- ✅ « The 2022 correction illustrated this duration sensitivity: the Nasdaq fell 33% as the 10-year yield rose from 1.5% to above 4%. »
- ❌ « Investors should reduce Nasdaq exposure when the 10-year yield rises. »
- Pas de prédiction matérialisée (« the index will likely… », « the next move should… »). Tout au passé descriptif ou présent factuel.

---

## 7. Construction & Components — [COMPOSITE], section centrale

200-300 mots. C'est l'élément différenciant SEO du Cas B : ce que les gens googlent (« how is X calculated », « X formula »). Quatre blocs imposés (cf. template §5, 5bis) :

1. **Formula** — notation mathématique simple, sur une ligne (`A − B`, `A / B`), jamais en prose.
2. **Components** — chaque composante : nom canonique + code/source + **fréquence native** + rôle. Nommer par la source canonique (« Fed Funds Effective Rate (FEDFUNDS) », pas « the Fed Funds rate »).
3. **Frequency reconciliation** — comment Eco3min aligne des fréquences hétérogènes (interpolation, forward-fill, ou « all monthly, no interpolation »).
4. **Coverage** — plage précise + raison des bornes historiques.

Distinction stricte avec Methodology : **Construction = la formule et les composantes** ; **Methodology = le pipeline** (comment Eco3min produit techniquement la donnée). Ne pas dupliquer la formule en Methodology.

---

## 8. What This Index Captures (And What It Doesn't) — [COMPOSITE]

250-350 mots. Combine pédagogie + AMF + différenciation. Remplace le « Common Pitfalls » des datasets bruts, plus adapté aux composites interprétables.

- **What it captures** : 3 aspects que le composite isole bien. Rester descriptif — ❌ « use this indicator to time… ».
- **What it does NOT capture** : 3-4 misinterprétations, chacune en `<strong>` + 2-3 phrases factuelles. Cibles fréquentes : confusion stock vs variation, causalité présumée vers les prix d'actifs, périmètre géographique, qualité vs quantité, décalage d'un proxy (CPI trailing vs anticipations).
- Clôture factuelle sur l'usage responsable (outil de classification de régime ≠ déclencheur tactique).

AMF renforcé : les composites sont **plus interprétables** donc plus risqués (« Net Liquidity tombe → vendre »). Vigilance maximale, voir §16.

---

## 9. Data Quality & Provider Notes — [COMPOSITE]

Trois angles spécifiques aux composites :
- **Latence dictée par la composante la plus lente** (une composante weekly H.4.1 plafonne la fraîcheur à une semaine).
- **Propagation des révisions** : toute composante révisée (CPI, earnings Shiller) change le composite en amont de la révision → Eco3min remplace le CSV entier à chaque release.
- **Sources alternatives** : le plus souvent **aucune** série native équivalente (point de différenciation). Si une alternative payante existe (ex. GMO 7-Year Forecast pour Excess CAPE Yield), la nommer factuellement.

---

## 10. Historical Regimes — signature Eco3min

4 à 6 régimes datés et nommés. Format `<p><strong>[Période] — [Nom].</strong> …</p>` **ou** `<ul><li><strong>…</strong></li></ul>` (les deux acceptés ; la page Excess CAPE Yield de référence utilise `<ul>`).

- **Nom distinctif** : « Dot-com bubble », « Zero real-rate era », « AI and concentration » — pas « Period 1 ».
- **Chiffres datés systématiquement** : « surged from 1,000 to 5,048 in five years », pas « rose strongly ».
- **Mécanisme exprimé** : pourquoi ce régime.
- **Cohérence cross-régime** : enchaînement logique, paramètre de transition visible.
- Cas B : concept canonique mentionné 3-4× dans la section ; 2-3 liens datasets + 1-2 liens études.

AMF : ✅ « Many stocks lost 90-99% of their value » (factuel) · ❌ « Investors who held growth stocks regretted not diversifying » (jugement rétroactif).

---

## 11. Intro éditoriale

`<p class="eco3min-intro">` en ouverture.

**Cas A/A'** — 2-3 phrases : (1) ce qu'est l'indicateur ; (2) couverture/source ; (3 optionnel) particularité. Pas de « Welcome », « In this page », « Discover ». On entre dans la définition.

**Cas B** — 4-5 phrases denses : concept canonique nommé **2×** + mention explicite **« an Eco3min composite »/« Eco3min calculation »** + composantes principales (formule simplifiée) + couverture précise.

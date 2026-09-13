---
name: production-research-study
description: Doctrine ÉDITORIALE et PIPELINE de production des études de recherche Eco3min. Éditorial : Backlink Hook (phrase citable ≤25 mots), Adversarial Pre-Review (4 reviewers hostiles) et Thesis Pivot Doctrine, Beat 1/2/3 (consensus, contradiction, steelman), anti-editorializing, Yield Curve Lesson, Citation Readiness Test, robustesse comme blindage, Key Levels to Watch non prescriptifs, AUDIT EXTRACTIF CSV-LED (le CSV énumère les claims, pas Claude), cohérence multi-livrables contre cargo-copy, patterns à haut risque (within X of Y, superlatifs, arrondis, hedging). Pipeline : workflow Step 0→10, 14-18 livrables dont le CHART INTERACTIF obligatoire (SVG JS natif, repli statique), structure de page en 28 blocs, déploiement WordPress (namespace par étude, snippet autonome), verrous A→G (le G éditorial : cadratins, tics IA), registre d'erreurs. Activer pour toute étude visant backlink journalistique ou viralité Reddit défendable.
---

# Principes éditoriaux — Eco3min Research Studies

> Ce skill code la **couche éditoriale ET le pipeline de production** des études killer Eco3min. La couche éditoriale (§1-16) est transférable au-delà des research studies : tout article pilier majeur, dataset à fort potentiel ou Q&A à enjeu viral peut en bénéficier. Le pipeline (§17-24) est spécifique aux études.
>
> Ce qui reste dans les Custom Instructions du projet : le fichier de mapping et son registre de statuts, les codes d'étude, les chemins locaux. Rien d'autre.
>
> Voir aussi `editeur-eco3min` (identité + AMF), `visuels-eco3min` (data viz), `production-dataset` (pages dataset brutes), `production-q-and-a` (Q&A).

---

## 1. Double objectif éditorial

Tout contenu visant le rang research-study doit réussir **simultanément** sur deux fronts :

1. **Viralité Reddit** — High-effort OC avec un "aha moment" visible en 3 secondes
2. **Backlinks journalistiques** — Insight citation-ready, zéro friction cognitive pour un journaliste sur deadline

Ces objectifs ne sont **pas en conflit**. Les mêmes données servent les deux si la structure est correcte. Reddit récompense l'effort visible et le pattern frappant. Les journalistes récompensent une phrase qu'ils peuvent copier-coller en attribution.

---

## 2. Step 0 — Backlink Hook (avant tout le reste)

**Avant toute production, écrire la réponse à cette question :**

> "Quelle est LA phrase qu'un journaliste peut citer sans avoir compris l'analyse complète ?"

### 2.1 Critères du hook

- ≤ 25 mots
- Contient une statistique frappante
- Compréhensible par quelqu'un qui n'a jamais entendu parler du sujet
- Directement copy-pasteable comme : *"According to Eco3min, [phrase]."*

### 2.2 Exemples de hooks réussis

✅ "72% of all US inflation since 1914 occurred during just four periods spanning 29% of the time."

✅ "Every yield curve inversion since 1976 has preceded a recession, with a median lead time of 14 months."

✅ "The S&P 500 has never delivered a negative 12-month return when the VIX was below 15."

### 2.3 Exemples de hooks qui échouent

❌ "The tent-shaped relationship between real rates and CAPE suggests a non-monotonic equilibrium."

❌ "Net liquidity regime transitions explain 68% of forward return variance conditional on..."

(Trop techniques, exigent du contexte avant d'être compris.)

### 2.4 Règle d'arrêt

**Si tu ne peux pas produire un hook fort, l'angle de l'étude n'est pas prêt.** Proposer un angle plus tranchant avant de continuer. Ne jamais commencer la production sans hook validé.

### 2.5 Le hook devient ensuite

- Le premier bullet de l'Executive Summary
- Le texte du bloc TL;DR
- Le titre Reddit
- La base du social snippet package

---

## 3. Step 1.5 — Adversarial Pre-Review

Après lecture du brief, **avant de fetch les données**, simuler quatre reviewers hostiles. Cette étape économise des semaines de retours négatifs après publication.

### 3.1 Reviewer 1 — r/economics Moderator (Rule IV : no editorializing)

- Le titre implique-t-il un jugement normatif ?
- La thèse présuppose-t-elle sa conclusion ?
- Y a-t-il des termes chargés dans les 3 premiers paragraphes ?
- Ce titre survivrait-il sans intervention modérateur ?

### 3.2 Reviewer 2 — FT Data Journalist (méthodologie)

- La fenêtre temporelle est-elle choisie pour soutenir la thèse ? Que se passe-t-il avec ±10 ans ?
- Les frontières d'épisodes sont-elles définies objectivement ou hand-picked ?
- Le résultat survit-il à un changement de seuil de ±1 unité ?
- Une explication plus simple existe-t-elle ?
- Y a-t-il des corrélations sans contrôle des confondants ?

### 3.3 Reviewer 3 — Quant (rigueur statistique)

- Forward returns avec look-ahead bias ?
- Classifications de régime ex-post ou calculables en temps réel ?
- Buckets avec n < 20 ?
- Fenêtres glissantes qui gonflent la significativité ?
- La relation est-elle stationnaire à travers les sous-périodes ?

### 3.4 Reviewer 4 — Macro Economist (steelman counter-thesis)

- Quel est le contre-argument le plus fort ?
- Quel contexte manquant changerait l'interprétation ?
- Que ne mesure pas le dataset que les lecteurs vont supposer mesuré ?
- Où est-ce que la politique / l'institution critiquée a effectivement FONCTIONNÉ ?

### 3.5 Format de sortie

```
═══════════════════════════════════════════════════════
ADVERSARIAL PRE-REVIEW — [Titre du contenu]
═══════════════════════════════════════════════════════

BACKLINK HOOK : "[la phrase]"

REVIEWER 1 (r/economics mod) :
▸ Attaque : [spécifique] → Défense : [comment + où dans le contenu]

REVIEWER 2 (FT data journalist) :
▸ Attaque : [spécifique] → Défense : [comment + où]

REVIEWER 3 (Quant) :
▸ Attaque : [spécifique] → Défense : [comment + où]

REVIEWER 4 (Macro economist) :
▸ Contre-argument le plus fort : → Défense :
▸ Contexte manquant : → Section ou donnée additionnelle :

CHANGEMENTS DE DESIGN :
1. [Données additionnelles à fetch]
2. [Sections additionnelles à ajouter]
3. [Reformulations de wording]
4. [Décisions d'échelle de chart]
```

### 3.6 Si la pre-review révèle une thèse indéfendable — Thesis Pivot Doctrine

Ne pas dépenser le temps de production sur une thèse qui ne tient pas l'épreuve adverse. **La donnée est la source de vérité.** Quand la donnée principale contredit le cadrage du brief :

1. Vérifier la contradiction contre **au moins deux références indépendantes**.
2. Identifier le **noyau défendable** que la donnée soutient réellement — il est généralement **plus tranchant et plus citable** que l'original. Précédents : C1 cultivé-vs-extrait, C3 vitesse-pas-niveau, C4 fiable-puis-épisodique, C5 écart headline−core, #31 pass-through conditionnel, #27 logistique-pas-géopolitique.
3. Signaler le pivot à Paul avec les preuves, produire sur la thèse pivotée, et **cadrer l'inversion de façon transparente** sur la page là où c'est pertinent : c'est un actif de rigueur, pas une faiblesse.
4. Mettre à jour l'entrée du fichier de mapping et son Thesis Pivot Registry.

---

## 4. Structure narrative Beat 1 → Beat 2 → Beat 3

Les sections analytiques doivent contenir cette séquence narrative, dans cet ordre :

| Beat | Rôle | Exemple |
|---|---|---|
| **Beat 1** | Énoncer le récit dominant **équitablement** | "The dominant narrative holds that [X]." |
| **Beat 2** | Contradiction empirique avec chiffres | "The data shows [Y, with specific numbers]." |
| **Beat 3** | Steelman du contre-argument (OBLIGATOIRE) | "A legitimate analytical qualification is that [Z]." |

### 4.1 Règles strictes de la séquence

- **Beat 1 doit être présenté FAIRLY**, sans caricature. Si le récit dominant est mal formulé, le lecteur cesse de croire à la rigueur du reste.
- **Beat 2 contient la thèse** — la contradiction empirique chiffrée. C'est le cœur de l'étude.
- **Beat 3 est OBLIGATOIRE, pas optionnel.** C'est ce qui distingue Eco3min des contenus polémiques.
- **Beat 3 doit apparaître dans les 2 sections suivant Beat 2**, pas en fin d'article où personne ne le lit.

### 4.2 Contenu requis pour Beat 3

Au moins UN parmi :
- Un contre-fait avec un chiffre précis
- Une qualification structurelle (ex : "ce dataset ne mesure pas X")
- Une interprétation alternative cohérente avec les mêmes données
- Une mise en garde de taille d'échantillon (n < 15, période courte, etc.)
- Une reconnaissance d'un cas où la politique / le mécanisme critiqué a fonctionné

### 4.3 Pourquoi Beat 3 est non négociable

Sans Beat 3, l'étude devient un texte d'opinion déguisé en analyse. Les modérateurs r/economics le détectent immédiatement. Les journalistes FT/Bloomberg ne citent pas un texte qu'ils ne peuvent pas défendre face à un editor sceptique. Beat 3 **augmente** la viralité tout en réduisant les attaques — pas un trade-off.

---

## 5. Anti-editorializing — règles strictes

### 5.1 Tableau des termes proscrits

| Terme | En H1 | Dans le corps | Remplacement |
|---|---|---|---|
| "destruction" | ❌ JAMAIS | ⚠ Uniquement entre guillemets avec contre-argument | "erosion", "decline", "loss" |
| "tax" (pour inflation) | ❌ JAMAIS | ⚠ Uniquement en citation attribuée | "cost", "erosion" |
| "manipulation" | ❌ JAMAIS | ❌ JAMAIS | "intervention", "adjustment" |
| "failed" (politique) | ❌ JAMAIS | ⚠ Uniquement avec une métrique précise | "did not achieve [X]" |
| "should" / "must" (prescriptif) | ❌ | ❌ | "historically associated with" |
| "will" (certitude) | ❌ | ❌ | "if [condition], then [pattern]" |
| "obviously" / "clearly" | ❌ | ❌ | Énoncer le fait directement |
| "undeniably" / "proves that" | ❌ | ❌ | "the evidence indicates" |

### 5.2 La Yield Curve Lesson

Avant d'écrire le contenu, te poser cette question :

> "Si je supprimais TOUT le commentaire et publiais SEULEMENT le tableau de données + un chart + la FAQ + la méthodologie, est-ce que ça forcerait quand même les citations ?"

**Si OUI** → les sections analytiques sont additives. Les garder COURTES et DÉFENSIVES.

**Si NON** → les sections portent l'insight, elles doivent être ESPECIALMENT rigoureuses.

C'est un test diagnostic puissant. La plupart des études échouent parce que les auteurs croient ajouter de la valeur via le commentaire alors qu'ils ajoutent des angles d'attaque.

### 5.3 Exemple — le contraste qui change tout

❌ "The Fed failed spectacularly during the Great Inflation"

✅ "The Fed Funds rate remained below CPI YoY for 38 consecutive months — the longest negative-real-rate regime since 1954."

La seconde version est **plus dévastatrice ET moins attaquable**. Aucune adjective normative, juste un fait compté précisément. Un journaliste peut citer la seconde immédiatement. La première force le journaliste à hedger.

### 5.4 Règle générale de la voix

Construire la critique par **accumulation de faits**, pas par adjectives. Le lecteur tire ses propres conclusions, c'est plus puissant que de les lui imposer.

---

### 5.5 La robustesse comme blindage

Quand un résultat central **dépend d'un choix méthodologique** — déflateur, millésime de données, seuil — divulguer le résultat de l'alternative, **y compris quand le signe s'inverse**. En trois endroits : une phrase dans la TL;DR, le développement complet dans le Beat 3, et le détail dans la méthodologie.

« We report both rather than choosing the flattering one » est un **actif de citation**, pas un aveu de faiblesse : c'est précisément la phrase qui désarme le reviewer FT et le modérateur r/economics.

Corollaire pour le pre-flight r/economics (§15) : la divulgation de robustesse est offerte **proactivement dans le self-comment**, ce qui coupe l'attaque déflateur/seuil avant qu'elle ne parte.

---

## 6. Citation Readiness Test

Avant publication, vérifier :

- [ ] Le backlink hook est-il visible **above the fold** (premier écran de contenu sans scroller) ?
- [ ] Le hook est-il dans la TL;DR ?
- [ ] Le hook est-il le **premier bullet** de l'Executive Summary ?
- [ ] Le hook tel que présent peut-il être copié dans un article par un journaliste sans modification ?
- [ ] Si oui, est-ce que cette citation rendrait l'article du journaliste meilleur ?

Si une seule réponse est non → retravailler le hook ou son placement avant publication.

---

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

## 10. Sélection du type de chart

**Règle directrice** : la donnée dicte le visuel, pas un template figé.

Choix possibles :
- Line chart + zones grisées de régimes (séries temporelles avec décomposition)
- Scatter plot (corrélations bivariées)
- Heatmap (matrices de relations)
- Small multiples (comparaisons inter-épisodes)
- Ridge plot (distributions par régime)
- Waterfall (décomposition d'une variation)
- Stacked area (composition évolutive)
- Density / quantile bands (distributions historiques)
- Gantt / timeline (séquencement d'événements)

### 10.1 Justification obligatoire

Pour chaque chart de l'étude, documenter :

```
SCALE JUSTIFICATION:
Data range: [min] to [max], ratio = [X]×
→ Primary: [log/linear] because [reason]
→ Supplementary: [yes/no]
```

### 10.2 Politique d'échelle

| Ratio max/min | Échelle primaire | Vue supplémentaire |
|---|---|---|
| > 5× | Log (default obligatoire) | Linear comme "Supplementary View" |
| 2×–5× | Choix justifié | Autre échelle si utile |
| < 2× | Linear | Pas nécessaire |

### 10.3 Le chart "r/dataisbeautiful"

Une étude doit avoir un chart conçu pour fonctionner **standalone** sur les réseaux sociaux :
- Compréhensible sans l'article
- Visuellement mémorable (layout non conventionnel encouragé)
- "Aha moment" en 3 secondes
- Version standalone qui raconte l'histoire complète sans texte d'accompagnement

C'est typiquement le **Chart B** (le scatter ou le ridge plot, pas le hero line chart).

### 10.4 Les autres règles data viz

Les standards Eco3min (sourcing intégré dans le chart, AMF visuel, anti-patterns 3D / pie / double Y, accentuation des majuscules, etc.) restent ceux du skill `visuels-eco3min`. Ce skill ajoute uniquement la dimension narrative ci-dessus.

---

### 10.5 Discipline de génération

Le script de chart **lit le CSV** (`parse_dates` là où c'est pertinent), imprime **chaque valeur annotée**, et se termine par un **bloc d'assertions** vérifiant chaque annotation contre le CSV.

Puis : **inspecter visuellement chaque chart** avec l'outil de vue, et corriger chevauchements et troncatures avant livraison, avec contrôle de lisibilité à 380 px.

Exports : page ~1400×750 · OG 1200×630 · social autonome 1920×1080 pour le chart destiné à r/dataisbeautiful quand il est poussé.

---

### 10.6 Le chart interactif — livrable obligatoire

Les charts statiques restent la preuve citable et l'image OG. Le chart interactif
est ce qu'un lecteur de Hacker News manipule avant de décider s'il upvote, et ce
qu'une IA ne peut pas résumer à la place du lecteur. Il **s'ajoute**, il ne
remplace rien.

**Contrat technique.** SVG construit en JavaScript natif, **aucune bibliothèque
externe** — pas de CDN, pas de dépendance qui pourrira, aucun tiers qui voit le
lecteur. Le markup est un conteneur à attributs `data-*` dans le corps HTML ; tout
le JS vit dans le snippet, parce que le corps ne contient ni `<style>` ni
`<script>` (§20.2). La donnée vient du **CSV publié de l'étude**, servi en
same-origin depuis `uploads/[YYYY]/[MM]/`.

**Contrat d'audit.** Toute valeur affichée par le module vient d'une colonne du
CSV. Le module ne calcule rien qui ne soit pas déclaré ; une transformation
déclarée est assertée dans `compute_stats.py` comme n'importe quelle autre
statistique (§18.2). Les valeurs affichées par défaut — typiquement la dernière
observation — entrent dans le périmètre imprimé du Step 4.

**Contrat AMF.** Descriptif uniquement. Pas de flèche directionnelle, pas de zone
« acheter / vendre », pas de projection, pas de seuil présenté comme un signal
d'action. Les bandes grisées ne portent que des **épisodes datables et sourcés**,
jamais des zones interprétatives. Les règles de `visuels-eco3min` s'appliquent au
survol et aux étiquettes comme aux charts statiques.

**Dégradation, non négociable.** Si le fetch échoue, si le CSV est malformé, ou si
JS est absent, le `<picture>` de repli contenu dans le conteneur reste affiché et
la page reste complète et citable. Le module ne retire le repli qu'**après** un
rendu réussi. Tester le repli réseau coupé — le supposer ne suffit pas.

**Vérifications avant livraison** : le CSV est en ligne à l'URL exacte et au bon
mois · chaque colonne déclarée existe dans l'en-tête au caractère près · trois
valeurs échantillonnées au survol correspondent au CSV · le repli s'affiche réseau
coupé · Tab atteint le graphe et les flèches déplacent le curseur · lisible à
380 px.

Le code de référence, les attributs et le CSS vivent dans le `snippet_model.php`
du projet de série, section « INTERACTIVE CHART ».

---

## 11. Loaded-terms scan (post-production)

Avant publication, scanner le contenu complet pour ces termes :

```
destruction, tax (en contexte inflation), manipulation, failed,
should (prescriptif), will (certitude), obviously, clearly,
undeniably, proves that
```

Tout match → supprimer, remplacer, ou justifier (entre guillemets attribués avec contre-argument).

### 11.1 Output du scan

```
LOADED-TERMS SCAN:
- Termes trouvés : [liste]
- Termes corrigés : [liste]
- Termes conservés avec justification : [liste]
- Hook visible above the fold : OUI / NON
- Status : PASS / FAIL
```

---

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

## 15. r/economics pre-flight (avant submission Reddit)

Si le contenu est destiné à être posté sur r/economics, vérifier :

- [ ] Titre Reddit : ZÉRO terme chargé
- [ ] Titre Reddit : énonce un FINDING avec des chiffres
- [ ] Titre Reddit : inclut une fenêtre de dates ou un nombre d'observations
- [ ] Self-comment : finding + taille d'échantillon + "CC BY 4.0, methodology in comments"
- [ ] H1 du contenu : provocant OK, jugement normatif PAS OK
- [ ] 3 premiers paragraphes : 100 % factuel
- [ ] Context-box présent dans la première section analytique
- [ ] Beat 3 présent dans les 2 sections suivant Beat 2
- [ ] Aucun langage prescriptif sur la page

Si une seule case échoue, le post sera modéré ou hued. La rigueur ici protège l'investissement de production.

---

## 16. Checklist éditoriale pré-publication

**Backlink Hook**
- [ ] Hook défini avant production (≤25 mots, statistique frappante)
- [ ] Hook visible above the fold
- [ ] Hook dans TL;DR + 1er bullet Executive Summary + social snippets
- [ ] Hook compréhensible sans lire la page entière

**Adversarial Pre-Review**
- [ ] 4 reviewers simulés avant fetch des données
- [ ] Chaque attaque a une défense localisée dans le contenu
- [ ] Les changements de design issus de la pre-review sont implémentés

**Structure narrative**
- [ ] Beat 1 énoncé fairly (pas de strawman)
- [ ] Beat 2 = contradiction empirique chiffrée
- [ ] Beat 3 présent et substantiel (pas une phrase token)
- [ ] Beat 3 dans les 2 sections suivant Beat 2

**Anti-editorializing**
- [ ] Loaded-terms scan effectué et fixé
- [ ] Yield Curve Lesson appliquée (data + tableau + FAQ + methodology forcent les citations sans commentaire)
- [ ] H1 sans jugement normatif
- [ ] 3 premiers paragraphes 100 % factuels

**Data accuracy production** (si CSV produit)
- [ ] Tous les chiffres du contenu viennent du CSV
- [ ] Statistiques calculées via Python, copiées depuis stdout
- [ ] Épisodes historiques vérifiés ligne par ligne
- [ ] Direction vs niveau vérifiés séparément
- [ ] Chiffres hors-CSV marqués `<!-- SOURCE -->` ou `<!-- VERIFY -->`

**Audit extractif CSV-led (section 12)**
- [ ] Verifier CSV-led extractif produit (énumère depuis CSV, pas depuis HTML)
- [ ] Toutes les catégories de statistiques de la section 12.3 listées dans le verifier
- [ ] Seuils de tolérance respectés (section 12.5) — pas d'arrondi optimiste
- [ ] 100% des claims présents dans HTML vérifiées au verifier
- [ ] **0 failure** dans le verifier (pas de seuil "tolérable")

**Cohérence multi-livrables (section 13)**
- [ ] Tous les claims numériques répétés grep-ifiés dans TOUS les fichiers (HTML, PHP, MD)
- [ ] Single-source-of-truth table maître documentée
- [ ] Après toute correction d'une valeur : grep ancien-et-nouveau effectué dans TOUS les fichiers
- [ ] Liste finale 13.5 des fichiers parcourue

**Patterns à haut risque (section 14)**
- [ ] Toutes les claims "within X of Y" vérifiées arithmétiquement (14.1)
- [ ] Toutes les claims superlatives "since DATE" vérifiées par lookup CSV (14.2)
- [ ] Tous les comptages appariés à leur filtre exact dans `compute_stats.py` ET la prose (14.3)
- [ ] Aucun arrondi optimiste — précision matche la donnée (14.4)
- [ ] Tout "approximately X" a une justification documentée dans `hedge_justifications.json` (14.5)

**Forward distributions / Surveillance** (si applicable)
- [ ] Disclaimer légal présent ("Past distributions are not predictive...")
- [ ] Surveillance block en 3 éléments (invalidation, confirmation, catalyst)
- [ ] Aucune formulation prescriptive
- [ ] Marqueur `<!-- UPDATEABLE -->` présent

**Chart**
- [ ] Type de chart choisi pour matcher la donnée (pas template forcé)
- [ ] Justification d'échelle documentée
- [ ] Chart B fonctionne standalone pour r/dataisbeautiful
- [ ] Subtitle = takeaway journalistique, pas description d'axe

**Critère final**
- [ ] La page passe le test : un journaliste FT pressé peut citer le hook **dans les 30 secondes** sans lire la suite
- [ ] La page passe le test r/economics pre-flight (zéro point de friction modérateur)
- [ ] Le verifier extractif rapporte 100% des claims du HTML vérifiées contre le CSV (section 12)

---

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

### 17.3 Workflow Step 0 → Step 10

```
Step 0     → BACKLINK HOOK (§2)
Step 0.5   → PRE-FLIGHT DU SLUG : choisir le slug, vérifier sa disponibilité
             dans WP (le motif de collision « -2 » a frappé au moins 3 études).
             Vérifier le dossier du mois d'upload [YYYY]/[MM]. Vérifier chaque
             slug de lien interne prévu contre le snapshot du site.
             Verrouiller l'INVENTAIRE DES CHARTS et leurs noms de fichiers.
Step 1     → Lire le brief dans le fichier de mapping (statut + cannibalisation)
Step 1.5   → PRE-REVIEW ADVERSE (§3) — c'est un livrable
Step 2     → Récupérer la donnée, y compris les séries défensives issues du 1.5 (§23)
Step 3     → Construire le CSV, colonnes défensives comprises
Step 4     → compute_stats.py — TOUTES les statistiques qui apparaîtront où que
             ce soit, organisées par section (périmètre imposé en §18.2), bloc
             FILTERS canonique en tête, imprimées sur stdout.
             Sauver intermediate_stats.json POUR LA PRODUCTION UNIQUEMENT —
             jamais comme source d'audit (Verrou A).
Step 5     → Écrire le HTML : défenses intégrées, valeurs copiées DEPUIS stdout,
             formulation concept-cohérente (Verrou B), chaque filtre temporel
             formellement défini (Verrou F)
Step 6     → AUDIT EXTRACTIF (§12) : EXTRACT → VERIFY (recalcul depuis le CSV
             brut uniquement) → GATE (couverture 100 %)
Step 6.5a  → Scan des termes chargés + vérification des défenses + citabilité
Step 6.5b  → Tripwire de direction narrative (claims datés contre CSV)
Step 6.5c  → Audit d'appariement concept-nombre (Verrou B)
Step 6.5d  → Scan automatique des hedges + hedge_justifications.json (Verrou D)
Step 6.5e  → Contrôle d'assertion des claims de comptage (Verrou E)
Step 6.5f  → Contrôle de formalité des filtres (Verrou F)
Step 6.5g  → Verrous éditoriaux (Verrou G) : zéro cadratin, zéro tic IA,
             zéro verbe prescriptif, zéro langage d'action ou de timing
Step 7     → Snippets sociaux (§15 pre-flight r/economics)
Step 8     → Specs des charts (justification d'échelle) + vérification visuelle
Step 8b    → CHART INTERACTIF (§10.6) : module SVG en JS natif alimenté par le
             CSV publié, markup data-* dans le corps, JS dans le snippet, repli
             <picture> testé réseau coupé, clavier et 380 px vérifiés
Step 9     → Guide d'upload des images
Step 10    → Assembler et livrer le jeu complet, résumé d'audit inclus
```

**Tout échec en 6 ou 6.5a-g → HALT. Pas de livraison.**

### 17.4 Mode opératoire

Les études se demandent **une à la fois** (« Produce Study C6 — Gold Real ATH »).
Dérouler Step 0 → Step 10 dans une seule conversation, de façon autonome, étape
par étape, **sans s'arrêter pour approbation**, puis livrer le jeu complet.

Si l'angle du mapping est faible ou contredit par la donnée : pivoter selon la
doctrine (§3.6), le signaler, et produire quand même.

**Sortie canonique unique** : un slug, un H1, un jeu de metas. Pas de variantes.

---

## 18. Le système de verrous A→G

Les §7 et §12 à §14 posent les règles d'écriture et l'audit extractif. Cette
section les **nomme** et ajoute les contrôles mécaniques qui manquaient. Chaque
verrou est né d'une erreur réelle livrée en production (§24).

### 18.1 Les dix règles d'écriture (avant le Step 5)

1. **Le CSV est la source unique de vérité.** HTML ≠ CSV → c'est le HTML qui a
   tort.
2. **Calculer avant d'écrire.** Toute valeur quantitative de tout livrable a été
   calculée en Python et imprimée sur stdout, puis copiée. Jamais de mémoire,
   jamais estimée à l'œil sur un chart.
3. **« Approximately / roughly / about / around / ~ » est interdit** pour toute
   valeur calculable depuis le CSV. Autorisé uniquement pour : valeurs externes
   non récupérables (`<!-- SOURCE -->`), vérification en attente
   (`<!-- VERIFY -->`), arrondi narratif documenté (« ten-fold » pour 10,36×, le
   chiffre exact énoncé à proximité). Chaque occurrence exige une entrée dans
   `hedge_justifications.json` avec son motif : `external_unverifiable`,
   `verify_pending` ou `narrative_rounding`.
4. **Claims « X of top N »** : classement Python explicite → filtre → comptage →
   impression → copie.
5. **Claims de comptage** (« N events / onsets / observations dans [période] ») :
   assertion Python sur filtre explicite. Sans exception.
6. **Filtres temporels en prose** (« excluding X », « pre-Y », « ex-COVID ») :
   définition formelle dans un dict `FILTERS` canonique en tête de
   compute_stats.py **et** dans le bloc « Filter Definitions » du HTML.
7. **Formulation concept-cohérente** : un nombre juste attribué au mauvais
   concept est une erreur. Longueur de série ≠ délai d'avance. Motifs suspects :
   « only N consecutive [units] » contre « N [units] lead/ahead of » — vérifier
   que la formule correspond au concept énoncé en prose.
8. **Points de retournement historiques** : lookups ligne à ligne
   `df[df.date>=...].iloc[0]`, impression de tous les composants, **piège des
   deux dates** — chaque date traitée séparément.
9. **Claims de direction de régime** : variation de niveau (`df[end]>df[start]`)
   ≠ direction du YoY (`yoy>0`). Vérifier celle qui est réellement affirmée.
10. **Cohérence inter-livrables** : HTML, JSON-LD du PHP, snippets sociaux,
    textes alt et annotations de chart portent les MÊMES valeurs. Une statistique
    fausse se propage 6 fois ou plus. L'audit balaie **tous** les livrables, pas
    seulement le HTML. (Voir §13.)

### 18.2 compute_stats.py — périmètre imprimé obligatoire

`[LATEST OBSERVATION]` · `[EXECUTIVE SUMMARY VALUES]` · `[STATS PANEL]` ·
`[FORWARD RETURNS TABLE]` — par régime **plus chaque union de régimes et chaque
sous-période mentionnée où que ce soit en prose**, plus les variantes ex-COVID si
elles sont mentionnées · `[CHART ANNOTATIONS]` — chaque valeur datée de chaque
chart · `[TURNING POINTS]` — dumps de lignes complètes · `[INTERP-GRID VALUES]` —
chaque comptage et pourcentage de chaque carte · `[SURVEILLANCE BLOCK]` ·
`[COUNTING STATISTICS]` — chaque comptage en prose via filtre explicite et
assertion · `[METHODOLOGY]` — sorties de sensibilité · plus le bloc `FILTERS`
canonique en tête.

**Une section absente de stdout → le Step 6 ÉCHOUE.**

### 18.3 Les sept verrous

| Verrou | Ce qu'il bloque | Où il s'exécute |
|---|---|---|
| **A** | Un fichier intermédiaire qui sert de source de vérité à l'audit | Step 6, PASS 2 |
| **B** | Un nombre juste attribué au mauvais concept | Step 6.5c |
| **C** | Une statistique dérivée hors périmètre de calcul (unions, sous-périodes) | Step 4 |
| **D** | Un hedge interdit utilisé quand même | Step 6.5d |
| **E** | Un comptage lu à l'œil sur un chart | Step 6.5e |
| **F** | Un filtre temporel ambigu | Step 6.5f |
| **G** | Une règle éditoriale de `editeur-eco3min` violée sans que rien ne la signale | Step 6.5g |

**Verrou A — la règle la plus importante.** Au PASS 2, chaque valeur extraite doit
être adossée à une assertion Python **recalculée depuis le CSV brut**, avec
tolérance explicite. **Aucun fichier intermédiaire** — `locked_stats.json`, dumps
de stdout, `intermediate_stats.json` — ne peut servir de source de vérité à
l'audit : **l'audit ne charge que le CSV brut.** Sinon une valeur fausse
s'auto-valide. C'est exactement ce qui a produit 14 copies d'une même erreur à
l'étude #20.

**Verrou B — appariement concept-nombre (Step 6.5c).** Pour chaque nombre en prose
analytique — Beats, méthodologie, FAQ, surveillance ; les cellules de tableau sont
exemptes, leur concept est l'en-tête de colonne — déclarer
`(number, concept_label, python_formula_str, expected)` dans `CONCEPT_PAIRINGS`,
exécuter la formule, apparier la valeur, et vérifier heuristiquement la
compatibilité concept ↔ contexte de la phrase par correspondance de mots-clés sur
les motifs suspects de la règle 7.

**Verrou C — unions et sous-périodes.** Toute union de régimes et toute
sous-période mentionnée en prose est calculée dans compute_stats.py, jamais de
tête.

**Verrou D — scan des hedges (Step 6.5d).** Grep automatique de
`approximately|roughly|about|around|~|close to` suivi d'un chiffre. Chaque
occurrence justifiée dans `hedge_justifications.json`, ou ÉCHEC.

**Verrou E — claims de comptage (Step 6.5e).** Grep automatique de
`N events / occurrences / observations / onsets / episodes / recessions /
false positives / triggers / crossings / cases / instances / times / weeks /
months / years`, ainsi que `N/M` et `N of M`. Chaque occurrence exige une
assertion dans compute_stats.py qui produit exactement ce N.

**Verrou F — formalité des filtres (Step 6.5f).** Grep automatique des expressions
de filtre temporel ; chacune doit exister dans le dict `FILTERS` **et** dans le
bloc « Filter Definitions » du HTML.

**Verrou G — verrous éditoriaux (Step 6.5g).** Les six verrous ci-dessus ne
regardent que des nombres. Les règles de `editeur-eco3min` sont invisibles pour
eux, et ne se dérivent d'aucun CSV : rien ne les signale, ni à l'écriture, ni à
la relecture. Elles se grepent, comme les hedges.

- **Zéro cadratin ( — )** dans tout livrable destiné au site — corps HTML,
  package social, metas, alt et title. Ruptures : virgule, deux-points,
  parenthèses, ou deux phrases. Les plages gardent le demi-cadratin (`1959–2007`)
  et les valeurs négatives le signe moins (`−0,013`). Règle durcie juillet 2026,
  validée programmatiquement côté pipeline B.
- **Zéro tic IA** de la liste de `editeur-eco3min` §5, versant EN compris :
  `worth noting`, `delve`, `dive into`, `ever-evolving`, `paradigm shift`,
  `as we navigate`, `in conclusion,`, `truly`, `literally`, `undeniably`,
  `fundamentally`.
- **Zéro verbe prescriptif** appliqué à un profil (`should`, `must`, `need to`,
  `ought to`, `we recommend`) et **zéro langage d'action ou de timing**
  (`buy`, `sell`, `entry point`, `price target`, `now is the time`,
  `overweight`, `underweight`). Règles AMF 2, 3 et 6.

Mesuré sur l'étude R1 (08/09/2026) : **43 cadratins dans le corps et 18 dans le
package social**, alors que l'audit extractif passait à 100 % sur 163 claims et
que les trois autres scans étaient propres. Un audit numérique ne voit pas une
règle de doctrine.

### 18.4 Step 6.5a — audit post-production

Relire le document du Step 1.5 et vérifier que **chaque défense est présente**.
Scan des termes chargés (§11). Citabilité : le hook est-il au-dessus de la ligne
de flottaison, en premier bullet de l'Executive Summary, et dans la TL;DR ?
Sortie : défenses N/N · termes trouvés/corrigés · hook visible OUI/NON ·
PASS/FAIL.

### 18.5 Step 6.5b — tripwire de direction narrative

Chaque date `YYYY-MM` en prose devient un tuple
`(label, date, csv_column, expected, tol)` dans `NARRATIVE_EVENTS`, ou une entrée
justifiée dans `WHITELISTED_NO_CLAIM`. Exécuter
`narrative_audit.run_narrative_checks(...)` en mode strict.

Attrape : les erreurs de direction, les valeurs datées de pic ou de creux fausses,
les étiquettes de régime fausses, les dates en prose absentes du CSV.
N'attrape pas : les claims de tendance non datés, les claims causaux, les erreurs
internes au CSV.

### 18.6 Périmètre du Step 6 — les sections historiquement oubliées

L'extraction du PASS 1 couvre explicitement : les **sous-titres de charts**, les
**comptages des interp-grids**, les **encarts takeaway**, les **bullets de
surveillance**, et les **textes alt et title des images**. Ce sont précisément
celles que les audits déclaratifs sautent.

### 18.7 Ce que le système ne couvre pas — limites assumées

- Les erreurs **à l'intérieur du CSV** (bugs de `build_csv`). La protection reste
  le Step 1.5 et une passe manuelle de bon sens sur le CSV.
- La **mésinterprétation économique** : corrélation prise pour causalité, seuils
  ad hoc choisis pour maximiser la performance. C'est le travail du Step 1.5.
- Les erreurs **dans un chiffre externe légitimement cité** : leur exactitude
  repose sur la source.

Quand une erreur est découverte après livraison : ajouter son motif au registre
(§24) et son verrou au workflow. Les motifs inconnus futurs exigeront leurs
propres verrous.

---

## 19. Structure de la page HTML — ordre imposé

28 blocs, dans cet ordre. Le markup est dans le template de page de référence.

1. Wrapper `eco3-[STUDY]` > `-container`
2. **Hero** : chapeau = le hook développé → `<picture>` chart hero → chapeau de
   positionnement → ligne de méta. Le H1 vit dans le champ titre de WP ; la même
   chaîne sert de `headline` JSON-LD et d'`og:title`.
3. **Intro SEO** — 3 à 4 phrases, mot-clé en tête, 100 % factuel, zéro adjectif
   normatif. Registre dépêche Reuters.
4. **TL;DR** — le hook + les chiffres clés en gras + une phrase de divulgation de
   robustesse s'il y en a une + un caveat de périmètre renvoyant à #methodology
   et #limitations.
5. **Sommaire** — les ancres doivent correspondre aux id de section, l'audit le
   vérifie.
6. **Latest Observation** — 4 métriques, marquées `<!-- UPDATEABLE -->`.
7. **Executive Summary** — 4 à 6 bullets. Le premier est le hook. Au moins un qui
   conteste le consensus, un d'actualité, un de force méthodologique. Le dernier
   porte la reproductibilité et la licence CC BY 4.0.
8. **Barre de téléchargement** (1re occurrence) + ligne nombre d'observations et
   licence.
9. **Panneau de stats** — 5 à 6 cartes.
10. **Section du chart principal** — figure avec sous-titre journalistique et
    prose « comment lire ».
11. **Vue supplémentaire** si l'amplitude du chart principal dépasse 5× —
    complément linéaire, éventuellement un chart transformé (barres divergentes
    de variation en %).
12. **Beat 1** — le consensus, énoncé loyalement, en expliquant pourquoi il
    paraissait vrai.
13. **Beat 2** — la contradiction empirique, avec son mécanisme. **Encart de
    contexte obligatoire** dans la première séquence analytique : contexte
    structurel et ce que le dataset **ne mesure pas**, avec un contre-fait
    concret et un `<!-- SOURCE -->`.
14. **Beat 3** — le steelman, au plus deux sections H2 après le Beat 2. Au moins
    un élément parmi : contre-fait chiffré, qualification structurelle,
    interprétation alternative, caveat de taille d'échantillon, reconnaissance de
    ce sur quoi l'adversaire de la thèse a raison. Les divulgations de robustesse
    complètes vivent ici.
14b. **Figure interactive** (§10.6) — le conteneur `data-eco3-live` avec son
    `<picture>` de repli, placé après le Beat 3 : le lecteur a lu la thèse et sa
    limite, il veut maintenant manipuler la série lui-même. Sous-titre = invitation
    à explorer, pas répétition du takeaway du chart hero.
15. Section **spotlight** optionnelle, avec sa propre figure.
16. **Forward distribution** — benchmark naturel, conditionnel au régime, unions
    de régimes calculées si mentionnées (Verrou C), caveat si n<15, note sur les
    fenêtres chevauchantes, et la ligne légale : « Past distributions are not
    predictive of future outcomes… ».
17. **Levels to Watch** — 3 à 4 cartes d'interprétation, marqueurs **descriptifs
    uniquement**, `<!-- UPDATEABLE -->`. Motif : « if [condition observable], then
    [changement de régime], historically associated with [résultat factuel] ».
    JAMAIS buy / sell / should. (Voir §9.)
18. **Tableau(x) de données** — au moins un en pleine largeur : décennies,
    épisodes ou régimes.
19. **Points de retournement historiques** — 3 à 5 épisodes plus l'observation
    courante. Lookups ligne à ligne, piège des deux dates, comparaisons
    directionnelles énoncées dans les deux sens à la première occurrence.
20. **Méthodologie** — formules en formula-box ; algorithme formel des épisodes et
    régimes ; sensibilité (±1 unité, ±20 %) ; ancrage dans la littérature, ou la
    phrase de périodisation NBER ; **bloc Filter Definitions** dès qu'un filtre
    temporel apparaît en prose (Verrou F) ; tableau de design du dataset ; code
    Python de reproduction.
21. **Téléchargement** (2e occurrence)
22. **Lien vers le hub de données** — slug vérifié
23. **Sources** — 5 à 8, dont au moins 2 académiques ; intégrées en prose ou en
    liste de badges
24. **Limitations** — 4 à 6 : révisions, composition, non-stationnarité, fenêtres
    chevauchantes, ex-post contre ex-ante, date de départ, caractère rétrospectif
25. **FAQ** — 5 à 6 vraies requêtes Google, dont au moins une **défensive** et une
    de **périmètre**. Reprise **verbatim** dans le FAQPage du snippet.
26. **Encart de citation**
27. **Kit de partage et embed** — optionnel, pour les killers et quasi-killers
28. **Related** (slugs vérifiés) + footer

**À l'échelle de la page** : au moins 3 encarts takeaway, au moins 2 tableaux de
données (ou un tableau plus une grille d'interprétation), et **au moins 8 liens
internes tissés dans la prose**. La page dataset brute appariée est le lien le
plus important. Ne jamais lier un slug absent du snapshot.

---

## 20. Architecture de déploiement (vérifiée sur WordPress)

### 20.1 Namespace CSS par étude

Chaque classe est `eco3-[STUDY]-*`, où `[STUDY]` est un code court propre à
l'étude. Le namespace partagé `eco3-realrates` est **retiré**.

Le bloc CSS scopé — environ 12 000 caractères, 63 classes canoniques — s'extrait
par curl depuis **l'étude publiée la plus récente**, puis se re-namespace. Jamais
reconstruit de zéro, jamais repris d'une page ancienne qui pourrait ne pas avoir
les règles de l'accordéon FAQ.

### 20.2 Le snippet est autonome

Un Code Snippet par étude. Ordre : fonction de garde (slug + variante `-2`) → CSS
scopé (`wp_head` priorité 4) → JSON-LD Article/Dataset/FAQPage (`wp_head`
priorité 5) → meta OG et Twitter (`wp_head` priorité 99) → filtres RankMath
title/description (priorité 99, **jamais** l'onglet Social) → JS (`wp_footer`
priorité 99 : délégation FAQ sur `document` avec drapeau anti-double-init, copie
de partage, sélecteur d'embed, sommaire mobile).

**Le corps HTML ne contient ni `<style>` ni `<script>`** : WordPress et Autoptimize
les retirent ou les réordonnent quand ils sont dans le contenu.

### 20.3 Règles WordPress dures

- **UTF-8 littéral** dans les `content:""` du CSS — WP supprime les échappements
  de type `\2713`.
- Code Snippets se colle **sans balise `<?php` ouvrante**.
- Le heredoc `<<<'CSS'` est l'alternative valide pour embarquer le CSS.
- URL d'assets en `wp-content/uploads/[YYYY]/[MM]` avec le **mois courant**,
  identiques dans le HTML, le snippet et les guides.
- WP peut créer des variantes `-scaled` des PNG : **référencer les originaux non
  suffixés**.
- Uploader les SVG — c'est la `<source>` primaire du `<picture>`.

### 20.4 Discipline de slug

Vérifier la disponibilité **avant** production. Si WP attribue un `-2`, le
propager à : la fonction de garde, le `@id` / `mainEntityOfPage` / `url` du
JSON-LD, l'`og:url`, l'encart de citation, le package social. Un fragment
orphelin fait échouer la garde.

⚠️ **D'où vient ce `-2`, et comment ne plus jamais le subir.** Ce n'est pas WP qui
est capricieux : `wp_unique_post_slug()` vérifie `post_type IN ('page',
'attachment')`, donc **une pièce jointe occupe l'espace de noms des slugs de
page**. Le CSV de l'étude, nommé comme le slug, prend le slug ; le XLSX prend le
`-2` ; la page ne peut plus obtenir que le `-3`. La règle est donc en amont :
**le nom de base des assets n'est jamais le slug de la page**, et le bundle
s'importe **avant** l'upload des données. Autorité complète, assertion de build,
diagnostic en une ligne et procédure de réparation :
`eco3min-import-contenu-bilingue`, section « Le slug de page ne doit JAMAIS être
le nom de base d'un asset ».

### 20.5 Mécanisme FAQ

Un `<h3>` à l'intérieur de `.eco3-[STUDY]-faq-item`, qui bascule
`.eco3-[STUDY]-open`.

### 20.6 Conventions de chemins

- Données et charts :
  `https://eco3min.fr/wp-content/uploads/[YYYY]/[MM]/[fichier]`, mois courant.
- Noms de charts : `[study-slug]-hero-v1.{png,svg,pdf}` et
  `[study-slug]-[descriptif]-v1.{png,svg,pdf}`.
- L'image OG **est** le PNG hero. Pas de rendu OG séparé, sauf poussée forte :
  alors 1200×630.
- Liens internes : `/en/` côté EN, vérifiés contre le snapshot.
- Embeds : `https://eco3min.fr/embed/[chart-slug]`.

---

## 21. Checklist consolidée du pipeline

Complète la checklist éditoriale du §16.

**Structure** : H1 spécifique + période + amorce d'insight, ≤110 · TL;DR
hook + robustesse + périmètre · latest-obs 4 · exec 4-6 dont le premier = hook ·
stats 5-6 · figure hero + sous-titre journalistique · prose « comment lire » ·
vue supplémentaire si >5× · 3 à 5 H2 analytiques avec mécanismes · Beats 1→2→3,
le 3 au plus deux sections après le 2 · encart de contexte · ≥2 tableaux ou
grilles · ≥3 takeaways · forward distribution + disclaimer · Levels to Watch 3-4 ·
points de retournement + observation courante · méthodologie (algorithme +
sensibilité + Filter Definitions + Python) · FAQ 5-6 (défensive + périmètre) ·
citation · related 3-6 vérifiés · footer.

**Intégrité des données** : CSV en premier · chaque valeur issue de stdout ·
PASS 1/2/3 exécutés, couverture 100 %, **audit recalculé depuis le CSV brut
uniquement** · sous-titres de charts, interp-grids, takeaways, surveillance et
textes alt assertés · aucun hedge injustifié (`hedge_justifications.json`
complet) · aucun claim de comptage sans assertion · aucun filtre temporel
informel · appariements concept-nombre vérifiés · tripwire narratif propre ·
points de retournement vérifiés ligne à ligne · directions de régime vérifiées ·
cohérence des valeurs entre livrables.

**Chart interactif** : présent · aucune bibliothèque externe · alimenté par le
CSV publié à l'URL exacte · chaque colonne déclarée existe dans l'en-tête · trois
valeurs de survol échantillonnées contre le CSV · repli `<picture>` testé réseau
coupé · navigable au clavier · lisible à 380 px · bandes grisées limitées à des
épisodes datables et sourcés · zéro élément prescriptif.

**Backlink** : hook défini au Step 0 · présent en TL;DR, en Exec-1 et dans le
social · compréhensible à froid · sous-titres = takeaways · type de chart dicté
par la donnée.

**Éditorial** : trois premiers paragraphes factuels · Beat 3 sincère (au moins une
concession) · « le système a fonctionné » reconnu là où c'est vrai · robustesse
divulguée, pas cachée · ≥8 liens internes vérifiés contre le snapshot · zéro
conseil, zéro certitude · **zéro cadratin dans tout livrable destiné au site,
zéro tic IA, zéro verbe prescriptif, zéro langage d'action (Verrou G)** · les
deux pre-flights et tous les audits en PASS.

**Sourcing** : chaque série FRED destinée à une colonne publiée vérifiée sans le
marqueur « Copyrighted: Citation Required » · niveaux recoupés contre l'émetteur,
pas contre le canal de redistribution · `provenance.md` complet.

**Technique et déploiement** : pre-flight du slug fait · le corps n'a ni style ni
script · namespace `eco3-[STUDY]-*` cohérent (un grep du placeholder ne renvoie
rien) · snippet complet (CSS, JSON-LD, OG, RankMath, JS, anti-double-init,
délégation) · JSON-LD validé · FAQ de la page et du schéma identiques au mot près ·
`uploads/[YYYY]/[MM]` correct et identique partout · `-2` propagé si applicable ·
alt et title sur chaque image · charts inspectés visuellement ·
`<!-- UPDATEABLE -->` sur latest-obs et surveillance · preview rendue et vérifiée.

---

## 22. Package social (livrable 14) et guide d'upload (livrable 15)

### 22.1 Package social

- **RankMath meta title** ≤60 : `[Insight central] — [Dataset] ([Années]) | Eco3min`
- **Meta description** ≤155 : le hook en une phrase
- **OG title / description** ≤200
- **X** ≤280 · **LinkedIn** ~600
- **r/economics** : factuel, orienté dataset, zéro terme chargé, avec la période
  couverte ou le nombre d'observations
- **r/dataisbeautiful** : `[OC]`, visuel signature
- **r/investing** : question ou insight
- **Self-comment** : 3 à 4 lignes — le résultat, sa taille, et « CC BY 4.0, happy
  to discuss methodology »
- **HN** ≤80, factuel

Le pre-flight r/economics obligatoire est en §15.

### 22.2 Guide d'upload des images

Par fichier : **Title** WP (≤60) · **Alt** (identique à l'alt du HTML) ·
**Caption** (le sous-titre du chart) · **Description** (2 à 3 phrases : quoi, le
résultat, l'attribution).

Plus : uploader SVG **et** PNG, plus le PDF en archive · la règle de l'original
non suffixé (§20.3) · les chemins `uploads/[YYYY]/[MM]` exacts · la justification
d'échelle de chaque chart.

---

## 23. Acquisition des données — playbook

La **légalité et la hiérarchie des sources** restent l'affaire de
`sourcing-donnees-eco3min`, qui fait autorité, et dont l'annexe B porte les
endpoints et leurs pièges. Ce qui suit est ce qui est propre aux études.

- **World Bank Pink Sheet** (matières premières, 1960→, annuel et mensuel,
  gratuit) : curl direct du XLSX depuis `thedocs.worldbank.org`. Si le jeton
  tourne, re-localiser depuis worldbank.org/commodity-markets. Feuilles d'indices
  annuels : **les données commencent ligne 10** ; nominal et réel MUV ; colonnes
  Fertilizers et Precious Metals incluses, plus le déflateur MUV.
- **CPI US** : API World Bank `FP.CPI.TOTL` (1960→T-1, base 2010=100), chaînée
  avec BLS v1 `CUUR0000SA0` pour l'année courante. Bizarreries de BLS v1 :
  **ignore les filtres d'année** (parser par année soi-même), sauter `M13`,
  sauter les valeurs `'-'`. Une moyenne d'année partielle se divulgue comme telle.
- **FRED** : `curl fredgraph.csv?id={ID}` depuis Bash est la route de première
  intention, et elle marche. Testée 7 sources sur 7 en HTTP 200 le 04/09/2026
  (`sourcing-donnees-eco3min`, annexe B), 6 séries sur 6 le 08/09/2026 (étude R1).
  L'ancienne note « peu fiable, coupures d'egress, 403 » portée ici était vraie
  dans son environnement et à sa date ; elle est **retirée** parce que, non datée,
  elle détournait durablement de la route la plus rapide.
  **L'autorité sur les endpoints et leurs replis est `sourcing-donnees-eco3min`,
  annexe B** — ne pas redocumenter les points d'entrée ici, deux sources de vérité
  divergent toujours.
  ⚠️ **Le contrôle de licence est un GATE du Step 0, pas une vérification de fin
  de production.** Il se fait **avant** de mesurer la profondeur d'une série et
  avant d'écrire une ligne, sur **chaque série destinée à une colonne publiée**,
  et sur **chaque intrant** d'un composite — une série dérivée hérite du niveau
  le plus dur de ses intrants. FRED distingue **trois** statuts, pas deux, et ils
  n'ont pas les mêmes conséquences : *public domain: citation requested* → CSV
  CC BY 4.0 possible · *copyrighted: citation required* → publiable avec
  attribution mais **jamais** en CC BY 4.0 · *copyrighted: pre-approval required*
  → **rien** sans accord écrit du détenteur, sur un site commercial. Le détail
  des trois niveaux, la commande de contrôle et la sortie applicable à chacun
  sont dans `sourcing-donnees-eco3min`, section « Cas FRED » — **autorité unique,
  ne pas les redocumenter ici**.
  Deux cas vécus. R1 (08/09/2026) : `USREC` et `M2V` sont « citation required » ;
  la colonne de récession a été reconstruite depuis les pics et creux du NBER,
  avec assertion qu'elle reproduit `USREC` à l'identique. R5 (10/09/2026) : les
  séries ICE BofA sont « pre-approval required », ce qui a **tué l'étude au
  Step 0** — aucun historique, si long soit-il, ne rattrape une licence fermée.
  C'est pour ce second cas que le contrôle remonte du Step 10 au Step 0.
- **FAO FFPI** : classeur en téléchargement direct, CC BY 4.0.
- **Jacks 1850–2025 (XLSX)** : bloqué par captcha à l'automatisation. Le
  demander à la main si une extension centenaire est voulue.
- **yfinance et agrégateurs scrapés : interdits** comme source d'un CSV publié.
  Le footer nomme la **vraie** source des chiffres, jamais un relabel plus
  présentable.

**Règle d'arrêt.** Si une source nécessaire est bloquée : **s'arrêter et demander
les fichiers.** Ne jamais substituer la mémoire du modèle à une récupération
ratée.

---

## 24. Annexe — registre des motifs d'erreur

Post-mortems compressés. C'est l'origine du système de verrous : ne pas les
alléger sans relire cette annexe.

**Étude #22 — 6 erreurs, un seul mécanisme.** Des claims quantitatifs écrits dans
les sections « annexes » — sous-titre du Chart B, interp-grid de vélocité, encart
takeaway — **estimés visuellement, jamais calculés**. L'audit déclaratif ne
vérifiait que les claims dont le producteur se souvenait. Pires écarts : comptages
de régime à −51 % et +154 %.
→ D'où : audit extractif PASS 1/2/3, calculer-avant-d'écrire, restriction des
hedges, règle Top-N, périmétrage explicite des sections oubliées.

**Étude #20 — 10 erreurs, cinq motifs.**

- **A — une erreur, quatorze copies.** `finalize_stats.py` calculait `ma_above` à
  la dernière date au lieu de `trigger_8w` ; la valeur fausse est entrée dans
  `locked_stats.json`, **s'est auto-validée à travers l'audit**, puis s'est
  propagée dans le HTML (×3), le JSON-LD et le social (×3) : « 20-week run » pour
  4 réelles, « November 2025 » pour juillet, « 25 weeks » pour 42. → **Verrou A.**
- **B — bon nombre, mauvais concept (×2).** « 7 », qui était un délai d'avance à
  seuil 12 semaines, écrit comme « 7 consecutive weeks above the 52w MA » (série
  réelle : 18) ; et « missed » affirmé pour une récession pourtant détectée.
  → **Verrou B** (Step 6.5c).
- **C — statistique dérivée hors périmètre.** « B+A combined median +12.4 % » tapé
  de tête ; valeur réelle +14,07 %. → **Verrou C** (unions et sous-périodes
  obligatoires).
- **D — hedge interdit employé quand même.** « approximately 40 onsets » ; réel :
  36. → **Verrou D** (scan automatique + fichier de justification).
- **E — comptage lu sur le chart.** « 1985–86 (4 events) » ; réel : 3 dans la
  fenêtre. → **Verrou E** (une assertion par claim de comptage).
- **F — filtre ambigu.** « outside of 2020 » produisait deux écarts-types
  différents, 20 667 et 20 543. → **Verrou F** (définitions formelles).

**Étude #6.** « DGS2 easing pivot in November 1983 » alors que le CSV étiquetait
1983-11 en HIKE — **aucun nombre extractible à vérifier**. → D'où le tripwire de
direction narrative (Step 6.5b).

**Étude R1 (série GENERIQUE, 08/09/2026) — 4 défauts, un seul mécanisme : la
règle non chargée.** L'étude a été produite en chargeant 2 skills sur les 9
déclarées faisant autorité. L'audit extractif passait à 100 % sur 163 claims,
les chiffres étaient justes, la thèse tenait. Ce qui restait :

- **licence** : `USREC` et `M2V` portent le marqueur FRED « Copyrighted: Citation
  Required » ; `USREC` alimentait une colonne d'un CSV redistribué en CC BY 4.0.
  Rien dans la donnée ne le signale, il faut ouvrir la page de série.
  → D'où le contrôle de licence en §23 et la ligne Sourcing de la checklist §21.
- **typographie** : 43 cadratins dans le corps, 18 dans le package social, contre
  une règle à zéro. → **Verrou G.**
- **visuel** : bandes de récession non légendées sur deux charts
  (`visuels-eco3min` §2.2), et 3 des 4 assertions matplotlib de son §7 ter
  absentes du script. Une fois posées, la troisième a mordu immédiatement :
  14 % de recouvrement entre deux lignes de pied, invisible à l'œil à 7 pt.
- **traçabilité** : aucun registre de provenance. → D'où le livrable 17b.

**La leçon transversale** : un audit numérique, si exhaustif soit-il, ne protège
que de ce qu'il sait chercher. Aucun de ces quatre défauts n'est dérivable d'un
CSV — ce sont des règles de doctrine, et **une règle de doctrine non chargée
n'existe pas**. Le premier verrou du pipeline n'est pas le Step 6, c'est le
chargement des skills avant le Step 1.

**Validation du système** : si les verrous avaient été actifs à l'étude #20, les
10 erreurs auraient été bloquées avant livraison — vérifié motif par motif.

---

## RAPPEL BLOQUANT — Zéro commentaire HTML dans le contenu publié

Les marqueurs de section en commentaire HTML utilisés dans les templates de ce skill
(`<!-- 1. INTRO -->`, `<!-- 5. MACRO TAKEAWAY -->`, etc.) sont des **repères d'assemblage**.
Ils ne survivent pas dans le HTML livré : on les retire avant de coller le contenu ou d'émettre
le bundle.

Motif : Autoptimize scanne `<script>` / `<style>` en regex **sans ignorer les commentaires HTML**.
Une balise littérale citée en prose dans un commentaire fait avaler du texte au minifieur JS,
provoque une fatale dans le callback de buffer et renvoie un **HTTP 500 avec le corps complet** —
page normale dans le navigateur, invisible pour Google. Incident du 27 août 2026, 8 pages
désindexées. `wpautop` mutile en plus ces commentaires (enveloppe en `<p>`, saut de ligne inséré
au milieu dès qu'un nom de balise bloc y figure).

Règle canonique, vérifications mécaniques et alternative (commentaire PHP dans le snippet) :
voir `eco3min-import-contenu-bilingue`, section « RÈGLE FIGÉE (août 2026) ».

Contrôle avant livraison :

```python
import re
assert not re.findall(r'<!--.*?-->', html, re.S), "commentaire HTML dans le contenu"
```

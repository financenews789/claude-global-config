---
name: review-article-eco3min
description: Gate de review AVANT publication d'une page Eco3min chiffrée (étude, dataset, "Every X", chart page, FR/EN), déjà produite ou non. Couche d'orchestration QA : oriente vers l'audit extractif CSV-led de production-research-study §12-14 si le CSV existe, et fournit le fallback sans CSV (cohérence interne prose ↔ table ↔ cards — on certifie alors "cohérent", pas "100% exact"). Ajoute ce que les audits de valeurs ponctuelles ratent : tripwire de DIRECTION (claims de trajectoire type "declined steadily" contredits par le sentier réel), taxonomie des claims non-CSV (A issu du CSV / B sourcé externe / C inventé = interdit), cohérence inter-pages (pages sœurs), intégrité du CSV téléchargeable (trou, compteur), surface Rule IV / AMF. Produit un verdict GO/NO-GO rangé par criticité sans pushback fabriqué, et code la discipline de régénération (copie verbatim + str_replace + vérif). Activer pour "audite cette page", "review avant publication", "vérifie que c'est 100% exact".
---

# Review pré-publication — Eco3min

> Ce skill est le **gate qualité avant publication**, distinct de la production. Il s'applique à une page **déjà construite** (étude, dataset, "Every X", chart page, FR/EN) autant qu'à une page qu'on vient de produire. Il ne réécrit pas l'article : il le **certifie** — ou bloque — et corrige chirurgicalement.
>
> Voir aussi : `production-research-study` (audit extractif CSV-led §12, cohérence multi-livrables §13, patterns à haut risque §14 — ce skill les **oriente**, ne les duplique pas) · `editeur-eco3min` (AMF, termes proscrits) · `sourcing-donnees-eco3min` (légalité/provenance de la donnée publiée) · `narrative_audit.py` (module tripwire dates, Step 6.5b du projet killer studies).

---

## 1. Quand l'activer, et ce qu'il produit

**Activer** dès qu'on demande : « audite cette page », « review avant que je publie », « est-ce 100% exact ? », « vérifie avant le push r/economics », ou après toute régénération de page chiffrée.

**Entrées** :
- la page (bloc HTML/WP, FR ou EN) ;
- **le(s) CSV source(s) si elles existent** — c'est la source de vérité. Si absente, voir §3 branche B.

**Sortie** : un **verdict GO / NO-GO** avec findings rangés par criticité (§8). Jamais une liste fabriquée pour « faire rigoureux » : si rien de solide ne tient, le dire explicitement.

---

## 2. Principe cardinal : recompute, ne lis jamais

**Chaque nombre est recalculé depuis la source via Python. On ne lit jamais une valeur affichée pour la valider — l'afficher est précisément ce qui a pu l'introduire fausse.**

Corollaire — **le piège de l'œil** : avant de signaler une erreur, vérifier que c'est bien la prose qui a tort et non la fenêtre de calcul du reviewer. Exemple vécu : un sommet « 1,53 (1990-91) » semblait faux en fenêtre NBER stricte (donnait 1,20), mais devenait exact en fenêtre cycle-emploi (pic post-creux, juil. 1991 = 1,53). **Un flag qui se révèle faux coûte autant de crédibilité qu'une erreur ratée.** Choisir la bonne fenêtre, sanity-check, *puis* flagger.

---

## 3. Arbre de décision : avec CSV vs sans CSV

### Branche A — CSV disponible
→ **Audit extractif CSV-led** : appliquer `production-research-study` §12 (le CSV énumère les claims, pas l'inverse), §13 (multi-livrables), §14 (patterns à haut risque). Ce skill ajoute par-dessus les passes P3→P6 (§4).
→ On peut alors certifier **« 100% exact contre la source »**.

### Branche B — pas de CSV (la page seule)
→ **Audit de cohérence interne**. La **table affichée devient la source de vérité de second rang**. On vérifie que tout concorde :

> prose ↔ table ↔ stat cards / ticker / chiffres du hero / alt-text / caption / snippets sociaux

→ On certifie seulement **« cohérent en interne »**, jamais « 100% exact ». **Le dire explicitement dans le verdict** : si le CSV source diffère de la table, c'est la table qu'il faudra corriger, pas la prose — et ça, seul Paul peut le vérifier.

C'est cette branche qui a attrapé les erreurs de la page dollar (« five below 1% » vs 6 réels ; « 6 of 7 / 2 of 11 » contredit par la table qui montrait 8 négatifs concentrés sur GFC+suivantes).

---

## 4. Les 6 passes du review

| Passe | Objet | Renvoi |
|---|---|---|
| **P1** | Recompute (branche A) **ou** cohérence interne (branche B) | §3, prod-research-study §12 |
| **P2** | Comptages & dénominateurs : tout « X of Y », %, médiane, min/max recalculés | §14.2/14.3 prod-research-study |
| **P3** | **Tripwire de DIRECTION** — claims de trajectoire | §5 (cœur de ce skill) |
| **P4** | **Taxonomie des claims non-CSV** (A/B/C) | §6 |
| **P5** | Cohérence **inter-pages** + intégrité artefact téléchargeable | §7 |
| **P6** | Surface **Rule IV / AMF** (titre, snippets, OP) | editeur-eco3min, projet Step 7.5 |

Une seule passe qui échoue sur du BLOQUANT → NO-GO. Pas de seuil « tolérable ».

---

## 5. P3 — Le tripwire de direction (ce qui a failli partir en prod)

**Les audits de valeurs ponctuelles vérifient « 0,13 en avril 2026 ». Ils ne vérifient PAS « a reculé régulièrement jusqu'à 0,13 » — un claim sur le SENTIER entre deux points.** `narrative_audit.py` attrape les **dates** ; il n'attrape pas les **mots de trajectoire**.

**Règle** : tout mot de direction/tendance déclenche une vérif de la sous-série complète entre les deux dates citées :

> *steadily, monotonically, regularly, continued, fell back, rose, climbed, stabilized, plateaued, reversed cleanly, fully reversed, entièrement résorbé, reculé régulièrement, sans interruption…*

**Méthode** :
```python
seg = df[(df.date >= d_start) & (df.date <= d_end)].sort_values("date")
# monotone ? rebonds ? franchissements d'un seuil ?
print("monotone décroissant:", (seg.val.diff().dropna() <= 0).all())
print("min:", seg.val.min(), "| max après le pic:", seg[seg.date > d_peak].val.max())
```

**Catch canonique** : « It then declined steadily … to 0.13 » / « a ensuite reculé régulièrement … 0,13 ». Le CSV montrait 0,57 → **0,10 (juil. 2025) → rebond à 0,43 (nov. 2025, à 0,07 du seuil)** → 0,13. Non monotone, avec retour à 0,07 du re-déclenchement. Ce claim se faisait **débunker à J+1 sur le CSV même offert au téléchargement**. Correctif : décrire le sentier réel — plus honnête *et* plus intéressant, et il pré-empte l'objection.

**Note** : « fully reversed » / « entièrement résorbé » comme **état final** (retour à la baseline) reste vrai même si le chemin a rebondi — ne pas sur-corriger. C'est la **monotonie affirmée** qui est fausse, pas le retour à 0,13.

---

## 6. P4 — Taxonomie des claims non issus du CSV

Tout fait factuel doit tomber dans une catégorie. **La (C) est interdite et bloque la publication.**

| Cat. | Nature | Exigence | Exemples vus |
|---|---|---|---|
| **A** | Issu du CSV | Recalculé en P1 | crossings, peaks, latest, comptages |
| **B** | Sourcé hors-CSV | Source réelle vérifiable | dates NBER, identité série FRED, citations (lien), **autres datasets** |
| **C** | Ni l'un ni l'autre | **INTERDIT** → halt | toute valeur « plausible » non tracée |

Précisions sur la **catégorie B** :
- **Dates NBER, identité de série, formule** : vérifiables, stables — recalcul/contre-vérif rapide.
- **Citations** (ex. Claudia Sahm) : sourcées + liées = pas inventées, mais le **verbatim** doit être confirmable. Si non vérifiable dans l'environnement, le **signaler** (« confirmer le mot-à-mot »), ne pas certifier.
- **Zone dangereuse = claims cross-dataset dans une section « deux signaux » / appât-à-backlink.** Pas dans le CSV de la page, donc non couverts par l'audit extractif, **et** facilement recomputés par un lecteur. Exemple : « 2s10s inversée 26 mois, désinversée en août 2024 » — le mois était faux (consensus : **septembre 2024**, ~793 jours), et « 26 mois » divergeait de la page sœur (« 25 »). Ces claims exigent **vérif externe** (sources) **+** réconciliation inter-pages (§7).

---

## 7. P5 — Cohérence inter-pages & intégrité de l'artefact

**Inter-pages** : tout nombre répété sur des pages **liées entre elles** doit concorder. Un lecteur qui clique verra les deux. Vus ici : 26 mois (page Sahm) vs 25 mois (page sœur yield curve) ; « deepest » vs « second-deepest » entre deux pages dollar. → choisir la valeur défendable (793 j ≈ 26 mois) et **aligner les deux pages**.

**Intégrité du CSV téléchargeable** (la page le présente sous « Data & reproducibility ») :
- **Contiguïté** : pas de mois manquant au milieu de la fenêtre récente (le trou oct. 2025 vu ici).
- **Compteur** : « N observations » = nombre réel de lignes. Si on ajoute une ligne, mettre à jour le compteur.
- **Règle d'or anti-invention** : si une série a un trou, **ne jamais le combler par interpolation**. Un trou honnête + note d'une ligne vaut mieux qu'un point fabriqué — fabriquer violerait précisément le « rien d'inventé ». Soit on tire la vraie valeur de la source, soit on documente l'absence.

---

## 8. Hiérarchie de criticité & format du verdict

| Niveau | Définition | Action |
|---|---|---|
| **🔴 BLOQUANT** | claim contredit par la donnée · nombre inventé · incohérence interne · déclencheur Rule IV/AMF | **NO-GO** tant que non corrigé |
| **🟡 MOYEN** | trou d'artefact · incohérence inter-pages · choix définitionnel défendable mais porteur du titre | corriger **ou** documenter |
| **🟢 FAIBLE** | inférence légère, wording | optionnel |

**Format de sortie** (dans cet ordre) :
1. **Verdict** : GO / NO-GO en une ligne, + branche (A « 100% exact contre source » / B « cohérent en interne seulement »).
2. **Bloquants** d'abord, le plus impactant en tête (préférence Paul : défaut structurel le plus impactant, puis le plus actionnable).
3. **Moyens**.
4. **Vérifié propre — à ne pas casser en itérant** : lister ce qui tient (et nommer la **colonne structurante** : thèse/angle/architecture).
5. Pour chaque faille : une **piste de résolution** ou un **test**.

Si rien de solide ne tient → le dire. **Ne pas fabriquer de pushback.**

---

## 9. Discipline de régénération (quand on corrige la page)

« Régénère avec uniquement les corrections, le reste 100% pareil » ne se garantit **que** par des éditions ciblées, jamais par une ré-émission à la main.

1. Écrire la page **verbatim** sur disque (`create_file` — copie pure, zéro édition mêlée).
2. **`str_replace` chirurgical**, un par correction.
3. **Vérifier** : nouvelle chaîne présente (=1), ancienne partie (=0), ancres d'intégrité intactes (compteurs, shortcodes type `[mailpoet_form]`/`[lwptoc]`, nb de lignes de table, constantes type scale factor), et **décimales FR en virgule** si page FR (0,10 / 0,43 / 0,07).
4. Livrer via `present_files` (fichier, pas bloc dans le chat — surtout sur mobile).

---

## 10. Checklist finale (2 minutes)

- [ ] Branche identifiée : CSV présent (A) ou page seule (B) — et le **verdict le dit**.
- [ ] P1 : tous les nombres recalculés (A) / toutes les vues concordent (B).
- [ ] P2 : chaque « X of Y », %, médiane, min/max recompté.
- [ ] P3 : chaque mot de **direction** vérifié contre la sous-série réelle.
- [ ] P4 : zéro claim catégorie C ; cross-dataset vérifiés externes + réconciliés.
- [ ] P5 : nombres répétés alignés entre pages liées ; CSV téléchargeable contigu + compteur juste ; aucun point interpolé.
- [ ] P6 : titre/snippets/OP sans will/won't/should, sans cadrage prédictif, claims attribués (Rule IV + AMF).
- [ ] Verdict GO/NO-GO rangé par criticité, colonne structurante nommée, zéro pushback fabriqué.
- [ ] Si corrections : régénération par str_replace + vérif (§9).

---

## 11. Anti-patterns du reviewer

1. **Lire au lieu de recalculer** une valeur affichée pour la « valider ».
2. **Fabriquer des critiques** pour paraître rigoureux quand la page tient.
3. **Certifier « 100% exact » sans le CSV** — sans la source, on ne certifie que la cohérence interne.
4. **Combler un trou de série par interpolation** au lieu de tirer la vraie valeur ou de documenter l'absence.
5. **Sur-corriger** : changer plus que les corrections demandées quand on régénère « à l'identique ».
6. **Faire confiance aux valeurs ponctuelles** et rater les **mots de trajectoire** (le piège du §5).
7. **Flagger sans sanity-check** (mauvaise fenêtre de calcul → faux positif, §2).
8. **Sur-corriger un état final correct** : « entièrement résorbé » reste vrai si le retour à la baseline est acquis, même après un rebond.

---

## GATE AJOUTÉ (août 2026) — Statut HTTP et commentaires HTML

Deux contrôles bloquants à passer avant tout GO, en plus des audits de valeurs.

### 1. Commentaires HTML dans le contenu — NO-GO immédiat

```python
import re
found = re.findall(r'<!--.*?-->', html, re.S)
assert not found, f"{len(found)} commentaire(s) HTML — {[c[:80] for c in found[:3]]}"
```

Aucun commentaire HTML ne doit subsister dans le `post_content`. Le cas critique est le
commentaire qui **cite une balise en prose** (`Pas de <script> ici`, `pas de <style> inline`) :
Autoptimize scanne `<script>` / `<style>` en regex sans ignorer les commentaires, avale la prose
comme du JavaScript, et la page part en **HTTP 500 avec le corps complet**.

### 2. Statut HTTP réel de la page publiée — NO-GO immédiat

Le navigateur ne valide rien : Chrome affiche le corps d'une réponse 500 exactement comme un 200,
navigation privée comprise. Seul le code de statut compte, et c'est le seul signal que lit Google.

```bash
for u in <slug-fr> en/<slug-en>; do
  a=$(curl -sS -o /dev/null -w '%{http_code}' "https://eco3min.fr/$u/")
  b=$(curl -sS -o /dev/null -w '%{http_code}' "https://eco3min.fr/$u/?ao_noptimize=1")
  echo "$a $b  $u"
done
```

| Résultat | Lecture |
|---|---|
| `200 200` | OK |
| `500 200` | Autoptimize s'étrangle sur le contenu → chercher une balise littérale dans un commentaire HTML avant toute autre hypothèse |
| `500 500` | fatale côté PHP indépendante d'Autoptimize → snippet de la paire, ou log `debug.log` |

Ce gate est né de l'incident du 27 août 2026 : 8 pages en 500 depuis leur publication, parfaitement
lisibles au navigateur, découvertes seulement par la Search Console.

Règle de production associée : voir `eco3min-import-contenu-bilingue`, section
« RÈGLE FIGÉE (août 2026) — Zéro commentaire HTML dans le contenu publié ».

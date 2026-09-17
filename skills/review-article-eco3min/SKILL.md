---
name: review-article-eco3min
description: "Gate de review AVANT publication (ou après, sur une page déjà en ligne) de toute page Eco3min chiffrée : étude, page dataset, Every X, chart page, paire FR/EN. Ne réécrit pas la page, la certifie ou la bloque : verdict GO / NO-GO rangé 🔴 🟡 🟢, colonne structurante nommée, zéro pushback fabriqué, puis correction chirurgicale. Activer pour « audite cette page », « review avant que je publie », « vérifie que c'est 100% exact », « c'est cohérent ? », « GO ou NO-GO ? », « relis les chiffres », « vérifie avant le push r/economics », « la page dit X mais la table dit Y », « régénère avec uniquement les corrections », « la page est en 500 », « il reste des commentaires HTML ? », après toute régénération de page chiffrée, et pour tout verdict demandé sur un fact_check_audit.md ou un audit_extract.py. Skill courte, non découpée (les six passes servent à chaque invocation) ; pas de scripts/ propres : elle importe production-research-study/scripts/study_locks.py (Claims, close, editorial_locks, assert_no_html_comments) et oriente vers production-research-study references/05 (§12 audit extractif CSV-led, §13 cohérence multi-livrables, §14 patterns à haut risque) sans les dupliquer. Doctrines : recompute, ne lis jamais (chaque nombre est recalculé en Python depuis la source, jamais lu à l'écran pour être validé) ; piège de l'œil (un flag faux coûte autant de crédibilité qu'une erreur ratée : bonne fenêtre de calcul, sanity-check, puis flagger) ; branche A avec CSV = certifiable 100% exact contre la source, branche B sans CSV = cohérent en interne seulement, la table affichée devient la vérité de second rang et le verdict le dit ; six passes P1 à P6 plus P7 GATE ; tripwire de DIRECTION (steadily, monotonically, fell back, reculé régulièrement, sans interruption… déclenchent la vérification de la sous-série complète entre les deux dates ; catch canonique 0,57 → 0,10 → rebond 0,43 → 0,13 ; un état final entièrement résorbé reste vrai malgré un rebond, ne pas sur-corriger) ; taxonomie des claims A issu du CSV / B sourcé hors CSV / C ni l'un ni l'autre = interdit et halt ; zone dangereuse des claims cross-dataset des sections deux signaux (2s10s désinversée en septembre 2024, pas août ; 26 mois contre 25 sur la page sœur) ; cohérence inter-pages avec la page jumelle FR/EN en tête, lue au degré d'adaptation arbitré (1 miroir / 2 adaptation légère / 3 adaptation forte : seuls les faits communs doivent être identiques au chiffre près, les faits propres passent leur propre audit, un repère substitué conforme au degré n'est pas une erreur), et le registre eco3min-knowledge faits/claims.jsonl comme liste des pages sœurs ; intégrité du CSV téléchargeable (contiguïté, compteur N observations, jamais d'interpolation d'un trou) ; surface Rule IV / AMF sur titre, snippets, OP (aucun will / won't / should, aucun cadrage prédictif, claims attribués) ; GATE bloquant d'août 2026 : zéro commentaire HTML dans le post_content (Autoptimize avale une balise citée en prose et sert un HTTP 500 lisible au navigateur, 8 pages le 27 août 2026) et curl du statut réel avec et sans ?ao_noptimize=1 ; discipline de régénération = copie verbatim + str_replace chirurgical + vérification (nouvelle chaîne = 1, ancienne = 0, ancres d'intégrité, décimales FR en virgule). Hors périmètre : la production elle-même (production-research-study, production-dataset, production-every-x-record, production-chart-of-the-week), l'assemblage et l'import (eco3min-import-contenu-bilingue), la légalité de la donnée (sourcing-donnees-eco3min), la revue périodique des datasets périmés (revue-datasets-perimes), la revue de style (editeur-eco3min). Combiner avec production-research-study, editeur-eco3min, eco3min-import-contenu-bilingue, sourcing-donnees-eco3min, hub-card-etude."
---

# Review pré-publication — Eco3min

> Ce skill est le **gate qualité avant publication**, distinct de la production. Il s'applique à une page **déjà construite** (étude, dataset, "Every X", chart page, FR/EN) autant qu'à une page qu'on vient de produire. Il ne réécrit pas l'article : il le **certifie** — ou bloque — et corrige chirurgicalement.
>
> Voir aussi : `production-research-study` (audit extractif CSV-led §12, cohérence multi-livrables §13, patterns à haut risque §14 — les trois dans `references/05-audit-extractif-coherence-patterns.md` depuis le découpage du 15/09/2026 ; ce skill les **oriente**, ne les duplique pas) · `editeur-eco3min` (AMF, termes proscrits : §4 et `references/03-amf-7-regles-disclaimer.md`) · `sourcing-donnees-eco3min` (légalité/provenance de la donnée publiée) · `narrative_audit.py` (module tripwire dates, Step 6.5b du projet killer studies ; sur disque `eco3min-projets/Eco3min Etude approdondie -  GENERIQUE/docs/narative-audit.py`, doctrine en `production-research-study/references/07-verrous-a-g.md` §18.5).

---

## 1. Quand l'activer, et ce qu'il produit

**Activer** dès qu'on demande : « audite cette page », « review avant que je publie », « est-ce 100% exact ? », « vérifie avant le push r/economics », ou après toute régénération de page chiffrée.

**Entrées** :
- la page (bloc HTML/WP, FR ou EN) ;
- **le(s) CSV source(s) si elles existent** — c'est la source de vérité. Si absente, voir §3 branche B.
- si la page est **déjà en ligne** : lire son `post_content` par l'ability WPAI `ewpa/get-page` (ID lu dans la classe `page-id-*` du `<body>` de la page publique ; `ewpa/get-pages` ne sait pas chercher), jamais le texte rendu par le navigateur, qui n'expose ni les commentaires HTML ni le statut HTTP (cf. GATE).

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
→ Lire `production-research-study/references/05-audit-extractif-coherence-patterns.md` avant P1 ; importer `production-research-study/scripts/study_locks.py` (`Claims`, `close`, `TOLERANCE`, docstring en tête du module) plutôt que réécrire un verifier.

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
| **P6** | Surface **Rule IV / AMF** (titre, snippets, OP) | editeur-eco3min §4 (`references/03-amf-7-regles-disclaimer.md`) ; production-research-study Step 7 / §15 pre-flight r/economics (`references/10-social-preflight-upload.md`) et reviewer Rule IV §3.1 (`references/01-hook-prereview-pivot.md`) ; contrôle mécanique `study_locks.editorial_locks` |
| **P7** | **GATE** : zéro commentaire HTML (avant import) + statut HTTP réel (page publiée) | GATE AJOUTÉ (août 2026), en fin de fichier |

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

Le module `narrative_audit` n'est pas versionné avec les skills (copie dans `docs/narative-audit.py` du projet GENERIQUE) : le bloc Python ci-dessus est la méthode opérationnelle du reviewer. En étude, chaque date en prose est en plus un tuple `NARRATIVE_EVENTS` du Step 6.5b (`production-research-study/references/07-verrous-a-g.md` §18.5).

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
- **Contrôle rapide de la catégorie B** (registre des faits publiés, depuis le 16/09/2026) : `grep` du fait dans `~/eco3min/eco3min-knowledge/faits/claims.jsonl`. Présent avec la même valeur → B confirmé, page citée à l'appui ; présent avec une autre valeur → incohérence inter-pages à réconcilier en P5 ; absent → vérif externe obligatoire, rien n'est certifié par défaut.

---

## 7. P5 — Cohérence inter-pages & intégrité de l'artefact

**Inter-pages** : tout nombre répété sur des pages **liées entre elles** doit concorder. Un lecteur qui clique verra les deux. Vus ici : 26 mois (page Sahm) vs 25 mois (page sœur yield curve) ; « deepest » vs « second-deepest » entre deux pages dollar. → choisir la valeur défendable (793 j ≈ 26 mois) et **aligner les deux pages**.

**Page jumelle** : la version de l'autre langue (paire FR/EN) est la première page sœur à réconcilier, **au degré d'adaptation arbitré** à la production (`eco3min-import-contenu-bilingue`, « Décision bilingue » : 1 miroir, 2 adaptation légère, 3 adaptation forte ; le degré est écrit dans le recap de livraison, sinon le demander avant de flagger). Ce qui se réconcilie dépend du degré : degré 1, tous les faits ; degré 2, les données centrales — les points de référence substitués (Fed/Treasury/S&P 500 contre BCE/OAT/CAC 40) sont des claims B distincts, chacun vérifié de son côté ; degré 3, seule la thèse est commune, les données propres à chaque langue passent leur propre audit A ou B en section distincte. Dans les trois cas, invariant repris de la règle figée : un **fait commun** aux deux versions est identique au chiffre près, décimales FR en virgule, et un écart chiffré est un défaut **bloquant** (🔴), jamais un arrondi ; un chiffre « équivalent » fabriqué pour singer l'autre langue est un claim C. Une différence de repère ou de donnée conforme au degré n'est pas une erreur : ne pas la flagger.

**Registre des faits publiés** : `grep` du fait dans `~/eco3min/eco3min-knowledge/faits/claims.jsonl` liste les autres pages qui l'affirment, au-delà des pages reliées par un lien. Une correction qui change un chiffre enregistré **ajoute** une ligne et pose `superseded` sur l'ancienne (append-only, cf. `eco3min-knowledge/CLAUDE.md`), jamais d'effacement.

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

Équivalents Claude Code : `create_file` = Write, `str_replace` = Edit, `present_files` = SendUserFile. Les vérifications du point 3 s'écrivent comme des assertions dans un fichier `.py` exécuté depuis le disque, jamais dans un heredoc shell (les backslashes des regex y disparaissent en silence).

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
- [ ] GATE (P7) : zéro commentaire HTML dans le `post_content` (`assert_no_html_comments`) ; page publiée : `200 200` au curl avec et sans `?ao_noptimize=1`.
- [ ] Page jumelle FR/EN : degré d'adaptation identifié (1 miroir / 2 légère / 3 forte) ; faits communs identiques au chiffre près, décimales FR en virgule ; faits propres du degré 2-3 audités séparément, aucun chiffre « équivalent » fabriqué.
- [ ] Catégorie B et pages sœurs : `faits/claims.jsonl` interrogé ; chiffre corrigé → nouvelle ligne + `superseded`.

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

La même vérification est portée par `production-research-study/scripts/study_locks.py` (`assert_no_html_comments`, `find_html_comments`) ; `editorial_locks` du même module donne le contrôle mécanique de P6 (cadratins U+2014, tics IA, verbes prescriptifs `should` / `must`, verbes d'action) sur le titre, les snippets et l'OP.

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

## Versions

- **v1** (août 2026) — six passes, hiérarchie de criticité, discipline de régénération ; GATE commentaires HTML + statut HTTP ajouté après l'incident du 27 août 2026.
- **v1.1** (17/09/2026) — description réécrite ; pointeurs réalignés sur les skills découpées (§12-14 → `references/05`, « Step 7.5 » inexistant → Step 7 / §15, chemin du module narrative_audit) ; P7 GATE dans la table des passes et la checklist ; catégorie B et pages sœurs adossées au registre `faits/claims.jsonl` ; page jumelle FR/EN en P5, lue au degré d'adaptation arbitré (miroir / légère / forte, règle figée d'import-bilingue) ; lecture d'une page publiée par `ewpa/get-page` ; équivalents Claude Code des outils ; `study_locks` comme contrôle mécanique du GATE et de P6. Aucune règle de fond retirée. Skill volontairement non découpée (213 lignes à l'origine, les six passes servent à chaque invocation).

# production-research-study — référence : Pre-flight r/economics, package social, guide d'upload des images (§15, §22)

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

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

Le pre-flight r/economics obligatoire est en §15. À J+48h après la soumission,
le post se logge dans `~/eco3min/eco3min-knowledge/distribution/reconomics_posts.csv`
via `knowledge.add_reco_post` (voir `production-killer-hn` §6) ; les champs
éditoriaux (`structure_narrative`, `context_box_present`, `scope_caveat_present`,
`loaded_terms_check`, `posture_consensus`) se remplissent depuis le pre-flight,
pas de mémoire.

### 22.2 Guide d'upload des images

Par fichier : **Title** WP (≤60) · **Alt** (identique à l'alt du HTML) ·
**Caption** (le sous-titre du chart) · **Description** (2 à 3 phrases : quoi, le
résultat, l'attribution).

Plus : uploader SVG **et** PNG, plus le PDF en archive · la règle de l'original
non suffixé (§20.3) · les chemins `uploads/[YYYY]/[MM]` exacts · la justification
d'échelle de chaque chart.

---

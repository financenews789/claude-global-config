# production-research-study — référence : Beats 1→2→3, anti-editorializing, Citation Readiness Test, loaded-terms scan (§4, §5, §6, §11)

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

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

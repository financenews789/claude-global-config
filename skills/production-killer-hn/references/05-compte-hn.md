# production-killer-hn — référence : Le compte HN — filtre anti-self-comment, ratio domaine, diagnostic, déblocage (§5)

Extrait VERBATIM de SKILL.md (découpage du 17/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 5. Le compte HN — la variable sous-estimée

> **C'est ce qui a tué le lancement term-premium, pas le contenu.** Cette section vaut plus que n'importe quel tweak de titre.

### 5.1 Le filtre anti-self-comment

**Symptôme observé** : tous les commentaires postés par l'auteur **sur ses propres soumissions** sont auto-[dead] (invisibles aux autres), MÊME quand la soumission pointe vers un tiers (Reuters, Bloomberg). Les commentaires ailleurs passent normalement.

**Cause** : HN a un filtre automatique (software, pas modérateur humain) qui tue les commentaires d'un auteur sur sa propre soumission. C'est la signature classique du spammeur. Un compte avec un historique de soumissions de son propre domaine l'active.

**Conséquence** : ta défense anti-nitpick préparée (premier commentaire) **n'est pas visible**. Tu réponds au cas par cas dans le fil (tes réponses aux AUTRES passent).

**Ne JAMAIS** re-poster le commentaire en boucle (renforce le flag).

### 5.2 Le ratio domaine

Un compte qui poste régulièrement son propre domaine entre en **zone de défiance algorithmique** : malus de classement silencieux, voire shadow-kill. Vérifier le ratio sur la page `/submitted?id=USERNAME`.

**Cible de réhabilitation : ~3 posts externes de qualité pour 1 post de son domaine, max un lien direct toutes les 6-8 semaines.**

### 5.3 Diagnostic shadow-kill vs filtre ciblé

| Test | Résultat | Diagnostic |
|---|---|---|
| Post visible en navigation privée (déconnecté) ? | Oui | Pas de shadow-kill sur la soumission |
| Commentaire sur le post d'un AUTRE, vu en privé ? | Visible | Compte OK, seul le self-comment est filtré (cas le moins grave) |
| | Invisible | Shadowban global du compte (grave) |

### 5.4 La seule voie propre de déblocage

**Email à hn@ycombinator.com** — court, honnête, sans agressivité. Les mods (dang) répondent bien aux gens de bonne foi qui produisent du vrai contenu. Ils peuvent lever le filtre manuellement et "vouch" les commentaires morts.

Template :
> Hi — my comments on my own submissions are consistently getting auto-killed, even on submissions linking to third-party sources. I post first comments to add author context / methodology, not to spam. Could you check whether my account has a filter catching this? Happy to adjust my behaviour. Username: [USERNAME].

**Important** : l'email répare le FUTUR, pas le post du jour (traitement = heures). Ne pas s'acharner sur le post en cours pendant ce temps.

### 5.5 Ce qu'on NE fait JAMAIS

- Demander à des amis/réseau d'aller upvoter (pic de votes coordonné = pénalité, surtout sur compte à risque).
- Se re-share sur X/Reddit dans l'heure en pointant vers le post HN (vote brigading détectable).
- Re-soumettre dans la foulée (pénalité re-post).

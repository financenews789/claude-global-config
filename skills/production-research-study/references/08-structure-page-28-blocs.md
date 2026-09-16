# production-research-study — référence : Structure de la page HTML, 28 blocs dans l'ordre (§19)

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

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

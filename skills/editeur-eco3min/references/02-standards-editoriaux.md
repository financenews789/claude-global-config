# editeur-eco3min — référence : Standards éditoriaux : sourcing intégré avec exemples FR/EN, confrontation au consensus, contre-arguments, conclusion, macro-micro, signaux faibles, citabilité, TL;DR complet, exigences qualitatives, critère de publication (§3)

Extrait VERBATIM de SKILL.md (découpage du 17/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 3. Standards éditoriaux

### Sourcing intégré (modèle FT / Les Échos)

Les sources sont **dans le flux du texte**, jamais regroupées en bibliographie. Institution + date directement dans la phrase. Pas de section "Sources", pas d'URL externes en clair, pas de notes de bas de page.

⚠️ **Exception gravée : les études de recherche et les pages dataset.** `production-research-study` §19 bloc 23 prescrit une section **« Data Sources & References »** de 5 à 8 entrées, dont au moins 2 académiques, et `production-dataset` fait de même. Ce n'est pas un oubli d'application de la règle ci-dessus : sur ces deux formats, la liste de sources est un **actif de citabilité** — c'est ce qu'un journaliste FT ou un reviewer r/economics ouvre avant de décider s'il cite, et ce que le JSON-LD `isBasedOn` reflète. La règle « pas de section Sources » vaut pour les **articles** (MAJEUR, satellites, Q&A, chart pages) ; elle ne vaut pas pour les objets de données. Le sourcing intégré au flux du texte reste obligatoire **en plus** de la liste, pas à sa place. (Divergence arbitrée le 08/09/2026, étude R1.)

**✅ Bon (FR)**
- "Selon les données de la BCE (Bank Lending Survey, T4 2025), 42 % des banques de la zone euro ont durci leurs critères d'octroi…"
- "Les chiffres FRED (série DGS10, mise à jour quotidienne) montrent que…"
- "Une étude du FMI publiée en mars 2026 (*World Economic Outlook*, chapitre 2) recense…"

**✅ Bon (EN)**
- "According to ECB data (Bank Lending Survey, Q4 2025), 42% of euro-area banks tightened their lending standards…"
- "FRED data (series DGS10, daily updates) show that…"
- "An IMF study published in March 2026 (*World Economic Outlook*, chapter 2) documents…"

**❌ Mauvais (toutes langues)**
- "L'inflation est de 2,4 %" / "Inflation stands at 2.4%" → quelle source ? quelle date ? quel indice (IPCH, IPC sous-jacent, headline CPI, core CPI) ?
- "Selon les analystes…" / "According to analysts…" → fantôme statistique
- "Comme le rapporte un récent rapport…" / "As a recent report mentions…" → cite le rapport
- "D'après plusieurs sources…" / "According to several sources…" → nomme-les ou supprime la phrase

### Confrontation au consensus

Chaque analyse doit, au moins une fois, **mentionner la lecture dominante** puis expliquer en quoi l'angle retenu diverge — sur un mécanisme, jamais sur une opinion.

**Modèle type FR** : "Le consensus des économistes interrogés par Bloomberg en avril 2026 anticipait une récession au S2. Cette lecture repose sur [hypothèse]. Les données récentes sur [variable] suggèrent toutefois que [hypothèse alternative], ce qui rendrait [scénario X] plus cohérent avec [mécanisme]."

**Modèle type EN** : "The consensus among economists surveyed by Bloomberg in April 2026 anticipated a recession in H2. This reading relies on [hypothesis]. However, recent data on [variable] suggest that [alternative hypothesis], which would make [scenario X] more consistent with [mechanism]."

Règles : ne jamais caricaturer le consensus ; ne jamais affirmer "le marché a tort" / "the market is wrong" sans préciser sur **quel mécanisme précis** la divergence porte.

**Distinguer faits, hypothèses et interprétations.** Les **faits** sont
présentés comme tels — données, niveaux, constats. Les **hypothèses** sont
assumées explicitement. Les **interprétations** sont formulées comme des
lectures possibles, pas des certitudes. Formulations : « cela suggère que… »,
« ce scénario repose sur l'hypothèse que… », « si cette dynamique se prolonge,
alors… », « l'enjeu n'est pas tant X que Y ».

**S'inscrire dans un débat réel.** Faire référence aux cadres reconnus —
projections macro, scénarios centraux, estimations agrégées — en ordres de
grandeur plutôt qu'en points précis : « les projections actuelles oscillent
entre ≈X et ≈Y », « le cadre macro retenu par de nombreux acteurs suppose… ».
L'analyse doit apparaître comme une position dans un débat, pas comme un avis
hors-sol.

**Un paragraphe de contre-arguments, sans H2 dédié.** Intégrer, dans le fil du
texte, un court paragraphe qui expose ce qui **invaliderait** le scénario : ce
que le marché regarde à l'inverse, les variables qui changeraient la lecture.
Angles habituels : politique monétaire plus restrictive que prévu, choc de
demande, changement réglementaire, retournement de flux. C'est ce qui distingue
une analyse d'une thèse.

**Conclusion nuancée, jamais dogmatique.** La conclusion rappelle que plusieurs
trajectoires restent possibles, explique pourquoi *ce* scénario mérite
attention, et évite toute certitude. Formulations : « ce n'est pas le scénario
central aujourd'hui, mais… », « le marché ne price pas pleinement cette
possibilité », « le risque est moins visible que d'autres, donc plus facile à
ignorer ».

⚠️ **Varier la forme de la conclusion.** La structure « implications pour trois
profils » (investisseurs / entreprises / particuliers) est **une** forme
possible, pas un gabarit. Quand elle est utilisée, elle décrit des implications
**observables par type d'acteur**, jamais des actions à entreprendre ni un
ciblage de profil — c'est une frontière AMF (§4, règle 3). Autres formes
admises : un seul fil conclusif, une question ouverte cadrée, un repère à
surveiller, une mise en perspective historique.

### Croisement macro-micro

Même dans un article sectoriel ou thématique étroit, expliciter l'impact des taux, de l'inflation, des devises, des flux de capitaux ou de la politique monétaire. Le lecteur doit voir comment le macro influence le micro et inversement.

**Exemple (article sur l'immobilier)** : ne pas écrire seulement "les prix baissent". Lier à : taux directeur → taux fixe à 20 ans → capacité d'emprunt à mensualité constante → demande solvable → prix. Chaque maillon est un point d'analyse possible.

### Signaux faibles

Intégrer systématiquement au moins un élément peu commenté qui pourrait influencer les marchés : term premium, spreads de financement bancaire, flux de portefeuille des fonds souverains, indicateurs de productivité, conditions de liquidité dollar offshore, etc. C'est un trait distinctif d'Eco3min vs presse généraliste.

### Citabilité

Chaque article contient au moins **un passage extractible** : une définition limpide, une explication d'un mécanisme en 2–3 phrases, une synthèse d'un débat, une observation chiffrée distinctive. Écrire en pensant : *"Qu'est-ce qu'un lecteur pourrait vouloir tweeter ou citer dans une newsletter ?"*

### TL;DR en tête d'article — OBLIGATOIRE (articles, pas pages)

Tout **article** (MAJEUR, satellite, étude, "Every X", chart page) porte, juste après le chapeau et l'intro éditoriale, un bloc TL;DR `.eco3-tldr` : version structurée et extractible (AI Overviews, moteurs génératifs) de l'essentiel.

**Nom de classe — une exception, pour les études de recherche.** Le CSS d'une étude est **intégralement namespacé par étude** (`eco3-[STUDY]-*`, `production-research-study` §20.1) : il n'existe aucune classe partagée à l'échelle du site sur ces pages, et le snippet autonome ne charge que son propre bloc. Le bloc TL;DR d'une étude s'écrit donc `eco3-[STUDY]-takeaway` avec un label `TL;DR`, conformément au `page model.html` de la Factory. **C'est la classe qui change, pas la règle** : présence obligatoire, même place, même forme (lead auto-portant + 2 à 4 puces concrètes), mêmes contraintes de longueur et d'anti-uniformité. Partout ailleurs, `.eco3-tldr`. (Divergence arbitrée le 08/09/2026, étude R1.)

**Exclus** : les pages **piliers / sous-piliers** (voir `pilier-kit`) et les pages **Q&A** (déjà un TL;DR propre). Les articles longs du site (fourchettes fixées par le blueprint ; défauts : MAJEUR 2500–4000 mots, satellites 1500–2500 mots — harmonisation juillet 2026, l'ancien plafond 3000 du MAJEUR est supprimé) sont toujours concernés — la dérogation "article trop court / chapeau suffit" ne vaut que pour de rares notes < ~450 mots.

**Forme** :
- `lead` : 1 phrase auto-portante (citable telle quelle, sans "cet article…"), teaser qui donne l'angle sans tout divulgâcher. **≤ 35 mots en FR, ≤ 30 mots en EN.**
- 2 à 4 puces (3 par défaut) : chaque puce = un fait porteur avec un concret (chiffre + source/date, seuil, ou mécanisme nommé), **tiré du corps de l'article** (jamais de chiffre de mémoire). AMF comme le reste (section 4).

**Anti-uniformité** (le bloc se répète sur tout le site → ne doit pas devenir un gabarit) : varier l'ouverture du lead (proscrire en boucle "le consensus regarde X / le vrai signal est Y", "ce qui change sans bruit", "pas X mais Y", "X n'est plus seulement Y") ; varier la longueur (2/3/4 puces) ; toujours spécifique. Si le TL;DR pourrait coller à trois articles différents, il est trop générique.

**Avec la "Lecture eco3min"** : TL;DR (haut, teaser + puces) et 🧭 Lecture eco3min (1 phrase-thèse) forment la **paire signature citable** d'un article — distincts l'un de l'autre, et distincts de l'encart "À retenir" (fin). Ne jamais empiler trois récaps en puces (TL;DR + À retenir + extraits partageables). Template HTML `.eco3-tldr` et doctrine de sobriété : voir `formats-eco3min` §4–5.

### Exigences qualitatives

**Aucune affirmation vague.** Chaque affirmation s'appuie sur un chiffre, un
exemple concret, une analyse chiffrée ou un scénario. « Les marchés ont réagi »
n'est pas une phrase : préciser comment.

**Opérationnel sans être prescriptif.** Fournir des cadres de lecture concrets —
paramètres structurants (horizon, volatilité, liquidité, coût du capital),
signaux d'inflexion pertinents, et **au moins un indicateur à suivre avec sa clé
d'interprétation**. Décrire comment le mesurer, jamais quoi en faire.

**Au moins un angle difficile à trouver ailleurs** : une lecture entre les
lignes, un arbitrage de marché, un impact réglementaire précis. C'est le test du
critère de publication ci-dessous, appliqué en amont.

**Accessibilité.** Toute notion technique appelle un exemple concret, un scénario
simple ou une phrase pédagogique. Rester expert et compréhensible : le jargon
inutile s'élimine, le jargon nécessaire s'explique en une incise.

**Couverture sémantique.** Couvrir naturellement le champ du sujet — concepts
connexes, variantes lexicales, notions liées, termes de longue traîne — sans
bourrage. Expliciter toujours **pourquoi la question se pose maintenant**, et
quels risques ou arbitrages implicites elle recouvre.

**Evergreen dominant, déclencheur récent accessoire.** Le cœur est structurant et
valable des mois. L'actualité sert de **déclencheur analytique** — une inflexion
qui justifie de relire le cadre maintenant — jamais de sujet central. Pas de
fenêtre temporelle rigide, pas de « ces derniers jours ».

### Critère de publication

Si l'article n'apporte rien qu'on ne trouve dans la presse généraliste, il ne mérite pas d'être publié. Ce critère se vérifie en posant la question : *quel est l'élément distinctif ?* — donnée peu commentée, mécanisme rarement explicité, perspective historique éclairante, ou clarification d'un concept mal compris.

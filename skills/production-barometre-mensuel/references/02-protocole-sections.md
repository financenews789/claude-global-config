# production-barometre-mensuel — référence : Protocole section par section (SECTION 1 à 17 + sections inchangées)

Extrait VERBATIM de SKILL.md (découpage du 16/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 2. Protocole section par section

Appliquer dans cet ordre. Ne passer à la section suivante qu'une fois les données de la section
courante vérifiées et écrites.

### SECTION 1 — Header

**Ce qui change :**
- Le titre du mois vit dans le **titre WordPress** de la page (« Macroeconomic Barometer — [Mois N+1] [Année] » / « Baromètre macroéconomique — [Mois N+1] [Année] »), mis à jour via `ewpa/update-post` `title` — JAMAIS dans le bloc HTML. Le HTML ne porte **ni `<h1>` ni `baro-header__title`** : Blocksy rend déjà le titre WordPress en `<h1 class="page-title">` (septembre 2026 : deux H1 sur la page ; le titre du header a été retiré). Contrôle avant livraison : `assert '<h1' not in html`.
- `baro-header__date span` : "1er [mois N+1], [année]" (ou date d'arrêté réelle)

**Ce qui ne change pas :** countdown div, KPI strip (la brand line n'existe plus depuis septembre 2026).

**Vérification AMF :** aucune.

---

### SECTION 2 — Commentaire shortcode [eco3min_regime]

**Ce qui change :**
- Ligne "Ce mois-ci ([mois]) : flag ACTIF/INACTIF" : mettre à jour selon Brent YoY du mois
- Ligne "Repo : github.com/eco3min/macro-regime-classifier" : vérifier qu'elle est présente et exacte (repo créé : https://github.com/eco3min/macro-regime-classifier)

**Règle flag `headline_underlying_divergence` :**
- Calculer Brent YoY au 1er du mois N+1 : `(Brent actuel / Brent il y a 12 mois − 1) × 100`
- Si YoY > +20% → flag ACTIF dans le commentaire
- Si YoY ≤ +20% → flag INACTIF

Le shortcode lui-même gère l'affichage automatiquement via le JSON — le commentaire sert
uniquement de documentation pour le prochain rédacteur.

---

### SECTION 3 — Synthèse (bloc navy)

**Rôle éditorial :** résumé de ~3 paragraphes sur les faits marquants du mois écoulé.
Structure du mois de référence (à maintenir) :
1. Fait dominant du mois (inflation, croissance, banques centrales) avec chiffres clés
2. Contre-signal ou nuance (pourquoi ce n'est pas la catastrophe ou l'euphorie)
3. Phrase de sourcing / cadrage légal

**Protocole :**
1. Collecter d'abord TOUTES les données (sections 4 à 13) avant d'écrire ce bloc
2. Identifier le fait dominant : quelle donnée a le plus bougé par rapport au mois précédent ?
3. Identifier le contre-signal : quelle donnée va dans le sens inverse ?
4. Rédiger en Libre Baskerville style (sobre, factuel, pas de jugement directionnel)

**⚠ AMF — interdits stricts dans ce bloc :**
- "l'économie va [mieux/pire]" sans ancrage empirique chiffré
- "les marchés anticipent" sans source explicite (FOMC minutes, breakevens, etc.)
- "il faut surveiller" avec implication d'action pour l'investisseur
- Toute formulation qui implique une recommandation d'allocation

**Template de structure (à adapter selon les faits du mois) :**
```
[Fait dominant avec chiffres clés vérifiés et sourcing inline]
[Contre-signal avec chiffres vérifiés — "Cependant, [indicateur] reste [description factuelle]"]
[Phrase de cadrage : "Toutes les données ci-dessous sont issues de sources institutionnelles
publiques. Aucune prévision ni recommandation d'investissement n'est formulée."]
```

**Note sur les citations :** les formulations *italiques* dans la synthèse (ex. *soft stagflation
pattern*) doivent soit être des citations directes d'une source identifiée, soit des descriptions
purement factuelles. Jamais une opinion non sourcée présentée comme un fait.

---

### SECTION 4 — Signaux de cycle (NFCI, Sahm, SOS)

Pour chaque indicateur, mettre à jour :
- La valeur numérique (`.baro-index-score__value`)
- Le texte de description (`.baro-index-reading`) : dates précises, valeurs des sous-composantes si disponibles
- La largeur de la barre (`.baro-index-bar__fill`) : calculée comme `(valeur / seuil) × 100%` pour Sahm et SOS ; pour NFCI, `(valeur + 3) / 9 × 100%` sur une échelle −3 à +6 (ajuster si la plage change)

**NFCI :** préciser la semaine exacte, le mouvement (s'est resserré / s'est assoupli), et si
disponibles les sous-indices risk/credit/leverage qui expliquent le mouvement.

**Sahm :** préciser le mois de référence, la comparaison avec le mois précédent, et rappeler
le seuil de 0.50. Sourcer `SAHMREALTIME` (pas `SAHMCURRENT`).

**SOS :** préciser la semaine exacte, "last updated [date]". Ne pas écrire "bien en dessous" sans
la valeur — toujours la valeur + le seuil.

**Note de bas de section :** conserver la note AMF actuelle (les indicateurs sont pour la
détection, pas des signaux de trading). Ne pas la modifier.

---

### SECTION 5 — Description graphique Yield curve / Sahm

Mettre à jour uniquement les valeurs explicitement mentionnées dans le texte descriptif
(`.baro-chart-desc`). Conserver le titre, les codes FRED, les liens internes.

**⚠ Règle :** si le texte descriptif dit "pour la semaine du [date], X = Y", mettre la valeur
réelle du mois. Si le texte est générique (il décrit le mécanisme, pas une valeur ponctuelle),
ne rien changer.

---

### SECTION 6 — Description graphique NFCI

Mettre à jour les valeurs ponctuelles dans `.baro-chart-desc` si elles y figurent.
Codes FRED (NFCI, NFCIRISK, NFCICREDIT, NFCILEVERAGE) : inchangés.

---

### SECTION 7 — Faits marquants (baro-signal)

**Label :** "Factual highlights — [Mois écoulé] [Année]" (le mois dont on a les données)

**Structure à maintenir :** 4–5 blocs thématiques, chacun avec `<strong>` pour le titre du fait.
Thèmes récurrents : FOMC, BCE, Inflation, Croissance, Énergie/Géopolitique.

**Pour chaque fait :**
1. Chercher le communiqué officiel de l'événement
2. Citer uniquement des chiffres présents dans ce communiqué
3. Source en fin de paragraphe : "Source: [Institution], [type de document], [date]."

**⚠ AMF — contrôle par paragraphe :**

FOMC : ✓ "Le Fed a maintenu les taux à [X]–[Y]% par un vote [A]-[B]"
       ✓ "[Nom] a voté en faveur d'une [hausse/baisse] de [X] bp"
       ✓ "Le communiqué décrit désormais l'inflation comme [citation exacte entre guillemets]"
       ✗ "Le Fed devrait baisser en [mois]" — prévision
       ✗ "Le Fed a envoyé un signal" — interprétation

BCE :  Mêmes règles. Citer exactement le communiqué de presse officiel.

Inflation : ✓ "Le CPI de [mois] ressort à [X]% en glissement annuel (publié le [date])"
            ✓ "Le composante essence a progressé de [X]% sur le mois"
            ✗ "L'inflation reste préoccupante" — jugement
            ✗ "Les prix pourraient continuer à monter" — prévision

Croissance : ✓ "Le PIB du T[X] [année] s'établit à +[X]% SAAR selon l'estimation [advance/second]
               du BEA publiée le [date]"
             ✓ Préciser le type d'estimation et si elle sera révisée
             ✗ "La croissance est solide" — jugement non ancré

Énergie : ✓ Prix de clôture avec source et date
          ✓ Événement factuel (décision OPEC, incident, accord)
          ✗ "Les prix restent sous pression" — jugement
          ✗ "Le marché craint" — attribution de sentiment au marché

---

### SECTION 8 — Description graphique Emploi (ICSA)

Mettre à jour la valeur ICSA la plus récente disponible :
- Valeur en milliers
- Date de la semaine

---

### SECTION 9 — Tableau indices boursiers

**Pour chaque ligne :** niveau de clôture (2 décimales), date de clôture, flèche mensuelle.

**Calcul de la flèche :** comparer le cours de clôture du dernier jour du mois N au cours de
clôture du dernier jour du mois N-1. ↑ = hausse, ↓ = baisse, → = variation < 0.5%.

**Date :** utiliser la date de clôture réelle (le dernier jour de bourse du mois, pas le 30 ou 31
automatiquement — vérifier si fin de mois tombe un weekend **ou un jour férié de place** : le 31/08/2026 était le
Summer bank holiday britannique, Londres fermé, FTSE 100 et fixing LBMA datés du 28 alors que Paris, Francfort et
New York cotaient ; deux lignes du tableau datées différemment, expliquées en note de bas de tableau. Calendriers de
place : `sourcing-donnees-eco3min`, annexe B).

**Note de bas de tableau :** conserver la note sur le caractère indicatif et l'absence de valeur
prédictive des flèches. Ne pas la modifier.

---

### SECTION 10 — Tableau taux / matières premières / volatilité

Pour chaque ligne : valeur, date.

**Check de cohérence T10Y2Y :** la valeur dans ce tableau doit correspondre au signe mentionné
dans la description du graphique yield curve. Si T10Y2Y = +0.51% ici, le texte du graphique
ne peut pas dire "la courbe est inversée".

**Note de bas de tableau :** ajuster si le contexte énergétique a changé (ex. si le Brent a
repassé sous son niveau pré-conflit, la note sur "+60% au-dessus des niveaux pré-conflit" serait
fausse et doit être mise à jour ou supprimée).

---

### SECTION 11 — Description graphique Taux

Mettre à jour les valeurs ponctuelles dans `.baro-chart-desc` si elles y figurent.
Codes FRED : inchangés.

---

### SECTION 12 — Description graphique Credit Spread (HY OAS)

Mettre à jour la valeur et la date. Conserver la note sur le niveau historiquement serré si elle
est toujours exacte — vérifier le contexte percentile (la valeur est-elle toujours basse ?) en
comparant à la moyenne historique HY OAS ~5.5% ; si la valeur est autour de 3%, "historiquement
serré" reste correct.

---

### SECTION 13 — Cartes macro (US + Zone euro)

**Carte États-Unis — mettre à jour :**
- PIB : dernier chiffre publié (avec type d'estimation : advance/second/third)
- CPI : headline YoY du mois le plus récent
- Core CPI
- Fed funds (fourchette cible)
- NFP du mois le plus récent
- NFP du mois précédent avec révision si elle a eu lieu
- Taux de chômage
- NFCI dernière valeur avec date
- Sahm Rule

**Carte Zone euro — mettre à jour :**
- PIB : dernière estimation publiée (q/q)
- HICP : headline YoY
- Core HICP
- Énergie YoY si notable
- Trois taux BCE
- Prochaine décision BCE (date exacte)
- Données nationales si mentionnées (inflation France, etc.)

**⚠ Règle de sourcing :** chaque valeur doit avoir une source identifiable. Les cartes macro
sont le cœur du contenu factuel — aucune approximation tolérée. Si une donnée n'a pas encore
été publiée, laisser la valeur du mois précédent avec "(révision attendue le [date])".

---

### SECTION 14 — Description graphique Inflation et anticipations

**Valeurs à mettre à jour :**
- T10YIE (breakeven 10Y) : valeur + date
- T5YIFR (5Y5Y forward) : valeur + date
- DFII10 (taux réel 10Y) : valeur + date

**Note sur le T5YIFR :** le baromètre le décrit comme "the Fed's preferred gauge of long-run
expectations anchoring". Vérifier que cette formulation reste exacte (c'est une description
largement acceptée dans la littérature Fed — stable).

---

### SECTION 15 — Framework (bloc ambré baro-regime)

**Rôle :** analyse factuelle du mois, 4–5 paragraphes thématiques.
Thèmes récurrents : activité, emploi, inflation, banques centrales.

**Protocole :**
1. Ne rédiger ce bloc qu'après avoir collecté toutes les données
2. Chaque paragraphe est ancré sur au moins un chiffre vérifié
3. Les "nuances" (ex. "le rebond du PIB doit être lu avec prudence") sont autorisées si elles
   s'appuient sur des données (ex. "une part significative vient de [composante X]")
4. Structure suggérée : un paragraphe d'introduction de la "configuration du mois" + un
   paragraphe par thème

**⚠ AMF — contrôle de chaque paragraphe :**
- Aucune phrase commençant par "les marchés devraient" / "il faut surveiller X car Y pourrait"
- Aucune association régime → allocation (ex. "en période de stagflation, les matières premières
  surperforment" → INTERDIT même présentée comme "observation historique" sans ancrage empirique)
- Les formulations `<strong>` en bleu navy doivent souligner des faits, pas des jugements
  ("both the Fed and the ECB held rates in April" = fact ✓ ;
   "central banks are losing the battle against inflation" = opinion ✗)

---

### SECTION 16 — Key items to watch

**Label :** "Key items — [Mois N+1]–[Mois N+2] [Année] calendar"

**Structure : 5–6 items numérotés**

Chaque item = un événement futur avec date précise ou une question ouverte avec date d'éclairage.

**Sources pour le calendrier :**
```
FOMC : web_fetch https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
BCE : web_fetch https://www.ecb.europa.eu/press/calendars/mgcgc/html/index.en.html
BLS : web_fetch https://www.bls.gov/schedule/news_release/cpi.htm
BEA : web_fetch https://www.bea.gov/news/schedule
Eurostat : web_search "Eurostat release calendar [mois] [année]"
```

**Types d'items récurrents :**
- NFP du mois suivant : date précise, question analytique spécifique au contexte
- CPI du mois suivant : date précise, ce qu'on surveille (base effect, composante énergie, etc.)
- Prochaine réunion FOMC : date, contexte (SEP ou pas, dissents attendus ou pas)
- Prochaine réunion BCE : date, contexte
- Événements géopolitiques ou structurels en cours : formuler comme "situation à surveiller" avec
  les indicateurs mesurables qui l'encadrent, jamais comme prévision

**⚠ AMF :**
- "Markets will closely monitor X" = OK (description d'un comportement marché, pas une consigne)
- "You should watch X" = INTERDIT (adresse le lecteur comme investisseur)
- "X could push inflation higher" = limite ; cadrer comme "selon [institution], X pourrait..."
  si la formulation citée vient d'une source institutionnelle. Sinon : supprimer.

---

### SECTION 17 — Description graphique Liquidité nette

**Mettre à jour :**
- WALCL : dernière valeur hebdomadaire (en milliards $)
- TGA (WTREGEN) : dernière valeur
- RRP (RRPONTSYD) : dernière valeur
- Net liquidity calculée = WALCL − TGA − RRP
- Variation mensuelle approximative (différence fin de mois N vs fin de mois N-1)
- Date de référence ("As of [date]")

**Note sur le RRP :** si le RRP est proche de zéro (comme en mai 2026), le dire explicitement.
Si le RRP remonte significativement, mettre à jour la note analytique en conséquence.

---

### SECTIONS INCHANGÉES (vérification uniquement)

Ces sections ne changent normalement pas de mois en mois. Les lire pour s'assurer qu'elles
restent exactes dans le nouveau contexte.

**Baro-internal-links :** vérifier que les URLs cibles existent encore (web_fetch rapide sur
les liens internes eco3min.fr). Si une page a changé de slug, mettre à jour.

**Baro-promesse :** ne pas modifier. Si la liste des sources institutionnelles citées change
(ex. nouvelle source ajoutée), mettre à jour la liste.

**Baro-disclaimer :** NE PAS MODIFIER. Texte juridique figé.

**CSS + fonts import :** NE PAS MODIFIER.

**Descriptions de graphiques génériques (mécanisme)** : ne modifier que les valeurs ponctuelles
datées, jamais la description du mécanisme (ex. la description du mécanisme NFCI "Composite of
105 variables" est stable — vérifier seulement les chiffres ponctuels).

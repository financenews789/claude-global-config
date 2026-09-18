# production-killer-hn — référence : Choix du sujet du post mensuel r/economics (§10)

Ajouté le 18/09/2026, après la sélection du post du 22/09/2026 (rafraîchissement de
l'étude #6, « 2-year Treasury leads the Fed », six jours après la première hausse Fed
depuis 2023). Le SKILL.md traite r/economics comme repli de HN ; depuis avril 2026 c'est
un canal primaire à cadence mensuelle, et le choix du contenu à y poster n'était écrit
nulle part. Ce fichier fait foi au même titre que SKILL.md.

## 10.1 Le corpus d'abord, la production ensuite

Le post mensuel se choisit dans ce qui existe avant de produire. Trois sources, dans cet
ordre : `python scripts/dashboard.py reco` (cadence, rotation, survie), le snapshot filtré
sur les études et registres EN jamais loggés dans `reconomics_posts.csv`, la chronologie
`events.csv` des trois dernières semaines. Une étude publiée et jamais distribuée vaut
plus qu'une étude neuve produite en quatre jours : elle a déjà passé ses verrous.

## 10.2 Les quatre critères, tous nécessaires

1. **Actualité macro de la semaine.** L'événement qui occupe le sub le jour du post
   (décision Fed, chiffre d'inflation, choc) désigne le cluster. Le sweet spot documenté
   par le post #2 : publier après qu'un événement a testé la thèse, jamais avant.
2. **Rotation.** Cluster et posture des trois derniers posts dans `dashboard.py reco`.
   Un cluster déjà servi deux fois sur six se saute même s'il est d'actualité (le
   18/09/2026, la page « disinflation doesn't stick » avait raison depuis mai et a été
   écartée : inflation déjà 2 posts sur 6 dont le dernier).
3. **Robustesse Rule III.** Posture descriptive (la seule à 117 000 vues, les deux
   postures « challenge » retirées), context box dès la première section, sensibilités et
   limites déjà dans la page. Une étude qui doit être blindée après coup n'est pas prête
   pour ce mois-ci.
4. **Hook ≤25 mots vérifié par calcul.** Le chiffre du hook se recalcule depuis la source
   primaire le jour du choix, pas depuis la page. Sur #6 : 129 pb sur clôtures FRED,
   75 pb sur moyennes mensuelles, deux chiffres vrais et non sommables, désamorcés dans
   l'OP.

## 10.3 Calculer avant de préférer

Le meilleur titre du 18/09/2026 était un registre neuf, « chaque reprise de hausse après
un cycle de baisse depuis 1954 ». Dix minutes de calcul sur DFEDTAR l'ont tué : neuf
« retournements » entre 1983 et 1988 sur des micro-ajustements, et aucun motif dans ce
qui a suivi (récession à 22 mois en 1999, à 89 mois en 1983). Règle : toute candidate
dont le hook n'a pas été recalculé sort de la liste, quelle que soit sa surface virale.
C'est la même doctrine que la Thesis Pivot de `production-research-study`, appliquée
avant la production plutôt qu'après.

## 10.4 Ce que le mémo de lancement contient

Un fichier daté dans le dossier de l'étude : la décision et ses quatre critères, le tableau
des chiffres vérifiés avec leur source et leur date, le hook, le titre principal et le
fallback, le commentaire OP complet (désamorçage en première ligne, mix de fréquences,
repro en clôture), le steelman en réserve, le timing avec le calendrier macro du jour, la
liste des candidates écartées avec la raison chiffrée. Le journal `reconomics_posts.csv`
se remplit à J+48h depuis ce mémo, pas de mémoire.

## 10.5 La vignette

Reddit lit le premier `og:image` de la page. Sur eco3min.fr c'est RankMath qui l'émet,
depuis l'image à la une, avant le `og:image` du snippet de l'étude. Poser l'image à la une
et `facebook_image` sur le hero, purger le cache, puis tester sur opengraph.xyz. Le hero
avec bandeau de tuiles KPI (post #5, Sahm) reste la meilleure vignette du registre.

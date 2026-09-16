# formats-eco3min — référence : Méta-titre, ancres internes, sources autorisées, outils, bulletin, format HTML (§7 à §12)

Extrait VERBATIM de SKILL.md (découpage du 16/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 7. Méta-titre — règles

**Interdit** : année explicite (2025, 2026), date calendaire, "actuellement", "aujourd'hui", "cette année". Le titre doit rester pertinent dans 6–12 mois.

**Actualité implicite** : un mécanisme qui évolue, un seuil franchi, une inflexion, un déséquilibre — sans dater.

**Test** : si le titre est amélioré en supprimant la date, la version sans date est obligatoire.

**Évite** : titres vagues ("tendances", "panorama", "le marché de…").

---

## 8. Variation des ancres internes

Trois règles cumulatives.

**Inter-articles** : pour un même lien cible, des articles différents utilisent des ancres différentes.

**Intra-article** : aucune ancre n'est répétée dans un même article. 5 liens = 5 ancres distinctes.

**Qualité** :
- 3 à 8 mots
- Descriptive du contenu de la cible
- Intégrée naturellement dans une phrase
- Jamais "cliquez ici", "voir ici", "lire aussi", "en savoir plus"

**Exemple** — pour des liens vers `/cycle-economique/`

| Article | Ancre |
|---|---|
| Majeur | les dynamiques du cycle économique |
| Satellite 1 | comprendre les phases conjoncturelles |
| Satellite 2 | l'alternance expansion-récession |
| Satellite 3 | le fonctionnement des cycles |

---

## 9. Sources autorisées (référence rapide)

Citer **institution + date** dans le flux du texte. Pas de section "Sources" en fin d'article, pas d'URL externes, pas de notes de bas de page.

**Banques centrales** : Fed (Réserve fédérale), BCE, BoE, BoJ, BNS.

**Institutions internationales** : FMI, OCDE, BRI (Banque des règlements internationaux), Banque mondiale.

**Statistiques nationales** : INSEE (France), BLS / Bureau of Labor Statistics (USA), Eurostat, ONS (UK), Destatis (Allemagne).

**Enquêtes bancaires clés** : *Bank Lending Survey* (BCE), *Senior Loan Officer Opinion Survey* / SLOOS (Fed).

**Autres** : Trésors et ministères des Finances, autorités de régulation (AMF, SEC, FCA), agences de notation (Moody's, S&P, Fitch — pour ratings uniquement).

**Données estimées** : préfixer avec `≈` et expliciter brièvement la méthode.

**Exemples conformes**
- "Selon le *Bank Lending Survey* de la BCE (T4 2025), 42 % des banques de la zone euro…"
- "D'après les séries longues de la BRI, le ratio crédit/PIB est passé de ≈165 % au T1 2010 à ≈180 % fin 2021."
- "Le *Senior Loan Officer Opinion Survey* de la Fed (janvier 2026) indique…"

---

## 10. Outils Eco3min — linking interne (optionnel)

Trois outils analytiques **du pôle macro** sont listés ci-dessous. **Maximum 1 lien outil par article. Aucun lien outil = choix valide.** Insérer un lien uniquement si l'outil éclaire un point précis du raisonnement. Les outils éligibles dépendent du pilier : d'autres piliers ont (ou auront) leurs propres outils — la pipeline B reçoit la liste éligible en paramètre.

| Outil | URL | Quand l'utiliser |
|---|---|---|
| **Lecture du cycle de taux** | `/outils-analyse-macroeconomique/lecture-cycle-taux/` | Articles sur politique monétaire, taux, crédit, immobilier via financement, marchés dépendants du régime de taux — surtout si le texte évoque variation, plateau, durée de maintien, délais |
| **Diagnostic du cycle macro** | `/outils-analyse-macroeconomique/diagnostic-du-cycle-macro-cadre-danalyse-eco3min/` | Articles macro ou pont, lectures de régime, études de cas transversales — surtout si le texte évoque ambiguïté de régime, signaux contradictoires, transition lente, stabilité fragile |
| **Indicateur économique trompeur** | `/outils-analyse-macroeconomique/indicateur-economique-trompeur/` | Articles évoquant indicateurs rassurants, résilience apparente, marchés calmes, chômage bas, inflation stable, bénéfices solides — quand un risque de lecture biaisée existe |

**Règles**
- Ancre neutre et descriptive ; jamais "voir notre outil", "outil eco3min"
- Lien intégré dans un paragraphe analytique, jamais en intro ou conclusion
- Si retirer le lien ne change rien à la compréhension de l'article → ne pas l'insérer

---

## 11. Bulletin macro hebdomadaire — linking interne (optionnel)

URL : `/barometre-macroeconomique-feuille-de-route/`

À mentionner ponctuellement, jamais systématiquement. Ancre naturelle ("le point macro hebdomadaire", "le baromètre macro", etc.), pas d'ancre SEO.

---

## 12. Format HTML général

Compatible WordPress Gutenberg.

**Balises autorisées** : `<h2>`, `<h3>`, `<p>`, `<strong>`, `<em>`, `<ul>`, `<li>`, `<a href="">`.

**Encarts** : `div` nus, sans repères `<!-- wp:html -->` ni aucun autre commentaire HTML (décision du 16/09/2026 ; voir le RAPPEL BLOQUANT de SKILL.md).

**Interdit** : Markdown, `<html>`, classes CSS custom (sauf préfixe `eco3min-` et le bloc `.eco3-tldr`), styles inline.

**Méta-description** : portée par le champ `rank_math_description` du JSON de sortie (≤155 caractères), **jamais dans le corps**. Ne pas l'écrire en `<p><em>…</em></p>` en tête d'article (elle s'afficherait en italique et doublerait le chapeau).

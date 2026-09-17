# production-every-x-record — référence : Design graphique découplé du brand kit, interdits de cosplay (§2)

Extrait VERBATIM de SKILL.md (découpage du 17/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 2. Design graphique — DÉCOUPLÉ DU BRAND KIT ECO3MIN

**Principe figé : une page backlink n'optimise PAS la cohérence avec le site. Elle optimise les CODES VISUELS DU GENRE (autorité FT / Fed / Bloomberg) + la lisibilité en vignette + la survie en dark-mode.** Le brand kit Eco3min (fond crème #F8F5EE, terracotta #B85C3C) est fait pour le site, pas pour ces pages. La palette se choisit par objectif, page par page.

> "Optimal pour la viralité" est un faux levier partiel : aucune couleur ne *fait* le partage. Ce qui scrolle-stoppe = **contraste fort + lisibilité une fois rétréci à ~400px + tenue en dark-mode + une seule couleur qui pointe l'anomalie**. La sobriété EST l'optimisation. Plus de couleurs = moins de partage.

### 2.1 Palette optimale par défaut (record / anomalie)
- **Fond : blanc pur `#FFFFFF`** (ou `#FCFCFC`). Code FT/Fed, contraste max, tient en dark-mode (le feed pose un cadre clair). **Jamais de crème** ici (vire au beige sale en vignette / dark-mode).
- **Texte : encre quasi-noire `#14141A`.**
- **Séries/contexte (l'histoire, le récit) : gris neutre `#9CA3AF`.** C'est le FOND.
- **Bandes de contexte (récessions, zones) : gris froid `#D9DCE1`.**
- **Grille : gris très clair `#E3E5E9`.**
- **UN SEUL accent saturé, RÉSERVÉ à l'élément focal/l'anomalie : rouge vermillon `#E03127`** (registre "alerte / exception / le chiffre qui compte" — le défaut FT pour la donnée saillante). La ligne de seuil/référence critique peut prendre l'accent (pointillé) car sémantiquement liée à l'anomalie.

### 2.2 Figure / fond (le dispositif qui fait l'aha)
- **Contexte en gris muet, anomalie en accent saturé.** L'œil doit voir "X chose en rouge = l'exception" en 3 secondes.
- **L'accent est RÉSERVÉ.** Ne JAMAIS colorier les éléments de contexte dans l'accent. (Anti-pattern réel : colorier les pics de récession en rouge "pour les rendre visibles" → détruit le figure/fond, on ne voit plus l'anomalie. Les rendre visibles autrement — voir §2.3.)
- **Dispositif géométrique de l'aha (autorisé, léger)** : un tracé auxiliaire discret qui MATÉRIALISE le finding peut porter l'accent s'il lui est sémantiquement lié — même statut que la ligne de seuil de §2.1 (cas réel : escalier pointillé rouge reliant les trois pics croissants 1970→1974→1980 ; alpha ~0,5, trait fin, il souligne sans concurrencer la série). Un seul dispositif par visuel ; s'il faut l'expliquer par une légende dédiée, il est trop malin.

### 2.3 Le piège de l'axe Y (récurrent) + labels off-scale
Si la donnée a des outliers énormes qui écrasent le seuil/l'anomalie dans les 10 % bas du graphe (ex. Sahm COVID = 9,5 ; 1975 = 3,8 vs seuil 0,50 et anomalie 0,57) → **plafonner l'axe** à une valeur qui rend le seuil + l'anomalie lisibles, et **laisser les gros pics sortir par le haut** (clip).
- **Labeller chaque pic hors-échelle avec sa valeur** (ex. "9.5", "3.9") en **gris foncé `#54545f`** (PAS en accent). Répond à "pourquoi l'axe est coupé ?" et prouve "ces pics montent jusqu'à 9.5, hors échelle". C'est la bonne façon de rendre le dépassement visible sans casser le rouge.

### 2.4 Typographie (seul héritage toléré, car il sert l'autorité)
Le trio peut rester : **serif éditorial pour le titre** (Source Serif 4 — un serif de qualité signale "éditorial sérieux", code FT), **sans pour les labels/UI** (Inter), **mono pour les chiffres** (IBM Plex Mono). Ce n'est PAS une obligation de brand — c'est que ces fonts servent l'objectif autorité. Ce qui rompt avec le brand = le FOND et la COULEUR d'accent, pas forcément la typo.
- Piège technique mono : IBM Plex Mono n'a pas l'espace fine (U+2009) → utiliser l'insécable U+00A0 pour les nombres FR ("4,2 %"), sinon glyphe manquant au rendu.

### 2.5 Autorité EARNED, jamais ASSERTED — interdits de cosplay (FIGÉ)
**L'autorité se gagne par le CONTENU (rigueur, dataset ouvert, finding honnête, méthodologie transparente, source primaire). Elle ne s'AFFICHE jamais par des widgets.** Une page solo qui colle les insignes d'une revue académique ou d'un institut signale l'inverse de ce qu'elle vise : un curateur FT/Ritholtz sent le toc immédiatement (ça BAISSE la crédibilité), et r/economics lit ça comme de l'auto-promo (risque Rule IV). Une page de référence FT/Fed est SOBRE et CONFIANTE — pas une landing de content-marketing, pas un cosplay de papier. C'est le pendant visuel de l'honnêteté-comme-blindage (§1.2) : on ne décore pas, on prouve.

**INTERDITS explicites — ne JAMAIS mettre sur la page :**
- Bloc **"Cite this" / "How to cite"**, citation format type BibTeX/APA, **DOI** ou identifiant fabriqué → cosplay de revue.
- Rangée de boutons **"Share" / "Share this research"** (X, LinkedIn, Reddit…) → auto-promo, try-hard, signal Rule IV.
- **Click-to-copy** (bouton/affordance "copier la phrase", "copy stat", copy-icon sur le hook) → même famille que les share-buttons : ça RÉCLAME la citation au lieu de la mériter. Un journaliste sélectionne et copie tout seul. (Correction v2 : une version antérieure de ce skill le prescrivait dans le snippet — c'était en contradiction directe avec cette section ; il est désormais banni.)
- **Badges / pills** "Public dataset", "Open research", "Peer-reviewed", "Verified", trust-seals, compteurs de vues/citations → autorité assertée.
- **Badge / logo de licence décoratif** (le logo CC en gros) → la licence est une LIGNE de meta discrète, pas un insigne.
- Bloc **auteur / affiliation / ORCID** façon académique, "About the researcher" → tu es un éditeur, pas un labo ; le prétendre se retourne.
- Cadre labellisé **"Abstract"**, "Working paper", "Download the paper / PDF version" → c'est une PAGE, pas un papier.
- Capture **email / newsletter** (déjà banni §4) → clarté de mission.

**AUTORISÉ (c'est du contenu / de la transparence, pas du cosplay) :**
- Bouton **CSV** simple (donnée ouverte utile) · **ligne de meta** discrète "License: CC BY 4.0" (rend la donnée réutilisable, sans insigne) · **source** FRED · NBER · section **Méthodologie** (substance : comment le chiffre est calculé) · **TL;DR** en langage simple (PAS "Abstract") · petit **kicker** de section éditorial (≠ CTA de prestige).

**Règle de tri :** est-ce du **CONTENU** (ça informe / prouve / explique) ou de la **DÉCORATION** (ça réclame qu'on te traite comme prestigieux / qu'on partage) ? Le contenu reste, la décoration dégage.

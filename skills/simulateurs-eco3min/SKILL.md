---
name: simulateurs-eco3min
description: "Production et maintenance des simulateurs interactifs d'Eco3min (pages outils, FR/EN). Architecture figée : un snippet global Code Snippets (CSS + moteur JS vanilla + shortcode [eco3min_simulateur type=\"…\" lang=\"fr|en\"]) rend le markup par type+langue ; la page = shortcode + SEO + maillage (plus d'iframe). Activer pour créer, réviser, débugger, étendre ou traduire un simulateur. Couvre les 5 archétypes (trajectoire, composition, sensibilité, deux-branches, ledger daté), la frontière partagé vs spécifique, le contrat moteur (data-bind, synchro range↔number bidirectionnelle, dispatch boot), la méthode d'insertion assertée (node --check, sanity maths), l'AMF data viz (jamais de trajectoire prospective unique, marqueurs descriptifs, pas de montant empruntable max, asymétrie de risque), la cohérence des chiffres avec le hero, les tokens brand web, l'i18n, et le protocole page (slugs EN plats vs imbriqués, jamais inventer un slug, parentage /en/ → 301). Combiner avec brand-kit-eco3min, visuels-eco3min, pilier-kit."
---

# Simulateurs Eco3min

> Les outils interactifs (calculateurs, simulateurs) des pages outils d'Eco3min.
> **Principe directeur** : un simulateur ne prédit pas un résultat — il rend visibles
> les hypothèses sous lesquelles ce résultat tient. L'outil doit *incarner* la thèse
> éditoriale, pas seulement la prêcher en prose.
> Esthétique FT/Bloomberg : sobre mais pas inerte. L'intensité passe par la hiérarchie
> et l'accent terracotta unique, jamais par la décoration (pas d'ombre, pas de dégradé).

Artefact canonique : `eco3min-simulateurs-snippet.php` (état courant **v2.0**, 9 types — série complète, plus aucune iframe).

---

## 1. Architecture figée (3 couches)

1. **Snippet global** (Code Snippets, PHP, « Run everywhere », collé SANS `<?php`) :
   - `eco3_simu_css()` — CSS `.eco3-simu*` (préfixé, aucune touche au global/Blocksy).
   - `eco3_simu_js()` — moteur JS vanilla, zéro dépendance, auto-gardé (heredoc `ECO3JS`).
   - `eco3_simu_markup($type,$lang)` — markup déclaratif par type + langue (heredoc `HTML`).
   - shortcode `eco3min_simulateur` + enqueue **conditionnel** (assets seulement sur les
     pages qui appellent le shortcode).
2. **Shortcode** dans la page : `[eco3min_simulateur type="…" lang="fr|en"]` (`lang` défaut `fr`).
3. **Page** (Gutenberg, vue Code) : shortcode + prose SEO + maillage. Rien d'autre.

**Pourquoi.** Opérateur solo, souvent mobile : un bug de layout se corrige **une** fois
dans le snippet, pas dans N pages. Le pilier-kit réserve déjà le snippet comme l'endroit du JS.

**Ce que ça remplace.** Les iframes `wp-content/uploads/.../index*.html` : hauteur figée (CLS),
hors-charte, **SEO invisible à Google** (caché dans l'iframe). Reconstruire en natif, jamais reporter une iframe.

---

## 2. Contrat moteur (invariants — ne pas casser)

- Racine : `<div class="eco3-simu" data-eco3-simu="{type}" data-lang="{fr|en}">`.
  `boot()` lit ces deux attributs et dispatche vers `init{Type}`.
- **Champs** : chaque entrée a un `data-bind`. Un `data-bind` groupe un `input[type=number]`
  ET un `input[type=range]`. **Le `number` est la source de vérité** ; le `range` est
  `aria-hidden tabindex="-1"`.
- **Synchro range↔number BIDIRECTIONNELLE** (piège v1.0→v1.1) : `syncFrom(el,k)` copie
  range→number au glissement, number→range (clampé) à la frappe. Sans le sens range→number,
  le curseur bouge puis se fait écraser et rien ne se calcule.
- **Sorties** : `data-out`. Le conteneur résultats est une grille 2 colonnes par défaut ;
  pour 3 cartes utiliser une classe `.is-three` (pas de `:has()`).
- **3 champs d'entrée → grille 3 colonnes** : ajouter le type au sélecteur partagé
  `…__grid{grid-template-columns:repeat(3,minmax(0,1fr))}` (+ repli 1 colonne mobile). Sinon
  3 champs donnent un orphelin 2+1. Déjà groupé : `capital-rentes`, `risque-taux`, `budget`,
  `rendement-reel` — y **ajouter** le nouveau type, ne pas dupliquer la règle.
- **Arrondir tout chiffre affiché** (`Math.round` / `Intl.NumberFormat`) — les floats fuient.
- **SVG construit en JS** (pas de lib), viewBox `0 0 720 360`, `width:100%;height:auto`.
- Valeur vedette potentiellement infinie (`∞`) : l'afficher **courte** dans la carte, le
  détail va dans la phrase de synthèse — sinon la carte déborde.

---

## 3. Les 5 archétypes (le cœur)

Chaque outil tombe dans un archétype. L'archétype fixe la **maths**, le **layout des 2 cartes**
et le **visuel signature**. Ne pas plaquer un visuel d'un archétype sur un autre.

| Archétype | Thèse-type | Maths | Cartes (cool / terra) | Visuel signature | Exemples |
|---|---|---|---|---|---|
| **A. Trajectoire** | un chiffre vedette cache le chiffre qui compte | capitalisation / déplétion sur axe **temps** ; 1 à 3 lignes | chiffre regardé / chiffre réel | courbes sur X=temps ; bande ou coin terra ; point terra ; valeurs en bout | `interets-composes` (nominal vs réel), `resilience-financiere` (normal vs choc → durée) |
| **B. Composition** | un ratio/total ne dit rien sans sa décomposition | décomposition d'un total **à un instant** | ratio / part-clé restante | **barre empilée horizontale** + marqueur(s) de seuil descriptif | `capacite-endettement` (taux vs reste à vivre, marqueur HCSF 35 %), `budget` (besoins/envies/épargne, repères 50-30-20 à 50 % et 80 %) |
| **C. Sensibilité / fonction** | le résultat est l'otage d'**une** hypothèse | `f(hypothèse)` — hyperbole, droite, droite **signée**, ou Fisher | hypothèse effective / résultat | **courbe Y=résultat vs X=hypothèse**, point terra de l'utilisateur, référence/seuil | `capital-rentes` (capital vs taux), `epargne-mensuelle` (effort vs durée), `risque-taux` (Δvaleur vs Δtaux, **axe signé**), `rendement-reel` (réel vs inflation, **axe signé** + seuil) |
| **D. Deux branches / arbitrage** | l'écart entre deux options décide, pas l'intuition | deux trajectoires comparées ; l'**écart** = résultat | écart/spread / avantage | **deux courbes divergentes**, coin terra = avantage cumulé | `arbitrage-credit-epargne` (placer vs rembourser) |
| **E. Ledger daté / règle de calcul** | le résultat dépend des **dates** de chaque flux, pas d'un taux affiché | opérations datées saisies (liste dynamique) → moteur qui rejoue la règle réglementaire période par période (quinzaines, capitalisation, plafond) ; les paramètres externes (taux de chaque période, indice des prix) sont **lus dans une source du site**, jamais codés dans l'outil | résultat de la règle (terra) / solde nominal (cool) / paramètre appliqué (gris) | **marches du solde rémunéré + courbe des intérêts cumulés** sur l'axe des périodes, tableau déplié par période | `livret-a-quinzaines` (snippet autonome 18/09/2026 : versements et retraits datés, taux lus dans les `periods` du snippet 230 et dans le dataset des paliers, IPC INSEE servi par le site pour la lecture en pouvoir d'achat) |

Notes structurantes :
- **A et D** partagent le moteur de tracé temporel (multi-lignes) ; D ajoute le coin entre
  courbes et la prudence anti-prescription (ne jamais désigner une option « gagnante »).
- **C** est la forme qui satisfait l'**AMF §2.4** en *refusant* de donner un nombre unique :
  réserver C aux sujets où la sensibilité à une hypothèse EST la thèse.
- **C — sous-cas « axe signé »** : quand l'hypothèse et/ou le résultat peuvent passer en négatif
  (Δtaux ±, inflation > nominal), l'axe Y est **centré sur 0** (gain au-dessus, perte en dessous),
  ligne zéro appuyée, et le **seuil de bascule** marqué (pointillé + label). Vu sur `risque-taux`
  (droite de pente −duration, hausse ET baisse) et `rendement-reel` (courbe Fisher croisant 0 à
  inflation = nominal). Le point utilisateur reste l'unique accent terra.
- **B** est le seul à ne pas avoir d'axe temps → barre, pas courbe.
- **E** est le seul archétype à **liste dynamique d'entrées** (ajout / suppression de lignes datées) et le seul dont la maths est une **règle exogène** (texte réglementaire, pratique bancaire) plutôt qu'une formule financière : le moteur se teste contre un port indépendant (Python) et deux ou trois cas analytiques avant toute page, et il refuse de calculer au-delà de la dernière période publiée (« aucun taux publié à partir du… », jamais une projection). Ses paramètres vivent hors de l'outil : une constante de taux dans le JS est un défaut. Sous douze mois, un indice des prix brut est saisonnier : la lecture en pouvoir d'achat passe alors par le glissement annuel du dernier mois publié au prorata, et le dit.
- Avant de coder : nommer l'archétype. S'il n'en existe pas, c'en est un 6ᵉ → l'ajouter ici.

---

## 4. Partagé vs spécifique

**PARTAGÉ — ne jamais redévelopper par type :**
- shell snippet (enqueue conditionnel, shortcode, `sanitize_title`), structure markup
  (head : kicker mono + filet doré + titre serif + sous-titre ; grille champs ; cartes
  résultats `--nominal`/`--real` ; bloc chart ; breakdown ; source) ;
- CSS `.eco3-simu*` + tokens web + responsive ;
- moteur : `data-bind`, `syncFrom` bidir, `readVal`, `niceMax`, dispatch `boot()` ;
- i18n `I18N[lang]` + locale monétaire ; AMF (ligne source, accent terra unique) ;
- déploiement et conventions de page.

**SPÉCIFIQUE par type :** la maths (`compute()`), les labels des 2 cartes, le visuel
(`draw()`), les clés `I18N.{type}` du type, les marqueurs descriptifs propres.

Si une « spécificité » se répète sur 2 types, elle remonte dans le partagé.

---

## 5. Ajouter / modifier un type — méthode assertée

Le fichier dépasse 1000 lignes : **jamais d'édition à l'aveugle**. Insertion par script
Python avec assertion de comptage sur chaque ancre.

1. **Markup** : insérer `case '{type}':` (bloc `if ($lang==='en'){…}` heredoc EN, puis FR
   heredoc par défaut) **avant** `default:`. Ancre : `\n\n\t\tdefault:`, `assert count==1`.
2. **I18N** : ajouter `{type}:{…}` dans `I18N.fr` ET `I18N.en` (légende, libellés d'axe,
   delta, phrase breakdown, libellés infini/équivalence). Ancres = fermetures de bloc, `assert count==1`.
3. **Module + dispatch** : insérer `init{Type}(root)` avant `function boot(){`, et
   `case '{type}': init{Type}(root); break;` après le dernier case. `assert count==1` sur chaque.
4. **Bumper** version + chaîne d'enqueue (`'1.x'`).

**Vérification obligatoire après chaque insertion** (sinon on shippe un snippet cassé) :
- heredocs équilibrés : `grep -c "^HTML;$"` == `grep -c "<<<'HTML'"` (= 2 × nb de types) ;
- extraire le bloc `ECO3JS` (`sed -n "/<<<'ECO3JS'/,/^ECO3JS;$/p" | sed '1d;$d'`) → `node --check` ;
- **sanity maths** en `node -e` sur 2-3 cas : défaut + une borne (taux 0, déficit ≤0, etc.).

Le module type suit toujours : lire `data-lang` → `T = I18N[lang].{type}` + formatteur →
`readVal`/`syncFrom` → `compute()` (écrit les `data-out` + appelle `draw()`) → events `input`.

---

## 6. Bilinguisme

- Markup : libellés statiques rendus côté serveur par `$lang` (y compris H1 in-tool, notes
  de carte, ligne source).
- JS : seuls les libellés **dynamiques** passent par `I18N` + le **locale monétaire**
  (`fr-FR` → `76 123 €` ; `en-IE` → `€76,123`). `shortEur` localise aussi le suffixe.
- Pas de switch runtime : une page = une langue = un `lang=`.
- WordPress : lier les deux pages comme **traductions Polylang** pour le `hreflang` — le
  snippet ne s'en occupe pas.

---

## 7. Conformité AMF (data viz + texte)

- **Règle cardinale (visuels §2.4)** : jamais une trajectoire prospective **unique** tracée
  fermement. La satisfaire selon l'archétype : A → ≥2 scénarios ; C → la courbe de
  sensibilité (montre que le résultat dépend de l'hypothèse) ; D → deux branches comparées.
- **Marqueurs = descriptifs, jamais prescriptifs.** Repères factuels autorisés en gris neutre,
  étiquetés « repère / couramment cité » : HCSF 35 %, matelas 3–6 mois, fourchette de
  prélèvement 3–5 %. Jamais « vous devez / visez X ».
- **Interdits** : flèche achat/vente, cible de prix, allocation %/ratio, zone prescriptive,
  timing actionnable, et **montant empruntable maximum** (= conseil ; un outil de dette
  éclaire l'empreinte d'un crédit saisi, il ne maximise rien).
- **Arbitrages (archétype D) : asymétrie de risque obligatoire.** Comparer un taux certain
  (crédit, sans risque) à un rendement *espéré* (placement risqué) doit être dit
  explicitement — sous-titre + synthèse + source : « cet écart n'intègre pas le risque ».
  Ne jamais nommer une option « gagnante » de façon prescriptive.
- **Ligne source obligatoire** dans l'outil : nature de l'opération (projection /
  observation / arithmétique conditionnelle), « non prédictive », hypothèses saisies,
  base méthodo (ex. « capitalisation annuelle » ; « préservation du capital, distinct de la
  règle des 4 % »), « Eco3min — outil pédagogique, ni conseil ni recommandation ».

---

## 8. Brand & graphe (sobre ≠ inerte)

- Tokens **web** (pas la triade export) : `--e3s-cream #f8f5ee`, `--e3s-navy #1a237e`,
  `--e3s-terra #b85c3c`, `--e3s-cool #4a6b8a`, `--e3s-gold #c9a84c`, gris `#9aa3af`, lignes `#dcdfe6`.
  Polices : Libre Baskerville / DM Sans / JetBrains Mono.
- En-tête commun : kicker mono + **filet doré** `.eco3-simu__rule` + titre serif + sous-titre.
- **Accent terracotta UNIQUE = le résultat**, jamais la décoration : point/bande/coin terra
  selon l'archétype (bout de courbe réelle ; part reste-à-vivre ; point utilisateur ; coin
  d'écart). Les éléments secondaires sont cool / gris. Repères descriptifs en gris.
- Hiérarchie résultats : la carte terra `--real` domine (fond crème, ~1,85–2 rem) + delta.
- Plafond d'intensité : pousser sur le **fond** (repère historique, bande régime descriptive),
  pas sur le décor — sinon on quitte FT/Bloomberg pour le « dashboard SaaS ».
- `niceMax` = plus petit `{1,2,2.5,5,10}·10^k ≥ max` (ne pas sur-compliquer, bug v1.0).

---

## 9. Maths & cohérence des chiffres

- **Cohérence avec le publié (visuels §6)** : un outil qui afficherait 81 k à côté d'un hero
  à 76 k passe pour cassé.
- **La capitalisation est PAR PAGE, pas « annuelle » par défaut — vérifier, ne pas présumer.**
  `interets-composes` capitalise **annuellement** (cale sur son hero : `10000·1,07^30 = 76 123` ;
  `1,055^30 = 49 840` ; réel `/1,02^30 = 27 515`) : `FV = P·(1+r)^t + (m·12)·((1+r)^t−1)/r`,
  `r=0 → P+m·12·t`. `epargne-mensuelle` capitalise **mensuellement** (cale sur sa table publiée
  754/341/417/305/97 €) : `M = C·r/((1+r)^n−1)`, `r` mensuel, `n` mois, `r=0 → C/n`. Toujours
  recaler les chiffres de l'outil sur les chiffres déjà publiés de SA page avant de livrer.
- Formules par type déjà posées : mensualité amortissable `M = C·i/(1−(1+i)^−n)` (capacité) ;
  durée de résistance `épargne ÷ déficit mensuel sous choc` ; capital perpétuité
  `dépenses annuelles ÷ taux de prélèvement effectif` (effectif = rendement réel × (1−marge)) ;
  arbitrage `L·(1+rs)^n` vs `L·(1+rd)^n`, écart = résultat ; **sensibilité taux**
  `Δvaleur ≈ −duration × Δtaux` (1er ordre, convexité ignorée) ; **rendement réel (Fisher)**
  `réel = (1+nominal)/(1+inflation) − 1` (pas la soustraction ; seuil de perte à inflation = nominal).
- **Réel = déflation par l'inflation** (robuste). Rendement de rente = **réel** (sinon
  l'inflation érode la base). Inflation **s'annule** entre deux trajectoires nominales (arbitrage).
- **Hypothèses disputées = optionnelles + étiquetées.** Écart comportemental Dalbar
  (−1,5 %/an) : case à cocher, jamais par défaut, signalé contesté (Morningstar « Mind the Gap »).

---

## 10. Protocole page outil (SEO / maillage / URLs)

- Le SEO vit dans la **page** (DOM), pas dans l'outil : intro recadrée sur la thèse, mécanisme,
  exemple chiffré aligné sur le défaut de l'outil, limites, FAQ, à retenir.
- **Reconstruction depuis une iframe** : conserver l'encart d'en-tête et ses liens (corriger
  ceux qui pointent vers la mauvaise langue), remplacer l'iframe par le shortcode, **réaligner
  la copie sur ce que l'outil fait réellement** (ne pas promettre 3 leviers s'il y en a 2).
- **Règle dure : l'outil dicte la copie, jamais l'inverse.** Ne jamais agréger des unités non
  homogènes (un choc en capital € + un coût récurrent €/an) pour tenir une promesse marketing
  (« transversal »). Scoper l'outil à ce qui est **rigoureusement calculable et homogène**,
  renvoyer le reste en prose vers les outils frères. Vu 2× : résilience (page « 3 leviers » →
  l'outil ne calcule qu'une durée de résistance) ; risque-taux (page « transversal crédit +
  obligations + épargne » → l'outil ne quantifie que la jambe obligataire via la duration,
  crédit/épargne restant qualitatifs). Si la page sur-promet, on corrige la **page**.
- **Pièges récurrents à corriger en passant** : copier-coller décrivant le *mauvais* outil ;
  lien interne pointant vers une autre page outil que celle annoncée ; liens FR→`/en/` sur
  une page FR (et inverse).
- **H1 = titre WordPress de la page** (rendu en H1), **distinct** du titre interne de l'outil
  (`.eco3-simu__title`, un `<p>`) → aucun conflit de H1. Fournir H1 + slug + méta-titre + méta-desc.
- **Slugs — règle absolue : ne jamais en inventer**, surtout en EN ; n'utiliser que des URL
  confirmées (hub, pages existantes). Sinon laisser sans lien plutôt que créer un 404.
  - FR : tous sous `/page-education-financiere/outils-financiers/{slug}/`.
  - EN : **incohérent** — certains plats `/en/{slug}/`, d'autres imbriqués sous
    `/en/financial-education-macroeconomic-regimes/financial-tools-simulators-test-assumptions-decisions/{slug}/`.
    Pour un slug EN **neuf**, préférer le **plat** (majorité des satellites, évite la profondeur).
  - **Page FR mal parentée sous `/en/…`** (vu sur capacité d'endettement) : la vraie page FR
    doit migrer vers le parent FR + **301** depuis l'ancienne URL `/en/…`. Peser le coût SEO
    du 301 selon l'indexation réelle (GSC).
- Maillage = ancrage réel (diagnostic pilier-kit), pas de bourrage : sous-pilier outils,
  outils frères complémentaires, cluster du sujet, pilier. Maillage **FR sur la page FR, EN sur
  la page EN**.

---

## 11. Déploiement

- Snippet : Code Snippets → PHP → « Run everywhere », coller **sans** `<?php`, activer.
  À chaque évolution : re-coller (additif), bumper version + journal. Les pages déjà en ligne
  ne bougent pas.
- Page : coller le markup Gutenberg dans la vue **Code**. Polices déjà chargées par le thème.
- **Blocksy peut styler globalement inputs/range** : si le curseur ressort mal, passer les
  propriétés critiques de `::-webkit-slider-thumb` en `!important` (comme le pilier-kit).

---

## 12. Checklist pré-livraison

- [ ] Archétype nommé ; visuel signature = celui de l'archétype.
- [ ] Range glisse ET frappe au clavier (synchro bidirectionnelle).
- [ ] AMF §2.4 satisfaite selon l'archétype ; 1 seul accent terracotta ; ligne source présente ;
      marqueurs descriptifs ; pas de montant max / d'option « gagnante » prescriptive ; asymétrie
      de risque dite (archétype D).
- [ ] Chiffres cohérents avec le publié (capitalisation annuelle vérifiée).
- [ ] Tout montant arrondi ; format monétaire correct par langue ; vedette infinie courte.
- [ ] FR **et** EN rendus (markup + I18N) ; pages liées en Polylang.
- [ ] SEO dans le DOM (pas d'iframe) ; copie = outil réel ; maillage par langue, sans slug inventé.
- [ ] Heredocs équilibrés (`grep`) ; JS passe `node --check` ; sanity maths sur 2-3 cas.
- [ ] Mobile 380px : champs 1 colonne, résultats empilés.

---

## Registre des types (v2.0)

| `type` | Archétype | Slug FR | Slug EN |
|---|---|---|---|
| `interets-composes` | A trajectoire | `calculateur-interets-compose` | `…/compound-interest-calculator-investment-growth` (imbriqué) |
| `resilience-financiere` | A trajectoire (normal/choc) | `simulateur-resilience-financiere` | `financial-resilience-simulator-shock-absorption` (plat) |
| `capacite-endettement` | B composition | `capacite-endettement-reste-a-vivre-simulateur` | `debt-capacity-disposable-income-simulator` (plat, à publier) |
| `budget` | B composition (50-30-20) | `gestion-budget-personnel` | `personal-budget-management` (plat) |
| `capital-rentes` | C sensibilité | `capital-vivre-de-ses-rentes-simulateur` | `capital-required-investment-income-simulator` (plat, à publier) |
| `epargne-mensuelle` | C sensibilité (effort/durée) | `calculateur-depargne-mensuelle-objectif` | `monthly-savings-calculator-target-goal` (plat) |
| `risque-taux` | C sensibilité (axe signé) | `sensibilite-risque-taux-simulateur` | `interest-rate-risk-sensitivity-simulator` (plat) |
| `rendement-reel` | C sensibilité (Fisher, axe signé) | `simulateur-rendement-reel-apres-inflation` | `…/real-return-after-inflation-calculator` (imbriqué) |
| `arbitrage-credit-epargne` | D deux-branches | `arbitrage-credit-ou-epargne-simulateur` | `debt-repayment-savings-tradeoff-simulator` (plat) |
| `livret-a-quinzaines` (snippet autonome « Eco3min — simulateur-livret-a-quinzaines », shortcode `[eco3min_livret_a_quinzaines]`) | E ledger daté | `simulateur-livret-a-interets-quinzaine` (page 43510, parent `outils-financiers`) | — (FR seule : la règle des quinzaines est un objet français) |

FR tous sous `/page-education-financiere/outils-financiers/`. Les EN imbriqués sont sous
`/en/financial-education-macroeconomic-regimes/financial-tools-simulators-test-assumptions-decisions/`.
**Snippets autonomes.** Depuis août 2026, les outils à moteur spécifique (prix à la pompe 211, crack 212, replay retraite 215, inflation 240, Livret A quinzaines) vivent chacun dans **leur propre snippet** (CSS + moteur + shortcode + JSON-LD base64 gardé par slug), livrés par le bundle « Page bilingue » ; le snippet global v2.0 reste celui des 9 types à `data-bind`. Un type nouveau va dans le snippet global s'il tient dans le contrat moteur §2, dans un snippet autonome sinon.

**Série complète — plus aucune iframe.** Restent côté plateforme (contenus déjà produits) :
publier capacité EN (slug plat) et capital-rentes EN, et migrer la page capacité FR sous le
parent FR + 301 depuis son URL `/en/…` actuelle (mal parentée).

---

## Versioning

**Skill v2.2** (18/09/2026) — **5ᵉ archétype E, ledger daté / règle de calcul** (S009, simulateur Livret A par quinzaine) : liste dynamique d'opérations datées, règle exogène rejouée période par période, paramètres lus dans une source du site (snippet 230, dataset des paliers, IPC servi), port Python de contrôle, refus de projeter au-delà de la dernière période publiée, prorata du glissement annuel sous douze mois. Registre des types : ligne `livret-a-quinzaines` ; note sur les snippets autonomes. Aucune règle antérieure supprimée.

**Skill v2.1** (mai 2026) — série **complète : 9 types** sur les 4 archétypes (plus aucune
iframe). Ajoute : le **sous-cas « axe signé »** de l'archétype C (résultat/hypothèse négatifs,
axe Y centré sur 0, seuil de bascule — `risque-taux`, `rendement-reel`) ; l'invariant **grille
3 colonnes** pour les types à 3 champs (sélecteur partagé à étendre) ; la **capitalisation par
page** (annuelle pour `interets-composes`, mensuelle pour `epargne-mensuelle` — recaler sur les
chiffres publiés de la page, ne pas présumer) ; les formules Fisher et duration ; la **règle dure
« l'outil dicte la copie »** (jamais agréger des unités non homogènes pour tenir une promesse
« transversale »). Registre des slugs FR/EN à jour (capacité EN → slug plat).

**Skill v2** (mai 2026) — généralise sur **4 archétypes** prouvés bilingues (trajectoire,
composition, sensibilité, deux-branches), 5 types livrés. Formalise la frontière partagé /
spécifique, la méthode d'insertion assertée + vérification (heredocs, `node --check`, sanity
maths), l'AMF élargie (marqueurs descriptifs, pas de montant max, asymétrie de risque), et le
protocole page complet (recadrage SEO, slugs FR/EN plats vs imbriqués, parentage `/en/` → 301,
H1 vs titre in-tool). Remplace le v1.

**v1** (mai 2026) — figeait l'architecture snippet/shortcode/page, le contrat moteur, l'AMF,
le graphe éditorial, la cohérence des chiffres, l'i18n et le déploiement, sur le seul archétype
mono-métrique (intérêts composés).

Snippet : v1.0 (graphe plat) → v1.1 (synchro bidir + graphe éditorial) → v1.2 (bilingue, I18N) →
v1.3 (`capacite-endettement`, archétype composition) → v1.4 (`resilience-financiere`) →
v1.5 (`capital-rentes`, archétype sensibilité) → v1.6 (`arbitrage-credit-epargne`, deux-branches) →
v1.7 (`epargne-mensuelle`, capitalisation mensuelle) → v1.8 (`risque-taux`, axe signé / duration) →
v1.9 (`budget`, composition 50-30-20) → v2.0 (`rendement-reel`, Fisher / seuil — série complète).

---

## RAPPEL BLOQUANT — Zéro commentaire HTML dans le contenu publié

Les marqueurs de section en commentaire HTML utilisés dans les templates de ce skill
(`<!-- 1. INTRO -->`, `<!-- 5. MACRO TAKEAWAY -->`, etc.) sont des **repères d'assemblage**.
Ils ne survivent pas dans le HTML livré : on les retire avant de coller le contenu ou d'émettre
le bundle.

Motif : Autoptimize scanne `<script>` / `<style>` en regex **sans ignorer les commentaires HTML**.
Une balise littérale citée en prose dans un commentaire fait avaler du texte au minifieur JS,
provoque une fatale dans le callback de buffer et renvoie un **HTTP 500 avec le corps complet** —
page normale dans le navigateur, invisible pour Google. Incident du 27 août 2026, 8 pages
désindexées. `wpautop` mutile en plus ces commentaires (enveloppe en `<p>`, saut de ligne inséré
au milieu dès qu'un nom de balise bloc y figure).

Règle canonique, vérifications mécaniques et alternative (commentaire PHP dans le snippet) :
voir `eco3min-import-contenu-bilingue`, section « RÈGLE FIGÉE (août 2026) ».

Contrôle avant livraison :

```python
import re
assert not re.findall(r'<!--.*?-->', html, re.S), "commentaire HTML dans le contenu"
```

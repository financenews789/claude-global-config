---
name: regime-classifier-eco3min
description: "Architecture, taxonomie et production de tout ce qui touche à la classification de régime macro d'Eco3min : la card live [eco3min_regime] (snippet PHP Code Snippets), les pages dashboard (/regime-aujourdhui/, /en/current-regime/), la page méthodologie (/methodologie-classification-regime-macro/ + EN), et les 12 pages Atlas (6 régimes × FR/EN). Active ce skill pour toute création, révision ou débogage touchant : la taxonomie des régimes, le vocabulaire des couches, le crosswalk card→Atlas, le snippet [eco3min_regime], le dashboard, la méthodo, ou une page Atlas. RÈGLE CARDINALE figée mai 2026 : architecture à 3 couches dont le critère de coupe est falsifiable (le moteur calcule-t-il un signal, oui/non), et qui ne doit jamais présenter comme « mesuré » ce qui relève du « jugé ». À combiner avec archi-eco3min (structure site), editeur-eco3min (AMF, style), pilier-kit (design Atlas), pipeline-eco3min (données du JSON regime_current.json)."
---

# Regime Classifier Eco3min — architecture et production

## 0. Règle cardinale (à ne jamais casser)

La classification Eco3min vend une chose : **un verdict formel, reproductible, vérifiable**.
Tout ce qui suit existe pour protéger cette promesse. La ligne rouge :

> **Ne jamais présenter comme « mesuré » ce qui relève du « jugé ».**

Le critère qui sépare le calculé du jugé est **falsifiable** : *le moteur produit-il un signal
pour cet objet, oui ou non ?* Ce critère tranche toute ambiguïté de placement (voir §1).

---

## 1. Architecture à 3 couches (figée mai 2026)

Deux grilles de lecture **distinctes** coexistent et ne doivent jamais être confondues ni
fusionnées :

### Les 3 AXES = les ENTRÉES du calcul (ce que le moteur mesure)
- **Axe 1 — Croissance (G)** : CFNAI-MA3. États G+ / G= / G−.
- **Axe 2 — Inflation (I)** : Trimmed Mean PCE 12m (Dallas Fed). États I+ / I= / I−. Mesure
  l'inflation **sous-jacente** (exclut l'énergie → un choc pétrolier transitoire ne bouge pas
  cet axe ; c'est voulu, signalé par le flag `headline_underlying_divergence`).
- **Axe 3 — Conditions financières** : NFCI (Chicago Fed). Qualificatif 4 niveaux
  (accommodant / neutre / restrictif / stress aigu).

### Les 3 COUCHES = la NATURE des objets de régime (ce que produit/encadre la classification)

| Couche | Objets | Statut | Horizon | Codes G/I | Critère |
|--------|--------|--------|---------|-----------|---------|
| **1 — Cyclique** | Grille G×I : 7 régimes + transition. Méta-régimes Atlas : Inflationniste (colonne I+), Désinflationniste (colonne I−) | **CALCULÉ live** | mois/trimestres | **OUI** | sort des axes 1+2 |
| **2 — Overlay** | Dollar Shortage (+ le qualificatif NFCI en préfixe) | **CALCULÉ live** | semaines/mois, sans hystérésis | **NON** | l'axe 3 produit un signal |
| **3 — Structurel** | Stagnation séculaire, Répression financière, Dominance fiscale | **NON calculé — cadre éditorial** | années (déforme la grille) | **NON** | aucun signal live |

**La ligne de partage couche 2 / couche 3 est le cœur du système** : Dollar Shortage a
3 signaux mesurés (DTWEXBGS +5%/3m, NFCI >+0.30, HY OAS +150bps/4sem) → couche 2. Stagnation,
répression, dominance n'ont aucun signal live → couche 3. Cette frontière protège la crédibilité :
elle est vérifiable et empêche de sur-vendre le moteur.

### Pourquoi 3 et pas 2
Ne JAMAIS fusionner couches 2 et 3 sous « hors-grille ». « Hors-grille » est une négation, pas
une couche. La couche 2 se **superpose** à un état (court terme, réversible) ; la couche 3
**déforme la grille elle-même** (un r* durablement bas change ce que « G+ » signifie). Horizons
et statuts de preuve différents → deux couches.

### Double sens d'« overlay » (piège de vocabulaire récurrent)
Le mot « overlay » a deux sens, à deux granularités du **même axe 3** :
1. **overlay-qualificatif** : le préfixe NFCI léger (« sous conditions restrictives »).
2. **overlay-régime nommé** : Dollar Shortage (faisceau dollar + NFCI + spreads HY).
Toujours préciser lequel quand le mot apparaît, sinon on recrée la collision.

---

## 2. Méta-régimes cycliques : asymétrie assumée

Inflationniste et Désinflationniste sont des **méta-régimes cycliques** : ils regroupent les
colonnes de la grille (les 7 états s'y rangent). Ils gardent les codes G/I. Les 4 autres pages
Atlas (Dollar Shortage + les 3 structurels) ne sont PAS des états de grille → pas de codes G/I.
**Asymétrie 2 cycliques / 4 hors-grille : assumée, pas masquée.** Le dashboard la matérialise
en 3 groupes, ne JAMAIS revenir à une liste plate « 6 régimes ».

Mapping colonne → états (couche 1) :
- **Inflationniste** (I+) : Surchauffe (G+I+), Pression inflationniste (G=I+), Stagflation (G−I+).
- **Désinflationniste** (I−) : Désinflation expansive (G+I−), Contraction désinflationniste (G−I−), Ralentissement (G−I=).

---

## 3. Le crosswalk card → Atlas

La card live sort un **état cyclique** (couche 1). Le crosswalk nomme le **méta-régime de
destination** et y renvoie — **jamais « → Atlas » seul** (sinon l'utilisateur ne sait pas où
retomber). Déduit de `inflation_state` (déjà dans le JSON, zéro changement pipeline) :

- `I_plus`   → méta inflationniste   → `/atlas-regime-inflationniste/` (EN `/en/inflationary-macro-regime/`)
- `I_minus`  → méta désinflationniste → `/atlas-regime-desinflationniste/` (EN `/en/disinflationary-macro-regime/`)
- `I_neutral`→ pas de méta net → renvoi dashboard général `/regime-aujourdhui/` (EN `/en/current-regime/`)

**Règle d'affichage du crosswalk selon le mode du shortcode :**
- `card`, `full` → crosswalk **AFFICHÉ** (la page n'a pas l'Atlas en dessous : utile).
- `terminal` → crosswalk **MASQUÉ** (les dashboards affichent déjà l'Atlas plus bas : lien
  circulaire). Implémenté via le 4e param `$show_crosswalk` de `eco3min_regime_card()`, passé
  à `false` dans le case `terminal`. Même logique que `$show_full_link`.

Note : en I= (état neutre, fréquent), le crosswalk est volontairement tiède (renvoi général).
Normal — I= est un entre-deux sans méta-régime cyclique net.

---

## 4. Le snippet [eco3min_regime] (Code Snippets PHP, mode Functions)

Modes : `card` (défaut) · `badge` · `full` (card + tableau indicateurs) · `terminal`
(card + panneau 14 indicateurs zonés). Param `lang` auto-détecté via Polylang. Param
`full_link` (yes/no) override le CTA.

Fonctions clés : `eco3min_regime_load_data()` (lit `wp-content/uploads/eco3min-data/regime_current.json`),
`eco3min_regime_strings($lang)` (i18n FR/EN, contient les strings `cw_*` du crosswalk),
`eco3min_regime_crosswalk($data,$lang)`, `eco3min_regime_card($data,$lang,$show_full_link,$show_crosswalk)`,
`eco3min_regime_terminal()`, `eco3min_regime_inputs_table()`.

**Invariants à ne pas casser :**
- Couleurs régime pilotées par `--regime-zone/-line/-label` (du JSON).
- AMF : zones terminal jamais vert/rouge (`zone-calm/-tension/-stress/-na`), flèches tendance
  monochromes (▲▼▬ sans valence couleur).
- CTA `full_link` JAMAIS en terminal/badge. Crosswalk JAMAIS en terminal.
- Validation syntaxe : fichier Code Snippets = fragment sans `<?php` ouvrant. Pour `php -l`,
  préfixer `<?php` temporairement, sinon faux « unmatched } ».

**Champs JSON consommés** : `regime_name_FR/EN`, `growth_state`, `inflation_state`,
`stress_overlay`, `global_sync`, `global_qualifiers`, `headline_underlying_divergence`,
`input_values.{pce_trimmed_12m, brent_yoy_pct, ...}`, `color_*_hex`, `data_as_of`,
`thresholds_version`, `terminal[]`. (Source = pipeline, voir skill pipeline-eco3min.)

---

## 5. Les pages

### Dashboard (`/regime-aujourdhui/`, `/en/current-regime/`)
- Appelle `[eco3min_regime mode="terminal"]`.
- Section Atlas = **3 couches** (jamais liste plate). Titre « trois couches », pas « six régimes ».
- Codes G/I : sur les 2 tuiles cycliques uniquement. Couches 2-3 : marqueurs structurels, pas de G/I.
- Statut de preuve VISIBLE : couches 1-2 « ● calculé en temps réel », couche 3 « ○ cadre de
  long terme · non calculé mensuellement » + tuiles en pointillés (`--frame`).
- Classes : `dash-layer`, `dash-layer__num/title/status/desc`, `dash-atlas--two`, `dash-atlas__item--frame`.

### Méthodo (`/methodologie-classification-regime-macro/` + EN)
- Décrit la **couche 1** (grille 7 régimes) en détail. Appelle `[eco3min_regime mode="full"]`.
- DOIT contenir le bloc « Axes et couches » (id `meth-couches`) qui réconcilie les 2 grilles de
  lecture : axes = entrées du calcul, couches = nature des objets. « Les axes sont les
  ingrédients, les couches sont les plats. »
- L'axe 3 est nommé « Conditions financières (overlay-qualificatif) » et explicite son double sens.
- Limite explicite : couche 3 non calculée (honnêteté épistémique).

### Pages Atlas (12 = 6 régimes × FR/EN)
- Design system `eco3-atlas` (voir pilier-kit / production normalisée). 10 sections type.
- Slugs FR racine : `/atlas-regime-{inflationniste|desinflationniste|dollar-shortage|dominance-fiscale|repression-financiere|stagnation-seculaire}/`
- Slugs EN : `/en/{inflationary|disinflationary|dollar-shortage|fiscal-dominance|financial-repression|secular-stagnation}-macro-regime/`
- Couleurs régime figées (zéro régression) : Inflationniste #C73E2E/#F4DDD8/#8B2A1F · Désinflationniste #4A6B8A/#D8E2EC/#2D4256 · Dollar Shortage #7A6A65/#E8E0DC/#4A3A35 · Dominance fiscale #B8854A/#ECE2D2/#6E4E2B · Répression #2D4A6A/#C8D6E4/#1A2E42 · Stagnation #5A7A8A/#DCE8EC/#2E4A56.
- Maillage inter-Atlas : chaque page liste les 5 autres régimes.
- **Pas de H1 dans le HTML** (le template WP le fournit — éviter double H1).
- **Pas de disclaimer de pied en dur** (hook global bilingue le fournit — voir editeur-eco3min).
  Les encarts « Note AMF » inline avant les tableaux d'actifs RESTENT.
- Fix contraste bloc définition (override anti-Blocksy `!important` sur `.eco3-atlas
  .atlas-definition .atlas-definition__label/__text`, injecté avant `</style>`).

---

## 6. Pages-cibles à NE JAMAIS auto-mailler
- `16813` = `/en/current-regime/` (page dashboard EN elle-même)
- `16761` = `/atlas-regime-repression-financiere/` (page Atlas FR elle-même)
- `16777` = `/en/financial-repression-macro-regime/` (page Atlas EN elle-même)
Vérifier le slug avant tout maillage automatique vers une page régime (risque de lien vers soi).

---

## 7. Conformité AMF (rappel, voir editeur-eco3min pour le détail)
La card et les pages sont descriptives, jamais prescriptives. Le bloc divergence
(`headline_underlying_divergence`) est déjà AMF-safe (« dépasse », « mesurée par » — pas de
« devrait », pas de signal achat/vente). Toute évolution doit le rester.

---

## 8. Pièges connus (appris en production)
1. **Axes ≠ couches.** Ne jamais empiler un 3e vocabulaire. Les deux découpages sont légitimes
   et décrivent deux choses différentes — les nommer comme tels, ne pas en écraser un.
2. **Liste plate « 6 régimes »** = la collision d'origine. Toujours 3 groupes sur le dashboard.
3. **Codes G/I sur tuiles overlay/structurelles** = collision n°2. G/I réservés à la couche 1.
4. **Crosswalk « → Atlas » seul** = reproduit le trou. Toujours nommer le méta-régime de destination.
5. **Crosswalk en terminal** = lien circulaire (Atlas déjà affiché). Le masquer en terminal.
6. **Présenter la couche 3 comme calculée** = sur-vente du moteur, casse la crédibilité.

7. **Deux séries, pas une.** Le classificateur **live**
   (`regime_current.json`, rendu par la card et les dashboards) et le **lookup
   mensuel** (`regime_lookup.json`, entrée `months["{AAAA-MM}"]`) ne disent pas
   toujours la même chose. La carte de juin 2026 annonçait un basculement du
   live que le lookup mensuel ne montre pas.

   Conséquences, toutes payées en production :
   - **Citer la série qu'on affiche.** Un contenu qui pointe vers le dashboard
     recopie ses descripteurs **mot pour mot** depuis la page live, pas depuis le
     lookup. Le contenu et la page doivent dire la même chose.
   - **Ne jamais avancer une durée** (« inchangé depuis X ») sans l'avoir
     vérifiée **sur la série effectivement citée**.
   - Pour un **mois archivé**, c'est le **lookup qui fait foi** — le live affiche
     le régime du jour, pas celui du mois.

8. **Il n'existe aucun historique de `regime_current.json`.** Une fois le mois
   écoulé, l'instantané temps réel n'est plus récupérable : `regime_lookup.json`
   est la seule source de repli. Corollaire : un shortcode `[eco3min_regime]`
   laissé sur une page d'archive **réécrit l'histoire de la page** à chaque mise
   à jour du classificateur. Sur une archive, il se remplace par du HTML statique
   daté.

**Secrets GitHub** : `FRED_API_KEY`, `FTP_USER`, `FTP_HOST`, `FTP_PASSWORD`,
`WP_TOUCH_SECRET`.

**Remote SFTP OVH** : `/home/ecominl/www/wp-content/uploads/eco3min-data/`

**Touch WP** : `POST data={"key": secret}` (form-encoded, pas JSON).
Endpoint : `https://eco3min.fr/wp-json/eco3min/v1/touch-datasets`

**FRED** : pas de proxy PHP — appel direct via `fredapi.Fred(api_key)` (même
pattern que `eco3min_updater.py`). `FredFetcher` dans `eco3min_common.py` est
la source unique.

**HY OAS** : `bamlh0a0hym2_history.csv` — historique pré-2023 perdu (pipeline
a écrasé l'archive après la truncation FRED avril 2026). Seule fenêtre disponible :
2023-05 → 2026-05. `hy_oas_bps: null` avant mai 2023 dans le CSV. NFCI seul
en overlay primaire, définitivement.

---

## 12. Fixture de test live — régime mai 2026

Le cas mai 2026 est la meilleure fixture pour valider le shortcode, car il active
le bloc divergence (cas rare) :

```json
{
  "regime_code": 8,
  "growth_state": "G_neutral",
  "inflation_state": "I_neutral",
  "stress_overlay": "accommodating",
  "headline_underlying_divergence": true,
  "input_values": {
    "cfnai_ma3": -0.03,
    "pce_trimmed_12m": 2.36,
    "nfci": -0.515,
    "brent_yoy_pct": 72.2,
    "vixcls": 22.1
  },
  "data_as_of": "2026-03-01",
  "data_freshness": "lagged"
}
```

Ce cas teste simultanément : overlay accommodating, mode Transition (I_neutral → pas
de méta-régime cyclique net → crosswalk renvoie vers dashboard général), bloc divergence
affiché (I_neutral + Brent +72%), données laggées. En I_neutral, le crosswalk suit
la règle §3 : renvoi `/regime-aujourdhui/` (pas de méta cyclique net).

---

## 13. Résultats backtest épisodes clés (2003-2026)

| Épisode | Régime classifié | Overlay | Note |
|---------|-----------------|---------|------|
| GFC déc 2008 | Slowdown (G− I=) | Acute stress (oct 2008+) | PCE reste ≥1,86% → jamais I− |
| COVID avr 2020 | Slowdown (G− I=) | **Neutral** | Gate Sahm déclenche G−. NFCI +0,25 ≠ Acute |
| 2021 Reflation déc | Overheating (G+ I+) | Accommodating | PCE franchit 2,75% en déc 2021 |
| 2022 juin | Inflationary Pressure (G= I+) | **Neutral** | CFNAI-MA3 −0,22 : jamais G−. NFCI jamais Restrictive |
| 2023-2024 | Inflationary Pressure (G= I+) décroissante | Neutral | PCE reste >2,75% jusqu'à mi-2025 |
| Mai 2026 | Transition (G= I=) | Accommodating | PCE 2,36% → I_neutral. Divergence true |

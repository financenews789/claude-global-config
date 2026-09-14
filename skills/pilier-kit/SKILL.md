---
name: pilier-kit
description: Application du kit visuel Eco3min (blocs CSS-only .eco3-* injectes par un snippet PHP) aux pages PILIERS et SOUS-PILIERS, FR/EN. Activer pour toute mise a niveau visuelle d'une page pilier ou sous-pilier : la rendre scannable et sobre (FT/Bloomberg) sans toucher au CSS global ni a Blocksy, sans JS dans le contenu, en gardant tous les liens, le hero, l'absence de H1 et les ancres [lwptoc]. Couvre le contrat de classes (chapter, statrow, dichotomy, forces, ladder, level-tag, switch CSS-pur), la DOCTRINE diagnostic-avant-application (ne jamais plaquer : choisir les blocs ayant un ancrage reel ; pas de chapter sans regimes ; main legere sur page dense ; le ladder est un dispositif de PILIER, un sous-pilier veut un fil parent + cluster, voire un nouveau eco3-cluster-nav), la methode Python anti-erreur (verbatim, assert count==1, verif liens/hero/ids/H1), les 6 regles AMF, le deploiement Code Snippets + Gutenberg. Combiner avec archi-eco3min, editeur-eco3min, brand-kit-eco3min, formats-eco3min.
---

# Pilier Kit — mise à niveau visuelle des pages piliers & sous-piliers

Kit de blocs visuels **CSS-only** (classes `.eco3-*`) qui donne aux pages piliers/sous-piliers
d'eco3min.fr une allure FT/Bloomberg sobre tout en les rendant scannables. Le CSS est injecté par
**un seul snippet PHP** (Code Snippets) ; les blocs sont des `<!-- wp:html -->` collés dans le
contenu Gutenberg. État courant : **snippet v1.3** (7 composants).

## Contraintes dures (modèle de sécurité — non négociable)
1. **Jamais** supprimer un `href` existant ; **ajouter** est autorisé. Contrôle = *sous-ensemble* (tous les liens d'origine ⊆ sortie ; nouveaux liens OK). Vérifié programmatiquement.
2. **Aucun `<h1>`** ajouté (WordPress fournit le titre).
3. Garder l'**image hero** existante telle quelle.
4. **Zéro JS** dans le contenu — interactivité = CSS pur (`:checked`, `:hover`, `<details>`).
5. Snippet = **CSS `.eco3-*` uniquement** : aucun sélecteur d'élément nu, aucune touche au global/Blocksy ; `!important` sur les propriétés critiques.
6. `<h2 id>` réels conservés (TOC `[lwptoc]` + ancres survivent).

## Déploiement
- **Snippet** : Code Snippets → PHP → « Run everywhere », collé **sans** `<?php`. Activé une fois,
  réutilisé partout. Nouveau composant → on **étend** le snippet (additif), re-collage unique, puis il refige.
- **Pages** : page entière retournée en **markup de blocs Gutenberg**, FR + EN, collée dans l'Éditeur de code.

## DOCTRINE — diagnostic avant application (cœur du skill)
Ne jamais plaquer le kit. Par page :
1. Exiger le markup Gutenberg **FR + EN** ; ne jamais inventer slug / hero / lien / ancre.
2. Choisir les blocs qui ont un **ancrage réel** dans CE contenu (varie par page) :
   - `chapter` seulement si vraie structure régimes/chronologie — sinon **refuser** (placage).
   - `dichotomy` si opposition conceptuelle récurrente (nominal/réel, physique/financier, ancien/nouveau régime).
   - `statrow` si chiffres-clés pédagogiques (1 seul `--accent`).
   - `forces` pour remplacer une liste de 3–5 points structurés — **liens préservés dans les cartes**.
   - `switch` si concept **conditionnel au régime** qui gagne à être joué.
   - `level-tag` : composant **conservé dans le kit mais NON posé sur les pages** — aucune pastille de niveau visible. Le niveau de lecture est implicite et la méta `_eco3min_level` porte déjà le signal de classification. À n'émettre dans le markup que sur demande explicite.
3. **`ladder` = dispositif de PILIER**, pas de sous-pilier. Sous-pilier → fil vers pilier parent + articles
   du cluster (MAJEUR + satellites) ; proposer, ne pas présumer. Pattern récurrent → créer un composant
   `eco3-cluster-nav` (étendre le snippet) plutôt que bricoler.
4. Page dense en encarts → **main légère** (moins de blocs, espacés).
5. Présenter le diagnostic AVANT de produire (sauf consigne « fais tout toi-même »).

## Méthode de transformation (Python, anti-erreur)
1. Écrire le markup FR + EN **verbatim** sur disque.
2. `insert_after(text, ancre, bloc)` avec assert `count == 1` ; remplacements via regex `re.S` (assert un seul match).
   Pièges EN : guillemets/apostrophes courbes « “ ” ’ », markup parfois sur une seule ligne.
3. Vérifier AVANT livraison : `0` `<h1`, tous les `href` d'origine en sous-ensemble, hero présent,
   `[lwptoc]` présent, toutes les ancres `id` conservées, blocs présents, exactement `1` `--accent` par
   `statrow`, pas de `chapter` si « pas de régimes », blocs « tu ne touches pas » intacts.
4. `present_files` ; si le snippet a changé, le livrer + prévenir explicitement.

## AMF — 6 règles (descriptif, jamais prescriptif)
Pas d'allocation %/ratios ; pas de « devrait/should » par type d'investisseur ; pas de « achetez X quand Y » ;
pas de FAQ binaires ; comparaisons géo = observation statistique ; recommandations = observation empirique
avec ancrage temporel. `switch` = observation empirique, `cluster-nav`/`level-tag` = navigation, `dichotomy` = pédagogie.

## Latitude créative
Interaction CSS-pure tasteful autorisée quand elle *enseigne* (cf. `switch` régime). Impératifs : sobre,
`.eco3-*`, dégradation gracieuse (CSS absent → contenu lisible), **id-agnostique** (cibler l'ordre via
`:first-of-type`/`:nth-of-type`, jamais un id codé en dur — FR et EN partagent le CSS).

## Catalogue des blocs (squelettes HTML)
Conventions : **cool** = bleu (bénin/passé/nominal), **warm** = rouge/terra (tension/présent/réel).
Les squelettes exacts des 7 blocs (chapter `--cool/--neutral/--warm`, statrow/stat `--accent`,
dichotomy `__side--cool/--warm` + `__arrow` + `__verdict`, forces `__link`, ladder PILIER 3 niveaux,
level-tag `--deb/--inter/--adv`, switch radios-first id-agnostique `--low/--high` + `--pos/--neg`)
sont reproduits dans le prompt de passation `eco3-souspiliers-handoff-prompt.md` et reflètent à la
lettre les classes du snippet ci-dessous.

## Snippet kit v1.3 (référence canonique — contrat de classes complet)
Fichier de travail : `eco3-kit-snippet.php`. Coller dans Code Snippets sans le `<?php`.

```php
<?php
/**
 * Eco3min — Pillar Kit (CSS) v1.3
 * --------------------------------------------------------------------------
 * A coller dans Code Snippets (PHP, "Run everywhere"), puis activer.
 *
 * ROLE : ce snippet ajoute UNIQUEMENT le CSS des nouveaux blocs .eco3-*
 *        (chapter / statrow / stat / dichotomy / forces / ladder /
 *        level-tag / switch) utilises dans les pages piliers.
 *        Il ne touche PAS au CSS global du site :
 *        tous les selecteurs sont prefixes .eco3-, aucun selecteur
 *        d'element nu, le H2 des chapters garde la typo du theme.
 *
 * AUCUN script (pas de JS). Charge via enqueue_block_assets => le style
 * s'applique aussi dans l'editeur Gutenberg (apercu des blocs correct).
 *
 * Si un jour tu ajoutes un script, c'est ici (wp_enqueue_script).
 * --------------------------------------------------------------------------
 */

if ( ! defined( 'ABSPATH' ) ) { return; }

if ( ! function_exists( 'eco3_kit_css' ) ) :

add_action( 'enqueue_block_assets', 'eco3_kit_css' );
function eco3_kit_css() {
	$css = <<<'ECO3CSS'
:root{
  --e3-navy:#1a237e; --e3-ink:#0f204b; --e3-charcoal:#1a1a1a;
  --e3-gray:#5b6472; --e3-line:#dcdfe6; --e3-line-soft:#e9ebf0;
  --e3-cream:#f8f5ee; --e3-paper:#fcfbf6; --e3-gold:#c9a84c; --e3-terra:#b85c3c;
  --e3-pos:#2f7a4f;
  --e3-cool-zone:#d8e2ec; --e3-cool-line:#4a6b8a; --e3-cool-ink:#2d4256;
  --e3-warm-zone:#f4ddd8; --e3-warm-line:#c73e2e; --e3-warm-ink:#8b2a1f;
  --e3-serif:"Libre Baskerville",Georgia,"Times New Roman",serif;
  --e3-sans:"DM Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  --e3-mono:"JetBrains Mono","SF Mono",Consolas,monospace;
}

/* shared atoms */
.eco3-kicker{font-family:var(--e3-mono);font-size:10px;font-weight:500;
  letter-spacing:.18em;text-transform:uppercase;color:var(--e3-gray);}
.eco3-rule{height:2px;width:46px;background:var(--e3-gold);border:0;margin:0;}

/* ---------------------------------------------------------- 1. CHAPTER */
.eco3-chapter{margin:64px 0 18px;padding:0;}
.eco3-chapter__top{display:flex;align-items:baseline;gap:14px;margin-bottom:10px;}
.eco3-chapter__num{font-family:var(--e3-serif);font-weight:700;font-size:15px;
  line-height:1;color:var(--e3-terra);letter-spacing:.02em;}
.eco3-chapter__tag{font-family:var(--e3-mono);font-size:10px;font-weight:500;
  letter-spacing:.18em;text-transform:uppercase;color:var(--e3-gray);
  border-top:2px solid var(--e3-line);padding-top:8px;flex:1;}
.eco3-chapter__title{margin:6px 0 10px!important;}  /* on garde la typo h2 du thème */
.eco3-chapter__lead{font-family:var(--e3-serif);font-style:italic;color:var(--e3-gray);
  font-size:1.04rem;line-height:1.55;margin:0;max-width:60ch;}
.eco3-chapter--warm .eco3-chapter__num{color:var(--e3-warm-line);}
.eco3-chapter--warm .eco3-chapter__tag{border-top-color:var(--e3-warm-zone);}
.eco3-chapter--cool .eco3-chapter__num{color:var(--e3-cool-line);}
.eco3-chapter--cool .eco3-chapter__tag{border-top-color:var(--e3-cool-zone);}

/* --------------------------------------------------------- 2. STAT ROW */
.eco3-statrow{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));
  gap:0;margin:34px 0;border:1px solid var(--e3-line);background:var(--e3-paper);}
.eco3-statrow .eco3-stat{border:0;border-right:1px solid var(--e3-line);margin:0;background:transparent;}
.eco3-statrow .eco3-stat:last-child{border-right:0;}
.eco3-stat{margin:28px 0;padding:20px 22px;background:var(--e3-paper);
  border:1px solid var(--e3-line);border-top:2px solid var(--e3-line);
  position:relative;transition:border-color .2s ease,transform .2s ease;}
.eco3-stat__value{font-family:var(--e3-serif);font-weight:700;color:var(--e3-ink);
  font-size:2.35rem;line-height:1;letter-spacing:-.02em;font-variant-numeric:tabular-nums;}
.eco3-stat__label{display:block;font-family:var(--e3-sans);font-size:.86rem;
  line-height:1.4;color:var(--e3-charcoal);margin-top:11px;}
.eco3-stat__note{display:block;font-family:var(--e3-mono);font-size:9.5px;
  letter-spacing:.04em;color:var(--e3-gray);margin-top:9px;}
.eco3-stat--accent{border-top-color:var(--e3-terra);}
.eco3-statrow .eco3-stat--accent{box-shadow:inset 0 2px 0 0 var(--e3-terra);}
.eco3-stat:hover{border-top-color:var(--e3-navy);}

/* -------------------------------------------------------- 3. DICHOTOMY */
.eco3-dicho{margin:46px 0;}
.eco3-dicho__grid{display:grid;grid-template-columns:1fr auto 1fr;
  align-items:stretch;gap:0;}
.eco3-dicho__side{padding:24px 26px;border:1px solid var(--e3-line);
  transition:transform .2s ease,box-shadow .2s ease;}
.eco3-dicho__side:hover{transform:translateY(-2px);
  box-shadow:0 6px 22px -14px rgba(15,32,75,.4);}
.eco3-dicho__side--cool{background:var(--e3-cool-zone);border-color:#c4d3e2;}
.eco3-dicho__side--warm{background:var(--e3-warm-zone);border-color:#eccabf;}
.eco3-dicho__kicker{font-family:var(--e3-mono);font-size:10px;font-weight:500;
  letter-spacing:.16em;text-transform:uppercase;}
.eco3-dicho__side--cool .eco3-dicho__kicker{color:var(--e3-cool-line);}
.eco3-dicho__side--warm .eco3-dicho__kicker{color:var(--e3-warm-line);}
.eco3-dicho__title{font-family:var(--e3-serif);font-weight:700;font-size:1.18rem;
  line-height:1.25;margin:9px 0 12px;}
.eco3-dicho__side--cool .eco3-dicho__title{color:var(--e3-cool-ink);}
.eco3-dicho__side--warm .eco3-dicho__title{color:var(--e3-warm-ink);}
.eco3-dicho__body{font-family:var(--e3-sans);font-size:.95rem;line-height:1.62;
  color:#2b3340;}
.eco3-dicho__body p{margin:0 0 .5em;}
.eco3-dicho__body ul{margin:.2em 0 0;padding-left:1.05em;}
.eco3-dicho__body li{margin:.32em 0;}
.eco3-dicho__arrow{display:flex;align-items:center;justify-content:center;
  width:54px;font-family:var(--e3-serif);font-size:1.5rem;color:var(--e3-gray);
  user-select:none;}
.eco3-dicho__verdict{margin-top:0;border:1px solid var(--e3-line);border-top:0;
  border-left:3px solid var(--e3-terra);background:var(--e3-cream);
  padding:18px 24px;font-family:var(--e3-serif);font-style:italic;
  font-size:1.06rem;line-height:1.55;color:var(--e3-ink);}
.eco3-dicho__verdict strong{font-style:normal;}

/* ----------------------------------------------------------- 4. FORCES */
.eco3-forces{margin:46px 0;}
.eco3-forces__head{margin-bottom:20px;}
.eco3-forces__title{font-family:var(--e3-serif)!important;color:var(--e3-ink)!important;
  font-weight:700;font-size:1.38rem;line-height:1.2;margin:8px 0 8px;}
.eco3-forces__intro{font-family:var(--e3-sans);color:var(--e3-gray);
  font-size:.96rem;line-height:1.6;margin:0;max-width:64ch;}
.eco3-forces__grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
  gap:18px;}
.eco3-force{padding:22px 22px 20px;background:var(--e3-paper);
  border:1px solid var(--e3-line);position:relative;
  transition:transform .2s ease,box-shadow .2s ease,border-color .2s ease;}
.eco3-force:hover{transform:translateY(-2px);border-color:var(--e3-gold);
  box-shadow:0 8px 24px -16px rgba(15,32,75,.45);}
.eco3-force__n{font-family:var(--e3-mono);font-size:11px;font-weight:500;
  letter-spacing:.12em;color:var(--e3-gold);}
.eco3-force__title{font-family:var(--e3-serif);font-weight:700;font-size:1.07rem;
  line-height:1.28;color:var(--e3-ink);margin:8px 0 10px;}
.eco3-force__body{font-family:var(--e3-sans);font-size:.92rem;line-height:1.58;
  color:#2b3340;margin:0;}
.eco3-force__link{display:inline-block;margin-top:13px;font-family:var(--e3-mono);
  font-size:10.5px;letter-spacing:.04em;text-transform:uppercase;font-weight:500;
  color:var(--e3-navy)!important;text-decoration:none;
  border-bottom:1px solid var(--e3-line);padding-bottom:2px;transition:border-color .2s;}
.eco3-force__link:hover{border-bottom-color:var(--e3-gold);}

/* ------------------------------------------------------- 5. LADDER (niveaux) */
.eco3-ladder{margin:30px 0 42px;}
.eco3-ladder__head{margin-bottom:16px;}
.eco3-ladder__title{font-family:var(--e3-serif);font-weight:700;font-size:1.16rem;
  color:var(--e3-ink);line-height:1.25;margin:7px 0 0;}
.eco3-ladder__track{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;align-items:stretch;}
.eco3-ladder__step{display:flex;flex-direction:column;gap:7px;text-decoration:none!important;
  padding:18px 18px 16px;background:var(--e3-paper);border:1px solid var(--e3-line);
  border-top:3px solid var(--e3-line);position:relative;color:inherit;
  transition:transform .2s ease,box-shadow .2s ease,border-color .2s ease;}
a.eco3-ladder__step:hover{transform:translateY(-3px);border-color:var(--e3-gold);
  box-shadow:0 10px 30px -18px rgba(15,32,75,.5);}
.eco3-ladder__lvl{font-family:var(--e3-mono);font-size:10px;font-weight:500;
  letter-spacing:.16em;text-transform:uppercase;color:var(--e3-gray);}
.eco3-ladder__name{font-family:var(--e3-serif);font-weight:700;font-size:1.1rem;
  color:var(--e3-ink);line-height:1.2;}
.eco3-ladder__desc{font-family:var(--e3-sans);font-size:.85rem;line-height:1.5;
  color:#3a4452;flex:1;}
.eco3-ladder__go{font-family:var(--e3-mono);font-size:10px;font-weight:500;
  letter-spacing:.06em;text-transform:uppercase;color:var(--e3-navy);margin-top:3px;}
.eco3-ladder__hereTag{align-self:flex-start;margin-top:3px;font-family:var(--e3-mono);
  font-size:10px;letter-spacing:.1em;text-transform:uppercase;font-weight:600;color:#fff;
  background:var(--e3-terra);padding:4px 11px;border-radius:2px;}
.eco3-ladder__step--deb{border-top-color:var(--e3-cool-line);}
.eco3-ladder__step--deb .eco3-ladder__lvl,
.eco3-ladder__step--deb .eco3-ladder__go{color:var(--e3-cool-line);}
.eco3-ladder__step--adv{border-top-color:var(--e3-navy);}
.eco3-ladder__step--adv .eco3-ladder__lvl,
.eco3-ladder__step--adv .eco3-ladder__go{color:var(--e3-navy);}
.eco3-ladder__step--here{border-top-color:var(--e3-terra);background:var(--e3-cream);}
.eco3-ladder__step--here .eco3-ladder__lvl{color:var(--e3-terra);}

/* ----------------------------------------------------------- 6. LEVEL TAG */
.eco3-level-tag{display:inline-flex;align-items:center;gap:7px;font-family:var(--e3-mono);
  font-size:10px;font-weight:500;letter-spacing:.14em;text-transform:uppercase;
  padding:5px 11px;border:1px solid var(--e3-line);border-radius:2px;background:#fff;
  color:var(--e3-gray);margin:6px 0;}
.eco3-level-tag::before{content:"";width:7px;height:7px;border-radius:50%;
  background:var(--e3-gray);flex:none;}
.eco3-level-tag--deb{color:var(--e3-cool-line);border-color:var(--e3-cool-zone);}
.eco3-level-tag--deb::before{background:var(--e3-cool-line);}
.eco3-level-tag--inter{color:var(--e3-terra);border-color:#eccabf;}
.eco3-level-tag--inter::before{background:var(--e3-terra);}
.eco3-level-tag--adv{color:var(--e3-navy);border-color:#c7cbe0;}
.eco3-level-tag--adv::before{background:var(--e3-navy);}

/* --------------------------------------------- 7. SWITCH (regime, CSS pur) */
.eco3-switch{margin:38px 0;border:1px solid var(--e3-line);background:var(--e3-paper);position:relative;}
.eco3-switch__radio{position:absolute;opacity:0;width:0;height:0;pointer-events:none;}
.eco3-switch__head{padding:20px 24px 0;}
.eco3-switch__q{font-family:var(--e3-serif);font-weight:700;font-size:1.18rem;
  color:var(--e3-ink);margin:0 0 4px;line-height:1.25;}
.eco3-switch__sub{font-family:var(--e3-mono);font-size:10px;font-weight:500;
  letter-spacing:.12em;text-transform:uppercase;color:var(--e3-gray);}
.eco3-switch__tabs{display:flex;flex-wrap:wrap;gap:8px;padding:16px 24px 0;}
.eco3-switch__tab{cursor:pointer;font-family:var(--e3-mono);font-size:11px;font-weight:500;
  letter-spacing:.08em;text-transform:uppercase;color:var(--e3-gray);background:#fff;
  border:1px solid var(--e3-line);padding:9px 16px;user-select:none;
  transition:border-color .15s ease,color .15s ease,background .15s ease;}
.eco3-switch__tab:hover{border-color:var(--e3-navy);color:var(--e3-ink);}
.eco3-switch__panels{padding:18px 24px 6px;}
.eco3-switch__panel{display:none;}
.eco3-switch__line{display:block;font-family:var(--e3-mono);font-size:10px;
  letter-spacing:.06em;text-transform:uppercase;color:var(--e3-gray);margin-bottom:8px;}
.eco3-switch__big{display:block;font-family:var(--e3-serif);font-weight:700;
  font-size:2rem;line-height:1.05;letter-spacing:-.01em;font-variant-numeric:tabular-nums;}
.eco3-switch__big--pos{color:var(--e3-pos);}
.eco3-switch__big--neg{color:var(--e3-warm-line);}
.eco3-switch__verdict{display:block;font-family:var(--e3-sans);font-size:.95rem;
  line-height:1.55;color:#2b3340;margin-top:10px;max-width:60ch;}
.eco3-switch__foot{margin:14px 0 0;padding:14px 24px 20px;font-family:var(--e3-serif);
  font-style:italic;font-size:.95rem;color:var(--e3-gray);border-top:1px solid var(--e3-line-soft);}
/* etat actif independant des IDs : on cible l'ordre des radios */
.eco3-switch__radio:first-of-type:checked ~ .eco3-switch__panels .eco3-switch__panel--low{display:block!important;}
.eco3-switch__radio:nth-of-type(2):checked ~ .eco3-switch__panels .eco3-switch__panel--high{display:block!important;}
.eco3-switch__radio:first-of-type:checked ~ .eco3-switch__tabs .eco3-switch__tab--low,
.eco3-switch__radio:nth-of-type(2):checked ~ .eco3-switch__tabs .eco3-switch__tab--high{
  background:var(--e3-navy);color:#fff;border-color:var(--e3-navy);}

/* ----------------------------------------------------------- responsive */
@media (max-width:680px){
  .eco3-statrow{grid-template-columns:1fr;}
  .eco3-statrow .eco3-stat{border-right:0;border-bottom:1px solid var(--e3-line);}
  .eco3-statrow .eco3-stat:last-child{border-bottom:0;}
  .eco3-dicho__grid{grid-template-columns:1fr;}
  .eco3-dicho__arrow{width:auto;padding:8px 0;transform:rotate(90deg);}
  .eco3-ladder__track{grid-template-columns:1fr;}
}
@media (prefers-reduced-motion:reduce){
  .eco3-stat,.eco3-dicho__side,.eco3-force,.eco3-ladder__step,.eco3-switch__tab{transition:none;}
}
ECO3CSS;
	wp_register_style( 'eco3-kit', false );
	wp_enqueue_style( 'eco3-kit' );
	wp_add_inline_style( 'eco3-kit', $css );
}

endif;
```

## Journal de version
- **v1.0–v1.2** : chapter, statrow/stat, dichotomy, forces (+`__link`). Validé sur 6 piliers analytiques.
- **v1.3** : ajout `ladder` (boussole 3 niveaux, PILIER), `level-tag` (`--deb/--inter/--adv`),
  `switch` (régime CSS-pur, id-agnostique via ordre des radios, dégradation gracieuse), token `--e3-pos`.
  Introduit sur le pilier Éducation financière (qui a refusé `chapter` faute de régimes — exemple canonique
  de la doctrine diagnostic-avant-application).
- **À venir (sous-piliers)** : candidat `eco3-cluster-nav` (fil pilier parent + MAJEUR + satellites) si le
  besoin se confirme sur ≥2 sous-piliers.
- **Rév. doc — level-tag OFF page** : le `level-tag` n'est plus posé sur les pages (ni piliers ni sous-piliers).
  Le CSS `.eco3-level-tag*` reste dans le snippet (toujours **v1.3**, aucun re-collage requis) ; le composant
  existe « si besoin » mais n'est plus émis dans le markup par défaut. Le niveau reste porté par la méta
  `_eco3min_level`. À n'utiliser que sur demande explicite.

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

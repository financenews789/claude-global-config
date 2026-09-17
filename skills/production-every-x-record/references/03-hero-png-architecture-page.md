# production-every-x-record — référence : Hero PNG autoportant et architecture de page (§3, §4)

Extrait VERBATIM de SKILL.md (découpage du 17/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 3. Le hero PNG autoportant

- **PNG self-contained** : titre + sous-titre + **bande de 3-4 chiffres-clés** + sourcing 2 lignes mono + watermark, tout BAKÉ dans l'image. Objectif : l'image se suffit en partage hors-site (Reddit/X embed, FT). Format 1536×864 (livrer en ≥2x : 3072×1728).
- **Bande de chiffres-clés** en tête (ex. `9/9 · 0 · 0.57 · 0.13`) : crédibilise + rend l'image autoportante. **Zéro stat redondante dans la bande** : deux chiffres qui disent la même chose gaspillent un slot (cas réel : "1 escalating sequence" + "0 escalations since 1980" = la même information deux fois ; remplacer le doublon par une ancre distincte, ex. la valeur record "14.6% — unmatched since 1980").
- **PAS de tableau dans l'image si la donnée est mono-métrique** (Sahm = 1 métrique → courbe, pas tableau). Un tableau-dans-l'image n'a de sens que si la donnée est génuinement tabulaire (yield curve = 6 colonnes start/end/durée/trough/lag/récession). **Matcher le visuel à la nature de la donnée.**
- **Anti-doublon** : si le PNG est autoportant, le HTML autour est MINIMAL (dek éditorial + meta). Pas de `<figcaption>` qui répète le titre/source du PNG. Pas de titre HTML qui répète celui du PNG — **une seule couche dit le titre** (le PNG le garde, le H1 SEO est fourni par Blocksy).
- **Rendu : l'outil est libre (matplotlib, HTML→Playwright/Chromium, autre), le critère ne l'est pas** — tout élément chiffré tracé depuis le vrai CSV chargé dans la session ; layout vérifié (footer dans le cadre, rien de tronqué ni de chevauché) ; **screenshot rendu et INSPECTÉ avant livraison** ; l'aha doit se lire en vignette ~400px. La variante linguistique (hero FR) est rendue et inspectée séparément — les titres FR sont plus longs, prévoir taille/wording dédiés plutôt qu'une traduction qui tronque.

---

## 4. Architecture de page

- **Bloc HTML (markup + CSS uniquement, AUCUN `<script>`, AUCUN H1)** dans un bloc Custom HTML (pas l'éditeur classique → wpautop). Blocksy fournit le titre/H1.
- **CSS 100 % SCOPÉ (BLOQUANT)** : tout le markup vit dans UN wrapper à classe unique (ex. `.e3m-wave`) et **chaque sélecteur du `<style>` commence par ce wrapper**. **INTERDITS : `body{…}`, `*{…}`, `html{…}`, tout sélecteur d'élément nu (`p{}`, `a{}`, `table{}`)** — bug réel : un bloc qui stylait `body` et `*` fuyait sur le header/footer Blocksy de toute la page. Le reset box-sizing se fait en `.wrapper *{box-sizing:border-box}`. Vérification programmatique : extraire les sélecteurs du style et asserter qu'ils commencent tous par le wrapper (ou `@media`/`@import`).
- **Snippet PHP séparé** (Code Snippets, type PHP, "Run everywhere", **sans balise `<?php` de tête**), **guardé par slug** selon le motif canonique de `eco3min-import-contenu-bilingue` (`is_singular('page')` + `get_queried_object() instanceof WP_Post` + map par `post_name`, nom de snippet UNIQUE). Il porte :
  - **au `wp_head`** : le JSON-LD `@graph` (Article + Dataset + FAQPage) des DEUX langues, **encodé en base64 par slug** (jamais en clair/heredoc : l'échappement casse silencieusement à l'embarquement dans le bundle JSON — format aligné sur le skill import) ;
  - **au `wp_footer`**, guardé sur les MÊMES slugs : le **chart interactif dessiné main (canvas, AUCUNE lib)** — il injecte `window.<data>` + le JS et se monte sur un `<div id="…">` placeholder posé dans le bloc HTML. **Pas de shortcode nécessaire** : le bloc HTML reste sans script, et si le JS échoue le div vide est invisible (dégradation propre, le hero PNG couvre).
  - Rien d'autre. **Pas de click-to-copy** (banni §2.5).
- **Hook + TABLEAU du record above-the-fold, en HTML** (indexable — JAMAIS le record uniquement dans une image ; le HTML est ce que Google/les LLM citent).
  - **Pattern autorisé : barres de magnitude CSS pures dans le tableau** (span à largeur % inline, valeur/max ; lignes de l'anomalie en accent, contexte en gris, ligne "live" atténuée) — rend le finding visible dans le HTML indexable lui-même, sans script. Masquer la colonne sous ~480px si elle serre.
- **Chart interactif** : résout l'axe Y (readout au survol = valeur exacte même hors-échelle), ajoute le signal "high-effort OC" que Reddit récompense. **Les boutons jump remplacent un 2e chart comparatif** (cliquer "2008", "COVID" vs l'anomalie = comparaison dans le même chart). Plafonner à ~2 visuels (hero + interactif) ; au-delà = bascule "outil", perte du signal référence. Spécifications éprouvées :
  - readout mono au survol ET au touch (mobile) ; crosshair ; boutons de fenêtres (Full + 4-5 fenêtres calées sur les épisodes du registre) ;
  - labels des pics affichés au zoom **avec halo blanc** (`strokeText` épais sous le `fillText`) — bug réel attrapé au test mobile : label du point live croisant la courbe ;
  - **honnêteté des trous** : un mois manquant dans la source = `null` affiché "no data (…)" dans le readout, JAMAIS interpolé ni ponté ;
  - DPR-aware, responsive, i18n par slug (formats FR : virgule décimale + insécable) ;
  - **tester le WIDGET rendu dans un harnais navigateur (Playwright/Chromium), desktop + mobile + une vue zoomée, et INSPECTER les captures** avant livraison — même exigence que le hero.
- **Structure éditoriale** : Beat finding-first / mécanisme / steelman / "what it doesn't prove" (→ `production-research-study`).
- **CSV téléchargeable** = la conversion qui SERT le backlink (donnée libre = donnée citée). **Pas de capture email** sur une page backlink (clarté de mission ; la capture vit sur la page dataset). Bouton CSV SEUL dans la zone download (pas de bouton concurrent qui détourne) ; deux CSV liés au même dataset (série + registre) = OK, c'est toujours "CSV seul".
- **Maillage interne** vers le cluster : dans le corps + le bloc Related, PAS un bouton concurrent dans la zone download.
- **URLs des assets** (hero, CSV) : format `uploads/AAAA/MM/` avec année/mois EN COURS, base identique partout — règle et détail dans `eco3min-import-contenu-bilingue` (BLOQUANT là-bas, s'applique ici aussi).

---
name: hub-card-etude
description: >
  Ajout hebdomadaire de la carte d'une etude (paire FR + EN) en tete des deux hubs Eco3min : Macro Watch (EN, /en/macro-watch/) et Observatoire macro (FR, /observatoire-macro/). A activer quand Paul dit "ajoute la carte du cycle au hub" ou "mets a jour les hubs", apres production d'une etude. Couvre : nouvelle carte TOUJOURS en 1re position ; le PIEGE DU COMPTEUR (deux emplacements par hub, valeur = vrai nombre de cartes, jamais +1 aveugle, apprentissage du cycle SS) ; templates EN et FR verbatim ; slugs (EN sous /en/, FR plat) ; featured image (prefixe en/ cote EN, slug nu cote FR) ; asymetrie de lang-note (cartes EN avec lien FR, cartes FR sans) ; contrainte wpautop (.eco3-card__media sur UNE ligne) ; AMF ; coherence stricte des chiffres avec article/chart/audit ; methode Python anti-erreur (insertion + recomptage + bump compteur assertes) et checklist. Se combine avec production-chart-of-the-week, production-research-study, archi-eco3min, editeur-eco3min.
---

# Ajout d'une carte d'étude dans les hubs Macro Watch (EN) + Observatoire macro (FR)

Opération récurrente de fin de cycle. Une fois l'étude produite (chart + article + audit
levé), sa carte est ajoutée **en tête** des deux pages hub. Claude reçoit le HTML actuel
des deux hubs (collé par Paul, ou présent dans le projet), insère la carte, et **redonne
les deux pages complètes prêtes à coller** dans WordPress (mode Code). Paul ne modifie pas
le HTML lui-même : il colle ce que Claude produit.

---

## Les deux hubs

| | Hub EN | Hub FR |
|---|---|---|
| Nom | Macro Watch | Observatoire macro |
| Slug | `/en/macro-watch/` | `/observatoire-macro/` (plat, pas de `/fr/`) |
| Attribut racine | `data-eco3-hub="en"` | `data-eco3-hub="fr"` |
| Conteneur des cartes | `<div class="eco3-grid">` | idem |
| CTA carte | `Read the study` | `Lire l'étude` |
| Badge | `📄 Research study · {Month D, YYYY}` | `📄 Étude de recherche · {D mois YYYY}` |

---

## INVARIANT 1 — La nouvelle carte va TOUJOURS en première position

La carte du cycle s'insère **juste après `<div class="eco3-grid">`**, AVANT la carte
actuellement en tête. Le hub est anti-chronologique : le plus récent en haut. Ne jamais
ajouter en bas.

## INVARIANT 2 — Le compteur : DEUX emplacements par hub, valeur = VRAI nombre de cartes

**C'est le piège n°1 de cette opération** (révélé au cycle Social Security : l'ajout
Éolien+solaire avait incrémenté les cartes à 6 mais laissé les deux compteurs à 5).

Chaque hub affiche le nombre d'études à **deux endroits** :

```html
<!-- (1) bloc métriques -->
<span class="eco3-stat__value eco3-stat__value--accent">N</span>
<!-- (2) ligne de section -->
<p class="eco3-section__count">N studies · Updated every Tuesday</p>   <!-- EN -->
<p class="eco3-section__count">N études · Mise à jour chaque mardi</p>  <!-- FR -->
```

Règle ferme : **ne jamais faire « +1 » sur la valeur affichée.** Recompter le nombre réel
de blocs `<article class="eco3-card eco3-card--study"` dans le grid APRÈS insertion, et
poser ce nombre aux deux endroits, dans les deux hubs. Si le compteur affiché ne
correspondait pas au compte réel avant l'ajout, le corriger au vrai compte et **le signaler
explicitement à Paul** (« le compteur était à X mais il y avait Y cartes ; corrigé à Z »).

## INVARIANT 3 — Changelog + version

En tête de chaque fichier, dans le bloc commentaire, ajouter une entrée datée et bumper la
version `vX.Y` :

```
- 2026-06-02 v2.3 : ajout étude {sujet} (en tête). Compteur porté à {N}.
```

Si une correction de compteur a eu lieu, le noter dans l'entrée.

---

## Template de carte — EN (hub Macro Watch)

À coller en première position du grid. Remplacer les `{{...}}`.

```html
<!-- Study: {{Sujet EN}} ({{YYYY-MM-DD}}) — newest -->
<article class="eco3-card eco3-card--study" data-eco3-cat="{{cat}}" data-eco3-type="study">
  <a class="eco3-card__media" href="/en/{{slug-en}}/" aria-hidden="true" tabindex="-1">[eco3min_featured_image path="en/{{slug-en}}"]</a>
  <div class="eco3-card__badge eco3-card__badge--study">📄 Research study · {{Month D, YYYY}}</div>
  <h3 class="eco3-card__title">{{Titre EN — descriptif, inclut la plage de dates}}</h3>
  <p class="eco3-card__desc">{{Description EN, ~110–140 mots. Chiffres = ceux de l'audit. Descriptif, jamais prescriptif.}}</p>
  <p class="eco3-card__sources">Sources: {{source primaire}} · {{détail}} · Free CSV download</p>
  <p class="eco3-card__lang-note">🇫🇷 <a href="/{{slug-fr}}/">Version française disponible →</a></p>
  <div class="eco3-card__cta">
    <a class="eco3-btn eco3-btn--study" href="/en/{{slug-en}}/">Read the study</a>
  </div>
</article>
```

## Template de carte — FR (hub Observatoire macro)

```html
<!-- Étude : {{Sujet FR}} ({{YYYY-MM-DD}}) — la plus récente -->
<article class="eco3-card eco3-card--study" data-eco3-cat="{{cat}}" data-eco3-type="study">
  <a class="eco3-card__media" href="/{{slug-fr}}/" aria-hidden="true" tabindex="-1">[eco3min_featured_image path="{{slug-fr}}"]</a>
  <div class="eco3-card__badge eco3-card__badge--study">📄 Étude de recherche · {{D mois YYYY}}</div>
  <h3 class="eco3-card__title">{{Titre FR — descriptif, inclut la plage de dates}}</h3>
  <p class="eco3-card__desc">{{Description FR, ~110–140 mots. Mêmes chiffres que la carte EN. Descriptif.}}</p>
  <p class="eco3-card__sources">Sources : {{source primaire}} · {{détail}} · Téléchargement CSV gratuit</p>
  <div class="eco3-card__cta">
    <a class="eco3-btn eco3-btn--study" href="/{{slug-fr}}/">Lire l'étude</a>
  </div>
</article>
```

### Ordre des éléments dans la carte (strict)
media → badge → title → desc → sources → (`eco3-card__related` optionnel) → (lang-note, EN seulement) → cta.
Le bloc `related` (lien vers un dataset tracker sous-jacent), quand il existe, se place
**après** sources et **avant** lang-note :
```html
<p class="eco3-card__related">📊 <a href="/en/{{slug-dataset}}/">Underlying tracker dataset (auto-updated quarterly)</a></p>
```

---

## Règles de détail (chacune est un piège déjà rencontré)

1. **Featured image — préfixe.** EN : `path="en/{{slug-en}}"` (avec `en/`). FR :
   `path="{{slug-fr}}"` (slug nu, sans préfixe). Oublier le `en/` côté EN casse l'image.

2. **Slug FR plat.** Le FR n'a pas de `/fr/`. C'est `/{{slug-fr}}/`. (cf. archi-eco3min.)

3. **Asymétrie lang-note.** Les cartes EN portent une `eco3-card__lang-note` 🇫🇷 → slug FR.
   Les cartes FR **n'en portent pas** (pas de lien 🇬🇧 réciproque). Respecter le pattern :
   ne pas ajouter de lang-note à la carte FR. (Si Paul veut un jour symétriser, c'est une
   décision séparée qui touche TOUTES les cartes FR, pas un ajout ponctuel.)

4. **lang-note quand la version FR n'est pas encore en ligne.** Pointer le lien 🇫🇷 vers le
   hub FR `/observatoire-macro/` (jamais vers le hub EN — c'est le bug de la carte
   Purchasing Power qui pointait `/en/macro-watch/`). Corriger vers le slug FR exact dès
   que la page FR est publiée. Idem côté FR si c'est l'EN qui manque : le `href` de la carte
   et son CTA peuvent pointer la version disponible en attendant.

5. **wpautop.** Garder `<a class="eco3-card__media">...[shortcode]...</a>` sur **une seule
   ligne**. Un retour à la ligne autour du shortcode vide fait injecter des `<br>` par
   wpautop.

6. **`data-eco3-cat`.** Valeurs connues : `macro`, `commodities`, `equity`, ou combinaison
   séparée par espace (`commodities equity`). Choisir selon le sujet. Sujets fiscaux /
   démographiques / monétaires → `macro`.

7. **AMF.** Le texte de la carte est descriptif : aucun `should/must/buy/sell/allocate`,
   aucune cible chiffrée d'allocation. (cf. editeur-eco3min.)

8. **Cohérence des chiffres.** Tout nombre de la carte doit être **identique** à
   l'article, au chart et au `fact_check_audit.md`. La carte n'introduit aucun chiffre
   nouveau ni arrondi divergent. Reprendre les chiffres de l'audit, pas de mémoire.

9. **Faux-amis FR pour sujets US.** Traduire les noms d'institutions avec soin (ex. « Social
   Security » = régime de retraite américain, **pas** « Sécurité sociale » ; « payroll
   taxes » = cotisations sur salaires). Ancrer le pays.

10. **Date = jour de publication du cycle** (le mardi). Format EN « Month D, YYYY » ;
    format FR « D mois YYYY » avec mois en minuscule
    (janvier, février, mars, avril, mai, juin, juillet, août, septembre, octobre, novembre, décembre).

---

## Méthode Python anti-erreur (quand Claude édite les fichiers hub)

Si les deux fichiers hub sont disponibles sur disque, insérer par script plutôt qu'à la
main, avec assertions. Schéma :

```python
import re

CARD_EN = """{{bloc <article> EN complet, voir template}}"""
CARD_FR = """{{bloc <article> FR complet}}"""
PAT = '<article class="eco3-card eco3-card--study"'

for path, card, count_word in [(HUB_EN, CARD_EN, "studies"), (HUB_FR, CARD_FR, "études")]:
    s = open(path, encoding="utf-8").read()
    before = s.count(PAT)

    # 1) insérer la carte juste après l'ouverture du grid
    anchor = '<div class="eco3-grid">'
    assert s.count(anchor) == 1, f"grid introuvable/multiple dans {path}"
    s = s.replace(anchor, anchor + "\n\n" + card.strip() + "\n", 1)

    after = s.count(PAT)
    assert after == before + 1, f"insertion KO ({before}->{after})"

    # 2) compteur = vrai nombre de cartes, aux DEUX endroits
    N = after
    s = re.sub(r'(eco3-stat__value--accent">)\d+(</span>)', rf'\g<1>{N}\g<2>', s, count=1)
    s = re.sub(rf'(<p class="eco3-section__count">)\d+( {count_word} ·)', rf'\g<1>{N}\g<2>', s, count=1)

    # 3) garde-fous : exactement un compteur de chaque type
    assert s.count('eco3-stat__value--accent">'+str(N)) == 1
    assert re.search(rf'eco3-section__count">{N} {count_word}', s)

    open(path, "w", encoding="utf-8").write(s)
    print(f"{path}: {before} -> {N} cartes")
```

Puis bumper le changelog (entrée datée + version) en tête de chaque fichier, et **relire
visuellement** la première carte rendue. Ne pas livrer sans le recomptage assert.

---

## Checklist de pré-livraison (bloquante)

- [ ] Carte en **1re position** du grid (avant l'ancienne tête), dans les deux hubs
- [ ] Slug EN sous `/en/`, slug FR **plat**
- [ ] Featured image : `en/{slug}` (EN) · `{slug}` (FR)
- [ ] Badge au bon format et à la **date de publication** (mardi)
- [ ] **Compteur = vrai nombre de cartes**, aux **2 emplacements**, dans les **2 hubs** (recompté, pas +1)
- [ ] Carte EN **avec** lang-note 🇫🇷 (→ slug FR, ou `/observatoire-macro/` si FR pas prête)
- [ ] Carte FR **sans** lang-note
- [ ] `.eco3-card__media` sur **une seule ligne**
- [ ] Texte **AMF** : pas de should/must/buy/sell/allocate, pas de cible d'allocation
- [ ] **Tous les chiffres = audit** (identiques article + chart + fact_check_audit)
- [ ] Faux-amis FR traités si sujet US
- [ ] `data-eco3-cat` cohérent avec le sujet
- [ ] Bloc `related` ajouté **si** un dataset tracker sous-jacent existe (avant lang-note)
- [ ] **Changelog + version** bumpés dans les deux fichiers
- [ ] CTA : `Read the study` / `Lire l'étude`
- [ ] Livraison = **les deux pages complètes** prêtes à coller (mode Code WP)

---

## Récap des pièges (à scanner avant de livrer)

1. Compteur **+1 aveugle** → faux dès qu'un décalage préexiste. Recompter.
2. Oublier le **2e** compteur (`eco3-section__count`) : il y en a deux par hub.
3. Préfixe **`en/`** oublié sur la featured image côté EN.
4. lang-note EN pointant vers le **hub EN** au lieu du slug FR / hub FR.
5. Ajouter une lang-note à la carte **FR** (n'existe pas dans le pattern).
6. **`media`** wrappé sur plusieurs lignes → `<br>` injectés par wpautop.
7. Slug FR avec **`/fr/`** (faux : FR est plat).
8. Chiffres de la carte **divergents** de l'article/chart/audit.
9. Faux-ami FR (« Sécurité sociale » pour « Social Security », etc.).

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

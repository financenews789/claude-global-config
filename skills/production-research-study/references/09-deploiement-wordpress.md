# production-research-study — référence : Architecture de déploiement WordPress, namespace, snippet, slug, chemins (§20)

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 20. Architecture de déploiement (vérifiée sur WordPress)

### 20.1 Namespace CSS par étude

Chaque classe est `eco3-[STUDY]-*`, où `[STUDY]` est un code court propre à
l'étude. Le namespace partagé `eco3-realrates` est **retiré**.

Le bloc CSS scopé — environ 12 000 caractères, 63 classes canoniques — s'extrait
par curl depuis **l'étude publiée la plus récente**, puis se re-namespace. Jamais
reconstruit de zéro, jamais repris d'une page ancienne qui pourrait ne pas avoir
les règles de l'accordéon FAQ.

### 20.2 Le snippet est autonome

Un Code Snippet par étude. Ordre : fonction de garde (slug + variante `-2`) → CSS
scopé (`wp_head` priorité 4) → JSON-LD Article/Dataset/FAQPage (`wp_head`
priorité 5) → meta OG et Twitter (`wp_head` priorité 99) → filtres RankMath
title/description (priorité 99, **jamais** l'onglet Social) → JS (`wp_footer`
priorité 99 : délégation FAQ sur `document` avec drapeau anti-double-init, copie
de partage, sélecteur d'embed, sommaire mobile).

**Le corps HTML ne contient ni `<style>` ni `<script>`** : WordPress et Autoptimize
les retirent ou les réordonnent quand ils sont dans le contenu.

### 20.3 Règles WordPress dures

- **UTF-8 littéral** dans les `content:""` du CSS — WP supprime les échappements
  de type `\2713`.
- Code Snippets se colle **sans balise `<?php` ouvrante**.
- Le heredoc `<<<'CSS'` est l'alternative valide pour embarquer le CSS.
- URL d'assets en `wp-content/uploads/[YYYY]/[MM]` avec le **mois courant**,
  identiques dans le HTML, le snippet et les guides.
- WP peut créer des variantes `-scaled` des PNG : **référencer les originaux non
  suffixés**.
- Uploader les SVG — c'est la `<source>` primaire du `<picture>`.

### 20.4 Discipline de slug

Vérifier la disponibilité **avant** production. Si WP attribue un `-2`, le
propager à : la fonction de garde, le `@id` / `mainEntityOfPage` / `url` du
JSON-LD, l'`og:url`, l'encart de citation, le package social. Un fragment
orphelin fait échouer la garde.

⚠️ **D'où vient ce `-2`, et comment ne plus jamais le subir.** Ce n'est pas WP qui
est capricieux : `wp_unique_post_slug()` vérifie `post_type IN ('page',
'attachment')`, donc **une pièce jointe occupe l'espace de noms des slugs de
page**. Le CSV de l'étude, nommé comme le slug, prend le slug ; le XLSX prend le
`-2` ; la page ne peut plus obtenir que le `-3`. La règle est donc en amont :
**le nom de base des assets n'est jamais le slug de la page**, et le bundle
s'importe **avant** l'upload des données. Autorité complète, assertion de build,
diagnostic en une ligne et procédure de réparation :
`eco3min-import-contenu-bilingue`, section « Le slug de page ne doit JAMAIS être
le nom de base d'un asset ».

### 20.5 Mécanisme FAQ

Un `<h3>` à l'intérieur de `.eco3-[STUDY]-faq-item`, qui bascule
`.eco3-[STUDY]-open`.

### 20.6 Conventions de chemins

- Données et charts :
  `https://eco3min.fr/wp-content/uploads/[YYYY]/[MM]/[fichier]`, mois courant.
- Noms de charts : `[study-slug]-hero-v1.{png,svg,pdf}` et
  `[study-slug]-[descriptif]-v1.{png,svg,pdf}`.
- L'image OG **est** le PNG hero. Pas de rendu OG séparé, sauf poussée forte :
  alors 1200×630.
- Liens internes : `/en/` côté EN, vérifiés contre le snapshot.
- Embeds : `https://eco3min.fr/embed/[chart-slug]`.

---

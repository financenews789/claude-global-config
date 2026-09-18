# plugins-eco3min — référence : Format strict des patches v1.0.2 (§6)

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026), à une mention près (la règle cap 18 est attribuée au projet C, plus aux « custom instructions » claude.ai). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

---

## 6. Format strict des patches v1.0.2+ (onglet 🔗 Maillage du mega)

L'onglet 🔗 Maillage du mega (`class-eco3min-mega-tab-4-maillage.php`, héritier du plugin Maillage Cluster désactivé le 15/09/2026 — il n'y a plus qu'un seul applicateur de patches) rejette tout patch qui ne respecte pas exactement ce format :

```json
{
  "batch_id": "patches-{cluster_slug}-{n}",
  "generated_at": "2026-05-07T10:30:00+02:00",
  "cluster": "{cluster_slug}",
  "patches": [
    {
      "post_id": 4521,
      "anchor_before": "...",
      "insert_after_anchor": " ...<a href=\"...\">...</a>...",
      "expected_occurrences": 1,
      "comment": "..."
    }
  ]
}
```

**Règles dures** (rejet immédiat sinon) :
- `expected_occurrences` **toujours = 1** (le plugin vérifie que `mb_substr_count($content, $anchor)` = 1).
- `anchor_before` **80-200 chars** (mb_strlen), plain text, **exactement 1 occurrence** dans `source_post_content`.
- Pas de balises HTML dans `anchor_before` (`<a>`, `<strong>`, etc.).
- Pas dans une zone interdite : attribut HTML, `<script>`, `<style>`, `<!-- -->`, shortcode `[...]`, JSON-LD.
- `insert_after_anchor` doit avoir un `<a href>` complet avec URL absolue.
- Cohérence linguistique stricte : un FR ne pointe **jamais** vers `/en/`.

**Règles soft** (Claude doit respecter, sinon le patch est sous-optimal) :
> Note du 18/09/2026 : les trois premières (12 liens par article, 3 par cluster, 1 par paragraphe) datent du plugin Maillage Cluster et sont **supplantées** par `patches-maillage-eco3min` — §2.5.3 gate paragraphe gradué (≤ 2 liens existants dans le bloc hôte, 3 tolérés si ≥ 80 mots) et §5 densité relative par famille (alerte au rapport, jamais un skip). Conservées ici verbatim pour l'historique ; en cas de conflit, le skill de rédaction fait foi. Le cap 18 est par fichier (décision du 18/09/2026).
- 12 liens internes max par article après ajout.
- 3 liens max vers le même cluster dans un article.
- 1 lien par paragraphe max.
- Pas de lien dans les 2 premiers paragraphes (sauf vers pillar parent).
- Cap 18 patches/cible par batch (règle du projet C, `patches-maillage-eco3min`).

**Variation des ancres `<a>...</a>`** (anti-spam SEO) :
- **Le vrai signal SEO suspect = diversité des ancres, pas le nombre de liens.**
- Pour une même cible, varier syntaxiquement, lexicalement, positionnellement, par registre.
- Mots-pivots à varier : étude, analyse, cadre, dynamique, mécanisme, données, observation, etc.
- Sur 21 patches vers même cible : max ~5 fois le même mot-pivot (sinon spam pattern).

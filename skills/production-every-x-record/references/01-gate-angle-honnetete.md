# production-every-x-record — référence : GATE avant production et angle killer (§0, §1)

Extrait VERBATIM de SKILL.md (découpage du 17/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 0. GATE — avant toute production

### 0.1 La formule de sélection (ce qui mérite une page "Every X")
Le seul carton backlink confirmé (yield curve → FT + Ritholtz) réunissait les quatre :
- **indicateur ULTRA-CITÉ** (le lecteur le connaît déjà : courbe, Sahm, Fed, CAPE…) ;
- **track record quasi-parfait** sur longue période (le "X-for-X" ou "depuis 19XX") ;
- **une ANOMALIE LIVE** au moment de publier (l'exception en cours, le truc qui vient de casser) ;
- **un dataset unique téléchargeable** (CSV + JSON-LD Dataset).
Manque un pilier → la pièce sera plus faible. Pas d'anomalie live → c'est de l'evergreen SEO, pas un carton backlink ; route différente.

### 0.2 Le data-check bloquant (RÈGLE CARDINALE #2)
Avant d'écrire le hook ou de promettre quoi que ce soit : tirer la série (FRED/source primaire), **calculer le finding sur la vraie donnée**, et confirmer qu'il tient. Si le superlatif ("jamais", "chaque", "le seul") ne survit pas exactement → reformuler vers la version étroite qui tient (voir §1.2). Ne jamais publier un superlatif que le CSV ne soutient pas.

### 0.3 Le GATE surface virale (→ `production-killer-hn`)
Tester la surface virale du sujet AVANT de choisir le canal. Le format "Every X" est **r/economics-natif** (finding débattable, payoff sans expertise lourde) et **DIB-natif** si chart-centré. Il n'est PAS HN-natif si le sujet est macro-spécialisé sans hook universel (cf. échec term premium). Ne pas forcer HN.

---

## 1. L'angle killer

### 1.1 Le hook = la phrase citable (≤ 25 mots)
La phrase qu'un journaliste FT reprend telle quelle. Factuelle, datée, contre-intuitive. Ex : *"Since 1970 the real-time Sahm Rule never gave a false recession signal — until 2024, when it triggered, peaked, and reversed with no recession."* C'est le hook, pas un titre marketing. Le punch va dans le hook + le PNG + le 1er commentaire — **jamais dans le titre Reddit** (cf. §6).

### 1.2 L'honnêteté est le BLINDAGE (la leçon centrale)
La version honnête et étroite bat toujours le superlatif cherry-pické :
- "jamais trompé" était faux (Sahm compte 1959 + 1969 ; un touch à 0,50 en 1976). La version corrigée — *"premier faux signal depuis 1970 ; deux exceptions antérieures, chacune suivie d'une récession"* — est blindée contre le commentaire-tueur. Plus solide ET toujours explosive.
- **Disclose toi-même les cas gênants** (les re-triggers intra-épisode, les touches d'un mois, les bornes ambiguës). Pré-empter le reviewer hostile dans le corps + le 1er commentaire.
- **Le dek/hook ne doit JAMAIS contredire la table du record** (piège réel : dek "almost never come back bigger" alors que la table affichait 7/12 "higher" — commentaire-tueur servi sur un plateau ; corrigé en "almost never KEPT coming back bigger"). Relire le dek APRÈS la table, ligne par ligne : chaque superlatif du dek doit survivre à chaque ligne de la table.
- **Si le créateur/une autorité a commenté l'indicateur, le sourcer** (Sahm sur sa propre règle). Massif en crédibilité — et VÉRIFIER que ton décompte ne CONTREDIT pas le sien (Sahm ne compte pas 1976 ; si la page l'affichait comme "fausse alerte" à côté de sa citation, elle se contredisait).
- **Citation = source exacte obligatoire** (permalink + date + support). Jamais de citation de mémoire ; marquer `<!-- VERIFY -->` tant que non sourcée.

### 1.3 Cadrage technique non négociable
Décrire l'indicateur pour ce qu'il EST (coïncident vs prédicteur, real-time vs revised…). Mal cadrer = un quant te corrige en commentaire #2. Le cadrage juste rend souvent l'anomalie PLUS frappante.

### 1.4 La phrase de désamorçage sémantique
Pour tout finding reposant sur une classification ("faux signal", "récession", "épisode"), désamorcer le débat en assumant le choix de définition + la falsifiabilité : *"Whether X should be called a definitive Y is a classification choice. My criterion is explicit: […]. If [new data] later shows otherwise, I'll revise."* Coupe 50 commentaires de débat sémantique.

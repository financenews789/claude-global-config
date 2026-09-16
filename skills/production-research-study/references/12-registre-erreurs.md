# production-research-study — référence : Registre des motifs d'erreur, post-mortems #22, #20, #6, R1 (§24)

Extrait VERBATIM de SKILL.md (découpage du 15/09/2026). Fait foi avec SKILL.md ; SKILL.md porte la version condensée et le moment où lire ce fichier.

## 24. Annexe — registre des motifs d'erreur

Post-mortems compressés. C'est l'origine du système de verrous : ne pas les
alléger sans relire cette annexe.

**Étude #22 — 6 erreurs, un seul mécanisme.** Des claims quantitatifs écrits dans
les sections « annexes » — sous-titre du Chart B, interp-grid de vélocité, encart
takeaway — **estimés visuellement, jamais calculés**. L'audit déclaratif ne
vérifiait que les claims dont le producteur se souvenait. Pires écarts : comptages
de régime à −51 % et +154 %.
→ D'où : audit extractif PASS 1/2/3, calculer-avant-d'écrire, restriction des
hedges, règle Top-N, périmétrage explicite des sections oubliées.

**Étude #20 — 10 erreurs, cinq motifs.**

- **A — une erreur, quatorze copies.** `finalize_stats.py` calculait `ma_above` à
  la dernière date au lieu de `trigger_8w` ; la valeur fausse est entrée dans
  `locked_stats.json`, **s'est auto-validée à travers l'audit**, puis s'est
  propagée dans le HTML (×3), le JSON-LD et le social (×3) : « 20-week run » pour
  4 réelles, « November 2025 » pour juillet, « 25 weeks » pour 42. → **Verrou A.**
- **B — bon nombre, mauvais concept (×2).** « 7 », qui était un délai d'avance à
  seuil 12 semaines, écrit comme « 7 consecutive weeks above the 52w MA » (série
  réelle : 18) ; et « missed » affirmé pour une récession pourtant détectée.
  → **Verrou B** (Step 6.5c).
- **C — statistique dérivée hors périmètre.** « B+A combined median +12.4 % » tapé
  de tête ; valeur réelle +14,07 %. → **Verrou C** (unions et sous-périodes
  obligatoires).
- **D — hedge interdit employé quand même.** « approximately 40 onsets » ; réel :
  36. → **Verrou D** (scan automatique + fichier de justification).
- **E — comptage lu sur le chart.** « 1985–86 (4 events) » ; réel : 3 dans la
  fenêtre. → **Verrou E** (une assertion par claim de comptage).
- **F — filtre ambigu.** « outside of 2020 » produisait deux écarts-types
  différents, 20 667 et 20 543. → **Verrou F** (définitions formelles).

**Étude #6.** « DGS2 easing pivot in November 1983 » alors que le CSV étiquetait
1983-11 en HIKE — **aucun nombre extractible à vérifier**. → D'où le tripwire de
direction narrative (Step 6.5b).

**Étude R1 (série GENERIQUE, 08/09/2026) — 4 défauts, un seul mécanisme : la
règle non chargée.** L'étude a été produite en chargeant 2 skills sur les 9
déclarées faisant autorité. L'audit extractif passait à 100 % sur 163 claims,
les chiffres étaient justes, la thèse tenait. Ce qui restait :

- **licence** : `USREC` et `M2V` portent le marqueur FRED « Copyrighted: Citation
  Required » ; `USREC` alimentait une colonne d'un CSV redistribué en CC BY 4.0.
  Rien dans la donnée ne le signale, il faut ouvrir la page de série.
  → D'où le contrôle de licence en §23 et la ligne Sourcing de la checklist §21.
- **typographie** : 43 cadratins dans le corps, 18 dans le package social, contre
  une règle à zéro. → **Verrou G.**
- **visuel** : bandes de récession non légendées sur deux charts
  (`visuels-eco3min` §2.2), et 3 des 4 assertions matplotlib de son §7 ter
  absentes du script. Une fois posées, la troisième a mordu immédiatement :
  14 % de recouvrement entre deux lignes de pied, invisible à l'œil à 7 pt.
- **traçabilité** : aucun registre de provenance. → D'où le livrable 17b.

**La leçon transversale** : un audit numérique, si exhaustif soit-il, ne protège
que de ce qu'il sait chercher. Aucun de ces quatre défauts n'est dérivable d'un
CSV — ce sont des règles de doctrine, et **une règle de doctrine non chargée
n'existe pas**. Le premier verrou du pipeline n'est pas le Step 6, c'est le
chargement des skills avant le Step 1.

**Validation du système** : si les verrous avaient été actifs à l'étude #20, les
10 erreurs auraient été bloquées avant livraison — vérifié motif par motif.

**Quatre majeurs du 16/09/2026 — la licence corrigée sur les pages dataset, pas
sur les majeurs qui servent leur propre fichier.** Le mécanisme
`eco3_source_rights()` avait été posé sur les pages dataset du pipeline
(notice visible, JSON-LD `license` FRED citation-required, zéro « CC BY 4.0 »).
Les majeurs `net-liquidity-index-dataset` et `on-rrp-qt-offset-dataset`, EN et
FR, servaient chacun un CSV propre depuis `uploads/`, avec une colonne `sp500`
en niveau (S&P DJI, pre-approval required), une colonne `RRPONTSYD` (citation
required), six mentions « CC BY 4.0 » et un JSON-LD `license` Creative Commons.
Détecté depuis R6, qui avait écarté les deux séries au gate du Step 0. Un
balayage des 393 pages mentionnant `.csv` a trouvé huit autres fichiers
d'études du hub macro US portant un niveau `sp500` ou `nasdaq_close`, un
portant `bbb_oas_pct` (ICE), un portant vingt indices Case-Shiller, et trois
portant une colonne citation-required (`t5yie`/`t10yie`, `m2v`, spread Moody's)
sous CC BY 4.0.
→ D'où le **Verrou L** (Step 0 et Step 6) : aucun niveau brut pre-approval dans
un fichier d'étude, même en colonne de contexte ; une colonne citation-required
interdit « CC BY 4.0 » sur la page et impose la licence réelle dans le JSON-LD.
Et la règle de lecture : **un problème de licence se constate sur la notice et
le JSON-LD de la page, pas sur le CSV ni sur le tag FRED seuls.**

---


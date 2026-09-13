# -*- coding: utf-8 -*-
"""
Synchronise le miroir local des skills avec le compte claude.ai, et dit
QUI EST EN AVANCE SUR QUI.

Trois emplacements, trois roles :

  claude.ai       LA SOURCE DE VERITE. Seul endroit dont le contenu se charge
                  reellement. Tout le reste en decoule.

  cache AppData   Copie automatique, persistante, toujours a jour. Rafraichie
                  par le client quand le compte change. NE RIEN EN FAIRE :
                  ni l'editer, ni le supprimer. Ce script se contente de le
                  lire — c'est sa fenetre sur le compte.

  skills/         Ce dossier. L'HISTORIQUE VERSIONNE, et le seul endroit ou on
                  edite en local. Git y garde le diff, que ni le compte ni le
                  cache ne donnent.

Boucle de travail :

  1. editer un fichier de skills/
  2. l'uploader sur claude.ai (Settings > Skills, ecraser le contenu)
  3. relancer ce script : il confirme la parite

Le manifeste `.sync.json` enregistre l'etat a la derniere synchronisation. Il
permet de distinguer les trois situations, ce qu'une simple comparaison ne
sait pas faire :

  MIROIR EN AVANCE   tu as edite en local, pas encore uploade  -> uploader
  COMPTE EN AVANCE   le compte a change ailleurs               -> --ecrire
  CONFLIT            les deux ont bouge depuis la derniere sync -> arbitrer

Usage :
    python skills/rafraichir.py            # rapport seul, n'ecrit rien
    python skills/rafraichir.py --ecrire   # aligne le miroir sur le compte
"""
import glob
import hashlib
import json
import io
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))

# Les skills fournies par Anthropic ne sont pas mirroir-ees : elles ne sont pas
# de Paul, elles evoluent hors de son controle, et certaines portent des
# fichiers annexes binaires.
ANTHROPIC = {
    "pptx", "xlsx", "pdf", "docx", "morning", "schedule",
    "import-memory", "consolidate-memory", "explain-usage", "setup-cowork",
}


def trouver_cache():
    """Localise le cache de skills de la session courante (le plus recent)."""
    base = os.path.join(os.environ.get("APPDATA", ""), "Claude",
                        "local-agent-mode-sessions", "skills-plugin")
    motif = os.path.join(base, "*", "*", "skills")
    cands = [d for d in glob.glob(motif) if os.path.isdir(d)]
    if not cands:
        return None
    return max(cands, key=os.path.getmtime)


def lire(p):
    with io.open(p, encoding="utf-8") as f:
        return f.read()


def sha(t):
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:12]


def description(txt):
    """Extrait la description du frontmatter.

    Gere les trois formes YAML rencontrees : valeur sur la ligne, valeur
    entre guillemets, et scalaire de bloc (`>-`, `|`) sur plusieurs lignes.
    Sans ca, une description repliee est comptee a 1 ou 2 caracteres.
    """
    if not txt.startswith("---"):
        return ""
    fin = txt.find("\n---", 3)
    fm = txt[3:fin if fin > 0 else len(txt)]
    lignes = fm.split("\n")
    for i, l in enumerate(lignes):
        if not l.startswith("description:"):
            continue
        reste = l[len("description:"):].strip()
        if reste and reste not in (">", ">-", "|", "|-"):
            if len(reste) > 1 and reste[0] == reste[-1] and reste[0] in "\"'":
                reste = reste[1:-1]
            return reste
        # scalaire de bloc : on agrege les lignes indentees qui suivent
        bloc = []
        for suite in lignes[i + 1:]:
            if suite.strip() and not suite[0].isspace():
                break
            bloc.append(suite.strip())
        return " ".join(x for x in bloc if x)
    return ""


def main():
    ecrire = "--ecrire" in sys.argv
    cache = trouver_cache()
    if not cache:
        print("Cache de skills introuvable. Ce script doit tourner dans une "
              "session Claude Code ou le plugin skills a ete charge.")
        return 1

    print("Cache : %s" % cache)

    # --- etat du cache -------------------------------------------------
    amont = {}
    for n in sorted(os.listdir(cache)):
        p = os.path.join(cache, n, "SKILL.md")
        if n in ANTHROPIC or not os.path.exists(p):
            continue
        amont[n] = lire(p)

    # --- etat du miroir ------------------------------------------------
    miroir = {}
    for f in sorted(os.listdir(HERE)):
        if f.endswith(".md") and f not in ("README.md", "INVENTAIRE.md"):
            miroir[f[:-3]] = lire(os.path.join(HERE, f))

    # --- manifeste de la derniere synchronisation ------------------------
    mpath = os.path.join(HERE, ".sync.json")
    try:
        with io.open(mpath, encoding="utf-8") as f:
            manif = json.load(f)
    except Exception:
        manif = {}

    ajout = sorted(set(amont) - set(miroir))
    retrait = sorted(set(miroir) - set(amont))
    communs = sorted(set(amont) & set(miroir))

    compte_avance, miroir_avance, conflit, identiques = [], [], [], []
    for n in communs:
        ha, hm = sha(amont[n]), sha(miroir[n])
        if ha == hm:
            identiques.append(n)
            continue
        ref = manif.get(n)
        if ref is None:
            conflit.append(n)          # pas de reference : on ne peut pas trancher
        elif hm == ref:
            compte_avance.append(n)    # le local n'a pas bouge, le compte si
        elif ha == ref:
            miroir_avance.append(n)    # le compte n'a pas bouge, le local si
        else:
            conflit.append(n)          # les deux ont bouge

    print("")
    print("compte : %d skills (hors Anthropic)  |  miroir : %d  |  identiques : %d"
          % (len(amont), len(miroir), len(identiques)))
    print("")

    for n in ajout:
        print("  + SUR LE COMPTE, PAS EN LOCAL   %s" % n)
    for n in retrait:
        print("  - EN LOCAL, PAS SUR LE COMPTE   %s  (a uploader, ou supprimee "
              "du compte : verifier)" % n)
    for n in miroir_avance:
        print("  ^ MIROIR EN AVANCE              %s  -> A UPLOADER "
              "(compte %d car. -> local %d car.)"
              % (n, len(amont[n]), len(miroir[n])))
    for n in compte_avance:
        print("  v COMPTE EN AVANCE              %s  -> --ecrire (%d -> %d car.)"
              % (n, len(miroir[n]), len(amont[n])))
    for n in conflit:
        print("  ! CONFLIT                       %s  (les deux ont bouge, ou "
              "pas de reference de sync)" % n)

    if not (ajout or retrait or miroir_avance or compte_avance or conflit):
        print("  tout est aligne.")

    # --- garde-fou : longueur des descriptions du frontmatter ---------------
    # claude.ai refuse une description de plus de 1024 caracteres. Le refus
    # arrive a l'upload, apres coup, et le motif recurrent est une description
    # deja tres pleine qu'une edition allonge de quelques mots. On le dit ici,
    # avant l'upload, avec la marge restante.
    LIMITE, SERRE = 1024, 990
    longueurs = []
    for f in sorted(os.listdir(HERE)):
        if not f.endswith(".md") or f in ("README.md", "INVENTAIRE.md"):
            continue
        d = " ".join(description(lire(os.path.join(HERE, f))).split())
        longueurs.append((len(d), f[:-3]))
    trop_long = [(n, l) for l, n in longueurs if l > LIMITE]
    serres = sorted([(n, l) for l, n in longueurs if SERRE <= l <= LIMITE],
                    key=lambda x: -x[1])

    if trop_long:
        print("")
        print("  !! DESCRIPTION TROP LONGUE - claude.ai refusera l'upload (max %d) :" % LIMITE)
        for n, l in trop_long:
            print("     %-42s %d car.  (%d de trop)" % (n, l, l - LIMITE))
    if serres:
        print("")
        print("  ~  %d description(s) a moins de %d car. de la limite, la plus serree : %s (%d)."
              % (len(serres), LIMITE - SERRE + 1, serres[0][0], serres[0][1]))
        print("     Toute rallonge y depasse. Raccourcir AVANT d'ajouter, pas apres le refus.")

    if miroir_avance or conflit:
        print("")
        print("  >> %d fichier(s) a uploader sur claude.ai avant tout --ecrire."
              % (len(miroir_avance) + len(conflit)))
        print("     --ecrire les ECRASERAIT par la version du compte.")

    if not ecrire:
        print("")
        print("Rapport seul. Relancer avec --ecrire pour appliquer.")
        return 1 if trop_long else 0

    if miroir_avance or conflit:
        print("")
        print("REFUS : le miroir est en avance sur le compte pour %d fichier(s)."
              % (len(miroir_avance) + len(conflit)))
        print("Uploader d'abord, ou passer --force pour ecraser le local.")
        if "--force" not in sys.argv:
            return 2

    # --- ecriture ------------------------------------------------------
    for n, t in amont.items():
        with io.open(os.path.join(HERE, n + ".md"), "w",
                     encoding="utf-8", newline="\n") as f:
            f.write(t)
    for n in retrait:
        os.remove(os.path.join(HERE, n + ".md"))

    # --- inventaire ----------------------------------------------------
    lignes = []
    lignes.append(u"# Inventaire des skills du compte")
    lignes.append(u"")
    lignes.append(u"Genere par `rafraichir.py` le %s. **Ne pas editer a la "
                  u"main.**" % time.strftime("%d/%m/%Y"))
    lignes.append(u"")
    lignes.append(u"%d skills personnelles. Les skills fournies par Anthropic "
                  u"(%s) ne sont pas mirroir-ees."
                  % (len(amont), u", ".join(sorted(ANTHROPIC))))
    lignes.append(u"")
    lignes.append(u"| Skill | Taille | Description (car.) | Objet |")
    lignes.append(u"|---|---|---|---|")
    for n in sorted(amont):
        t = amont[n]
        d = description(t)
        objet = d[:120].replace(u"|", u"\\|")
        if len(d) > 120:
            objet = objet.rsplit(u" ", 1)[0] + u"…"
        alerte = u" ⚠️" if len(d) > 1014 else u""
        lignes.append(u"| [`%s`](%s.md) | %d Ko | %d%s | %s |"
                      % (n, n, len(t) // 1024, len(d), alerte, objet))
    lignes.append(u"")
    lignes.append(u"⚠️ = description au-dessus de 1014 caracteres, "
                  u"donc exposee a la troncature (c'est la queue qui saute, "
                  u"la ou vivent les renvois « activer pour… »).")
    lignes.append(u"")
    with io.open(os.path.join(HERE, "INVENTAIRE.md"), "w",
                 encoding="utf-8", newline="\n") as f:
        f.write(u"\n".join(lignes))

    with io.open(mpath, "w", encoding="utf-8", newline="\n") as f:
        json.dump({n: sha(x) for n, x in amont.items()}, f,
                  indent=1, sort_keys=True)

    print("")
    print("Ecrit : %d skills + INVENTAIRE.md + .sync.json" % len(amont))
    return 0


if __name__ == "__main__":
    sys.exit(main())

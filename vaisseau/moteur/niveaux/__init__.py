from moteur.niveaux.niveau_1 import NIVEAU
from moteur.niveaux.niveau_2 import NIVEAU as NIVEAU_2
from moteur.niveaux.niveau_3 import NIVEAU as NIVEAU_3
from moteur.niveaux.niveau_4 import NIVEAU as NIVEAU_4

NIVEAUX = (NIVEAU, NIVEAU_2, NIVEAU_3, NIVEAU_4)


def initialiser_progression(progression):
    progression.setdefault("niveaux_termines", [])
    progression.setdefault("niveau_debloque", 1)
    return progression


def actif(progression):
    initialiser_progression(progression)
    termines = set(progression["niveaux_termines"])
    for niveau in NIVEAUX:
        if niveau.identifiant <= progression["niveau_debloque"] and niveau.identifiant not in termines:
            return niveau
    return NIVEAUX[-1]


def enregistrer_victoire(progression, niveau):
    initialiser_progression(progression)
    if niveau.identifiant in progression["niveaux_termines"]:
        return False
    progression["niveaux_termines"].append(niveau.identifiant)
    progression["niveau_debloque"] = max(progression["niveau_debloque"], niveau.debloque)
    return True

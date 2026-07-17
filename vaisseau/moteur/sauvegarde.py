import json
from pathlib import Path

from moteur import etat as etat_mod

CHEMIN_SAUVEGARDE = Path(__file__).resolve().parent.parent / "sauvegarde.json"


def charger(chemin=CHEMIN_SAUVEGARDE):
    chemin = Path(chemin)
    if not chemin.exists():
        return None

    with chemin.open(encoding="utf-8") as fichier:
        donnees = json.load(fichier)

    vaisseau = donnees["etat"]
    if set(vaisseau) != set(etat_mod.RESSOURCES):
        raise ValueError("etat de sauvegarde invalide")
    if not isinstance(donnees["tick"], int) or donnees["tick"] < 0:
        raise ValueError("tick de sauvegarde invalide")
    if not isinstance(donnees["progression"], dict):
        raise ValueError("progression de sauvegarde invalide")

    return {
        "etat": vaisseau,
        "tick": donnees["tick"],
        "progression": donnees["progression"],
    }


def enregistrer(vaisseau, tick, progression, chemin=CHEMIN_SAUVEGARDE):
    chemin = Path(chemin)
    donnees = {"etat": vaisseau, "tick": tick, "progression": progression}
    temporaire = chemin.with_suffix(".tmp")

    with temporaire.open("w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=2)
        fichier.write("\n")
    temporaire.replace(chemin)

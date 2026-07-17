RESSOURCES = {
    "oxygene": {"min": 0, "max": 100, "seuil_critique": 20},
    "energie": {"min": 0, "max": 100, "seuil_critique": 20},
    "integrite": {"min": 0, "max": 100, "seuil_critique": 30},
}


def initial():
    return {nom: 100 for nom in RESSOURCES}


def appliquer(etat, ressource, delta):
    bornes = RESSOURCES[ressource]
    etat[ressource] = max(bornes["min"], min(bornes["max"], etat[ressource] + delta))


def est_critique(etat, ressource):
    return etat[ressource] <= RESSOURCES[ressource]["seuil_critique"]

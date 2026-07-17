def reguler_temperature(etat):
    """Retourne 21 si l'énergie permet de chauffer la serre, sinon None."""
    if etat["energie"] == 0:
        return None
    return 21


def recycler_eau(etat):
    """Retourne 10 si l'oxygène permet de recycler l'eau, sinon 0."""
    if etat["oxygene"] == 0:
        return 0
    return 10


def eclairer_cultures(etat):
    """Retourne True si l'énergie permet d'éclairer les cultures, sinon False."""
    return etat["energie"] != 0

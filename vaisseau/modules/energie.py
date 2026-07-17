def produire(etat):
    """Contrat module joueur : retourne le delta d'energie ce tick.

    etat : dict d'etat du vaisseau (lecture seule), cle 'tick' disponible.
    Pendant une vague, les ressources peuvent etre a 0 et 'signal_externe' a None.
    """
    if etat["energie"] == 0:
        return 0
    return 10 // etat["energie"]

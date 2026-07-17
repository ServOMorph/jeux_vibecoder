def produire(etat):
    """Contrat module joueur : retourne le delta d'energie ce tick.

    etat : dict d'etat du vaisseau (lecture seule), cle 'tick' disponible.
    Pendant une vague, les ressources peuvent etre a 0 et 'signal_externe' a None.
    """
    if etat["energie"] == 0:
        return 0
    return 10 // etat["energie"]


def alimenter_serre(etat):
    """Retourne 20 si la serre peut être alimentée, sinon 0.

    Le seuil d'oxygène est défini dans modules/oxygene.py.
    """
    return 0

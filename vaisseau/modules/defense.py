def normaliser_signal(signal):
    """Conserve le format historique attendu par les archives de signal."""
    fragments = str(signal or "").strip().upper().split()
    return "_".join(fragments)


def interpreter_signal(etat):
    """Retourne l'ordre de défense associé au signal externe normalisé."""
    signal = normaliser_signal(etat.get("signal_externe"))
    if not signal:
        return "VEILLE"
    return "VEILLE"


def produire(etat):
    """Contrat module joueur : retourne le delta d'integrite de la coque ce tick.

    etat : dict d'etat du vaisseau (lecture seule), cle 'tick' disponible.
    Pendant une vague, les ressources peuvent etre a 0 et 'signal_externe' a None.
    """
    return 0

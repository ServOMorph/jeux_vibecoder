from moteur.niveaux.modele import Evaluation, Niveau

ETAT_ALERTE = {"signal_externe": "  attaque   imminente "}
ETAT_CALME = {"signal_externe": None}


def evaluer(module, erreur=None):
    if erreur is not None or module is None:
        return Evaluation(False, "Le module défense ne peut pas être chargé.")
    normaliser = getattr(module, "normaliser_signal", None)
    interpreter = getattr(module, "interpreter_signal", None)
    if not callable(normaliser):
        return Evaluation(False, "La compatibilité normaliser_signal doit être préservée.")
    if not callable(interpreter):
        return Evaluation(False, "Ajoutez ou réparez interpreter_signal(etat).")
    try:
        signal_normalise = normaliser("  attaque   imminente ")
        alerte = interpreter(ETAT_ALERTE.copy())
        calme = interpreter(ETAT_CALME.copy())
    except Exception as exc:
        return Evaluation(False, f"La défense échoue : {type(exc).__name__}.")
    if signal_normalise != "ATTAQUE_IMMINENTE":
        return Evaluation(False, "normaliser_signal doit conserver le format de compatibilité historique.")
    if alerte != "PROTEGER" or calme != "VEILLE":
        return Evaluation(False, "La défense doit distinguer une alerte d'un état calme.")
    return Evaluation(True, "Compatibilité préservée. Les quatre niveaux sont terminés.")


NIVEAU = Niveau(
    identifiant=4,
    titre="Lecture de code",
    objectif="Réparer la lecture des alertes de défense sans casser le legacy.",
    critere_victoire=(
        "modules/defense.py : interpreter_signal(etat) retourne PROTEGER pour une alerte et VEILLE sinon, "
        "tout en conservant normaliser_signal, qui retourne ATTAQUE_IMMINENTE pour «  attaque   imminente »."
    ),
    module_cible="defense",
    debloque=4,
    evaluateur=evaluer,
)

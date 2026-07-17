from moteur.niveaux.modele import Evaluation, Niveau


def evaluer(module, erreur=None):
    if erreur is not None or module is None:
        return Evaluation(False, "La balise ne peut pas être chargée.")
    fonction = getattr(module, "emettre_signal", None)
    if not callable(fonction):
        return Evaluation(False, "Ajoutez emettre_signal(etat) dans modules/balise.py.")
    try:
        signal = fonction({"tick": 1, "oxygene": 100, "energie": 100, "integrite": 100})
    except Exception as exc:
        return Evaluation(False, f"La balise échoue : {type(exc).__name__}.")
    if signal is True:
        return Evaluation(True, "Signal de détresse émis. Niveau 2 débloqué.")
    return Evaluation(False, "La balise doit retourner exactement True.")


NIVEAU = Niveau(
    identifiant=1,
    titre="Premier signal",
    objectif="Rallumer la balise de détresse.",
    critere_victoire="modules/balise.py : emettre_signal(etat) retourne exactement True.",
    module_cible="balise",
    debloque=2,
    evaluateur=evaluer,
)

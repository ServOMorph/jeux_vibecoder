from moteur.niveaux.modele import Evaluation, Niveau

ETAT_STABLE = {"oxygene": 40, "energie": 20}
ETAT_OXYGENE_INSUFFISANT = {"oxygene": 39, "energie": 20}
ETAT_ENERGIE_INSUFFISANTE = {"oxygene": 40, "energie": 19}


def evaluer(module, erreur=None):
    if erreur is not None or module is None:
        return Evaluation(False, "Le module énergie ne peut pas être chargé.")
    fonction = getattr(module, "alimenter_serre", None)
    if not callable(fonction):
        return Evaluation(False, "Ajoutez alimenter_serre(etat) dans modules/energie.py.")
    try:
        production_stable = fonction(ETAT_STABLE.copy())
        production_sans_oxygene = fonction(ETAT_OXYGENE_INSUFFISANT.copy())
        production_sans_energie = fonction(ETAT_ENERGIE_INSUFFISANTE.copy())
    except Exception as exc:
        return Evaluation(False, f"La serre échoue : {type(exc).__name__}.")
    if production_stable != 20:
        return Evaluation(False, "La serre doit recevoir 20 unités avec les ressources suffisantes.")
    if production_sans_oxygene != 0:
        return Evaluation(False, "La serre doit couper son alimentation sous le seuil d'oxygène.")
    if production_sans_energie != 0:
        return Evaluation(False, "La serre doit couper son alimentation sous le seuil d'énergie.")
    return Evaluation(True, "Contrainte d'oxygène respectée. Niveau 3 débloqué.")


NIVEAU = Niveau(
    identifiant=2,
    titre="Contexte",
    objectif="Alimenter la serre en tenant compte de l'oxygène et de l'énergie.",
    critere_victoire=(
        "modules/energie.py : alimenter_serre(etat) retourne 20 avec oxygene=40 et energie=20, "
        "sinon 0 sous l'un de ces seuils. Le seuil d'oxygène est défini dans modules/oxygene.py."
    ),
    module_cible="energie",
    debloque=3,
    evaluateur=evaluer,
)

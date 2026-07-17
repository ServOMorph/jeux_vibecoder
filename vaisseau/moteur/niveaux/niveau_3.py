from moteur.niveaux.modele import Evaluation, Niveau

ETAT_STABLE = {"oxygene": 50, "energie": 50}
ETAT_SANS_OXYGENE = {"oxygene": 0, "energie": 50}
ETAT_SANS_ENERGIE = {"oxygene": 50, "energie": 0}


def evaluer(module, erreur=None):
    if erreur is not None or module is None:
        return Evaluation(False, "Le module serre ne peut pas être chargé.")
    fonctions = {
        "régulation thermique": getattr(module, "reguler_temperature", None),
        "recyclage de l'eau": getattr(module, "recycler_eau", None),
        "éclairage des cultures": getattr(module, "eclairer_cultures", None),
    }
    manquantes = [nom for nom, fonction in fonctions.items() if not callable(fonction)]
    if manquantes:
        return Evaluation(False, "Sous-systèmes manquants : " + ", ".join(manquantes) + ".")
    try:
        temperature = module.reguler_temperature(ETAT_STABLE.copy())
        eau = module.recycler_eau(ETAT_STABLE.copy())
        lumiere = module.eclairer_cultures(ETAT_STABLE.copy())
        eau_sans_oxygene = module.recycler_eau(ETAT_SANS_OXYGENE.copy())
        temperature_sans_energie = module.reguler_temperature(ETAT_SANS_ENERGIE.copy())
        lumiere_sans_energie = module.eclairer_cultures(ETAT_SANS_ENERGIE.copy())
    except Exception as exc:
        return Evaluation(False, f"La serre échoue : {type(exc).__name__}.")
    if temperature != 21 or eau != 10 or lumiere is not True:
        return Evaluation(False, "Les trois sous-systèmes doivent fonctionner en conditions stables.")
    if eau_sans_oxygene != 0:
        return Evaluation(False, "Le recyclage de l'eau doit s'arrêter sans oxygène.")
    if temperature_sans_energie is not None or lumiere_sans_energie is not False:
        return Evaluation(False, "La température et l'éclairage doivent réagir au manque d'énergie.")
    return Evaluation(True, "Serre opérationnelle. Niveau 4 débloqué.")


NIVEAU = Niveau(
    identifiant=3,
    titre="Découpage",
    objectif="Rendre la serre opérationnelle.",
    critere_victoire=(
        "modules/serre.py : réguler la température à 21, recycler 10 unités d'eau et allumer les cultures "
        "avec oxygene=50 et energie=50 ; chaque sous-système doit aussi gérer sa ressource insuffisante."
    ),
    module_cible="serre",
    debloque=4,
    evaluateur=evaluer,
)

import time

from moteur import etat as etat_mod
from moteur import rechargeur

MODULES = ["oxygene", "energie", "defense"]
RESSOURCE_PAR_MODULE = {"oxygene": "oxygene", "energie": "energie", "defense": "integrite"}
INTERVALLE_SEC = 1.0


def lancer():
    for nom in MODULES:
        rechargeur.charger(nom)

    vaisseau = etat_mod.initial()
    tick = 0
    while True:
        tick += 1
        etat_lecture = {"tick": tick, **vaisseau}

        statuts = {}
        for nom in MODULES:
            module, erreur_reload = rechargeur.verifier_et_recharger(nom)
            production = None
            erreur_appel = None
            if module is not None:
                try:
                    production = module.produire(etat_lecture)
                except Exception as exc:
                    erreur_appel = exc
            if production is not None:
                etat_mod.appliquer(vaisseau, RESSOURCE_PAR_MODULE[nom], production)
            statuts[nom] = {
                "production": production,
                "erreur_reload": erreur_reload,
                "erreur_appel": erreur_appel,
            }

        afficher(tick, vaisseau, statuts)
        time.sleep(INTERVALLE_SEC)


def afficher(tick, vaisseau, statuts):
    os_clear()
    print(f"--- Vaisseau-Ecosysteme --- tick {tick}")
    for ressource, valeur in vaisseau.items():
        marque = " [CRITIQUE]" if etat_mod.est_critique(vaisseau, ressource) else ""
        print(f"{ressource} : {valeur}{marque}")
    for nom, s in statuts.items():
        etat_txt = "OK" if s["production"] is not None else "EN ERREUR"
        print(f"Module {nom} : {etat_txt}")
        if s["erreur_reload"] is not None:
            print(f"  [rechargement] {type(s['erreur_reload']).__name__}: {s['erreur_reload']}")
        if s["erreur_appel"] is not None:
            print(f"  [execution] {type(s['erreur_appel']).__name__}: {s['erreur_appel']}")


def os_clear():
    print("\033[H\033[J", end="")

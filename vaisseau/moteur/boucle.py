import time

from moteur import rechargeur

NOM_MODULE = "oxygene"
INTERVALLE_SEC = 1.0


def lancer():
    rechargeur.charger(NOM_MODULE)
    tick = 0
    while True:
        tick += 1
        module, erreur_reload = rechargeur.verifier_et_recharger(NOM_MODULE)

        etat = {"tick": tick}
        production = None
        erreur_appel = None
        if module is not None:
            try:
                production = module.produire(etat)
            except Exception as exc:
                erreur_appel = exc

        os_clear()
        print(f"--- Vaisseau-Ecosysteme --- tick {tick}")
        print(f"Module oxygene : {'OK' if production is not None else 'EN ERREUR'}")
        if production is not None:
            print(f"Production oxygene : {production}")
        if erreur_reload is not None:
            print(f"[rechargement] {type(erreur_reload).__name__}: {erreur_reload}")
        if erreur_appel is not None:
            print(f"[execution] {type(erreur_appel).__name__}: {erreur_appel}")

        time.sleep(INTERVALLE_SEC)


def os_clear():
    print("\033[H\033[J", end="")

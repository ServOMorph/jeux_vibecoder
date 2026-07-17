import time

from moteur import etat as etat_mod
from moteur import rechargeur

MODULES = ["oxygene", "energie", "defense"]
RESSOURCE_PAR_MODULE = {"oxygene": "oxygene", "energie": "energie", "defense": "integrite"}
INTERVALLE_SEC = 1.0
INTERVALLE_VAGUE_TICKS = 20
LARGEUR_JAUGE = 20


def lancer():
    for nom in MODULES:
        rechargeur.charger(nom)

    vaisseau = etat_mod.initial()
    tick = 0
    dernieres_erreurs = {nom: None for nom in MODULES}
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
            erreur = erreur_reload or erreur_appel
            if erreur is not None:
                dernieres_erreurs[nom] = erreur
            statuts[nom] = {
                "production": production,
                "erreur_reload": erreur_reload,
                "erreur_appel": erreur_appel,
            }

        afficher(tick, vaisseau, statuts, dernieres_erreurs)
        time.sleep(INTERVALLE_SEC)


def afficher(tick, vaisseau, statuts, dernieres_erreurs):
    os_clear()
    ticks_avant_vague = INTERVALLE_VAGUE_TICKS - (tick % INTERVALLE_VAGUE_TICKS)
    print(f"--- Vaisseau-Ecosysteme --- tick {tick} --- prochaine vague dans {ticks_avant_vague} tick(s)")
    print()
    for ressource, valeur in vaisseau.items():
        marque = " [CRITIQUE]" if etat_mod.est_critique(vaisseau, ressource) else ""
        print(f"{ressource:10s} {jauge(ressource, valeur)} {valeur:3d}{marque}")
    print()
    for nom, s in statuts.items():
        if s["production"] is not None:
            etat_txt = "OK"
        elif s["erreur_reload"] is not None:
            etat_txt = "CASSE"
        else:
            etat_txt = "EN ERREUR"
        print(f"Module {nom:10s} : {etat_txt}")
        erreur = dernieres_erreurs.get(nom)
        if erreur is not None:
            print(f"  derniere erreur : {type(erreur).__name__}: {erreur}")


def jauge(ressource, valeur):
    bornes = etat_mod.RESSOURCES[ressource]
    proportion = (valeur - bornes["min"]) / (bornes["max"] - bornes["min"])
    remplies = round(proportion * LARGEUR_JAUGE)
    return "[" + "#" * remplies + "-" * (LARGEUR_JAUGE - remplies) + "]"


def os_clear():
    print("\033[H\033[J", end="")

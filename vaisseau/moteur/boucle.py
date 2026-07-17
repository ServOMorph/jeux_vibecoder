import time

from moteur import etat as etat_mod
from moteur import rechargeur
from moteur import sauvegarde
from moteur import score
from moteur import vagues

MODULES = ["oxygene", "energie", "defense"]
RESSOURCE_PAR_MODULE = {"oxygene": "oxygene", "energie": "energie", "defense": "integrite"}
INTERVALLE_SEC = 1.0
LARGEUR_JAUGE = 20


def lancer():
    for nom in MODULES:
        rechargeur.charger(nom)

    reprise = sauvegarde.charger()
    if reprise is None:
        vaisseau = etat_mod.initial()
        tick = 0
        progression = {"vague_initiale_terminee": False}
    else:
        vaisseau = reprise["etat"]
        tick = reprise["tick"]
        progression = reprise["progression"]
    dernieres_erreurs = {nom: None for nom in MODULES}
    while True:
        tick += 1
        etat_lecture = {"tick": tick, **vaisseau}
        vague = vagues.active(tick)
        charge = vague["charge"] if vague is not None else 1
        if vague is not None:
            etat_lecture = vagues.etat_sous_charge(etat_lecture, vague)

        statuts = {}
        for nom in MODULES:
            module, erreur_reload = rechargeur.verifier_et_recharger(nom)
            production = 0
            erreur_appel = None
            if module is not None:
                for _ in range(charge):
                    try:
                        resultat = module.produire(etat_lecture)
                        if not isinstance(resultat, int):
                            raise TypeError("produire(etat) doit retourner un entier")
                        production += resultat
                    except Exception as exc:
                        erreur_appel = exc
                        break
            else:
                production = None
            if production is not None and erreur_appel is None:
                etat_mod.appliquer(vaisseau, RESSOURCE_PAR_MODULE[nom], production)
            erreur = erreur_reload or erreur_appel
            if erreur is not None:
                dernieres_erreurs[nom] = erreur
            statuts[nom] = {
                "production": production,
                "erreur_reload": erreur_reload,
                "erreur_appel": erreur_appel,
            }

        modules_en_echec = [
            nom
            for nom, statut in statuts.items()
            if statut["erreur_reload"] is not None or statut["erreur_appel"] is not None
        ]
        degats = vagues.degats(vague, modules_en_echec) if vague is not None else 0
        if degats:
            etat_mod.appliquer(vaisseau, "integrite", -degats)

        progression["vague_initiale_terminee"] = (
            vague is None and vagues.ticks_avant_prochaine(tick) is None
        )
        sauvegarde.enregistrer(vaisseau, tick, progression)
        afficher(tick, vaisseau, statuts, dernieres_erreurs, vague, degats)
        time.sleep(INTERVALLE_SEC)


def afficher(tick, vaisseau, statuts, dernieres_erreurs, vague, degats):
    os_clear()
    if vague is not None:
        vague_txt = f"VAGUE ACTIVE : charge x{vague['charge']} | conditions degradees"
        if degats:
            vague_txt += f" | degats coque : {degats}"
    else:
        ticks_avant_vague = vagues.ticks_avant_prochaine(tick)
        vague_txt = (
            f"prochaine vague dans {ticks_avant_vague} tick(s)"
            if ticks_avant_vague is not None
            else "vague terminee"
        )
    print(f"--- Vaisseau-Ecosysteme --- tick {tick} --- {vague_txt}")
    print()
    for ressource, valeur in vaisseau.items():
        marque = " [CRITIQUE]" if etat_mod.est_critique(vaisseau, ressource) else ""
        print(f"{ressource:10s} {jauge(ressource, valeur)} {valeur:3d}{marque}")
    print()
    for nom, s in statuts.items():
        if s["erreur_reload"] is not None:
            etat_txt = "CASSE"
        elif s["erreur_appel"] is not None:
            etat_txt = "EN ERREUR"
        else:
            etat_txt = "OK"
        iterations = score.nombre_rechargements(nom)
        print(f"Module {nom:10s} : {etat_txt} | iterations IA : {iterations}")
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

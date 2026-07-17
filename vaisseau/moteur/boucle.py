import time

from moteur import etat as etat_mod
from moteur import niveaux
from moteur import rechargeur
from moteur import sauvegarde
from moteur import score
from moteur import vagues

MODULES = ["oxygene", "energie", "defense"]
RESSOURCE_PAR_MODULE = {"oxygene": "oxygene", "energie": "energie", "defense": "integrite"}
INTERVALLE_SEC = 1.0
LARGEUR_JAUGE = 20


class Partie:
    def __init__(self, vaisseau, tick, progression):
        self.vaisseau = vaisseau
        self.tick = tick
        self.progression = niveaux.initialiser_progression(progression)
        self.dernieres_erreurs = {nom: None for nom in MODULES}

    @classmethod
    def charger(cls):
        for nom in MODULES:
            rechargeur.charger(nom)

        reprise = sauvegarde.charger()
        if reprise is None:
            return cls.nouvelle()
        return cls(reprise["etat"], reprise["tick"], reprise["progression"])

    @classmethod
    def nouvelle(cls):
        return cls(etat_mod.initial(), 0, {"vague_initiale_terminee": False})

    def preparer_vague_dev(self):
        self.tick = vagues.TICK_DEPART - 1
        self.progression["vague_initiale_terminee"] = False

    def etat_niveau(self):
        niveau = niveaux.actif(self.progression)
        module, erreur = rechargeur.verifier_et_recharger(niveau.module_cible)
        evaluation = niveau.evaluer(module, erreur)
        return niveau, evaluation

    def avancer(self):
        self.tick += 1
        etat_lecture = {"tick": self.tick, **self.vaisseau}
        vague = vagues.active(self.tick)
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
                etat_mod.appliquer(self.vaisseau, RESSOURCE_PAR_MODULE[nom], production)
            erreur = erreur_reload or erreur_appel
            if erreur is not None:
                self.dernieres_erreurs[nom] = erreur
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
            etat_mod.appliquer(self.vaisseau, "integrite", -degats)

        niveau, evaluation_niveau = self.etat_niveau()
        if evaluation_niveau.reussi:
            niveaux.enregistrer_victoire(self.progression, niveau)

        self.progression["vague_initiale_terminee"] = (
            vague is None and vagues.ticks_avant_prochaine(self.tick) is None
        )
        sauvegarde.enregistrer(self.vaisseau, self.tick, self.progression)
        return {
            "tick": self.tick,
            "vaisseau": self.vaisseau.copy(),
            "statuts": statuts,
            "dernieres_erreurs": self.dernieres_erreurs.copy(),
            "vague": vague,
            "degats": degats,
            "niveau": {
                "titre": niveau.titre,
                "objectif": niveau.objectif,
                "critere_victoire": niveau.critere_victoire,
                "reussi": evaluation_niveau.reussi,
                "diagnostic": evaluation_niveau.diagnostic,
            },
        }


def lancer():
    partie = Partie.charger()
    while True:
        tour = partie.avancer()
        afficher(
            tour["tick"],
            tour["vaisseau"],
            tour["statuts"],
            tour["dernieres_erreurs"],
            tour["vague"],
            tour["degats"],
        )
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

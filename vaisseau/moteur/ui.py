import tkinter as tk
from tkinter import ttk

from moteur import boucle
from moteur import etat as etat_mod
from moteur import score
from moteur import vagues

COULEUR_FOND = "#08111f"
COULEUR_PANNEAU = "#111f33"
COULEUR_BORDURE = "#29445f"
COULEUR_TEXTE = "#e8f1ff"
COULEUR_SECONDAIRE = "#91a9c4"
COULEUR_OK = "#55d6a0"
COULEUR_ALERTE = "#ffb86b"
COULEUR_DANGER = "#ff6b6b"


def texte_vague(tick, vague):
    if vague is not None:
        return f"VAGUE ACTIVE · CHARGE x{vague['charge']} · CONDITIONS DÉGRADÉES"
    restant = vagues.ticks_avant_prochaine(tick)
    if restant is None:
        return "VAGUE TERMINÉE · SYSTÈMES STABILISÉS"
    return f"PROCHAINE VAGUE DANS {restant} TICK(S)"


def statut_module(statut):
    if statut["erreur_reload"] is not None:
        return "CODE CASSÉ", COULEUR_DANGER
    if statut["erreur_appel"] is not None:
        return "EN ERREUR", COULEUR_ALERTE
    return "OPÉRATIONNEL", COULEUR_OK


def texte_niveau(niveau):
    statut = "TERMINÉ" if niveau["reussi"] else "EN COURS"
    return f"NIVEAU : {niveau['titre'].upper()} · {statut} · {niveau['objectif']}"


class JaugeRessource(tk.Canvas):
    def __init__(self, parent, ressource):
        super().__init__(parent, height=72, background=COULEUR_PANNEAU, highlightthickness=0)
        self.ressource = ressource
        self.bind("<Configure>", lambda _event: self.afficher(100))

    def afficher(self, valeur):
        self.delete("all")
        largeur = max(self.winfo_width(), 260)
        bornes = etat_mod.RESSOURCES[self.ressource]
        proportion = (valeur - bornes["min"]) / (bornes["max"] - bornes["min"])
        critique = valeur <= bornes["seuil_critique"]
        couleur = COULEUR_DANGER if critique else COULEUR_OK
        self.create_text(0, 10, anchor="nw", text=self.ressource.upper(), fill=COULEUR_SECONDAIRE, font=("Segoe UI", 9, "bold"))
        self.create_text(largeur - 4, 7, anchor="ne", text=f"{valeur:03d}%", fill=COULEUR_TEXTE, font=("Consolas", 18, "bold"))
        self.create_rectangle(0, 42, largeur - 4, 58, fill="#1d314b", outline="")
        self.create_rectangle(0, 42, max(0, (largeur - 4) * proportion), 58, fill=couleur, outline="")


class TableauDeBord(tk.Tk):
    def __init__(self):
        super().__init__()
        self.partie = boucle.Partie.charger()
        self.en_cours = False
        self.tour_programme = None
        self.jauges = {}
        self.cartes_modules = {}
        self.title("Vaisseau-Écosystème · Centre de commandement")
        self.minsize(900, 660)
        self.configure(background=COULEUR_FOND)
        self._configurer_styles()
        self._construire()
        self._afficher_attente()

    def _configurer_styles(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Action.TButton", background="#275b88", foreground=COULEUR_TEXTE, borderwidth=0, padding=(16, 10), font=("Segoe UI", 10, "bold"))
        style.map("Action.TButton", background=[("active", "#3479b4"), ("disabled", "#203449")])
        style.configure("Secondaire.TButton", background=COULEUR_PANNEAU, foreground=COULEUR_TEXTE, borderwidth=0, padding=(16, 10), font=("Segoe UI", 10, "bold"))

    def _panneau(self, parent, **options):
        return tk.Frame(parent, background=COULEUR_PANNEAU, highlightbackground=COULEUR_BORDURE, highlightthickness=1, **options)

    def _construire(self):
        conteneur = tk.Frame(self, background=COULEUR_FOND, padx=28, pady=24)
        conteneur.pack(fill="both", expand=True)

        entete = tk.Frame(conteneur, background=COULEUR_FOND)
        entete.pack(fill="x", pady=(0, 20))
        tk.Label(entete, text="VAISSEAU-ÉCOSYSTÈME", background=COULEUR_FOND, foreground=COULEUR_TEXTE, font=("Segoe UI", 22, "bold")).pack(anchor="w")
        tk.Label(entete, text="Centre de commandement · Modifiez les modules puis observez leur effet en direct.", background=COULEUR_FOND, foreground=COULEUR_SECONDAIRE, font=("Segoe UI", 10)).pack(anchor="w", pady=(3, 0))

        self.bandeau_vague = tk.Label(conteneur, background="#163d5c", foreground=COULEUR_TEXTE, anchor="w", padx=16, pady=12, font=("Segoe UI", 10, "bold"))
        self.bandeau_vague.pack(fill="x", pady=(0, 16))
        self.bandeau_niveau = tk.Label(conteneur, background=COULEUR_PANNEAU, foreground=COULEUR_TEXTE, anchor="w", padx=16, pady=10, font=("Segoe UI", 10, "bold"))
        self.bandeau_niveau.pack(fill="x", pady=(0, 16))

        corps = tk.Frame(conteneur, background=COULEUR_FOND)
        corps.pack(fill="both", expand=True)
        corps.columnconfigure(0, weight=3)
        corps.columnconfigure(1, weight=4)
        corps.rowconfigure(0, weight=1)

        ressources = self._panneau(corps, padx=18, pady=16)
        ressources.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        tk.Label(ressources, text="INTÉGRITÉ DU VAISSEAU", background=COULEUR_PANNEAU, foreground=COULEUR_TEXTE, font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(0, 12))
        for ressource in etat_mod.RESSOURCES:
            jauge = JaugeRessource(ressources, ressource)
            jauge.pack(fill="x", pady=5)
            self.jauges[ressource] = jauge

        modules = self._panneau(corps, padx=18, pady=16)
        modules.grid(row=0, column=1, sticky="nsew", padx=(8, 0))
        tk.Label(modules, text="MODULES SURVEILLÉS", background=COULEUR_PANNEAU, foreground=COULEUR_TEXTE, font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(0, 12))
        for nom in boucle.MODULES:
            carte = tk.Frame(modules, background="#0d1929", padx=14, pady=10)
            carte.pack(fill="x", pady=5)
            titre = tk.Label(carte, text=nom.upper(), background="#0d1929", foreground=COULEUR_TEXTE, font=("Segoe UI", 10, "bold"))
            titre.grid(row=0, column=0, sticky="w")
            statut = tk.Label(carte, background="#0d1929", font=("Segoe UI", 9, "bold"))
            statut.grid(row=0, column=1, sticky="e")
            detail = tk.Label(carte, background="#0d1929", foreground=COULEUR_SECONDAIRE, anchor="w", font=("Consolas", 9))
            detail.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(6, 0))
            carte.columnconfigure(0, weight=1)
            self.cartes_modules[nom] = (statut, detail)

        bas = tk.Frame(conteneur, background=COULEUR_FOND)
        bas.pack(fill="x", pady=(16, 0))
        self.indicateur_tick = tk.Label(bas, background=COULEUR_FOND, foreground=COULEUR_SECONDAIRE, font=("Consolas", 11, "bold"))
        self.indicateur_tick.pack(side="left")
        self.erreur = tk.Label(bas, background=COULEUR_FOND, foreground=COULEUR_ALERTE, anchor="w", font=("Segoe UI", 9))
        self.erreur.pack(side="left", fill="x", expand=True, padx=18)
        self.bouton_lancer = ttk.Button(bas, text="DÉMARRER", style="Action.TButton", command=self.basculer)
        self.bouton_lancer.pack(side="right", padx=(8, 0))
        ttk.Button(bas, text="NOUVELLE PARTIE", style="Secondaire.TButton", command=self.nouvelle_partie).pack(side="right")
        ttk.Button(bas, text="DÉCLENCHER VAGUE (DEV)", style="Secondaire.TButton", command=self.declencher_vague_dev).pack(side="right", padx=(0, 8))

    def _afficher_attente(self):
        niveau, evaluation = self.partie.etat_niveau()
        self._mettre_a_jour({
            "tick": self.partie.tick,
            "vaisseau": self.partie.vaisseau,
            "statuts": {nom: {"erreur_reload": None, "erreur_appel": None, "production": 0} for nom in boucle.MODULES},
            "dernieres_erreurs": self.partie.dernieres_erreurs,
            "vague": vagues.active(self.partie.tick),
            "degats": 0,
            "niveau": {
                "titre": niveau.titre,
                "objectif": niveau.objectif,
                "reussi": evaluation.reussi,
                "diagnostic": evaluation.diagnostic,
            },
        })

    def basculer(self):
        self.en_cours = not self.en_cours
        self.bouton_lancer.configure(text="PAUSE" if self.en_cours else "REPRENDRE")
        if self.en_cours:
            self._tour_suivant()
        elif self.tour_programme is not None:
            self.after_cancel(self.tour_programme)
            self.tour_programme = None

    def nouvelle_partie(self):
        self.en_cours = False
        if self.tour_programme is not None:
            self.after_cancel(self.tour_programme)
            self.tour_programme = None
        self.bouton_lancer.configure(text="DÉMARRER")
        self.partie = boucle.Partie.nouvelle()
        self._afficher_attente()

    def declencher_vague_dev(self):
        if self.tour_programme is not None:
            self.after_cancel(self.tour_programme)
            self.tour_programme = None
        self.partie.preparer_vague_dev()
        self.en_cours = True
        self.bouton_lancer.configure(text="PAUSE")
        self._tour_suivant()

    def _tour_suivant(self):
        self.tour_programme = None
        if not self.en_cours:
            return
        self._mettre_a_jour(self.partie.avancer())
        self.tour_programme = self.after(int(boucle.INTERVALLE_SEC * 1000), self._tour_suivant)

    def _mettre_a_jour(self, tour):
        vague = tour["vague"]
        danger = vague is not None
        self.bandeau_vague.configure(text=texte_vague(tour["tick"], vague), background="#6b2634" if danger else "#163d5c")
        self.bandeau_niveau.configure(text=texte_niveau(tour["niveau"]))
        self.indicateur_tick.configure(text=f"TICK {tour['tick']:03d}")
        for ressource, valeur in tour["vaisseau"].items():
            self.jauges[ressource].afficher(valeur)
        erreurs = []
        for nom, statut in tour["statuts"].items():
            libelle, couleur = statut_module(statut)
            statut_label, detail_label = self.cartes_modules[nom]
            statut_label.configure(text=libelle, foreground=couleur)
            production = statut["production"]
            detail_label.configure(text=f"production : {production if production is not None else '—'}  ·  itérations IA : {score.nombre_rechargements(nom)}")
            erreur = tour["dernieres_erreurs"].get(nom)
            if erreur is not None:
                erreurs.append(f"{nom} : {type(erreur).__name__}")
        texte_erreur = " · ".join(erreurs)
        if tour["degats"]:
            texte_erreur = f"DÉGÂTS COQUE : -{tour['degats']}" + (f" · {texte_erreur}" if texte_erreur else "")
        self.erreur.configure(text=texte_erreur)


def lancer():
    application = TableauDeBord()
    application.mainloop()

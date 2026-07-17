## v0.7 — 2026-07-17

### Ajouté
- Tableau de bord Tkinter local : ressources, états des modules, vague, erreurs et commandes de partie.
- Mode développeur permettant de déclencher immédiatement la vague pour tester le hot-reload et les dégâts.

### Modifié
- Moteur exécuté tour par tour pour être piloté par l'interface ; couverture portée à 16 tests.
- Jalon J1 validé manuellement : panne sous vague, dégâts, correction hot-reload et fin de vague.

## v0.6 — 2026-07-17

### Ajouté
- Sauvegarde atomique et reprise de l'état, du tick et de la progression dans `sauvegarde.json`.
- Compteur non punitif d'itérations IA par module, affiché dans le dashboard.

### Modifié
- `run.py` devient le point d'entrée à la racine ; le rechargeur trouve les modules depuis tout dossier courant.
- Couverture moteur portée à 11 tests.

## v0.5 — 2026-07-17

### Ajouté
- `vaisseau/moteur/vagues.py` : vague scriptée, charge progressive, conditions dégradées et calcul des dégâts.
- `vaisseau/tests/test_vagues.py` : six tests du cycle de vague, des dégâts et de la mécanique de dette.

### Modifié
- `vaisseau/moteur/boucle.py` : intégration de la vague réelle au dashboard et à l'exécution des modules.
- `vaisseau/moteur/rechargeur.py` : persistance des erreurs de chargement jusqu'à la réparation hot-reload.
- `roadmap_phase1.md` et `ROADMAP.md` : sous-phases 1c et 1d marquées terminées.

## v0.4 — 2026-07-17

### Modifié
- `vaisseau/moteur/boucle.py` : dashboard console complet — jauges ASCII par ressource, statut par module (OK/CASSE/EN ERREUR), compte à rebours de la prochaine vague (placeholder), dernière erreur persistée par module.
- `roadmap_phase1.md` : sous-phase 1b marquée [FAIT].

## v0.3 — 2026-07-17

### Ajouté
- `roadmap_phase1.md` : suivi détaillé de la Phase 1, découpée en sous-phases 1a-1f avec checkpoints `/compact`.
- `vaisseau/moteur/etat.py` : modèle d'état centralisé du vaisseau (oxygène, énergie, intégrité, seuils critiques).
- `vaisseau/modules/energie.py`, `vaisseau/modules/defense.py` : modules joueur additionnels.

### Modifié
- `vaisseau/moteur/boucle.py` : généralisé pour piloter plusieurs modules (au lieu du seul `oxygene` en dur).
- `ROADMAP.md` : Phase 1 marquée en cours, renvoi vers `roadmap_phase1.md`.

## v0.2 — 2026-07-17

### Ajouté
- Repo du jeu `vaisseau/` : `run.py`, `moteur/boucle.py`, `moteur/rechargeur.py`, `modules/oxygene.py`, `JOURNAL_DE_BORD.md`.

### Modifié
- ROADMAP.md : Phase 0 marquée terminée, Jalon J0 tranché (hot-reload continu retenu).

## v0.1 — 2026-07-17

### Ajouté
- Session de brainstorming complète (`docs/brainstorm/session-2026-07-17.md`) : cadrage, divergence, SCAMPER, convergence.
- Concept validé : Vaisseau-Écosystème, hybride Usine à Robots + Tour de Garde, hot-reload permanent (`docs/PROJET.md`).
- Plan de développement en 4 phases + post-MVP (`docs/PLAN_DEVELOPPEMENT.md`).
- Roadmap de suivi (`ROADMAP.md`).

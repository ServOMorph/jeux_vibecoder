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

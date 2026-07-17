# jeux_vibecoder

## Objectif
Vaisseau-Écosystème : jeu Python où le joueur pilote son propre agent de codage IA (Claude Code, Cursor, Copilot…) par des prompts pour réparer, construire et défendre un vaisseau-écosystème dont les systèmes sont un vrai chantier de code inachevé. Le jeu n'a pas d'interface autonome : le jeu, c'est le code lui-même. Objectif pédagogique : enseigner le vibecoding compétence par compétence, par niveaux progressifs.

## Stack
Python local, point d'entrée unique `run.py`. Architecture pensée pour le hot-reload (modification de code par l'agent → effet observable en relançant/rechargeant). Dashboard console texte (pygame minimal en option ultérieure). Aucun LLM intégré : jeu 100 % déterministe et scripté, agnostique à l'agent utilisé.

## Structure
- `docs/PROJET.md` — description de référence du concept (issue du brainstorm)
- `docs/PLAN_DEVELOPPEMENT.md` — plan de développement par phases
- `docs/brainstorm/` — historique de la session de brainstorming
- `ROADMAP.md` — suivi d'avancement (phases, jalons)
- `roadmap_phase1.md` — suivi détaillé des sous-phases de la Phase 1
- `_contexte/` — contexte de session (protocole vibecoding)
- `vaisseau/` — repo du jeu (run.py, moteur/, modules/)

## État actuel
Phase 0 (spike hot-reload) terminée. Phase 1 (moteur de jeu minimal) en cours : modèle d'état centralisé, boucle généralisée à 3 modules (oxygène, énergie, défense) et dashboard console complet (jauges, statut modules, compte à rebours de vague, dernière erreur) livrés et testés. Prochaine étape : système de vagues.

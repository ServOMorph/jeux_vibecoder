# jeux_vibecoder

## Objectif
Vaisseau-Écosystème : jeu Python où le joueur pilote son propre agent de codage IA (Claude Code, Cursor, Copilot…) par des prompts pour réparer, construire et défendre un vaisseau-écosystème dont les systèmes sont un vrai chantier de code inachevé. Le jeu n'a pas d'interface autonome : le jeu, c'est le code lui-même. Objectif pédagogique : enseigner le vibecoding compétence par compétence, par niveaux progressifs.

## Stack
Python local, point d'entrée unique `run.py`. Architecture pensée pour le hot-reload (modification de code par l'agent → effet observable en relançant/rechargeant). Tableau de bord Tkinter natif, avec boucle console disponible comme fallback moteur. Aucun LLM intégré : jeu 100 % déterministe et scripté, agnostique à l'agent utilisé.

## Structure
- `docs/PROJET.md` — description de référence du concept (issue du brainstorm)
- `docs/PLAN_DEVELOPPEMENT.md` — plan de développement par phases
- `docs/brainstorm/` — historique de la session de brainstorming
- `ROADMAP.md` — suivi d'avancement (phases, jalons)
- `roadmap_phase1.md` — suivi détaillé des sous-phases de la Phase 1
- `roadmap_phase2.md` — suivi détaillé du contenu pédagogique des niveaux 1 à 4
- `roadmap_ui.md` — suivi de l'interface graphique locale
- `_contexte/` — contexte de session (protocole vibecoding)
- `run.py` — point d'entrée du jeu
- `vaisseau/` — moteur, modules joueur et tests

## État actuel
Les phases 0 à 2 sont terminées et les jalons J0, J1 et J2 sont validés. Lancez `python run.py` depuis la racine pour ouvrir le tableau de bord ; les quatre niveaux sont terminables avec un agent de codage et leurs déblocages sont sauvegardés. Le journal contient les quatre briefs et la suite compte 31 tests réussis. La prochaine étape est la phase 3 de playtest et d’équilibrage.

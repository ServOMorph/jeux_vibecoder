# Contexte — jeux_vibecoder

## Objectif (immuable sauf décision explicite)
Vaisseau-Écosystème : jeu Python où le joueur pilote son propre agent de codage IA (Claude Code, Cursor, Copilot…) par des prompts pour réparer, construire et défendre un vaisseau-écosystème dont les systèmes sont un vrai chantier de code inachevé. Le jeu n'a pas d'interface autonome : le jeu, c'est le code lui-même. Objectif pédagogique : enseigner le vibecoding compétence par compétence, par niveaux progressifs (prompts directs, contexte, découpage, lecture de code legacy, validation, itération sous pression, dette technique).

## Stack / contraintes techniques (stable, rarement modifié)
Projet Python local, point d'entrée unique `run.py`. Architecture pensée pour le hot-reload (modification de code par l'agent → effet observable en relançant/rechargeant). Tableau de bord Tkinter natif ; la boucle console est conservée comme fallback moteur. Aucun LLM intégré : jeu 100 % déterministe et scripté, agnostique à l'agent utilisé. Critères de victoire/progression lisibles dans le code.

## État actuel (réécrit intégralement à chaque /close)
Les phases 0 et 1 sont terminées ; le jalon J1 est validé par une partie manuelle complète. `run.py` lance un tableau de bord Tkinter avec contrôle de partie et déclenchement direct de vague en mode développement. Le moteur est exécutable tour par tour et conserve le hot-reload, les dégâts et la sauvegarde. La suite compte 16 tests réussis. La prochaine étape est le contenu pédagogique de la phase 2.

## Décisions structurantes (append only — 10 entrées max, archiver au-delà)
- 2026-07-17 : Initialisation du protocole vibecoding.
- 2026-07-17 : Concept retenu — Vaisseau-Écosystème (hybride Usine à Robots + Tour de Garde), univers vaisseau-écosystème vivant à la dérive, hot-reload permanent.
- 2026-07-17 : Rôle de l'IA tranché — agent de codage réel du joueur (pas de LLM intégré au jeu), agnostique à l'outil.
- 2026-07-17 : MVP scopé — 1 module + 1 vague, niveaux pédagogiques 1 à 4. Extension "Mission & Audit" repoussée en post-MVP.
- 2026-07-17 : Plan de développement validé — 4 phases (spike hot-reload, moteur, contenu pédagogique, playtest) suivies dans ROADMAP.md.
- 2026-07-17 : Jalon J0 tranché — hot-reload continu validé par spike, pas de repli sur "reprise d'état".
- 2026-07-17 : Phase 1 découpée en sous-phases (1a-1f) dans `roadmap_phase1.md`, avec checkpoint `/compact` après chacune.
- 2026-07-17 : Vague initiale déterministe retenue : ticks 20 à 22, charge progressive et conditions dégradées sans altération de l'état réel.
- 2026-07-17 : `run.py` est déplacé à la racine ; le rechargeur résout les modules sans dépendre du dossier courant.
- 2026-07-17 : Le tableau de bord Tkinter devient l'interface par défaut ; J1 est validé manuellement et le mode développeur peut déclencher une vague immédiate.

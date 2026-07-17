# Contexte — jeux_vibecoder

## Objectif (immuable sauf décision explicite)
Vaisseau-Écosystème : jeu Python où le joueur pilote son propre agent de codage IA (Claude Code, Cursor, Copilot…) par des prompts pour réparer, construire et défendre un vaisseau-écosystème dont les systèmes sont un vrai chantier de code inachevé. Le jeu n'a pas d'interface autonome : le jeu, c'est le code lui-même. Objectif pédagogique : enseigner le vibecoding compétence par compétence, par niveaux progressifs (prompts directs, contexte, découpage, lecture de code legacy, validation, itération sous pression, dette technique).

## Stack / contraintes techniques (stable, rarement modifié)
Projet Python local, point d'entrée unique `run.py`. Architecture pensée pour le hot-reload (modification de code par l'agent → effet observable en relançant/rechargeant). Dashboard console texte (pygame minimal en option ultérieure). Aucun LLM intégré : jeu 100 % déterministe et scripté, agnostique à l'agent utilisé. Critères de victoire/progression lisibles dans le code.

## État actuel (réécrit intégralement à chaque /close)
Brainstorming et cadrage terminés (docs/PROJET.md, docs/PLAN_DEVELOPPEMENT.md, ROADMAP.md rédigés). Concept validé : Vaisseau-Écosystème, hybride Usine à Robots + Tour de Garde. MVP scopé (1 module + 1 vague, niveaux 1-4). Aucun code du jeu écrit — prochaine étape : Phase 0 (spike hot-reload).

## Décisions structurantes (append only — 10 entrées max, archiver au-delà)
- 2026-07-17 : Initialisation du protocole vibecoding.
- 2026-07-17 : Concept retenu — Vaisseau-Écosystème (hybride Usine à Robots + Tour de Garde), univers vaisseau-écosystème vivant à la dérive, hot-reload permanent.
- 2026-07-17 : Rôle de l'IA tranché — agent de codage réel du joueur (pas de LLM intégré au jeu), agnostique à l'outil.
- 2026-07-17 : MVP scopé — 1 module + 1 vague, niveaux pédagogiques 1 à 4. Extension "Mission & Audit" repoussée en post-MVP.
- 2026-07-17 : Plan de développement validé — 4 phases (spike hot-reload, moteur, contenu pédagogique, playtest) suivies dans ROADMAP.md.

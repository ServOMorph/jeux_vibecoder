# Vaisseau-Écosystème (nom provisoire) — Description du projet

## Vision & pitch

Vous êtes seul aux commandes d'un vaisseau-écosystème à la dérive dont les systèmes sont un chantier de code inachevé. En dirigeant votre agent IA de codage à coups de prompts précis, vous réparez, construisez et défendez votre arche vivante contre des vagues qui mettent votre code — et vos compétences de vibecoding — à l'épreuve.

Le jeu n'a pas d'interface de jeu autonome : **le jeu, c'est le code lui-même**. Le joueur reçoit un vrai projet Python doté d'un point d'entrée `run.py`. Il ne l'édite (quasiment) pas à la main : il ouvre son agent de codage IA habituel (Claude Code, Cursor, Copilot…) dans son propre environnement, et "joue" en écrivant des prompts dans le chat de cet agent. L'agent modifie les fichiers réels du projet ; le joueur relance `run.py` pour observer, en direct, le résultat concret de ce que l'agent a produit.

## Public cible & objectifs pédagogiques

**Public** : des développeurs qui découvrent les agents de codage IA — pas des débutants absolus en programmation, mais des débutants en *vibecoding*.

**Compétences enseignées, dans l'ordre d'apparition** :
- Formuler des prompts directs et précis
- Donner du contexte et poser des contraintes explicites
- Décomposer un objectif flou en sous-tâches promptables
- Lire et comprendre du code existant avant de le modifier
- Itérer et corriger à partir des sorties de l'agent
- Valider un résultat (demander des tests, relire le code généré) plutôt que de faire confiance aveuglément
- Gérer un agent sous pression (itération rapide, urgence)
- Arbitrer vitesse vs qualité et vivre les conséquences de la dette technique

## Concept de jeu

**Boucle de gameplay** (minute par minute) :
1. Observer l'état du vaisseau (dashboard texte / pygame minimal) : modules cassés, ressources, alerte de vague à venir.
2. Prioriser : réparer un module vital, préparer la défense, ou optimiser la production.
3. Écrire un prompt ciblé dans le chat de l'agent, sur un fichier précis.
4. L'agent modifie le code du projet.
5. Lancer `run.py` (**hot-reload**) et observer immédiatement le résultat.
6. Reprompter si le résultat ne correspond pas à l'intention, ou passer au module suivant.
7. Une vague arrive (timer visible) : les modules construits sont testés en conditions réelles, et toute dette technique bâclée craque sous la pression.
8. Bilan post-vague : nouvelle compétence débloquée, cycle suivant.

**Univers, thème, ton** : science-fiction contemplative. Le vaisseau est à la fois une arche générationnelle et une biosphère vivante à entretenir — on ne répare pas de simples machines, on maintient un écosystème. Ton oscillant entre solitude et espoir.

**Rôle de l'IA** : le joueur utilise son **véritable agent de codage** (Claude Code, Cursor, Copilot, etc.), dans son propre environnement de développement. Le jeu lui-même ne contient **aucun LLM intégré** : c'est un projet Python entièrement déterministe et scripté. Conséquences : coût nul pour le studio, fonctionnement possible hors-ligne (hormis l'agent lui-même), et **agnosticisme total** vis-à-vis de l'agent choisi par le joueur — n'importe quel outil de codage IA doit pouvoir jouer le jeu.

## Progression pédagogique (compétences par niveau)

| Niveau | Nom | Compétence introduite |
|---|---|---|
| 1 | Premier signal | Prompts simples et directs, sur un seul fichier |
| 2 | Contexte | Contraintes précises, dépendances entre fichiers |
| 3 | Découpage | Décomposer un objectif flou en sous-tâches promptables |
| 4 | Lecture de code | Comprendre du code legacy avant de le modifier (vaisseau en ruine) |
| 5 | Validation | Demander à l'agent d'écrire/lancer des tests, relire sa sortie |
| 6 | Itération sous pression | Reprompt rapide pendant une vague |
| 7 | Dette technique | Arbitrer vitesse vs qualité, en subir les conséquences différées |
| 8+ | *(réservé)* | Extension "Mission & Audit" — voir Idées en réserve |

Chaque niveau introduit **une** compétence nouvelle et nommée, sur le modèle de *The Farmer Was Replaced* qui débloque les concepts Python un par un.

## Périmètre MVP / Hors périmètre

**MVP** : un unique module à réparer + une vague unique. Dette technique visible sur ce module. Hot-reload fonctionnel via `run.py`. Agnostique à l'agent utilisé. Couvre les niveaux de progression 1 à 4.

**Hors périmètre (explicitement écarté, au moins pour le MVP)** :
- Vraie API LLM intégrée au jeu (le jeu reste 100 % déterministe)
- Multijoueur
- Leaderboard ou mode compétitif (concept "Arène de Prompts" écarté au vote)
- Extension "Mission & Audit" (modules en autonomie totale + audit du code ennemi)
- Interface graphique riche : on reste sur du texte ou du pygame minimal

## Contraintes techniques & choix pressentis

- Projet **Python local**, pas un jeu web autonome.
- Point d'entrée unique `run.py`.
- Architecture pensée pour le **hot-reload** : les modifications de code par l'agent doivent produire un effet observable en relançant `run.py`, sans friction.
- Le jeu doit rester jouable avec **n'importe quel agent de codage IA** (Claude Code, Cursor, Copilot…) — aucune dépendance à un outil précis.
- Dashboard/affichage : texte en console dans un premier temps, éventuellement pygame minimal ensuite.
- Critères de victoire et de progression doivent être **lisibles dans le code** par le joueur (et donc par son agent) — c'est une compétence enseignée, pas seulement une contrainte technique.

## Risques & inconnues à prototyper en premier

1. **Faisabilité du hot-reload** : le mécanisme technique qui permet d'observer en direct l'effet d'un code modifié par l'agent est la pierre angulaire du jeu — à valider en tout premier.
2. **Fun sur la durée** : le joueur n'a pas d'input direct dans le jeu (tout passe par le chat de son agent externe) — risque de friction ou d'ennui à vérifier tôt avec un playtest minimal.
3. **Équilibrage de la dette technique** : trouver le bon niveau de pénalité pour qu'elle soit instructive sans être punitive.
4. **Agnosticisme réel entre agents** : vérifier concrètement que le jeu fonctionne aussi bien avec Claude Code, Cursor, Copilot, etc.
5. **Concevoir l'échec "intéressant"** : les niveaux doivent faire échouer un prompt paresseux de façon pédagogique, sans jamais devenir frustrants ou arbitraires.

## Idées en réserve (issues du brainstorm)

- **Extension "Mission & Audit"** (variante C) : modules envoyés en autonomie totale sans correction possible en vol, et code ennemi lisible que le joueur doit auditer pour concevoir sa contre-mesure. Combine les concepts *Mission Contrôle* et *Code Détective*. À envisager après le MVP.
- Concept *Le Golem* : faire évoluer une créature dont le comportement est littéralement le code du projet — piste distincte, non retenue mais notée.
- Concept *La Startup* : simulation de CTO avec tickets clients et dette technique — partiellement absorbé dans le concept retenu (dette technique), reste en réserve pour une inspiration narrative plus poussée.
- Concept *Arène de Prompts* : katas à budget de prompts limité, écarté explicitement par l'utilisateur.
- Univers médiéval et univers spatial "pur" (sans écosystème vivant) : écartés au vote par points au profit du vaisseau-écosystème vivant.

## Prochaines étapes

1. **Prototyper le hot-reload** : valider techniquement qu'un fichier modifié par un agent de codage produit un effet observable immédiat via `run.py`.
2. **Construire le MVP** : un module + une vague, niveaux 1 à 4 de la progression pédagogique.
3. **Playtest minimal** pour vérifier le risque #2 (fun sans input direct).
4. → Passer à l'élaboration d'un **plan de développement** détaillé à partir de ce document, puis d'une **roadmap**.

---
*Document issu de la session de brainstorming du 2026-07-17 — voir `docs/brainstorm/session-2026-07-17.md` pour le détail complet du processus (divergence, SCAMPER, votes).*

# /brainstorm — Atelier de brainstorming guidé

Tu animes un atelier de brainstorming structuré avec l'utilisateur pour définir le projet : **un jeu pour apprendre à vibecoder**, dans l'esprit de *The Farmer Was Replaced* (qui enseigne Python en faisant programmer un drone agricole).

Sujet éventuel passé en argument : $ARGUMENTS (si vide, le sujet est le jeu d'apprentissage du vibecoding).

## Règles d'animation (valables tout du long)

- Tu es un **facilitateur**, pas un décideur : tu proposes, tu relances, tu reformules, mais c'est l'utilisateur qui tranche.
- **Une seule phase à la fois.** Ne passe à la phase suivante qu'après validation de l'utilisateur.
- **Pas de critique en phase de divergence** : toutes les idées sont notées, même farfelues. Le tri vient plus tard.
- Pose des questions **une par une ou par petits groupes** (utilise AskUserQuestion quand des options claires existent), jamais un mur de 15 questions.
- À la fin de chaque phase, affiche une **synthèse courte** de ce qui est acquis avant de continuer.
- Tiens à jour un fichier de travail `docs/brainstorm/session-<date>.md` où tu notes toutes les idées au fil de l'eau (rien ne doit être perdu).

## Phase 0 — Cadrage (5 min)

Avant de générer des idées, clarifie le problème avec l'utilisateur :

1. **Public cible** : qui apprend à vibecoder ? (débutants complets, devs qui découvrent les agents IA, enfants, etc.)
2. **Définition du "vibecoding" à enseigner** : quelles compétences concrètes ? (formuler un bon prompt, décomposer un problème, itérer sur les sorties de l'IA, relire/valider du code généré, gérer un agent, debugger avec l'IA…)
3. **Contraintes** : plateforme (web, desktop), techno envisagée, solo/multi, budget temps, jeu réel avec vraie IA intégrée ou IA simulée ?
4. Reformule le tout en **3 à 5 questions "Comment pourrions-nous…" (How Might We)** et fais valider la question principale.

## Phase 1 — Divergence : générer un maximum d'idées

Enchaîne ces techniques (propose-les, l'utilisateur peut en sauter) :

### 1a. Analyse du modèle (*The Farmer Was Replaced*)
Décompose ce qui fait marcher le jeu de référence : boucle de gameplay (coder → observer → optimiser), progression par déblocage de concepts un par un, tâche répétitive qui rend l'automatisation gratifiante, feedback visuel immédiat. Pour chaque mécanique, demande : **quel est l'équivalent pour le vibecoding ?**

### 1b. Crazy 8s (adapté)
Génère toi-même **8 concepts de jeu radicalement différents** en une passe rapide (une ligne chacun : pitch + boucle de gameplay). Demande à l'utilisateur d'en ajouter, puis de réagir à chauds : ❤️ / 🤔 / ❌ sur chacun.

### 1c. SCAMPER sur le(s) concept(s) préféré(s)
Passe le concept favori au crible : **S**ubstituer (autre univers que la ferme ?), **C**ombiner (mélanger deux concepts ?), **A**dapter (mécaniques d'autres jeux : incrémental, tower defense, roguelike ?), **M**odifier (amplifier une mécanique ?), **P**roposer d'autres usages, **É**liminer (simplifier au maximum ?), **R**enverser (et si le joueur était l'IA ?).

### 1d. Brainstorming inversé
« Comment faire un jeu qui **échouerait totalement** à enseigner le vibecoding ? » Liste les anti-patterns (trop de texte, pas de feedback, IA qui fait tout, progression plate…) puis inverse chacun en principe de design.

## Phase 2 — Convergence : choisir et affiner

1. Regroupe toutes les idées par thèmes (mind map textuelle dans le fichier de session).
2. **Vote par points** : l'utilisateur distribue 5 points sur les idées/mécaniques qui comptent le plus.
3. Évalue les 3 finalistes sur une grille simple : valeur pédagogique / fun / faisabilité (petit tableau).
4. Fais choisir **un concept principal** et note explicitement ce qui est écarté (dans une section "Idées en réserve").

## Phase 3 — Approfondissement du concept retenu

Travaille avec l'utilisateur jusqu'à pouvoir répondre à tout ceci :

- **Pitch** en une phrase.
- **Boucle de gameplay** principale (que fait le joueur minute par minute ?).
- **Progression pédagogique** : liste ordonnée des compétences de vibecoding enseignées, niveau par niveau (comme TFWR introduit les concepts Python un par un).
- **Rôle de l'IA** : vraie API LLM, IA simulée/scriptée, ou hybride ? Conséquences (coût, hors-ligne, triche).
- **Univers / thème / ton**.
- **Conditions de victoire, feedback, système de score ou de déblocage**.
- **Périmètre du MVP** : le plus petit jeu jouable qui enseigne déjà quelque chose.
- **Hors périmètre** (explicitement).
- **Risques principaux** et inconnues à prototyper en premier.

## Phase 4 — Livrable final (obligatoire)

Rédige `docs/PROJET.md` : la description de référence du projet. Structure imposée :

```markdown
# <Nom du jeu> — Description du projet
## Vision & pitch
## Public cible & objectifs pédagogiques
## Concept de jeu (boucle de gameplay, univers, rôle de l'IA)
## Progression pédagogique (compétences par niveau)
## Périmètre MVP / Hors périmètre
## Contraintes techniques & choix pressentis
## Risques & inconnues à prototyper
## Idées en réserve (issues du brainstorm)
## Prochaines étapes (→ plan de développement, → roadmap)
```

Ce fichier doit être **autosuffisant** : quelqu'un qui n'a pas assisté au brainstorm doit pouvoir en tirer un plan de développement puis une roadmap. Fais-le relire à l'utilisateur, intègre ses corrections, puis conclus en résumant les décisions clés et en proposant la suite (création du plan de développement).

# jeux_vibecoder — jeu pédagogique pour apprendre le vibecoding

**jeux_vibecoder** est un jeu Python inédit où le joueur pilote son propre agent de codage IA (Claude Code, Cursor, Copilot, etc.) à coups de prompts pour réparer, construire et défendre un **vaisseau-écosystème** dont les systèmes sont un vrai chantier de code inachevé. Le jeu n'a pas d'interface autonome : **le jeu, c'est le code lui-même**. Le joueur écrit des prompts dans le chat de son agent de codage habituel ; l'agent modifie les fichiers réels du projet ; le joueur relance `run.py` pour observer le résultat en direct.

Stack : **Python (stdlib uniquement)**, interface graphique **Tkinter** native, **aucune dépendance externe**, **aucun LLM intégré** — jeu 100 % déterministe et scripté, agnostique à l'agent de codage utilisé. Conçu pour apprendre le vibecoding compétence par compétence, par niveaux progressifs (prompt direct → contexte → découpage → lecture de code legacy).

## Prérequis

- **Python 3.10 ou plus récent** (le code utilise la syntaxe d'union de types `X | None`, PEP 604).
- `tkinter`, livré en standard avec les distributions officielles CPython (sous Linux, installer le paquet système si absent : `python3-tk` sous Debian/Ubuntu).
- Un agent de codage IA au choix (Claude Code, Cursor, Copilot, etc.) pour « jouer » en modifiant le code des modules.

Aucune dépendance Python externe (aucun `pip install` nécessaire).

## Installation

```bash
git clone https://github.com/ServOMorph/jeux_vibecoder.git
cd jeux_vibecoder
```

## Usage

```bash
python run.py
```

Ouvre le tableau de bord Tkinter : jauges d'oxygène / énergie / intégrité, état des modules, compte à rebours de la prochaine vague, niveau pédagogique en cours. Le tableau de bord console est également disponible comme fallback dans `vaisseau/moteur/boucle.py`.

Pour « jouer » : ouvrez votre agent de codage IA à la racine du dépôt, lisez le brief de niveau dans `vaisseau/JOURNAL_DE_BORD.md`, puis demandez à l'agent (par prompts) de réparer les modules ciblés dans `vaisseau/modules/`. Relancez `python run.py` après chaque modification pour observer l'effet — le moteur recharge le code sans redémarrage manuel (hot-reload).

## Comment ça marche

Le moteur tourne **tick par tick** (1 s par défaut). À chaque tick, la fonction `Partie.avancer()` (`vaisseau/moteur/boucle.py`) :

1. **Lit l'état** du vaisseau (`moteur/etat.py`) : trois ressources bornées — `oxygene`, `energie`, `integrite` — chacune avec un seuil critique.
2. **Détermine la vague** (`moteur/vagues.py`) : à partir du tick 20, trois vagues de charge croissante (1 → 2 → 3) ; pendant une vague, les ressources reçues par les modules sont dégradées et tout module en échec inflige des dégâts de coque.
3. **Recharge et exécute les modules** (`moteur/rechargeur.py`) : chaque module (`vaisseau/modules/*.py`) expose `produire(etat) -> int` ; le rechargeur relit le fichier à chaque tick, ce qui permet à l'agent IA d'éditer un module en direct et de voir l'effet au tick suivant (hot-reload). Si un module lève une exception ou refuse de compiler, il est marqué CASSE / EN ERREUR.
4. **Évalue le niveau courant** (`moteur/niveaux/`) : chaque niveau (1 à 4 dans le MVP) vérifie un critère déterministe (anti-paresse) sur le module cible ; en cas de réussite, la progression est persistée et le niveau suivant est débloqué.
5. **Persiste l'état** atomiquement dans `vaisseau/sauvegarde.json` (`moteur/sauvegarde.py`) : état, tick, niveaux terminés et déblocages survivent à un redémarrage.

Le tableau de bord Tkinter (`moteur/ui.py`) pilote cette même boucle via un minuteur ; `moteur/boucle.py` expose aussi un affichage console (`Partie.lancer`).

## Objectif pédagogique

Public : développeurs découvrant les **agents de codage IA** — pas des débutants en programmation, mais des débutants en *vibecoding*.

Compétences introduites niveau par niveau :

| Niveau | Compétence |
|---|---|
| 1 — Premier signal | Prompts simples et directs sur un seul fichier |
| 2 — Contexte | Contraintes précises, dépendances entre fichiers |
| 3 — Découpage | Décomposer un objectif flou en sous-tâches promptables |
| 4 — Lecture de code | Comprendre du code legacy avant de le modifier |

## Structure du projet

- `run.py` — point d'entrée unique du jeu.
- `vaisseau/moteur/` — cœur du moteur : `etat.py`, `vagues.py`, `rechargeur.py`, `boucle.py` (console), `ui.py` (Tkinter), `sauvegarde.py`, `score.py`, `niveaux/`.
- `vaisseau/modules/` — modules joueur que l'agent IA doit réparer : `balise.py`, `oxygene.py`, `energie.py`, `serre.py`, `defense.py`.
- `vaisseau/JOURNAL_DE_BORD.md` — briefs narratifs des niveaux (l'énoncé que lit le joueur).
- `vaisseau/tests/` — suite de tests du moteur (31 tests réussis à l'état actuel).
- `docs/` — `PROJET.md` (description de référence du concept), `PLAN_DEVELOPPEMENT.md`, `brainstorm/`.
- `ROADMAP.md`, `roadmap_phase1.md`, `roadmap_phase2.md`, `roadmap_ui.md` — suivi d'avancement par phase.

## État actuel

Phases 0 à 2 terminées, jalons J0, J1 et J2 validés. Les quatre niveaux sont terminables avec un agent de codage et leurs déblocages sont sauvegardés. La suite compte 31 tests réussis. Prochaine étape : phase 3 (playtest et équilibrage). Voir `CHANGELOG.md` pour le détail des versions.

## Licence

MIT — voir [`LICENSE`](LICENSE). Copyright (c) 2026 ServOMorph.

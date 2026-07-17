# Vaisseau-Écosystème — Plan de développement

> Document dérivé de [PROJET.md](PROJET.md). Objectif : passer du concept validé à un MVP jouable (un module + une vague, niveaux pédagogiques 1 à 4), en attaquant les risques dans l'ordre.

## Principe directeur

Les inconnues identifiées dans PROJET.md se prototypent **avant** de produire du contenu. L'ordre des phases suit l'ordre des risques : d'abord prouver que le hot-reload fonctionne (risque #1), ensuite prouver que c'est amusant (risque #2), et seulement après fabriquer les niveaux.

Rappel de la contrainte structurante : le joueur ne touche pas au code à la main — il pilote son agent IA. Donc **tout ce que le jeu affiche, vérifie ou récompense doit être lisible dans les fichiers du projet**, et le moteur du jeu doit survivre à du code arbitraire (bon, mauvais, cassé) écrit par un agent.

## Architecture cible du projet livré au joueur

```
vaisseau/                      ← le repo que le joueur reçoit
├── run.py                     ← point d'entrée unique : lance le jeu + hot-reload
├── moteur/                    ← code du jeu, PAS destiné à être modifié par le joueur
│   ├── boucle.py              ← boucle principale, ticks, timer de vague
│   ├── rechargeur.py          ← hot-reload des modules joueur (watch + import sécurisé)
│   ├── sandbox.py             ← exécution protégée du code joueur (erreurs capturées)
│   ├── dashboard.py           ← affichage console (état du vaisseau, jauges, alertes)
│   ├── vagues.py              ← définition et exécution des vagues
│   ├── dette.py               ← mesure de la dette technique des modules joueur
│   ├── score.py               ← score de clarté, sauvegarde de progression
│   └── niveaux/               ← définitions des niveaux (objectifs, critères lisibles)
│       ├── niveau_1.py
│       └── ...
├── modules/                   ← LA zone de jeu : fichiers que l'agent du joueur modifie
│   ├── oxygene.py             ← ex. module en ruine à réparer (niveau 4)
│   ├── energie.py
│   └── defense.py
├── JOURNAL_DE_BORD.md         ← narration + brief du niveau courant (≤ 3 lignes de consigne)
└── sauvegarde.json            ← progression (triche possible, assumée)
```

Décisions techniques pressenties :
- **Python pur, zéro dépendance obligatoire** pour le MVP (console texte). Pygame éventuel en post-MVP seulement.
- Hot-reload par surveillance des fichiers de `modules/` (mtime ou `watchdog` si nécessaire) + `importlib.reload` dans un try/except global : un module cassé affiche l'erreur dans le dashboard mais **ne tue jamais la boucle de jeu**.
- Le contrat entre moteur et modules joueur = des fonctions à signature imposée (ex. `def produire(etat) -> int`), documentées dans les docstrings du module en ruine. C'est ce contrat que l'agent du joueur doit découvrir en lisant le code.
- La dette technique est mesurée par des moyens simples et déterministes (ex. : absence de gestion d'erreur détectée à l'exécution sous conditions dégradées pendant les vagues — pas d'analyse statique sophistiquée au MVP).

---

## Phase 0 — Spike : prouver le hot-reload (risque #1)

**Objectif** : démontrer la boucle complète *l'agent modifie `modules/x.py` → effet visible en direct dans la console sans redémarrer `run.py`*.

Tâches :
1. Boucle de jeu minimale (tick chaque seconde, affichage console qui se rafraîchit).
2. Rechargeur : détection de modification de `modules/`, `importlib.reload`, capture de toute exception (syntaxe comprise) sans crash de la boucle.
3. Un module d'exemple `modules/oxygene.py` avec une fonction au contrat simple.
4. Test manuel réel : ouvrir Claude Code sur le repo, prompter une modification du module, constater l'effet en direct.

**Critère de sortie** : une vidéo/démo où l'on prompte "double la production d'oxygène" et où le chiffre change à l'écran sans relancer quoi que ce soit — y compris le cas où l'agent écrit du code cassé (le dashboard affiche l'erreur, le jeu continue).

**Si le hot-reload en continu s'avère trop fragile** : repli assumé sur un mode "relancer `run.py` reprend la partie où elle en était" (état persisté). Moins spectaculaire, toujours jouable — la décision se prend à la fin de cette phase, pas plus tard.

## Phase 1 — Moteur de jeu minimal

**Objectif** : transformer le spike en socle : état du vaisseau, ressources, timer de vague, une vague exécutable, dashboard lisible.

Tâches :
1. Modèle d'état du vaisseau (ressources : oxygène, énergie, intégrité de la coque).
2. Dashboard console : jauges, état des modules (OK / cassé / en erreur), compte à rebours de vague, dernier message d'erreur du code joueur.
3. Système de vagues : une vague scriptée qui sollicite les modules (montée de charge) et applique des dégâts si un module échoue.
4. Sandbox de la dette : pendant la vague, les modules sont appelés sous conditions dégradées (valeurs limites, entrées inattendues) — un code bâclé qui "tenait" en phase calme échoue ici. C'est l'implémentation concrète de la mécanique "Ruine & Dette".
5. Sauvegarde/reprise (`sauvegarde.json`).
6. Score de clarté : compter les rechargements de chaque module (proxy du nombre d'itérations de prompt), affichage non punitif.

**Critère de sortie** : une partie complète jouable à la main (sans contenu pédagogique) : réparer un module, survivre — ou non — à une vague, voir la dette craquer.

## Phase 2 — Contenu pédagogique : niveaux 1 à 4

**Objectif** : la progression du MVP, une compétence nommée par niveau, briefs ≤ 3 lignes dans `JOURNAL_DE_BORD.md`.

| Niveau | Compétence | Situation de jeu à construire |
|---|---|---|
| 1 — Premier signal | Prompt simple, un fichier | Rallumer la balise de détresse : une fonction vide à faire implémenter, contrat évident |
| 2 — Contexte | Contraintes et dépendances | Module énergie dépendant d'oxygène : le prompt sans contexte produit un module qui viole une contrainte visible |
| 3 — Découpage | Décomposer un objectif flou | "Rendez la serre opérationnelle" : objectif volontairement large, impossible en un prompt, 3 sous-systèmes à traiter |
| 4 — Lecture de code | Comprendre du legacy | Module en ruine : code existant tordu mais fonctionnel à moitié, le réécrire aveuglément casse une dépendance — il faut d'abord le faire lire par l'agent |

Tâches transverses :
1. Format de définition de niveau (`moteur/niveaux/`) : objectif, critères de victoire **lisibles dans le code**, déblocage du suivant.
2. Écriture des 4 niveaux + leur vérification déterministe.
3. Test anti-paresse sur chaque niveau : vérifier qu'un prompt du type "fais le niveau" échoue de façon instructive (spec ambiguë, contrainte cachée dans le code, critère précis). C'est un critère de recette, pas une option.
4. Narration minimale du journal de bord (ton : solitude et espoir).

**Critère de sortie** : les 4 niveaux se terminent en vibecodant réellement, et le test anti-paresse passe sur chacun.

## Phase 3 — Playtest & équilibrage (risques #2, #3, #4)

**Objectif** : vérifier que c'est amusant, jouable avec plusieurs agents, et bien dosé.

Tâches :
1. Auto-playtest complet avec Claude Code, puis avec au moins un autre agent (Cursor ou Copilot) — noter toute dépendance involontaire à un outil.
2. 2-3 playtests externes (développeurs découvrant les agents = le public cible), observation sans aide.
3. Équilibrage : durée des phases calmes, sévérité des vagues, dosage de la dette technique (instructive, pas punitive).
4. Corrections issues des playtests ; README d'installation (« clonez, ouvrez votre agent, lancez `run.py` »).

**Critère de sortie (= MVP terminé)** : un joueur cible finit les niveaux 1 à 4 sans aide extérieure, avec n'importe quel agent, et sait nommer ce qu'il a appris.

## Phase 4 — Post-MVP (non planifié en détail, rappel du réservé)

Dans l'ordre de valeur pressenti : niveaux 5-7 (validation, itération sous pression, dette technique avancée) → habillage pygame → extension "Mission & Audit" (variante C en réserve dans PROJET.md) → niveaux communautaires.

---

## Jalons récapitulatifs

| Jalon | Contenu | Décision associée |
|---|---|---|
| J0 | Spike hot-reload concluant | Go/no-go sur le hot-reload continu vs repli "reprise d'état" |
| J1 | Moteur jouable (1 module + 1 vague, sans pédagogie) | Valider la boucle de jeu ressentie |
| J2 | Niveaux 1-4 terminables | Valider la progression pédagogique |
| J3 | Playtests passés, MVP livrable | Go/no-go sur le post-MVP |

## Risques suivis (rappel PROJET.md → traitement)

| Risque | Traité en |
|---|---|
| #1 Hot-reload fragile | Phase 0 (spike + solution de repli explicite) |
| #2 Fun sans input direct | Phase 1 (J1 : boucle ressentie) puis Phase 3 (playtests) |
| #3 Équilibrage de la dette | Phase 1 (mécanique) + Phase 3 (dosage) |
| #4 Agnosticisme entre agents | Phase 0 (test Claude Code) + Phase 3 (second agent) |
| #5 Échec "intéressant" du prompt paresseux | Phase 2 (test anti-paresse comme critère de recette) |

## Prochaine étape

Démarrer la **Phase 0** : créer la structure du repo du jeu et le spike hot-reload. La roadmap datée pourra être posée une fois J0 franchi (c'est J0 qui conditionne le reste).

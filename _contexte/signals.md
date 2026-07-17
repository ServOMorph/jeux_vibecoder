# Signals — jeux_vibecoder   (MAJ 2026-07-17)

## Actions ouvertes
- [P1|ouvert] Démarrer la Phase 0 du plan de dev : spike hot-reload (structure repo jeu, `run.py`, `moteur/`, `modules/`) — fait quand: la démo "prompt → effet visible sans relancer" fonctionne, y compris cas de code cassé — réf: docs/PLAN_DEVELOPPEMENT.md (Phase 0), ROADMAP.md (Jalon J0)

## Questions ouvertes

## Échéances

## Blocages

## Contexte chaud
- Décision go/no-go hot-reload continu vs repli "reprise d'état" à trancher à l'issue du spike Phase 0 (critère déjà défini dans PLAN_DEVELOPPEMENT.md)

## Dernière session (2026-07-17)
<!-- Écrasé intégralement par /close. Synthèse < 25 lignes. -->
# Session du 2026-07-17

## Décisions prises
- Concept retenu : Vaisseau-Écosystème (hybride Usine à Robots + Tour de Garde), univers vaisseau-écosystème vivant à la dérive
- MVP défini : 1 module + 1 vague, niveaux pédagogiques 1 à 4
- Rôle de l'IA tranché : agent de codage réel du joueur, jeu 100 % déterministe, agnostique à l'agent
- Plan de dev en 4 phases (spike hot-reload → moteur → contenu pédagogique → playtest) + post-MVP en réserve

## Livrables produits ou modifiés
- docs/brainstorm/session-2026-07-17.md : créé
- docs/PROJET.md : créé
- docs/PLAN_DEVELOPPEMENT.md : créé
- ROADMAP.md : créé
- README.md : créé
- CHANGELOG.md : créé (v0.1)

## Hypothèses validées / invalidées
- EN ATTENTE : faisabilité du hot-reload continu (rien codé, à prototyper en Phase 0)
- EN ATTENTE : fun sans input direct dans le jeu (à vérifier en playtest, Phase 3)

## Prochaine étape exacte
Créer la structure du repo du jeu (`run.py`, `moteur/`, `modules/`) et réaliser le spike hot-reload (Phase 0 du plan de dev).

## Question bloquante pour la session suivante
Aucune

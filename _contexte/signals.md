# Signals — jeux_vibecoder   (MAJ 2026-07-17)

## Actions ouvertes
- [P1|ouvert] Construire le format de définition de niveau et le niveau 1 — fait quand: un niveau « Premier signal » définit un objectif, des critères de victoire lisibles et un déblocage déterministe ; réf: ROADMAP.md (phase 2) ; docs/PLAN_DEVELOPPEMENT.md (phase 2)

## Questions ouvertes

## Échéances

## Blocages

## Contexte chaud
- Jalon J0 franchi : hot-reload continu validé, pas de repli nécessaire.
- Jalon J1 franchi : la boucle complète panne, dégâts, correction hot-reload et fin de vague a été validée manuellement.
- Contrat module généralisé : `produire(etat) -> int`, un module par ressource (`oxygene`, `energie`, `defense` -> intégrité). Modules `energie.py` et `defense.py` retournent 0 par défaut (pas encore de contenu pédagogique).
- La vague unique se déroule aux ticks 20 à 22, avec une charge de 1 à 3 appels par module et 10 dégâts de coque par module défaillant.
- Pendant la vague, les modules reçoivent un état dégradé (ressources à 0 et `signal_externe=None`) sans modifier l'état réel affiché du vaisseau.
- `run.py` ouvre le tableau de bord Tkinter ; le rechargeur résout les modules indépendamment du dossier courant.
- Le mode développeur déclenche immédiatement la vague ; la suite moteur et UI contient 16 tests.

## Dernière session (2026-07-17)
<!-- Écrasé intégralement par /close. Synthèse < 25 lignes. -->
# Session du 2026-07-17

## Décisions prises
- Le tableau de bord Tkinter devient l'interface par défaut ; le moteur reste déterministe et hot-reloadable.
- Le jalon J1 est validé manuellement ; un bouton de vague immédiate est ajouté pour les tests de développement.

## Livrables produits ou modifiés
- `vaisseau/moteur/ui.py` : tableau de bord Tkinter avec ressources, modules, vague et commandes de partie.
- `vaisseau/moteur/boucle.py` : partie pilotable tour par tour et préparation de vague en mode développement.
- `run.py` : point d'entrée vers l'interface graphique.
- `vaisseau/tests/` : tests de partie et d'interface ajoutés ; 16 tests réussis.

## Hypothèses validées / invalidées
- VALIDE : le hot-reload, la panne sous vague, les dégâts et la correction en cours de partie sont visibles dans l'interface.
- VALIDE : le déclenchement direct de vague reproduit le tick 20 sans attendre le compte à rebours.
- EN ATTENTE : contenu pédagogique des niveaux 1 à 4.

## Prochaine étape exacte
Créer le format de niveau, puis implémenter le niveau 1 « Premier signal » avec ses critères de victoire déterministes.

## Question bloquante pour la session suivante
Aucune

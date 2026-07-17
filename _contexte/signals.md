# Signals — jeux_vibecoder   (MAJ 2026-07-17)

## Actions ouvertes
- [P1|ouvert] Valider le jalon J1 par une partie complète manuelle — fait quand: un module fragile est rechargé, échoue pendant la vague puis les dégâts et le dashboard sont constatés jusqu'à la fin de la vague — réf: ROADMAP.md (jalon J1) ; vaisseau/moteur/vagues.py ; vaisseau/moteur/boucle.py

## Questions ouvertes

## Échéances

## Blocages

## Contexte chaud
- Jalon J0 franchi : hot-reload continu validé, pas de repli nécessaire.
- Les sous-phases 1a à 1f de la phase 1 sont livrées et couvertes par 11 tests ; le jalon J1 demande encore une validation manuelle complète.
- Contrat module généralisé : `produire(etat) -> int`, un module par ressource (`oxygene`, `energie`, `defense` -> intégrité). Modules `energie.py` et `defense.py` retournent 0 par défaut (pas encore de contenu pédagogique).
- La vague unique se déroule aux ticks 20 à 22, avec une charge de 1 à 3 appels par module et 10 dégâts de coque par module défaillant.
- Pendant la vague, les modules reçoivent un état dégradé (ressources à 0 et `signal_externe=None`) sans modifier l'état réel affiché du vaisseau.
- `run.py` est le point d'entrée à la racine ; le rechargeur résout les modules indépendamment du dossier courant.
- La suite de tests du moteur contient 11 tests, dont une panne pendant vague, une reprise de sauvegarde et le score d'itérations.

## Dernière session (2026-07-17)
<!-- Écrasé intégralement par /close. Synthèse < 25 lignes. -->
# Session du 2026-07-17

## Décisions prises
- `run.py` devient le point d'entrée unique à la racine du projet ; son exécution depuis l'IDE est validée.
- La sauvegarde, la reprise et le score d'itérations sont intégrés au moteur sans effet punitif.

## Livrables produits ou modifiés
- `vaisseau/moteur/sauvegarde.py` : sauvegarde atomique et chargement de l'état, du tick et de la progression.
- `vaisseau/moteur/score.py` : compteur d'itérations par module.
- `run.py` : point d'entrée déplacé à la racine ; `vaisseau/moteur/rechargeur.py` utilise des chemins absolus.
- `vaisseau/tests/` : tests de sauvegarde, reprise, score et affichage ajoutés ; 11 tests réussis.

## Hypothèses validées / invalidées
- VALIDE : la sauvegarde reprend le tick suivant et conserve l'état du vaisseau.
- VALIDE : le lancement depuis la racine fonctionne et localise les modules correctement.
- EN ATTENTE : validation manuelle complète du jalon J1.

## Prochaine étape exacte
Lancer `python run.py`, introduire un module fragile avant la vague et constater sa panne, les dégâts et la fin de vague.

## Question bloquante pour la session suivante
Aucune

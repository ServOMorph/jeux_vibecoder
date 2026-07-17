# Signals — jeux_vibecoder   (MAJ 2026-07-17)

## Actions ouvertes
- [P1|ouvert] Sous-phase 1e : sauvegarde / reprise — fait quand: `sauvegarde.json` conserve l'état, le tick et la progression, puis est rechargé au lancement lorsqu'il existe — réf: roadmap_phase1.md (section 1e) ; vaisseau/moteur/etat.py ; vaisseau/moteur/boucle.py

## Questions ouvertes

## Échéances

## Blocages

## Contexte chaud
- Jalon J0 franchi : hot-reload continu validé, pas de repli nécessaire.
- Phase 1 découpée en sous-phases dans `roadmap_phase1.md` (1a à 1f), avec checkpoint `/compact` après chacune. Les sous-phases 1a à 1d sont terminées ; 1e est prête à démarrer.
- Contrat module généralisé : `produire(etat) -> int`, un module par ressource (`oxygene`, `energie`, `defense` -> intégrité). Modules `energie.py` et `defense.py` retournent 0 par défaut (pas encore de contenu pédagogique).
- La vague unique se déroule aux ticks 20 à 22, avec une charge de 1 à 3 appels par module et 10 dégâts de coque par module défaillant.
- Pendant la vague, les modules reçoivent un état dégradé (ressources à 0 et `signal_externe=None`) sans modifier l'état réel affiché du vaisseau.
- La suite de tests du moteur contient 6 tests, dont une panne pendant vague et un module fragile qui échoue uniquement sous pression.

## Dernière session (2026-07-17)
<!-- Écrasé intégralement par /close. Synthèse < 25 lignes. -->
# Session du 2026-07-17

## Décisions prises
- La première vague est déterministe : ticks 20 à 22, charge progressive de 1 à 3 et 10 dégâts de coque par module défaillant.
- Les modules sont testés pendant la vague avec des ressources à 0 et un `signal_externe` à `None`, sans altérer l'état réel du vaisseau.

## Livrables produits ou modifiés
- `vaisseau/moteur/vagues.py` : définition et exécution de la vague scriptée.
- `vaisseau/moteur/boucle.py` : charge progressive, conditions dégradées, dégâts et affichage de vague réelle.
- `vaisseau/moteur/rechargeur.py` : erreur de chargement conservée jusqu'à la réparation du module.
- `vaisseau/tests/test_vagues.py` : couverture de la vague, des dégâts et de la dette.
- Roadmaps, README et changelog : état de session mis à jour.

## Hypothèses validées / invalidées
- VALIDE : une vague applique une charge progressive et des dégâts à l'intégrité lorsqu'un module échoue.
- VALIDE : un code fonctionnel à l'état nominal peut échouer uniquement sous les conditions dégradées de la vague.
- EN ATTENTE : sauvegarde / reprise et score de clarté.

## Prochaine étape exacte
Sous-phase 1e : enregistrer l'état, le tick et la progression dans `sauvegarde.json`, puis le charger au lancement s'il existe.

## Question bloquante pour la session suivante
Aucune

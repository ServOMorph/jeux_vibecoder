# Signals — jeux_vibecoder (MAJ 2026-07-17)

## Actions ouvertes
- [P1|ouvert] Finaliser la recette J2 et la narration des niveaux — fait quand: les quatre briefs du journal respectent trois lignes maximum et une recette valide le parcours complet, les déblocages et les quatre tests anti-paresse ; réf: `roadmap_phase2.md` (2e), `vaisseau/moteur/niveaux/`, `vaisseau/tests/test_niveaux.py`

## Questions ouvertes

## Échéances

## Blocages

## Contexte chaud
- Jalon J0 franchi : hot-reload continu validé, pas de repli nécessaire.
- Jalon J1 franchi : la boucle complète panne, dégâts, correction hot-reload et fin de vague a été validée manuellement.
- Les niveaux 1 à 4 ont un critère de victoire déterministe, une progression persistée et un test anti-paresse dédié.
- Les niveaux actifs ciblent successivement la balise, l’énergie, la serre et la défense ; le tableau de bord affiche leur objectif.
- La vague unique se déroule aux ticks 20 à 22, avec une charge de 1 à 3 appels par module et 10 dégâts de coque par module défaillant.
- La suite moteur et UI compte 30 tests réussis.

## Dernière session (2026-07-17)
<!-- Écrasé intégralement par /close. Synthèse < 25 lignes. -->
# Session du 2026-07-17

## Décisions prises
- Les niveaux utilisent une définition commune, une vérification déterministe et un déblocage persisté.
- Les quatre compétences MVP sont incarnées par les niveaux Premier signal, Contexte, Découpage et Lecture de code.

## Livrables produits ou modifiés
- `vaisseau/moteur/niveaux/` : format commun et définitions des quatre niveaux.
- `vaisseau/modules/` : balise, serre et contrats pédagogiques énergie, oxygène et défense.
- `vaisseau/moteur/boucle.py` et `ui.py` : progression de niveau et objectif affiché.
- `vaisseau/tests/` : recette de progression et tests anti-paresse ; 30 tests réussis.

## Hypothèses validées / invalidées
- VALIDE : les critères de victoire et déblocages sont déterministes et persistés dans la sauvegarde.
- VALIDE : un retour constant, une réponse globale ou une réécriture legacy aveugle échouent de façon explicite.
- EN ATTENTE : narration complète des niveaux et recette J2 du parcours joueur.

## Prochaine étape exacte
Écrire les briefs de journal pour les quatre niveaux, puis exécuter la recette J2 du parcours complet.

## Question bloquante pour la session suivante
Aucune

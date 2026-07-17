# Signals — jeux_vibecoder   (MAJ 2026-07-17)

## Actions ouvertes
- [P1|ouvert] Sous-phase 1c : système de vagues (montée de charge scriptée, dégâts intégrité si module échoue, timer déjà en place en 1b) — fait quand: une vague scriptée s'exécute, inflige des dégâts à l'intégrité en cas d'échec de module, et le timer du dashboard reflète le vrai déclenchement — réf: roadmap_phase1.md (section 1c)

## Questions ouvertes

## Échéances

## Blocages

## Contexte chaud
- Jalon J0 franchi : hot-reload continu validé, pas de repli nécessaire.
- Phase 1 découpée en sous-phases dans `roadmap_phase1.md` (1a à 1f), avec checkpoint `/compact` après chacune. 1a et 1b terminées, 1c prête à démarrer.
- Contrat module généralisé : `produire(etat) -> int`, un module par ressource (`oxygene`, `energie`, `defense` -> intégrité). Modules `energie.py` et `defense.py` retournent 0 par défaut (pas encore de contenu pédagogique).
- Dashboard (`boucle.py`) affiche jauges ASCII, statut module (OK/CASSE/EN ERREUR) et dernière erreur persistée par module. Le compte à rebours de vague affiché est un placeholder (`INTERVALLE_VAGUE_TICKS = 20`, simple modulo) : la vraie mécanique de vague (1c) doit s'y brancher, pas le redéfinir en parallèle.

## Dernière session (2026-07-17)
<!-- Écrasé intégralement par /close. Synthèse < 25 lignes. -->
# Session du 2026-07-17

## Décisions prises
- Aucune décision structurante nouvelle (implémentation de la sous-phase 1b prévue par la roadmap)

## Livrables produits ou modifiés
- vaisseau/moteur/boucle.py : dashboard complet (jauges ASCII, statut par module, compte à rebours de vague placeholder, dernière erreur persistée par module)
- roadmap_phase1.md : sous-phase 1b marquée [FAIT]

## Hypothèses validées / invalidées
- VALIDE : rendu du dashboard vérifié manuellement (jauges, statuts OK/EN ERREUR, dernière erreur affichée)

## Prochaine étape exacte
Sous-phase 1c : système de vagues (montée de charge scriptée, dégâts à l'intégrité si un module échoue, brancher le timer déjà affiché).

## Question bloquante pour la session suivante
Aucune

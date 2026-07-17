# Signals — jeux_vibecoder   (MAJ 2026-07-17)

## Actions ouvertes
- [P1|ouvert] Démarrer la Phase 1 du plan de dev : moteur de jeu minimal (état du vaisseau, dashboard, vagues, dette, sauvegarde, score) — fait quand: une partie complète est jouable à la main (réparer un module, subir une vague, voir la dette craquer) — réf: docs/PLAN_DEVELOPPEMENT.md (Phase 1), ROADMAP.md (Jalon J1)

## Questions ouvertes

## Échéances

## Blocages

## Contexte chaud
- Jalon J0 franchi : hot-reload continu validé (repo `vaisseau/` créé et fonctionnel : run.py, moteur/boucle.py, moteur/rechargeur.py, modules/oxygene.py). Aucun repli "reprise d'état" nécessaire. Jalon J1 conditionne le ressenti de fun de la boucle de jeu (risque #2).

## Dernière session (2026-07-17)
<!-- Écrasé intégralement par /close. Synthèse < 25 lignes. -->
# Session du 2026-07-17

## Décisions prises
- Jalon J0 tranché : hot-reload continu retenu (spike concluant, pas de repli sur "reprise d'état")

## Livrables produits ou modifiés
- vaisseau/run.py : créé
- vaisseau/moteur/boucle.py : créé
- vaisseau/moteur/rechargeur.py : créé
- vaisseau/modules/oxygene.py : créé
- vaisseau/JOURNAL_DE_BORD.md : créé
- vaisseau/.gitignore : créé
- ROADMAP.md : Phase 0 cochée, Jalon J0 renseigné
- _contexte/signals.md : mis à jour

## Hypothèses validées / invalidées
- VALIDE : faisabilité du hot-reload continu (modification de valeur répercutée en direct, erreur de syntaxe volontaire capturée sans crash de la boucle)
- EN ATTENTE : fun sans input direct dans le jeu (à vérifier en playtest, Phase 3)

## Prochaine étape exacte
Démarrer la Phase 1 : modèle d'état du vaisseau, dashboard console complet, système de vagues, mécanique de dette, sauvegarde, score de clarté.

## Question bloquante pour la session suivante
Aucune

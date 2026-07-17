# Roadmap — Vaisseau-Écosystème

> Suivi d'avancement du projet. Référence : [docs/PROJET.md](docs/PROJET.md) (concept) et [docs/PLAN_DEVELOPPEMENT.md](docs/PLAN_DEVELOPPEMENT.md) (détail des phases).
> Convention : `[ ]` à faire · `[x]` fait · `[~]` en cours. Mettre à jour ce fichier à chaque session de travail.

**État global : 🟡 Phase 2 en cours (voir [roadmap_phase2.md](roadmap_phase2.md))** *(mis à jour le 2026-07-17)*

---

## Phase 0 — Spike hot-reload (risque #1)

- [x] Structure du repo du jeu (`run.py`, `moteur/`, `modules/`, `JOURNAL_DE_BORD.md`)
- [x] Boucle de jeu minimale (tick 1 s, affichage console rafraîchi)
- [x] Rechargeur : détection des modifications de `modules/` + `importlib.reload` + capture de toute exception sans crash
- [x] Module d'exemple `modules/oxygene.py` avec contrat simple
- [x] Test réel avec Claude Code : prompter une modification, constater l'effet en direct
- [x] Cas d'erreur vérifié : code cassé par l'agent → erreur affichée au dashboard, le jeu continue

**🏁 Jalon J0** — [x] Décision go/no-go : hot-reload continu **ou** repli "reprise d'état au relancement"
> Décision prise : hot-reload continu retenu. Test manuel concluant — modification de `modules/oxygene.py` (changement de valeur puis erreur de syntaxe volontaire) répercutée en direct sans redémarrage de `run.py`, aucun crash de la boucle, ancienne valeur conservée pendant l'erreur.

---

## Phase 1 — Moteur de jeu minimal

> Suivi détaillé dans [roadmap_phase1.md](roadmap_phase1.md).

- [x] Modèle d'état du vaisseau (oxygène, énergie, intégrité de la coque)
- [x] Dashboard console : jauges, état des modules, compte à rebours de vague, dernière erreur du code joueur
- [x] Système de vagues : une vague scriptée (montée de charge, dégâts si un module échoue)
- [x] Mécanique de dette : appel des modules sous conditions dégradées pendant la vague
- [x] Sauvegarde / reprise (`sauvegarde.json`)
- [x] Score de clarté (compteur de rechargements par module, non punitif)

**🏁 Jalon J1** — [x] Partie complète jouable (réparer un module, subir une vague, voir la dette craquer) ; boucle validée manuellement

---

## Phase 2 — Contenu pédagogique : niveaux 1 à 4

> Suivi détaillé dans [roadmap_phase2.md](roadmap_phase2.md).

- [x] Format de définition de niveau (objectif, critères de victoire lisibles dans le code, déblocage)
- [x] Niveau 1 — Premier signal (prompt simple, un fichier)
- [x] Niveau 2 — Contexte (contraintes et dépendances)
- [x] Niveau 3 — Découpage (objectif flou → sous-tâches)
- [x] Niveau 4 — Lecture de code (module legacy en ruine)
- [x] Test anti-paresse passé sur chacun des 4 niveaux ("fais le niveau" échoue de façon instructive)
- [ ] Narration du journal de bord (briefs ≤ 3 lignes, ton solitude/espoir)

**🏁 Jalon J2** — [ ] Les 4 niveaux se terminent en vibecodant réellement

---

## Phase 3 — Playtest & équilibrage

- [ ] Auto-playtest complet avec Claude Code
- [ ] Playtest avec un second agent (Cursor ou Copilot) — aucune dépendance involontaire à un outil
- [ ] 2-3 playtests externes avec le public cible (observation sans aide)
- [ ] Équilibrage : durée des phases calmes, sévérité des vagues, dosage de la dette
- [ ] Corrections issues des playtests
- [ ] README d'installation (« clonez, ouvrez votre agent, lancez `run.py` »)

**🏁 Jalon J3 = MVP livrable** — [ ] Un joueur cible finit les niveaux 1-4 sans aide, avec n'importe quel agent, et sait nommer ce qu'il a appris

---

## Phase 4 — Post-MVP *(non planifiée en détail — ordre de valeur pressenti)*

- [ ] Niveaux 5-7 (validation, itération sous pression, dette technique avancée)
- [ ] Habillage pygame
- [ ] Extension "Mission & Audit" (variante C en réserve dans PROJET.md)
- [ ] Niveaux communautaires

---

## Journal des jalons

| Jalon | Date | Décision / remarque |
|---|---|---|
| J0 | 2026-07-17 | Hot-reload continu validé, pas de repli nécessaire |
| J1 | 2026-07-17 | Panne sous vague, dégâts, correction hot-reload et fin de vague validées manuellement dans l'interface Tkinter |
| J2 | — | |
| J3 | — | |

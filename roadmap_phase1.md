# Roadmap — Phase 1 : Moteur de jeu minimal

> Référence : docs/PLAN_DEVELOPPEMENT.md (Phase 1), ROADMAP.md (Jalon J1)
> Critère de sortie global : une partie complète jouable à la main (réparer un module, subir une vague, voir la dette craquer).

---

## 1a — Modèle d'état du vaisseau [FAIT]

- [x] Structure d'état centralisée : oxygène, énergie, intégrité de la coque (valeurs, seuils critiques)
- [x] Généraliser `boucle.py` pour piloter l'état via les modules (au lieu du seul `oxygene` en dur)
- [x] Modules `energie.py` et `defense.py` (contrats simples, même esprit que `oxygene.py`)
- [x] Tests manuels : chaque module influence bien l'état correspondant

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## 1b — Dashboard console complet [FAIT]

- [x] Jauges (oxygène, énergie, intégrité)
- [x] État de chaque module (OK / cassé / en erreur)
- [x] Compte à rebours de la prochaine vague
- [x] Dernière erreur du code joueur affichée

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## 1c — Système de vagues [FAIT]

- [x] Une vague scriptée : montée de charge sur les modules
- [x] Dégâts à l'intégrité de la coque si un module échoue pendant la vague
- [x] Timer de vague intégré au dashboard (1b)

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## 1d — Mécanique de dette [FAIT]

- [x] Appel des modules sous conditions dégradées pendant la vague (valeurs limites, entrées inattendues)
- [x] Un code bâclé qui « tenait » en phase calme échoue sous charge

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## 1e — Sauvegarde / reprise [FAIT]

- [x] `sauvegarde.json` : état du vaisseau, tick, progression
- [x] Chargement au lancement si le fichier existe

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## 1f — Score de clarté [FAIT]

- [x] Compteur de rechargements par module (proxy du nombre d'itérations de prompt)
- [x] Affichage non punitif dans le dashboard

**🏁 Jalon J1 [FAIT]** — Partie complète jouable : panne sous vague, dégâts, correction hot-reload et fin de vague validées manuellement.

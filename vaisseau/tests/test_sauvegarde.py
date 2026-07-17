import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from moteur import boucle
from moteur import sauvegarde


class SauvegardeTest(unittest.TestCase):
    def test_enregistrer_et_charger_conservent_etat_tick_et_progression(self):
        with tempfile.TemporaryDirectory() as dossier:
            chemin = Path(dossier) / "sauvegarde.json"
            etat = {"oxygene": 75, "energie": 50, "integrite": 90}
            progression = {"vague_initiale_terminee": True}

            sauvegarde.enregistrer(etat, 23, progression, chemin)

            self.assertEqual(
                sauvegarde.charger(chemin),
                {"etat": etat, "tick": 23, "progression": progression},
            )
            self.assertEqual(json.loads(chemin.read_text(encoding="utf-8"))["tick"], 23)

    def test_charger_retourne_none_en_absence_de_sauvegarde(self):
        with tempfile.TemporaryDirectory() as dossier:
            chemin = Path(dossier) / "sauvegarde.json"

            self.assertIsNone(sauvegarde.charger(chemin))

    def test_la_boucle_reprend_au_tick_suivant_de_la_sauvegarde(self):
        reprise = {
            "etat": {"oxygene": 75, "energie": 50, "integrite": 90},
            "tick": 19,
            "progression": {"vague_initiale_terminee": False},
        }
        affichages = []

        def afficher(tick, vaisseau, statuts, erreurs, vague, degats):
            affichages.append((tick, vaisseau.copy(), vague))

        with (
            patch.object(boucle.rechargeur, "charger"),
            patch.object(boucle.rechargeur, "verifier_et_recharger", return_value=(None, None)),
            patch.object(boucle.sauvegarde, "charger", return_value=reprise),
            patch.object(boucle.sauvegarde, "enregistrer") as enregistrer,
            patch.object(boucle, "afficher", side_effect=afficher),
            patch.object(boucle.time, "sleep", side_effect=StopIteration),
        ):
            with self.assertRaises(StopIteration):
                boucle.lancer()

        self.assertEqual(affichages[0][0], 20)
        self.assertEqual(affichages[0][1], reprise["etat"])
        self.assertIsNotNone(affichages[0][2])
        enregistrer.assert_called_once_with(
            reprise["etat"], 20, {"vague_initiale_terminee": False}
        )

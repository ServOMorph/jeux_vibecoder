import unittest

from moteur import ui


class NiveauInterfaceTest(unittest.TestCase):
    def test_texte_niveau_affiche_l_objectif_et_le_statut(self):
        niveau = {"titre": "Premier signal", "objectif": "Rallumer la balise.", "reussi": False}

        texte = ui.texte_niveau(niveau)

        self.assertIn("PREMIER SIGNAL", texte)
        self.assertIn("EN COURS", texte)

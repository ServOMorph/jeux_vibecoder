import unittest

from moteur import ui
from moteur import vagues


class InterfaceTest(unittest.TestCase):
    def test_texte_vague_signale_la_phase_active(self):
        self.assertIn("VAGUE ACTIVE", ui.texte_vague(20, vagues.active(20)))
        self.assertIn("19", ui.texte_vague(1, None))
        self.assertIn("TERMINÉE", ui.texte_vague(23, None))

    def test_statut_module_reconnait_les_erreurs(self):
        sain = {"erreur_reload": None, "erreur_appel": None}
        appel_en_erreur = {"erreur_reload": None, "erreur_appel": RuntimeError("panne")}
        code_casse = {"erreur_reload": SyntaxError("erreur"), "erreur_appel": None}

        self.assertEqual(ui.statut_module(sain)[0], "OPÉRATIONNEL")
        self.assertEqual(ui.statut_module(appel_en_erreur)[0], "EN ERREUR")
        self.assertEqual(ui.statut_module(code_casse)[0], "CODE CASSÉ")

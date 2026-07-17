import unittest
from unittest.mock import patch

from moteur import boucle


class PartieTest(unittest.TestCase):
    def test_nouvelle_partie_commence_avec_un_vaisseau_intact(self):
        partie = boucle.Partie.nouvelle()

        self.assertEqual(partie.tick, 0)
        self.assertEqual(partie.vaisseau, {"oxygene": 100, "energie": 100, "integrite": 100})
        self.assertFalse(partie.progression["vague_initiale_terminee"])

    def test_un_tour_retourne_les_donnees_pour_l_interface(self):
        class ModuleSain:
            @staticmethod
            def produire(etat):
                return 0

        partie = boucle.Partie.nouvelle()
        with (
            patch.object(boucle.rechargeur, "verifier_et_recharger", return_value=(ModuleSain(), None)),
            patch.object(boucle.sauvegarde, "enregistrer"),
        ):
            tour = partie.avancer()

        self.assertEqual(tour["tick"], 1)
        self.assertEqual(tour["vaisseau"], partie.vaisseau)
        self.assertEqual(set(tour["statuts"]), set(boucle.MODULES))

    def test_le_mode_dev_prepare_le_premier_tick_de_vague(self):
        partie = boucle.Partie.nouvelle()

        partie.preparer_vague_dev()

        self.assertEqual(partie.tick, 19)
        self.assertFalse(partie.progression["vague_initiale_terminee"])

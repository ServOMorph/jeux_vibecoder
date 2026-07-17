import unittest
from unittest.mock import patch

from moteur import boucle
from moteur import vagues


class VaguesTest(unittest.TestCase):
    def test_la_vague_progresse_sur_trois_ticks(self):
        self.assertEqual(vagues.active(20)["charge"], 1)
        self.assertEqual(vagues.active(21)["charge"], 2)
        self.assertEqual(vagues.active(22)["charge"], 3)
        self.assertIsNone(vagues.active(23))

    def test_le_compte_a_rebours_vise_le_vrai_depart(self):
        self.assertEqual(vagues.ticks_avant_prochaine(1), 19)
        self.assertEqual(vagues.ticks_avant_prochaine(19), 1)
        self.assertIsNone(vagues.ticks_avant_prochaine(20))

    def test_les_degats_ne_comptent_qu_une_fois_par_module(self):
        vague = vagues.active(20)
        self.assertEqual(vagues.degats(vague, ["oxygene", "oxygene", "defense"]), 20)

    def test_la_vague_expose_des_conditions_degradees_sans_modifier_l_etat_reel(self):
        etat_reel = {"tick": 20, "oxygene": 100, "energie": 100, "integrite": 100}
        etat_degrade = vagues.etat_sous_charge(etat_reel, vagues.active(20))

        self.assertEqual(etat_reel["energie"], 100)
        self.assertEqual(etat_degrade["oxygene"], 0)
        self.assertEqual(etat_degrade["energie"], 0)
        self.assertEqual(etat_degrade["integrite"], 0)
        self.assertIsNone(etat_degrade["signal_externe"])

    def test_un_module_en_erreur_subit_des_degats_pendant_la_vague(self):
        class ModuleSain:
            @staticmethod
            def produire(etat):
                return 0

        class ModuleDefaillant:
            @staticmethod
            def produire(etat):
                raise RuntimeError("panne")

        module_sain = ModuleSain()
        module_defaillant = ModuleDefaillant()
        affichages = []

        def verifier(nom):
            if nom == "defense":
                return module_defaillant, None
            return module_sain, None

        def afficher(tick, vaisseau, statuts, erreurs, vague, degats):
            affichages.append((vaisseau.copy(), vague, degats))

        with (
            patch.object(boucle.vagues, "TICK_DEPART", 1),
            patch.object(boucle.rechargeur, "charger"),
            patch.object(boucle.rechargeur, "verifier_et_recharger", side_effect=verifier),
            patch.object(boucle.sauvegarde, "charger", return_value=None),
            patch.object(boucle.sauvegarde, "enregistrer"),
            patch.object(boucle, "afficher", side_effect=afficher),
            patch.object(boucle.time, "sleep", side_effect=StopIteration),
        ):
            with self.assertRaises(StopIteration):
                boucle.lancer()

        vaisseau, vague, degats = affichages[0]
        self.assertIsNotNone(vague)
        self.assertEqual(degats, 10)
        self.assertEqual(vaisseau["integrite"], 90)

    def test_un_code_fragile_fonctionne_hors_vague_mais_echoue_sous_pression(self):
        class ModuleFragile:
            @staticmethod
            def produire(etat):
                return 10 // etat["energie"]

        class ModuleSain:
            @staticmethod
            def produire(etat):
                return 0

        module_fragile = ModuleFragile()
        module_sain = ModuleSain()
        affichages = []

        def verifier(nom):
            if nom == "energie":
                return module_fragile, None
            return module_sain, None

        def afficher(tick, vaisseau, statuts, erreurs, vague, degats):
            affichages.append((statuts, degats))

        self.assertEqual(module_fragile.produire({"energie": 100}), 0)
        with (
            patch.object(boucle.vagues, "TICK_DEPART", 1),
            patch.object(boucle.rechargeur, "charger"),
            patch.object(boucle.rechargeur, "verifier_et_recharger", side_effect=verifier),
            patch.object(boucle.sauvegarde, "charger", return_value=None),
            patch.object(boucle.sauvegarde, "enregistrer"),
            patch.object(boucle, "afficher", side_effect=afficher),
            patch.object(boucle.time, "sleep", side_effect=StopIteration),
        ):
            with self.assertRaises(StopIteration):
                boucle.lancer()

        statuts, degats = affichages[0]
        self.assertIsInstance(statuts["energie"]["erreur_appel"], ZeroDivisionError)
        self.assertEqual(degats, 10)

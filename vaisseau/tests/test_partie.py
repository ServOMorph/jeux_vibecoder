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
        self.assertEqual(tour["niveau"]["titre"], "Premier signal")

    def test_un_signal_allume_valide_le_premier_niveau(self):
        class ModuleSain:
            @staticmethod
            def produire(etat):
                return 0

        class BaliseAllumee:
            @staticmethod
            def emettre_signal(etat):
                return True

        partie = boucle.Partie.nouvelle()

        def verifier(nom):
            if nom == "balise":
                return BaliseAllumee(), None
            return ModuleSain(), None

        with (
            patch.object(boucle.rechargeur, "verifier_et_recharger", side_effect=verifier),
            patch.object(boucle.sauvegarde, "enregistrer"),
        ):
            tour = partie.avancer()

        self.assertTrue(tour["niveau"]["reussi"])
        self.assertEqual(partie.progression["niveaux_termines"], [1])
        self.assertEqual(partie.progression["niveau_debloque"], 2)

    def test_le_niveau_2_est_verifie_apres_la_victoire_du_premier(self):
        class ModuleSain:
            @staticmethod
            def produire(etat):
                return 0

            @staticmethod
            def alimenter_serre(etat):
                if etat["oxygene"] < 40 or etat["energie"] < 20:
                    return 0
                return 20

        class BaliseAllumee:
            @staticmethod
            def emettre_signal(etat):
                return True

        partie = boucle.Partie.nouvelle()

        def verifier(nom):
            if nom == "balise":
                return BaliseAllumee(), None
            return ModuleSain(), None

        with (
            patch.object(boucle.rechargeur, "verifier_et_recharger", side_effect=verifier),
            patch.object(boucle.sauvegarde, "enregistrer"),
        ):
            partie.avancer()
            tour = partie.avancer()

        self.assertEqual(tour["niveau"]["titre"], "Contexte")
        self.assertTrue(tour["niveau"]["reussi"])
        self.assertEqual(partie.progression["niveaux_termines"], [1, 2])

    def test_le_niveau_3_est_verifie_apres_les_deux_premiers(self):
        class ModuleSain:
            @staticmethod
            def produire(etat):
                return 0

            @staticmethod
            def alimenter_serre(etat):
                return 20 if etat["oxygene"] >= 40 and etat["energie"] >= 20 else 0

            @staticmethod
            def reguler_temperature(etat):
                return 21 if etat["energie"] >= 20 else None

            @staticmethod
            def recycler_eau(etat):
                return 10 if etat["oxygene"] >= 40 else 0

            @staticmethod
            def eclairer_cultures(etat):
                return etat["energie"] >= 30

        class BaliseAllumee:
            @staticmethod
            def emettre_signal(etat):
                return True

        partie = boucle.Partie.nouvelle()

        def verifier(nom):
            if nom == "balise":
                return BaliseAllumee(), None
            return ModuleSain(), None

        with (
            patch.object(boucle.rechargeur, "verifier_et_recharger", side_effect=verifier),
            patch.object(boucle.sauvegarde, "enregistrer"),
        ):
            partie.avancer()
            partie.avancer()
            tour = partie.avancer()

        self.assertEqual(tour["niveau"]["titre"], "Découpage")
        self.assertTrue(tour["niveau"]["reussi"])
        self.assertEqual(partie.progression["niveaux_termines"], [1, 2, 3])

    def test_le_niveau_4_est_verifie_apres_les_trois_premiers(self):
        class ModuleSain:
            @staticmethod
            def produire(etat):
                return 0

            @staticmethod
            def alimenter_serre(etat):
                return 20 if etat["oxygene"] >= 40 and etat["energie"] >= 20 else 0

            @staticmethod
            def reguler_temperature(etat):
                return 21 if etat["energie"] >= 20 else None

            @staticmethod
            def recycler_eau(etat):
                return 10 if etat["oxygene"] >= 40 else 0

            @staticmethod
            def eclairer_cultures(etat):
                return etat["energie"] >= 30

            @staticmethod
            def normaliser_signal(signal):
                return "_".join(str(signal or "").strip().upper().split())

            @staticmethod
            def interpreter_signal(etat):
                signal = ModuleSain.normaliser_signal(etat.get("signal_externe"))
                return "PROTEGER" if signal else "VEILLE"

        class BaliseAllumee:
            @staticmethod
            def emettre_signal(etat):
                return True

        partie = boucle.Partie.nouvelle()

        def verifier(nom):
            if nom == "balise":
                return BaliseAllumee(), None
            return ModuleSain(), None

        with (
            patch.object(boucle.rechargeur, "verifier_et_recharger", side_effect=verifier),
            patch.object(boucle.sauvegarde, "enregistrer"),
        ):
            partie.avancer()
            partie.avancer()
            partie.avancer()
            tour = partie.avancer()

        self.assertEqual(tour["niveau"]["titre"], "Lecture de code")
        self.assertTrue(tour["niveau"]["reussi"])
        self.assertEqual(partie.progression["niveaux_termines"], [1, 2, 3, 4])

    def test_le_mode_dev_prepare_le_premier_tick_de_vague(self):
        partie = boucle.Partie.nouvelle()

        partie.preparer_vague_dev()

        self.assertEqual(partie.tick, 19)
        self.assertFalse(partie.progression["vague_initiale_terminee"])

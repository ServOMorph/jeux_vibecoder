import unittest

from moteur import niveaux
from moteur.niveaux.niveau_1 import NIVEAU
from moteur.niveaux.niveau_2 import NIVEAU as NIVEAU_2
from moteur.niveaux.niveau_3 import NIVEAU as NIVEAU_3
from moteur.niveaux.niveau_4 import NIVEAU as NIVEAU_4


class NiveauxTest(unittest.TestCase):
    def test_le_niveau_1_est_actif_par_defaut(self):
        progression = {"vague_initiale_terminee": False}

        niveau = niveaux.actif(progression)

        self.assertEqual(niveau, NIVEAU)
        self.assertEqual(progression["niveau_debloque"], 1)
        self.assertEqual(progression["niveaux_termines"], [])

    def test_le_critere_de_victoire_demande_un_vrai_signal(self):
        class BaliseEteinte:
            @staticmethod
            def emettre_signal(etat):
                return False

        class BaliseAllumee:
            @staticmethod
            def emettre_signal(etat):
                return True

        self.assertFalse(NIVEAU.evaluer(BaliseEteinte()).reussi)
        self.assertTrue(NIVEAU.evaluer(BaliseAllumee()).reussi)

    def test_la_victoire_debloque_le_niveau_suivant_une_seule_fois(self):
        progression = {"vague_initiale_terminee": False}

        self.assertTrue(niveaux.enregistrer_victoire(progression, NIVEAU))
        self.assertFalse(niveaux.enregistrer_victoire(progression, NIVEAU))

        self.assertEqual(progression["niveaux_termines"], [1])
        self.assertEqual(progression["niveau_debloque"], 2)

    def test_le_niveau_2_devient_actif_apres_le_premier_signal(self):
        progression = {"vague_initiale_terminee": False}

        niveaux.enregistrer_victoire(progression, NIVEAU)

        self.assertEqual(niveaux.actif(progression), NIVEAU_2)

    def test_le_niveau_2_recompense_le_contexte_et_pas_un_retour_constant(self):
        class ReponseParesseuse:
            @staticmethod
            def alimenter_serre(etat):
                return 20

        class SerreContextuelle:
            @staticmethod
            def alimenter_serre(etat):
                if etat["oxygene"] < 40 or etat["energie"] < 20:
                    return 0
                return 20

        evaluation_paresseuse = NIVEAU_2.evaluer(ReponseParesseuse())

        self.assertFalse(evaluation_paresseuse.reussi)
        self.assertIn("oxygène", evaluation_paresseuse.diagnostic)
        self.assertTrue(NIVEAU_2.evaluer(SerreContextuelle()).reussi)

    def test_le_niveau_3_devient_actif_apres_le_niveau_2(self):
        progression = {"vague_initiale_terminee": False}

        niveaux.enregistrer_victoire(progression, NIVEAU)
        niveaux.enregistrer_victoire(progression, NIVEAU_2)

        self.assertEqual(niveaux.actif(progression), NIVEAU_3)

    def test_le_niveau_3_exige_trois_sous_systemes(self):
        class ReponseParesseuse:
            @staticmethod
            def reguler_temperature(etat):
                return 21

            @staticmethod
            def recycler_eau(etat):
                return 10

            @staticmethod
            def eclairer_cultures(etat):
                return True

        class SerreComplete:
            @staticmethod
            def reguler_temperature(etat):
                return 21 if etat["energie"] >= 20 else None

            @staticmethod
            def recycler_eau(etat):
                return 10 if etat["oxygene"] >= 40 else 0

            @staticmethod
            def eclairer_cultures(etat):
                return etat["energie"] >= 30

        evaluation_paresseuse = NIVEAU_3.evaluer(ReponseParesseuse())

        self.assertFalse(evaluation_paresseuse.reussi)
        self.assertIn("oxygène", evaluation_paresseuse.diagnostic)
        self.assertTrue(NIVEAU_3.evaluer(SerreComplete()).reussi)

    def test_le_niveau_4_devient_actif_apres_le_niveau_3(self):
        progression = {"vague_initiale_terminee": False}

        for niveau in (NIVEAU, NIVEAU_2, NIVEAU_3):
            niveaux.enregistrer_victoire(progression, niveau)

        self.assertEqual(niveaux.actif(progression), NIVEAU_4)

    def test_le_niveau_4_exige_la_compatibilite_legacy(self):
        class ReecritureAveugle:
            @staticmethod
            def interpreter_signal(etat):
                return "PROTEGER" if etat.get("signal_externe") else "VEILLE"

        class DefenseCompatible:
            @staticmethod
            def normaliser_signal(signal):
                return "_".join(str(signal or "").strip().upper().split())

            @staticmethod
            def interpreter_signal(etat):
                signal = DefenseCompatible.normaliser_signal(etat.get("signal_externe"))
                return "PROTEGER" if signal else "VEILLE"

        evaluation_aveugle = NIVEAU_4.evaluer(ReecritureAveugle())

        self.assertFalse(evaluation_aveugle.reussi)
        self.assertIn("compatibilité", evaluation_aveugle.diagnostic)
        self.assertTrue(NIVEAU_4.evaluer(DefenseCompatible()).reussi)

import unittest
from pathlib import Path
from unittest.mock import patch

from moteur import boucle
from moteur import rechargeur
from moteur import score


class ScoreTest(unittest.TestCase):
    def setUp(self):
        self.mtimes = rechargeur._mtimes.copy()
        self.modules = rechargeur._modules.copy()
        self.erreurs = rechargeur._erreurs.copy()
        self.rechargements = score._rechargements.copy()
        rechargeur._mtimes.clear()
        rechargeur._modules.clear()
        rechargeur._erreurs.clear()
        score._rechargements.clear()

    def tearDown(self):
        rechargeur._mtimes.clear()
        rechargeur._mtimes.update(self.mtimes)
        rechargeur._modules.clear()
        rechargeur._modules.update(self.modules)
        rechargeur._erreurs.clear()
        rechargeur._erreurs.update(self.erreurs)
        score._rechargements.clear()
        score._rechargements.update(self.rechargements)

    def test_un_rechargement_effectif_est_compte_par_module(self):
        module = object()
        rechargeur._mtimes["oxygene"] = 1
        rechargeur._modules["oxygene"] = module

        with (
            patch.object(Path, "stat", return_value=type("Stat", (), {"st_mtime": 2})()),
            patch.object(rechargeur.importlib, "reload", return_value=module),
        ):
            rechargeur.verifier_et_recharger("oxygene")

        self.assertEqual(score.nombre_rechargements("oxygene"), 1)
        self.assertEqual(score.nombre_rechargements("energie"), 0)

    def test_le_dashboard_affiche_les_iterations_sans_effet_sur_les_statuts(self):
        statuts = {
            "oxygene": {"erreur_reload": None, "erreur_appel": None},
            "energie": {"erreur_reload": None, "erreur_appel": None},
            "defense": {"erreur_reload": None, "erreur_appel": None},
        }
        lignes = []

        with (
            patch.object(boucle, "os_clear"),
            patch(
                "builtins.print",
                side_effect=lambda *args: lignes.append(args[0] if args else ""),
            ),
            patch.object(score, "nombre_rechargements", return_value=3),
        ):
            boucle.afficher(
                1,
                {"oxygene": 100, "energie": 100, "integrite": 100},
                statuts,
                {"oxygene": None, "energie": None, "defense": None},
                None,
                0,
            )

        self.assertIn("Module oxygene    : OK | iterations IA : 3", lignes)

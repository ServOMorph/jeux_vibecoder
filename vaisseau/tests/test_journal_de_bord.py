from pathlib import Path
import unittest


JOURNAL = Path(__file__).resolve().parents[1] / "JOURNAL_DE_BORD.md"
TITRES_ATTENDUS = (
    "## 1 — Premier signal",
    "## 2 — Contexte",
    "## 3 — Découpage",
    "## 4 — Lecture de code",
)


class JournalDeBordTest(unittest.TestCase):
    def test_chaque_niveau_a_un_brief_de_trois_lignes_maximum(self):
        lignes = JOURNAL.read_text(encoding="utf-8").splitlines()

        for titre in TITRES_ATTENDUS:
            debut = lignes.index(titre)
            fin = next((index for index in range(debut + 1, len(lignes)) if lignes[index].startswith("## ")), len(lignes))
            brief = [ligne for ligne in lignes[debut + 1 : fin] if ligne]

            self.assertLessEqual(len(brief), 3)
            self.assertTrue(brief)

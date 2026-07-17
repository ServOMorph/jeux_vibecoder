import sys
from pathlib import Path

RACINE_VAISSEAU = Path(__file__).resolve().parent / "vaisseau"
sys.path.insert(0, str(RACINE_VAISSEAU))

from moteur.ui import lancer


if __name__ == "__main__":
    lancer()

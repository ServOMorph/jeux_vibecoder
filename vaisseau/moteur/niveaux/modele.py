from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Evaluation:
    reussi: bool
    diagnostic: str


@dataclass(frozen=True)
class Niveau:
    identifiant: int
    titre: str
    objectif: str
    critere_victoire: str
    module_cible: str
    debloque: int
    evaluateur: Callable[[object, Exception | None], Evaluation]

    def evaluer(self, module, erreur=None):
        return self.evaluateur(module, erreur)

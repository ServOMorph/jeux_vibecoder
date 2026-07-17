import importlib
from pathlib import Path

from moteur import score

_mtimes = {}
_modules = {}
_erreurs = {}


def _chemin(nom_module):
    return Path(__file__).resolve().parent.parent / "modules" / f"{nom_module}.py"


def charger(nom_module):
    chemin = _chemin(nom_module)
    _mtimes[nom_module] = chemin.stat().st_mtime
    try:
        module = importlib.import_module("modules." + nom_module)
        _modules[nom_module] = module
        _erreurs.pop(nom_module, None)
        return module, None
    except Exception as exc:
        _erreurs[nom_module] = exc
        return None, exc


def verifier_et_recharger(nom_module):
    """Recharge le module si son fichier a change depuis le dernier chargement.

    Retourne (module, erreur). En cas d'erreur, l'ancien module reste utilisable
    dans _modules si un chargement precedent a reussi.
    """
    chemin = _chemin(nom_module)
    mtime_actuel = chemin.stat().st_mtime
    if _mtimes.get(nom_module) == mtime_actuel:
        return _modules.get(nom_module), _erreurs.get(nom_module)

    _mtimes[nom_module] = mtime_actuel
    score.enregistrer_rechargement(nom_module)
    try:
        if nom_module in _modules:
            module = importlib.reload(_modules[nom_module])
        else:
            module = importlib.import_module("modules." + nom_module)
        _modules[nom_module] = module
        _erreurs.pop(nom_module, None)
        return module, None
    except Exception as exc:
        _erreurs[nom_module] = exc
        return _modules.get(nom_module), exc

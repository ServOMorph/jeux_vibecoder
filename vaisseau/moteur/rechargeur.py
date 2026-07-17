import importlib
import os

_mtimes = {}
_modules = {}


def _chemin(nom_module):
    return os.path.join("modules", nom_module + ".py")


def charger(nom_module):
    chemin = _chemin(nom_module)
    _mtimes[nom_module] = os.path.getmtime(chemin)
    try:
        module = importlib.import_module("modules." + nom_module)
        _modules[nom_module] = module
        return module, None
    except Exception as exc:
        return None, exc


def verifier_et_recharger(nom_module):
    """Recharge le module si son fichier a change depuis le dernier chargement.

    Retourne (module, erreur). En cas d'erreur, l'ancien module reste utilisable
    dans _modules si un chargement precedent a reussi.
    """
    chemin = _chemin(nom_module)
    mtime_actuel = os.path.getmtime(chemin)
    if _mtimes.get(nom_module) == mtime_actuel:
        return _modules.get(nom_module), None

    _mtimes[nom_module] = mtime_actuel
    try:
        if nom_module in _modules:
            module = importlib.reload(_modules[nom_module])
        else:
            module = importlib.import_module("modules." + nom_module)
        _modules[nom_module] = module
        return module, None
    except Exception as exc:
        return _modules.get(nom_module), exc

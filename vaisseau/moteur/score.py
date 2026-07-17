from collections import defaultdict

_rechargements = defaultdict(int)


def enregistrer_rechargement(nom_module):
    _rechargements[nom_module] += 1


def nombre_rechargements(nom_module):
    return _rechargements[nom_module]

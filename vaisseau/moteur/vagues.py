TICK_DEPART = 20
CHARGES = (1, 2, 3)
DEGATS_PAR_MODULE_EN_ECHEC = 10


def active(tick):
    index = tick - TICK_DEPART
    if 0 <= index < len(CHARGES):
        return {
            "charge": CHARGES[index],
            "degats_par_module": DEGATS_PAR_MODULE_EN_ECHEC,
            "conditions_degradees": True,
        }
    return None


def ticks_avant_prochaine(tick):
    if tick < TICK_DEPART:
        return TICK_DEPART - tick
    return None


def degats(vague, modules_en_echec):
    return vague["degats_par_module"] * len(set(modules_en_echec))


def etat_sous_charge(etat, vague):
    etat_degrade = etat.copy()
    etat_degrade.update({"oxygene": 0, "energie": 0, "integrite": 0})
    etat_degrade["signal_externe"] = None
    etat_degrade["charge_vague"] = vague["charge"]
    return etat_degrade

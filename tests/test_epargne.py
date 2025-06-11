from src.mon_module.models.epargne import Epargne

def test_initialisation_epargne():
    ep = Epargne("Livret A", 0.024, 0.0, 0, 22950)
    assert ep.nom == "Livret A"
    assert ep.taux_interet == 0.024
    assert ep.fiscalite == 0.0

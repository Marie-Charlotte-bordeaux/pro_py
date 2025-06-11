from src.mon_module.utils import calcul_interets_composes

def test_interets_composes_basique():
    result = calcul_interets_composes(1000, 0.05, 2)
    assert round(result, 2) == round((1000 + 0) * 1.05 + 1000, 2) * 1.05

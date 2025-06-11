from src.mon_module.models.resultat import ResultatEpargne

def test_resultat_epargne():
    r = ResultatEpargne("Livret A", 100.0, 1200.0, True)
    assert r.nom_produit == "Livret A"
    assert r.effort_mensuel == 100.0
    assert r.montant_net_final == 1200.0
    assert r.objectif_atteint is True

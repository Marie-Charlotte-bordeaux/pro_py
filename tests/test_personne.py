from src.mon_module.models.personne import Personne

def test_initialisation_personne():
    p = Personne("Alice", 30, 40000, 800, 1000, 50000, 10, None)
    assert p.nom == "Alice"
    assert p.age == 30
    assert p.revenu_annuel == 40000

def test_capacite_epargne():
    p = Personne("Bob", 40, 48000, 1000, 1200, 60000, 10, None)
    capacite = p._calcul_capacite_epargne()
    revenu_mensuel = 48000 / 12
    attendu = revenu_mensuel - 1000 - 1200
    assert capacite == attendu

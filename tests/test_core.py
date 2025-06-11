from src.mon_module.core import import_epargnes, import_personnes


def test_import_epargnes():
    epargnes = import_epargnes("epargnes.csv")
    assert len(epargnes) > 0
    assert epargnes[0].nom.lower().startswith("livret")

def test_import_personnes():
    personnes = import_personnes("personnes.csv")
    assert len(personnes) > 0
    assert personnes[0].nom != ""

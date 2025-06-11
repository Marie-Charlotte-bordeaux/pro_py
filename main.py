from src.mon_module.core import import_epargnes, import_personnes, suggestion_epargne
from src.mon_module.models.personne import Personne

# p1 = Personne("Alice", 30, 36000, 700, 500, 10000, 5)
# print(p1)


# epargnes = import_epargnes("epargnes.csv")

# print(" Liste des produits d’épargne :\n")
# for ep in epargnes:
#     print(ep)


# personnes = import_personnes("personnes.csv")

# for p in personnes:
#     print(p)
    
    
    

# personnes = import_personnes("personnes.csv")
# epargnes = import_epargnes("epargnes.csv")

# # On teste avec la première personne
# p1 = personnes[0]
# resultats = suggestion_epargne(p1, epargnes, p1.objectif, p1.duree_epargne)

# # Affichage
# for res in resultats:
#     res.afficher()


# Étape 1 : Charger les données
epargnes = import_epargnes("epargnes.csv")
personnes = import_personnes("personnes.csv")

# Étape 2 : Choisir une personne 
personne = personnes[29]
objectif = personne.objectif
duree = personne.duree_epargne

print(f"\nSimulation pour {personne.nom} (objectif : {objectif} €, durée : {duree} ans)\n")

# Étape 3 : Appeler la fonction de simulation
resultats = suggestion_epargne(personne, epargnes, objectif, duree)

# Étape 4 : Afficher les résultats formatés
for resultat in resultats:
    resultat.afficher()
import pandas as pd
from typing import List, Optional
from src.mon_module.models.epargne import Epargne
from src.mon_module.models.personne import Personne
from src.mon_module.models.resultat import ResultatEpargne 
from src.mon_module.utils import calcul_interets_composes 


# Fonctions import 
def import_epargnes(fichier: str) -> List[Epargne]:
    try:
        if fichier.endswith('.csv'):
            df = pd.read_csv(fichier)
        elif fichier.endswith('.xlsx'):
            df = pd.read_excel(fichier)
        elif fichier.endswith('.txt'):
            df = pd.read_csv(fichier, sep='\t')
        else:
            raise ValueError("Format de fichier non supporté.")

        # Nettoyage des données
        df = df.fillna("None")
        epargnes = []

        for _, row in df.iterrows():
            nom = row["nom"]
            taux_interet = float(row["taux_interet"])
            fiscalite = float(row["fiscalite"])
            duree_min = int(row["duree_min"])

            # Gestion propre de "None" ou vide
            versement_max = row["versement_max"]
            if versement_max == "None":
                versement_max = None
            else:
                versement_max = float(versement_max)

            ep = Epargne(nom, taux_interet, fiscalite, duree_min, versement_max)
            epargnes.append(ep)

        return epargnes

    except Exception as e:
        print(f"Erreur lors de l'import : {e}")
        return []

def import_personnes(fichier: str) -> List[Personne]:
    try:
        if fichier.endswith('.csv'):
            df = pd.read_csv(fichier)
        elif fichier.endswith('.xlsx'):
            df = pd.read_excel(fichier)
        elif fichier.endswith('.txt'):
            df = pd.read_csv(fichier, sep='\t')
        else:
            raise ValueError("Format de fichier non supporté.")
        
        df = df.fillna("None")
        personnes = []

        for _, row in df.iterrows():
            nom = row["nom"]
            age = int(row["age"])
            revenu_annuel = float(row["revenu_annuel"])
            loyer = float(row["loyer"])
            depenses_mensuelles = float(row["depenses_mensuelles"])
            objectif = float(row["objectif"])
            duree_epargne = int(row["duree_epargne"])

            versement_mensuel_utilisateur = row["versement_mensuel_utilisateur"]
            if versement_mensuel_utilisateur == "None":
                versement_mensuel_utilisateur = None
            else:
                versement_mensuel_utilisateur = float(versement_mensuel_utilisateur)

            personne = Personne(nom, age, revenu_annuel, loyer, depenses_mensuelles,
                                objectif, duree_epargne, versement_mensuel_utilisateur)
            personnes.append(personne)

        return personnes

    except Exception as e:
        print(f"Erreur lors de l'import personnes : {e}")
        return []

# ----------------------------
# Fonctions metier
# ----------------------------

def suggestion_epargne(personne: Personne, epargnes: List[Epargne], objectif: float, duree: int) -> List[ResultatEpargne]:
    resultats = []

    # Scénarios d'effort mensuel
    base = personne.versement_mensuel_utilisateur
    if base is None:
        base = personne._calcul_capacite_epargne()

    scenarios = [base * p for p in [0.25, 0.5, 0.75, 1.0]]
    if personne.versement_mensuel_utilisateur is not None:
        scenarios = [personne.versement_mensuel_utilisateur] + scenarios

    for epargne in epargnes:
        if duree < epargne.duree_min:
            continue  # produit non disponible

        for effort in scenarios:
            versement_annuel = effort * 12
            if epargne.versement_max is not None and versement_annuel * duree > epargne.versement_max:
                continue  # dépasse le plafond

            montant_brut = calcul_interets_composes(versement_annuel, epargne.taux_interet, duree)
            montant_net = montant_brut * (1 - epargne.fiscalite)
            objectif_atteint = montant_net >= objectif

            resultat = ResultatEpargne(epargne.nom, effort, montant_net, objectif_atteint)
            resultats.append(resultat)

    return resultats
import pandas as pd

class ResultatEpargne: 
  def __init__(self, nom_produit: str, effort_mensuel: float, montant_net_final: float, objectif_atteint: bool):
          self.nom_produit = nom_produit
          self.effort_mensuel = effort_mensuel
          self.montant_net_final = montant_net_final
          self.objectif_atteint = objectif_atteint
        
  def afficher(self):
    status = "Objectif atteint" if self.objectif_atteint else "Objectif non atteint"
    print(f"Produit : {self.nom_produit}")
    print(f"Effort mensuel : {self.effort_mensuel:.2f} €")
    print(f"Montant final net : {self.montant_net_final:.2f} €")
    print(status)
    print("-" * 40)
  
  def to_dataframe(self):
    return pd.DataFrame([{
      "Produit": self.nom_produit,
      "Effort mensuel (€)": self.effort_mensuel,
      "Montant net final (€)": self.montant_net_final,
      "Objectif atteint": self.objectif_atteint
    }])

from typing import Optional
class Epargne: 
      def __init__(self, nom: str, taux_interet: float, fiscalite: float, duree_min: float, versement_max: Optional[float]):
        self.nom = nom
        self.taux_interet = taux_interet
        self.fiscalite = fiscalite
        self.duree_min = duree_min
        self.versement_max = versement_max
        
        
      def __repr__(self):
        return f"Epargne({self.nom!r}, {self.taux_interet}, {self.fiscalite}, {self.duree_min}, {self.versement_max})"

      
      def __str__(self):
        return f"{self.nom} - Taux: {self.taux_interet*100:.2f}% | Fisacalité: {self.fiscalite*100:.1f}% | Durée min: {self.duree_min} ans"
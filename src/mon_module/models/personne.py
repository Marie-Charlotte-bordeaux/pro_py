class Personne: 
      def __init__(self, nom: str, age: int, revenu_annuel: float, loyer: float, depenses_mensuelles: float, 
          objectif: float, duree_epargne: int, versement_mensuel_utilisateur: float = None):
        self.nom = nom
        self.age = age
        self.revenu_annuel = revenu_annuel
        self.loyer = loyer
        self.depenses_mensuelles = depenses_mensuelles
        self.objectif = objectif
        self.duree_epargne = duree_epargne
        self.versement_mensuel_utilisateur = versement_mensuel_utilisateur
        
      def _calcul_capacite_epargne(self) -> float:
        revenu_mensuel = self.revenu_annuel / 12
        return revenu_mensuel - self.loyer - self.depenses_mensuelles
      
      def __str__(self) -> str:
        return f"{self.nom}, {self.age} ans — capacité d'épargne : {self._calcul_capacite_epargne():.2f}€/mois"
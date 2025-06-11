from datetime import datetime
from functools import wraps
from colorama import Fore, Style

def calcul_interets_composes(versement_annuel: float, taux_annuel: float, duree_annees: int) -> float:
    def accumuler(montant_actuel: float, annees_restantes: int) -> float:
        if annees_restantes == 0:
            return montant_actuel
        montant_suivant = (montant_actuel + versement_annuel) * (1 + taux_annuel)
        return accumuler(montant_suivant, annees_restantes - 1)

    return accumuler(0.0, duree_annees)


def main():
    # test manuel
    versement_annuel = 1000.0
    taux_annuel = 0.05
    duree_annees = 10

    montant_final = calcul_interets_composes(versement_annuel, taux_annuel, duree_annees)
    print(f"📈 Montant final après {duree_annees} ans avec un versement de {versement_annuel} €/an à {taux_annuel*100:.1f}% : {montant_final:.2f} €")


if __name__ == "__main__":
    main()
    
# Decorateur fonction suggestion_epargne ::: 
def afficher_intro_comparaison(func):
    @wraps(func)
    def wrapper(personne, epargnes, *args, **kwargs):
        maintenant = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\n" + "=" * 80)
        print(f"📅 {maintenant} – Nous allons faire une comparaison de {Fore.YELLOW}{len(epargnes)}{Style.RESET_ALL} placements selon la situation de {Fore.MAGENTA}{personne.nom}{Style.RESET_ALL}.")
        print("=" * 80 + "\n")
        return func(personne, epargnes, *args, **kwargs)
    return wrapper
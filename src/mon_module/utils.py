def calcul_interets_composes(versement_annuel: float, taux_annuel: float, duree_annees: int) -> float:
    """
    Calcule le montant final avec intérêts composés et versements annuels constants.

    :param versement_annuel: Montant versé chaque année
    :param taux_annuel: Taux d’intérêt annuel (ex: 0.05 pour 5%)
    :param duree_annees: Durée de l’épargne en années
    :return: Montant final épargné
    """
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
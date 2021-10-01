# 30/09/2021 par Pacco ANENIN
class Matrice:

    # annuler x avec y = x = x - ((x/y) * y)

    def __init__(self, tableau_matrice):
        """
        :param tableau_matrice: tableau représentant la matrice
        :type tableau_matrice: list
        """

        self.tableau = tableau_matrice

        if len(tableau_matrice) != 0:
            self.dimension = [len(tableau_matrice[0]), len(tableau_matrice)]
        else:
            self.dimension = [0, 0]

    def __str__(self):
        return str(self.tableau)

    # METHODS
    def scale_to(self, scaler):
        """
        :type scaler: float
        """

        for y in range(0, self.dimension[1]):
            for x in range(0, self.dimension[0]):
                self.tableau[y][x] *= scaler

    # STATICS
    @staticmethod
    def multiply(matrice_a, matrice_b):
        """ Multiplie les deux matrices renseignées et renvoit le résultat
        :param matrice_a:
        :type matrice_a: Matrice
        :param matrice_b:
        :type matrice_b: Matrice
        :rtype Matrice
        """

        # test de la compatibilité des dimensions
        if matrice_a.dimension[0] != matrice_b.dimension[1]:
            raise TypeError("Les dimensions des matrices ne sont pas"
                            "compatibles pour la multiplication")

        # matrice qui contiendra le résultat
        matrice_produit_tableau = []
        for a_row_index in range(0, matrice_a.dimension[1]):
            matrice_produit_tableau.append([])
            for b_col_index in range(0, matrice_b.dimension[0]):
                matrice_produit_tableau[a_row_index].append(0)

        for b_col_index in range(0, matrice_b.dimension[0]):
            a_row: list
            for a_row in matrice_a.tableau:

                to_sum = []

                a_row_index = matrice_a.tableau.index(a_row)

                coef_col_index = 0
                for x in a_row:
                    to_sum.append(x * matrice_b.tableau[coef_col_index][b_col_index])
                    coef_col_index += 1

                matrice_produit_tableau[a_row_index][b_col_index] = sum(to_sum)

        return Matrice(matrice_produit_tableau)

    @staticmethod
    def sum(matrice_a, matrice_b):
        """Fait la somme de la matrice A et B
        :param matrice_a:
        :type matrice_a: Matrice
        :param matrice_b:
        :type matrice_b: Matrice
        :return: La matrice résultat (la somme)
        :rtype: Matrice
        """

        # vérification du type des matrices
        if (type(matrice_a) != Matrice or
                type(matrice_b) != Matrice):
            raise TypeError
        elif matrice_a.dimension != matrice_b.dimension:
            raise TypeError("Les matrices additionnées doivent être de même dimension !")

        # création du futur tableau pour le résultat
        new_matrice_tab = []
        for y in range(0, matrice_a.dimension[1]):
            new_matrice_tab.append([])
            for x in range(0, matrice_a.dimension[0]):
                new_matrice_tab[y].append(0)

        # calcul et affecation des sommes
        for y in range(0, matrice_a.dimension[1]):
            for x in range(0, matrice_a.dimension[0]):
                new_matrice_tab[y][x] = matrice_a.tableau[y][x] + matrice_b.tableau[y][x]

        return Matrice(new_matrice_tab)
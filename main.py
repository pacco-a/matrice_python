from matrice import Matrice

# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def demo_matrice_sum():
    matrice1 = Matrice(tableau_matrice=[[1, 2, 3],
                                        [4, 5, 6]])

    matrice2 = Matrice(tableau_matrice=[[1, 2, 3],
                                        [4, 5, 6]])

    matrice_somme = Matrice.sum(matrice1, matrice2)

    print(matrice_somme)


def demo_matrice_scaler():
    matrice1 = Matrice(tableau_matrice=[[1, 2, 3],
                                        [4, 5, 6]])
    matrice1.scale_to(scaler=2)
    print(matrice1)


def demo_matrice_multiply():
    matrice1 = Matrice(tableau_matrice=[[9, 4],
                                        [-8, 5],
                                        [11, -2],
                                        [442, -8]])

    matrice2 = Matrice(tableau_matrice=[[56, 2, 19, -2, 0],
                                        [9, 14, -22, 1, 0]])

    print(Matrice.multiply(matrice1, matrice2))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    demo_matrice_multiply()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

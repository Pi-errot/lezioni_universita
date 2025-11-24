#     Data una matrice n x n contenente solo valori 0 e 1. Un'isola è definita come un gruppo di celle adiacenti contenenti 1 che possono essere collegate orizzontalmente o verticalmente (non diagonalmente). Scrivere una funzione find_largest_island che trova la dimensione dell’isola più grande presente nella matrice.
# Esempio:
# matrice = [
#     [1, 1, 0, 0],
#     [1, 0, 0, 1],
#     [0, 0, 1, 1],
#     [0, 1, 1, 1]
# ]
# La funzione find_largest_island(matrice) restituirebbe 6, che è la dimensione dell'isola in basso a destra.


def find_largest_island(matrice):
    pointsWithOne = []
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j]:
                pointsWithOne.append((i,j))
    isole = []
    for i in range(len(pointsWithOne)):
        punto = pointsWithOne[i]
        (Xp,Yp) = punto
        isNearOtherPoint = False
        for isola in isole:
            for puntoIsola in isola:
                if Xp-1 <= puntoIsola[0] <= Xp+1 ^ Yp-1 <= puntoIsola[1] <= Yp+1:
                    isNearOtherPoint = True
                    isola.append(punto)
                    break

        if not isNearOtherPoint:
            isole.append([punto])

    print("lista di punti con 1: ", pointsWithOne)
    print("Isole:", isole)
    return 0

matrice = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1]
]

print(find_largest_island(matrice))

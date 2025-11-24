"""
    Data una matrice n x n contenente solo valori 0 e 1. Un'isola è definita come un gruppo di celle adiacenti contenenti 1 che possono essere collegate orizzontalmente o verticalmente (non diagonalmente). Scrivere una funzione find_largest_island che trova la dimensione dell’isola più grande presente nella matrice.
Esempio:
matrice = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1]
]
La funzione find_largest_island(matrice) restituirebbe 6, che è la dimensione dell'isola in basso a destra.
"""
def findAllPointOfIsland(startingPoint, matrix):
    isola = [startingPoint]
    (x, y) = startingPoint
    matrix[x][y] = 0

    for offset in [-1, +1]:
        for applyToX in [0,1]:
            newX = x+offset*(applyToX)
            newY = y+offset*((applyToX+1)%2)
            if newX < 0 or newX >= len(matrix) or newY < 0 or newY >= len(matrix[0]):
                continue
            if matrix[newX][newY]:
                isola.extend(findAllPointOfIsland((newX, newY), matrix))
    return isola

def find_largest_island(matrice, punto = (0,0)):
    isole = []
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j]:
                isola = findAllPointOfIsland((i,j), matrice)
                isole.append(isola)
    
    maxLenght = 0
    for isola in isole:
        if len(isola) > maxLenght:
            maxLenght = len(isola)
    return maxLenght


matrice = [
    [1, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1]
]

print(find_largest_island(matrice))


"""
    Data una matrice n x m, scrivere una funzione che restituisca la matrice trasposta m x n. La trasposta di una matrice si calcola scambiando le righe con le colonne, quindi la riga 0 diventa la colonna 0 della prima matrice, la riga 1 la colonna 1, ecc.
Esempio:
matrice = [
    [2, 4, 7],
    [3, 1, 3]
]
La matrice trasposta è
matrice_trasposta = [
    [2, 3],
    [4, 1],
    [7, 3]
]
"""

def trasposta(matrice):
    mTrasposta = []
    for i in range(len(matrice[0])):
        mTrasposta.append([])
        for j in range(len(matrice)):
            mTrasposta[i].append(matrice[j][i])
    return mTrasposta

matrice = [
    [2, 4, 7],
    [3, 1, 3]
]


print(trasposta(matrice))

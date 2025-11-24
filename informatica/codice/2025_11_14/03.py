#     Data una matrice n x n che rappresenta una griglia, dove ogni cella contiene 0 per una cella libera e 1 per una cella con ostacolo, scrivere una funzione che restituisca True se esiste un percorso dalla cella in alto a sinistra (0, 0) alla cella in basso a destra (n-1, n-1), False altrimenti. È possibile muoversi solo in orizzontale o verticale (non in diagonale) e si può assumere che in posizione (0, 0) ci sia sempre uno 0.
# Esempio:
# matrice = [
#     [0, 0, 1, 0],
#     [1, 0, 1, 0],
#     [0, 0, 0, 0],
#     [1, 1, 0, 0]
# ]
# La funzione deve restituire True perché è possibile seguire il seguente percorso: (0,0), (0,1), (1,0), (2,1), (2,2), (3,2), (3,3).

def trovaCellaSuccessiva(punto, matrice):
    (x, y) = punto
    if x+1 < len(matrice) and matrice[x+1][y] == 0:
        return (x+1,y)
    if y+1 < len(matrice) and matrice[x][y+1] == 0:
        return (x,y+1)
    
    print("Dal punto ", punto, " non si può andare avanti")
    print("valore cella: ", matrice[x][y])
    return False

def trovaPercorso(matrice):
    punto = (0, 0)
    percorso = []
    while punto != (len(matrice)-1, len(matrice)-1):
        if punto == False:
            return False
        punto = trovaCellaSuccessiva(punto, matrice)
        percorso.append(punto)
    
    print("Percorso trovato:", percorso )
    return True

matrice = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 1, 0, 0]
]

print("Esiste un percorso possibile? ", trovaPercorso(matrice))
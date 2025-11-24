# # Scrivere una funzione scambia_colonne(c1, c2, M) che riceva in input:
# #     un indice di colonna c1
# #     un indice di colonna c2, con c1 != c2
# #     una matrice M di valori interi 
# # La funzione scambia le colonne di indici c1 e c2 nella matrice M. Si dia per buona la correttezza dei dati in input.
# # Ad esempio, se l'input è:
# # c1 = 1
# # c2 = 3
# # M = [[11, 32, 93, 74],
# #      [25, 46, 97, 58],
# #      [89, 10, 11, 12]]
# # l'output sarà:
# # M = [[11, 74, 93, 32],
# #      [25, 58, 97, 46],
# #      [89, 12, 11, 10]]

# c1 = 1
# c2 = 3
# M = [[11, 32, 93, 74],
#      [25, 46, 97, 58],
#      [89, 10, 11, 12]]
# # M = [[11, 74, 93, 32],
# #      [25, 58, 97, 46],
# #      [89, 12, 11, 10]]

def scambia_colonne(c1, c2, M):
    for vettore in M:
        vettore[c1], vettore[c2] = vettore[c2], vettore[c1]

# scambia_colonne(c1, c2, M)

# print(M)

Matrice = [[0,-1],[1]]

for i in range(len(Matrice)):
    for j in range(len(Matrice[i])):
        print(Matrice[i][j])

for vettore in Matrice:
    for elemento in vettore:
        print(elemento)


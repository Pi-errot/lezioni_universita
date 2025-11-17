# Scrivere una funzione is_submatrix(sub, mat) che riceva in input:
#     una matrice di numeri interi sub
#     una matrice di numeri interi mat di dimensioni maggiori o uguali a quelle di sub
# La funzione ritorna True se la matrice sub è contenuta nella matrice mat. Si dia per buona la correttezza dei dati in input.
# Ad esempio, se l'input è:
# sub = [[46, 97],
#        [10, 11]]
# mat = [[11, 32, 93, 74],
#        [25, 46, 97, 58],
#        [89, 10, 11, 12]]
# la funzione ritorna True perché la matrice sub è una sottomatrice di mat.
# Se l'input è:
# sub = [[25, 26],
#        [31, 73]]
# mat = [[11, 32, 93, 74],
#        [25, 46, 97, 58],
#        [89, 10, 11, 12]]
# la funzione ritorna False perché la matrice sub non è una sottomatrice di mat.

# sub = [[25, 26],
#        [31, 73]]
# mat = [[11, 32, 93, 74],
#        [25, 46, 97, 58],
#        [89, 10, 11, 12]]


sub = [[46, 97],
       [10, 11]]
mat = [[11, 32, 93, 74],
       [25, 46, 97, 58],
       [89, 10, 11, 12]]

def is_submatrix(sub, mat):
    result = False
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if result:
                return True

            if sub[0][0] != mat[i][j]:
                continue
            tempResult = True

            for k in range(len(sub)):
                if not tempResult:
                    continue
                for l in range(len(sub[k])):
                    if not tempResult:
                        continue
                    tempResult = sub[k][l] == mat[i+k][j+l]
                    
                    # if sub[k][l] != mat[i+k][j+l]:
                    #     tempResult = False

            result = tempResult            
    return result

print(is_submatrix(sub,mat))
# Scrivere un programma che chieda all'utente di inserire un numero intero positivo n e stampi un quadrato di dimensione n x n, dove ogni riga alterna i numeri 1 e 0, partendo da 1. La prima riga inizia con 1, la seconda con 0, e così via.

n= int(input("Inserisci un numero intero positivo"))
if n > 0:
    for i in range(0, n):
        for j in range(0, n):
            print((i+j+1)%2 , end=" ")
        print("")
else: 
    print("Numero non valido")
# Scrivere un programma che chieda all'utente di inserire due numeri interi positivi, n e m, rappresentanti le dimensioni di un labirinto. Il programma deve generare casualmente un labirinto di dimensione n x m, dove il simbolo & rappresenta un muro e il simbolo @ rappresenta un percorso. Ogni cella ha una probabilità casuale del 30% di essere un muro e del 70% di essere un percorso. Assicurarsi che il bordo del labirinto sia sempre formato da muri.

import random

n = int(input("Inserisci un numero intero positivo: "))
m = int(input("Inserisci un altro numero intero positivo: "))

if n<5 or m<5:
    print("Numeri troppo piccoli")
else: 
    for i in range(0,n):
        for j in range(0,m):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                char = "&"
            else:
                char = "@" if random.randint(0, 100) < 70 else "&" 
            print(char, end="")
        print("")
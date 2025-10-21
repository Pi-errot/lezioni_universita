# Scrivere un programma che chieda all'utente un numero intero positivo n e stampi un triangolo formato da asterischi (*), dove la prima riga contiene 1 asterisco, la seconda 2 asterischi, e così via, fino a n asterischi.

n = int(input("Inserisci un numero intero positivo: "))
while i in range(0,n):
    print("*" * (i + 1))
    i += 1
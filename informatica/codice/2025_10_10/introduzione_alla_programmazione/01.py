# Scrivere un programma che riceva in input una stringa dall'utente e verifichi se la lunghezza della stringa è maggiore, minore o uguale a 10 caratteri.

inputStringa = input("Scrivi una stringa: ")
if len(inputStringa) < 10:
    print("La stringa è minore di 10 caratteri")
elif len(inputStringa) > 10:
    print("La stringa è maggiore di 10 caratteri")
else:
    print("La stringa è lunga 10 caratteri")



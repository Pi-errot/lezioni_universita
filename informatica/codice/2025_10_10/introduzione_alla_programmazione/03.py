# Scrivere un programma che riceva in input una stringa dall'utente e verifichi se la stringa è tutta in maiuscolo, tutta in minuscolo o se è mista.

inputStringa = input("Inserisci una stringa: ")

if inputStringa.isupper():
    print("La stringa è maiuscola")
elif inputStringa.islower():
    print("La stringa è minuscola")
else: 
    print("La stringa è mista")

    
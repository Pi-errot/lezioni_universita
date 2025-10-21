# scrivere un programma che rilevi se una stringa è palindroma come nel caso di "I Topi Non Avevano Nipoti"

inputStringa = input("Inserisci una stringa: ")
stringaLowerCased = inputStringa.replace(" ", "").lower()

if stringaLowerCased == stringaLowerCased[::-1]:
    print("La stringa è palindroma")
else:
    print("La stringa non è palindroma")
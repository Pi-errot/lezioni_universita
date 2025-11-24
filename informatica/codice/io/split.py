frase = "Ciao mondo"

acronimo = ""
for parola in frase.split():
    acronimo += list(parola)[0].capitalize()

print(acronimo)
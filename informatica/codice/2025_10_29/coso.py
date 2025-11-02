lista = ["ciao", "mondo"]
lista_enumerata = [(0, "ciao"), (1, "mondo")]

(indice, parola) = (0, "ciao")


for indice_e_parola in enumerate(lista):
    print(indice_e_parola)    

# print(enumerate(lista))
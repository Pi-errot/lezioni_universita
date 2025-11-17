# Scrivere una funzione ricerca_con_tolleranza(x, lst, epsilon) che ritorna True se x è contenuto nella lista lst con tolleranza epsilon, cioè se esiste almeno un elemento elem della lista per cui vale la relazione:
# elem - epsilon <= x <= elem + epsilon

# Il tipo degli elementi è float. Si supponga la lista non vuota.
# Ad esempio, se l'input è:
# x = 3.125
# lst = [0.016, 7.933, 5.479, 3.113, 6.787, 9.081]
# epsilon = 0.1
# la funzione ritorna True perché l'elemento 3.113 soddisfa la condizione, mentre se
# espilon = 0.01
# la funzione ritorna False perché nessun elemento rientra nell'intervallo di tolleranza.


# def ricerca_con_tolleranza(x, lst, epsilon):
#     for i in lst:
#         if x >= i-epsilon and x <= i+epsilon:
#             return True
#     return False

x = 3.125
lst = [0.016, 7.933, 5.479, 3.113, 6.787, 9.081]
epsilon = 0.1


def ricerca_con_tolleranza(x, lst, epsilon):
    risultato = False
    for i in lst:
        if risultato:
            return True
        risultato = risultato or (x >= i-epsilon and x <= i+epsilon)    
    return risultato

print(ricerca_con_tolleranza(x, lst, epsilon))
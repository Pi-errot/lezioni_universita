# Scrivere una funzione ricerca_con_tolleranza2(sub, lst, epsilon) che riceva in input:
#     una lista di numeri float sub
#     una lista di numeri float lst di dimensione maggiore o uguale alla dimensione di sub
#     un valore di tolleranza epsilon di tipo float 
# La funzione ritorna True se la lista sub è contenuta nella lista lst con tolleranza epsilon su ognuno degli elementi. Si ricorda che, dato x in sub e elem in lst, x è uguale a elem con tolleranza epsilon se
# elem - epsilon <= x <= elem + epsilon
# Si dia per buona la correttezza dei dati in input.
# Ad esempio, se l'input è:
# sub = [3.125, 6.781]
# lst = [0.016, 7.933, 5.479, 3.113, 6.787, 9.081]
# epsilon = 0.1
# la funzione ritorna True perché la sottolista [3.113, 6.787] di lst soddisfa la condizione, mentre se
# espilon = 0.01
# la funzione ritorna False perché nessuna sottolista di lst soddisfa la condizione su ogni elemento.

sub = [3.125, 6.781]
lst = [0.016, 7.933, 5.479, 3.113, 6.787, 9.081]
epsilon = 0.1

def ricerca_con_tolleranza(x, lst, epsilon):
    risultato = False
    for i in lst:
        if risultato:
            return True
        risultato = risultato or (x >= i-epsilon and x <= i+epsilon)    
    return risultato

def ricerca_con_tolleranza2(sub, lst, epsilon):
    risultato = True
    for i in sub:
        if(not risultato):
            return False
        risultato = risultato and ricerca_con_tolleranza(i, lst, epsilon)
    return risultato

print(ricerca_con_tolleranza2(sub, lst, epsilon))
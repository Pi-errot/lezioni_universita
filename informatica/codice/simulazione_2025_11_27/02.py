def getNumeriDispari(lst):
    numeriDispari = []
    posizioniNumeriDispari = []
    for i in range(len(lst)):
        if lst[i] % 2:
            numeriDispari.append(lst[i])
            posizioniNumeriDispari.append(i)

    print(f'posizioni: {posizioniNumeriDispari}, valori: {numeriDispari}')
    return numeriDispari, posizioniNumeriDispari

def bubbleSort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] < lst[j]:
                lst[j], lst[i] = lst[i], lst[j]
    return lst
    
def ordina(lst):
    numeriDispari, posizioniNumeriDispari = getNumeriDispari(lst)
    print(f'posizioni: {posizioniNumeriDispari}, valori: {numeriDispari}')
    numeriDispari = bubbleSort(numeriDispari)
    for i in range(len(posizioniNumeriDispari)):
        print(f'posizione: {posizioniNumeriDispari[i]}, valore: {numeriDispari[i]}')
        lst[posizioniNumeriDispari[i]] = numeriDispari[i]

    return lst

if __name__ == "__main__":
    import random
    seed = int(input())
    random.seed(seed)
    n = int(input())
    if n < 0:
        n = -n
        value = 3**n
    else:
        value = n+2
    n+=2
    lst = []
    for i in range(n):
        lst.append(random.randint(1,20))

    print(f"Input: {lst} - Risultato: {ordina(lst.copy())}")
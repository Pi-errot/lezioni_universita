def rimuoviDuplicati(lst):
    decremento = 0
    
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i == j:
                continue
            if lst[i-decremento] == lst[j-decremento]:
                lst.pop(j)
                decremento+=1

def trova_feste(lst1, lst2):
    rimuoviDuplicati(lst1)
    rimuoviDuplicati(lst2)
    feste = 0
    
    for festa in lst1:
        if not (festa in lst2):
            feste+=1
    for festa in lst2:
        if festa in lst1:
            feste+=1
    return feste

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
    lst1 = []
    lst2 = []
    for i in range(n):
        lst1.append(random.randint(1,value))
        lst2.append(random.randint(1,value))
    
    numero = random.randint(1, value)
    print(f"Input, lst1: {lst1}, lst2: {lst2} - Risultato: {trova_feste(lst1.copy(), lst2.copy())}")
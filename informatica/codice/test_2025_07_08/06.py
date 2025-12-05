# Si implementi una funzione calcolo(lst) che, ricevuta in input una lista di numeri interi lst, restituisca il numero di coppie (a, b) all'interno della lista per cui valgono tutte le seguenti proprietá:


def calcolo(numeri):
    coppie = []
    for i in range(len(numeri)):
        for j in range(i+1, len(numeri)):
            num = numeri[i]
            num2= numeri[j]
            if num == num2:
                continue
            if (num*num2)%2:
                continue
            maggiore = max(num, num2)
            minore = min(num, num2)
            if (maggiore - minore) < 4:
                continue
            tempRisultato = (maggiore, minore) 
            coppie.append(tempRisultato)
    return len(coppie)

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
        lst.append(random.randint(1,value))
    
    print(f"Input: {lst} - Risultato: {calcolo(lst.copy())}")
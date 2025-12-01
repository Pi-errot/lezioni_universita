def isPrimo(n):
    if n < 2:
        return False
    if n < 4:
        return True
    isdivisible = False
    for i in range(2, n):
        if isdivisible:
            break
        temp = (n % i) == 0
        print(f'numero: {n}, è divisibile per {i} ? {temp}')
        isdivisible = isdivisible or temp
    return not isdivisible


def filtra(lst):
    risultato = []
    for i in range(1, len(lst)-1):
        if not((lst[i-1] % 2) == 0 and (lst[i+1] % 2) == 1):
            continue
        numero = lst[i]
        numeroIsPrimo = isPrimo(numero)
        if numeroIsPrimo:
            risultato.append(numero)
    return risultato


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

    print(f"Input: {lst} - Risultato: {filtra(lst)}")
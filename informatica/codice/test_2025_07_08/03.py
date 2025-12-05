def decToBin(num,numeroBit):
    binario = []

    for _ in range(numeroBit):
        binario.append(0)

    isNegativo = not num>=0
    binario[0] = 0 if isNegativo else 1
    num = num if num>=0 else -num-1

    for contatore in range(numeroBit):
        binario[numeroBit-1-contatore] = (num^(not isNegativo))%2
        print(f'num pre divisione: {num}')
        num = num//2
        print(f'num post divisione: {num}')
        if(num == 0):
            break
    binario = binario[::-1]
    return binario

numero = 3
numeroBit = 12
print(f'risultato: {decToBin(numero, numeroBit)}')
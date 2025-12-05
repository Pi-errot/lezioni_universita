def conversioneBinToDec(numero):
    numeroSeparato = list(str(numero))
    totale = 0
    for i in range(0, len(numeroSeparato)):
        print(f'i: {i}, 2^i: {2**i}')
        totale += int(numeroSeparato[len(numeroSeparato)-1-i]) * 2**i

    return totale

numeroInput = 11000011100111000101000000000000
print(conversioneBinToDec(numeroInput)) 
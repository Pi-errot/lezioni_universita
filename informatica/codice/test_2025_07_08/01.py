def funzioneLogica(a,b,c):
    aDoppioImplicatoB = a == b
    negatoBDoppioImplicatoC = (not b) == c
    negatoADoppioImplicatoNegatoC = (not a) == (not c)
    # print(f'risultati parziali: {aDoppioImplicatoB} \t {negatoBDoppioImplicatoC} \t {negatoADoppioImplicatoNegatoC}')
    quasiRisultato = aDoppioImplicatoB and negatoBDoppioImplicatoC and negatoADoppioImplicatoNegatoC

    risultato = not quasiRisultato
    return risultato

casi = [False, True]

for a in casi:
    for b in casi:
        for c in casi:
            print(f"a:{a}, b:{b}, c:{c}, risultato:{funzioneLogica(a,b,c)}")
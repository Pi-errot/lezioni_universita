def occorrenze(lst):
    # Inserisci qui la tua implementazione
    occorrenze_lettere = {}
    for i in range(0, len(lst)):
        if not lst[i] in occorrenze_lettere:
            occorrenze_lettere[lst[i]] = {'apparizioni': 1, 'numero': lst[i]}
        else:
            occorrenze_lettere[lst[i]]['apparizioni'] += 1
    
    raw_ordinati = sorted(occorrenze_lettere.values(), key=lambda x: (-x['apparizioni'], x['numero']))
    #ordinati = []
    ordinati = [x['numero'] for x in raw_ordinati]
    #    print("Generato: ")
    #    print(ordinati)
    
    return ordinati


caso_1 = [-8, 6, 12, -10, -4, -9, 3, 12, 2, 3, 8, 0]
print(occorrenze(caso_1))
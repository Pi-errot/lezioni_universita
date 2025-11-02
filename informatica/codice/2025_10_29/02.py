a_p_partenza = ""
temp_a_p = ""
temp_budget = 0
def voli_con_a_p_corrispondente (volo):
    global temp_a_p
    (partenza,arrivo,budget) = volo
    return partenza == temp_a_p 

def voli_con_budget_rispettato (volo):
    global temp_budget
    (partenza,arrivo,budget) = volo
    return budget <= temp_budget

def trova_voli(a_p, b, voli):
    if (b < 0):
        return []
    global a_p_partenza
    global temp_a_p 
    global temp_budget

    if(a_p_partenza == ""):
       a_p_partenza = a_p

    temp_a_p = a_p
    temp_budget = b
    print("\n")
    # Inserisci qui la tua implementazione
    print("Areoporto di partenza: ", a_p)
    print("Budget di partenza: ", b)
    print("Voli pre filtri: ", voli)
    possibili_voli_per_a_p = list(filter(voli_con_a_p_corrispondente, voli))
    print("Voli post filtro aereoporto di partenza: ",possibili_voli_per_a_p)
    possibili_voli_per_budget = list(filter(voli_con_budget_rispettato, possibili_voli_per_a_p))

    print("Voli post filtro budget: ",possibili_voli_per_budget)
    if(len(possibili_voli_per_budget) == 0):
        print("Nessun volo trovato")
        return [a_p]
    
    risultati =  [a_p] if a_p != a_p_partenza else []
    for (partenza,arrivo,budget) in possibili_voli_per_budget:
        temp_a_p = a_p
        temp_budget = b
        temp_risultato = trova_voli(arrivo,temp_budget - budget, voli)
        if not (temp_a_p in risultati):
            risultati.extend(temp_risultato)
    print("Risultati: ", risultati)
    risultati = sorted(list(set(risultati)))
    return risultati

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

    value = n

    aereporti = ["lamezia", "milano", "roma", 
                "catania", "napoli", "bari", 
                "torino", "bergamo", "verona", 
                "bologna"]

    na = len(aereporti)
    
    a_p = random.choice(aereporti)
    b = random.randint(0, value*2)

    voli = []
    p = 0.2
    for i in range(na):
      for j in range(na):
        if i == j:
          continue
        x = random.random()
        if x <= p:
          c = random.randint(1, value)
          voli.append((aereporti[i], aereporti[j], c))

    
    res = trova_voli(a_p, b, voli)
    print(res)
    # res.sort()
    # print(f"Input: {a_p}, {b}, {voli} - Risultato: {res}")
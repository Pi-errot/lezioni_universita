#     Scrivere una funzione ricorsiva chiamata anchestor che, dato una lista con l'elenco di coppie padre-figlio e due stringhe rappresentanti un potenziale antenato (person1) e un potenziale discendente (person2), determini se il primo è un antenato del secondo. Si può assumere che la lista in input rispetti le seguenti condizioni:
#     Il nome identifica univocamente ciascuna persona presente nella lista.
#     Ogni figlio ha al massimo un padre.
#     Non sono presenti cicli nella relazione padre-figlio (ad esempio, non può verificarsi il caso in cui Mario è il padre di Antonio, che è il padre di Giovanni, che a sua volta è il padre di Mario).
# Esempio. Se la lista fosse: father_son = [("antonio", "alberto"), ("francesco", "simone"), ("francesco", "mario"), ("angelo", "andrea"), ("antonio", "marco"), ("marco", "gabriele"), ("gabriele", "eugenio")] la funzione anchestor(father_son, "antonio", "eugenio")) restituirebbe True perché antonio è il padre di alberto e di marco, marco è il padre di gabriele e gabriele è il padre di eugenio. Quindi, antonio è un antenato di eugenio.
# Bonus: Scrivere anche la versione iterativa della funzione.


def anchestor(famiglia, padre, figlio):
    if padre == figlio:
        return True
    figliDiPadre = []
    for (tempPadre,tempFiglio) in famiglia:
        if tempPadre == padre:
            figliDiPadre.append(tempFiglio)
    totalResult = False
    for tempFiglio in figliDiPadre:
        totalResult = totalResult or anchestor(famiglia, tempFiglio, figlio)
    return totalResult

father_son = [("antonio", "alberto"), ("francesco", "simone"), ("francesco", "mario"), ("angelo", "andrea"), ("antonio", "marco"), ("marco", "gabriele"), ("gabriele", "eugenio")] 

print(anchestor(father_son, "antonio", "eugenio"))
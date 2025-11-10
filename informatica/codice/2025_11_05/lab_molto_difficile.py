# BONUS (molto difficile). Scrivere una funzione max_sum_non_adjacent(lst) che riceve una lista di numeri interi positivi lst e calcola la somma massima ottenibile sommando elementi non adiacenti nella lista.
# Esempio: max_sum_non_adjacent([2, 1, 1, 1, 10, 4, 6, 9]) restituisce 22 (dato dalla somma di 2, 1, 10 e 9).

def checkNextThreeAndReturnPositionOffset(miniArr):
    # print("Mini arr:", miniArr)
    indexMaxPos = 0
    for i in range(1, len(miniArr)):
        if miniArr[indexMaxPos] < miniArr[i]:
            indexMaxPos = i
    return indexMaxPos

def _max_sum_non_adjacent(arr):
    sum = 0
    choosenValues = []
    offset=0
    def getOffset():
        return offset + 2
    i = 0
    while i < len(arr):
        # print("Indice:",i)
        # print("Offset:",getOffset())
        offset = checkNextThreeAndReturnPositionOffset(arr[i:i+3]) % 2
        choosenValue = arr[i+offset]
        choosenValues.append([i+offset,choosenValue])
        sum+= choosenValue
        i += getOffset()
    
    # print(choosenValues) 
    return sum

def max_sum_non_adjacent(lst):
    max_sum = 0
    max_without_prev = 0

    for i in range(len(lst)):
        with_i = max_without_prev + lst[i]
        max_without_prev = max_sum
        print("with_i:", with_i)
        print("max_without_prev:", max_without_prev)
        if with_i > max_sum:
            max_sum = with_i
            print("max_sum: ", max_sum)
        print()
    return max(max_sum, max_without_prev)

def _max_sum_non_adjacent(lst):
    sum = 0
    i = 0
    while i < len(lst):
        sum_couple = lst[i] + lst[i+2]
        sum_next_couple = lst[i+1] + lst[i+3]
        if sum_couple < sum_next_couple:
            i+=5
            sum += sum_next_couple
        else:
            i+=4
            sum += sum_couple
    return sum
arrInput = [4, 7, 4, 4, 7]
print(max_sum_non_adjacent(arrInput))
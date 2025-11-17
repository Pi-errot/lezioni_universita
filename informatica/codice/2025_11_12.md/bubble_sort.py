array = [10, 8, 7, 6, 5, 3, 4, 1, 2, 0]

def bubble_sort(arr):
    itemScambiati = True
    while(itemScambiati):
        itemScambiati = False
        for j in range(0, len(array)-1):
            if(array[j] > array[j+1]):
                itemScambiati = True
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

print(bubble_sort(array))

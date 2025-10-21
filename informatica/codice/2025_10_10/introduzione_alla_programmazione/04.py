# Scrivere un programma che riceva in input tre numeri interi dall'utente e stampi se il primo è maggiore della somma tra il secondo e il terzo.

array = [0,0,0]
for i in range(0,3):
    array[i] = int(input("Inserisci un numero: "))

if array[0] > array[1] + array[2]:
    print("Il primo è maggiore della somma degli altri 2 numeri")
else:
    print("Il primo non è maggiore della somma degli altri 2 numeri")
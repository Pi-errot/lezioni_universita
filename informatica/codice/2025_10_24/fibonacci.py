def fibonacci_ricorsivo(n):
    if n == 0 or n == 1:
        return n
    return fibonacci_ricorsivo(n-1) + fibonacci_ricorsivo(n-2)

def fibonacci_iterativo(n):
    a = b = 1
    for _ in range(2, n):
        c = a + b
        a = b
        b = c
    return c

print("Iterativo: " , fibonacci_iterativo(int(input("Inserisci un numero intero: "))))
print("Ricorsivo: " , fibonacci_ricorsivo(int(input("Inserisci un numero intero: "))))

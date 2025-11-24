# def fib_ricorsivo(n):
    # if n == 0 or n==1:
        # return n
    # return fib_ricorsivo(n-1) + fib_ricorsivo(n-2)
# 
# numero = 3
# print(f"Fibonacci di {numero}: ", fib_ricorsivo(numero))
# 
# for i in range(10):
#     print("Numero passato: ", i)
#     print("Risultato di fibonacci: ", fib_ricorsivo(i))



def fattoriale_ricorsivo(n):
    if n == 0 or n == 1:
        return n
    return n * fattoriale_ricorsivo(n-1)

print(fattoriale_ricorsivo(4))
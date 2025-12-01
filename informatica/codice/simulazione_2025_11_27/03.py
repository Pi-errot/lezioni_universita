def numero(n):
    if n < 0:
        return n
    if n == 0 or n == 1:
        return n
    if n > 49:
        return int(n%2)
    if n % 2 == 0:
        return int(numero(n/2))
    if n % 2:
        return 1 + int(numero((n-1)/2+1))

if __name__ == "__main__":
    n = int(input())
    if n < 0:
        for i in range(0, 52):
            print(f"Input: {i} - Risultato: {numero(i)}")
    else:
        print(f"Input: {n} - Risultato: {numero(n)}")
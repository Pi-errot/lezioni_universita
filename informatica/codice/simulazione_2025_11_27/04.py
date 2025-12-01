def battaglia_navale(matrice, colpi):
    for colpo in colpi:
        x,y = colpo
        if not (0 <= x < len(matrice)) or not (0 <= y < len(matrice[0])):
            # print(f'fuori dalla matrice: {colpo}')
            continue
        if matrice[x][y]:   
            matrice[x][y] = 0

    naviRimaste = 0
    for rigo in matrice:
        for nave in rigo:
            naviRimaste += nave
    return naviRimaste


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
    M = [[random.randint(0,1) for _ in range(n)] for _ in range(n)]
    
    m = random.randint(0,2*n)
    colpi = [(random.randint(n-5,n+5),random.randint(n-5,n+5)) for _ in range(m)]

    my_str = "\n".join([" ".join([str(el) for el in row]) for row in M])
    print(f"Input: \n{my_str}\n{colpi}\nRisultato:\n{battaglia_navale(M.copy(), colpi.copy())}")
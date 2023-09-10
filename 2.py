import random
def isnieparzysta(num):
    if num % 2 == 0:
        return False
    else:
        return True

N = int(input())
t = int(input())
def program(N, t):
    tablica = [[random.randrange(1, 1000) for i in range(t)] for _ in range(N)]
    print(tablica)
    for x in range(0, len(tablica)):
        for y in range(0, len(tablica[x])):
            if isnieparzysta(tablica[x][y]):
                tablica[x][y] = True
            else:
                tablica[x] = [False]
                break
        for b in range(len(tablica[x])):
            if tablica[x][b] == True:
                tablica[x] = [True]
            else:
                tablica[x] = [False]
                break

    print(tablica)
    for a in range(0, len(tablica)):
        if tablica[a][0] == True:
                continue
        else:
            return False
    return True
print(program(N, t))
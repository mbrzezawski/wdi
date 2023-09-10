import math
def sito(num):
    tablica = [True] * (num + 1)
    tablica_z_prime = []
    for i in range(2, int(math.sqrt(num)) + 1):
        if tablica[i]:
            for k in range(i*i, num + 1, i):
                tablica[k] = False
    for i in range(2, num + 1):
        if tablica[i]:
            tablica_z_prime.append(i)
    return tablica_z_prime
print(sito(100))

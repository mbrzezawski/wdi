def czy_zlozona_z_nieparzysta(num):
    while num != 0:
        temp_num = num
        temp_num %= 10
        if temp_num % 2 == 0:
            return False
        num //= 10
    return True

def zadanie2(T):
    n = len(T)
    for i in range(0, n):
        for j in range(0, len(T[i])):
            if czy_zlozona_z_nieparzysta(T[i][j]):
                break
        else:
            return False
    return True

T = [[354, 54, 33, 65], [153, 421, 324, 32], [32, 576, 213, 43]]
print(zadanie2(T))


def przy1_liczba_parzysta(num):
    while num != 0:
        temp_num = num
        temp_num %= 10
        if temp_num % 2 == 0:
            return True
        num //= 10
    else:
        return False

def zadanie3(T):
    n = len(T)
    for i in range(0, n):
        for j in range(0, len(T[i])):
            if przy1_liczba_parzysta(T[i][j]):
                continue
            else:
                break
        else:
            return True
    else:
        return False

T = [[354, 54, 33, 65], [153, 421, 324, 32], [32, 576, 213]]
print(zadanie3(T))
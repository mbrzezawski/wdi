def zadanie4(T):
    n = len(T)
    sum_k = 0
    sum_w = 0
    max_ = 0
    wiersz, kolumna = 0, 0
    for i in range(0, n):
        for j in range(0, n):
            sum_k += T[j][i]
            sum_w += T[i][j]
            if sum_k / sum_w > max_:
                max_ = sum_k / sum_w
                wiersz, kolumna = i, j
        sum_k = 0
        sum_w = 0

    return wiersz, kolumna

T = [[54, 33, 65], [13, 421, 324], [32, 576, 213]]
print(zadanie4(T))

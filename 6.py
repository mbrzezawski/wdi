def distane(T):
    max_index = 0
    min_index = 0
    n = len(T)
    for i in range(1, n):
        for j in range(n):
            if T[i][j] > T[max_index][j]:
                max_index = i
                break
            if T[i][j] < T[min_index][j]:
                min_index = i
                break
    return max_index - min_index

T = [[0,1,1,1,0], [1,0,0,1,0], [1,1,0,0,0], [0,1,1,1,1], [1,1,1,0,0]]
print(distane(T))
import random
def fun(T):
    n = len(T)
    leng = 2
    max_leng = 1
    q = T[1] / T[0]
    for i in range(2, n):
        if T[i] == T[i - 1] * q:
            leng += 1
        else:
            max_leng = max(max_leng, leng)
            leng = 2
            q = T[i] / T[i - 1]
    return max_leng
a = int(input())
T = [random.randint(0, 100) for _ in range(a)]
print(T)
print(fun(T))


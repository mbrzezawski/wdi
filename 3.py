import random
def fun(T):
    n = len(T)
    max_leng = 1
    leng = 2
    r = T[1] - T[0]
    for i in range(2, n):
        if T[i] == T[i - 1] + r:
            leng += 1
        else:
            max_leng = max(max_leng, leng)
            leng = 2
            r = T[i] - T[i - 1]
    return max_leng

a = int(input())
T = [random.randint(0, 100) for _ in range(a)]
print(T)
print(fun(T))
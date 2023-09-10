import math
def isprime(num):
    if num == 2 or num == 3:
        return True
    if num <= 1 or num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i < int(math.sqrt(num) + 1):
        if num % i == 0:
            return False
        i += 2
        if num % i == 0:
            return False
        i += 4
    else:
        return True
def divide(N,k):
    if N == 0:
        if isprime(k):
            return True
        else:
            return False
    dlugosc = int(math.log10(N) + 1)
    for i in range(1, dlugosc + 1):
        if isprime(N % (10 ** i)):
            if divide(N // 10 ** i, k+1):
                return True
            else:
                return False
print(divide(42,0))
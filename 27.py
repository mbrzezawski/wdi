import math
def zamiana(num, system):
    znaki = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    wynik = ""
    while num > 0:
        indeks = num % system
        wynik = znaki[indeks] + wynik
        num //= system
    return wynik


num = 21345
print(int(math.log10(num) + 1))
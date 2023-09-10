def print_tab(tab):
    for line in tab:
        print(line)

n = int(input())

tab = [[0]*n for _ in range(n)]

x, y = 0, 0
i = 1
maxi = n ** 2

while i <= maxi:
    while y < n - 1 and tab[x][y+1] == 0:
        tab[x][y] = i
        y += 1
        i += 1
    while x < n - 1 and tab[x+1][y] == 0:
        tab[x][y] = i
        x += 1
        i += 1
    while y > 0 and tab[x][y-1] == 0:
        tab[x][y] = i
        y -= 1
        i += 1
    while x > 0 and tab[x-1][y] == 0:
        tab[x][y] = i
        x -= 1
        i += 1
    if i == maxi:
        tab[x][y] = i
        break
print_tab(tab)


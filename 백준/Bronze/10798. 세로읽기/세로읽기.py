from sys import stdin
m, n = 15,5
a = [['@']*m for _ in range(n)]

for i in range(n):
    k = stdin.readline().strip('\n')
    for j in range(len(k)):
        a[i][j] = k[j]
for i in range(m):
    for j in range(n):
        if a[j][i] == '@':
            continue
        else:
            print(a[j][i], end='')
from sys import stdin
from collections import deque
#k = stdin.readline().strip('\n')
arr = []
tmp = []
n = int(stdin.readline())
for i in range(n):
    k = list(stdin.readline().strip('\n'))
    arr.append(k)
for i in range(n):
    k = list(stdin.readline().strip('\n'))
    tmp.append(k)

def BFS(x, y):
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    cnt = 0
    for i in range(8):
        x_ = x + dx[i]
        y_ = y + dy[i]
        if x_ < 0 or x_ >= n or y_ < 0 or y_ >= n:
            continue
        if arr[x_][y_] == '*':
            cnt += 1
    tmp[x][y] = str(cnt)
        
a = 0
for i in range(n):
    for j in range(n):
        if tmp[i][j] == 'x' and arr[i][j] == '.':
            BFS(i, j)
        if tmp[i][j] == 'x' and arr[i][j] == '*':
            a += 1

if a > 0:
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '*':
                tmp[i][j] = '*'

for i in range(n):
    for j in range(n):
        print(tmp[i][j], end='')
    print()
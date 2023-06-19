from sys import stdin
from collections import deque
import re
N, M = map(int, stdin.readline().split())
arr = [[] for i in range(N)]
for i in range(N):
    arr[i] = list(stdin.readline().strip('\n').split(' '))
queue = deque()
def BFS(x, y):
    #상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue.append([x, y])
    while queue:
        [a, b] = queue.popleft()
        for i in range(4):
            x_ = (a + dx[i])%N #0~N-1
            y_ = (b + dy[i])%M #0~M-1
            if arr[x_][y_] == '0':
                arr[x_][y_] = '1'
                queue.append([x_, y_])
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == '0':
            BFS(i, j)
            cnt += 1
print(cnt)
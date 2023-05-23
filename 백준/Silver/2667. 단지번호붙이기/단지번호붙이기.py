from sys import stdin
from collections import deque
#k = stdin.readline().strip('\n')
n = int(stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, stdin.readline().strip('\n'))))
result = []

def BFS(x, y):
    #상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    arr[x][y] = 0 
    cnt = 1
   
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            if x_ < 0 or x_ >= n or y_ < 0 or y_ >= n: #인덱스가 범위 벗어난 경우
                continue
            if arr[x_][y_] == 0:
                continue
            if arr[x_][y_] == 1:
                arr[x_][y_] = 0 #재방문 금지
                cnt += 1
                queue.append((x_, y_))
    return cnt

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            result.append(BFS(i, j))
print(len(result))
result.sort()
for i in range(len(result)):
    print(result[i])
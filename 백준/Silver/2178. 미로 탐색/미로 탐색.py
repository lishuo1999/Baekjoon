from sys import stdin
from collections import deque

#k = stdin.readline().strip('\n')
a, b = map(int, stdin.readline().split())
arr = []
for i in range(a):
    arr.append(list(map(int, stdin.readline().strip('\n'))))
def BFS(x, y):
    #상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            if x_ < 0 or x_ >= a or y_ < 0 or y_ >= b: #인덱스가 범위 벗어난 경우
                continue
            if arr[x_][y_] == 0: #0인 경우
                continue
            if arr[x_][y_] == 1:
                arr[x_][y_] = arr[x][y] + 1
                queue.append((x_, y_))
    return arr[a-1][b-1]

print(BFS(0, 0))
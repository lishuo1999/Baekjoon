from sys import stdin
from collections import deque
#k = stdin.readline().strip('\n')
n = int(stdin.readline())
target = int(stdin.readline())
arr = [[0 for j in range(n)] for i in range(n)]
num = 1
x, y = int(n/2), int(n/2)
arr[x][y] = num
result = []
if num == target:
    result.append(x)
    result.append(y)
num += 1

def fill(x, y, cnt, num, target, result):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    arr[x-1][y] = num # 위로 한칸 이동
    x -= 1
    if num == target:
        result.append(x)
        result.append(y)
    num += 1 
    for i in range(4):
        if i == 0: #우
            for j in range(cnt*2-1):
                x += dx[i]
                y += dy[i]
                arr[x][y] = num
                if num == target:
                    result.append(x)
                    result.append(y)
                num += 1
        elif i == 1: #하
            for j in range(cnt*2):
                x += dx[i]
                y += dy[i]
                arr[x][y] = num
                if num == target:
                    result.append(x)
                    result.append(y)
                num += 1
        elif i == 2: #좌
            for j in range(cnt*2):
                x += dx[i]
                y += dy[i]
                arr[x][y] = num
                if num == target:
                    result.append(x)
                    result.append(y)
                num += 1
        else: #상
            for j in range(cnt*2):
                x += dx[i]
                y += dy[i]
                arr[x][y] = num
                if num == target:
                    result.append(x)
                    result.append(y)
                num += 1
    return num, result
    
for i in range(int(n/2)):
    num, result = fill(x, y, i+1, num, target, result)
    x -= 1
    y -= 1
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()
print(result[0]+1, result[1]+1)
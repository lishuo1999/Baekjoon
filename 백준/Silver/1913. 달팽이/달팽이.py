N = int(input())
K = int(input())

arr = [[0 for j in range(N)] for i in range(N)]
num = 1
arr[int(N/2)][int(N/2)] = num
x, y = int(N/2), int(N/2)
for cnt in range(1, int(N/2)+1):
    dx = [0, 1, 0, -1] #우, 아래, 좌, 위
    dy = [1, 0, -1, 0]
    x += dx[3]
    y += dy[3]
    num += 1
    arr[x][y] = num
    for i in range(4):
        if i == 0: #오른쪽
            for j in range(2*cnt-1):
                x += dx[i]
                y += dy[i]
                num += 1
                arr[x][y] = num
        elif i == 1: #아래 
            for j in range(2*cnt):
                x += dx[i]
                y += dy[i]
                num += 1
                arr[x][y] = num
        elif i == 2: #왼쪽
            for j in range(2*cnt):
                x += dx[i]
                y += dy[i]
                num += 1
                arr[x][y] = num
        elif i == 3: #위
            for j in range(2*cnt):
                x += dx[i]
                y += dy[i]
                num += 1
                arr[x][y] = num

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
        if arr[i][j] == K:
            x = i
            y = j
    print()
print(x+1, y+1)
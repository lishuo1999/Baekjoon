from sys import stdin
from collections import deque
T = int(stdin.readline())

def rotation(n, arr, angle):
    if angle >= 0: #시계방향
        cnt = int(angle / 45) # 회전 횟수
        for k in range(cnt): 
            for i in range(int(n/2)):
                tmp = arr[i][i]
                arr[i][i] = arr[int(n/2)][i]
                arr[int(n/2)][i] = arr[n-i-1][i]
                arr[n-i-1][i] = arr[n-i-1][int(n/2)]
                arr[n-i-1][int(n/2)] = arr[n-i-1][n-i-1]
                arr[n-i-1][n-i-1] = arr[int(n/2)][n-i-1]
                arr[int(n/2)][n-i-1] = arr[i][n-i-1]
                arr[i][n-i-1] = arr[i][int(n/2)]
                arr[i][int(n/2)] = tmp
    else: #반시계방향
        angle = abs(angle)
        cnt = int(angle / 45)
        for k in range(cnt): 
            for i in range(int(n/2)):
                tmp = arr[i][i]
                arr[i][i] = arr[i][int(n/2)]
                arr[i][int(n/2)] = arr[i][n-i-1]
                arr[i][n-i-1] = arr[int(n/2)][n-i-1]
                arr[int(n/2)][n-i-1] = arr[n-i-1][n-i-1]
                arr[n-i-1][n-i-1] = arr[n-i-1][int(n/2)]
                arr[n-i-1][int(n/2)] = arr[n-i-1][i]
                arr[n-i-1][i] = arr[int(n/2)][i]
                arr[int(n/2)][i] = tmp
arr_sum = [[] for i in range(T)]
for cnt in range(T):
    n, angle = map(int, stdin.readline().split())
    arr = [[] for i_ in range(n)]
    for i in range(n):
        line = list(map(int, stdin.readline().split()))
        arr[i] = line
    rotation(n, arr, angle)
    arr_sum[cnt] = arr
for k in range(T):
    for i in range(len(arr_sum[k])):
        for j in range(len(arr_sum[k][i])):
            print(arr_sum[k][i][j], end=' ')
        print()
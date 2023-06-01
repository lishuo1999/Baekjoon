from sys import stdin
from collections import deque
#k = stdin.readline().strip('\n')

def change(a, b):
    if a == 1: # 남학생
        for i in range(b-1, len(arr), b):
            if arr[i] == 0:
                arr[i] = 1
            else:
                arr[i] = 0
    if a == 2: #여학생
        if arr[b-1] == 0:
                arr[b-1] = 1
        else:
            arr[b-1] = 0
        left = b-2
        right = b
        while 1:
            if left < 0 or right >= len(arr):
                break
            if arr[left] != arr[right]:
                break
            if arr[left] == 0:
                arr[left], arr[right] = 1, 1
            else:
                arr[left], arr[right] = 0, 0
            left -= 1
            right += 1
    
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
k = int(stdin.readline())
for i in range(k):
    a, b = map(int, stdin.readline().split())
    change(a, b)
cnt = 0
for i in range(len(arr)):
    print(arr[i], end=' ')
    cnt += 1
    if cnt == 20:
        cnt = 0
        print()
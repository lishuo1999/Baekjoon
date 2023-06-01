from sys import stdin
from collections import deque
#k = stdin.readline().strip('\n')
k = int(stdin.readline())
arr = [[] for i in range(1 + (k-1)*4)]
for i in range(1 + (k-1)*4):
    arr[i] = list(('*'*(1 + (k-1)*4)))

for i in range(int(len(arr)/2)+1):
    if i % 2 == 0:
        cnt = i #공백의 개수
        for j in range(int(len(arr[i])/2)):
            if j % 2 == 1 and cnt > 0:
                arr[i][j] = ' '
                arr[i][j-1-i] = ' '
                cnt -= 2
    else:
        cnt = i+1 #별의 개수
        for j in range(int(len(arr[i])/2) + 1):
            if j % 2 == 0 and cnt > 0:
                cnt -= 2
            else:
                arr[i][j] = ' '
                arr[i][len(arr[i])-1-j] = ' '

for i in range(int(len(arr)/2)):
    arr[len(arr)-1-i] = arr[i]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end='')
    print()
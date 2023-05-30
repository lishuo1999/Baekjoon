from sys import stdin
from collections import deque
#k = stdin.readline().strip('\n')
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

a = [n, 0] # 첫번째 원소 현금, 두번째 원소 주식 개수
for i in range(len(arr)):
    a[1] += int(a[0] // arr[i])
    a[0] %= arr[i]
J = a[0] + (arr[13] * a[1])
b = [n, 0]
cnt_up = 0
cnt_down = 3
for i in range(1, len(arr)):
    if arr[i-1] < arr[i]:
        cnt_up += 1
        cnt_down = 3
        if cnt_up == 3:
            cnt_up -= 1
            #매도
            b[0] += b[1]*arr[i]
            b[1] = 0
    elif arr[i-1] > arr[i]:
        cnt_down -= 1
        cnt_up = 0
        if cnt_down == 0:
            cnt_down += 1
            #매수
            b[1] += int(b[0] // arr[i])
            b[0] %= arr[i]
    else:
        continue
S = b[0] + (arr[13] * b[1])
if J > S:
    print('BNP')
elif S > J:
    print('TIMING')
else:
    print('SAMESAME')
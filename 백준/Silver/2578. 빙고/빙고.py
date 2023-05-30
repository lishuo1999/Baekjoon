from sys import stdin
from collections import deque
#k = stdin.readline().strip('\n')
arr = []
tmp = []
def check(arr):
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    cnt_4 = 0
    result = 0
    for i in range(5):
        cnt_3 += arr[i][i]
        cnt_4 += arr[i][4-i]
        for j in range(5):
            cnt_1 += arr[i][j]
            cnt_2 += arr[j][i]
        if cnt_1 == -5:
            result += 1
        if cnt_2 == -5:
            result += 1
        cnt_1 = 0
        cnt_2 = 0
            
    if cnt_3 == -5:
        result += 1
    if cnt_4 == -5:
        result += 1
    return result

for i in range(5):
    k = list(map(int, stdin.readline().split()))
    arr.append(k)
for i in range(5):
    k = list(map(int, stdin.readline().split()))
    tmp.append(k)
cnt = 0
for i in range(5):
    for j in range(5):
        for z in range(5):
            if tmp[i][j] in arr[z]:
                arr[z][arr[z].index(tmp[i][j])] = -1
                cnt += 1
                #빙고 여부
                if check(arr) >= 3:
                    print(cnt)
                    exit()

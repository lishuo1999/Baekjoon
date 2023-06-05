from sys import stdin
from collections import deque
k = stdin.readline().strip('\n')
k = list(k)
tmp = []
flag = 0
def substitution(k, index, tmp):
    cnt = 0
    for i in range(index-len(tmp), index):
        k[i] = tmp[cnt]
        cnt += 1
    tmp.clear()
for i in range(len(k)):
    if k[i] == '<':
        flag = 1
        if len(tmp) > 0:
            substitution(k, i, tmp)
        continue
    elif k[i] == '>':
        flag = 0
        continue
    
    if flag == 0:
        if (k[i] >= 'a' and k[i] <= 'z') or (k[i] >= '0' and k[i] <= '9'):
            tmp.insert(0, k[i])
        else:
            substitution(k, i, tmp)
if len(tmp) > 0:
    substitution(k, len(k), tmp)
print(''.join(k))
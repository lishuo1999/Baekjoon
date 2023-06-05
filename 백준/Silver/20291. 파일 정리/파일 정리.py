from sys import stdin
from collections import deque
#k = stdin.readline().strip('\n')
n = int(stdin.readline())
arr = [[''] for i in range(n)]
for i in range(n):
    k = stdin.readline().strip('\n')
    index = k.index('.')
    arr[i] = k[index+1:]
result = {}
for i in range(len(arr)):
    if arr[i] in result:
        result[arr[i]] += 1
    else:
        result[arr[i]] = 1
result = dict(sorted(result.items()))
for key, value in result.items():
    print(key, value)
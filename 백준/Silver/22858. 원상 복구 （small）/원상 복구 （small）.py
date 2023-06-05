from sys import stdin
from collections import deque
import copy
n, k = map(int, stdin.readline().split())
end = list(stdin.readline().strip('\n').split(' '))
D = list(stdin.readline().strip('\n').split(' '))
result = [0 for i in range(n)]

for cnt in range(k):
    for i in range(n):
        result[int(D[i])-1] = int(end[i])
    end = copy.deepcopy(result)
for i in range(n):
    print(result[i], end=' ')
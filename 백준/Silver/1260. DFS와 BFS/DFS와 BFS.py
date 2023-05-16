from sys import stdin
from collections import deque
#k = stdin.readline().strip('\n')
n1, n2, n3 = map(int, stdin.readline().split())
arr = [[] for i in range(n1)]
for i in range(n2):
    a, b = map(int, stdin.readline().split())
    arr[a-1].append(b-1)
    arr[a-1] = list(set(arr[a-1]))
    arr[b-1].append(a-1)
    arr[b-1] = list(set(arr[b-1]))
for i in arr:
    i.sort() #i는 각 내부 리스트 의미
visited = [0]*n1
queue = deque()
def DFS(k):
    visited[k] = 1
    print(k+1, end=' ')
    for i in arr[k]:
        if visited[i] == 0:
            DFS(i)
def BFS(k):
    visited = [0]*n1
    visited[k] = 1
    queue.append(k)
    while queue:
        k = queue.popleft()
        print(k+1, end=' ')
        for i in arr[k]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1

DFS(n3-1)
print()
BFS(n3-1)
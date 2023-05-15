from sys import stdin
#k = stdin.readline().strip('\n')
n1 = int(stdin.readline())
n2 = int(stdin.readline())
arr = [[0]*n1 for i in range(n1)]
for i in range(n2):
    a, b = map(int, stdin.readline().split())
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)
visited = [0]*n1

def DFS(k):
    visited[k] = 1
    for i in arr[k]:
        if visited[i] == 0:
            DFS(i)
DFS(0)
print(sum(visited)-1)
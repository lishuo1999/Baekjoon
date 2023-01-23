from sys import stdin
#k = stdin.readline().strip('\n')
n = int(stdin.readline())
arr = []
for i in range(n):
    k = int(stdin.readline())
    arr.append(k)
arr.sort(reverse=True) #내름차순 정렬
result = 0
for i in range(n):
    if arr[i] - (i+1-1) > 0:
        result += arr[i] - (i+1-1)
print(result)
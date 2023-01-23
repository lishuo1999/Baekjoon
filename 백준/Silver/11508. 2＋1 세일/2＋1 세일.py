from sys import stdin
#k = stdin.readline().strip('\n')
n = int(stdin.readline())
arr = []
for i in range(n):
    k = int(stdin.readline())
    arr.append(k)
arr.sort(reverse=True) #내림차순
result = 0
for i in range(n):
    if (i+1) % 3 != 0:
        result += arr[i]
print(result)
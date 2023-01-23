from sys import stdin
#k = stdin.readline().strip('\n')
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
arr.sort() #오름차순
result = 0
cnt = 0
for i in range(n):
    cnt += arr[i]
    result += cnt
print(result)
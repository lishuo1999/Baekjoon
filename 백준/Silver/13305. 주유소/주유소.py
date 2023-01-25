from sys import stdin
#k = stdin.readline().strip('\n')
n = int(stdin.readline())
arr1 = list(map(int, stdin.readline().split()))
arr2 = list(map(int, stdin.readline().split()))
result = 0
result += arr1[0]*arr2[0]
for i in range(1, n-1):
    cnt = min(arr2[0:i+1])
    result += cnt*arr1[i]
print(result)
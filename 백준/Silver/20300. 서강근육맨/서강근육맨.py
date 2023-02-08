from sys import stdin
#k = stdin.readline().strip('\n')
n = int(stdin.readline())

arr = list(map(int, stdin.readline().split()))
arr.sort() #오름차순
result = []
if n % 2 == 0:
    for i in range(n//2):
        result.append(arr[i] + arr[n-1-i])
else:
    for i in range(n//2):
        result.append(arr[i] + arr[n-2-i])
    result.append(arr[n-1])
print(max(result))
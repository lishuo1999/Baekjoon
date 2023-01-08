from sys import stdin
#k = stdin.readline().strip('\n')
n = int(stdin.readline())
arr = []
for i in range(n):
    k = int(stdin.readline())
    arr.append(k)
arr.sort() #오름차순 정렬
for i in range(n):
    arr[i] = arr[i]*(n-i)
print(max(arr))
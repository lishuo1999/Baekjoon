from sys import stdin
#k = stdin.readline().strip('\n')
n = int(stdin.readline())
k = stdin.readline().strip('\n')
first = k[0]
arr = list(map(list, k.split(first)))
arr = list(filter(None, arr))
print(len(arr) + 1)
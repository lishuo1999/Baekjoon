from sys import stdin
k = stdin.readline().strip('\n')
#n = int(stdin.readline())
result = 0
arr = list(map(str, k.split('-')))
for i in range(len(arr)):
    tmp = arr[i].split('+')
    k = 0
    for j in range(len(tmp)):
        tmp[j] = tmp[j].lstrip('0') #왼쪽 0제거
        k += int(tmp[j])
    if i == 0:
        result += k
    else:
        result -= k
print(result)
    
from sys import stdin
k = int(stdin.readline())
result = 0
lis = []
for i in range(k):
    a = stdin.readline()
    tmp = 0
    lis.append(a[0])
    for j in range(1, len(a)-1): # 두번째 문자부터 검사
        if a[j] != a[j-1]:
            if a[j] not in lis:
                lis.append(a[j])
            else:
                tmp = 1
                break
    if tmp != 1:
        result += 1
    else:
        tmp = 0
    lis.clear()
print(result)
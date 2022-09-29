from sys import stdin
def test1(k): #통과: 0
    arr = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(k)):
        if k[i] in arr:
            return 0
    return 1
def test2(k): #실패: 1
    arr = ['a', 'e', 'i', 'o', 'u']
    cnt1, cnt2 = 0, 0
    for i in range(len(k)):
        if k[i] in arr: #모음인 경우
            cnt2 = 0
            cnt1 += 1
            if cnt1 >= 3:
                return 1
        else: #자음인 경우
            cnt1 = 0
            cnt2 += 1
            if cnt2 >= 3:
                return 1
    return 0
def test3(k):
    for i in range(0, len(k)-1):
        if k[i] == k[i+1] and (k[i] != 'e' and k[i] != 'o'):
            return 1
    return 0
while 1:
    k = stdin.readline().strip('\n')
    result = 0
    if k == 'end':
        break
    result += test1(k) + test2(k) + test3(k)
    if result >= 1:
        print("<"+ k +"> is not acceptable.")
    else:
        print("<"+ k +"> is acceptable.")
from sys import stdin
from collections import deque
#k = stdin.readline().strip('\n')
n = int(stdin.readline())
arr = [[] for i in range(11)]
result = 0
for i in range(n):
    a, b = map(int, stdin.readline().split())
    arr[a].append(b)
for i in range(11):
    if arr[i] != None and len(arr[i]) >= 2: #null이 아니고 2개 이상 들어간 경우
        k = arr[i][0] #첫번째 원소 저장
        for j in range(1, len(arr[i])): #안쪽 배열 두번째 원소부터 검사
            if k != arr[i][j]:
                result += 1
                k = arr[i][j] 
print(result)
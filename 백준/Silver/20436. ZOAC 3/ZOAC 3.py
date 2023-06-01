from sys import stdin
from collections import deque
#k = stdin.readline().strip('\n')
L, R = map(str, stdin.readline().strip('\n').split())
word = stdin.readline().strip('\n')
arr = [[] for i in range(3)]
arr[0] = list(map(str, 'qwertyuiop'))
arr[1] = list(map(str, 'asdfghjkl'))
arr[2] = list(map(str, 'zxcvbnm'))
left = [0, 0]
right = [0, 0]
result = 0
def find_xy(a):
    for i in range(3): #L의 좌표 찾기
        if str(arr[i]).find(a) == -1:
            continue
        x = i
        y = arr[i].index(a)
    return [x, y]
left = find_xy(L)
right = find_xy(R)

for i in range(len(word)):
    position = find_xy(word[i])
    if (position[0] < 2 and position[1] <= 4) or (position[0] == 2 and position[1] <= 3): #자음인 경우
        result += 1 + abs(position[0] - left[0]) + abs(position[1] - left[1])
        left = position
    else: #모음인 경우
        result += 1 + abs(position[0] - right[0]) + abs(position[1] - right[1])
        right = position
print(result)
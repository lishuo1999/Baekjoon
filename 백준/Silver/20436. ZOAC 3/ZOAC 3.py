arr = [['q', 'w', 'e','r', 't', 'y', 'u', 'i', 'o', 'p'],
['a','s','d','f','g','h','j','k','l'],
['z','x','c','v','b','n','m']]

a, b = input().split()
word = input()
result = len(word)
#입력받은 문자의 좌표 저장
x = []
y = []

def find_index(a): #좌표 찾기 함수
    k = 0
    for j in range(3):
        if a in arr[j]:
            x = j
            y = arr[j].index(a)
    if (x == 0 and 0 <= y and y <= 4) or (x == 1 and 0 <= y and y <= 4) or (x == 2 and 0 <= y and y <= 3):
        return x, y, 1 #왼손이면 1 반환
    else:
        return x, y, 0

a_x, a_y, a_k = find_index(a)
b_x, b_y, b_k = find_index(b)
for i in range(len(word)):
    x, y, k = find_index(word[i])
    if k == 1: #왼손인 경우
        result += abs(a_x - x) + abs(a_y - y)
        a_x = x
        a_y = y
    else: #오른손인 경우
        result += abs(b_x - x) + abs(b_y - y)
        b_x = x
        b_y = y

print(result)

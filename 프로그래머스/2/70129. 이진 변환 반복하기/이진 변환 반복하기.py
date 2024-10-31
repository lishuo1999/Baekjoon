def solution(s):
    a, b = 0, 0
    while s != '1':
        b += s.count('0')
        s = s.replace('0','') #모든 0 제거
        s = bin(len(s))[2:]
        a += 1

    answer = [a, b] #변환 횟수, 제거 0의 개수
    return answer
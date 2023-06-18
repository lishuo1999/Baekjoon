import re
def solution(babbling):
    answer = 0
    arr = ['aya', 'ye', 'woo', 'ma']
    for i in range(len(babbling)):
        for j in range(len(arr)):
            if babbling[i].find(arr[j]) != -1: #문자열 안에 존재
                cnt = babbling[i].count(arr[j]) #개수
                babbling[i] = babbling[i].replace(arr[j], str(j), cnt)
        #연속된 숫자 없고 모두 숫자인 경우만
        if babbling[i].isdigit():
            start = babbling[i][0]
            for k in range(1, len(babbling[i])):
                if babbling[i][k] == start:
                    start = -1
                    break
                else:
                    start = babbling[i][k]
            if start != -1:
                answer += 1
    return answer
def solution(n, words):
    answer = []
    #1. 끝말 이었는지
    #2. 중복인지
    a, b = 0, 0
    for i in range(1, len(words)):
        # 두번째 사람 첫번째 차례부터 검사
        if (words[i-1][-1] != words[i][0]) or (words[i] in words[0:i]): #끝말 이었는지
            a = (i % n) + 1
            b = int(i / n) + 1
            break
    answer = [a, b]
    return answer
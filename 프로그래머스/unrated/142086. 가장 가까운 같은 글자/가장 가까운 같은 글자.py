def solution(s):
    answer = []
    cnt = 0
    for i in range(len(s)):
        for j in range(i-1, -1, -1):
            if s[i] == s[j]:
                answer.append(i-j)
                cnt += 1
                break
        if cnt == 0:
            answer.append(-1)
        cnt = 0
    return answer
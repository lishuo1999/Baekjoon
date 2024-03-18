def solution(babbling):
    answer = 0
    result = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        for j in range(4):
            babbling[i] = babbling[i].replace(result[j],',')
        if babbling[i].islower() == False: #소문자 아예 없어야 함
            answer += 1
    return answer
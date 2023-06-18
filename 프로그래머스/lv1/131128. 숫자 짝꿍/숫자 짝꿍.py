def solution(X, Y):
    answer = ''
    inter = []
    #교집합
    inter = list(set(X) & set(Y))
    if len(X) != len(set(X)) or len(Y) != len(set(Y)):
        for i in range(len(inter)):
            for cnt in range(min(X.count(inter[i]), Y.count(inter[i]))-1):
                inter.append(inter[i])
                
    
    inter.sort(reverse=True)
    if len(inter) == 0 : #비어 있는 경우
        answer = '-1'
    else:
        inter = list(map(int, inter)) #정수형으로 변환
        if sum(inter) == 0:
            answer = '0'
        else:
            inter = list(map(str, inter))
            answer = ''.join(inter)
    return answer
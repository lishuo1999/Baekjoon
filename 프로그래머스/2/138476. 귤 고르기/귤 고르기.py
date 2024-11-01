def solution(k, tangerine):
    answer = 0
    tmp = 0
    dic = {}
    for i in range(len(tangerine)):
        if tangerine[i] not in dic:
            dic[tangerine[i]] = 1
        else:
            dic[tangerine[i]] += 1
    
    #cnt 기준으로 내림차순 정렬 (value 기준으로 정렬)
    dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    dic = dict(dic)
    for key, value in dic.items():
        tmp += value
        answer += 1
        if tmp >= k: 
            break
    return answer
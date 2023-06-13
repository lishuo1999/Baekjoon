def solution(survey, choices):
    answer = ''
    dic = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for i in range(len(survey)):
        sub = list(survey[i])
        if choices[i] <= 3:
            dic[sub[0]] += 4 - choices[i]
        elif choices[i] >= 5:
            dic[sub[1]] += choices[i] - 4
    arr = list(dic.items())
    for i in range(0,8,2):
        if arr[i][1] > arr[i+1][1]:
            answer += arr[i][0]
        elif arr[i][1] < arr[i+1][1]:
            answer += arr[i+1][0]
        else: #사전순
            if arr[i][0] < arr[i+1][0]:
                answer += arr[i][0]
            else:
                answer += arr[i+1][0]
    return answer
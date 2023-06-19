import re
def solution(dartResult):
    answer = 0
    
    arr_num = re.split(r'[SDT*#]', dartResult)
    arr_num = list(filter(None, arr_num))
    dartResult = re.split(r'[0-9]', dartResult)
    dartResult = list(filter(None, dartResult))
    arr_answer = [0 for i in range(len(arr_num))]
                                       
    for i in range(len(arr_num)):
        if dartResult[i][0] == 'S':
                arr_answer[i] = int(arr_num[i])
        elif dartResult[i][0] == 'D':
                arr_answer[i] = int(arr_num[i])**2
        elif dartResult[i][0] == 'T':
                arr_answer[i] = int(arr_num[i])**3
    
        if len(dartResult[i]) == 2: #옵션이 있는 경우
            if dartResult[i][1] == '*':
                arr_answer[i] *= 2 #두개
                if i >= 1:
                    arr_answer[i-1] *= 2
            elif dartResult[i][1] == '#':
                arr_answer[i] *= -1

    answer = sum(arr_answer)
    
    return answer
def solution(today, terms, privacies):
    answer = []
    dic = {}
    for i in range(len(terms)):
        a, b = terms[i].split()
        dic[a] = b
    arr = [[] for i in range(len(privacies))]
    for i in range(len(privacies)):
        arr[i] = privacies[i].split()
        arr[i][1] = dic[arr[i][1]]
    
    today_split = today.split('.')
    today_add = int(today_split[2]) + int(today_split[1])*28 + int(today_split[0])*28*12
    for i in range(len(arr)): #유효기간 지났는지 검사
        k = []
        k = arr[i][0].split('.')
        add = int(k[2]) + int(k[1])*28 + int(k[0])*28*12 + int(arr[i][1])*28
        if today_add >= add:
            answer.append(i+1)
    return answer
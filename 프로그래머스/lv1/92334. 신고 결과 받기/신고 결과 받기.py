def solution(id_list, report, k):
    answer = []
    answer = [0 for i in range(len(id_list))]
    report = list(set(report))
    id_stop = []
    tmp = [[] for i in range(len(id_list))] #각 id 신고한 id 리스트
    cnt = [0 for i in range(len(id_list))] #각 id 신고 당한 개수
    for i in range(len(report)):
        a, b = report[i].split()
        tmp[id_list.index(a)].append(b)
    for i in range(len(id_list)):
        for j in range(len(tmp)):
            cnt[i] += tmp[j].count(id_list[i])
        if cnt[i] >= k:
            id_stop.append(id_list[i]) #정리된 id 저장
    for i in range(len(tmp)):
        for j in range(len(id_stop)):
            if id_stop[j] in tmp[i]:
                answer[i] += 1
    return answer
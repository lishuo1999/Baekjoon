def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    inter = list(set(reserve) & set(lost))
    reserve = list(set(reserve) - set(inter))
    lost = list(set(lost) - set(inter))
    for i in range(len(lost)):
        if lost[i]-1 in reserve:
            reserve.remove(lost[i]-1)
        elif lost[i]+1 in reserve:
            reserve.remove(lost[i]+1)
        else:
            n -= 1
    answer = n
    return answer
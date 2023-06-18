def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zero = 0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            cnt += 1
        elif lottos[i] == 0:
            zero += 1
    first = cnt + zero
    last = cnt
    answer.append(min(6,7-first))
    answer.append(min(6,7-last))
    return answer
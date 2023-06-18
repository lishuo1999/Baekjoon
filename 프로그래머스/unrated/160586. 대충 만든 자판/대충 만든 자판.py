def solution(keymap, targets):
    answer = []
    for i in range(len(targets)):
        m = 101
        sum_ = 0
        for j in range(len(targets[i])):
            cnt = 0
            for key in range(len(keymap)):
                if targets[i][j] in keymap[key]:
                    index = keymap[key].find(targets[i][j])
                    if index+1 < m:
                        m = index+1
                else:
                    cnt += 1
            if cnt == len(keymap):
                cnt = -1
                break
            sum_ += m
            m = 101
        if cnt == -1:
            sum_ = -1
        answer.append(sum_)
    return answer
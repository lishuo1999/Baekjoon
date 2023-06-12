def solution(park, routes):
    answer = []
    for i in range(len(park)):
        if 'S' in park[i]:
            answer.append(i)
            answer.append(park[i].find('S'))
            break
    for i in range(len(routes)):
        R, C = routes[i].split()
        if R == 'N' and (answer[0]-int(C) >= 0):
            k = 0
            for j in range(answer[0], answer[0]-int(C)-1, -1):
                if park[j][answer[1]] == 'X':
                    k += 1
            if k == 0:
                answer[0] -= int(C)
        elif R == 'S' and (answer[0]+int(C) < len(park)):
            k = 0
            for j in range(answer[0], answer[0]+int(C)+1):
                if park[j][answer[1]] == 'X':
                    k += 1
            if k == 0:
                answer[0] += int(C)
        elif R == 'W' and (answer[1]-int(C) >= 0) and ('X' not in park[answer[0]][answer[1]-int(C):answer[1]+1]):
            answer[1] -= int(C)
        elif R == 'E' and (answer[1]+int(C) < len(park[answer[0]])) and ('X' not in park[answer[0]][answer[1]+1:answer[1]+int(C)+1]):
            answer[1] += int(C)
    return answer
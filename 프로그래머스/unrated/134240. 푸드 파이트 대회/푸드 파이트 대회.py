def solution(food):
    answer = ''
    for i in range(1, len(food)):
        for j in range(int(food[i]/2)):
            answer += str(i)
    res = ''.join(reversed(answer))
    answer += '0' + res
    return answer
print(solution([1, 7, 1, 2]	))
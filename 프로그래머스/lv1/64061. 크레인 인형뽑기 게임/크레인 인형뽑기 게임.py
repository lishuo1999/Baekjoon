def solution(board, moves):
    answer = 0
    result = []
    for i in range(len(moves)):
        for x in range(len(board)):
            if board[x][moves[i]-1] != 0:
                result.append(board[x][moves[i]-1])
                board[x][moves[i]-1] = 0
                break
        if len(result) >= 2:
            if result[-1] == result[-2]:
                answer += 2
                del result[-2:]
    return answer
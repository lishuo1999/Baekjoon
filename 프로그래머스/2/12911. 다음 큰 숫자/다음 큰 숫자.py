def solution(n):
    n_bin = bin(n)[2:]
    n_cnt = n_bin.count('1') # 1의 개수
    while 1:
        n += 1
        n_bin = bin(n)[2:]
        if n_cnt == n_bin.count('1'):
            answer = n
            break
    return answer
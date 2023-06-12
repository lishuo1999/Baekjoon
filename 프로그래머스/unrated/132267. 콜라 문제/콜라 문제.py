def solution(a, b, n):
    answer = 0
    while n>=a:
        k = int(n/a)*b
        answer += k
        n %= a
        n += k
    return answer
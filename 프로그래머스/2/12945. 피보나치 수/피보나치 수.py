def solution(n):
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a + b
    answer = b
    return answer % 1234567

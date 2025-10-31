from itertools import product
def solution(numbers, target):
    answer = 0
    for k in product(['+','-'],repeat=len(numbers)):
        sum = 0
        for x,y in zip(k,numbers):
            if x == '+':
                sum += y
            else:
                sum -= y
        if sum == target:
            answer += 1
    
    return answer
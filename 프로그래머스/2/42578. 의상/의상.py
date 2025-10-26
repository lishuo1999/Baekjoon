from collections import Counter

def solution(clothes):
    answer = 1
    counter = Counter([category for _,category in clothes])
    print(counter)
    for k in counter.values():
        answer *= (k+1)

    return answer - 1
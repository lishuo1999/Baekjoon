def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            add = numbers[i] + numbers[j]
            if add not in answer:
                answer.append(add)
    answer.sort()
    return answer
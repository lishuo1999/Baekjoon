def solution(s):
    answer = 0
    index = 1
    same = 1
    diff = 0
    while index < len(s):
        if s[index] == s[0]:
            same += 1
        else:
            diff += 1
        if same == diff:
            s = s[index+1:]
            index, same = 1, 1
            diff = 0
            answer += 1
        else:
            index += 1
    if len(s) != 0:
        answer += 1
    return answer
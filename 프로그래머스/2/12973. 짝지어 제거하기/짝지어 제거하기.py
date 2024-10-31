def solution(s):
    arr = []
    arr.append(s[0])
    for i in range(1, len(s)):
        if len(arr) > 0 and s[i] == arr[-1]: #짝인 경우
            arr.pop()
        else:
            arr.append(s[i])
    if len(arr) == 0:
        answer = 1
    else:
        answer = 0
    return answer
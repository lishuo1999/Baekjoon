def solution(s):
    answer = True
    arr = []
    for i in range(len(s)):
        if s[i] == '(':
            arr.append(s[i])
        else:
            if '(' in arr: # ( 있는 경우
                arr.pop()
            else:# 없는 경우
                arr.append(s[i])

    if len(arr) == 0:
        return True
    else:
        return False

def solution(s):
    s = s.lower()
    s = list(s) 
    if s[0] >= 'a' and s[0] <= 'z':
        s[0] = s[0].upper()
    for i in range(1, len(s)):
        if s[i-1] == ' ':
            if s[i] >= 'a' and s[i] <= 'z':
                s[i] = s[i].upper()
    answer = ''.join(s)
    return answer
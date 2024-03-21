S = input()
S = list(S)
cnt = 0
tmp = 0
k = []
def substitution(S, a, b, k):
    k_ = 0
    for i in range(a, b+1):
        S[i] = k[k_]
        k_ += 1

for i in range(len(S)):
    if S[i] == '<':
        cnt += 1
        if tmp > 0: #< 바로 앞에 문자열 있는 경우
            substitution(S, i-tmp, i-1, k)
            k.clear()
            tmp = 0
        continue
    elif S[i] == '>':
        cnt = 0
        continue

    if cnt == 0: #<> 사이의 문자가 아닌 경우
        if S[i] != ' ':
            k.insert(0, S[i])
            tmp += 1
        else: #공백의 경우 -> 뒤집기
            substitution(S, i-tmp, i-1, k)
            k.clear()
            tmp = 0
if tmp != 0:
    substitution(S, len(S)-tmp, len(S)-1, k)
print(''.join(S))
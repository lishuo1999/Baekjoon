N, M = map(int, input().split())
tmp = []
tmp_ = []
result = 1
arr = [[0 for j in range(20)] for i in range(N)]

for i in range(M):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
        arr[tmp[1]-1][tmp[2]-1] = 1
    elif tmp[0] == 2:
        arr[tmp[1]-1][tmp[2]-1] = 0
    elif tmp[0] == 3: #뒤로
        for j in range(19, -1, -1):
            arr[tmp[1]-1][j] = arr[tmp[1]-1][j-1]
        arr[tmp[1]-1][0] = 0
    elif tmp[0] == 4: #앞으로
        for j in range(19):
            arr[tmp[1]-1][j] = arr[tmp[1]-1][j+1]
        arr[tmp[1]-1][19] = 0
tmp_.append(arr[0])
for i in range(N):
    if arr[i] in tmp_: #중복
        continue 
    else: #중복x
        tmp_.append(arr[i])
        result += 1
        
print(result)

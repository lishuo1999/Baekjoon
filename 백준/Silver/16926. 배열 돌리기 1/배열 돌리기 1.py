from collections import deque
N, M, R = map(int, input().split())
arr = [[] for _ in range(N)]
for i in range(N):
    arr[i].extend(input().split())
cnt = min(N,M)
que = deque()

for i in range(int(cnt/2)):
    que.clear()
    #큐에 저장
    que.extend(arr[i][i:M-i]) #위
    for j in range(i+1, N-i-1): #오른쪽
        que.append(arr[j][M-i-1])
    que.extend(reversed(arr[N-i-1][i:M-i])) #아래
    for j in range(N-i-2, i, -1): #왼쪽
        que.append(arr[j][i])
    #회전
    que.rotate(-R)
  
    #다시 배열에 넣기
    for j in range(i, M-i): #위
        arr[i][j] = que.popleft()
    for j in range(i+1, N-i-1): #오른쪽
        arr[j][M-i-1] = que.popleft()
    for j in range(M-i-1, i, -1): #아래
        arr[N-i-1][j] = que.popleft()
    for j in range(N-i-1, i, -1): #왼쪽
        arr[j][i] = que.popleft()

for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    print()
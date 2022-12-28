from sys import stdin
import copy
k = stdin.readline().strip('\n')
k_ = copy.deepcopy(k)
k = k.split('.')
result = ""
for i in range(len(k)):
    if len(k[i]) % 4 == 0:
        new = k[i].replace('X','A')
        result += new
    else:
        r = len(k[i]) % 4
        count = len(k[i]) // 4
        new = k[i].replace('X', 'A', count*4)
        if r % 2 == 0:
            new2 = new.replace('X', 'B')
        else:
            print(-1)
            exit(0)
        result += new2
cnt = 0
for i in range(len(k_)):
    if k_[i] != '.':
        k_ = k_.replace('X',result[cnt],1)
        cnt += 1
print(k_)

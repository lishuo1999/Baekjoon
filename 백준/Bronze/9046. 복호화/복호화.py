from sys import stdin
import re
n = int(stdin.readline().strip('\n'))
dic = {}
for i in range(n):
    k = stdin.readline().replace(' ','').strip('\n')
    dic.clear()
    for j in range(len(k)):
        if k[j] not in dic:
            dic[k[j]] = 1
        else:
            dic[k[j]] += 1
    dic = dict(sorted(dic.items(), key=lambda x:x[1], reverse=True))
    if len(dic) >= 2:
        first = list(dic.values())[0]
        second = list(dic.values())[1]
        if first == second:
            print('?')
        else:
            print(list(dic.keys())[0])
    else:
        print(list(dic.keys())[0])
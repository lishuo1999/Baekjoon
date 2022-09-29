from sys import stdin
n = int(stdin.readline())
dic = {}
for i in range(n):
    k = stdin.readline()
    k = k.replace('\n', '')
    dic[k] = len(k)

#dic = sorted(dic.items(), reverse=True) # key-value 쌍으로 반환
dic = dict(sorted(dic.items(), key=lambda x: (x[1], x[0]))) # 오름차순
dic_list = list(dic.keys())
ans = ""
for i in range(len(dic_list)):
    ans += dic_list[i] + '\n'
print(ans)
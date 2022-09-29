from sys import stdin
import re
a = stdin.readline().strip('\n')
b = stdin.readline().strip('\n')
a = re.sub('[0-9]','',a)
if a.find(b) == -1:
    print(0)
else:
    print(1)
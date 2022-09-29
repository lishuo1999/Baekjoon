from sys import stdin
while 1:
    k = stdin.readline().strip('\n')
    if k == 'END':
        break
    k = list(k)
    for letter in reversed(k):
        print(letter, end='')
    print()
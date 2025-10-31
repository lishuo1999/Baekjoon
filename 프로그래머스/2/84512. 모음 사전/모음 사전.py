from itertools import product

def join_(n):
    return ''.join(n)

def solution(word):
    word_all = ['A','E','I','O','U']
    arr = []
    for i in range(5):
        arr.extend(list(map(join_ ,list(product(word_all,repeat=i+1)))))
    arr.sort()
    return arr.index(word)+1
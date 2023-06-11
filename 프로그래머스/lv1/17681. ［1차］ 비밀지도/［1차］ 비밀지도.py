def solution(n, arr1, arr2):
    answer = ["" for i in range(n)]
    for i in range(n):
        bi_1 = bin(arr1[i])[2:].zfill(n)
        bi_2 = bin(arr2[i])[2:].zfill(n)
        for j in range(n):
            if bi_1[j] == '1' or bi_2[j] == '1':
                answer[i] += '#'
            else:
                answer[i] += ' '

    print(answer)
    return answer
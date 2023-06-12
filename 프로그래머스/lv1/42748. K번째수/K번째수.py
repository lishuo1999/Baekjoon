def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        for j in range(3):
            arr = array[commands[i][0]-1:commands[i][1]]
            arr.sort()
        answer.append(arr[commands[i][2]-1])
    return answer
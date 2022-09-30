from sys import stdin
while True:
    try:
        line = stdin.readline().strip('\n').split(' ')
        if len(line) == 1:
            break
        cnt, index = 0, -1
        for i in range(len(line[0])):
            if line[0][i] in line[1]:
                index = line[1].find(line[0][i])
                line[1] = line[1][index+1:]
                cnt += 1
                if cnt == len(line[0]):
                    break
        if cnt == len(line[0]):
            print("Yes")
        else:
            print("No")
        line.clear()
    except EOFError: #입력이 끝날 때
        break
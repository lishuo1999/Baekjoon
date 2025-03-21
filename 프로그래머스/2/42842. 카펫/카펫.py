def solution(brown, yellow):
    answer = []

    #brown_x, brown_y, yellow_x, yellow_y
    # 구하려는 것: brown_x, brown_y
    # brown_x = yellow_x + 2
    # brown_y = yellow_y + 2
    # yellow = yellow_x*yellow_y
    # brown_x*brown_y = yellow + brown -> for 
    brown_x, brown_y = 0, 0

    for i in range(3, int((brown+yellow)**(1/2)) + 1): #제곱근
        if (brown+yellow)%i == 0: #나머지가 0 일때때
            brown_x = i
            brown_y = int((brown+yellow)/i)
            yellow_x = brown_x - 2
            yellow_y = brown_y - 2
            if (yellow_x*yellow_y) == yellow:
                break
    return [brown_y, brown_x]
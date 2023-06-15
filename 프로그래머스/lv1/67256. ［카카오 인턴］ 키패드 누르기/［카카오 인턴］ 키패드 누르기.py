def solution(numbers, hand):
    answer = ''
    left = [3, 0]
    right = [3, 2]
    arr = [[1, 2, 3],[4, 5, 6],[7, 8, 9],['*', 0, '#']]
    for i in range(len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            answer += 'L'
            for a in range(3):
                if numbers[i] in arr[a]:
                    left[0] = a
                    left[1] = 0
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            answer += 'R'
            for a in range(3):
                if numbers[i] in arr[a]:
                    right[0] = a
                    right[1] = 2
        else:
            for a in range(4):
                if numbers[i] in arr[a]:
                    x = a
                    y = arr[a].index(numbers[i])
            L = abs(left[0] - x) + abs(left[1] - y)
            R = abs(right[0] - x) + abs(right[1] - y)
            if L > R:
                answer += 'R'
                right[0] = x
                right[1] = y
            elif L < R:
                answer += 'L'
                left[0] = x
                left[1] = y
            else:
                answer += hand.upper()[0]
                if hand.upper()[0] == 'L':
                    left[0] = x
                    left[1] = y
                else:
                    right[0] = x
                    right[1] = y
    return answer
def keylocation(num):
    keyboard = {1:(0,0), 2:(0,1), 3:(0,2),
                4:(1,0), 5:(1,1), 6:(1,2),
                7:(2,0), 8:(2,1), 9:(2,2),
                '*':(3,0), 0:(3,1), '#':(3,2)}
    return keyboard[num]

def solution(numbers, hand):
    answer = ''
    left = keylocation('*')
    right = keylocation('#')
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            left = keylocation(num)
            answer += 'L'
        elif num == 3 or num == 6 or num == 9:
            right = keylocation(num)
            answer += 'R'
        elif num == 2 or num == 5 or num == 8 or num == 0:
            quest = keylocation(num)
            dif_l = abs(quest[0] - left[0]) + abs(quest[1] - left[1])
            dif_r = abs(quest[0] - right[0]) + abs(quest[1] - right[1])
            if dif_l > dif_r:
                right = quest
                answer += 'R'
            elif dif_l < dif_r:
                left = quest
                answer += 'L'
            elif dif_l == dif_r:
                if hand == 'right':
                    right = quest
                    answer += 'R'
                elif hand == 'left':
                    left = quest
                    answer += 'L'
    return answer

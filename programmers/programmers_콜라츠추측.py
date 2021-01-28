def solution(n):
    answer = 0
    if n == 1: answer = 0
    else:
        while True:
            if n % 2 ==0:
                n //= 2
            else:
                n = n * 3 + 1
            answer +=1
            if n == 1:break
            if answer > 500: answer = -1; break
    return answer

#다른사람 풀이
def collatz(num):
    answer = 0
    while num != 1:
        if num % 2 == 0: num = num / 2
        else: num = 3 * num + 1
        answer += 1

        if answer >= 500: return -1
    return answer

        

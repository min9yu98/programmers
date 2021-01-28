def solution(n):
    answer = []
    while True:
        n, rest = divmod(n, 3)
        answer.append(rest)
        if n == 0:break
    answer = list(reversed(answer))
    return sum([num * 3**i for i, num in enumerate(answer)])

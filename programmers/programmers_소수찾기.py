def solution(n):
    num = set([i for i in range(3, n + 1, 2)])
    for i in range(3, n + 1, 2):
        if i in num:
            num -= set([i for i in range(i * 2, n + 1, i)])
    return len(num) + 1

#다른사람 풀이
def solution(n):
    num = set(range(2, n + 1))

    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    return len(num)
                



def solution(n):
    num = list(map(str, reversed(sorted(str(n)))))
    return int(''.join(num))

#다른사람 풀이
def solution(n):
    return int("".join(sorted(list(str(n)), reversed=True)))

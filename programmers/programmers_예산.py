def solution(d, budget):
    part = []
    for i in sorted(d):
        budget -= i
        if budget < 0:
            break
        part.append(i)
    return len(part)

#다른사람 풀이
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

#다른사람 풀이
def solution(d, budget):
    d.sort()
    cnt = 0
    for i in d:
        budget -= i
        if budget < 0: break
        cnt += 1
    return cnt

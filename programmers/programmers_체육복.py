def solution(n, lost, reserve):
    lost_p = set(lost) - set(reserve)
    reserve_p = set(reserve) - set(lost)
    for data in reserve_p:
        if data-1 in lost_p:
            lost_p.remove(data-1)
        elif data+1 in lost_p:
            lost_p.remove(data+1)
    return n - len(lost_p)

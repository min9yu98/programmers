def solution(num):
    return "Odd" if num%2 else "Even"

#다른사람 풀이
def solution(num):
    return ["Even", "Odd"][num & 1]

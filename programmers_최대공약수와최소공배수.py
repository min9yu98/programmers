from math import gcd
def lcm(x, y):
    return x * y // gcd(x, y)
def solution(n, m):
    return [gcd(n, m), lcm(n, m)]

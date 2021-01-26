def solution(s):    
    return 'true' if s.upper().count('P') == s.upper().count('Y') else 'false'

#다른사람 풀이
def solution(s):
    return s.lower().count('p') == s.lower().count('y')

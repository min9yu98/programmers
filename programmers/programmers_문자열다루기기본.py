def solution(s):
    if len(s) == 4 or len(s) == 6:
        try: s = int(s); return True
        except ValueError: return False
    else:
        return False

#다른사람 풀이

def solution(s):
    s.isdigit() and len(s) in (4, 6)
    
    

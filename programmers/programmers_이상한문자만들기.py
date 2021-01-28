def solution(s):
    answer = ''
    st = s.split(' ')
    for str in st:
        for i, spell in enumerate(str):
            answer += spell.upper() if i % 2 == 0 else spell.lower()
        answer += ' '
    return answer[:-1]

#다른사람 풀이

def solution(s):
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower for i, c in enumerate(w)]) for w in s.split(' ')])

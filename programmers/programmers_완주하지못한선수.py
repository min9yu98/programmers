def solution(participant, completion):
    par, com = sorted(participant), sorted(completion)
    completion += ['z']
    for p, c in zip(par, com):
        if p != c:
            answer = p
            break
    return answer

# 다른사람  풀이
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
    

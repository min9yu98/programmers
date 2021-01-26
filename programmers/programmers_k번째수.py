def solution(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(sorted(array[i - 1:j])[k - 1])
    return answer

#다른사람 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands)


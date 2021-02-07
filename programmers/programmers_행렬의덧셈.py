def solution(arr1, arr2):
    answer = []
    for x, y in zip(arr1, arr2):
        answer.append([a + b for a, b in zip(x, y)])
    return answer


# 다른사람 풀이 
def solution(arr1, arr2):
    answer = [[a + b for a, b in zip(x, y)] for x, y in zip(arr1, arr2)]
    return answer 

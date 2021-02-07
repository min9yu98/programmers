def solution(n, stages):
    stage = [i for i in range(1, n + 1)]
    count = len(stages)
    numbers = []
    for i, num in enumerate(stage):
        if count == 0:
            numbers.append([i+1, 0])
        else:
            son = stages.count(num)
            numbers.append([i+1, son/count])
            count = count - son
    return [i[0] for i in sorted(numbers, key=lambda x : x[1], reverse = True)]

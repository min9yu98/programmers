def solution(numbers):
    answer = []
    for i in range(len(numbers) - 1):
        for j in numbers[i + 1:]:
            answer.append(numbers[i] + j)
    return list(sorted(set(answer)))

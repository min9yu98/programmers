def solution(board, moves):
    answer = []
    reposit = []
    for i in moves:
        for layer in board:
            if layer[i - 1]:
                reposit.append(layer[i - 1])
                layer[i - 1] = 0
                if reposit[-1:] == reposit[-2:-1]:
                    answer.append(reposit[-1:])
                    reposit = reposit[:-2]
                break
    return len(answer) * 2


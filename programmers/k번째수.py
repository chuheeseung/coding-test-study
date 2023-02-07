def solution(array, commands):
    # answer = [0 for i in range(len(commands))]
    answer = []

    for command in commands:
        i, j, k = command[0], command[1], command[2]
        cut = sorted(array[i-1:j])
        answer.append(cut[k-1])

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
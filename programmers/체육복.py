def solution(n, lost, reserve):
    answer = 0

    _reverse = set(reserve) - set(lost)
    _lost = set(lost) - set(reserve)

    for i in _reverse:
        if i-1 in _lost:
            _lost.remove(i-1)
        elif i+1 in _lost:
            _lost.remove(i+1)

    answer = n - len(_lost)

    return answer

# n = 5
# lost = [2, 4]
# reserve = [1, 3, 5]
# answer = solution(n, lost, reserve)
# print(answer)
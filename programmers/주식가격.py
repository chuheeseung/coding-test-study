from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)

    while queue:
        count = 0
        pop_queue = queue.popleft()

        for q in queue:
            count += 1

            if q < pop_queue:
                break

        answer.append(count)

    return answer

prices = [1, 2, 3, 2, 3]
answer = solution(prices)
print(answer)
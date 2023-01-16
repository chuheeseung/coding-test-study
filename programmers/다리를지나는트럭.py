from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    temp = 0
    truck_bridge_deque = deque(bridge_length * [0])
    truck_weights_deque = deque(truck_weights)

    while len(truck_bridge_deque):
        answer += 1
        temp -= truck_bridge_deque[0]
        truck_bridge_deque.popleft()

        if truck_weights_deque:
            if temp + truck_weights_deque[0] <= weight:
                temp += truck_weights_deque[0]
                truck_bridge_deque.append(truck_weights_deque.popleft())
            else:
                truck_bridge_deque.append(0)

    return answer

bridge_length = 2 # 다리에 올라갈 수 있는 트럭 수
weight = 10 # 다리가 견딜 수 있는 무게
truck_weights = [7, 4, 5, 6] # 트럭 별 무게

# bridge_length = 100
# weight = 100
# truck_weights = [10]

# bridge_length = 100
# weight = 100
# truck_weights = [10,10,10,10,10,10,10,10,10,10]

answer = solution(bridge_length, weight, truck_weights)
print(answer)
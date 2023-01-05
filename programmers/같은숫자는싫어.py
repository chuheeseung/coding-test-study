from collections import deque

def solution(arr):
    queue = deque()

    # queue.append(arr[0])
    for a in arr:
        if len(queue) == 0 or a != queue[-1]: # 기억해두면 나중에 유용할듯
            queue.append(a)

    return list(queue)

arr = [1,1,3,3,0,1,1]
answer = solution(arr)
print("answer : ", answer)
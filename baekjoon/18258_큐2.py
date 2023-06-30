import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque([])

for _ in range(n):
    inputs = input().split()

    if inputs[0] == 'push':
        queue.append(inputs[-1])
    elif inputs[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif inputs[0] == 'size':
        print(len(queue))
    elif inputs[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif inputs[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif inputs[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

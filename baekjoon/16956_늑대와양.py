import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = []
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
boolean = False

for _ in range(r):
    graph.append(list(input().rstrip()))

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'W':
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]

                if 0 <= x < r and 0 <= y < c and graph[x][y] == 'S':
                    boolean = True
                    break
        elif graph[i][j] == 'S':
            continue
        elif graph[i][j] == '.':
            graph[i][j] = 'D'

if boolean:
    print(0)
else:
    print(1)

    for i in graph:
        print(''.join(i))

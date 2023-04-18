n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0] * n for _ in range(n)]
dx = [0, 1] # 오른쪽, 아래만 이동 가능
dy = [1, 0]
queue = [[0, 0]]

while queue:
    x, y = queue[0][0], queue[0][1] # queue 맨 앞 원소를 꺼내서 위치 파악
    del queue[0]

    if graph[x][y] == -1: # 맨 오른쪽 아래 도달하면 HaruHaru 출력, while문 종료
        print("HaruHaru")
        exit(0)

    jump = graph[x][y] # 점프한 값

    for i in range(2):
        nx = x + dx[i] * jump # 점프값만큼 이동
        ny = y + dy[i] * jump

        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            # 범위 안에 있고 방문하지 않았으면 방문 체크 후 queue에 넣기
            visited[nx][ny] = 1
            queue.append([nx, ny])

print("Hing")
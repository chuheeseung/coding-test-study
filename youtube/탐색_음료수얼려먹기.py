def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m: # 주어진 범위를 벗어나면 즉시 종료
        return False

    if graph[x][y] == 0: # 현재 노드를 아직 방문하지 않았다면
        graph[x][y] = 1 # 현재 노드 방문 처리

        dfs(x-1, y) # 상하좌우 모두 재귀적으로 호출
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x-1, y)

        return True

    return False

n, m = map(int, input().split())
graph = []
result = 0

for i in range(n): # 맵 정보 입력 받아서 graph 배열에 저장
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True: # 현재 위치에서 DFS 수행
            result += 1

print(result)
# 방문 정보를 리스트로 표현
visited = [False] * 9

# 각 노드가 연결된 정보를 2차원 리스트로 표현
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

def DFS(graph, v, visited):
    visited[v] = True  # 현재 노드 방문 처리
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            # 현재 노드와 연결된 다른 노드들을 재귀적으로 방문
            DFS(graph, i, visited)


DFS(graph, 1, visited)

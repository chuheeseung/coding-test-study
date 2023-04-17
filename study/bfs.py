from collections import deque

graph = [  # 각 노드가 연결된 정보를 2차원 리스트로 표현
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

visited = [False] * 9  # 방문 정보를 리스트로 표현

def BFS(graph, start, visited):
    queue = deque([start]) # 큐 구현을 위해 라이브러리 사용
    visited[start] = True # 현재 노드 방문 처리

    while queue: # 큐가 빌 때까지 반복
        v = queue.popleft() # 큐의 원소 하나를 뽑아 출력
        print(v, end=' ')
        for i in graph[v]: # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
            if not visited[i]:
                queue.append(i)
                visited[i] = True


BFS(graph, 1, visited)

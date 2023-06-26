import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(s):
    for i in graph[s]:
        if visited[i] == 0: # 부모의 노드 번호가 있지 않은 경우
            visited[i] = s # 부모의 노드 번호를 visited에 추가
            dfs(i)

dfs(1) # 루트부터 돌아야 하니까 1부터 시작

for x in range(2, n + 1):
    print(visited[x])
n, m = map(int, input().split())
tiles = [list(input()) for _ in range(n)]
count = 0  # 타일 개수
visited = [[False for _ in range(m)] for _ in range(n)]


def dfs(x, y):
    visited[x][y] = True

    if tiles[x][y] == '|':
        if x + 1 < n and tiles[x + 1][y] == '|' and visited[x + 1][y] == False:
            dfs(x + 1, y)
        else:
            return
    elif tiles[x][y] == '-':
        if y + 1 < m and tiles[x][y + 1] == '-' and visited[x][y + 1] == False:
            dfs(x, y + 1)
        else:
            return


for i in range(n):
    for j in range(m):
        if visited[i][j] == False:
            dfs(i, j)
            count += 1

print(count)

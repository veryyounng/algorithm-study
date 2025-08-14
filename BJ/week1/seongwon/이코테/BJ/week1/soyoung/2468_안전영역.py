import sys
sys.setrecursionlimit(100000)  # 넉넉하게 재귀 깊이 늘려줌


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

max_safe = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y, h, visited):
    visited[x][y] = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny] > h:
                DFS(nx, ny, h, visited)
    
max_height = max(map(max, graph))

for h in range(0, max_height+1):
    cnt = 0
    visited = [[False] * (n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > h:
                DFS(i, j , h, visited)
                cnt += 1

    max_safe = max(max_safe, cnt)
print(max_safe)
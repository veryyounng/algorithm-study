from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(sx, sy):
    queue = deque([(sx, sy)])
    visited[sx][sy] = 1
    area = 1
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny]== 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                    area += 1
    return area

max_area = 0
cnt = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            max_area = max(max_area, BFS(i, j))
print(cnt)
print(max_area if cnt > 0 else 0)
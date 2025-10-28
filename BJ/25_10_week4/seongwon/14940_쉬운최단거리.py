import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
n,m  = map(int,input().split())

dx = [0,-1,0,1]
dy = [1,0,-1,0]

# maps = [list(map(int, input().split())) for _ in range(n)]
# visited = [[False] * m for _ in range(n)]  

# def bfs(i, j):      
#     q = deque([(i, j)])
#     visited[i][j] = True
#     maps[i][j] = 0  

#     while q:
#         x, y = q.popleft()
#         for k in range(4):
#             xx = x + dx[k]
#             yy = y + dy[k]
#             if 0 <= xx < n and 0 <= yy < m and not visited[xx][yy] and maps[xx][yy] != 0:
#                 visited[xx][yy] = True
#                 maps[xx][yy] = maps[x][y] + 1
#                 q.append((xx, yy))

# for i in range(n):
#     for j in range(m):
#         if maps[i][j] == 2:
#             bfs(i, j)

# for i in range(n):
#     for j in range(m):
#         if maps[i][j] == 1:
#             maps[i][j] = -1

# for row in maps:
#     print(*row)




# 거리 배열 (-1로 초기화)
n, m = map(int, input().split())  # n: 세로, m: 가로
maps = [list(map(int, input().split())) for _ in range(n)]

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 거리 배열 (-1로 초기화)
dist = [[-1] * m for _ in range(n)]

# 목표지점(2) 찾기
for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            start = (i, j)
        if maps[i][j] == 0:  # 갈 수 없는 땅은 거리 0으로 표시
            dist[i][j] = 0

# BFS 시작
q = deque([start])
dist[start[0]][start[1]] = 0  # 시작점 거리 0

while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if maps[nx][ny] == 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

# 출력
for i in range(n):
    print(*dist[i])
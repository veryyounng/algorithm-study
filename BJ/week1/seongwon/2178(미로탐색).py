import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

n,m = map(int,input().split())
maps = [list(map(int,input().strip())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]


# def bfs(x,y):
#     queue = deque([(x,y)])
#     visited[x][y]=True
#     while queue:
#         x,y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny] == 1:
#                 visited[nx][ny] = True
#                 queue.append((nx, ny))
#                 maps[nx][ny] = maps[x][y]+1

# bfs(0,0)
# print(maps[n-1][m-1])

min_dist = n * m  # 최소 칸 수 (최대값으로 초기화)

# dfs 로도 풀어보기
def dfs(x, y, dist):
    global min_dist
    
    # 도착점 도달
    if x == n-1 and y == m-1:
        min_dist = min(min_dist, dist)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            if maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, dist + 1)
                visited[nx][ny] = False  # 백트래킹

# 시작점 방문 처리
visited[0][0] = True
dfs(0, 0, 1)

print(visited)
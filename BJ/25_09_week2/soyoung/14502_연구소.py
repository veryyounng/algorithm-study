from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

best = 0
virus = []
empty = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append((i, j))
        elif graph[i][j] == 0:
            empty.append((i, j))
            
E = len(empty)
            

def BFS():
    global best
    temp_graph = [row[:] for row in graph]
    queue = deque(virus)
    
    infected = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < m:
                if temp_graph[nx][ny] == 0:
                    temp_graph[nx][ny] = 2
                    infected += 1
                    
                    if E -3 - infected <= best:
                        return
                    queue.append((nx, ny))
    safe = E - 3 - infected
    if safe > best:
        best = safe
    
for wall in combinations(empty, 3):
    for x, y in wall:
        graph[x][y] = 1
    BFS()
    for x, y in wall:
        graph[x][y] = 0
            
print(best)
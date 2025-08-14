from collections import deque
n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    queue = [(x, y)]
    graph[x][y] = 0
    count = 1

    while queue:
        x, y = queue.pop(0)
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


cnt =[]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            graph[i][j] = 0
            cnt.append(BFS( i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])
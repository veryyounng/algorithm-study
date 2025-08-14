from collections import deque

#입력 받기
m, n, h = map(int, input().split())

graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

#좌표 방향
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

queue = deque()

#익은 토마토 다 넣기
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((i, j, k))

#BFS
def bfs():
    #큐에서 빼기
    while queue:
        x, y, z = queue.popleft()
    
    #좌표 이동
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
        
    #그래프 범위 체크
            if nx<0 or nx>=h or ny<0 or ny>=n or nz<0 or nz>=m:
                continue
        
            if graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = graph[x][y][z] + 1
                queue.append((nx, ny, nz))
            
#토마토 익히기
bfs()

#익히지 않은 토마토가 있으면 -1 출력
day = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                exit()
            else:
                day = max(day, graph[i][j][k])

print(day - 1)  # 마지막에 익은 토마토는 1이므로 -1을 해줘야 함
            
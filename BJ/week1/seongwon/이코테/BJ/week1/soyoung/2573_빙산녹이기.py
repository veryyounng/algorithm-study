#입력 처리

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

#빙산이 몇 덩어리인지 세기 (BFS로 탐색)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(x, y, visited):
    visited[x][y] = 1
    
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < m:
                if  visited[nx][ny] == 0 and graph[nx][ny] > 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))


def count(graph):
    cnt = 0
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
                if graph[i][j] == 0 or visited[i][j]:
                    continue
                if visited[i][j] == 0 and graph[i][j] > 0:
                    BFS(i, j, visited)
                    cnt += 1
    
    return cnt

#빙산 녹이기 (melt 함수)
def melt(graph):
    melt_amount = [[0] * m for _ in range(n)]
    ice_pos = []  # 빙산 위치만 저장

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                ice_pos.append((i, j))

    # 빙산 위치만 녹이기
    for x, y in ice_pos:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    melt_amount[x][y] += 1

    # 동시에 반영
    for x, y in ice_pos:
        graph[x][y] = max(0, graph[x][y] - melt_amount[x][y])

            

year = 0

while True:
    result = count(graph)
    
    if result == 0:
        print(0)
        break
    
    elif result >= 2:
        print(year)
        break
    
    melt(graph)
    year += 1
    

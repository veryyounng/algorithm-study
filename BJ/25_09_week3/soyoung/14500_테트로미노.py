n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
maximum = 0

def DFS(x, y, tmp, cnt):
    global maximum
    
    if cnt == 4:
        maximum = max(maximum, tmp)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if cnt == 2:
                visited[nx][ny] = 1
                DFS(nx, ny, tmp + board[nx][ny], cnt +1)
                visited[nx][ny] = 0
            
            visited[nx][ny] = 1
            DFS(nx, ny, tmp+ board[nx][ny], cnt +1)
            visited[nx][ny] = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        DFS(i, j, board[i][j], 1)
        visited[i][j] = 0
print(maximum)
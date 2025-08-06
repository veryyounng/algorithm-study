n = int(input())

#graph 만들기
graph = [list(map(int, input().strip())) for _ in range(n)]

#방향 배열 만들기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    # 방문 표시하기
    graph[x][y] = 0
    global count
    count +=1
    
    #count 초기화
    #이동해서 범위 벗어나지 않으면 dfs 돌리기
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        
        if graph[nx][ny] == 1:
            DFS(nx, ny)
        
        
cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count = 0
            DFS(i, j)
            cnt.append(count)

cnt.sort()
print(len(cnt))

for i in range(len(cnt)):
    print(cnt[i])
            
    
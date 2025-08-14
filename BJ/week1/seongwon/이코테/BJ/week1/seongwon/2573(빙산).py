import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)
from collections import deque

n,m  = map(int, input().split())

maps1 = [list(map(int,input().split()))  for _  in range(n) ]


cnt = 0
answer = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]



answer = 0 
def dfs(x,y):
    maps2[x][y]=0
    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        if 0<=nx<n and 0<=ny<m and maps2[nx][ny]!=0:
            dfs(nx,ny)
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    maps2[x][y] = 0  # 방문 처리
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps2[nx][ny] != 0:
                maps2[nx][ny] = 0  # 방문 처리
                queue.append((nx, ny))
while True:
    maps2 = [[0]*m for _ in range(n)]
    ice_exist = False  # 빙산 유무 체크

    for i in range(n):
        for j in range(m):
            if maps1[i][j]!=0:
                ice_exist = True
                # 일단 녹여 
                height=0
                for k in range(4):
                    x=dx[k]+i
                    y=dy[k]+j
                    if 0 <= x < n and 0 <= y < m and maps1[x][y] == 0:
                        height += 1
                maps2[i][j] = max(0, maps1[i][j] - height)
             
     # 빙산이 하나도 없으면 0 출력 후 종료
    if not ice_exist:
        print(0)
        break   
    for i in range(n):
        for j in range(m):
            maps1[i][j]=maps2[i][j]

    #maps2 로 영역갯수세기
    cnt = 0
    for i in range(n):
        for j in range(m):
            if maps2[i][j]!=0:
                cnt+=1
                bfs(i, j)
    answer+=1
    
    # 빙산이 다 녹았으면 0 출력하고 종료
    if cnt == 0:
        print(0)
        break
    
    # 분리됐으면 answer 출력 후 종료
    if cnt>=2:
        print(answer)
        break


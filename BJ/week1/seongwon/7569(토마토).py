import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)
from collections import deque


m,n,h = map(int, input().split())
maps = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h) ]


dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
queue = deque()
def bfs():
    while queue:
        zz,xx,yy = queue.popleft()
        for i in range(6):
            nz = dz[i]+zz
            nx = dx[i]+xx
            ny = dy[i]+yy
            if 0<=nx<n and 0<=ny<m and 0<=nz<h and maps[nz][nx][ny]!=-1 and maps[nz][nx][ny]==0:
                maps[nz][nx][ny] = maps[zz][xx][yy] + 1
                queue.append((nz, nx, ny))


for k in range(h):
    for i in range(n):
        for j in range(m):
            if maps[k][i][j]==1:
                queue.append((k,i,j))
          
bfs()
# 정답 계산
answer = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if maps[k][i][j] == 0:
                print(-1)
                sys.exit(0)
            answer = max(answer, maps[k][i][j])

print(answer - 1)
import sys
sys.stdin = open('input.txt', 'r')

t = int(input())

dx = [0,1,-1,0]
dy = [1,0,0,-1]

def dfs(x,y):
    field[y][x]=0
    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        if 0<=nx<m and 0<=ny<n and field[ny][nx]==1:
            dfs(nx,ny)

for i in range(t):
    m,n,k = map(int,input().split()) 
    field = [[0]*m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1  # 배추 심기
    count = 0
    for y in range(n):
        for x in range(m):
            if field[y][x]==1:
                dfs(x,y)
                count+=1
    print(count)
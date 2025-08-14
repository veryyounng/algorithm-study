import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)


m,n,k = map(int,input().split())

maps = [[0]*n for _ in range(m)]

for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())

    for i in range(y1,y2):
        for j in range(x1,x2):
            maps[i][j]=1

areas=[]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(x,y):
    global cnt 
    cnt+=1
    maps[x][y]=1
    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        if 0<=nx<m and 0<=ny<n and maps[nx][ny]==0:
            dfs(nx,ny)
    
    

for i in range(m):
    for j in range(n):
        if maps[i][j]==0:
            cnt = 0  
            dfs(i,j)
            areas.append(cnt)

areas.sort()
print(len(areas))
print(' '.join(map(str, areas)))
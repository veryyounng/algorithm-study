import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)


n,m = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(x,y):
    if x==n-1 and y==m-1:
        return 
    if dp[x][y]!=-1:
        return dp[x][y]
    dp[x][y]=0
    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        if 0<=nx<n and 0<=ny<m and maps[x][y]<maps[nx][ny]:
            dp[x][y]+=dfs(nx,ny)
    return dp[x][y]    
print(dfs(0,0))
     
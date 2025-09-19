import sys
sys.stdin = open('input.txt', 'r')

n,m = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(n)]
check = [[0]*m for _ in range(n)]


dx=[1,0,-1,0]
dy=[0,1,0,-1]


answer = set()

def dfs(x,y,sum,cnt):
    check[x][y]=1
    if cnt == 4:
        answer.add(sum)
        return
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m and check[nx][ny] == 0:
            dfs(nx,ny,sum+maps[nx][ny],cnt+1)
            check[nx][ny]=0
            



def fuckcheck(i,j):
    
    sum=0
    # j는 오른쪽으로 두번가기 
    # i는 가운데 위로 한칸씩 
    if 0<=j+2<m and 0<=i-1<n:
        sum=max(sum,maps[i][j]+maps[i][j+1]+maps[i-1][j+1]+maps[i][j+2])
    # j는 오른쪽으로 두번가기 
    # i는 가운데 아래로 한칸씩  
    if 0<=j+2<m and 0<=i+1<n:
        sum=max(sum,maps[i][j]+maps[i][j+1]+maps[i+1][j+1]+maps[i][j+2])
    # j는 가운데 오른쪽 한칸
    # i는 아래로 두칸
    if 0<=j+1<m and 0<=i+2<n:
        sum=max(sum,maps[i][j]+maps[i+1][j]+maps[i+1][j+1]+maps[i+2][j])
    # j는 가운데 왼쪽 한칸
    # i는 아래로 두칸
    if 0<=j-1<m and 0<=i+2<n:
        sum=max(sum,maps[i][j]+maps[i+1][j]+maps[i+1][j-1]+maps[i+2][j])
    return sum

for i in range(n):
    for j in range(m):     
        dfs(i,j,maps[i][j],1)
        check[i][j]=0
        answer.add(fuckcheck(i,j))

print(max(answer))
import sys
sys.stdin = open('input.txt', 'r')
n = int(input())
maps = [list(map(int,input().strip())) for _ in range(n)]


total = 0
answer=[]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
def dfs(x,y,cnt):
    maps[x][y]=0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and maps[nx][ny]==1:
            cnt = dfs(nx,ny,cnt+1)
    return cnt
for i in range(n):
    for j in range(n):
        if maps[i][j]==1:
            total += 1
            answer.append(dfs(i,j,1))        

print(total)
for num in sorted(answer):
    print(num)

import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)

n,m  = map(int, input().split())

maps = [list(map(int,input().split()))  for _  in range(n) ]


cnt = 0
answer = []
dx =[0,0,1,-1]
dy =[1,-1,0,0]
# def dfs(x,y,cnt):
#     maps[x][y]=0
#     for i in range(4):
#         nx = dx[i]+x
#         ny = dy[i]+y
#         if 0<=nx<n and 0<=ny<m  and maps[nx][ny]==1:
#             cnt=dfs(nx,ny,cnt+1)
#     return cnt
    

# for i in range(n):
#     for j in range(m):
#         if maps[i][j]==1:
#             cnt +=1
#             answer.append(dfs(i,j,1))
# print(cnt)
# print(max(answer) if answer else 0)

def dfs(x, y):
    maps[x][y] = 0
    area = 1
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
            area += dfs(nx, ny)
    return area

cnt = 0
answer = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            cnt += 1
            answer.append(dfs(i, j))

print(cnt)
print(max(answer) if answer else 0)
import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]

pic_cnt = 0


dx = [1,0,-1,0]
dy = [0,1,0,-1]


def dfs(x,y):
    maps[x][y] = 0
    cnt = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m and maps[nx][ny]==1:
            cnt = dfs(nx,ny)+1
    return cnt

max_cnt_in_picture = 0
for i in range(n):
    for j in range(m):
        if maps[i][j]==1:
            pic_cnt = pic_cnt + 1
            cnt = dfs(i,j)
            print(cnt)
            if max_cnt_in_picture<cnt:
                max_cnt_in_picture = cnt
if pic_cnt == 0:
    print(0)
    print(0)
else:
    print(pic_cnt)
    print(max_cnt_in_picture)



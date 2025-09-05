import sys
sys.stdin = open('input.txt', 'r')

maps = []
for _ in range(5):
    maps.append(list(map(int,input().split())))


dx = [1,0,-1,0]
dy = [0,1,0,-1]
answer = set()
def dfs(x,y,s,node):
    if node == 5:
        answer.add(s)
        return
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<5 and 0<=yy<5:
            dfs(xx,yy,s+str(maps[xx][yy]),node+1)

for i in range(5):
    for j in range(5):
        dfs(i,j,str(maps[i][j]),0)
print(len(answer))
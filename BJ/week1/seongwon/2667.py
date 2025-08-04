

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque


n = int(input())

maps = []
answer = []
for _ in range(n):
    a = list(map(int, input().strip()))
    maps.append(a)
    


def bfs(x,y):
    queue = deque([[x, y]])
    maps[x][y]=0
    dx=[0,1,-1,0]
    dy=[1,0,0,-1]
    
    count = 1
    while queue:
        [xx,yy] = queue.popleft()    
        for i in range(4):
            nx =xx+dx[i]
            ny =yy+dy[i]
            if 0 <= nx < n and 0 <= ny < n and maps[nx][ny]==1:
                count+=1
                maps[nx][ny]=0
                queue.append([nx,ny])
    answer.append(count)
            
            
for x in range(n):
    for y in range(n):
        if maps[x][y]==1:
            bfs(x,y)
print(len(answer))
for cnt in sorted(answer):
    print(cnt)
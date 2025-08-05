# import sys
from collections import deque

# sys.stdin = open('./BJ/week1/soyoung/input.txt', 'r')
# sys.stdout = open('./BJ/week1/soyoung/output.txt', 'w')

# 미로 만들기
n, m = map(int, input().split())

arr = [list(map(int, input().strip())) for _ in range(n)]

# 미로 생성할 방향 배열 만들기
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#bfs 만들기
def BFS(x, y):
    #큐 만들기
    queue = deque()
    queue.append((x,y))
    
    #큐 돌리기
    while queue:
        x, y = queue.popleft()
        
        #이동하기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if arr[nx][ny] == 0:
                continue
            
            #미로 1이면 방문 표시 => 거리 더하기, 큐 안에 넣기
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))
    
    return arr[n-1][m-1]

print(BFS(0,0))
import sys
sys.stdin = open('input.txt', 'r')

sys.setrecursionlimit(10**6)

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def dfs(x,y):
    graph[y][x]=0
    for i in range(8):
        nx = dx[i]+x 
        ny = dy[i]+y
        if 0 <= nx < w and 0 <= ny < h and graph[ny][nx] == 1:
            dfs(nx, ny) 
                        

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    
    for _ in range(h):
        graph.append(list(map(int,input().split())))
    count = 0
    for y in range(h):
        for x in range(w):
            if graph[y][x] == 1:
                dfs(x, y)
                count += 1
    print(count)
#시간초과...

import sys
sys.setrecursionlimit(10000)  
sys.stdin = open('input.txt', 'r')
n, m = map(int, sys.stdin.readline().split())
maps = [list(sys.stdin.readline().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [False] * 26 
max_count = 0

def dfs(x, y, count):
    global max_count
    max_count = max(max_count, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            idx = ord(maps[nx][ny]) - ord('A')
            if not visited[idx]:
                visited[idx] = True
                dfs(nx, ny, count + 1)
                visited[idx] = False 


visited[ord(maps[0][0]) - ord('A')] = True
dfs(0, 0, 1)

print(max_count)

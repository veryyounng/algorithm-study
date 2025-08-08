import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

n,m,k  = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, n+1):
    graph[i].sort()
    
dfs_visited = [False]*(n+1)
bfs_visited = [False]*(n+1)

def bfs(v):
    queue = deque([v])
    bfs_visited[v] = True  # 큐에 넣는 순간 방문 처리
    while queue:
        node = queue.popleft()
        print(node, end = " ")
        for nv in graph[node]:
            if not bfs_visited[nv]:
                bfs_visited[nv] = True
                queue.append(nv)
                
                
def dfs(v):
    print(v, end=' ')
    dfs_visited[v]=True
    for nv in graph[v]:
        if not dfs_visited[nv]:
            dfs(nv)
        
dfs(k)
print()
bfs(k)
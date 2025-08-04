# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 
# 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 
# 그 다음 줄에는 BFS를 수행한 결과를 출력한다. 
# V부터 방문된 점을 순서대로 출력하면 된다.
import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

n,m,v = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
dfs_visited = [False] * (n+1)

def dfs (graph, v, dfs_visited):
    dfs_visited[v] = True
    print(v,end =' ')
    for next in graph[v]:
        if not dfs_visited[next]:
            dfs(graph,next,dfs_visited)

def bfs(graph,start):
    queue = deque()
    queue.append(start)
    visited = [False] * len(graph)
    visited[start]=True
    while queue:
        v = queue.popleft()
        print (v, end  =' ')
        for next in graph[v]:
            if not visited[next]:
                visited[next]=True
                queue.append(next)
                
    


dfs(graph,v,dfs_visited)
bfs(graph,v)
# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end=' ')
#     for next in graph[v]:
#         if not visited[next]:
#             dfs(graph, next, visited)

# def bfs(graph, start):
#     visited = [False] * len(graph)
#     queue = deque([start])
#     visited[start] = True

#     while queue:
#         v = queue.popleft()
#         print(v, end=' ')
#         for next in graph[v]:
#             if not visited[next]:
#                 visited[next] = True
#                 queue.append(next)

# # 입력 받기
# n, m, v = map(int, input().split())
# graph = [[] for _ in range(n + 1)]

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# # 방문 순서를 위해 정렬
# for i in range(1, n + 1):
#     graph[i].sort()

# # DFS 출력
# visited_dfs = [False] * (n + 1)
# dfs(graph, v, visited_dfs)
# print()

# # BFS 출력
# bfs(graph, v)

import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,weight = map(int, input().split())
    graph[a].append((b,weight))
    graph[b].append((a,weight))



def dfs(v, weight, visited):
    visited[v] = True
    farthest = (weight, v)
    for neighbor in graph[v]:
        neighbor_node, neighbor_weight  = neighbor
        if not visited[neighbor_node]:
            tmp = dfs(neighbor_node,neighbor_weight+weight,visited)
            if tmp[0] > farthest[0]:
                farthest = tmp
    
    return farthest


# 정점의 가장 먼 곳을 찾아서 
visited = [False]*(n+1)
_, far_node = dfs(1, 0, visited)

# 그 점에서 가장 먼 곳을 찾느다 
visited = [False] * (n + 1)
max_dist, _ = dfs(far_node, 0, visited)

print(max_dist)
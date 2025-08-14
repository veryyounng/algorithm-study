import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
    
    
#방법 1    
# cnt = 0
# def dfs(v):
#     global cnt
#     cnt+=1
#     visited[v]=True
#     for nv in graph[v]:
#         if not visited[nv]:
#             dfs(nv)
            
# dfs(1)    
# print(cnt-1)

# 방법 2
# def dfs(v):
#     cnt = 1
#     visited[v]=True
#     for nv in graph[v]:
#         if not visited[nv]:
#             cnt += dfs(nv)
#     return cnt
# print(dfs(1)-1)

# 방법 3
def dfs(v,cnt):
    visited[v]=True
    for nv in graph[v]:
        if not visited[nv]:
           cnt = dfs(nv,cnt+1)
    return cnt

print(dfs(1,0))
# 바이러스

import sys
sys.stdin = open('input.txt', 'r')

n= int(input())
m= int(input())

visited = [False ]*(n+1)
graph = [[]for _ in range(n+1)]


for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)



count = 0
def dfs(v):
    global count
    if not visited[v]:
        visited[v]=True
        count+=1
        for next in graph[v]:
            dfs(next)
dfs(1)
print(count-1, end = '')
    

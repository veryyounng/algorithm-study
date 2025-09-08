from collections import deque;

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n+1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)
arr = [0]*(n+1)

def DFS(v, num):

    visited[v] = 1
    num += 1
    arr[v].append(num)

    for i in graph[v]:
        if visited[i]  == 0:
            DFS(i, num)

DFS(1,0)
num = min(num, )




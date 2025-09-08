import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)


def bfs(i):
    visited=[False]*(n+1)
    queue = deque()
    queue.append(i)
    cnt=1
    while queue:
        q = queue.popleft()
        visited[q]=True
        for g in graph[q]:
            if not visited[g]:
                queue.append(g)
                cnt=cnt+1
    return cnt

answer = []
for i in range(1,n+1):
    answer.append((i,bfs(i)))
max_b = max(b for _,b in answer)
result = [a for a, b in answer if b == max_b]
print(*result)
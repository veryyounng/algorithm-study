import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)


n = int(input())
a,b = map(int,input().split())

m = int(input())
list = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    x, y = map(int, input().split())
    list[x].append(y)
    list[y].append(x)


def dfs(v,cnt):
    global answer
    visited[v]=True
    if v == b:
        answer = cnt
        return
    for next in list[v]:
        if not visited[next]:
            dfs(next,cnt+1)

answer = -1
dfs(a,0)
print(answer)

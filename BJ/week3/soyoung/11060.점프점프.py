from collections import deque

n = int(input())
graph = list(map(int, input().split()))

def BFS():
    queue = deque()
    queue.append((0,0))

    visited = [0] * (n+1)
    visited[0] = 1

    while queue:
        x, cnt = queue.popleft()

        if x == n-1:
            return cnt
        
        for next in range(x+1,  min(n, x + graph[x] + 1)):
            if visited[next] == 0:
                visited[next] = 1
                queue.append((next, cnt+1))

    return -1

print(BFS())
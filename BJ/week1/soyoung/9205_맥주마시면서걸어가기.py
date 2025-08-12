from collections import deque

def men(a, b):
    return abs(a[0]-b[0]) + abs(a[1] - b[1])

t = int(input())
for _ in range(t):
    n = int(input().strip())
    
    graph = [list(map(int, input().split())) for _ in range(n+2)]
    visited = [0] * (n+2)
    
    queue = deque([0])
    visited[0] = 1
    
    happy = False
    
    while queue:
        v = queue.popleft()
        
        if v == n+1:
            happy = True
            break
        
        for next in range(n+2):
            if visited[next] == 0 and men(graph[v], graph[next]) <= 1000:
                visited[next] = 1
                queue.append(next)

    print("happy" if happy else "sad")
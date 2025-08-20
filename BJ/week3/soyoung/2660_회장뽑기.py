from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    
    graph[a].append(b)
    graph[b].append(a)

def BFS(v):
    visited = [-1] * (n+1)
    queue = deque([v])
    while queue:
        v = queue.popleft()
        visited[v] = 0
    
        for next in graph[v]:
            if visited[next] == -1:
                visited[next] = visited[v] + 1
                queue.append(next)
    
        if -1 in visited[1:]:
            return 10**9
        return max(visited[1:])
    
score = [0] * (n + 1)
for i in range(1, n + 1):
    score[i] = BFS(i)

minimum = score[1]
for i in range(2, n + 1):
    if score[i] < minimum:
        minimum = score[i]
        
candidate = []
score = [0] * (n+1)

for i in score:
    if score[i] == minimum:
        candidate.append(i)
        
print(minimum, len(candidate))
print(*sorted(candidate))
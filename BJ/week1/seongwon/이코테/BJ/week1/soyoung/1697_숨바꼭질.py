from collections import deque

n, k = map(int, input().split())

queue = deque()
queue.append(n)
max = 100001
visited = [0] * (max)

def BFS(v):
    while queue:
        v = queue.popleft()
        if v == k:
            return visited[v]
        for next in (v-1, v+1, v*2):
            if next >=0 and next < max and visited[next] == 0:
                visited[next] = visited[v] + 1
                queue.append(next)

print(BFS(n))

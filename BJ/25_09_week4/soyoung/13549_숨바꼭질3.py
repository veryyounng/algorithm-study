from collections import deque
n, k = map(int, input().split())

queue = deque()
queue.append(n)
maxi = 2000000
visited = [-1] * (maxi)
visited[n] = 0

def BFS(x):
    while queue:
        x = queue.popleft()
        if x == k:
            return visited[x]
        
        for nxt in (2*x, x+1, x-1):
            if 0 <= nxt < maxi and visited[nxt] == -1:
                if nxt == 2*x:
                    visited[nxt] = visited[x]
                    queue.appendleft(nxt)
                else:
                    visited[nxt] = visited[x] + 1
                    queue.append(nxt)

    return -1

print(BFS(n))
    
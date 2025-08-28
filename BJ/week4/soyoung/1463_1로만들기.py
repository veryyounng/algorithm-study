from collections import deque
import sys

n = int(input())

if n == 0:
    print(0)
    sys.exit(0)
    
dist = [-1] * (n+1)
queue = deque([n])
dist[n] = 0

while queue:
    x = queue.popleft()
    
    if x == 1:
        print(dist[1])
        break
    
    if x % 3 == 0 and dist[x // 3] == -1:
        dist[x // 3] = dist[x] + 1
        queue.append(x//3)
        
    if x % 2 == 0 and dist[x // 2] == -1:
        dist[x // 2] = dist[x] + 1
        queue.append(x // 2)
        
    if x-1 >= 1 and dist[x-1] == -1:
        dist[x-1] = dist[x] + 1
        queue.append(x-1)

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

n = int(input())
arr = list(map(int,input().split()))+([0]*100)
dist = [-1]*1100
dist[0]=0

queue = deque([0])
while queue:
    q = queue.popleft()
    for i in range(q+1,arr[q]+q+1):
        if dist[i]==-1:
            dist[i]=dist[q]+1
            queue.append(i)
if dist[n-1] == -1:
    print(-1)
else:
    print(dist[n-1])

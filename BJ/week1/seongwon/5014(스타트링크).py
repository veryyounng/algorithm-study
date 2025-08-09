import sys
sys.stdin = open('input.txt','r')
from collections import deque
totalfloor, startfloor, targetfloor, up, down = map(int,input().split())


visited = [False]*(totalfloor+1)
def bfs(start):
    queue = deque()
    queue.append((start,0))
    visited[start]=True
    while queue:
        pos,cnt = queue.popleft()
        if pos == targetfloor:
            return cnt 
        for next_pos in (pos+up, pos-down):
            if 1 <= next_pos <= totalfloor and not visited[next_pos]:
                visited[next_pos]=True
                queue.append((next_pos,cnt+1))
    return None
result = bfs(startfloor)
if result is None:
    print("use the stairs")
else:
    print(result)
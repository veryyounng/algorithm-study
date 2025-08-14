import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

n,k = map(int,input().split())
MAX = 100000
visited = [False] * (MAX + 1)

def bfs(start):
    queue = deque()
    queue.append((start, 0))  # (현재 위치, 시간)
    visited[start] = True

    while queue:
        pos,time = queue.popleft()
        if pos == k : 
            return time
        for next_pos in (pos-1, pos+1, pos*2):
            if 0<=next_pos<=MAX and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos,time+1))




print(bfs(n))

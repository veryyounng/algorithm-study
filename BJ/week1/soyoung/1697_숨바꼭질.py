from collections import deque
n, k = map(int, input().split())

maxi = 200000
dis = [-1] * (maxi)

queue = deque()
queue.append(n)
dis[n] = 0

def BFS():
    while queue:
        x = queue.popleft()
        if x == k:
            return dis[x]
    
        for nxt in (x-1, x+1, 2*x):
            if 0 <= nxt < maxi and dis[nxt] == -1:
                dis[nxt] = dis[x] + 1
                queue.append(nxt)

print(BFS())
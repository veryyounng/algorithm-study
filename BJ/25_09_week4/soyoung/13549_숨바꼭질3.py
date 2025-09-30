from collections import deque

n, k = map(int, input().split())
maxi = 100000

dis = [-1] * (maxi + 1)
dis[n] = 0

def BFS():
    queue = deque()
    queue.append(n)
    
    while queue:
        x = queue.popleft()
        
        if x == k:
            return dis[x]
        
        for nxt in (x-1, x+1, 2*x):
            if 0 <= nxt <= maxi and dis[nxt] == -1:
                if nxt == 2*x:
                    dis[nxt] = dis[x]
                    queue.appendleft(nxt)
                    
                else:
                    dis[nxt] = dis[x] + 1
                    queue.append(nxt)
print(BFS())
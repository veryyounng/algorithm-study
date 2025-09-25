import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split())

MAX = 100001
dp = [-1] * MAX

def bfs(start):
    q = deque([start])
    dp[start] = 0
    
    while q:
        node = q.popleft()
        if node == m:
            print(dp[node])
            return
        
        next_node = node * 2
        if 0 <= next_node < MAX and dp[next_node] == -1:
            dp[next_node] = dp[node]
            q.appendleft(next_node)

        for next_node in (node - 1, node + 1):
            if 0 <= next_node < MAX and dp[next_node] == -1:
                dp[next_node] = dp[node] + 1
                q.append(next_node)

bfs(n)

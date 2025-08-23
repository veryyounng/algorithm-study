import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

n = int(input())

members = [[] for _ in range(n+1)]
while True:
    
    a,b = map(int,input().split())
    if a==-1 and b==-1:
        break
    members[a].append(b)
    members[b].append(a)

def bfs(i,score):
    check = [0]*(n+1)
    queue = deque()
    queue.append((i,score))
    print(i)
    while queue:
        print(queue)
        (i,score) = queue.popleft()
        check[i] = 1
        for friend in members[i]:
            if check[friend]==0:
                queue.append((friend,score+1))
    return score

result = []
answer = []

for i in range(1, n+1):    
    score = bfs(i,0)
    result.append((i,score))

possible_score = n
for i,score in result:
    if score <= possible_score:
        possible_score = score
count = 0
for i,score in result:
    if possible_score==score:
        count+=1
        answer.append(i)
# print(possible_score, count)
# for a in sorted(answer):
#     print(a)






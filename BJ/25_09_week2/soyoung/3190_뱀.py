from collections import deque

n = int(input())
k = int(input())

#0은 빈칸, 1은 사과, 2는 뱀
board = [[0] * n for _ in range(n)]
for _ in range(k):
    x,y = map(int, input().split())
    board[x-1][y-1] = 1

l = int(input().strip())
#뱀의 방향 전환
turns = {}
for _ in range(l):
    x, c = input().split()
    turns[int(x)] = c
    #x초 뒤에 c방향으로 회전
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
idx = 0

sanke = deque()
sanke.append((0,0))
board[0][0] = 2

time = 0
while True:
    time += 1
    hr, hc = sanke[0]
    dr, dc = dirs[idx]
    nr, nc = hr + dr, hc + dc
    
    #벽 충돌
    if not (0 <= nr < n and 0 <= nc < n):
        print(time)
        break
    
    apple = board[nr][nc] == 1
    
    #사과 없으면 꼬리만 이동
    if not apple:
        tr, tc = sanke.pop()
        board[tr][tc] = 0
    
    #자기 몸 충돌
    if board[nr][nc] == 2:
        print(time)
        break
    
    # 머리 이동, 사과 먹으면
    sanke.appendleft((nr,nc))
    board[nr][nc] = 2
    
    # 회전
    if time in turns:
        if turns[time] == 'D':
            idx = (idx + 1) % 4
        else:
            idx = (idx + 3) % 4


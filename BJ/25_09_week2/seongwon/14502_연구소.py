import sys
sys.stdin = open('input.txt', 'r')

n,m = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

tmp = [[0]*m for _ in range(n)]

def virus(x,y):
    tmp[x][y]=2
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<n and 0<=yy<m and tmp[xx][yy]==0:
            virus(xx,yy)
answer = 0
def dfs(x,y,cnt):
    global answer
    maps[x][y]=1
    if cnt==3: #벽을 3개 세운거임
        #바이러스를 퍼뜨린다.
        for i in range(n):
            for j in range(m):
                tmp[i][j] = maps[i][j]
        for i in range(n):
            for j in range(m):
                if tmp[i][j]==2:
                    virus(i,j)
        
        #tmp에서 0의 개수(안전영역)를 센다.
        safe_cnt = 0
        for i in range(n):
            for j in range(m):
                if tmp[i][j]==0:
                    safe_cnt = safe_cnt + 1
        answer = max(answer, safe_cnt)
    else:
        for i in range(n):
            for j in range(m):
                if maps[i][j] == 0:
                    dfs(i, j, cnt+1)
                    maps[i][j] = 0
    maps[x][y] = 0




for i in range(n):
    for j in range(m):
        if maps[i][j]==0:
            dfs(i,j,1)
            

print(answer)


##############################
##지피티코드
# import sys
# sys.stdin = open('input.txt', 'r')

# n, m = map(int, input().split())

# maps = [list(map(int, input().split())) for _ in range(n)]

# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# tmp = [[0]*m for _ in range(n)]

# def virus(x, y):
#     tmp[x][y] = 2
#     for i in range(4):
#         xx = x + dx[i]
#         yy = y + dy[i]
#         if 0 <= xx < n and 0 <= yy < m and tmp[xx][yy] == 0:
#             virus(xx, yy)

# answer = 0

# def dfs(cnt):
#     global answer
#     if cnt == 3:  # 벽 3개 세움
#         # maps 복사 -> tmp
#         for i in range(n):
#             for j in range(m):
#                 tmp[i][j] = maps[i][j]
#         # 바이러스 퍼뜨리기
#         for i in range(n):
#             for j in range(m):
#                 if tmp[i][j] == 2:
#                     virus(i, j)
#         # 안전 영역 계산
#         safe_cnt = 0
#         for i in range(n):
#             for j in range(m):
#                 if tmp[i][j] == 0:
#                     safe_cnt += 1
#         answer = max(answer, safe_cnt)
#         return

#     for i in range(n):
#         for j in range(m):
#             if maps[i][j] == 0:
#                 maps[i][j] = 1
#                 dfs(cnt+1)
#                 maps[i][j] = 0


# dfs(0)
# print(answer)
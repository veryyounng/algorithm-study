import sys
sys.stdin = open('input.txt', 'r')
n,m,x,y,c = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
cmds=list(map(int,input().split()))

dice = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]


def swap(cmd):
   
    #동쪽
    if cmd==1:
        dice[1][0],dice[1][1],dice[1][2],dice[3][1] = dice[1][1], dice[1][2], dice[3][1], dice[1][0]
    #서쪽
    elif cmd==2:
        dice[1][0],dice[1][1],dice[1][2],dice[3][1] = dice[3][1], dice[1][0], dice[1][1], dice[1][2]
    #북쪽
    elif cmd==3:
        dice[0][1],dice[1][1],dice[2][1],dice[3][1] = dice[1][1],dice[2][1],dice[3][1],dice[0][1]
    #남쪽
    elif cmd==4:
        dice[0][1],dice[1][1],dice[2][1],dice[3][1] = dice[3][1],dice[0][1],dice[1][1],dice[2][1]
    

#북동남서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

for c in cmds:
    #북
   
    if c==3:
        nx=x+dx[0]
        ny=y+dy[0]
        if 0<=nx<n and 0<=ny<m:
            swap(c)
            #바닥이
            if maps[nx][ny]==0:
                maps[nx][ny]=dice[3][1]     
            elif maps[nx][ny]!=0:
                dice[3][1]=maps[nx][ny]
                maps[nx][ny]=0
            x=nx
            y=ny
            print(dice[1][1])
    #동
    elif c==1:
        nx=x+dx[1]
        ny=y+dy[1]
        if 0<=nx<n and 0<=ny<m:
            swap(c)
            #바닥이
            if maps[nx][ny]==0:
                maps[nx][ny]=dice[3][1]     
            elif maps[nx][ny]!=0:
                dice[3][1]=maps[nx][ny]
                maps[nx][ny]=0
            x=nx
            y=ny
            print(dice[1][1])
    #남
    elif c==4:
        nx=x+dx[2]
        ny=y+dy[2]
        if 0<=nx<n and 0<=ny<m:
            swap(c)
            #바닥이
            if maps[nx][ny]==0:
                maps[nx][ny]=dice[3][1]     
            elif maps[nx][ny]!=0:
                dice[3][1]=maps[nx][ny]
                maps[nx][ny]=0
            x=nx
            y=ny
            print(dice[1][1])
    #서
    elif c==2:
        nx=x+dx[3]
        ny=y+dy[3]
        if 0<=nx<n and 0<=ny<m:
            swap(c)
            #바닥이
            if maps[nx][ny]==0:
                maps[nx][ny]=dice[3][1]     
            elif maps[nx][ny]!=0:
                dice[3][1]=maps[nx][ny]
                maps[nx][ny]=0
            x=nx
            y=ny
            print(dice[1][1])

    
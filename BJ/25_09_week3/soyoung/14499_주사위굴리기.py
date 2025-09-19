n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dice_move = list(map(int, input().split()))
dice = [0,0,0,0,0,0]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def roll(move):
    if move == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
    elif move == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
    elif move == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
    elif move == 4:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]
    
for i in dice_move:
    nx = x + dx[i-1]
    ny = y + dy[i-1]

    if not (0 <= nx < n and 0 <= ny < m):
        continue
    x, y = nx, ny

    roll(i)

    if board[x][y] == 0:
        board[x][y] = dice[5]
    else:
        dice[5] = board[x][y]
        board[x][y] = 0
    print(dice[0])


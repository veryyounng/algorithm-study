n, m = map(int, input().split())

#지금 칸 좌표, 방향
r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]

#방향 설정 배열 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0

while True:
    #지금 칸이 빈칸이라면 청소할 것
    if room[r][c] == 0:
        room[r][c] = 2
        cnt += 1

    cleaned = False

    #방향 정하기, 반시계 방향
    for _ in range(4):
        d = (d + 3) % 4
        nx = r + dx[d]
        ny = c + dy[d]

        if room[nx][ny] == 0:
            cleaned = True
            r, c = nx, ny
            break
    
    if cleaned:
        continue

    #현재 칸의 주변 4칸 중 청소되지 않은 빈칸이 없는 경우 후진
    back = (d+2) % 4
    br, bc = r + dx[back], c + dy[back]
    
    if room[br][bc] == 1:
        break
    else:
        r,c = br, bc

print(cnt)
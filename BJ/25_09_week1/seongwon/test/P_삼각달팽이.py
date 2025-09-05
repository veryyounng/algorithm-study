def solution(n):
    maps = [[0]*n for _ in range(n)]
    x, y = 0, 0
    cnt = 1
    total = n*(n+1)//2  # 삼각 달팽이 총 숫자 개수
    cmd = ['down', 'right', 'dia']
    direction = 0  # 현재 방향

    while cnt <= total:
        maps[x][y] = cnt
        cnt += 1

        if cmd[direction] == 'down':
            nx, ny = x + 1, y
        elif cmd[direction] == 'right':
            nx, ny = x, y + 1
        else:  # 'dia'
            nx, ny = x - 1, y - 1


        if nx >= n or ny >= n or nx < 0 or ny < 0 or maps[nx][ny] != 0:
            direction = (direction + 1) % 3
            if cmd[direction] == 'down':
                nx, ny = x + 1, y
            elif cmd[direction] == 'right':
                nx, ny = x, y + 1
            else:  # 'dia'
                nx, ny = x - 1, y - 1

        x, y = nx, ny

    # 결과를 1차원 리스트로 변환
    result = []
    for row in maps:
        for num in row:
            if num != 0:
                result.append(num)
    return result


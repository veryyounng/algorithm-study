import sys
import copy
sys.stdin = open('input.txt', 'r')

sys.setrecursionlimit(10**6)

n = int(input())

original_maps = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

def dfs(x, y, maps):
    maps[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] != 0:
            dfs(nx, ny, maps)

def safecount(maps, water_level):
    for i in range(n):
        for j in range(n):
            if maps[i][j] <= water_level:
                maps[i][j] = 0

    count = 0
    for i in range(n):
        for j in range(n):
            if maps[i][j] != 0:
                dfs(i, j, maps)
                count += 1
    return count

answer = 0
max_height = max(map(max, original_maps))  # 높이 최대값 계산

for water_level in range(0, max_height + 1):
    tempmaps = copy.deepcopy(original_maps)
    region_count = safecount(tempmaps, water_level)
    answer = max(answer, region_count)

print(answer)

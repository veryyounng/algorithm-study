import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int,input().split())
maps=[]
for _ in range(n):
    maps.append(list(input()))

answer = n*m+1
for i in range(n-7):
    for j in range(m-7):
        before=maps[i][j]
        cnt = 0
        for x in range(8):
            for y in range(8):
                if before !=maps[i+x][y]:
                    before = maps[x][y]
                else:
                    if before=="W":
                        before="B"
                    else:
                        before="W"
                cnt+=1
        if answer>cnt:
            answer = cnt
print(answer)
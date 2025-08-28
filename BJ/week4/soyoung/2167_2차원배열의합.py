n, m = map(int, input().split())

p = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    row = [0] + list(map(int, input().split()))
    row_sum = 0
    
    for j in range(1, m+1):
        row_sum += row[j]
        p[i][j] = p[i-1][j] + row_sum

k = int(input())
out = []
    
for _ in range(k):
    i, j, x, y = map(int, input().split())
    s = p[x][y]- p[i-1][y]- p[x][j-1] + p[i-1][j-1]
    out.append(str(s))
        
print('\n'.join(out))
        
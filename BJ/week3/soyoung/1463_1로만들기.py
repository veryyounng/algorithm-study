n = int(input())

dp = [0] * (n+1)

for x in range(2, n+1):
    best = dp[x-1]+1
    
    if x % 2 == 0:
        best = min(dp[x//2]+1, best)
        
    if x % 3 == 0:
        best = min(dp[x//3]+1, best)
        
    dp[x] = best
print(best)
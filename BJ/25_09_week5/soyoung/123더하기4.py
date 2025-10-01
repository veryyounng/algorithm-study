t = int(input())
coins = [1,2,3]
arr = []

for _ in range(t):
    n = int(input())
    dp = [0] * (n+1)
    dp[0] = 1
    
    for c in coins:
        for i in range(c, n+1):
            dp[i] += dp[i-c]
    
    arr.append(dp[n])
    
for i in arr:
    print(i)
import sys
sys.stdin = open('input.txt', 'r')


t = int(input())

dp = [1] * 10001


#2추가
for i in range(2, 10001):
    dp[i] += dp[i - 2]
    
#3추가
for i in range(3, 10001):
    dp[i] += dp[i - 3]

for _ in range(t):
    n = int(input())
    print(dp[n])
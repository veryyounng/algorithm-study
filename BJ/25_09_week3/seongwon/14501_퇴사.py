import sys
sys.stdin = open('input.txt', 'r')
n= int(input())
ti=[]
pi=[]
for _ in range(n):
    a,b=map(int,input().split())
    ti.append(a)
    pi.append(b)


maxx=-999999999
def dfs(L,sum):
    global maxx
    if L == n:
        if maxx < sum:
            maxx=sum
            return 
    else:
        if L+ti[L]<=n:
            dfs(L+ti[L],sum+pi[L])
        dfs(L+1,sum)

dfs(0,0)
print(maxx)
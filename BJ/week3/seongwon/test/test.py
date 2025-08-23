import sys
sys.stdin = open('input.txt', 'r')


n= int(input())
arr = list(map(int,input().split()))



tmp=[]
def dfs(v):
    global tmp
    if n==v:
        print(tmp)
        return
    else:
        tmp.append(arr[v])
        dfs(v+1)
        tmp.pop()
        dfs(v+1)

dfs(0)



import sys

s = list(input())
t = list(input())

def DFS(x):
    if x == s:
        print(1)
        sys.exit()
    if len(x) < len(s):
        return
    
    if x[-1] == 'A':
        DFS(x[:-1])
    if x[0] == 'B':
        DFS(x[1:][::-1])
DFS(t)
print(0)
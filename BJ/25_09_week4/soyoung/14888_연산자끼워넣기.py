n = int(input())
a = list(map(int, input().split()))
plus, minus, mul, divi = map(int, input().split())

def cxx14_div(x: int, y: int) -> int:
    q = abs(x) // abs(y)
    return -q if (x < 0) ^ (y < 0) else q

maximum = -10**18
minimum = 10**18

def DFS(i, tmp, p, mi, mu, di):
    global maximum, minimum
    
    if i == n:
        maximum = max(maximum, tmp)
        minimum = min(minimum, tmp)
        return
    
    if p:
        DFS(i+1, tmp + a[i], p-1, mi, mu, di)
    if mi:
        DFS(i+1, tmp - a[i], p, mi-1, mu, di)
    if mu:
        DFS(i+1, tmp * a[i], p, mi, mu-1, di)
    if di:
        DFS(i+1, cxx14_div(tmp, a[i]), p, mi, mu, di-1)

DFS(1, a[0], plus, minus, mul, divi)
print(maximum)
print(minimum)
    
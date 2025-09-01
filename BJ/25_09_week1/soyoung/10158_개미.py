w,h = map(int, input().split())
p,q = map(int, input().split())
t= int(input())

px = (p+t) % (2*w)
py = (q+t) % (2*h)

x = px if px <= w else 2*w -px
y = py if py <= h else 2*h -py

print(x,y)
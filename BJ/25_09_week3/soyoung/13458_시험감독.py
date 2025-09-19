import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
total = 0

for i in a:
    total += 1
    tmp = i - b
    if tmp > 0:
        total += (tmp + c-1)//c

print(total)
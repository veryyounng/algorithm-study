import sys
sys.stdin = open('input.txt', 'r')


n, m = map(int, input().split())

listen = set()
for _ in range(n):
    listen.add(input())  

see = set()
for _ in range(m):
    see.add(input())

# 교집합 구하기
result = sorted(listen & see)

# 출력
print(len(result))
for name in result:
    print(name)
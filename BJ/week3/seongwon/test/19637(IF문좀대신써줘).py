import sys
sys.stdin = open('input.txt', 'r')

n,m = map(int,input().split())
power_maps = []
for _ in range(n):
    (status,power) = input().split()
    power_maps.append((status, int(power)))


def score_print(num):
    for (status,power) in power_maps:
        if num<=power:
            return status



for _ in range(m):
    num = int(input())
    print(score_print(num))
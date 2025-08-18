import sys
sys.stdin = open('input.txt', 'r')

n = input()
sorted_digits = sorted(n, reverse =True)
result = ''.join(sorted_digits)  

print(result)

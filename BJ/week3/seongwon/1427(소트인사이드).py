import sys
sys.stdin = open('input.txt', 'r')

n = input()
sorted_digits = sorted(n, reverse =True)
print(sorted_digits)
result = ''.join(sorted_digits)  

print(result)

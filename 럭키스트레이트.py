import sys
sys.stdin = open('input.txt', 'r')
n = input()
summary = 0
length = len(n)
for i in range(length//2):
    summary += int(n[i])
for i in range(length//2,length):
    summary -= int(n[i])
if summary == 0:
    print("LUCKY")
else:
    print('READY')
    

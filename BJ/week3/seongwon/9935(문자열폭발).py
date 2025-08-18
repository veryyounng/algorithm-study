import sys
sys.stdin = open('input.txt', 'r')

alpha = input()
bomb = input()
bomb_len = len(bomb)

stack = []
for ch in alpha:
    stack.append(ch)
    if len(stack) >= bomb_len and ''.join(stack[-bomb_len:]) == bomb:
        #1 둘중 하나쓰면됨
        del stack[-bomb_len:]
        #2
        # for _ in range(bomb_len):
        #     stack.pop()
result = ''.join(stack)
print(result if len(result)>0 else "FRULA")

s = input().strip()
t = input().strip()

def game():
    cur = t
    while len(cur) > len(s):
        if cur[-1] == 'A':
            cur = cur[:-1]
        else:  # 마지막이 'B'면 B를 떼고 뒤집기
            cur = cur[:-1][::-1]
    return 1 if cur == s else 0

print(game())

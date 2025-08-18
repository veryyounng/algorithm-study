import sys
from collections import deque
input = sys.stdin.readline

T = int(input().strip())
answers = []

for _ in range(T):
    p = input().strip()
    n = int(input().strip())
    arr_str = input().strip()

    # 배열 파싱
    if n == 0:
        dq = deque()
    else:
        dq = deque(map(int, arr_str[1:-1].split(',')))

    rev = False
    error = False

    for cmd in p:
        if cmd == 'R':
            rev = not rev
        else:  # 'D'
            if not dq:
                answers.append('error')
                error = True
                break
            if rev:
                dq.pop()       # 뒤집힌 상태면 뒤에서 제거
            else:
                dq.popleft()   # 정상 상태면 앞에서 제거

    if not error:
        if rev:
            dq.reverse()  # 마지막에 한 번만 뒤집기
        answers.append('[' + ','.join(map(str, dq)) + ']')

print('\n'.join(answers))
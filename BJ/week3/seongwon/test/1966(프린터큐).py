import sys
sys.stdin = open('input.txt', 'r')
from collections import deque


# 문서 개수와 궁금한 문서의 위치
document_count, target_index = map(int, input().split())

# 각 문서의 중요도 입력
priorities = list(map(int, input().split()))

# (중요도, 원래 인덱스) 형태로 큐에 저장
queue = deque((priority, idx) for idx, priority in enumerate(priorities))

print_order = 0  # 몇 번째로 인쇄되는지 세는 변수

while queue:
    current = queue.popleft()

    # 현재 문서보다 높은 중요도를 가진 문서가 하나라도 있으면 맨 뒤로 보냄
    if any(current[0] < other[0] for other in queue):
        queue.append(current)
        print(queue)
    else:
        # 인쇄함
        print_order += 1
        if current[1] == target_index:
            print(print_order)
            break

    
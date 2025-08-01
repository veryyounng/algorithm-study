from sys import stdin
from collections import deque

# 빠른 입력
input = stdin.readline

# N: 숫자 개수, K: 한 번에 뒤집는 수의 개수
N,K = map(int, input().split())

# 숫자들을 공백 없이 문자열로 붙임 (처리 편하게 하기 위해)
numbers = "".join(input.split())

# 목표 상태 (오름차순 정렬된 문자열)
sorted_numbers = "".join(sorted(numbers))

# 방문한 상태를 저장 (중복 탐색 방지)
visited = []
visited[n] = True

#  visited = {
#     "54321": True
# }

# BFS를 위한 큐 초기화: [현재 상태, 현재까지 뒤집은 횟수]
queue = deque([[numbers, 0]])

# 정답 초기값 -1 (불가능한 경우)
ans = -1

# BFS 시작
while queue:
    target, count = queue.popleft()

    # 만약 정렬 완료 상태에 도달했다면 → 답 저장하고 종료
    if target == sorted_numbers:
        ans = count
        break

    # 가능한 모든 위치 i에서 i부터 i+K까지 K개의 수를 뒤집기
    for i in range(N - K +1):
        # 문자열 슬라이싱으로 i~i+K 범위만 뒤집기
        next_state = (
            target[0:i]                      # 왼쪽 그대로
            + target[i : i + K][::-1]        # 가운데 K개 뒤집기
            + target[i + K :]                # 오른쪽 그대로
        )

        # 이미 방문한 상태면 무시
        if next_state in visited:
            continue

        # 새 상태면 큐에 추가하고 방문 표시
        queue.append([next_state, count+1])
        visited[next_state] = True

# 결과 출력
print(ans)

# 💻 [문제 요약]
# N개의 컴퓨터, M개의 신뢰 관계가 있을 때
# '한 컴퓨터를 해킹하면 연결된 컴퓨터들도 같이 해킹된다'는 조건 하에
# 한 번 해킹으로 가장 많은 컴퓨터를 감염시킬 수 있는 컴퓨터 번호를 오름차순으로 출력하는 문제

import sys
from collections import deque

# 🔹 입력받기
input = sys.stdin.readline
n, m = map(int, input().split())  # n: 컴퓨터 수, m: 신뢰 관계 수

# 그래프 초기화: 컴퓨터 번호는 1번부터 시작하므로 n+1 크기로 생성
graph = [[] for _ in range(n + 1)]

# 🔹 신뢰 관계 입력 받기
# A B: A가 B를 신뢰한다 → B를 해킹하면 A도 해킹 가능 → 간선 방향은 B → A
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)  # 역방향 간선 저장

# 🔹 BFS 함수 정의
def bfs(start):
    visited = [False] * (n + 1)  # 방문 여부 체크
    queue = deque([start])      # 시작 노드를 큐에 넣음
    visited[start] = True
    count = 1  # 해킹 가능한 컴퓨터 수 (자기 자신 포함)

    while queue:
        now = queue.popleft()
        # 현재 노드(now)를 해킹했을 때 연결된 다른 노드를 확인
        for next_node in graph[now]:
            if not visited[next_node]:  # 아직 방문하지 않았다면
                visited[next_node] = True  # 방문 처리
                queue.append(next_node)   # 큐에 추가
                count += 1                # 해킹 가능한 컴퓨터 수 증가
    return count

# 🔹 모든 노드를 해킹 시작점으로 가정하여 BFS 돌리기
max_count = 0        # 현재까지 해킹 가능한 최대 컴퓨터 수
result = []          # 최대값을 만든 컴퓨터 번호들을 저장

for i in range(1, n + 1):
    count = bfs(i)   # i번 컴퓨터를 해킹 시작점으로 했을 때 감염 수
    if count > max_count:
        max_count = count      # 새로운 최대값이면 갱신
        result = [i]           # 결과 리스트 초기화
    elif count == max_count:
        result.append(i)       # 최대값과 같다면 결과 리스트에 추가

# 🔹 결과 출력
# sorted(result): 오름차순 정렬된 리스트 반환
# *result: 리스트를 언팩하여 공백으로 구분해 print
print(*sorted(result))  # 예: [1, 2, 3] → 출력: 1 2 3
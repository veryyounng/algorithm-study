from collections import deque

F, S, G, U, D = map(int, input().split())
arr = [0] * (F + 1)

def BFS(v):
    queue = deque([v])
    arr[v] = 1  # 시작 위치 방문 처리

    while queue:
        v = queue.popleft()
        if v == G:
            return arr[v] - 1  # 시작 지점이 1이므로 -1 해줘야 실제 버튼 누른 횟수
        for next in (v + U, v - D):
            if 0 < next <= F and arr[next] == 0:
                arr[next] = arr[v] + 1
                queue.append(next)

    return "use the stairs"

if S == G:
    print(0)
else:
    print(BFS(S))

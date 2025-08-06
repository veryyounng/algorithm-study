#입력받기
n = int(input())
m = int(input())

#graph 만들기
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b =map(int, input().split())
    graph[a].append(b)  # a에서 b로 가는 간선
    graph[b].append(a)  # b에서 a로 가는 간선 (무방향 그래프)
    
#방문 리스트 만들기
visited = [False] * (n + 1)

#dfs 함수 만들기
def dfs(v):
    visited[v] = True  # 현재 노드 방문 처리
    for next in graph[v]:  # 현재 노드와 연결된 모든 노드 탐색
        if not visited[next]:  # 아직 방문하지 않은 노드라면
            dfs(next)  # 재귀적으로 DFS 호출

# DFS 시작
dfs(1)  # 1번 컴퓨터에서 시작

# 감염된 컴퓨터 수 출력 (1번 컴퓨터는 제외)
print(visited.count(True) - 1)  # 방문한 노드 수에서 1번 컴퓨터 제외
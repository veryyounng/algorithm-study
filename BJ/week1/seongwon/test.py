# 1. 트리의 가장 먼 잎 노드 찾기
# 문제
# N개의 노드로 이루어진 트리(1번 루트, 무방향, 가중치 있음)가 주어진다.
# 1번 노드에서 출발해서, 가장 멀리 떨어진 잎 노드(자식 없는 노드)와 그 거리(가중치 합)를 출력하라.

# 입출력 예시
# 입력:
# 5
# 1 2 3
# 1 3 5
# 2 4 7
# 3 5 2
# 출력:
# 4 10

import sys
sys.stdin = open('input.txt', 'r')

n=int(input())
graph =  [[] for _ in range(n+1)]
for _ in range(n-1):
    v1,v2,weight = map(int,input().split())
    graph[v1].append((v2,weight))
    graph[v2].append((v1,weight))




def dfs (node, weight):
    visited[node]=True
    farthest = (node, weight)
    for neighbor_node,neighbor_weight in graph[node]:
        if not visited[neighbor_node]:
            (tmp_node,tmp_weight) = dfs(neighbor_node,weight+neighbor_weight)
            if tmp_weight > farthest[1]: 
                farthest = (tmp_node,tmp_weight)
    return farthest
visited = [False]*(n+1)  
(n,w) =dfs(1,0)
print(n,w)


# 2. 특정 값 이상인 경로의 최대 깊이 구하기
# 문제
# N개의 노드로 이루어진 트리(1번 루트, 무방향, 가중치 있음)가 주어진다.
# 모든 경로 중 **누적 가중치 합이 X 이상이 되는 경로의 최대 깊이(노드 개수)**를 출력하라.

# 입출력 예시
# 입력:
# 6
# 1 2 2
# 1 3 3
# 2 4 4
# 2 5 2
# 3 6 1
# 5
# 출력:
# 3
# 설명:
# 1-2-4 : 거리 6 (노드 3개)
# 1-3-6 : 거리 4 (X=5 미만)
# 최대 깊이는 3
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))
x = int(input())

def dfs(node, dist, depth, visited):
    visited[node] = True
    max_depth = 0
    # 리프노드거나 모든 자식 방문하면 반환
    is_leaf = True
    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            is_leaf = False
            ret = dfs(neighbor, dist + weight, depth + 1, visited)
            max_depth = max(max_depth, ret)
    # 리프 노드거나 자식 다 돌고 나서, 조건 만족하면 깊이 리턴
    if dist >= x:
        max_depth = max(max_depth, depth)
    return max_depth

visited = [False] * (n + 1)
answer = dfs(1, 0, 1, visited)
print(answer)

# 3. 모든 리프까지의 거리의 합 구하기 (DFS 리턴값 누적)
# 문제
# N개의 노드로 이루어진 트리(1번 루트, 무방향, 가중치 있음)가 주어진다.
# 루트(1번)에서 모든 리프노드까지의 거리의 합을 출력하라.
# DFS로 “서브트리에서 리프까지의 거리”를 리턴받아 누적하는 패턴을 연습해볼 것.

# 입출력 예시
# 입력:
# 4
# 1 2 3
# 1 3 2
# 2 4 4
# 출력:
# 9
# 설명:
# 1-3 : 2
# 1-2-4 : 3+4=7
# 총합: 2+7=9


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

def dfs(node, dist, visited):
    visited[node] = True
    is_leaf = True
    total = 0
    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            is_leaf = False
            total += dfs(neighbor, dist + weight, visited)
    # 리프노드라면 지금까지 온 거리(dist)를 반환
    if is_leaf:
        return dist
    return total

visited = [False] * (n + 1)
answer = dfs(1, 0, visited)
print(answer)
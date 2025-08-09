import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)


n = int(input())
a,b = map(int,input().split())

m = int(input())
list = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    x, y = map(int, input().split())
    list[x].append(y)
    list[y].append(x)


# def dfs(v,cnt):
#     global answer
#     visited[v]=True
#     if v == b:
#         answer = cnt
#         return
#     for next in list[v]:
#         if not visited[next]:
#             dfs(next,cnt+1)

# answer = -1
# dfs(a,0)
# print(answer)
def dfs(v, cnt):
    visited[v] = True
    if v == b:
        return cnt  # 목표에 도달했으면 현재 촌수 반환
    for nv in list[v]:
        if not visited[nv]:
            cnt_result = dfs(nv, cnt + 1)  # 재귀 호출
            if cnt_result is not None:  # 찾았다면 값 유지
                return cnt_result
    return None  # 못 찾으면 None 반환

result = dfs(a, 0)
print(result if result is not None else -1)

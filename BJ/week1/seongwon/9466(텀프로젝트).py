import sys
sys.stdin = open('input.txt', 'r')

testcase= int(input())
def dfs(x):
    global team_count
    visited[x] = 1  # 방문 중
    next_student = graph[x]

    if visited[next_student] == 0:  # 아직 방문 안 함
        dfs(next_student)
    elif visited[next_student] == 1:  # 사이클 발견
        # 사이클에 속한 노드 수 세기
        cur = next_student
        cycle_len = 1
        while graph[cur] != next_student:
            cur = graph[cur]
            cycle_len += 1
        team_count += cycle_len

    visited[x] = 2  # 처리 완료


for _ in range(testcase):
    n = int(input())
   
    arr = list(map(int,input().split()))
    graph = [0] + arr  
    visited = [0] * (n + 1)
    team_count = 0
    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(i)
        
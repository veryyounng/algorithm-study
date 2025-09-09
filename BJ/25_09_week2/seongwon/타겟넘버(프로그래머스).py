numbers = [1, 1, 1, 1, 1]
target = 3

answer = 0
def dfs(v,total):
    global answer
    if v==len(numbers):
        if total == target:
            answer += 1
        return
    else:
        dfs(v+1,total+numbers[v])
        dfs(v+1,total-numbers[v])

dfs(0,0)
print(answer)
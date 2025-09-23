begin="hit"
target="cog"
words=["hot", "dot", "dog", "lot", "log", "cog"]
visited = [False]*len(words)




answer = 999999
    
def dfs(L,start):
    global answer
    if L>len(words):
        return
    if start == target:
        answer = min(answer, L)
        return
    else:
        # 두개 이상 포함 되는 단어가 있으면 dfs
        for i in range(len(words)):
            cnt = 0 
            
            for j in range(len(words[i]))  :
                if words[i][j]==start[j]:
                    cnt+=1
                if cnt==len(words[i])-1 and not visited[i]:
                    visited[i]=True
                    dfs(L+1,words[i])
                    visited[i]=False

dfs(0,begin)
if answer==999999:
    answer = 0
print(answer)
import sys
sys.stdin = open('input.txt', 'r')

testcase = int(input())
answer = []
for _ in range(testcase):
    n = int(input())
    arr = list(map(int,input().split()))    
    maxx = max(arr)
    fail = []
    teams = [[] for _ in range(maxx+1)]

    for i in range(1,maxx+1):
        cnt = 0
        for j in arr:
            if j==i:
                cnt = cnt+1
        if cnt<6:
            fail.append(i)

    score = 0

    for a in arr:
        if a in fail:
            continue
        else:
            score = score+1
            teams[a].append(score)


    flag = True
    while flag:
        for i in range(3):
            candidate = []
            wins = []
            for teamidx in range(len(teams)):
                if teams[teamidx]:
                    summ = sum(teams[teamidx][0:4+i])
                    candidate.append((teamidx,summ))
            _,minval = min(candidate,key=lambda x:x[1])
            for teamidx in range(len(teams)):
                if teams[teamidx]:
                    summ = sum(teams[teamidx][0:4+i])
                    if summ == minval:
                        wins.append(teamidx)
                        
            if len(wins)==1:
                answer.append(wins[0])
                flag = False
                break
                

for a in answer:
    print(a)

from collections import Counter

T = int(input())
for _ in range(T):
    n = int(input())
    order = list(map(int, input().split()))
    
    cnt = Counter(order)
    
    filterd_order = []
    
    for i in cnt:
        if cnt[i] == 6:
            filterd_order.append(i)
            
    #자격 팀에게만 1,2,3... 점수 부여
    team_points = {}
    point = 0
    for team in team_points:
        if team not in team_points:
            team_points[team] = []
        team_points[team].append(point)
        point += 1
        
     # 4) 각 팀의 상위 4명 점수 합과 5번째 점수로 우승팀 결정
    winner = None
    best_sum = 10**18
    best_fifth = 10**18
    
    for team, pnts in team_points.items():
        s4 = sum(pnts[:4])
        t5 = pnts[4]
        
        if s4 < best_sum:
            best_sum = s4
            best_fifth = t5
            winner = team
            
        elif s4 == best_fifth and t5 < best_fifth:
            best_sum = s4
            best_fifth = t5
            winner = team
print(winner)
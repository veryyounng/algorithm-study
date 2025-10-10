def solution(friends, gifts):
    friend_dict = dict()
    gift_score = dict()

    answer = dict()
    for friend in friends:
        gift_score[friend] = 0
        answer[friend]=0
    # 선물 주고받은 횟수 저장용 (딕셔너리 안에 딕셔너리)
    for friend in friends:
        friend_dict[friend] = dict()
        for other in friends:
            friend_dict[friend][other] = 0           
    for gift in gifts:
        give,receive = gift.split(' ')
        friend_dict[give][receive]=friend_dict[give][receive]+1
        gift_score[give]=gift_score[give]+1
        gift_score[receive]=gift_score[receive]-1
        
    print(gift_score)
    for friend in friends:  
        for other in friend_dict[friend]:
            if friend!=other:
                if friend_dict[friend][other] > friend_dict[other][friend]:
                    answer[friend]+=1
                elif friend_dict[friend][other] == friend_dict[other][friend]:
                    if gift_score[friend] > gift_score[other]:
                        answer[friend]+=1


    maxx = -1 
    for key in answer:
        if maxx<answer[key]:
            maxx = answer[key]
    print(maxx)

            
    
    
    
    return maxx
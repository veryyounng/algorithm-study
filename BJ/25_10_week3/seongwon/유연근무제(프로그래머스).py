def solution(schedules, timelogs, startday):
    startday = startday-1
    days = ['월','화','수','목','금','토','일']
    arr = []
    answer=0
    for i in range(len(timelogs)):
        cnt = 0
        for j in range(len(timelogs[i])):
            if (j+startday)%7!=5 and (j+startday)%7!=6:
                   
                # 시간계산해서 cnt+=1
                hour = schedules[i] // 100
                minute = schedules[i] % 100 + 10
                if minute >= 60:
                    hour += 1
                    minute -= 60
                limit_time = hour * 100 + minute
                if timelogs[i][j] <= limit_time:
                    cnt += 1
        arr.append(cnt)
    
    for a in arr:
        if a==5:
            answer+=1
    return answer
def solution(arr):
    answer = []
    for a in arr:
        if not answer:
            answer.append(a)
        elif answer[-1] is not a:
            answer.append(a)
            
    return answer
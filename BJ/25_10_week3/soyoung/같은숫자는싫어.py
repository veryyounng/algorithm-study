def solution(arr):
    answer = []
    answer.append(arr[0])
    for c in arr:
        if len(answer) > 0 and not answer[-1] == c:
            answer.append(c)
    return answer
    print(answer)
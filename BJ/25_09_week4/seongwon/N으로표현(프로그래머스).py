def solution(N, number):
    if N == number:
        return 1
    
    dp = [set() for _ in range(9)]  # N을 i번 쓴 경우 만들 수 있는 숫자 집합
    
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))  # NNN... 같은 숫자 추가
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i-j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)
        if number in dp[i]:
            return i
    
    return -1

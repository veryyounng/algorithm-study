# 이 문제는 여기가서 풀면 댐!
# https://school.programmers.co.kr/learn/courses/30/lessons/60057
import sys
sys.stdin = open('input.txt', 'r')
s = input()
answer = len(s)
for step in range(1, len(s)//2+1):
    compressed = ""
    prev = s[0:step]
    count = 1
    for j in range(step, len(s),step):
        if prev == s[j:j+step]:
            count += 1
        else:
            if count >= 2:
                compressed += str(count) + prev
            else:
                compressed += prev
            prev = s[j:j+step]
            count = 1
    compressed += str(count) + prev if count >= 2 else prev
    answer = min(answer, len(compressed))
print(answer)
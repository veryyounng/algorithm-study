import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
strarr = set()

for _ in range(n):
    strarr.add(input().strip())  

# 정렬: 길이 → 사전순
sorted_words = sorted(strarr, key=lambda x: (len(x), x))
for word in sorted_words:
    print(word)
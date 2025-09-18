from collections import deque

t = int(input())
result = []

for _ in range(t):
    n, m = map(int,input().split())

    queue = deque(map(int, input().split()))
    count = 0

    while queue:
        max_num = max(queue)
        front = queue.popleft()

        if front == max_num:
            count += 1
            if m == 0:
                result.append(count)
                break
            else:
                m -= 1
        
        else:
            if m == 0:
                queue.append(front)
                m = len(queue)-1
            else:
                queue.append(front)
                m -= 1

for i in result:
    print(i)
        


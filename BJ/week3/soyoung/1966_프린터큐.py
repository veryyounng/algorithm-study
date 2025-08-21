from collections import deque
result = []

t = int(input())
count = 0
for _ in range(t):
    n, m = map(int, input().split())
    
    queue = deque(map(int, input().split()))
    count = 0
    
    while queue:
        
        max_num = max(queue)
        current = queue.popleft()
        
        if current == max_num:
            count += 1
            if m == 0:
                result.append(count)
                break
            else:
                m -= 1
        else:
            queue.append(current)
            if m == 0:
                m = len(queue)-1
            else:
                m -= 1
                
for i in result:
    print(i)
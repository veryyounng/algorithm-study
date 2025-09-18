import sys
sys.stdin = open('input.txt', 'r')
n = int(input())
arr = []
for i in range(1,n+1):
    arr.append(i)

check = list(map(int,input().split()))

for i in range(n):
    
    #왼쪽에 큰거 개수 세기
    cnt = 0 
    tmp = arr[i]
    for j in range(i):
        if tmp<arr[j]:
            cnt+=1
    
    right = check[i]-cnt
    
    if right>0:
        for j in range(i+1,n):
            if arr[j]>arr[i]:
                right -= 1
            if right==0:
                arr[i],arr[j]=arr[j],arr[i]
    else:
        for j in range(0,i):
            if arr[j]>arr[i]:
                right += 1
            if right==0:
                arr[i],arr[j]=arr[i],arr[j]
print(arr)
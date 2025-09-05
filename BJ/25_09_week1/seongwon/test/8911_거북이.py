import sys
sys.stdin = open('input.txt', 'r')
testcase = int(input())
for _ in range(testcase):
    orderinput = input()
    point = [0,0]
    # 북->동->서->남
    direction = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    check = []
    for order in orderinput:
        if order=='F':
            point[0]=point[0]+dx[direction]
            point[1]=point[1]+dy[direction]
        elif order =='B':
            point[0]=point[0]-dx[direction]
            point[1]=point[1]-dy[direction]
        elif order == 'L':
            direction = (direction - 1) % 4
        elif order == 'R':
            direction = (direction + 1) % 4
        # 움직일때마다 좌표넣기
        check.append((point[0],point[1]))


    #y의 최대값 2 최소값 0
    #x의 최대값 1 최소값 -1 
    xmin = 0
    xmax = 0
    ymin = 0
    ymax = 0
    area = 0
    for ch in check:
        if ch[0] < xmin:
            xmin = ch[0]
        if ch[0] > xmax:
            xmax = ch[0]
        if ch[1] < ymin:
            ymin = ch[1]
        if ch[1] > ymax:
            ymax = ch[1]

    area = (xmax-xmin)*(ymax-ymin)
    print(area)
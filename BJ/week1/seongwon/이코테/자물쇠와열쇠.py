key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	

def degree90(matrix):
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n-i-1]=matrix[i][j]
    return rotated



def check(new_lock,lock_len):
    for i in range(lock_len,lock_len*2):
        for j in range(lock_len,lock_len*2):
            if new_lock[i][j]!=1:
                return False
    return True


def solution(key,lock):
    lock_len = len(lock)
    key_len = len(key)
    new_lock = [[0] * (lock_len * 3) for _ in range(lock_len * 3)]

    #확장
    for i in range(lock_len):
        for j in range(lock_len):
            new_lock[i+lock_len][j+lock_len]=lock[i][j]

    #4번 회전하면서 감시 
    for _ in range(4):
        key = degree90(key)
        for x in range(1, lock_len*2):
            for y in range(1, lock_len*2):

                #key 더하기
                for i in range(key_len):
                    for j in range(key_len):
                        new_lock[x+i][y+j]+=key[i][j]
                if check(new_lock,lock_len):
                    return True
                
                for i in range(key_len):
                    for j in range(key_len):
                        new_lock[x+i][y+j]-=key[i][j]

    return False
print(solution(key,lock))
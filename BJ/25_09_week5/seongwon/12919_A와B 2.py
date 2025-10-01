import sys
sys.stdin = open('input.txt', 'r')

s = input()
t = input()


# A를 추가 
# B를 추가 후 뒤집기 
#
# def dfs(str):
#     if str==t:
#         print('1')
#         sys.exit()
#     if len(str)==0:
#         return
#     if str[-1]=='A':
#         dfs(str[:-1])
#     if str[0]=='B':
#         dfs(str[1:][::-1])
        
dfs(t)
print(0)

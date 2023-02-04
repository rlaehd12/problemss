import sys
sys.stdin = open('input10157.txt')
sys.setrecursionlimit(10**6)
###대체 값을 뭘 줬는지 재귀로 못품

def check(row, col, cnt, start_lst, final): # 한바퀴 돌기
    # col > row -1 > col -1> row -2> col -2> row -3
    for r in range(start_lst[1], col + start_lst[1]): # 1 col번
        if cnt == final:
            return start_lst
        cnt += 1
        start_lst = [start_lst[0], r]
        #print(start_lst, end= ' ')
    for c in range(start_lst[0] + 1, row + start_lst[0]): # 2 row -1 번
        if cnt == final:
            return start_lst
        cnt += 1
        start_lst = [c, start_lst[1]]
        #print(start_lst, end= ' ')
    # print('b')
    for r in range(start_lst[1] - 1, start_lst[1] - col, -1): # 3 col - 1번
        if cnt == final:
            return start_lst
        cnt += 1
        start_lst = [start_lst[0], r]
        #print(start_lst, end= ' ')
    for c in range(start_lst[0] - 1, start_lst[1], -1): # 4 row - 2번
        if cnt == final:
            return start_lst
        cnt += 1
        start_lst = [c, start_lst[1]]
        #print(start_lst, end= ' ')
    #print('a', end= '    ')
    return check(row - 2, col - 2, cnt, [start_lst[0], start_lst[1] + 1], final)
    
    

for i in range(3):
    row, col = map(int, input().split())
    n = int(input())
    count = 0

    if row * col < n:
        print('0')
    else:
        a = check(row, col, count, [1,1], n)
        print(a[0], a[1])

# #######답지 본거#########################
# m,n = map(int,input().split())
# k = int(input())
# if k > m*n: # 배열의 범위를 벗어남
#     print(0)
#     sys.exit()
    
# board = [[0]*m for _ in range(n)]
# board[0][0] = 1
# move = [(1,0),(0,1),(-1,0),(0,-1)]
# cur_dir = 0
# x,y = (0,0)
# for i in range(2,k+1):
#     while True:
#         a,b = move[cur_dir]
#         dx = x+a; dy = y+b
#         #print(x, y)
#         if n>dx>=0 and m>dy>=0 and board[dx][dy] == 0:
#             board[dx][dy] = i
#             x=dx; y=dy # 현재 위치 갱신
#             break
#         else:
#             cur_dir = (cur_dir+1)%4 # 방향전환
# print(y+1,x+1)
    
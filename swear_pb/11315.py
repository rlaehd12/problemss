import sys
sys.stdin = open("11315.txt")


# def chk():
#     for i in range(1,n+1):  # i,j 전부 돌면서
#         for j in range(1,n+1):
#             if lst[i][j] == 'o':  # 돌 발견하면 4방향에 대해 검사
#                 for k in range(4):
#                     for mul in range(5):
#                         ni,nj = i+di[k]*mul, j+dj[k]*mul
#                         if lst[ni][nj] != 'o':
#                             break
#                     else:
#                         return True
#     return False
#     #                 ci = i
#     #                 cj = j
#     #                 cnt = 0
#     #                 while lst[ci][cj] == 'o':
#     #                     ni = ci+di[k]
#     #                     nj = cj+dj[k]
#     #                     ci = ni
#     #                     cj = nj
#     #                     cnt += 1
#     #                 if cnt >=5:
#     #                     return True
#     # return False

# t = int(input())

# di = (0,1,1,1)  # 우, 우하, 하, 좌하
# dj = (1,1,0,-1)

# for tc in range(1,t+1):
#     n = int(input())
#     lst = ['.'*(n+2)]+['.'+input()+'.' for _ in range(n)]+['.'*(n+2)]  # padding
    
#     for i in lst:
#         print(i)
#     print()

#     if chk():
#         print(f'#{tc} YES')
#     else:
#         print(f'#{tc} NO')

###
def bfs(x, y):
    global result
    q = [(x, y)]

    while q:
        ci, cj = q.pop(0)
        for i in range(8):
            cnt = 0
            for j in range(1, 5):
                ni = ci + di[i] * j
                nj = cj + dj[i] * j
                # 연속된 돌이 없으면 빠져나오게
                if 0 <= ni < N and 0 <= nj < N:
                    if board[ni][nj] != 'o':
                        break
                # 연속된 돌이 있으면
                    elif board[ni][nj] == 'o':
                        cnt += 1
                        if cnt >= 4:
                            return 'YES'
    return 'NO'


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = 0
    board = [list(input()) for _ in range(N)]
    # 좌상대각선, 위, 우상대각선, 좌, 우, 좌하대각선, 하, 우하대각선
    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]
    result = 'NO'
    switch = True

    for i in range(len(board)):
        if not switch:
            break
        for j in range(len(board)):
            if not switch:
                break
            if board[i][j] == 'o':
                result = bfs(i, j)
                if result == 'YES':
                    switch = False

    print(f'#{tc}', result)
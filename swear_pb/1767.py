import sys
sys.stdin = open("1767.txt")

# di = (1,-1,0,0)  # 하상우좌
# dj = (0,0,1,-1)

def chk(idx, curans, cango):
    # if curans >= ans_lst[0]:  # 답보다 크면 검사 안해도 됨
    #     return

    if idx == len(core_lst):  # base case
        if cango > ans_lst[1]:
            ans_lst[0] = curans
            ans_lst[1] = cango
        elif cango >= ans_lst[1] and curans < ans_lst[0]:
            ans_lst[0] = curans
            ans_lst[1] = cango
        return

    if core_lst[idx][0] == 0 or core_lst[idx][0] == N-1 or\
        core_lst[idx][1] == 0 or core_lst[idx][1] == N-1:  # 벽이면 끝냄
        chk(idx+1, curans, cango+1)
    else:
        ci = core_lst[idx][0]
        cj = core_lst[idx][1]
        notgo = 0
        for k in range(4):
            mul = 1
            end = True
            while end:  # 검사하면서 2로 채워넣기
                ni = ci+di[k]*mul
                nj = cj+dj[k]*mul
                if (ni==0 or ni==N-1 or nj==0 or nj==N-1) and processor[ni][nj] == 0:
                    end = False
                    continue
                elif processor[ni][nj] != 0:
                    notgo += 1
                    break
                processor[ni][nj] = 2
                mul += 1

            else:  # 제대로 돌면 다음 코어 검사
                chk(idx+1, curans+mul, cango+1)
            if notgo>=4:
                chk(idx+1, curans, cango)

            for i in range(1,mul):  # 리스트 쓴거 원상복귀
                ni = ci+di[k]*i
                nj = cj+dj[k]*i
                processor[ni][nj] = 0
            



# t = int(input())
# for tc in range(1,t+1):
#     N = int(input())
#     processor = [list(map(int, input().split())) for _ in range(N)]
#     core_lst = []  # 코어 위치 저장
#     ans_lst = [99999999, 0]  # 정답 저장
#     for i in range(N):
#         for j in range(N):
#             if processor[i][j] == 1:
#                 core_lst.append((i,j))
    
#     if core_lst:
#         chk(0, 0, 0)

#     print(f'#{tc} {ans_lst[0]}')
#     # for i in processor:
#     #     print(i)


def line(alpha, beta, ddx, ddy):
    while -1<alpha<n-1 and -1<beta<n-1:
        alpha += ddx
        beta += ddy
        if check[alpha][beta]:
            return 0
    return 1

def checking(core_idx):
    global cnt
    if not core_idx:
        # print('check',check)
        return
    a, b = core_idx.pop()
    while core_idx and not a or not b:
        a, b = core_idx.pop()
    dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for ids, c in enumerate(dxdy):
        dx, dy = c
        if line(a, b, dx, dy):
            # print(a, b, dx, dy)
            # print(check)
            if ids == 2:
                cnt += b+1
                for i in range(1,n-b):
                    check[a][b+i] = True
                checking(core_idx)
                for j in range(1, n-b):
                    check[a][b+j] = False
            elif ids == 3:
                cnt += n-b-1
                for i in range(1, b):
                    check[a][b - i] = True
                checking(core_idx)
                for j in range(1, b):
                    check[a][b - j] = False
            elif ids == 1:
                cnt += a+1
                for i in range(1, a):
                    check[a-i][b] = True
                checking(core_idx)
                for j in range(1, a):
                    check[a-j][b] = False
            else:
                cnt += n-a-1
                # print('cntcntcntcntcntcntcntcnt', cnt)
                for i in range(1, n-a):
                    check[a+i][b] = True
                checking(core_idx)
                for j in range(1, n-a):
                    check[a+j][b] = False


T = int(input().rstrip())
for tt in range(1, T+1):
    n = int(input().rstrip())
    matrix = [list(map(int, input().rstrip().split())) for _ in range(n)]
    check = [[False] * (n) for _ in range(n)]
    core = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                core.append([i,j])
                check[i][j] = True
    # print(core)

    cnt = 0
    checking(core)
    print(cnt)
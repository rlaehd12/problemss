from collections import deque
# 나눠지는건 lst(r,c)//5

R, C, T = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(R)]
dr = ((1,0),(-1,0),(0,1),(0,-1))


def diffusion():
    cur = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if lst[i][j] >=5:
                cnt = 0
                for k in range(4):
                    ni = i+dr[k][0]
                    nj = j+dr[k][1]
                    if 0<=ni<R and 0<=nj<C and lst[ni][nj]!=-1:  # 범위 내, 공기청정기 아님
                        cur[ni][nj] += lst[i][j]//5
                        cnt += 1
                lst[i][j] -= cnt*(lst[i][j]//5)
    # 확산된거 더해서 리스트에 더하기
    for i in range(R):
        for j in range(C):
            if lst[i][j] == -1:
                continue
            lst[i][j] += cur[i][j]


# 청정기 위치 찾기
for i in range(R):
    if lst[i][0] == -1:
        conditioner = i
        break

for n in range(T):
    diffusion()
    # 위쪽
    ci= conditioner
    cj = 0
    before = 0
    for di,dj in ((0,1),(-1,0),(0,-1),(1,0)):
        ci += di
        cj += dj
        while 0<=ci<R and 0<=cj<C and ((ci,cj) != (conditioner,0)):
            tmp = lst[ci][cj]
            lst[ci][cj] = before
            before = tmp
            ci += di
            cj += dj
        else:
            ci -= di
            cj -= dj
    # 아래쪽
    ci= conditioner+1
    cj = 0
    before = 0
    for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
        ci += di
        cj += dj
        while 0<=ci<R and 0<=cj<C and ((ci,cj) != (conditioner+1,0)):
            tmp = lst[ci][cj]
            lst[ci][cj] = before
            before = tmp
            ci += di
            cj += dj
        else:
            ci -= di
            cj -= dj
            
    # for i in lst:
    #     print(i)
    # print()

cnt = 0
for i in range(R):
    for j in range(C):
        cnt += lst[i][j]
print(cnt+2)
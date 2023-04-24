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
                    if 0<=ni<R and 0<=nj<C and lst[ni][nj]!=-1:
                        cur[ni][nj] += lst[i][j]//5
                        cnt += 1
                lst[i][j] -= cnt*(lst[i][j]//5)
    # 확산된거 더해서 리스트에 더하기
    for i in range(R):
        for j in range(C):
            if lst[i][j] == -1:
                continue
            lst[i][j] += cur[i][j]
    


conditiner = 0  # 무조건 0번째열, 값/값+1
for i in range(R):
    if lst[i][0] == -1:
        conditiner = i
        break
# 위쪽 아래쪽=========
lst1 = []  # 뒤에서부터 덮어씌우면 됨
lst2 = []
#====================
diffusion()
for i in lst:
    print(i)
# 위쪽
ci= conditiner
cj = 0
for di,dj in ((0,1),(-1,0),(0,-1),(1,0)):
    ci += di
    cj += dj
    while 0<=ci<R and 0<=cj<C and ((ci,cj) != (conditiner,0)):
        lst1.append((ci,cj,lst[ci][cj]))
        ci += di
        cj += dj
    else:
        ci -= di
        cj -= dj
# 아래쪽
ci= conditiner+1
cj = 0
for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
    ci += di
    cj += dj
    while 0<=ci<R and 0<=cj<C and ((ci,cj) != (conditiner+1,0)):
        lst2.append((ci,cj,lst[ci][cj]))
        ci += di
        cj += dj
    else:
        ci -= di
        cj -= dj

for i in range(T-1):
    diffusion()
    # 공기청정기 순환
    for i in range(len(lst1),0,-1):
        lst1[i][2] = lst1[i-1][2]
    lst1[0][2] = 0
    for i in range(len(lst2),0,-1):
        lst2[i][2] = lst2[i-1][2]
    lst2[0][2] = 0
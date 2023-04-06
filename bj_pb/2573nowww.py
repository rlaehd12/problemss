N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

di = (1,-1,0,0)
dj = (0,0,1,-1)
while True:
    melt_lst = []
    for i in range(N):
        for j in range(M):
            if lst[i][j] != 0:
                cnt = 0
                for k in range(4):
                    ni = i+di[k]
                    nj = j+dj[k]
                    if 0<=ni<N and 0<=nj<M and lst[ni][nj] == 0:
                        cnt += 1
                melt_lst.append((i, j, cnt))
    
    for i,j,cnt in melt_lst:
        lst[i][j] = 0 if (lst[i][j] - cnt) < 0 else lst[i][j]-cnt
    for i in lst:
        print(i)
    print()

    if not melt_lst:
        break
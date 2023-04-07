from collections import deque

di = (1,-1,0,0)
dj = (0,0,1,-1)

def bfs(i, j):
    cnt = 1
    visited = [[0]*M for _ in range(N)]
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    while q:
        ci, cj = q.popleft()
        for k in range(4):
            ni = ci+di[k]
            nj = cj+dj[k]
            if lst[ni][nj] !=0 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
                cnt += 1
    return cnt



N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

ans = 0
while True:
    ans += 1
    flag = 0
    melt_lst = []
    for i in range(N):
        for j in range(M):
            if lst[i][j] != 0:
                cnt = 0
                for k in range(4):
                    ni = i+di[k]
                    nj = j+dj[k]
                    if lst[ni][nj] == 0:
                        cnt += 1
                melt_lst.append((i, j, cnt))
    
    # for i in lst:
    #     print(i)
    # print(len(melt_lst), bfs(melt_lst[0][0], melt_lst[0][1]))
    # print()

    if not melt_lst:
        print(0)
        break

    
    # 여기서 bfs
    if len(melt_lst) != bfs(melt_lst[0][0], melt_lst[0][1]):
        print(ans-1)
        break
    #
    
    for i,j,cnt in melt_lst:
        if (lst[i][j] - cnt) <= 0:  # 0이 하나라도 만들어지면
            lst[i][j] = 0
            flag = 1
        else: 
            lst[i][j] -= cnt

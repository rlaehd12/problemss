import sys
sys.stdin = open("2117.txt")


from collections import deque

t = int(input())

di = (1,-1,0,0)
dj = (0,0,1,-1)

def bfs(k, i, j):
    lst = [[0] * n for _ in range(n)]
    cnt = 0  # 집 개수
    queue = deque()
    queue.append((i,j))
    lst[i][j] = 1

    if zido[i][j] == 1:
        cnt += 1
    while queue:
        cur = queue.popleft()
        for direction in range(4):
            ni = cur[0] + di[direction]
            nj = cur[1] + dj[direction]
            if 0<=ni<n and 0<=nj<n and lst[ni][nj] == 0:
                lst[ni][nj] = lst[cur[0]][cur[1]] + 1

                if lst[ni][nj] > k:  # 현재 거리가 k보다 커지면 종료
                    return cnt
                
                queue.append((ni, nj))
                if zido[ni][nj] == 1:
                    cnt += 1
    return cnt


for tc in range(1,t+1):
    n, m = map(int, input().split())

    zido = []
    homes = 0
    k = 1

    for _ in range(n):
        zido.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(n):
            if zido[i][j] == 1:
                homes += 1

    big = 0
    cur_cost = (k**2) + ((k-1)**2)
    while homes*m > cur_cost:
        cur_big = 0
        for i in range(n):  # 전부탐색
            for j in range(n):
                cur = bfs(k, i, j)
                if cur * m < cur_cost:
                    pass
                else:
                    if cur_big < cur:
                        cur_big = cur
        
        if big < cur_big:
            big = cur_big

        
        k += 1
        cur_cost = (k**2) + ((k-1)**2)
    
    print(f'#{tc} {big}')
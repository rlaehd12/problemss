import sys
sys.stdin = open("2117.txt")

### 다른 풀이/ 인덱스 활용/ bfs
cost = [((k*k)+(k-1)*(k-1)) for k in range(40)]

def solve_loop():
    mx = 0
    for si in range(n):
        for sj in range(n):
            for k in range(1, 2*n):
                cnt = 0
                for i in range(si-k+1, si+k):
                    t = abs(si-i)
                    for j in range(sj-k+1+t, sj+k-t):
                        if 0<=i<n and 0<=j<n:
                            cnt += arr[i][j]
                # 운영비보다 수익이 같거나 큰 경우 갱신
                if cost[k] <= cnt * m:
                    mx = max(mx, cnt)
    return mx

def bfs(si, sj):
    q = []
    v = [[0]*n for _ in range(n)]
    old = 0
    mx = 0

    q.append((si, sj))
    v[si][sj] = 1
    cnt = arr[si][sj]  # 시작좌표가 집이면 1 아니면 0
    while q:
        ci, cj = q.pop(0)
        if old != v[ci][cj]:  # k값이 달라진 경우(범위가 커진 경우)
            old = v[ci][cj]
            if cost[v[ci][cj]] <= cnt*m:
                mx = max(mx, cnt)


        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<n and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj]+1
                cnt += arr[ni][nj]
    return mx

def solve_bfs():
    mx = 0
    for si in range(n):
        for sj in range(n):
            mx = max(mx, bfs(si, sj))
    return mx

'''
다른 방법
범위 기준 표시후 확산 , 집 기준 접근
[1] 집 좌표 저장
[2] 각 기준 위치에서 거리 표시(누적) 카운팅 함수처럼
'''

def solve_idea():
    mx = 0
    home = []
    for si in range(n):
        for sj in range(n): # [1] 집의 모든 위치를 저장
            if arr[si][sj]==1:
                home.append((si,sj))
 
    # [2] 각 기준위치에서 거리별 집의 개수 누적하기
    for si in range(n):
        for sj in range(n): #
            dist = [0]*40
            # 거리별 집위치를 누적
            for ti,tj in home:
                t = abs(si-ti)+abs(sj-tj)+1
                dist[t]+=1
 
            for k in range(1, 40):
                dist[k]+=dist[k-1]
                if cost[k]<=dist[k]*m:
                    mx = max(mx, dist[k])
    return mx

t = int(input())
for tc in range(1,t+1):
    n,m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # ans = solve_loop()
    ans = solve_idea()
    # ans = solve_bfs()
    print(f'#{tc} {ans}')
###

# from collections import deque

# t = int(input())

# di = (1,-1,0,0)
# dj = (0,0,1,-1)

# def bfs(k, i, j):
#     lst = [[0] * n for _ in range(n)]
#     cnt = 0  # 집 개수
#     queue = deque()
#     queue.append((i,j))
#     lst[i][j] = 1

#     if zido[i][j] == 1:
#         cnt += 1
#     while queue:
#         cur = queue.popleft()
#         for direction in range(4):
#             ni = cur[0] + di[direction]
#             nj = cur[1] + dj[direction]
#             if 0<=ni<n and 0<=nj<n and lst[ni][nj] == 0:
#                 lst[ni][nj] = lst[cur[0]][cur[1]] + 1

#                 if lst[ni][nj] > k:  # 현재 거리가 k보다 커지면 종료
#                     return cnt
                
#                 queue.append((ni, nj))
#                 if zido[ni][nj] == 1:
#                     cnt += 1
#     return cnt


# for tc in range(1,t+1):
#     n, m = map(int, input().split())

#     zido = []
#     homes = 0
#     k = 1

#     for _ in range(n):
#         zido.append(list(map(int, input().split())))

#     for i in range(n):
#         for j in range(n):
#             if zido[i][j] == 1:
#                 homes += 1

#     big = 0
#     cur_cost = (k**2) + ((k-1)**2)
#     while homes*m > cur_cost:
#         cur_big = 0
#         for i in range(n):  # 전부탐색
#             for j in range(n):
#                 cur = bfs(k, i, j)
#                 if cur * m < cur_cost:
#                     pass
#                 else:
#                     if cur_big < cur:
#                         cur_big = cur
        
#         if big < cur_big:
#             big = cur_big

        
#         k += 1
#         cur_cost = (k**2) + ((k-1)**2)
    
#     print(f'#{tc} {big}')
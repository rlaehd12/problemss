import sys
sys.stdin = open("17142.txt")
from itertools import combinations
from collections import deque
from copy import deepcopy

di = (1,-1,0,0)
dj = (0,0,1,-1)

def bfs():
    while q:
        cur = q.popleft()
        ci = cur[0]
        cj = cur[1]
        # if visit[ci][cj] > ans[1]:  # backtracking
        #     return 99999

        # 이거 아님
        # 일단 다른곳에 보관하고 크기 순서대로 큐에 삽입
        # cq = []  # 혹시 더 큰거 먼저 확인해서 값이 커지는 경우 대비
        for i in range(4):
            ni = ci+di[i]
            nj = cj+dj[i]
            if 0<=ni<N and 0<=nj<N:
                if visit[ni][nj] == 2:
                    visit[ni][nj] = visit[ci][cj]+1
                    q.append((ni,nj))
                elif visit[ni][nj] == 0:
                    visit[ni][nj] = visit[ci][cj]+1
                    q.append((ni,nj))
    return chk()


def chk():
    big = 0
    for i in range(N):
        for j in range(N):
            c = visit[i][j]
            if c == 0:
                return 99999
            if big < c and ((i,j) not in v_lst):
                big = c
    if big == 0:
        return 99999
    return big



N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

v_lst = []
cnt = [0, 0]  # 바이러스, 벽 개수
for i in range(N):  # 바이러스 위치 찾기
    for j in range(N):
        if lst[i][j] == 2:
            v_lst.append((i,j))
            cnt[0]+=1
        if lst[i][j] == 1:
            cnt[1]+=1
ans = [-1, 99999]  # 출력할거, 체크용 답

if sum(cnt)==N**2:
    print(0)
else:
    for s in combinations(v_lst, M):  # M개만큼 고른거 돌면서
        visit = deepcopy(lst)
        q = deque()
        for i in s:
            visit[i[0]][i[1]] = 3
            q.append(i)
        cur = bfs()
        if ans[1] > cur:
            ans[1] = cur

    if ans[1] == 99999:
        print(ans[0])
    else:
        print(ans[1]-3)
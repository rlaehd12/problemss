import sys
sys.stdin = open("2589.txt")
from collections import deque

di = (1,-1,0,0)
dj = (0,0,1,-1)


def bfs(s):
    cnt = 0
    visit = [[0]*M for _ in range(N)]
    q = deque()
    q.append(s)
    visit[s[0]][s[1]] = 1
    while q:
        c = q.popleft()
        ci = c[0]
        cj = c[1]
        for k in range(4):
            ni = ci+di[k]
            nj = cj+dj[k]
            if 0<=ni<N and 0<=nj<M and lst[ni][nj] == 'L' and visit[ni][nj] == 0:
                q.append((ni,nj))
                visit[ni][nj] = visit[ci][cj]+1
    for i in visit:
        for j in i:
            if cnt < j:
                cnt = j
    return cnt

N, M = map(int, input().split())
lst = [input() for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(M):
        if lst[i][j] == 'L':
            cnt = bfs((i,j))
            if ans < cnt:
                ans = cnt
print(ans-1)
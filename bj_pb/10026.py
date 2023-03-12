import sys
sys.stdin = open("10026.txt")

# RG는 한꺼번에 탐색, 나중에 만들어진걸로 다시 탐색
from collections import deque

di = (1,-1,0,0)
dj = (0,0,1,-1)

def bfs(s, lst, visit):
    q = deque()
    q.append(s)
    while q:
        c = q.popleft()
        ci = c[0]
        cj = c[1]
        for k in range(4):
            ni = ci+di[k]
            nj = cj+dj[k]
            if 0<=ni<N and 0<=nj<N and visit[ni][nj] == 0:
                if lst[ci][cj]=='B' and (lst[ni][nj] == lst[ci][cj]):
                    q.append((ni,nj))
                    visit[ni][nj] = 'B'
                elif lst[ni][nj] == lst[ci][cj]:
                    q.append((ni,nj))
                    visit[ni][nj] = 'R'



ans = [0,0]  # 일반, 적녹
N = int(input())
lst = [input() for _ in range(N)]
visit = [[0]*N for _ in range(N)]
vg = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            if lst[i][j] == 'B':
                visit[i][j] = 'B'
            else:
                visit[i][j] = 'R'
            ans[0] += 1
            bfs((i,j), lst, visit)
for i in range(N):
    for j in range(N):
        if vg[i][j] == 0:
            if lst[i][j] == 'B':
                vg[i][j] = 'B'
            else:
                vg[i][j] = 'R'
            ans[1] += 1
            bfs((i,j), visit, vg)
print(ans[0], ans[1])

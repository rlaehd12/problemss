from collections import deque
import sys
sys.stdin = open("7569.txt")

def chk():
    start = []
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if lst[h][i][j] == 1:
                    start.append((h,i,j))
    return start

def bfs():
    q = deque()
    # visited = [[[0]*M for _ in range(N)] for _ in range(H)]
    for i in s_lst:
        q.append(i)
        # visited[i[0]][i[1]][i[2]] = 1
    while q:
        s = q.popleft()
        ch, ci, cj = s[0], s[1], s[2]
        for k in range(6):
            nh = ch+dh[k]
            ni = ci+di[k]
            nj = cj+dj[k]
            if 0<=nh<H and\
                0<=ni<N and 0<=nj<M:  # 범위 안에 있스면
                if lst[nh][ni][nj] == 0 and lst[nh][ni][nj] != -1:
                    lst[nh][ni][nj] = lst[ch][ci][cj]+1
                    q.append((nh,ni,nj))
    return answer(lst)

def answer(lst):
    ans = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                c = lst[h][i][j]
                if c == 0:
                    return -1
                if ans < c:
                    ans = c
    return ans-1
    


di = (1,-1,0,0,0,0)  # 하 상 우 좌 아래 위
dj = (0,0,1,-1,0,0)
dh = (0,0,0,0,1,-1)

M, N, H = map(int, input().split())
# h, i, j 순서로 탐색할거임 - 층,행,열 순
lst = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]  # 3차원 리스트

s_lst = chk()
print(bfs())
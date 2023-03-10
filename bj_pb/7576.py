from collections import deque
import sys
sys.stdin = open("7576.txt")

# def val_answer(n, m):
#     tmp = 0
#     for lst in tomato:
#         if 0 in lst:
#             tmp += 1
#     if not tmp:
#         return tmp
#     mx_value = 0
#     for x in range(n):
#         for y in range(m):
#             if not mature[x][y]:
#                 if (x, y) in start or (x, y) in box_point:
#                     continue
#                 else:
#                     return -1
#             if mature[x][y] >= mx_value:
#                 mx_value = mature[x][y]
#     return mx_value


# M, N = map(int, input().split())  # N: 행, M: 열
# tomato = [list(map(int, input().split())) for _ in range(N)]
# mature = [[0] * M for _ in range(N)]
# queue = []
# start = []
# box_point = []
# for i in range(N):
#     for j in range(M):
#         if tomato[i][j] == 1:
#             queue.append((i, j))
#             start.append((i, j))
#         elif tomato[i][j] == -1:
#             box_point.append((i, j))
# di = [0, 0, 1, -1]
# dj = [1, -1, 0, 0]
# # bfs
# while queue:
#     cur = queue.pop(0)
#     for idx in range(4):
#         ni = cur[0] + di[idx]
#         nj = cur[1] + dj[idx]
#         if 0 <= ni < N and 0 <= nj < M and not mature[ni][nj] and tomato[ni][nj] != -1 \
#                 and not tomato[ni][nj]:
#             queue.append((ni, nj))
#             mature[ni][nj] = mature[cur[0]][cur[1]] + 1
# print(val_answer(N, M))

def chk():
    start = []
    for i in range(N):
        for j in range(M):
            print(i,j)
            if lst[i][j] == 1:
                start.append((i,j))
    return start

def bfs():
    q = deque()
    # visited = [[[0]*M for _ in range(N)] for _ in range(H)]
    for i in s_lst:
        q.append(i)
        # visited[i[0]][i[1]][i[2]] = 1
    while q:
        s = q.popleft()
        ci, cj = s[0], s[1]
        for k in range(4):
            ni = ci+di[k]
            nj = cj+dj[k]
            if 0<=ni<N and 0<=nj<M:  # 범위 안에 있스면
                if lst[ni][nj] == 0 and lst[ni][nj] != -1:
                    lst[ni][nj] = lst[ci][cj]+1
                    q.append((ni,nj))
    return answer(lst)

def answer(lst):
    ans = 0
    for i in range(N):
        for j in range(M):
            c = lst[i][j]
            if c == 0:
                return -1
            if ans < c:
                ans = c
    return ans-1
    


di = (1,-1,0,0)  # 하 상 우 좌 아래 위
dj = (0,0,1,-1)

M, N = map(int, input().split())
# i, j 순서로 탐색할거임 -행,열 순
lst = [list(map(int, input().split())) for _ in range(N)]  # 2차원 리스트
s_lst = chk()
print(bfs())
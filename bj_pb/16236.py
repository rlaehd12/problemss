from collections import deque


di = (-1,0,0,1)
dj = (0,-1,1,0)
# 이거 돌리고 마지막에 추가하는 방향으로 하자

def bfs():
    global ans
    visited = [[0]*N for _ in range(N)]
    q = deque()
    q.append((shark[0], shark[1]))
    visited[shark[0]][shark[1]] = 1
    nxt_lst = [9999, 9999, 9999]
    while q:
        ci, cj = q.popleft()
        if nxt_lst[2] <= visited[ci][cj]:
            break
        for k in range(4):
            ni = ci+di[k]
            nj = cj+dj[k]
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
                if sea[ni][nj] == 0 or sea[ni][nj] == shark[2]:  # 이동
                    # print(ni, nj)
                    visited[ni][nj] = visited[ci][cj] + 1
                    q.append((ni,nj))
                elif sea[ni][nj] < shark[2]:  # 먹는지 아닌지 확인(위치)
                    nxt_lst[2] = visited[ci][cj] + 1
                    if nxt_lst[0] > ni:
                        nxt_lst[0] = ni
                        nxt_lst[1] = nj
                    elif nxt_lst[0] == ni and nxt_lst[1] > nj:
                        nxt_lst[0] = ni
                        nxt_lst[1] = nj
                    visited[ni][nj] = visited[ci][cj] + 1
    if nxt_lst[0] != 9999:
        shark[3] += 1
        sea[nxt_lst[0]][nxt_lst[1]] = 0
        shark[0] = nxt_lst[0]
        shark[1] = nxt_lst[1]
        ans += (nxt_lst[2]-1)
        # print(nxt_lst, shark)
        return True
    return False


N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
# fish_lst = []
shark = [0, 0, 2, 0]  # i/ j/ size/ eat count/
# 먹을때마다 bfs 돌리기
ans = 0
fish_cnt = 0
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            shark[0] = i
            shark[1] = j
            sea[i][j] = 0
        elif sea[i][j] != 0:
            fish_cnt += 1

while fish_cnt:
    a = bfs()
    if shark[2] == shark[3]:
        shark[2] += 1
        shark[3] = 0
    fish_cnt-=1
    if not a:
        break
    # print(ans)

print(ans)
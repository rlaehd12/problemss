import sys
sys.stdin = open("1861.txt")

t = int(input())


def bfs(si, sj):
    q = [] # [0] 생성
    alst = [] 

    q.append((si, sj))  # [1] 초기데이터 삽입
    v[si][sj] = 1
    alst.append(arr[si][sj])

    while q:
        ci, cj = q.pop()

        # 4방향, 미방문, 조건맞으면(1차이)
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<n and abs(arr[ci][cj] - arr[ni][nj]) == 1:
            
                q.append((ni, nj))
                v[ni][nj] = 1
                alst.append(arr[ni][nj])

        return min(alst), len(alst)

for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    v = [[0]*n for _ in range(n)]
    ans, cnt = n*n, 0
    for si in range(n):
        for sj in range(n):
            if v[si][sj] == 0:
                t, tcnt = bfs(si, sj)
                if cnt < tcnt or (cnt == tcnt and ans > t):
                    ans, cnt = t, tcnt

    print(f'#{tc} {ans} {cnt}')

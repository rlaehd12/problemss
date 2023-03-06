import sys
sys.stdin = open("9490.txt")

di = (1, -1, 0, 0)  # 하상우좌
dj = (0, 0, 1, -1)

t = int(input())

for tc in range(1, t+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N):
        for j in range(M):
            # print(arr[i][j], end='')
            cnt = 0
            curN = arr[i][j]
            ci = i
            cj = j
            for d in range(4):
                for k in range(1, 1 + curN):
                    ni = ci + di[d] * k
                    nj = cj + dj[d] * k
                    if 0 <= ni < N and 0 <= nj < M:
                        cnt += arr[ni][nj]
            cnt += curN
            if maxV < cnt:
                maxV = cnt

    print(f'{tc} {maxV}')

a = [1,2,3]
try:  # 오류날때까지는 실행 함, 저장도 다 됨
    a[0] = 5
    a[1] = 5
    a[2] = 5
    a[3] = 5
except:
    pass

print(a)
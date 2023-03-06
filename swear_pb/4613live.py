import sys
sys.stdin = open("4613.txt")

t = int(input())

for tc in range(1, t+1):

    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]

    # for i in flag:
    #     print(i)

    minV = 2500
    #    W        B          R
    # (0 ~ i), (i+1 ~ j), (j+1 ~ N)
    for i in range(N-2):
        for j in range(i+1, N-1):
            cnt = 0

            for p in range(0, i+1):  # W 영역
                for q in range(M):
                    if flag[p][q] != 'W':
                        cnt += 1

            for p in range(i+1, j+1):  # B 영역
                for q in range(M):
                    if flag[p][q] != 'B':
                        cnt += 1

            for p in range(j+1, N):  # R 영역
                for q in range(M):
                    if flag[p][q] != 'R':
                        cnt += 1

            if minV > cnt:
                minV = cnt

    print(f'#{tc} {minV}')

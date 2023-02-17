import sys
sys.stdin = open("230217.txt")

t = int(input())

for tc in range(1,t+1):
    n, m = map(int, input().split())

    lst = [[9] * (m+2)] + [[9] + list(map(int, input().split())) + [9] for _ in range(n)] + [[9] * (m+2)]  # 패딩, 밖은 9로 초기화

    ans = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            cnt = 0
            for di, dj in ((1,0), (1,1), (1,-1), (0,1), (0,-1), (-1,0), (-1,-1), (-1,1)):  # 8방향 확인
                if lst[i][j] > lst[i+di][j+dj]:
                    cnt += 1
            if cnt >= 4:
                ans += 1

    print(f'#{tc} {ans}')
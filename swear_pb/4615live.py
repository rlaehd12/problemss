import sys
sys.stdin = open("4615.txt")

t = int(input())

for tc in range(1,t+1):
    n, M = map(int, input().split())
    # arr 패딩하기
    arr = [[0] * (n+2) for _ in range(n+2)]
    m = n//2
    arr[m][m] = arr[m+1][m+1] = 2
    arr[m+1][m] = arr[m][m+1] = 1


    for _ in range(M):
        si, sj, d = map(int, input().split())
        arr[si][sj] = d
        for di, dj in ((-1,-1), (-1,0), (-1,1), (0,1), (0,-1), (1,0), (1,-1), (1,1)):
            tlst = []
            for multi in range(1, n):
                ni, nj = si + di*multi, sj + dj*multi
                if arr[ni][nj] == 0:
                    break
                elif arr[ni][nj] != d:  # 다른돌인 경우
                    tlst.append((ni, nj))  # 뒤집기 후보들 좌표
                else:  # 같은 돌 만나면 후보에 있는 돌들 뒤집음
                    while tlst:
                        ti, tj = tlst.pop()
                        arr[ti][tj] = d
                    break
    cnt1 = cnt2 = 0
    for i in arr:
        for j in i:
            if j == 1:
                cnt1 += 1
            elif j == 2:
                cnt2 += 1
    
    print(f'#{tc} {cnt1} {cnt2}')
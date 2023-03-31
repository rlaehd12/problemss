def chk(r, c, n):
    cur = lst[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if lst[i][j] != cur:  # 하나라도 다르면 종이 쪼개기
                chk(r, c, n//2)
                chk(r+n//2, c, n//2)
                chk(r, c+n//2, n//2)
                chk(r+n//2, c+n//2, n//2)
                return
    ans[cur] += 1

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
ans = [0,0]
chk(0, 0, N)
for i in ans:
    print(i)

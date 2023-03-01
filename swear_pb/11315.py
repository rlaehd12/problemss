import sys
sys.stdin = open("11315.txt")


def chk():
    for i in range(1,n+1):  # i,j 전부 돌면서
        for j in range(1,n+1):
            if lst[i][j] == 'o':  # 돌 발견하면 4방향에 대해 검사
                for k in range(4):
                    ci = i
                    cj = j
                    cnt = 0
                    while lst[ci][cj] == 'o':
                        ni = ci+di[k]
                        nj = cj+dj[k]
                        ci = ni
                        cj = nj
                        cnt += 1
                    if cnt >=5:
                        return True
    return False

t = int(input())

di = (0,1,1,1)  # 우, 우하, 하, 좌하
dj = (1,1,0,-1)

for tc in range(1,t+1):
    n = int(input())
    lst = ['.'*(n+2) for _ in range(n+2)]  # padding
    for i in range(n):
        lst[i+1] = '.' + input() + '.'
    
    for i in lst:
        print(i)
    print()

    if chk():
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')
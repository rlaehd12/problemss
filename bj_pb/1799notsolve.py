import sys
sys.stdin = open("1799.txt")

def dfs(i, v):
    if v+1 == possible_chess:  # base case
        # print(ans)
        if ans[0] < ans[1]:
            ans[0] = ans[1]
        return
    if check_lst[v+1][0]%2 == 0:
        dfs(i+1, v+1)
        return

    lc = check_lst[v+1][0]
    rc = check_lst[v+1][1]
    if left_check[lc] == 0 and right_check[rc] == 0:
        left_check[lc] = 1
        right_check[rc] = 1
        ans[1] += 1

        dfs(i+1, v+1)

        left_check[lc] = 0
        right_check[rc] = 0
        ans[1] -= 1
        dfs(i+1, v+1)
    else:
        dfs(i+1, v+1)

def dfsr(i, v):
    if v+1 == possible_chess:
        # print(ans, 'aaa')
        if ans[2] < ans[1]:
            ans[2] = ans[1]
        return
    if check_lst[v+1][0]%2 == 1:
        dfsr(i+1, v+1)
        return
    lc = check_lst[v+1][0]
    rc = check_lst[v+1][1]
    if left_check[lc] == 0 and right_check[rc] == 0:
        left_check[lc] = 1
        right_check[rc] = 1
        ans[1] += 1

        dfsr(i+1, v+1)

        left_check[lc] = 0
        right_check[rc] = 0
        ans[1] -= 1
        dfsr(i+1, v+1)
    else:
        dfsr(i+1, v+1)


N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]
check_lst = []
ans = [0, 0, 0]  # global, local, dfsr glb
for i in range(N):
    for j in range(N):
        if lst[i][j] == 1:  # 놓을 수 있는지 확인
            check_lst.append((i+j, i + N-1 - j))
possible_chess = len(check_lst)
check_lst.append((-1,-1))

# print(check_lst)
if possible_chess == N**2:
    print(2*N - 2)
elif possible_chess == 0:
    print(0)
else:
    # 초기화 0번째 미포함
    left_check = [0] * ((2*N)-1)
    right_check = [0] * ((2*N)-1)  # 대각선 방향 체크
    dfs(0, 0)
    dfsr(0, 0)

    # 초기화 0번째 포함, 가능할 때만
    left_check = [0] * ((2*N)-1)
    right_check = [0] * ((2*N)-1)  # 대각선 방향 체크
    ans[1] = 1
    left_check[check_lst[0][0]] = 1
    right_check[check_lst[0][1]] = 1
    if check_lst[0][0]%2 == 0:
        dfsr(0, 0)
    else:
        dfs(0, 0)
    print(ans[0] + ans[2])
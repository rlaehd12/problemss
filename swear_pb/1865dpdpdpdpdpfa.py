import sys
sys.stdin = open("1865.txt")

# def dfs(depth):
#     if depth == N:  # base case
#         if ans[0] < ans[1]:
#             ans[0] = ans[1]
#         return

#     if ans[0] >= ans[1]*(100**(N-depth)):  # prunning
#         # print(ans, ans[1]*(100**(N-depth)), depth)
#         return

#     for i in range(N):
#         if visited[i] == 0 and lst[depth][i] != 0:
#             visited[i] = 1
#             ans[1] *= lst[depth][i]

#             dfs(depth+1)
#             visited[i] = 0
#             ans[1] //= lst[depth][i]
    


# T = int(input())

# for tc in range(1,T+1):
#     N = int(input())
#     lst = [list(map(int, input().split())) for _ in range(N)]
#     ans = [1, 1]
#     visited = [0]*N
#     memo = [[0] * (1<<N) for _ in range(N)]
#     dfs(0)
#     print(f"#{tc} {(ans[0]/100**(N-1)):.6f}")



def solve(row, used):
    global N, arr, memo, cntt
 
    if row == N:
        return 1
    elif memo[row][used]:
        cntt += 1
        return memo[row][used]
 
    ret = 0
    for col in range(N):
        if used & (1<<col):
            continue
        ret = max(ret, arr[row][col] * solve(row + 1, used | (1<<col)))
    memo[row][used] = ret
    return ret
 
 
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
    cntt = 0
    memo = [[0] * (1 << N) for _ in range(N)]
    print(f"#{tc} {solve(0, 0) * 100:.6f}")
    print(cntt)

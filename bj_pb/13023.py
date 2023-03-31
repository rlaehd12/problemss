def dfs(v, i):  # when i ==5 stop, v== current vertex
    if i == 4:
        print(1)
        exit()
    else:
        # print(v)
        for n in lst[v]:  # n == next vertex
            if visited[n] == 1:
                continue
            if v in lst[n]:  # 다음 vertex에 v가 있어야만 갈 수 있음
                visited[n] = 1
                dfs(n, i+1)
                visited[n] = 0  # 원상복귀



lst = [[] for _ in range(2010)]

N, M = map(int, input().split())
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

for v in range(N+1):
    if lst[v]:  # 있으면 dfs 돌리기
        visited = [0]*2010
        visited[v] = 1
        dfs(v, 0)

print(0)
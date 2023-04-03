from collections import deque

def comb(n, r):
    global ans
    if r == 0:
        visited = [0]*(N+1)  # bfs 방문 초기화
        visited[0] = 1
        tmpp = list(set(cities)-set(tmp))  # 차집합
        bfs(tmpp, visited)
        bfs(tmp, visited)
        if 0 in visited:  # 구역 생성 못하면 끝냄
            return
        else:
            sum1 = 0
            sum2 = 0
            for i in tmp: sum1 += lst[i]
            for i in tmpp: sum2 += lst[i]
            if ans > abs(sum1-sum2):
                ans = abs(sum1-sum2)
                
    elif n < r:
        return
    else:
        tmp[r-1] = cities[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


def bfs(temp, visited):
    # print(temp)
    q = deque()
    q.append(temp[0])
    visited[temp[0]] = 1
    while q:
        cur = q.popleft()
        # print(cur)
        for nxt in edges[cur]:
            if (nxt in temp) and visited[nxt] == 0:
                visited[nxt] = 1
                q.append(nxt)
    # print('end')



N = int(input())
lst = [0] + list(map(int, input().split()))  # 노드 인구수 표시
edges = [[] for _ in range(N+1)]  # 노드와 연결된 노드 표시, 연결리스트
for i in range(1, N+1):
    a, *b = list(map(int, input().split()))
    edges[i] = b
# print(edges)

cities = [i for i in range(1,N+1)]
ans = 9999  # global ans
for i in range(1, N//2 + 1):
    tmp = [0]*i  # 조합용
    comb(N, i)  # 조합
if ans == 9999:
    print(-1)
else: print(ans)

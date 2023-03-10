
import sys
sys.stdin = open("15900.txt")
from collections import deque

def dfs(s):
    ans = 0
    visit = [0]*(N+1)
    q = deque()
    q.append(s)
    visit[s] = 1
    while q:
        c = q.pop()
        flag = 0  # 확인용
        for n in lst[c]:  # 연결된 간선 전부 확인
            if visit[n] == 0:  # 만약 아직 방문 안했으면 전부 메달음
                q.append(n)
                visit[n] = visit[c]+1
                flag = 1
        if flag == 0:
            ans += (visit[c]-1)
    return ans
        
# def bfs():
#     ans = 0
#     visit = [0]*(N+1)
#     q = deque()
#     q.append(1)
#     visit[1] = 1
#     while q:
#         c = q.popleft()

#         flag = 0
#         for n in lst[c]:  # 연결된 간선 전부 확인
#             if visit[n] == 0:  # 만약 아직 방문 안했으면 전부 메달음
#                 q.append(n)
#                 visit[n] = visit[c]+1
#                 flag = 1
#         if flag == 0:
#             ans += (visit[c]-1)

#     return ans

N = int(input())
lst = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

ans = dfs(1)
# print(ans)
if ans %2 == 0:
    print("No")
else:
    print("Yes")




# from collections import deque

# N = int(input())
# graph = [[0] * (N + 1) for _ in range(N + 1)]
# visited = [0] * (N + 1)
# for _ in range(N-1):
#     ni, nj = map(int, input().split())
#     graph[ni][nj] = 1
#     graph[nj][ni] = 1
# routes = 0
# queue = deque()
# queue.append(1)
# visited[1] = 1
# while queue:
#     cur = queue.popleft()
#     leaf_val = 0
#     for w in range(1, N+1):
#         if not visited[w] and graph[cur][w]:
#             visited[w] = visited[cur] + 1
#             queue.append(w)
#         else:
#             leaf_val += 1
#     if leaf_val == N:
#         routes += (visited[cur] - 1)

# print(routes)

# if routes % 2:
#     print("Yes")
# else:
#     print("No")
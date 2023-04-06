import sys
sys.stdin = open("1854.txt")

# 1~n의 정점이 존재할 경우의 최단경로
import heapq # 우선순위 queue를 활용하여 가중치가 작은 값부터 계산

n, m, k = map(int, input().split())
graph = {i : dict() for i in range(1, n+1)}

for _ in range(m):
    a, b, c = map(int, input().split())
    if b not in graph[a]:
        graph[a][b] = c
    if graph[a][b] > c:
        graph[a][b] = c
print(graph)
path = [[] for _ in range(n+1)]

def dijkstra(graph, start):
    path[start].append(0)
    queue = []
    heapq.heappush(queue, (0, start)) # queue에 heapq를 이용하여 (weight, start)를 추가한다.
    while queue:
        now_dist, now = heapq.heappop(queue) # now_dist에 지금위치까지의 가중치, now에 현재 위치를 갱신
        
        for nxt, nxt_dist in graph[now].items(): # now에서 갈 수있는 위치와 weight를 nxt, nxt_dist로 받아준다.
            dist = nxt_dist + now_dist # 현재까지의 거리 + now에서 nxt까지의 weight를 합친 값이
            if len(path[nxt]) == k and path[nxt][-1] >= dist:
                path[nxt].pop()
                path[nxt].append(dist)
                path[nxt].sort()
                heapq.heappush(queue, (dist, nxt)) # 전부 다 추가
            elif len(path[nxt]) < k:
                path[nxt].append(dist)
                path[nxt].sort()
                heapq.heappush(queue, (dist, nxt)) # 전부 다 추가

dijkstra(graph, 1)
for i in path[1:]:
    if len(i) == k:
        print(i[-1])
    else:
        print(-1)
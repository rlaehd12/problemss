import sys
sys.stdin = open("11725.txt")

from collections import deque

def bfs():
    ans = 0
    visit = [0]*(N+1)
    q = deque()
    q.append(1)
    visit[1] = 1
    while q:
        c = q.popleft()
        for n in lst[c]:  # 연결된 간선 전부 확인
            if visit[n] == 0:  # 만약 아직 방문 안했으면 전부 메달음
                q.append(n)
                visit[n] = c
                flag = 1
    for i in visit[2:]:
        print(i)


N = int(input())
lst = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

ans = bfs()
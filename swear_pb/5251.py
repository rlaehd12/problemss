INF = 99999999


def dijkstra(s):

    for i in range(N+1):
        D[i] = adjM[s][i]  # 시작지점 간선 추가
    visited[s] = 1  # 시작지점 확정

    for _ in range(N):  # 시작지점 제외 나머지 결정
        minV = INF
        for i in range(N+1):  # D에서 최소값 찾기
            if D[i] < minV and visited[i] == 0:
                nxt = i
                minV = D[i]
        
        visited[nxt] = 1  # 방문 표시
        # print(visited)

        for i in range(N+1):
            if adjM[nxt][i] != 0 and adjM[nxt][i] != INF:
                D[i] = min(D[i], D[nxt] + adjM[nxt][i])


T = int(input())
for tc in range(1,T+1):
    N, E = map(int, input().split())
    adjM = [[INF]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        adjM[i][i] = 0
    for _ in range(E):
        s, e, w = map(int, input().split())
        adjM[s][e] = w

    # for i in adjM:
    #     print(i)

    D = [0] * (N+1)  # 최소 거리 리스트
    visited = [0] * (N+1)  # 확정 리스트
    dijkstra(0)
    print(f'#{tc} {D[N]}')
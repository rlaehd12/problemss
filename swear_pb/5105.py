import sys
sys.stdin = open("5105.txt")

di = (1,-1,0,0)
dj = (0,0,1,-1)


def find_start(n):  # 시작지점 찾기
    for i in range(n):
        for j in range(n):
            if lst[i+1][j+1] == '2':
                return (i+1,j+1)


def BFS(n):  # 그냥 bfs 구현한거
    visited = [[0]*(n+2) for _ in range(n+2)]  # 방문 확인용 리스트 생성
    s = find_start(n)
    queue = [s]
    while queue:
        cur = queue.pop(0)
        for i in range(4):
            ni = cur[0] + di[i]
            nj = cur[1] + dj[i]
            if lst[ni][nj] == '0' and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = visited[cur[0]][cur[1]] + 1
            elif lst[ni][nj]  == '3':
                visited[ni][nj] = visited[cur[0]][cur[1]] + 1
                return visited[ni][nj] - 1
    return 0


t = int(input())

for tc in range(1,t+1):
    n = int(input())

    lst = [list(map(int, input())) for _ in range(n)]
    print(lst)

    # lst = ['1'*(n+2) for _ in range(n+2)]  # padding
    # for i in range(n):
    #     lst[i+1] = '1' + input() + '1'
    
    # print(f'#{tc} {BFS(n)}')
import sys
sys.stdin = open("1226.txt")

di = (1,-1,0,0)
dj = (0,0,1,-1)

def find_start():  # 시작지점 찾기
    for i in range(16):
        for j in range(16):
            if lst[i][j] == '2':
                return (i,j)

def BFS():  # 그냥 bfs 구현한거
    visited = [[0]*16 for _ in range(16)]  # 방문 확인용 리스트 생성
    s = find_start()
    queue = [s]
    while queue:
        cur = queue.pop(0)
        for i in range(4):
            ni = cur[0] + di[i]
            nj = cur[1] + dj[i]
            if lst[ni][nj] == '0' and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = 1
            elif lst[ni][nj]  == '3':
                return 1
    return 0

for tc in range(1,11):
    t = int(input())

    lst = []
    for _ in range(16):
        lst.append(input())
    
    print(f'#{tc} {BFS()}')
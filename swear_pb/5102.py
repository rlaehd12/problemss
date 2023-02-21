import sys
sys.stdin = open("5102.txt")


def BFS(s, g):  # 그냥 bfs 구현한거

    visited = [0] * (v+1)
    queue = [s]
    visited[s] = 1
    while queue:
        cur = queue.pop(0)
        for i in lst[cur]:
            if visited[i] == 0 and i != g:  # 아직 방문 안했다면
                queue.append(i)
                visited[i] = visited[cur] + 1
            elif i == g:
                visited[i] = visited[cur] + 1
                return visited[i] - 1
    return 0


t = int(input())

for tc in range(1,t+1):

    v, e = map(int, input().split())
    input_lst = []
    for _ in range(e):
        input_lst.append(tuple(map(int, input().split())))
    s, g = map(int, input().split())
    
    lst = [[] for _ in range(v+1)]

    for i in input_lst:
        lst[i[0]].append(i[1])
        lst[i[1]].append(i[0])
    
    print(f'#{tc} {BFS(s, g)}')

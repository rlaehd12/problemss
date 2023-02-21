import sys
sys.stdin = open("1238.txt")

def BFS(s):  # 그냥 bfs 구현한거
    queue = [s]
    visit_dit[s] = 1
    while queue:
        cur = queue.pop(0)
        for i in dit[cur]:
            if visit_dit[i] == 0:  # 아직 방문 안했다면
                queue.append(i)
                visit_dit[i] = visit_dit[cur] + 1



for tc in range(1,11):

    e, s = map(int, input().split())
    input_lst = list(map(int, input().split()))
    insert_set = set(input_lst)
    
    dit = {}  # edge 표시한 딕셔너리
    visit_dit = {}  # 방문 표시할 딕셔너리

    for i in insert_set:  # 딕셔너리 초기화
        dit[i] = []
        visit_dit[i] = 0

    for i in range(e//2):  # edge 매달기
        dit[input_lst[2*i]].append(input_lst[2*i+1])

    BFS(s)
    big = 0
    ans = 0

    for i in visit_dit:  # 거리 확인하려구 딕셔너리 순회
        if visit_dit[i] > big:
            big = visit_dit[i]
            ans = i
        elif visit_dit[i] == big:
            if ans < i:
                ans = i

    print(f'#{tc} {ans}')

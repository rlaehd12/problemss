import sys
sys.stdin = open("1267.txt")

# 문제 몬가 이상함 없는거 있음
# 잘못 이해함 전부 연결되야만 앞으로 갈 수 있음
def find_start(lst, start):
    for edge in lst:
        if start[0] == edge[1]:
            return find_start(lst, edge)
    else:
        return start


for test_case in range(1, 11):
    v, e = map(int, input().split())
    lstt = list(map(int, input().split()))

    counting = [0] * (v+1)
    for i in lstt:
        counting[i] += 1

    ans = []

    for i in range(v):
        if counting[i+1] == 0:
            ans.append(i+1)



    lst = [[] for _ in range(e)]  # 헷갈려서 2차원으로 만듬

    for i in range(2 * e):
        lst[i // 2].append(lstt[i])

    visited = [0] * (v + 1)  # vertices 수 + 1만큼 생성, idx헷갈려

    # 최상위 찾은다음 시작해야할듯 모두의 최상위 찾고 set에다 넣은다음 거기서부터 시작
    start_set = set()
    for i in lst:
        start_set.add(find_start(lst, i)[0])
    # print(start_set)


    cur_stack = []
    for st in start_set:  # 시작점 전부 돌면서, st = 시작점 정점
        ans.append(st)
        visited[st] = 1
        for startt in lst:
            if startt[0] == st:  # 길에서 시작점 같은거 찾기
                cur_stack.append(startt)
                if startt[1] not in ans:
                    ans.append(startt[1])
                visited[startt[1]] = 1

                while 0 in visited[1:]:  # 아직 방문 안한곳 있으면
                    for edge in lst:
                        if visited[edge[1]] == 0 and (cur_stack[-1][1] == edge[0]):  # 행선지 아직 방문 안했으면
                            cur_stack.append(edge)
                            ans.append(edge[1])
                            visited[edge[1]] = 1
                            break
                    else:
                        cur_stack.pop(-1)

                    if not cur_stack:  # 비어버림
                        break


    print(f'#{test_case}', end=' ')
    for i in ans:
        print(i, end=' ')
    print()
    print(len(ans), len(set(ans)))  # 중복이 있슴??
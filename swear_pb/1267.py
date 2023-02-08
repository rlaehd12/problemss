import sys
sys.stdin = open("1267.txt")


def find_start(lst, start):
    for edge in lst:
        if start[0] == edge[1]:
            return find_start(lst, edge)
    else:
        return start


for test_case in range(1, 11):
    v, e = map(int, input().split())
    lstt = list(map(int, input().split()))

    lst = [[] for _ in range(e)]  # 헷갈려서 2차원으로 만듬

    for i in range(2 * e):
        lst[i // 2].append(lstt[i])

    visited = [0] * (v + 1)  # vertices 수 + 1만큼 생성, idx헷갈려

    # 최상위 찾은다음 시작해야할듯 모두의 최상위 찾고 set에다 넣은다음 거기서부터 시작
    start_set = set()
    for i in lst:
        start_set.add(find_start(lst, i)[0])
    print(start_set)
'''

    while 0 in visited[1:]:
        for edge in lst[1:]:
            if visited[edge[1]] == 0 and (cur_stack[-1][1] == edge[0]):  # 행선지 아직 방문 안했으면
                cur_stack.append(edge)
                ans.append(edge[1])
                visited[edge[1]] = 1
                break
        else:
            cur_stack.pop(-1)

        if not cur_stack:  # 비어버림
            for edge in lst[1:]:
                if visited[edge[0]] == 0 and visited[edge[1]] == 0:
                    cur_stack.append(edge)
                    ans.append(edge[0])
                    ans.append(edge[1])
                    visited[edge[0]] = 1
                    visited[edge[1]] = 1
                    break
            else:
                if visited[edge[0]] == 0:
                    ans.append(edge[0])
                    visited[edge[0]] = 1

    print(ans)
    '''
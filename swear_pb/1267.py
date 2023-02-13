import sys
sys.stdin = open("1267.txt")

for tc in range(1,11):
    v, e = map(int, input().split())
    lstt = list(map(int, input().split()))

    lst = [[] for _ in range(e)]  # 헷갈려서 2차원으로 만듬

    for i in range(2 * e):
        lst[i // 2].append(lstt[i])
    
    # 리스트에 없으면 상위 작업 없음
    link_edge = [[] for _ in range(v+1)]  # 0~v+1개 생성, 그니까 1번정점은 1번 인덱스, 헷갈려서 하나 추가
    for edge in lst:
        link_edge[edge[1]].append(edge[0])
    
    ans = []  # 정답 리스트
    now = 0
    while len(ans) < v+1:
        for i in range(v+1):  # 연결된곳 없고, 정답에도 없으면 정답에 매달음
            if not link_edge[i] and (i not in ans):
                ans.append(i)
        
        for i in ans[now:]:  # ans에 있는 값 가지고 있으면 삭제 / 이미 작업했으니까
            for j in link_edge:
                if i in j:
                    j.remove(i)
        now = len(ans)

    ans.remove(0)
    print(f'#{tc}', end=' ')
    for i in ans:
        print(i, end=' ')
    print()


# # 문제 몬가 이상함 없는거 있음
# # 잘못 이해함 전부 연결되야만 앞으로 갈 수 있음
# def find_start(lst, start):
#     for edge in lst:
#         if start[0] == edge[1]:
#             return find_start(lst, edge)
#     else:
#         return start


# for test_case in range(1, 11):
#     v, e = map(int, input().split())
#     lstt = list(map(int, input().split()))

#     counting = [0] * (v+1)
#     for i in lstt:
#         counting[i] += 1

#     ans = []

#     for i in range(v):  # 도로 연결되지 않은 정점이면 그냥 답에 추가
#         if counting[i+1] == 0:
#             ans.append(i+1)



#     lst = [[] for _ in range(e)]  # 헷갈려서 2차원으로 만듬

#     for i in range(2 * e):
#         lst[i // 2].append(lstt[i])

#     visited = [0] * (v + 1)  # vertices 수 + 1만큼 생성, idx헷갈려

#     # 최상위 찾은다음 시작해야할듯 모두의 최상위 찾고 set에다 넣은다음 거기서부터 시작
#     start_set = set()
#     for i in lst:
#         start_set.add(find_start(lst, i)[0])
#     # print(start_set)


#     cur_stack = []
#     for st in start_set:  # 시작점 전부 돌면서, st = 시작점 정점
#         ans.append(st)
#         visited[st] = 1
#         for startt in lst:
#             if startt[0] == st:  # 길에서 시작점 같은거 찾기
#                 cur_stack.append(startt)
#                 if startt[1] not in ans:
#                     ans.append(startt[1])
#                 visited[startt[1]] = 1

#                 while 0 in visited[1:]:  # 아직 방문 안한곳 있으면
#                     for edge in lst:
#                         if visited[edge[1]] == 0 and (cur_stack[-1][1] == edge[0]):  # 행선지 아직 방문 안했으면
#                             cur_stack.append(edge)
#                             ans.append(edge[1])
#                             visited[edge[1]] = 1
#                             break
#                     else:
#                         cur_stack.pop(-1)

#                     if not cur_stack:  # 비어버림
#                         break


#     print(f'#{test_case}', end=' ')
#     for i in ans:
#         print(i, end=' ')
#     print()
#     print(len(ans), len(set(ans)))  # 중복이 있슴??
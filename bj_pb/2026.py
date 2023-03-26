K, N, F = map(int, input().split())
lst = [[] for i in range(N+1)]
for _ in range(F):
    a,b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

# dfs 돌림
# 이전 방문한 노드를 가지고 있으면 계속 검사
# 아니면 되돌리기?


# =========================아닌듯
# for i in range(1, N+1):
#     if len(lst[i]) >= K:
#         cnt = 1
#         not_in_set = set()
#         cur_set = set(lst[i])
#         for chk in lst[i]:  # 각 노드에 대해서 검사
#             if chk != i:  # 일단 자기 자신 아니고
#                 chk_set = set(lst[chk])
#                 if len(cur_set.intersection(chk_set)) >= K:  # 교집합 검사
#                     ex = cur_set-chk_set
#                     for e in ex:
#                         not_in_set.add(e)
#                     cnt += 1
#         if cnt >= K:
#             lst[i].sort()
#             num = 0
#             for p in lst[i]:
#                 if p in not_in_set or num >K:
#                     continue
#                 else:
#                     print(p)
#                     num += 1
#             break
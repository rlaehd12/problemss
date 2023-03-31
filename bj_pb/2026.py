def dfs(v, i):
    if end[0] == 1:
        return

    if i == K:  # 이거 들어오면 끝
        for a in ans:
            print(a)
            end[0] = 1
    else:
        for p in range(v+1, N+1):  # v+1부터 시작 안하면 시간초과
            for chk in range(1,N+1):  
                if visited[chk] == 1:  # 다음으로 갈려면 현재 방문한 모든 정점 방문할수 있는 점이어야 함
                    if chk in lst[p]:
                        continue
                    else:
                        break
            else:  # 갈수 있으면 더 들어감
                if visited[p] == 1:
                    continue
                visited[p] = 1
                ans.append(p)
                dfs(p, i+1)
                visited[p] = 0
                ans.pop()

K, N, F = map(int, input().split())
lst = [[] for i in range(N+1)]
for _ in range(F):
    a,b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

# print(lst)
end = [0]
for v in range(1, N+1):
    visited = [0]*(N+1)  # 초기화
    visited[v] = 1
    ans = [v]
    dfs(v, 1)

if end[0] == 0:
    print(-1)

# dfs 돌림
# 이전 방문한 노드를 가지고 있으면 계속 검사
# 아니면 되돌리기?

# =============================================== 다른 빠른 풀이
# import sys
# input = sys.stdin.readline


# def checking(group, new_member):
#     for x in group:
#         if not relation[x][new_member]:
#             return False
#     return True


# def backtracking(idx, group):
#     global ans, finish
#     if finish:
#         return
    
#     if len(group) == k:
#         ans = group.copy()
#         finish = True
#         return
#     if idx == n:
#         return
    
#     for i in range(idx+1, n):
#         if not visited[i] and checking(group, i):
#             group.append(i)
#             backtracking(i, group)
#             group.pop()
            

# k, n, f = map(int, input().split())
# relation = [[0]*n for _ in range(n)]
# for _ in range(f):
#     a, b = map(lambda x:int(x)-1, input().split())
#     relation[a][b] = relation[b][a] = 1
# for i in range(n):
#     relation[i][i] = 1



# visited = [False] * n
# for x in range(n):
#     if sum(relation[x]) < k:
#         visited[x] = True
        
# ans, finish = [-2], False
# backtracking(-1, [])
# print('\n'.join(map(lambda x:str(x+1), ans)))           


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
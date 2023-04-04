# def find(x):
#     if x != rep[x]:
#         rep[x] = find(rep[x])
#     return rep[x]

# def union(x, y):
#     x = find(x)
#     y = find(y)
#     if x < y:
#         rep[y] = rep[x]
#     else:
#         rep[x] = rep[y]


# T = int(input())

# for tc in range(1,T+1):
#     N, M = map(int, input().split())
#     lst = list(map(int, input().split()))

#     rep = [i for i in range(N+1)]  # 대표자 생성
#     for i in range(M):
#         a = lst[i*2]
#         b = lst[i*2 + 1]
#         union(a, b)
#     cnt_set = set()
#     for i in range(1,N+1):
#         cnt_set.add(find(i))
#     print(f'#{tc} {len(cnt_set)}')

def find_set(node):
    if lst[node] == node:
        return node
    return find_set(lst[node])
 
def union(parent, child):
    lst[find_set(child)] = lst[find_set(parent)]
 
for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    lst = [i for i in range(N+1)]
    queue = list(map(int, input().split()))
    for i in range(M):
        union(queue[2*i], queue[2*i+1])
    result = 0
    for i in range(1, N+1):  # 자기 자신 가르키면 집합 하나임
        if lst[i] == i:
            result += 1
    print(lst)
    print(f'#{tc} {result}')


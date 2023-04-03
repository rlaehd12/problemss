def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    x = find(a)
    y = find(b)
    if x < y:
        parent[y] = parent[x]
    else:
        parent[x] = parent[y]

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])
parent = [i for i in range(N+1)]
cnt = 0
flag = 0
for v1, v2, w in edges:
    # print(v1, v2, w, end=' ')
    if find(v1) != find(v2):
        union(v1, v2)
        union(v1, v2)
        cnt += w
        flag = w
    # print(parent)
print(cnt-flag)

print(1<<10)
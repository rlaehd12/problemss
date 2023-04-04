def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        p[y] = p[x]
    else:
        p[x] = p[y]

def find(x):
    while x != p[x]:
        x = p[x]
    return p[x]


V, E = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(E)]
lst.sort(key=lambda x: x[2])
p = [i for i in range(V+1)]
ans = 0
cnt = 0
for x, y, w in lst:
    if find(x) != find(y):
        cnt += 1
        ans += w
        union(x, y)
        if cnt == V-1:
            break
print(ans)
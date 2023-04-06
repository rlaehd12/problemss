N = int(input())
lst = list(map(int, input().split())) + [0, 0]
# print(lst)

ans = 0
for i in range(N):
    if lst[i] == 0:
        continue
    # 반례
    if lst[i+1] > lst[i+2]:
        cur = lst[i+1]-lst[i+2] if lst[i] > lst[i+1]-lst[i+2] else lst[i]
        lst[i] -= cur
        lst[i+1] -= cur
        ans += 5*cur
    # [3]
    a = min(lst[i], lst[i+1], lst[i+2])
    if a != 0:
        lst[i] -= a
        lst[i+1] -= a
        lst[i+2] -= a
        ans += 7*a
    # [2]
    b = min(lst[i], lst[i+1])
    if b != 0:
        lst[i] -= b
        lst[i+1] -= b
        ans += 5*b

    # [1]
    ans += lst[i]*3
    lst[i] = 0


print(ans)
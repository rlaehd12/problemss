N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

ans = [0, 0, 0]

for i in range(1,N):
    lst[i][0] += min(lst[i-1][1], lst[i-1][2])
    lst[i][1] += min(lst[i-1][0], lst[i-1][2])
    lst[i][2] += min(lst[i-1][1], lst[i-1][0])

print(min(lst[i][0], lst[i][1], lst[i][2]))
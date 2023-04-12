N = int(input())
lst = list(map(int, input().split()))
dp = [9999]* len(lst)
dp[0] = 0
for i in range(1, len(lst)):
    for j in range(0, i):
        if i <= j+lst[j]:
            dp[i] = min(dp[i], dp[j]+1)

if dp[N-1] == 9999: print(-1)
else: print(dp[N-1])


'''
10
1 2 0 1 3 2 1 5 4 2
'''
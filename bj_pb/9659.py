N = int(input())

# dp = [0] * 1000000000000
# dp[1] = 1
# dp[2] = 0
# dp[3] = 1
# dp[4] = 0

# for i in range(5,N):
#     if dp[i-1] == 0 and dp[i-3] == 0:
#         dp[i] = 1
#     else:
#         dp[i] = 0

# if dp[N]:
#     print('CY')
# else:
#     print('SK')

if N%2:
    print('CY')
else:
    print('SK')
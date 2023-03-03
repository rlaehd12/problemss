def solution(n, money):
    dp = [1]+[0]*(n)
    for coin in money:
        for i in range(coin,n+1):
            dp[i] += dp[i-coin]
    print(dp)
    return

solution(122, [1,3,5])
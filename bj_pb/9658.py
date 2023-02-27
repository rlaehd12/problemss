## 가져가면 짐 1,3,4

n = int(input())

dp = [0,1,0,1,0,0]

i = 6
while i <= n:
    if dp[i-1] == 0 and dp[i-3] == 0 and dp[i-4] ==0:
        dp.append(1)
    else:
        dp.append(0)
    
    i+=1

print(dp)

if dp[n] == 1:
    print('CY')
else:
    print('SK')
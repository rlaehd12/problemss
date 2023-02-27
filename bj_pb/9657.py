## 1, 3,4,5,6, 8, 10,11,12,13, 15, 17,18,19,20, 22, 24,25,26,27
## 2를 못줘버리는 수
## 0,2, 7,9, 14,16, 21,23
## 2+ 1,3,4
## 7+ 1,3,4

n = int(input())
# print('CY') if (n%7 == 0 or n%7 == 2) else print('SK')

##############
DP = [0] * 1001
DP[0]=1
DP[1]=0
DP[2]=1
DP[3]=0
DP[4]=0

for i in range(5,n+1):
    DP[i] =  0 if (DP[i-1] or DP[i-3] or DP[i-4]) else 1

print(DP[:n])
print("SK" if DP[n]==0 else "CY")
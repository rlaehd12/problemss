import sys
sys.stdin = open("2805.txt")

t = int(input())

for tc in range(1,t+1):
    n = int(input())
    ############### 다른 풀이, 규칙성
    # arr = [list(map(int, input())) for _ in range(n)]
    # ans = 0
    # m = n//2
    # for i in range(n):
    #     for j in range(abs(m-i), n-abs(m-i)):
    #         ans += arr[i][j]
    ############## 또 다른 풀이, 범위
    arr = [list(map(int, input())) for _ in range(n)]
    ans = 0
    m = n//2
    s = e = m
    for i in range(n):
        for j in range(s,e+1):
            ans += arr[i][j]
        if i<m:
            s-=1
            e+=1
        else:
            s+=1
            e-=1
    ##############
    # lst = []
    # ans = 0
    # for i in range(n):
    #     lst.append(input())
    
    
    # for i in range(n//2):
    #     for numb in lst[i][n//2 - i: n//2 + 1 + i]:
    #         ans += int(numb)

    # for numb in lst[n//2]:
    #     ans += int(numb)

    # for i in range(n-1,n//2,-1):
    #     for numb in lst[i][n//2 - (n-1-i): n//2 + 1 + (n-1-i)]:
    #         ans += int(numb)
    ##############

    print(f'#{tc} {ans}')
    pass
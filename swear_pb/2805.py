import sys
sys.stdin = open("2805.txt")

t = int(input())

for tc in range(1,t+1):
    n = int(input())
    lst = []
    ans = 0
    for i in range(n):
        lst.append(input())
    
    
    for i in range(n//2):
        for numb in lst[i][n//2 - i: n//2 + 1 + i]:
            ans += int(numb)

    for numb in lst[n//2]:
        ans += int(numb)

    for i in range(n-1,n//2,-1):
        for numb in lst[i][n//2 - (n-1-i): n//2 + 1 + (n-1-i)]:
            ans += int(numb)

    print(f'#{tc} {ans}')
    pass
import sys
sys.stdin = open("5431.txt")

t = int(input())

for tc in range(1,1+t):
    n, k = map(int, input().split())  # n 사람, k 제출수
    klst = list(map(int, input().split()))
    submit = [0] * (n+1)

    for i in klst:
        submit[i] = 1
    
    print(f'#{tc}', end=' ')
    for i in range(1,n+1):
        if submit[i] == 0:
            print(i, end=' ')
    print()


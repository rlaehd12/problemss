import sys
sys.stdin = open("1860.txt")


t = int(input())
for tc in range(1,t+1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    eat = 1
    for i in lst:
        if eat > i//M * K:
            print(f'#{tc} Impossible')
            break
        else:
            eat += 1
    else:
        print(f'#{tc} Possible')
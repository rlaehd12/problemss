t = int(input())

for tc in range(1,t+1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    print(f'#{tc} {lst[m%n]}')
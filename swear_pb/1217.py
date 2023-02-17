import sys
sys.stdin = open("1217.txt")

def multi(n, m):
    if m == 1:
        return n
    return n * multi(n, m-1)

for tc in range(1,11):
    t = int(input())
    n, m = map(int, input().split())
    print(f'#{tc} {multi(n, m)}')
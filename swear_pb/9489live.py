import sys
sys.stdin = open("9489.txt")

def count(arr):
    mx = 2
    for lst in arr:
        cnt = 0
        for n in lst:
            if n==1:
                cnt += 1
                if mx < cnt:
                    mx = cnt
            else:
                cnt = 0
    return mx

t = int(input())
for tc in range(1,t+1):
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]
    arr_t = list(map(list, zip(*arr)))

    ans = count(arr)
    t = count(arr_t)

    if ans<t:
        ans = t
    print(f'#{tc} {ans}')
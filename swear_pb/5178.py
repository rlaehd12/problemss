import sys
sys.stdin = open("5178.txt")


def postorder(t):
    if t <= n:  # 범위 안이면
        postorder(2*t)
        postorder(2*t+1)
        # 할거
        if 2*t > n:
            pass
        elif 2*t+1 > n:
            fulltree[t] = fulltree[2*t]
        else:
            fulltree[t] = fulltree[2*t] + fulltree[2*t+1] 

t = int(input())

for tc in range(1,1+t):
    n, m, l = map(int, input().split())
    fulltree = [0] * (n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        fulltree[a] = b

    postorder(1)
    print(f'#{tc} {fulltree[l]}')

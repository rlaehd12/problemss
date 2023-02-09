import sys
sys.stdin = open("6190.txt")

t = int(input())

for tc in range(1,1+t):
    n = int(input())
    alst = input().split()
    blst = []
    for i in range(n-1):
        for j in range(i+1, n):
            blst.append(int(alst[i])*int(alst[j]))
    danzo = []

    blst = list(map(str, blst))

    for numb in blst:
        i = numb[0]
        for j in numb:  # j는 각 자리수
            cur = j
            if int(cur) >= int(i):
                i = cur
                continue
            else:
                break
        else:
            danzo.append(numb)

    danzo = list(map(int, danzo))
    danzo.sort()


    if len(danzo) >= 1:
        print(f'#{tc} {danzo[-1]}')
    elif not danzo:
        print(f'#{tc} {-1}')

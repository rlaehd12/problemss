import sys
sys.stdin = open("5356.txt")

t = int(input())

for tc in range(1,t+1):
    lst = []
    for _ in range(5):
        lst.append(input())

    print(f'#{tc}', end=' ')

    for j in range(15):
        for i in range(5):
            try: print(lst[i][j], end='')
            except: pass
    print()

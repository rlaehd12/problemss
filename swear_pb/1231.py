import sys
sys.stdin = open("1231.txt")


def inorder(t):
    if t != 0:
        inorder(c1[t])
        print(item[t], end='')
        inorder(c2[t])


for tc in range(1,11):
    n = int(input())

    item = [0] * (n+1)  # 아이템, 왼쪽 오른쪽 초기화
    c1 = [0] * (n+1)
    c2 = [0] * (n+1)

    for i in range(n):
        cur = input().split()

        idx = int(cur[0])
        item[idx] = cur[1]

        try: c1[idx] = int(cur[2])
        except: pass
            
        try: c2[idx] = int(cur[3])
        except: pass
    
    print(f'#{tc}', end=' ')
    inorder(1)
    print()
    
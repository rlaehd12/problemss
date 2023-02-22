import sys
sys.stdin = open("5174.txt")

def inorder(t):  # 순회
    if t != 0:
        inorder(c1[t])
        ans[0] += 1
        inorder(c2[t])

t = int(input())
for tc in range(1,t+1):
    e, s = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = [0]  # 정답 리스트

    c1 = [0] * (e+2)
    c2 = [0] * (e+2)

    for i in range(e):
        root = lst[2*i]
        sib = lst[2*i+1]
        if c1[root] == 0:  # 왼쪽 비었으면
            c1[root] = sib
        else:
            c2[root] = sib
    
    inorder(s)
    print(f'#{tc} {ans[0]}')


    

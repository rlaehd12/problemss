import sys
sys.stdin = open("5176.txt")


def inorder(t, n):  # 순회, n은 트리 크기
    if t <= n:  # 트리 벗어나지 않으면
        inorder(2*t, n)  # 왼쪽 자식 노드
        tree_lst[t] = cur[0]
        cur[0] += 1
        inorder(2*t+1, n)  # 오른쪽 자식 노드


t = int(input())
for tc in range(1,t+1):
    n = int(input())
    cur = [1]
    tree_lst = [0] * (n+1)  # 트리 크기만큼 배열 생성

    inorder(1, n)
    print(f'#{tc} {tree_lst[1]} {tree_lst[n//2]}')
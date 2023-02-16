import sys
sys.stdin = open("4880.txt")

t = int(input())

def f(i, j):    # i~j번까지의 승자를 찾는 함수
    if i==j:    # 한 명만 남은 경우
        return i
    else:       # 두 명 이상인 경우 두 그룹의 승자를 찾차 최종 승자를 가림
        left = f(i, (i+j)//2)       # 왼쪽 그룹의 승자
        right = f((i+j)//2+1, j)    # 오른쪽 그룹의 승자
        return win(left, right)     # 두 그룹의 승자를 찾는 함수

def win(l, r):
    if lst[l] == lst[r]:
        return l
    elif lst[l] - lst[r] == 1 or lst[l] - lst[r] == -2:
        return l
    else:
        return r


for tc in range(1,t+1):
    n = int(input())
    lst = list(map(int, input().split()))
    a = f(0, n-1)
    print(f'#{tc} {a+1}')


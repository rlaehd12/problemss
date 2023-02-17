import sys
sys.stdin = open("4881.txt")

t = int(input())

def permu(lst, i, n):
    global small
    if i == n:  # base case
        s= 0
        for i in range(n):
            s += my_lst[i][lst[i]]
        if small > s:  # 더하는데 가장 작은값보다 커지면 중간에 멈춤
            small = s  # 굳이 없어도 될듯
    else:
        for j in range(i, n):
            s = 0
            lst[i], lst[j] = lst[j], lst[i]
            for k in range(i):  # 현재까지 만든 순열 확인
                s += my_lst[k][lst[k]]  # 그 순열 합이 최소값보다 벌써 크면 가지치기함
                if s > small:
                    return
            permu(lst, i+1, n)
            lst[i], lst[j] = lst[j], lst[i]

for tc in range(1,t+1):
    small = 9999999999999999
    n = int(input())
    lst = [i for i in range(n)]
    my_lst = []
    for _ in range(n):
        my_lst.append(list(map(int, input().split())))
    
    permu(lst, 0, n)
    print(f'#{tc} {small}')
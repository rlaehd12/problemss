import sys
sys.stdin = open("1859.txt")

t = int(input())

def find_max(lst):
    pos = lst.index(max(lst))
    local_max = (pos * max(lst)) - sum(lst[:pos])
    return (lst[pos+1:], local_max)

for tc in range(1,t+1):
    n = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    while lst:
        lst, add = find_max(lst)
        cnt += add
    print(f'#{tc} {cnt}')

import sys
sys.stdin = open("4839.txt")

def binary(n, t):  # n 책 쪽 / t 타겟
    l = 1
    r = n
    cnt = 0
    c = 0
    while c != t and l < r:
        cnt += 1
        c = int((l+r)/2)
        if c < t:
            l = c
        else:
            r = c
    return cnt


t = int(input())

for test_case in range(1, t+1):
    print(f'#{test_case}', end=' ')

    p, a, b = map(int, input().split())  # p 책쪽수/ a, b 각자 목표

    ac = binary(p, a)
    bc = binary(p, b)

    if ac > bc:
        print('B')
    elif ac == bc:
        print(0)
    else:
        print('A')
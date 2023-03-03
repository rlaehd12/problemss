import sys
sys.stdin = open("1946.txt")

t = int(input())

for tc in range(1,t+1):
    N = int(input())
    lst = ''

    for _ in range(N):
        cur = list(input().split())
        lst += cur[0]*int(cur[1])
    
    print(f'#{tc}')

    i = 0
    for word in lst:
        print(word, end='')
        i += 1
        if i %10 == 0:
            print()
    print()

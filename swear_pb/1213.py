import sys
sys.stdin = open("1213.txt")


for tc in range(1,11):
    t= int(input())
    b = input()
    a = input()

    cur = 0
    cnt = 0
    for i in range(len(a)-len(b) + 1):  # brute
        if cur > i: 
            continue
        for j in b:
            if a[i] == j:
                i += 1
                continue
            else:
                break
        else:
            cnt += 1
            cur = i
    pass
    print(f'#{tc} {cnt}')
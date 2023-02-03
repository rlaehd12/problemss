import sys
sys.stdin = open("inputbaby.txt")

t = int(input())

for tc in range(1, t + 1):
    c = [0] * 12 # 인덱스 에러 뜰까바
    num = input()
    
    for str_numb in num:
        c[int(str_numb)] += 1
    

    #print(c)

    i = 0
    tri = 0
    while i < 10:
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue
        if (c[i] >= 1) and (c[i+1] >= 1) and (c[i+2] >= 1):
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            tri += 1
            continue
        i += 1
    
    if tri == 2:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')
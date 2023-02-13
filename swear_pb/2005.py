t = int(input())

for tc in range(1, t+1):
    n = int(input())
    lst = [[] for _ in range(n)]

    for i in range(n):
        if i == 0:  # 첫번째는 1
            lst[i].append(1)
            continue
        for j in range(i+1):  
            if j == 0 or j == i:  # 앞, 뒤는 1
                lst[i].append(1)
            else:
                lst[i].append(lst[i-1][j] + lst[i-1][j-1])  # 아니면 위에거 합
    
    print(f'#{tc}')

    for i in lst:
        for j in i:
            print(j, end=' ')
        print()
    pass
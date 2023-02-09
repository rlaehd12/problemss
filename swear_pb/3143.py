

t = int(input())

for tc in range(1,t+1):
    a, b= input().split()

    cur = 0
    cnt = 0
    for i in range(len(a)-len(b) + 1):  # brute
        if cur > i:  # 현재가 i보다 크면 그냥 넘어감
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
    
    print(f'#{tc} {len(a) - len(b) * cnt + cnt}')


